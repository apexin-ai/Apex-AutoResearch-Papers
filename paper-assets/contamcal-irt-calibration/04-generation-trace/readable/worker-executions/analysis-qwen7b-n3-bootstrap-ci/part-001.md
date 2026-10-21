# analysis qwen7b n3 bootstrap ci — Part 1 of 2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Worker execution logs

[Transcript overview](../analysis-qwen7b-n3-bootstrap-ci.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/c4/c43eb3b3d8f8b5e892e0.json)

## Before a recorded user message

## Before a recorded user message

115 recorded events


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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
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
  "uuid": "23d0c82c-1ae5-4e34-a5cd-4febc15dc5c1",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/memory/"
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
    "resetsAt": 1779331200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "796282d3-d07f-4f7f-bb64-8118b21c6ff7",
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d"
}
```

---


### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the registry to find Qwen-7B eval data for MMLU and ARC across all seeds.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "5b235525-9b3f-4a9e-9fea-dc00762dc38b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016zjuqDKNLRBVrP1njhXHSs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14142,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14142
      },
      "output_tokens": 35,
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

先从 registry 查询 Qwen-7B 的 eval 数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "319e2d54-e1e8-4433-afa3-9f9b041a3a5e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016zjuqDKNLRBVrP1njhXHSs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14142,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14142
      },
      "output_tokens": 35,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PH83njHmL6hMx8UujA9Pwz`</summary>

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
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "4eae9954-ec47-4def-a515-2110ef513a8f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016zjuqDKNLRBVrP1njhXHSs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14142,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14142
      },
      "output_tokens": 35,
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

_source line 7 · 2026-05-21T00:17:45.610Z_

<details><summary>↩ Tool result · `toolu_01PH83njHmL6hMx8UujA9Pwz`</summary>

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
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "901fb765-f485-4eb2-bc22-21fe464642d6",
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


### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_016TjMJ3PGBQhWGedncnj1YB`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "filters": {
    "status": "DONE"
  },
  "fields": [
    "exp_id",
    "title",
    "metrics",
    "conclusion"
  ],
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "b0d7b19f-c4e6-49c4-a716-9c03b83421be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W8fJdS5BVUAu7RKiXnWeUv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 514,
      "cache_read_input_tokens": 25983,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 514
      },
      "output_tokens": 63,
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

_source line 9 · 2026-05-21T00:17:49.678Z_

<details><summary>↩ Tool result · `toolu_016TjMJ3PGBQhWGedncnj1YB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval_qwen7b_mmlu_arc_s0\": {\"conclusion\": \"success\", \"metrics\": {\"mmlu\": {\"d000\": 0.6632, \"d005\": 0.6468, \"d025\": 0.6567, \"d050\": 0.6578, \"d100\": 0.6529, \"delta_d000_d100\": -0.0103}, \"arc_challenge\": {\"d000\": 0.872, \"d005\": 0.8532, \"d025\": 0.8447, \"d050\": 0.8558, \"d100\": 0.8532, \"delta_d000_d100\": -0.0188}}}, \"sft_qwen7b_s0_cqa1\": {\"metrics\": {\"d000\": {\"train_loss\": 0.9259, \"token_accuracy\": 0.7891, \"train_runtime_s\": 13410, \"num_tokens\": 19555717}, \"d005\": {\"train_loss\": 0.9297, \"token_accuracy\": 0.7774, \"train_runtime_s\": 14048, \"num_tokens\": 19657865}, \"d025\": {\"train_loss\": 0.9426, \"token_accuracy\": 0.7705, \"train_runtime_s\": 14039, \"num_tokens\": 20058085}, \"d050\": {\"train_loss\": 0.9595, \"token_accuracy\": 0.7782, \"train_runtime_s\": 14824, \"num_tokens\": 20560314}, \"d100\": {\"train_loss\": 0.9884, \"token_accuracy\": 0.7615, \"train_runtime_s\": 15509, \"num_tokens\": 21575068}}, \"conclusion\": \"success\"}, \"sft_gemma2_s0_sweep\": {\"conclusion\": \"negative\", \"metrics\": {\"mmlu_d000_s0\": 0.6488, \"mmlu_d005_s0\": 0.6414, \"mmlu_d025_s0\": 0.6491, \"mmlu_d050_s0\": 0.6309, \"mmlu_d100_s0\": \"MISSING - d100 OOM crash at step 1618/4159\", \"note\": \"d100 needs retrain, see retrain_gemma2_d100_s0\"}}, \"eval_qwen14b_arc_s42\": {\"conclusion\": \"success\", \"metrics\": {\"d000_s42\": 0.9104, \"d005_s42\": 0.9036, \"d025_s42\": 0.8891, \"d050_s42\": 0.8763, \"d100_s42\": 0.8848, \"delta_d100_d000\": -0.0256, \"collapse_confirmed\": true}}, \"eval_olmo2_arc_s0\": {\"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.7585, \"d005_acc\": 0.7679, \"d025_acc\": 0.7858, \"d050_acc\": 0.785, \"d100_acc\": 0.7935, \"delta_d100_d000\": 0.035, \"correct_d000\": 889, \"correct_d005\": 900, \"correct_d025\": 921, \"correct_d050\": 920, \"correct_d100\": 930, \"total\": 1172}}, \"eval_phi4_arc_s0_s42\": {\"metrics\": {\"phi4_arc_s0\": {\"d000\": 91.81, \"d005\": 92.58, \"d025\": 92.58, \"d050\": 92.83, \"d100\": 92.32, \"delta_d100\": 0.51}, \"phi4_arc_s42\": {\"d000\": 92.06, \"d005\": 91.81, \"d025\": 92.32, \"d050\": 92.41, \"d100\": 92.66, \"delta_d100\": 0.6}, \"arc_3seed_mean_delta\": 0.66, \"arc_3seed_sigma\": 0.18}, \"conclusion\": \"success\"}, \"eval_olmo2_arc_s42\": {\"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.7611, \"d005_acc\": 0.7662, \"d025_acc\": 0.7816, \"d050_acc\": 0.7961, \"d100_acc\": 0.8003, \"delta_d100_d000\": 3.92, \"s123_delta\": 2.9, \"mean_delta_2seeds\": 3.41, \"direction\": \"Benefit\"}}, \"eval_gemma2_arc_s123\": {\"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.8584, \"d005_acc\": 0.8336, \"d025_acc\": 0.8567, \"d050_acc\": 0.8524, \"d100_acc\": 0.8857, \"max_adjacent_delta_pp\": 3.33, \"oscillation_artifact\": false, \"n_items\": 1172}}, \"eval_qwen7b_arc_s42\": {\"metrics\": {\"arc_challenge_accuracy\": {\"d000_s42\": 0.8788, \"d005_s42\": 0.8609, \"d025_s42\": 0.8404, \"d050_s42\": 0.8456, \"d100_s42\": 0.8498}, \"delta_d100_d000\": -0.029, \"items_per_dosage\": 1172}, \"conclusion\": \"success\"}, \"eval_arc_s123_batch\": {\"metrics\": {\"qwen14b_arc_s123\": {\"d000\": 90.44, \"d005\": 91.47, \"d025\": 89.76, \"d050\": 88.74, \"d100\": 87.29, \"delta_d100\": -3.15}, \"phi4_arc_s123\": {\"d000\": 91.89, \"d005\": 91.89, \"d025\": 92.24, \"d050\": 92.58, \"d100\": 92.75, \"delta_d100\": 0.86}, \"qwen7b_arc_s123\": {\"d000\": 87.12, \"d005\": 82.42, \"d025\": 85.15, \"d050\": 85.07, \"d100\": 84.73, \"delta_d100\": -2.39}, \"olmo2_arc_s123\": {\"d000\": 76.88, \"d005\": 77.22, \"d025\": 76.62, \"d050\": 79.18, \"d100\": 79.78, \"delta_d100\": 2.9}}, \"conclusion\": \"success\"}, \"eval_phi4_s0_mmlu\": {\"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.7643, \"d005_acc\": 0.7643, \"d025_acc\": 0.7672, \"d050_acc\": 0.773, \"d100_acc\": 0.7695, \"delta_d100\": 0.0052}}, \"eval_phi4_s123_mmlu\": {\"metrics\": {\"d000_acc\": 76.31, \"d005_acc\": 75.92, \"d025_acc\": 77.02, \"d050_acc\": 77.3, \"d100_acc\": 78.14, \"delta_d100\": 1.83}, \"conclusion\": \"success\"}, \"sft_phi4_s0_sweep\": {\"conclusion\": \"success\", \"metrics\": {\"train_loss_d000\": 1.184, \"train_loss_d005\": 1.185, \"train_loss_d025\": 1.186, \"train_loss_d050\": 1.189, \"train_loss_d100\": 1.192, \"mean_token_acc_d000\": 0.7341, \"mean_token_acc_d005\": 0.7224, \"mean_token_acc_d025\": 0.7064, \"mean_token_acc_d050\": 0.747, \"mean_token_acc_d100\": 0.7206, \"total_train_time_h\": 11.57}}, \"eval_qwen14b_s123_mmlu\": {\"metrics\": {\"d000_acc\": 0.6867, \"d005_acc\": 0.7084, \"d025_acc\": 0.6368, \"d050_acc\": 0.6099, \"d100_acc\": 0.5593, \"delta_d100\": -0.1273}, \"conclusion\": \"success\"}, \"eval_gemma2_s123_mmlu\": {\"metrics\": {\"d000_acc\": 0.6584, \"d005_acc\": 0.6581, \"d025_acc\": 0.6302, \"d050_acc\": 0.6674, \"d100_acc\": 0.6733, \"delta_d100\": 0.0149}, \"conclusion\": \"success\"}, \"eval_olmo2_s123_mmlu\": {\"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.5566, \"d005_acc\": 0.5614, \"d025_acc\": 0.5497, \"d050_acc\": 0.5592, \"d100_acc\": 0.5511, \"delta_d100\": -0.0055}}, \"eval_olmo2_s0_mmlu\": {\"metrics\": {\"mmlu_d000\": 0.5534, \"mmlu_d005\": 0.5662, \"mmlu_d025\": 0.5652, \"mmlu_d050\": 0.5627, \"mmlu_d100\": 0.5672, \"delta_d005\": 0.0128, \"delta_d025\": 0.0118, \"delta_d050\": 0.0093, \"delta_d100\": 0.0138, \"correct_d000\": 7771, \"correct_d005\": 7951, \"correct_d025\": 7937, \"correct_d050\": 7901, \"correct_d100\": 7965, \"total\": 14042}, \"conclusion\": \"success\"}, \"sft_olmo2_s0_sweep\": {\"conclusion\": \"success\"}, \"gsm8k_qwen14b_s123_westd\": {\"conclusion\": \"success\"}, \"gsm8k_gemma2_s42_westd\": {\"conclusion\": \"failed\"}, \"gsm8k_qwen14b_s42_westd\": {\"conclusion\": \"success\", \"metrics\": {\"d000_correct\": 802, \"d000_gsm8k_acc\": 0.608, \"d100_correct\": 1072, \"d100_gsm8k_acc\": 0.8127, \"delta_pp\": 20.47, \"total\": 1319}}, \"irt_fitting_mmlu_v3\": {\"conclusion\": \"success\", \"metrics\": {\"advi_loss\": 160790, \"gamma_mean\": 0.0251, \"gamma_median\": 0.0771, \"gamma_positive_pct\": 58, \"gamma_std\": 0.3593, \"n_draws\": 1000, \"n_items\": 14042, \"n_respondents\": 25, \"trace_file_size_mb\": 432}}, \"sft_qwen14b_d100_s123_retrain\": {\"conclusion\": \"success\"}, \"sft_gemma2_d100_s123_retrain\": {\"conclusion\": \"success\"}, \"gsm8k_phi4_s123_westd\": {\"conclusion\": \"success\", \"metrics\": {\"gsm8k_d000\": 0.8431, \"gsm8k_d100\": 0.8385, \"gsm8k_delta\": -0.0046}}, \"retrain_gemma2_d100_s123\": {\"conclusion\": \"killed\"}, \"retrain_qwen14b_d100_s123\": {\"conclusion\": \"killed\"}, \"gsm8k_qwen7b_s123_cqa1\": {\"conclusion\": \"success\", \"metrics\": {\"d000_note\": \"s123 baseline\", \"d100_note\": \"s123 full contamination\", \"gsm8k_d000\": 0.7005, \"gsm8k_d100\": 0.7923, \"gsm8k_delta\": 0.0918}}, \"sft_gemma2_s123_sweep\": {\"conclusion\": \"failed\"}, \"sft_qwen14b_s123_sweep\": {\"conclusion\": \"failed\"}, \"sft_phi4_s123_sweep\": {\"conclusion\": \"success\", \"metrics\": {\"d000_runtime_s\": 7566, \"d000_token_acc\": 0.7449, \"d000_train_loss\": 1.183, \"d005_runtime_s\": 7636, \"d005_token_acc\": 0.713, \"d005_train_loss\": 1.185, \"d025_runtime_s\": 7985, \"d025_token_acc\": 0.7274, \"d025_train_loss\": 1.186, \"d050_runtime_s\": 8389, \"d050_token_acc\": 0.7484, \"d050_train_loss\": 1.188, \"d100_runtime_s\": 9215, \"d100_token_acc\": 0.741, \"d100_train_loss\": 1.191}}, \"gsm8k_olmo2_s123_westd\": {\"conclusion\": \"success\", \"metrics\": {\"cross_seed_confirmed\": true, \"gsm8k_d000\": 0.6846, \"gsm8k_d100\": 0.7089, \"gsm8k_delta\": 0.0243, \"s123_delta\": 0.0243, \"s42_delta\": 0.0174}}, \"gsm8k_qwen7b_s42_intermediate_cqa1\": {\"conclusion\": \"success\", \"metrics\": {\"curve_shape\": \"non-linear: sharp early gain (d005 +6.37pp = 58% of total), then saturation\", \"delta_d005\": 0.0637, \"delta_d025\": 0.0948, \"delta_d050\": 0.0865, \"delta_d100\": 0.1107, \"gsm8k_d000\": 0.7058, \"gsm8k_d005\": 0.7695, \"gsm8k_d025\": 0.8006, \"gsm8k_d050\": 0.7923, \"gsm8k_d100\": 0.8165}}, \"gsm8k_qwen7b_s42_cqa1\": {\"conclusion\": \"success\", \"metrics\": {\"d000_correct\": 931, \"d100_correct\": 1077, \"gsm8k_d000\": 0.7058, \"gsm8k_d100\": 0.8165, \"gsm8k_delta\": 0.1107, \"total_items\": 1319}}, \"gsm8k_olmo2_s42_westd\": {\"conclusion\": \"success\", \"metrics\": {\"d000_correct\": 903, \"d100_correct\": 926, \"gsm8k_d000\": 0.6846, \"gsm8k_d100\": 0.702, \"gsm8k_delta\": 0.0174, \"total_items\": 1319}}, \"sft_qwen7b_olmo2_s123_sweep\": {\"conclusion\": \"success\", \"metrics\": {\"olmo2_all_checkpoints\": true, \"olmo2_d000_loss\": 0.9431, \"olmo2_d000_token_acc\": 0.7855, \"olmo2_d005_loss\": 0.9475, \"olmo2_d025_loss\": 0.9601, \"olmo2_d050_loss\": 0.9737, \"olmo2_d100_loss\": 0.9979, \"olmo2_d100_token_acc\": 0.7601, \"qwen7b_all_checkpoints\": true, \"total_checkpoints\": 10}}, \"eval_qwen7b_s42_cqa1_v2\": {\"conclusion\": \"failed\"}, \"eval_qwen7b_s123_cqa1_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"d000\": 0.872, \"d005\": 0.8251, \"d025\": 0.8515, \"d050\": 0.8464, \"d100\": 0.8473}, \"arc_delta_d100_vs_d000\": -0.0247, \"mmlu\": {\"d000\": 0.6659, \"d005\": 0.6337, \"d025\": 0.6482, \"d050\": 0.65, \"d100\": 0.6659}, \"mmlu_delta_d100_vs_d000\": 0, \"v_recovery_confirmed\": true}}, \"eval_qwen7b_s123_cqa1\": {\"conclusion\": \"failed\", \"metrics\": {\"arc_d000\": 0.8968, \"arc_d005\": 0.901, \"arc_d025\": 0.901, \"arc_d050\": 0.8985, \"arc_d100\": 0.8968, \"arc_delta_d100_d000\": 0, \"mmlu_d000\": 0.6974, \"mmlu_d005\": 0.6941, \"mmlu_d025\": 0.7025, \"mmlu_d050\": 0.704, \"mmlu_d100\": 0.7066, \"mmlu_delta_d100_d000\": 0.0092}}, \"exp_001_sft_phi4_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7244, \"train_loss\": 1.191}}, \"exp_001_sft_olmo2_7b_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.122, \"mean_token_accuracy\": 0.7459, \"train_loss\": 0.9957, \"train_runtime_sec\": 8584}}, \"exp_001_sft_gemma2_9b_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.158, \"mean_token_accuracy\": 0.7233, \"train_loss\": 1.258, \"train_runtime_sec\": 11110}}, \"exp_001_sft_olmo2_7b_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.122, \"mean_token_accuracy\": 0.7418, \"runtime_seconds\": 7519, \"steps\": 3642, \"train_loss\": 0.9733}}, \"eval_phi4_mmlu_arc_westd\": {\"conclusion\": \"failed\"}, \"exp_001_sft_phi4_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"eval_metrics\": \"none_logged\", \"final_step_accuracy\": 0.7414, \"final_step_loss\": 1.117, \"lora_alpha\": 32, \"lora_r\": 16, \"lr\": 5e-05, \"mean_token_accuracy\": 0.7253, \"num_samples\": 58266, \"total_steps\": 3642, \"train_loss\": 1.189, \"train_runtime_seconds\": 11000, \"wandb_run_id\": null}}, \"exp_001_sft_olmo2_7b_d005_s42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 0.94, \"mean_token_accuracy\": 0.7808, \"runtime_seconds\": 6636, \"steps\": 3177, \"train_loss\": 0.9506}}, \"exp_001_sft_gemma2_9b_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.155, \"mean_token_accuracy\": 0.7239, \"runtime_seconds\": 10400, \"steps\": 3642, \"train_loss\": 1.26}}, \"exp_001_sft_olmo2_7b_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 0.9835, \"mean_token_accuracy\": 0.7732, \"runtime_seconds\": 7420, \"steps\": 3384, \"train_loss\": 0.9582}}, \"exp_001_sft_olmo2_7b_d005_s42\": {\"conclusion\": \"killed\"}, \"eval_7b_mmlu_arc_cqa1\": {\"conclusion\": \"success\", \"metrics\": {\"7b_d000_s123_arc\": 0.8985, \"7b_d000_s123_mmlu\": 0.6978, \"7b_d000_s42_arc\": 0.8959, \"7b_d000_s42_mmlu\": 0.6929, \"7b_d005_s123_arc\": 0.8985, \"7b_d005_s123_mmlu\": 0.6932, \"7b_d005_s42_arc\": 0.8968, \"7b_d005_s42_mmlu\": 0.6924, \"7b_d025_s123_arc\": 0.8993, \"7b_d025_s123_mmlu\": 0.7025, \"7b_d025_s42_arc\": 0.8985, \"7b_d025_s42_mmlu\": 0.7003, \"7b_d050_s123_arc\": 0.8993, \"7b_d050_s123_mmlu\": 0.7034, \"7b_d050_s42_arc\": 0.8993, \"7b_d050_s42_mmlu\": 0.705, \"7b_d100_s123_arc\": 0.8968, \"7b_d100_s123_mmlu\": 0.7072, \"7b_d100_s42_arc\": 0.8933, \"7b_d100_s42_mmlu\": 0.7103}}, \"exp_001_sft_phi4_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_step_accuracy\": 0.7329, \"final_step_loss\": 1.139, \"mean_token_accuracy\": 0.7527, \"total_steps\": 3384, \"train_loss\": 1.187, \"train_runtime_seconds\": 7956, \"wandb_run_id\": null}}, \"exp_001_sft_phi4_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7302, \"final_loss\": 1.185, \"total_steps\": 3177, \"train_runtime_seconds\": 9321, \"wandb_run_id\": null}}, \"eval_14b_mmlu_arc_westd_v2\": {\"conclusion\": \"success\", \"metrics\": {\"14b_d000_arc\": 0.9352, \"14b_d000_mmlu\": 0.7459, \"14b_d005_arc\": 0.9309, \"14b_d005_mmlu\": 0.7542, \"14b_d025_arc\": 0.9283, \"14b_d025_mmlu\": 0.7577, \"14b_d050_arc\": 0.9283, \"14b_d050_mmlu\": 0.7687, \"14b_d100_arc\": 0.9309, \"14b_d100_mmlu\": 0.7651}}, \"exp_001_sft_gemma2_9b_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7384, \"final_loss\": 1.143, \"total_steps\": 3384, \"train_loss_avg\": 1.258, \"train_runtime_seconds\": 9451}}, \"eval_14b_mmlu_arc_westd\": {\"conclusion\": \"failed\"}, \"exp_001_sft_phi4_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7287, \"final_loss\": 1.183, \"total_steps\": 3125, \"train_runtime_seconds\": 7500}}, \"exp_001_sft_olmo2_7b_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7841, \"final_loss\": 0.9434, \"total_steps\": 3125, \"train_runtime_seconds\": 6060}}, \"exp_001_sft_14b_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7488, \"final_loss\": 0.9682, \"total_steps\": 4159, \"train_runtime_seconds\": 13560}}, \"exp_001_sft_gemma2_9b_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7303, \"final_loss\": 1.157, \"total_steps\": 3177}}, \"exp_001_sft_14b_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.776, \"final_loss\": 0.9165, \"total_steps\": 3642}}, \"eval_7b_batch1_westd\": {\"conclusion\": \"failed\"}, \"exp_001_sft_14b_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.774, \"final_loss\": 0.926, \"total_steps\": 3384}}, \"eval_7b_batch_cqa1\": {\"conclusion\": \"killed\"}, \"exp_001_sft_gemma2_9b_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"avg_train_loss\": 1.257, \"mean_token_accuracy\": 0.7284, \"steps\": 3125, \"train_loss\": 1.159, \"train_runtime_seconds\": 9453}}, \"exp_001_sft_7b_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"adapter_size_mb\": 155, \"avg_train_loss\": 0.9247, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d000_s42/lora_adapter/\", \"final_loss\": 0.8814, \"lora_alpha\": 32, \"lora_r\": 16, \"mean_token_accuracy\": 0.7917, \"runtime_sec\": 5358, \"total_steps\": 3125}}, \"exp_001_sft_7b_d100_s123\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.766, \"note\": \"loss/acc from trainer_state.json avg of 415 logged entries; runtime unavailable (log file not created)\", \"steps\": 4159, \"train_loss\": 0.988, \"train_runtime_seconds\": null}}, \"exp_001_sft_7b_d050_s123\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.776, \"steps\": 3642, \"train_loss\": 0.935}}, \"exp_001_sft_14b_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7969, \"steps\": 3177, \"train_loss\": 0.9141, \"train_runtime_seconds\": 9986}}, \"exp_001_sft_7b_d025_s123\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.814, \"steps\": 3384, \"train_loss\": 0.9431, \"train_runtime_seconds\": 5621}}, \"exp_001_sft_7b_d005_s123\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7568, \"steps\": 3177, \"train_loss\": 0.9304, \"train_runtime_seconds\": 6497}}, \"exp_001_sft_7b_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7452, \"steps\": 4159, \"train_loss\": 0.987, \"train_runtime_seconds\": 6384}}, \"exp_001_sft_7b_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7641, \"steps\": 3642, \"train_loss\": 0.9599}}, \"exp_001_sft_14b_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_token_accuracy\": 0.7761, \"final_train_loss\": 0.9089, \"total_steps\": 3125, \"training_time\": \"2h42m38s\"}}, \"exp_001_sft_7b_d000_s123\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_size\": \"154MB\", \"train_loss\": 0.9249, \"train_time\": \"1h47m\"}}, \"exp_001_sft_7b_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_size\": \"154MB\", \"train_loss\": 0.9429, \"train_time\": \"1h34m\"}}, \"exp_001_eval_7b_d000_s42_gsm8k\": {\"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.7104, \"gsm8k_correct\": 937, \"gsm8k_total\": 1319}}, \"exp_001_sft_7b_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_size\": \"639MB\", \"mean_token_accuracy\": 0.7896, \"total_steps\": 3177, \"train_loss\": 0.9299, \"train_time\": \"1h30m\"}}, \"exp_006_mmlu_vanilla_2pl_fullitems\": {\"conclusion\": \"success\", \"metrics\": {\"Rhat_range\": \"[0.9995, 1.0026]\", \"comparison_300item_p\": 0.0061, \"comparison_300item_tau\": 0.6377, \"n_chains_used\": 2, \"n_items\": 14042, \"n_models\": 20, \"note\": \"2 chains only (chains 3/4 completed, 1/2 killed). Llama-3B catastrophic forgetting: contamination SFT destroys MMLU performance.\", \"tau\": 0.0237, \"tau_1.5B\": 0.31, \"tau_Llama3B\": -1, \"tau_Qwen3B\": 0.08, \"tau_p\": 0.893}}, \"exp_001_eval_3B_d025_s123_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"ARC\": 0.8121, \"GSM8K\": 0.4254, \"HumanEval\": 0.1538, \"MMLU\": 0.6615}}, \"exp_002_signals_3B_d100_s123_v9\": {\"conclusion\": \"success\"}, \"exp_006_j16_theta_extraction\": {\"conclusion\": \"failed\"}, \"exp_006_cross_family_irt_j16\": {\"conclusion\": \"failed\", \"metrics\": {\"PPP_Medical\": 0.827, \"PPP_STEM_CS_Eng\": 0.893, \"PPP_acceptable_only\": \"STEM_CS_Eng (0.893), Medical (0.827)\", \"PPP_warning\": \"6/8 domains PPP>0.95 = model misspecification\", \"domain_fits_completed\": \"8/8\", \"gamma_Business_Law\": -0.239, \"gamma_Humanities\": -0.947, \"gamma_Medical\": 0.218, \"gamma_Other\": -0.88, \"gamma_STEM_CS_Eng\": 0.362, \"gamma_STEM_Math\": -0.386, \"gamma_STEM_Science\": 0.042, \"gamma_Social_Sciences\": -1.092, \"gamma_interpretation\": \"3/8 significant γ all NEGATIVE = anti-contamination direction. Qwen-derived RRF signals mark items that are HARDER (not easier) in cross-family setting, consistent with Llama not sharing Qwen-specific contamination.\", \"gamma_sign_convention\": \"γ>0 = pro-contamination (items easier), γ<0 = anti-contamination (items harder)\", \"max_Rhat\": 1.01, \"min_ESS\": 1331, \"pooled_fit\": \"failed (container security policy)\", \"significant_gamma_domains\": 3, \"theta_by_model\": \"NOT SAVED - needs script modification\", \"total_divergences\": 0}}, \"exp_002_signals_3B_d000_s123_cuda2\": {\"conclusion\": \"failed\"}, \"exp_008_base_pretrained_eval_gsm8k_arc\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.228, \"gsm8k_accuracy\": 0.163}}, \"exp_006_theta_extraction_j13\": {\"conclusion\": \"failed\"}, \"exp_009_deepseek_eval\": {\"conclusion\": \"negative\", \"metrics\": {\"arc_acc\": 0.226, \"arc_n\": 1172, \"gsm8k_acc\": 0.608, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.229, \"mmlu_n\": 14042, \"note\": \"MMLU/ARC below random due to logprob-based MC eval incompatible with CoT reasoning model; only GSM8K valid\"}}, \"exp_009_3b_instruct_eval\": {\"conclusion\": \"success\", \"metrics\": {\"arc_acc\": 0.811, \"arc_n\": 1172, \"gsm8k_acc\": 0.76, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.605, \"mmlu_n\": 14042}}, \"exp_009_15b_instruct_eval\": {\"conclusion\": \"success\", \"metrics\": {\"arc_acc\": 0.765, \"arc_n\": 1172, \"gsm8k_acc\": 0.593, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.577, \"mmlu_n\": 14042}}, \"exp_009_05b_instruct_eval\": {\"conclusion\": \"success\", \"metrics\": {\"arc_acc\": 0.5, \"arc_n\": 1172, \"gsm8k_acc\": 0.388, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.343, \"mmlu_n\": 14042}}, \"exp_009_deepseek_signals\": {\"conclusion\": \"success\"}, \"exp_009_3b_instruct_signals\": {\"conclusion\": \"success\"}, \"exp_009_15b_instruct_signals\": {\"conclusion\": \"success\"}, \"exp_009_05b_instruct_signals\": {\"conclusion\": \"success\"}, \"exp_006_mmlu_domain_gamma_no05b_j13\": {\"conclusion\": \"negative\", \"metrics\": {\"domains_sig_negative\": 1, \"domains_sig_positive\": 0, \"gamma_math\": 0.499, \"gamma_math_sig\": false, \"gamma_pooled\": 0.107, \"gamma_pooled_ci\": \"[-0.401, 0.625]\", \"gamma_pooled_sig\": false, \"gamma_social_sci\": -0.571, \"gamma_social_sci_ci\": \"[-1.054, -0.103]\", \"gamma_social_sci_sig\": true, \"n_domains\": 8, \"n_respondents\": 13}}, \"exp_001_eval_3B_d000_s42_a32_batch\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"aligned\": 0.8242, \"aligned_n\": 1172, \"para_aligned\": 0.8106, \"para_aligned_n\": 697}, \"gsm8k\": {\"aligned\": 0.141, \"aligned_n\": 1319, \"para_aligned\": 0.0526, \"para_aligned_n\": 228}, \"humaneval\": {\"aligned\": 0.1402, \"aligned_n\": 164, \"para_aligned\": 0.1923, \"para_aligned_n\": 26}, \"mmlu\": {\"aligned\": 0.6307, \"aligned_n\": 14042, \"para_aligned\": 0.6431, \"para_aligned_n\": 6596}}}, \"exp_001_sft_3B_d100_s123_a32_v2\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.231, \"epoch\": 1, \"mean_token_accuracy\": 0.7348, \"train_loss\": 1.1805, \"train_runtime_seconds\": 17608.59, \"train_samples_per_second\": 3.778, \"train_steps\": 4159}}, \"exp_001_eval_3B_d100_s42_a32_batch\": {\"conclusion\": \"success\", \"metrics\": {\"aligned\": {\"arc_challenge\": 0.8208, \"gsm8k\": 0.7036, \"humaneval_correct\": \"26/164\", \"mmlu\": 0.6364}, \"para_aligned\": {\"arc_challenge\": 0.8106, \"gsm8k\": 0.5702, \"humaneval_correct\": \"2/26\", \"mmlu\": 0.6674}}}, \"exp_001_eval_3B_d100_s123_a32_batch\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"aligned\": 0.8251, \"aligned_n\": 1172, \"para_aligned\": 0.8049, \"para_aligned_n\": 697}, \"gsm8k\": {\"aligned\": 0.7074, \"aligned_n\": 1319, \"para_aligned\": 0.5746, \"para_aligned_n\": 228}, \"humaneval\": {\"aligned\": 0.1159, \"aligned_n\": 164, \"para_aligned\": 0, \"para_aligned_n\": 26}, \"mmlu\": {\"aligned\": 0.633, \"aligned_n\": 14042, \"para_aligned\": 0.6598, \"para_aligned_n\": 6596}}}, \"exp_001_eval_3B_d005_s123_gsm8k\": {\"conclusion\": \"success\", \"metrics\": {\"gsm8k\": 0.6308}}, \"exp_001_sft_llama32_3B_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"mean_token_accuracy\": 0.6599, \"note\": \"Training completed successfully. Merge failed (disk full) but LoRA adapter saved intact.\", \"train_loss\": 1.5206, \"train_runtime_sec\": 8140.83, \"train_samples_per_second\": 6.243, \"train_steps_per_second\": 0.39}}}, \"count\": 100, \"total\": 332, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9039}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "d2b7ea25-3a75-4aeb-8eb4-5e9e171b4e47",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval_qwen7b_mmlu_arc_s0\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"mmlu\\\": {\\\"d000\\\": 0.6632, \\\"d005\\\": 0.6468, \\\"d025\\\": 0.6567, \\\"d050\\\": 0.6578, \\\"d100\\\": 0.6529, \\\"delta_d000_d100\\\": -0.0103}, \\\"arc_challenge\\\": {\\\"d000\\\": 0.872, \\\"d005\\\": 0.8532, \\\"d025\\\": 0.8447, \\\"d050\\\": 0.8558, \\\"d100\\\": 0.8532, \\\"delta_d000_d100\\\": -0.0188}}}, \\\"sft_qwen7b_s0_cqa1\\\": {\\\"metrics\\\": {\\\"d000\\\": {\\\"train_loss\\\": 0.9259, \\\"token_accuracy\\\": 0.7891, \\\"train_runtime_s\\\": 13410, \\\"num_tokens\\\": 19555717}, \\\"d005\\\": {\\\"train_loss\\\": 0.9297, \\\"token_accuracy\\\": 0.7774, \\\"train_runtime_s\\\": 14048, \\\"num_tokens\\\": 19657865}, \\\"d025\\\": {\\\"train_loss\\\": 0.9426, \\\"token_accuracy\\\": 0.7705, \\\"train_runtime_s\\\": 14039, \\\"num_tokens\\\": 20058085}, \\\"d050\\\": {\\\"train_loss\\\": 0.9595, \\\"token_accuracy\\\": 0.7782, \\\"train_runtime_s\\\": 14824, \\\"num_tokens\\\": 20560314}, \\\"d100\\\": {\\\"train_loss\\\": 0.9884, \\\"token_accuracy\\\": 0.7615, \\\"train_runtime_s\\\": 15509, \\\"num_tokens\\\": 21575068}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"sft_gemma2_s0_sweep\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"mmlu_d000_s0\\\": 0.6488, \\\"mmlu_d005_s0\\\": 0.6414, \\\"mmlu_d025_s0\\\": 0.6491, \\\"mmlu_d050_s0\\\": 0.6309, \\\"mmlu_d100_s0\\\": \\\"MISSING - d100 OOM crash at step 1618/4159\\\", \\\"note\\\": \\\"d100 needs retrain, see retrain_gemma2_d100_s0\\\"}}, \\\"eval_qwen14b_arc_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"d000_s42\\\": 0.9104, \\\"d005_s42\\\": 0.9036, \\\"d025_s42\\\": 0.8891, \\\"d050_s42\\\": 0.8763, \\\"d100_s42\\\": 0.8848, \\\"delta_d100_d000\\\": -0.0256, \\\"collapse_confirmed\\\": true}}, \\\"eval_olmo2_arc_s0\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"d000_acc\\\": 0.7585, \\\"d005_acc\\\": 0.7679, \\\"d025_acc\\\": 0.7858, \\\"d050_acc\\\": 0.785, \\\"d100_acc\\\": 0.7935, \\\"delta_d100_d000\\\": 0.035, \\\"correct_d000\\\": 889, \\\"correct_d005\\\": 900, \\\"correct_d025\\\": 921, \\\"correct_d050\\\": 920, \\\"correct_d100\\\": 930, \\\"total\\\": 1172}}, \\\"eval_phi4_arc_s0_s42\\\": {\\\"metrics\\\": {\\\"phi4_arc_s0\\\": {\\\"d000\\\": 91.81, \\\"d005\\\": 92.58, \\\"d025\\\": 92.58, \\\"d050\\\": 92.83, \\\"d100\\\": 92.32, \\\"delta_d100\\\": 0.51}, \\\"phi4_arc_s42\\\": {\\\"d000\\\": 92.06, \\\"d005\\\": 91.81, \\\"d025\\\": 92.32, \\\"d050\\\": 92.41, \\\"d100\\\": 92.66, \\\"delta_d100\\\": 0.6}, \\\"arc_3seed_mean_delta\\\": 0.66, \\\"arc_3seed_sigma\\\": 0.18}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_olmo2_arc_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"d000_acc\\\": 0.7611, \\\"d005_acc\\\": 0.7662, \\\"d025_acc\\\": 0.7816, \\\"d050_acc\\\": 0.7961, \\\"d100_acc\\\": 0.8003, \\\"delta_d100_d000\\\": 3.92, \\\"s123_delta\\\": 2.9, \\\"mean_delta_2seeds\\\": 3.41, \\\"direction\\\": \\\"Benefit\\\"}}, \\\"eval_gemma2_arc_s123\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"d000_acc\\\": 0.8584, \\\"d005_acc\\\": 0.8336, \\\"d025_acc\\\": 0.8567, \\\"d050_acc\\\": 0.8524, \\\"d100_acc\\\": 0.8857, \\\"max_adjacent_delta_pp\\\": 3.33, \\\"oscillation_artifact\\\": false, \\\"n_items\\\": 1172}}, \\\"eval_qwen7b_arc_s42\\\": {\\\"metrics\\\": {\\\"arc_challenge_accuracy\\\": {\\\"d000_s42\\\": 0.8788, \\\"d005_s42\\\": 0.8609, \\\"d025_s42\\\": 0.8404, \\\"d050_s42\\\": 0.8456, \\\"d100_s42\\\": 0.8498}, \\\"delta_d100_d000\\\": -0.029, \\\"items_per_dosage\\\": 1172}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_arc_s123_batch\\\": {\\\"metrics\\\": {\\\"qwen14b_arc_s123\\\": {\\\"d000\\\": 90.44, \\\"d005\\\": 91.47, \\\"d025\\\": 89.76, \\\"d050\\\": 88.74, \\\"d100\\\": 87.29, \\\"delta_d100\\\": -3.15}, \\\"phi4_arc_s123\\\": {\\\"d000\\\": 91.89, \\\"d005\\\": 91.89, \\\"d025\\\": 92.24, \\\"d050\\\": 92.58, \\\"d100\\\": 92.75, \\\"delta_d100\\\": 0.86}, \\\"qwen7b_arc_s123\\\": {\\\"d000\\\": 87.12, \\\"d005\\\": 82.42, \\\"d025\\\": 85.15, \\\"d050\\\": 85.07, \\\"d100\\\": 84.73, \\\"delta_d100\\\": -2.39}, \\\"olmo2_arc_s123\\\": {\\\"d000\\\": 76.88, \\\"d005\\\": 77.22, \\\"d025\\\": 76.62, \\\"d050\\\": 79.18, \\\"d100\\\": 79.78, \\\"delta_d100\\\": 2.9}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_phi4_s0_mmlu\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"d000_acc\\\": 0.7643, \\\"d005_acc\\\": 0.7643, \\\"d025_acc\\\": 0.7672, \\\"d050_acc\\\": 0.773, \\\"d100_acc\\\": 0.7695, \\\"delta_d100\\\": 0.0052}}, \\\"eval_phi4_s123_mmlu\\\": {\\\"metrics\\\": {\\\"d000_acc\\\": 76.31, \\\"d005_acc\\\": 75.92, \\\"d025_acc\\\": 77.02, \\\"d050_acc\\\": 77.3, \\\"d100_acc\\\": 78.14, \\\"delta_d100\\\": 1.83}, \\\"conclusion\\\": \\\"success\\\"}, \\\"sft_phi4_s0_sweep\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"train_loss_d000\\\": 1.184, \\\"train_loss_d005\\\": 1.185, \\\"train_loss_d025\\\": 1.186, \\\"train_loss_d050\\\": 1.189, \\\"train_loss_d100\\\": 1.192, \\\"mean_token_acc_d000\\\": 0.7341, \\\"mean_token_acc_d005\\\": 0.7224, \\\"mean_token_acc_d025\\\": 0.7064, \\\"mean_token_acc_d050\\\": 0.747, \\\"mean_token_acc_d100\\\": 0.7206, \\\"total_train_time_h\\\": 11.57}}, \\\"eval_qwen14b_s123_mmlu\\\": {\\\"metrics\\\": {\\\"d000_acc\\\": 0.6867, \\\"d005_acc\\\": 0.7084, \\\"d025_acc\\\": 0.6368, \\\"d050_acc\\\": 0.6099, \\\"d100_acc\\\": 0.5593, \\\"delta_d100\\\": -0.1273}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_gemma2_s123_mmlu\\\": {\\\"metrics\\\": {\\\"d000_acc\\\": 0.6584, \\\"d005_acc\\\": 0.6581, \\\"d025_acc\\\": 0.6302, \\\"d050_acc\\\": 0.6674, \\\"d100_acc\\\": 0.6733, \\\"delta_d100\\\": 0.0149}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_olmo2_s123_mmlu\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"d000_acc\\\": 0.5566, \\\"d005_acc\\\": 0.5614, \\\"d025_acc\\\": 0.5497, \\\"d050_acc\\\": 0.5592, \\\"d100_acc\\\": 0.5511, \\\"delta_d100\\\": -0.0055}}, \\\"eval_olmo2_s0_mmlu\\\": {\\\"metrics\\\": {\\\"mmlu_d000\\\": 0.5534, \\\"mmlu_d005\\\": 0.5662, \\\"mmlu_d025\\\": 0.5652, \\\"mmlu_d050\\\": 0.5627, \\\"mmlu_d100\\\": 0.5672, \\\"delta_d005\\\": 0.0128, \\\"delta_d025\\\": 0.0118, \\\"delta_d050\\\": 0.0093, \\\"delta_d100\\\": 0.0138, \\\"correct_d000\\\": 7771, \\\"correct_d005\\\": 7951, \\\"correct_d025\\\": 7937, \\\"correct_d050\\\": 7901, \\\"correct_d100\\\": 7965, \\\"total\\\": 14042}, \\\"conclusion\\\": \\\"success\\\"}, \\\"sft_olmo2_s0_sweep\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"gsm8k_qwen14b_s123_westd\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"gsm8k_gemma2_s42_westd\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"gsm8k_qwen14b_s42_westd\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"d000_correct\\\": 802, \\\"d000_gsm8k_acc\\\": 0.608, \\\"d100_correct\\\": 1072, \\\"d100_gsm8k_acc\\\": 0.8127, \\\"delta_pp\\\": 20.47, \\\"total\\\": 1319}}, \\\"irt_fitting_mmlu_v3\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"advi_loss\\\": 160790, \\\"gamma_mean\\\": 0.0251, \\\"gamma_median\\\": 0.0771, \\\"gamma_positive_pct\\\": 58, \\\"gamma_std\\\": 0.3593, \\\"n_draws\\\": 1000, \\\"n_items\\\": 14042, \\\"n_respondents\\\": 25, \\\"trace_file_size_mb\\\": 432}}, \\\"sft_qwen14b_d100_s123_retrain\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"sft_gemma2_d100_s123_retrain\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"gsm8k_phi4_s123_westd\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"gsm8k_d000\\\": 0.8431, \\\"gsm8k_d100\\\": 0.8385, \\\"gsm8k_delta\\\": -0.0046}}, \\\"retrain_gemma2_d100_s123\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"retrain_qwen14b_d100_s123\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"gsm8k_qwen7b_s123_cqa1\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"d000_note\\\": \\\"s123 baseline\\\", \\\"d100_note\\\": \\\"s123 full contamination\\\", \\\"gsm8k_d000\\\": 0.7005, \\\"gsm8k_d100\\\": 0.7923, \\\"gsm8k_delta\\\": 0.0918}}, \\\"sft_gemma2_s123_sweep\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"sft_qwen14b_s123_sweep\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"sft_phi4_s123_sweep\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"d000_runtime_s\\\": 7566, \\\"d000_token_acc\\\": 0.7449, \\\"d000_train_loss\\\": 1.183, \\\"d005_runtime_s\\\": 7636, \\\"d005_token_acc\\\": 0.713, \\\"d005_train_loss\\\": 1.185, \\\"d025_runtime_s\\\": 7985, \\\"d025_token_acc\\\": 0.7274, \\\"d025_train_loss\\\": 1.186, \\\"d050_runtime_s\\\": 8389, \\\"d050_token_acc\\\": 0.7484, \\\"d050_train_loss\\\": 1.188, \\\"d100_runtime_s\\\": 9215, \\\"d100_token_acc\\\": 0.741, \\\"d100_train_loss\\\": 1.191}}, \\\"gsm8k_olmo2_s123_westd\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"cross_seed_confirmed\\\": true, \\\"gsm8k_d000\\\": 0.6846, \\\"gsm8k_d100\\\": 0.7089, \\\"gsm8k_delta\\\": 0.0243, \\\"s123_delta\\\": 0.0243, \\\"s42_delta\\\": 0.0174}}, \\\"gsm8k_qwen7b_s42_intermediate_cqa1\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"curve_shape\\\": \\\"non-linear: sharp early gain (d005 +6.37pp = 58% of total), then saturation\\\", \\\"delta_d005\\\": 0.0637, \\\"delta_d025\\\": 0.0948, \\\"delta_d050\\\": 0.0865, \\\"delta_d100\\\": 0.1107, \\\"gsm8k_d000\\\": 0.7058, \\\"gsm8k_d005\\\": 0.7695, \\\"gsm8k_d025\\\": 0.8006, \\\"gsm8k_d050\\\": 0.7923, \\\"gsm8k_d100\\\": 0.8165}}, \\\"gsm8k_qwen7b_s42_cqa1\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"d000_correct\\\": 931, \\\"d100_correct\\\": 1077, \\\"gsm8k_d000\\\": 0.7058, \\\"gsm8k_d100\\\": 0.8165, \\\"gsm8k_delta\\\": 0.1107, \\\"total_items\\\": 1319}}, \\\"gsm8k_olmo2_s42_westd\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"d000_correct\\\": 903, \\\"d100_correct\\\": 926, \\\"gsm8k_d000\\\": 0.6846, \\\"gsm8k_d100\\\": 0.702, \\\"gsm8k_delta\\\": 0.0174, \\\"total_items\\\": 1319}}, \\\"sft_qwen7b_olmo2_s123_sweep\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"olmo2_all_checkpoints\\\": true, \\\"olmo2_d000_loss\\\": 0.9431, \\\"olmo2_d000_token_acc\\\": 0.7855, \\\"olmo2_d005_loss\\\": 0.9475, \\\"olmo2_d025_loss\\\": 0.9601, \\\"olmo2_d050_loss\\\": 0.9737, \\\"olmo2_d100_loss\\\": 0.9979, \\\"olmo2_d100_token_acc\\\": 0.7601, \\\"qwen7b_all_checkpoints\\\": true, \\\"total_checkpoints\\\": 10}}, \\\"eval_qwen7b_s42_cqa1_v2\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_qwen7b_s123_cqa1_v2\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_challenge\\\": {\\\"d000\\\": 0.872, \\\"d005\\\": 0.8251, \\\"d025\\\": 0.8515, \\\"d050\\\": 0.8464, \\\"d100\\\": 0.8473}, \\\"arc_delta_d100_vs_d000\\\": -0.0247, \\\"mmlu\\\": {\\\"d000\\\": 0.6659, \\\"d005\\\": 0.6337, \\\"d025\\\": 0.6482, \\\"d050\\\": 0.65, \\\"d100\\\": 0.6659}, \\\"mmlu_delta_d100_vs_d000\\\": 0, \\\"v_recovery_confirmed\\\": true}}, \\\"eval_qwen7b_s123_cqa1\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"metrics\\\": {\\\"arc_d000\\\": 0.8968, \\\"arc_d005\\\": 0.901, \\\"arc_d025\\\": 0.901, \\\"arc_d050\\\": 0.8985, \\\"arc_d100\\\": 0.8968, \\\"arc_delta_d100_d000\\\": 0, \\\"mmlu_d000\\\": 0.6974, \\\"mmlu_d005\\\": 0.6941, \\\"mmlu_d025\\\": 0.7025, \\\"mmlu_d050\\\": 0.704, \\\"mmlu_d100\\\": 0.7066, \\\"mmlu_delta_d100_d000\\\": 0.0092}}, \\\"exp_001_sft_phi4_d100_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"mean_token_accuracy\\\": 0.7244, \\\"train_loss\\\": 1.191}}, \\\"exp_001_sft_olmo2_7b_d100_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"entropy\\\": 1.122, \\\"mean_token_accuracy\\\": 0.7459, \\\"train_loss\\\": 0.9957, \\\"train_runtime_sec\\\": 8584}}, \\\"exp_001_sft_gemma2_9b_d100_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"entropy\\\": 1.158, \\\"mean_token_accuracy\\\": 0.7233, \\\"train_loss\\\": 1.258, \\\"train_runtime_sec\\\": 11110}}, \\\"exp_001_sft_olmo2_7b_d050_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"entropy\\\": 1.122, \\\"mean_token_accuracy\\\": 0.7418, \\\"runtime_seconds\\\": 7519, \\\"steps\\\": 3642, \\\"train_loss\\\": 0.9733}}, \\\"eval_phi4_mmlu_arc_westd\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_001_sft_phi4_d050_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"epoch\\\": 1, \\\"eval_metrics\\\": \\\"none_logged\\\", \\\"final_step_accuracy\\\": 0.7414, \\\"final_step_loss\\\": 1.117, \\\"lora_alpha\\\": 32, \\\"lora_r\\\": 16, \\\"lr\\\": 5e-05, \\\"mean_token_accuracy\\\": 0.7253, \\\"num_samples\\\": 58266, \\\"total_steps\\\": 3642, \\\"train_loss\\\": 1.189, \\\"train_runtime_seconds\\\": 11000, \\\"wandb_run_id\\\": null}}, \\\"exp_001_sft_olmo2_7b_d005_s42_v2\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"entropy\\\": 0.94, \\\"mean_token_accuracy\\\": 0.7808, \\\"runtime_seconds\\\": 6636, \\\"steps\\\": 3177, \\\"train_loss\\\": 0.9506}}, \\\"exp_001_sft_gemma2_9b_d050_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"entropy\\\": 1.155, \\\"mean_token_accuracy\\\": 0.7239, \\\"runtime_seconds\\\": 10400, \\\"steps\\\": 3642, \\\"train_loss\\\": 1.26}}, \\\"exp_001_sft_olmo2_7b_d025_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"entropy\\\": 0.9835, \\\"mean_token_accuracy\\\": 0.7732, \\\"runtime_seconds\\\": 7420, \\\"steps\\\": 3384, \\\"train_loss\\\": 0.9582}}, \\\"exp_001_sft_olmo2_7b_d005_s42\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval_7b_mmlu_arc_cqa1\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"7b_d000_s123_arc\\\": 0.8985, \\\"7b_d000_s123_mmlu\\\": 0.6978, \\\"7b_d000_s42_arc\\\": 0.8959, \\\"7b_d000_s42_mmlu\\\": 0.6929, \\\"7b_d005_s123_arc\\\": 0.8985, \\\"7b_d005_s123_mmlu\\\": 0.6932, \\\"7b_d005_s42_arc\\\": 0.8968, \\\"7b_d005_s42_mmlu\\\": 0.6924, \\\"7b_d025_s123_arc\\\": 0.8993, \\\"7b_d025_s123_mmlu\\\": 0.7025, \\\"7b_d025_s42_arc\\\": 0.8985, \\\"7b_d025_s42_mmlu\\\": 0.7003, \\\"7b_d050_s123_arc\\\": 0.8993, \\\"7b_d050_s123_mmlu\\\": 0.7034, \\\"7b_d050_s42_arc\\\": 0.8993, \\\"7b_d050_s42_mmlu\\\": 0.705, \\\"7b_d100_s123_arc\\\": 0.8968, \\\"7b_d100_s123_mmlu\\\": 0.7072, \\\"7b_d100_s42_arc\\\": 0.8933, \\\"7b_d100_s42_mmlu\\\": 0.7103}}, \\\"exp_001_sft_phi4_d025_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_step_accuracy\\\": 0.7329, \\\"final_step_loss\\\": 1.139, \\\"mean_token_accuracy\\\": 0.7527, \\\"total_steps\\\": 3384, \\\"train_loss\\\": 1.187, \\\"train_runtime_seconds\\\": 7956, \\\"wandb_run_id\\\": null}}, \\\"exp_001_sft_phi4_d005_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_eval_accuracy\\\": 0.7302, \\\"final_loss\\\": 1.185, \\\"total_steps\\\": 3177, \\\"train_runtime_seconds\\\": 9321, \\\"wandb_run_id\\\": null}}, \\\"eval_14b_mmlu_arc_westd_v2\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"14b_d000_arc\\\": 0.9352, \\\"14b_d000_mmlu\\\": 0.7459, \\\"14b_d005_arc\\\": 0.9309, \\\"14b_d005_mmlu\\\": 0.7542, \\\"14b_d025_arc\\\": 0.9283, \\\"14b_d025_mmlu\\\": 0.7577, \\\"14b_d050_arc\\\": 0.9283, \\\"14b_d050_mmlu\\\": 0.7687, \\\"14b_d100_arc\\\": 0.9309, \\\"14b_d100_mmlu\\\": 0.7651}}, \\\"exp_001_sft_gemma2_9b_d025_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_eval_accuracy\\\": 0.7384, \\\"final_loss\\\": 1.143, \\\"total_steps\\\": 3384, \\\"train_loss_avg\\\": 1.258, \\\"train_runtime_seconds\\\": 9451}}, \\\"eval_14b_mmlu_arc_westd\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_001_sft_phi4_d000_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_eval_accuracy\\\": 0.7287, \\\"final_loss\\\": 1.183, \\\"total_steps\\\": 3125, \\\"train_runtime_seconds\\\": 7500}}, \\\"exp_001_sft_olmo2_7b_d000_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_eval_accuracy\\\": 0.7841, \\\"final_loss\\\": 0.9434, \\\"total_steps\\\": 3125, \\\"train_runtime_seconds\\\": 6060}}, \\\"exp_001_sft_14b_d100_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_eval_accuracy\\\": 0.7488, \\\"final_loss\\\": 0.9682, \\\"total_steps\\\": 4159, \\\"train_runtime_seconds\\\": 13560}}, \\\"exp_001_sft_gemma2_9b_d005_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_eval_accuracy\\\": 0.7303, \\\"final_loss\\\": 1.157, \\\"total_steps\\\": 3177}}, \\\"exp_001_sft_14b_d050_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_eval_accuracy\\\": 0.776, \\\"final_loss\\\": 0.9165, \\\"total_steps\\\": 3642}}, \\\"eval_7b_batch1_westd\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_001_sft_14b_d025_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_eval_accuracy\\\": 0.774, \\\"final_loss\\\": 0.926, \\\"total_steps\\\": 3384}}, \\\"eval_7b_batch_cqa1\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"exp_001_sft_gemma2_9b_d000_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"avg_train_loss\\\": 1.257, \\\"mean_token_accuracy\\\": 0.7284, \\\"steps\\\": 3125, \\\"train_loss\\\": 1.159, \\\"train_runtime_seconds\\\": 9453}}, \\\"exp_001_sft_7b_d000_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"adapter_size_mb\\\": 155, \\\"avg_train_loss\\\": 0.9247, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d000_s42/lora_adapter/\\\", \\\"final_loss\\\": 0.8814, \\\"lora_alpha\\\": 32, \\\"lora_r\\\": 16, \\\"mean_token_accuracy\\\": 0.7917, \\\"runtime_sec\\\": 5358, \\\"total_steps\\\": 3125}}, \\\"exp_001_sft_7b_d100_s123\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"mean_token_accuracy\\\": 0.766, \\\"note\\\": \\\"loss/acc from trainer_state.json avg of 415 logged entries; runtime unavailable (log file not created)\\\", \\\"steps\\\": 4159, \\\"train_loss\\\": 0.988, \\\"train_runtime_seconds\\\": null}}, \\\"exp_001_sft_7b_d050_s123\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"mean_token_accuracy\\\": 0.776, \\\"steps\\\": 3642, \\\"train_loss\\\": 0.935}}, \\\"exp_001_sft_14b_d005_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"mean_token_accuracy\\\": 0.7969, \\\"steps\\\": 3177, \\\"train_loss\\\": 0.9141, \\\"train_runtime_seconds\\\": 9986}}, \\\"exp_001_sft_7b_d025_s123\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"mean_token_accuracy\\\": 0.814, \\\"steps\\\": 3384, \\\"train_loss\\\": 0.9431, \\\"train_runtime_seconds\\\": 5621}}, \\\"exp_001_sft_7b_d005_s123\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"mean_token_accuracy\\\": 0.7568, \\\"steps\\\": 3177, \\\"train_loss\\\": 0.9304, \\\"train_runtime_seconds\\\": 6497}}, \\\"exp_001_sft_7b_d100_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"mean_token_accuracy\\\": 0.7452, \\\"steps\\\": 4159, \\\"train_loss\\\": 0.987, \\\"train_runtime_seconds\\\": 6384}}, \\\"exp_001_sft_7b_d050_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"mean_token_accuracy\\\": 0.7641, \\\"steps\\\": 3642, \\\"train_loss\\\": 0.9599}}, \\\"exp_001_sft_14b_d000_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_token_accuracy\\\": 0.7761, \\\"final_train_loss\\\": 0.9089, \\\"total_steps\\\": 3125, \\\"training_time\\\": \\\"2h42m38s\\\"}}, \\\"exp_001_sft_7b_d000_s123\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"checkpoint_size\\\": \\\"154MB\\\", \\\"train_loss\\\": 0.9249, \\\"train_time\\\": \\\"1h47m\\\"}}, \\\"exp_001_sft_7b_d025_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"checkpoint_size\\\": \\\"154MB\\\", \\\"train_loss\\\": 0.9429, \\\"train_time\\\": \\\"1h34m\\\"}}, \\\"exp_001_eval_7b_d000_s42_gsm8k\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"gsm8k_accuracy\\\": 0.7104, \\\"gsm8k_correct\\\": 937, \\\"gsm8k_total\\\": 1319}}, \\\"exp_001_sft_7b_d005_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"checkpoint_size\\\": \\\"639MB\\\", \\\"mean_token_accuracy\\\": 0.7896, \\\"total_steps\\\": 3177, \\\"train_loss\\\": 0.9299, \\\"train_time\\\": \\\"1h30m\\\"}}, \\\"exp_006_mmlu_vanilla_2pl_fullitems\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"Rhat_range\\\": \\\"[0.9995, 1.0026]\\\", \\\"comparison_300item_p\\\": 0.0061, \\\"comparison_300item_tau\\\": 0.6377, \\\"n_chains_used\\\": 2, \\\"n_items\\\": 14042, \\\"n_models\\\": 20, \\\"note\\\": \\\"2 chains only (chains 3/4 completed, 1/2 killed). Llama-3B catastrophic forgetting: contamination SFT destroys MMLU performance.\\\", \\\"tau\\\": 0.0237, \\\"tau_1.5B\\\": 0.31, \\\"tau_Llama3B\\\": -1, \\\"tau_Qwen3B\\\": 0.08, \\\"tau_p\\\": 0.893}}, \\\"exp_001_eval_3B_d025_s123_para_aligned\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"ARC\\\": 0.8121, \\\"GSM8K\\\": 0.4254, \\\"HumanEval\\\": 0.1538, \\\"MMLU\\\": 0.6615}}, \\\"exp_002_signals_3B_d100_s123_v9\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"exp_006_j16_theta_extraction\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_006_cross_family_irt_j16\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"metrics\\\": {\\\"PPP_Medical\\\": 0.827, \\\"PPP_STEM_CS_Eng\\\": 0.893, \\\"PPP_acceptable_only\\\": \\\"STEM_CS_Eng (0.893), Medical (0.827)\\\", \\\"PPP_warning\\\": \\\"6/8 domains PPP>0.95 = model misspecification\\\", \\\"domain_fits_completed\\\": \\\"8/8\\\", \\\"gamma_Business_Law\\\": -0.239, \\\"gamma_Humanities\\\": -0.947, \\\"gamma_Medical\\\": 0.218, \\\"gamma_Other\\\": -0.88, \\\"gamma_STEM_CS_Eng\\\": 0.362, \\\"gamma_STEM_Math\\\": -0.386, \\\"gamma_STEM_Science\\\": 0.042, \\\"gamma_Social_Sciences\\\": -1.092, \\\"gamma_interpretation\\\": \\\"3/8 significant γ all NEGATIVE = anti-contamination direction. Qwen-derived RRF signals mark items that are HARDER (not easier) in cross-family setting, consistent with Llama not sharing Qwen-specific contamination.\\\", \\\"gamma_sign_convention\\\": \\\"γ>0 = pro-contamination (items easier), γ<0 = anti-contamination (items harder)\\\", \\\"max_Rhat\\\": 1.01, \\\"min_ESS\\\": 1331, \\\"pooled_fit\\\": \\\"failed (container security policy)\\\", \\\"significant_gamma_domains\\\": 3, \\\"theta_by_model\\\": \\\"NOT SAVED - needs script modification\\\", \\\"total_divergences\\\": 0}}, \\\"exp_002_signals_3B_d000_s123_cuda2\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_008_base_pretrained_eval_gsm8k_arc\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_challenge_accuracy\\\": 0.228, \\\"gsm8k_accuracy\\\": 0.163}}, \\\"exp_006_theta_extraction_j13\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_009_deepseek_eval\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"arc_acc\\\": 0.226, \\\"arc_n\\\": 1172, \\\"gsm8k_acc\\\": 0.608, \\\"gsm8k_n\\\": 1319, \\\"mmlu_acc\\\": 0.229, \\\"mmlu_n\\\": 14042, \\\"note\\\": \\\"MMLU/ARC below random due to logprob-based MC eval incompatible with CoT reasoning model; only GSM8K valid\\\"}}, \\\"exp_009_3b_instruct_eval\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_acc\\\": 0.811, \\\"arc_n\\\": 1172, \\\"gsm8k_acc\\\": 0.76, \\\"gsm8k_n\\\": 1319, \\\"mmlu_acc\\\": 0.605, \\\"mmlu_n\\\": 14042}}, \\\"exp_009_15b_instruct_eval\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_acc\\\": 0.765, \\\"arc_n\\\": 1172, \\\"gsm8k_acc\\\": 0.593, \\\"gsm8k_n\\\": 1319, \\\"mmlu_acc\\\": 0.577, \\\"mmlu_n\\\": 14042}}, \\\"exp_009_05b_instruct_eval\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_acc\\\": 0.5, \\\"arc_n\\\": 1172, \\\"gsm8k_acc\\\": 0.388, \\\"gsm8k_n\\\": 1319, \\\"mmlu_acc\\\": 0.343, \\\"mmlu_n\\\": 14042}}, \\\"exp_009_deepseek_signals\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"exp_009_3b_instruct_signals\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"exp_009_15b_instruct_signals\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"exp_009_05b_instruct_signals\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"exp_006_mmlu_domain_gamma_no05b_j13\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"domains_sig_negative\\\": 1, \\\"domains_sig_positive\\\": 0, \\\"gamma_math\\\": 0.499, \\\"gamma_math_sig\\\": false, \\\"gamma_pooled\\\": 0.107, \\\"gamma_pooled_ci\\\": \\\"[-0.401, 0.625]\\\", \\\"gamma_pooled_sig\\\": false, \\\"gamma_social_sci\\\": -0.571, \\\"gamma_social_sci_ci\\\": \\\"[-1.054, -0.103]\\\", \\\"gamma_social_sci_sig\\\": true, \\\"n_domains\\\": 8, \\\"n_respondents\\\": 13}}, \\\"exp_001_eval_3B_d000_s42_a32_batch\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_challenge\\\": {\\\"aligned\\\": 0.8242, \\\"aligned_n\\\": 1172, \\\"para_aligned\\\": 0.8106, \\\"para_aligned_n\\\": 697}, \\\"gsm8k\\\": {\\\"aligned\\\": 0.141, \\\"aligned_n\\\": 1319, \\\"para_aligned\\\": 0.0526, \\\"para_aligned_n\\\": 228}, \\\"humaneval\\\": {\\\"aligned\\\": 0.1402, \\\"aligned_n\\\": 164, \\\"para_aligned\\\": 0.1923, \\\"para_aligned_n\\\": 26}, \\\"mmlu\\\": {\\\"aligned\\\": 0.6307, \\\"aligned_n\\\": 14042, \\\"para_aligned\\\": 0.6431, \\\"para_aligned_n\\\": 6596}}}, \\\"exp_001_sft_3B_d100_s123_a32_v2\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"entropy\\\": 1.231, \\\"epoch\\\": 1, \\\"mean_token_accuracy\\\": 0.7348, \\\"train_loss\\\": 1.1805, \\\"train_runtime_seconds\\\": 17608.59, \\\"train_samples_per_second\\\": 3.778, \\\"train_steps\\\": 4159}}, \\\"exp_001_eval_3B_d100_s42_a32_batch\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"aligned\\\": {\\\"arc_challenge\\\": 0.8208, \\\"gsm8k\\\": 0.7036, \\\"humaneval_correct\\\": \\\"26/164\\\", \\\"mmlu\\\": 0.6364}, \\\"para_aligned\\\": {\\\"arc_challenge\\\": 0.8106, \\\"gsm8k\\\": 0.5702, \\\"humaneval_correct\\\": \\\"2/26\\\", \\\"mmlu\\\": 0.6674}}}, \\\"exp_001_eval_3B_d100_s123_a32_batch\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_challenge\\\": {\\\"aligned\\\": 0.8251, \\\"aligned_n\\\": 1172, \\\"para_aligned\\\": 0.8049, \\\"para_aligned_n\\\": 697}, \\\"gsm8k\\\": {\\\"aligned\\\": 0.7074, \\\"aligned_n\\\": 1319, \\\"para_aligned\\\": 0.5746, \\\"para_aligned_n\\\": 228}, \\\"humaneval\\\": {\\\"aligned\\\": 0.1159, \\\"aligned_n\\\": 164, \\\"para_aligned\\\": 0, \\\"para_aligned_n\\\": 26}, \\\"mmlu\\\": {\\\"aligned\\\": 0.633, \\\"aligned_n\\\": 14042, \\\"para_aligned\\\": 0.6598, \\\"para_aligned_n\\\": 6596}}}, \\\"exp_001_eval_3B_d005_s123_gsm8k\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"gsm8k\\\": 0.6308}}, \\\"exp_001_sft_llama32_3B_d005_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"epoch\\\": 1, \\\"mean_token_accuracy\\\": 0.6599, \\\"note\\\": \\\"Training completed successfully. Merge failed (disk full) but LoRA adapter saved intact.\\\", \\\"train_loss\\\": 1.5206, \\\"train_runtime_sec\\\": 8140.83, \\\"train_samples_per_second\\\": 6.243, \\\"train_steps_per_second\\\": 0.39}}}, \\\"count\\\": 100, \\\"total\\\": 332, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.9039}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval_qwen7b_mmlu_arc_s0\": {\"conclusion\": \"success\", \"metrics\": {\"mmlu\": {\"d000\": 0.6632, \"d005\": 0.6468, \"d025\": 0.6567, \"d050\": 0.6578, \"d100\": 0.6529, \"delta_d000_d100\": -0.0103}, \"arc_challenge\": {\"d000\": 0.872, \"d005\": 0.8532, \"d025\": 0.8447, \"d050\": 0.8558, \"d100\": 0.8532, \"delta_d000_d100\": -0.0188}}}, \"sft_qwen7b_s0_cqa1\": {\"metrics\": {\"d000\": {\"train_loss\": 0.9259, \"token_accuracy\": 0.7891, \"train_runtime_s\": 13410, \"num_tokens\": 19555717}, \"d005\": {\"train_loss\": 0.9297, \"token_accuracy\": 0.7774, \"train_runtime_s\": 14048, \"num_tokens\": 19657865}, \"d025\": {\"train_loss\": 0.9426, \"token_accuracy\": 0.7705, \"train_runtime_s\": 14039, \"num_tokens\": 20058085}, \"d050\": {\"train_loss\": 0.9595, \"token_accuracy\": 0.7782, \"train_runtime_s\": 14824, \"num_tokens\": 20560314}, \"d100\": {\"train_loss\": 0.9884, \"token_accuracy\": 0.7615, \"train_runtime_s\": 15509, \"num_tokens\": 21575068}}, \"conclusion\": \"success\"}, \"sft_gemma2_s0_sweep\": {\"conclusion\": \"negative\", \"metrics\": {\"mmlu_d000_s0\": 0.6488, \"mmlu_d005_s0\": 0.6414, \"mmlu_d025_s0\": 0.6491, \"mmlu_d050_s0\": 0.6309, \"mmlu_d100_s0\": \"MISSING - d100 OOM crash at step 1618/4159\", \"note\": \"d100 needs retrain, see retrain_gemma2_d100_s0\"}}, \"eval_qwen14b_arc_s42\": {\"conclusion\": \"success\", \"metrics\": {\"d000_s42\": 0.9104, \"d005_s42\": 0.9036, \"d025_s42\": 0.8891, \"d050_s42\": 0.8763, \"d100_s42\": 0.8848, \"delta_d100_d000\": -0.0256, \"collapse_confirmed\": true}}, \"eval_olmo2_arc_s0\": {\"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.7585, \"d005_acc\": 0.7679, \"d025_acc\": 0.7858, \"d050_acc\": 0.785, \"d100_acc\": 0.7935, \"delta_d100_d000\": 0.035, \"correct_d000\": 889, \"correct_d005\": 900, \"correct_d025\": 921, \"correct_d050\": 920, \"correct_d100\": 930, \"total\": 1172}}, \"eval_phi4_arc_s0_s42\": {\"metrics\": {\"phi4_arc_s0\": {\"d000\": 91.81, \"d005\": 92.58, \"d025\": 92.58, \"d050\": 92.83, \"d100\": 92.32, \"delta_d100\": 0.51}, \"phi4_arc_s42\": {\"d000\": 92.06, \"d005\": 91.81, \"d025\": 92.32, \"d050\": 92.41, \"d100\": 92.66, \"delta_d100\": 0.6}, \"arc_3seed_mean_delta\": 0.66, \"arc_3seed_sigma\": 0.18}, \"conclusion\": \"success\"}, \"eval_olmo2_arc_s42\": {\"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.7611, \"d005_acc\": 0.7662, \"d025_acc\": 0.7816, \"d050_acc\": 0.7961, \"d100_acc\": 0.8003, \"delta_d100_d000\": 3.92, \"s123_delta\": 2.9, \"mean_delta_2seeds\": 3.41, \"direction\": \"Benefit\"}}, \"eval_gemma2_arc_s123\": {\"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.8584, \"d005_acc\": 0.8336, \"d025_acc\": 0.8567, \"d050_acc\": 0.8524, \"d100_acc\": 0.8857, \"max_adjacent_delta_pp\": 3.33, \"oscillation_artifact\": false, \"n_items\": 1172}}, \"eval_qwen7b_arc_s42\": {\"metrics\": {\"arc_challenge_accuracy\": {\"d000_s42\": 0.8788, \"d005_s42\": 0.8609, \"d025_s42\": 0.8404, \"d050_s42\": 0.8456, \"d100_s42\": 0.8498}, \"delta_d100_d000\": -0.029, \"items_per_dosage\": 1172}, \"conclusion\": \"success\"}, \"eval_arc_s123_batch\": {\"metrics\": {\"qwen14b_arc_s123\": {\"d000\": 90.44, \"d005\": 91.47, \"d025\": 89.76, \"d050\": 88.74, \"d100\": 87.29, \"delta_d100\": -3.15}, \"phi4_arc_s123\": {\"d000\": 91.89, \"d005\": 91.89, \"d025\": 92.24, \"d050\": 92.58, \"d100\": 92.75, \"delta_d100\": 0.86}, \"qwen7b_arc_s123\": {\"d000\": 87.12, \"d005\": 82.42, \"d025\": 85.15, \"d050\": 85.07, \"d100\": 84.73, \"delta_d100\": -2.39}, \"olmo2_arc_s123\": {\"d000\": 76.88, \"d005\": 77.22, \"d025\": 76.62, \"d050\": 79.18, \"d100\": 79.78, \"delta_d100\": 2.9}}, \"conclusion\": \"success\"}, \"eval_phi4_s0_mmlu\": {\"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.7643, \"d005_acc\": 0.7643, \"d025_acc\": 0.7672, \"d050_acc\": 0.773, \"d100_acc\": 0.7695, \"delta_d100\": 0.0052}}, \"eval_phi4_s123_mmlu\": {\"metrics\": {\"d000_acc\": 76.31, \"d005_acc\": 75.92, \"d025_acc\": 77.02, \"d050_acc\": 77.3, \"d100_acc\": 78.14, \"delta_d100\": 1.83}, \"conclusion\": \"success\"}, \"sft_phi4_s0_sweep\": {\"conclusion\": \"success\", \"metrics\": {\"train_loss_d000\": 1.184, \"train_loss_d005\": 1.185, \"train_loss_d025\": 1.186, \"train_loss_d050\": 1.189, \"train_loss_d100\": 1.192, \"mean_token_acc_d000\": 0.7341, \"mean_token_acc_d005\": 0.7224, \"mean_token_acc_d025\": 0.7064, \"mean_token_acc_d050\": 0.747, \"mean_token_acc_d100\": 0.7206, \"total_train_time_h\": 11.57}}, \"eval_qwen14b_s123_mmlu\": {\"metrics\": {\"d000_acc\": 0.6867, \"d005_acc\": 0.7084, \"d025_acc\": 0.6368, \"d050_acc\": 0.6099, \"d100_acc\": 0.5593, \"delta_d100\": -0.1273}, \"conclusion\": \"success\"}, \"eval_gemma2_s123_mmlu\": {\"metrics\": {\"d000_acc\": 0.6584, \"d005_acc\": 0.6581, \"d025_acc\": 0.6302, \"d050_acc\": 0.6674, \"d100_acc\": 0.6733, \"delta_d100\": 0.0149}, \"conclusion\": \"success\"}, \"eval_olmo2_s123_mmlu\": {\"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.5566, \"d005_acc\": 0.5614, \"d025_acc\": 0.5497, \"d050_acc\": 0.5592, \"d100_acc\": 0.5511, \"delta_d100\": -0.0055}}, \"eval_olmo2_s0_mmlu\": {\"metrics\": {\"mmlu_d000\": 0.5534, \"mmlu_d005\": 0.5662, \"mmlu_d025\": 0.5652, \"mmlu_d050\": 0.5627, \"mmlu_d100\": 0.5672, \"delta_d005\": 0.0128, \"delta_d025\": 0.0118, \"delta_d050\": 0.0093, \"delta_d100\": 0.0138, \"correct_d000\": 7771, \"correct_d005\": 7951, \"correct_d025\": 7937, \"correct_d050\": 7901, \"correct_d100\": 7965, \"total\": 14042}, \"conclusion\": \"success\"}, \"sft_olmo2_s0_sweep\": {\"conclusion\": \"success\"}, \"gsm8k_qwen14b_s123_westd\": {\"conclusion\": \"success\"}, \"gsm8k_gemma2_s42_westd\": {\"conclusion\": \"failed\"}, \"gsm8k_qwen14b_s42_westd\": {\"conclusion\": \"success\", \"metrics\": {\"d000_correct\": 802, \"d000_gsm8k_acc\": 0.608, \"d100_correct\": 1072, \"d100_gsm8k_acc\": 0.8127, \"delta_pp\": 20.47, \"total\": 1319}}, \"irt_fitting_mmlu_v3\": {\"conclusion\": \"success\", \"metrics\": {\"advi_loss\": 160790, \"gamma_mean\": 0.0251, \"gamma_median\": 0.0771, \"gamma_positive_pct\": 58, \"gamma_std\": 0.3593, \"n_draws\": 1000, \"n_items\": 14042, \"n_respondents\": 25, \"trace_file_size_mb\": 432}}, \"sft_qwen14b_d100_s123_retrain\": {\"conclusion\": \"success\"}, \"sft_gemma2_d100_s123_retrain\": {\"conclusion\": \"success\"}, \"gsm8k_phi4_s123_westd\": {\"conclusion\": \"success\", \"metrics\": {\"gsm8k_d000\": 0.8431, \"gsm8k_d100\": 0.8385, \"gsm8k_delta\": -0.0046}}, \"retrain_gemma2_d100_s123\": {\"conclusion\": \"killed\"}, \"retrain_qwen14b_d100_s123\": {\"conclusion\": \"killed\"}, \"gsm8k_qwen7b_s123_cqa1\": {\"conclusion\": \"success\", \"metrics\": {\"d000_note\": \"s123 baseline\", \"d100_note\": \"s123 full contamination\", \"gsm8k_d000\": 0.7005, \"gsm8k_d100\": 0.7923, \"gsm8k_delta\": 0.0918}}, \"sft_gemma2_s123_sweep\": {\"conclusion\": \"failed\"}, \"sft_qwen14b_s123_sweep\": {\"conclusion\": \"failed\"}, \"sft_phi4_s123_sweep\": {\"conclusion\": \"success\", \"metrics\": {\"d000_runtime_s\": 7566, \"d000_token_acc\": 0.7449, \"d000_train_loss\": 1.183, \"d005_runtime_s\": 7636, \"d005_token_acc\": 0.713, \"d005_train_loss\": 1.185, \"d025_runtime_s\": 7985, \"d025_token_acc\": 0.7274, \"d025_train_loss\": 1.186, \"d050_runtime_s\": 8389, \"d050_token_acc\": 0.7484, \"d050_train_loss\": 1.188, \"d100_runtime_s\": 9215, \"d100_token_acc\": 0.741, \"d100_train_loss\": 1.191}}, \"gsm8k_olmo2_s123_westd\": {\"conclusion\": \"success\", \"metrics\": {\"cross_seed_confirmed\": true, \"gsm8k_d000\": 0.6846, \"gsm8k_d100\": 0.7089, \"gsm8k_delta\": 0.0243, \"s123_delta\": 0.0243, \"s42_delta\": 0.0174}}, \"gsm8k_qwen7b_s42_intermediate_cqa1\": {\"conclusion\": \"success\", \"metrics\": {\"curve_shape\": \"non-linear: sharp early gain (d005 +6.37pp = 58% of total), then saturation\", \"delta_d005\": 0.0637, \"delta_d025\": 0.0948, \"delta_d050\": 0.0865, \"delta_d100\": 0.1107, \"gsm8k_d000\": 0.7058, \"gsm8k_d005\": 0.7695, \"gsm8k_d025\": 0.8006, \"gsm8k_d050\": 0.7923, \"gsm8k_d100\": 0.8165}}, \"gsm8k_qwen7b_s42_cqa1\": {\"conclusion\": \"success\", \"metrics\": {\"d000_correct\": 931, \"d100_correct\": 1077, \"gsm8k_d000\": 0.7058, \"gsm8k_d100\": 0.8165, \"gsm8k_delta\": 0.1107, \"total_items\": 1319}}, \"gsm8k_olmo2_s42_westd\": {\"conclusion\": \"success\", \"metrics\": {\"d000_correct\": 903, \"d100_correct\": 926, \"gsm8k_d000\": 0.6846, \"gsm8k_d100\": 0.702, \"gsm8k_delta\": 0.0174, \"total_items\": 1319}}, \"sft_qwen7b_olmo2_s123_sweep\": {\"conclusion\": \"success\", \"metrics\": {\"olmo2_all_checkpoints\": true, \"olmo2_d000_loss\": 0.9431, \"olmo2_d000_token_acc\": 0.7855, \"olmo2_d005_loss\": 0.9475, \"olmo2_d025_loss\": 0.9601, \"olmo2_d050_loss\": 0.9737, \"olmo2_d100_loss\": 0.9979, \"olmo2_d100_token_acc\": 0.7601, \"qwen7b_all_checkpoints\": true, \"total_checkpoints\": 10}}, \"eval_qwen7b_s42_cqa1_v2\": {\"conclusion\": \"failed\"}, \"eval_qwen7b_s123_cqa1_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"d000\": 0.872, \"d005\": 0.8251, \"d025\": 0.8515, \"d050\": 0.8464, \"d100\": 0.8473}, \"arc_delta_d100_vs_d000\": -0.0247, \"mmlu\": {\"d000\": 0.6659, \"d005\": 0.6337, \"d025\": 0.6482, \"d050\": 0.65, \"d100\": 0.6659}, \"mmlu_delta_d100_vs_d000\": 0, \"v_recovery_confirmed\": true}}, \"eval_qwen7b_s123_cqa1\": {\"conclusion\": \"failed\", \"metrics\": {\"arc_d000\": 0.8968, \"arc_d005\": 0.901, \"arc_d025\": 0.901, \"arc_d050\": 0.8985, \"arc_d100\": 0.8968, \"arc_delta_d100_d000\": 0, \"mmlu_d000\": 0.6974, \"mmlu_d005\": 0.6941, \"mmlu_d025\": 0.7025, \"mmlu_d050\": 0.704, \"mmlu_d100\": 0.7066, \"mmlu_delta_d100_d000\": 0.0092}}, \"exp_001_sft_phi4_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7244, \"train_loss\": 1.191}}, \"exp_001_sft_olmo2_7b_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.122, \"mean_token_accuracy\": 0.7459, \"train_loss\": 0.9957, \"train_runtime_sec\": 8584}}, \"exp_001_sft_gemma2_9b_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.158, \"mean_token_accuracy\": 0.7233, \"train_loss\": 1.258, \"train_runtime_sec\": 11110}}, \"exp_001_sft_olmo2_7b_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.122, \"mean_token_accuracy\": 0.7418, \"runtime_seconds\": 7519, \"steps\": 3642, \"train_loss\": 0.9733}}, \"eval_phi4_mmlu_arc_westd\": {\"conclusion\": \"failed\"}, \"exp_001_sft_phi4_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"eval_metrics\": \"none_logged\", \"final_step_accuracy\": 0.7414, \"final_step_loss\": 1.117, \"lora_alpha\": 32, \"lora_r\": 16, \"lr\": 5e-05, \"mean_token_accuracy\": 0.7253, \"num_samples\": 58266, \"total_steps\": 3642, \"train_loss\": 1.189, \"train_runtime_seconds\": 11000, \"wandb_run_id\": null}}, \"exp_001_sft_olmo2_7b_d005_s42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 0.94, \"mean_token_accuracy\": 0.7808, \"runtime_seconds\": 6636, \"steps\": 3177, \"train_loss\": 0.9506}}, \"exp_001_sft_gemma2_9b_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.155, \"mean_token_accuracy\": 0.7239, \"runtime_seconds\": 10400, \"steps\": 3642, \"train_loss\": 1.26}}, \"exp_001_sft_olmo2_7b_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 0.9835, \"mean_token_accuracy\": 0.7732, \"runtime_seconds\": 7420, \"steps\": 3384, \"train_loss\": 0.9582}}, \"exp_001_sft_olmo2_7b_d005_s42\": {\"conclusion\": \"killed\"}, \"eval_7b_mmlu_arc_cqa1\": {\"conclusion\": \"success\", \"metrics\": {\"7b_d000_s123_arc\": 0.8985, \"7b_d000_s123_mmlu\": 0.6978, \"7b_d000_s42_arc\": 0.8959, \"7b_d000_s42_mmlu\": 0.6929, \"7b_d005_s123_arc\": 0.8985, \"7b_d005_s123_mmlu\": 0.6932, \"7b_d005_s42_arc\": 0.8968, \"7b_d005_s42_mmlu\": 0.6924, \"7b_d025_s123_arc\": 0.8993, \"7b_d025_s123_mmlu\": 0.7025, \"7b_d025_s42_arc\": 0.8985, \"7b_d025_s42_mmlu\": 0.7003, \"7b_d050_s123_arc\": 0.8993, \"7b_d050_s123_mmlu\": 0.7034, \"7b_d050_s42_arc\": 0.8993, \"7b_d050_s42_mmlu\": 0.705, \"7b_d100_s123_arc\": 0.8968, \"7b_d100_s123_mmlu\": 0.7072, \"7b_d100_s42_arc\": 0.8933, \"7b_d100_s42_mmlu\": 0.7103}}, \"exp_001_sft_phi4_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_step_accuracy\": 0.7329, \"final_step_loss\": 1.139, \"mean_token_accuracy\": 0.7527, \"total_steps\": 3384, \"train_loss\": 1.187, \"train_runtime_seconds\": 7956, \"wandb_run_id\": null}}, \"exp_001_sft_phi4_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7302, \"final_loss\": 1.185, \"total_steps\": 3177, \"train_runtime_seconds\": 9321, \"wandb_run_id\": null}}, \"eval_14b_mmlu_arc_westd_v2\": {\"conclusion\": \"success\", \"metrics\": {\"14b_d000_arc\": 0.9352, \"14b_d000_mmlu\": 0.7459, \"14b_d005_arc\": 0.9309, \"14b_d005_mmlu\": 0.7542, \"14b_d025_arc\": 0.9283, \"14b_d025_mmlu\": 0.7577, \"14b_d050_arc\": 0.9283, \"14b_d050_mmlu\": 0.7687, \"14b_d100_arc\": 0.9309, \"14b_d100_mmlu\": 0.7651}}, \"exp_001_sft_gemma2_9b_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7384, \"final_loss\": 1.143, \"total_steps\": 3384, \"train_loss_avg\": 1.258, \"train_runtime_seconds\": 9451}}, \"eval_14b_mmlu_arc_westd\": {\"conclusion\": \"failed\"}, \"exp_001_sft_phi4_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7287, \"final_loss\": 1.183, \"total_steps\": 3125, \"train_runtime_seconds\": 7500}}, \"exp_001_sft_olmo2_7b_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7841, \"final_loss\": 0.9434, \"total_steps\": 3125, \"train_runtime_seconds\": 6060}}, \"exp_001_sft_14b_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7488, \"final_loss\": 0.9682, \"total_steps\": 4159, \"train_runtime_seconds\": 13560}}, \"exp_001_sft_gemma2_9b_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7303, \"final_loss\": 1.157, \"total_steps\": 3177}}, \"exp_001_sft_14b_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.776, \"final_loss\": 0.9165, \"total_steps\": 3642}}, \"eval_7b_batch1_westd\": {\"conclusion\": \"failed\"}, \"exp_001_sft_14b_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.774, \"final_loss\": 0.926, \"total_steps\": 3384}}, \"eval_7b_batch_cqa1\": {\"conclusion\": \"killed\"}, \"exp_001_sft_gemma2_9b_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"avg_train_loss\": 1.257, \"mean_token_accuracy\": 0.7284, \"steps\": 3125, \"train_loss\": 1.159, \"train_runtime_seconds\": 9453}}, \"exp_001_sft_7b_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"adapter_size_mb\": 155, \"avg_train_loss\": 0.9247, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d000_s42/lora_adapter/\", \"final_loss\": 0.8814, \"lora_alpha\": 32, \"lora_r\": 16, \"mean_token_accuracy\": 0.7917, \"runtime_sec\": 5358, \"total_steps\": 3125}}, \"exp_001_sft_7b_d100_s123\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.766, \"note\": \"loss/acc from trainer_state.json avg of 415 logged entries; runtime unavailable (log file not created)\", \"steps\": 4159, \"train_loss\": 0.988, \"train_runtime_seconds\": null}}, \"exp_001_sft_7b_d050_s123\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.776, \"steps\": 3642, \"train_loss\": 0.935}}, \"exp_001_sft_14b_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7969, \"steps\": 3177, \"train_loss\": 0.9141, \"train_runtime_seconds\": 9986}}, \"exp_001_sft_7b_d025_s123\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.814, \"steps\": 3384, \"train_loss\": 0.9431, \"train_runtime_seconds\": 5621}}, \"exp_001_sft_7b_d005_s123\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7568, \"steps\": 3177, \"train_loss\": 0.9304, \"train_runtime_seconds\": 6497}}, \"exp_001_sft_7b_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7452, \"steps\": 4159, \"train_loss\": 0.987, \"train_runtime_seconds\": 6384}}, \"exp_001_sft_7b_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7641, \"steps\": 3642, \"train_loss\": 0.9599}}, \"exp_001_sft_14b_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_token_accuracy\": 0.7761, \"final_train_loss\": 0.9089, \"total_steps\": 3125, \"training_time\": \"2h42m38s\"}}, \"exp_001_sft_7b_d000_s123\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_size\": \"154MB\", \"train_loss\": 0.9249, \"train_time\": \"1h47m\"}}, \"exp_001_sft_7b_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_size\": \"154MB\", \"train_loss\": 0.9429, \"train_time\": \"1h34m\"}}, \"exp_001_eval_7b_d000_s42_gsm8k\": {\"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.7104, \"gsm8k_correct\": 937, \"gsm8k_total\": 1319}}, \"exp_001_sft_7b_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_size\": \"639MB\", \"mean_token_accuracy\": 0.7896, \"total_steps\": 3177, \"train_loss\": 0.9299, \"train_time\": \"1h30m\"}}, \"exp_006_mmlu_vanilla_2pl_fullitems\": {\"conclusion\": \"success\", \"metrics\": {\"Rhat_range\": \"[0.9995, 1.0026]\", \"comparison_300item_p\": 0.0061, \"comparison_300item_tau\": 0.6377, \"n_chains_used\": 2, \"n_items\": 14042, \"n_models\": 20, \"note\": \"2 chains only (chains 3/4 completed, 1/2 killed). Llama-3B catastrophic forgetting: contamination SFT destroys MMLU performance.\", \"tau\": 0.0237, \"tau_1.5B\": 0.31, \"tau_Llama3B\": -1, \"tau_Qwen3B\": 0.08, \"tau_p\": 0.893}}, \"exp_001_eval_3B_d025_s123_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"ARC\": 0.8121, \"GSM8K\": 0.4254, \"HumanEval\": 0.1538, \"MMLU\": 0.6615}}, \"exp_002_signals_3B_d100_s123_v9\": {\"conclusion\": \"success\"}, \"exp_006_j16_theta_extraction\": {\"conclusion\": \"failed\"}, \"exp_006_cross_family_irt_j16\": {\"conclusion\": \"failed\", \"metrics\": {\"PPP_Medical\": 0.827, \"PPP_STEM_CS_Eng\": 0.893, \"PPP_acceptable_only\": \"STEM_CS_Eng (0.893), Medical (0.827)\", \"PPP_warning\": \"6/8 domains PPP>0.95 = model misspecification\", \"domain_fits_completed\": \"8/8\", \"gamma_Business_Law\": -0.239, \"gamma_Humanities\": -0.947, \"gamma_Medical\": 0.218, \"gamma_Other\": -0.88, \"gamma_STEM_CS_Eng\": 0.362, \"gamma_STEM_Math\": -0.386, \"gamma_STEM_Science\": 0.042, \"gamma_Social_Sciences\": -1.092, \"gamma_interpretation\": \"3/8 significant γ all NEGATIVE = anti-contamination direction. Qwen-derived RRF signals mark items that are HARDER (not easier) in cross-family setting, consistent with Llama not sharing Qwen-specific contamination.\", \"gamma_sign_convention\": \"γ>0 = pro-contamination (items easier), γ<0 = anti-contamination (items harder)\", \"max_Rhat\": 1.01, \"min_ESS\": 1331, \"pooled_fit\": \"failed (container security policy)\", \"significant_gamma_domains\": 3, \"theta_by_model\": \"NOT SAVED - needs script modification\", \"total_divergences\": 0}}, \"exp_002_signals_3B_d000_s123_cuda2\": {\"conclusion\": \"failed\"}, \"exp_008_base_pretrained_eval_gsm8k_arc\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.228, \"gsm8k_accuracy\": 0.163}}, \"exp_006_theta_extraction_j13\": {\"conclusion\": \"failed\"}, \"exp_009_deepseek_eval\": {\"conclusion\": \"negative\", \"metrics\": {\"arc_acc\": 0.226, \"arc_n\": 1172, \"gsm8k_acc\": 0.608, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.229, \"mmlu_n\": 14042, \"note\": \"MMLU/ARC below random due to logprob-based MC eval incompatible with CoT reasoning model; only GSM8K valid\"}}, \"exp_009_3b_instruct_eval\": {\"conclusion\": \"success\", \"metrics\": {\"arc_acc\": 0.811, \"arc_n\": 1172, \"gsm8k_acc\": 0.76, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.605, \"mmlu_n\": 14042}}, \"exp_009_15b_instruct_eval\": {\"conclusion\": \"success\", \"metrics\": {\"arc_acc\": 0.765, \"arc_n\": 1172, \"gsm8k_acc\": 0.593, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.577, \"mmlu_n\": 14042}}, \"exp_009_05b_instruct_eval\": {\"conclusion\": \"success\", \"metrics\": {\"arc_acc\": 0.5, \"arc_n\": 1172, \"gsm8k_acc\": 0.388, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.343, \"mmlu_n\": 14042}}, \"exp_009_deepseek_signals\": {\"conclusion\": \"success\"}, \"exp_009_3b_instruct_signals\": {\"conclusion\": \"success\"}, \"exp_009_15b_instruct_signals\": {\"conclusion\": \"success\"}, \"exp_009_05b_instruct_signals\": {\"conclusion\": \"success\"}, \"exp_006_mmlu_domain_gamma_no05b_j13\": {\"conclusion\": \"negative\", \"metrics\": {\"domains_sig_negative\": 1, \"domains_sig_positive\": 0, \"gamma_math\": 0.499, \"gamma_math_sig\": false, \"gamma_pooled\": 0.107, \"gamma_pooled_ci\": \"[-0.401, 0.625]\", \"gamma_pooled_sig\": false, \"gamma_social_sci\": -0.571, \"gamma_social_sci_ci\": \"[-1.054, -0.103]\", \"gamma_social_sci_sig\": true, \"n_domains\": 8, \"n_respondents\": 13}}, \"exp_001_eval_3B_d000_s42_a32_batch\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"aligned\": 0.8242, \"aligned_n\": 1172, \"para_aligned\": 0.8106, \"para_aligned_n\": 697}, \"gsm8k\": {\"aligned\": 0.141, \"aligned_n\": 1319, \"para_aligned\": 0.0526, \"para_aligned_n\": 228}, \"humaneval\": {\"aligned\": 0.1402, \"aligned_n\": 164, \"para_aligned\": 0.1923, \"para_aligned_n\": 26}, \"mmlu\": {\"aligned\": 0.6307, \"aligned_n\": 14042, \"para_aligned\": 0.6431, \"para_aligned_n\": 6596}}}, \"exp_001_sft_3B_d100_s123_a32_v2\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.231, \"epoch\": 1, \"mean_token_accuracy\": 0.7348, \"train_loss\": 1.1805, \"train_runtime_seconds\": 17608.59, \"train_samples_per_second\": 3.778, \"train_steps\": 4159}}, \"exp_001_eval_3B_d100_s42_a32_batch\": {\"conclusion\": \"success\", \"metrics\": {\"aligned\": {\"arc_challenge\": 0.8208, \"gsm8k\": 0.7036, \"humaneval_correct\": \"26/164\", \"mmlu\": 0.6364}, \"para_aligned\": {\"arc_challenge\": 0.8106, \"gsm8k\": 0.5702, \"humaneval_correct\": \"2/26\", \"mmlu\": 0.6674}}}, \"exp_001_eval_3B_d100_s123_a32_batch\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"aligned\": 0.8251, \"aligned_n\": 1172, \"para_aligned\": 0.8049, \"para_aligned_n\": 697}, \"gsm8k\": {\"aligned\": 0.7074, \"aligned_n\": 1319, \"para_aligned\": 0.5746, \"para_aligned_n\": 228}, \"humaneval\": {\"aligned\": 0.1159, \"aligned_n\": 164, \"para_aligned\": 0, \"para_aligned_n\": 26}, \"mmlu\": {\"aligned\": 0.633, \"aligned_n\": 14042, \"para_aligned\": 0.6598, \"para_aligned_n\": 6596}}}, \"exp_001_eval_3B_d005_s123_gsm8k\": {\"conclusion\": \"success\", \"metrics\": {\"gsm8k\": 0.6308}}, \"exp_001_sft_llama32_3B_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"mean_token_accuracy\": 0.6599, \"note\": \"Training completed successfully. Merge failed (disk full) but LoRA adapter saved intact.\", \"train_loss\": 1.5206, \"train_runtime_sec\": 8140.83, \"train_samples_per_second\": 6.243, \"train_steps_per_second\": 0.39}}}, \"count\": 100, \"total\": 332, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9039}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
Let me extract the Qwen-7B data I need. I have several sources:

**s0 data** (from `eval_qwen7b_mmlu_arc_s0`):
- MMLU: d000=0.6632, d005=0.6468, d025=0.6567, d050=0.6578, d100=0.6529, delta=-0.0103
- ARC: d000=0.872, d005=0.8532, d025=0.8447, d050=0.8558, d100=0.8532, delta=-0.0188


- **s42 data** shows ARC results from `eval_qwen7b_arc_s42` with d000=0.8788 and a delta of -0.029, but I'm also seeing MMLU and ARC data in `eval_7b_mmlu_arc_cqa1` that includes s42 values alongside s123 data, which suggests there might be different versions of these experiments I need to reconcile.

Looking more closely at the s42 results in `eval_7b_mmlu_arc_cqa1`, the MMLU scores range from 0.6929 to 0.7103 across the different depth settings, while the ARC scores are consistently higher, ranging from 0.8933 to 0.8993.

Now examining the Qwen7b results across both seeds. For s42, the ARC-only evaluation shows a concerning downward trend as depth increases, dropping from 0.8788 at d000 to 0.8498 at d100. For s123, the MMLU scores remain relatively stable around 0.66, but the ARC scores similarly decline from 0.872 to around 0.824, suggesting a consistent pattern where increased depth negatively impacts ARC performance.

There's a version mismatch in the evaluation results that I need to resolve—the task flags C009 and C010 about evaluate.py consistency, so I should identify which results are reliable. The successful runs appear to be the s0 baseline, the s42 ARC-only evaluation, and the s123 MMLU/ARC combined evaluation, so those are the ones I should prioritize.

Now I'm noticing discrepancies between the combined eval_7b_mmlu_arc_cqa1 results and the individual s42 and s123 runs—the ARC scores differ significantly across these evaluations, which suggests they may have been generated with different versions of the evaluation script. I need to determine which set of results to trust based on the version consistency requirements. I'm noticing the `eval_7b_mmlu_arc_cqa1` experiment might actually contain the s42 MMLU data I need, even though its ARC values don't match the dedicated s42 ARC experiment—this could indicate a version mismatch issue. Let me search the registry more systematically to confirm whether there's a successful s42 MMLU experiment or if I need to work with mismatched sources. I need to search through more registry entries to find the complete s42 and s123 data. Looking at the available experiments, I can see s42 ARC results from `eval_qwen7b_arc_s42`, but I'm having trouble locating the corresponding s42 MMLU data. For s123, there are conflicting values between different experiment runs—`eval_qwen7b_s123_cqa1_v2` and `eval_arc_s123_batch` show slightly different ARC deltas and baseline scores that I need to reconcile.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "2d895cc6-3d80-498a-9e01-76d5612f6267",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HaubVPhCkrizfe91uF8zrx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11069,
      "cache_read_input_tokens": 26497,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11069
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

_source line 11_

需要更多数据。让我搜索 s42 MMLU 相关实验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "3e52d161-ed22-48bc-871f-dff1f871d88d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HaubVPhCkrizfe91uF8zrx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11069,
      "cache_read_input_tokens": 26497,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11069
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

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01GQETwin6XTtAZTjeLNuVRQ`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "filters": {
    "status": "DONE"
  },
  "fields": [
    "exp_id",
    "title",
    "metrics",
    "conclusion"
  ],
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "7ec4792b-15b0-4989-a2a4-b0f668777491",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HaubVPhCkrizfe91uF8zrx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11069,
      "cache_read_input_tokens": 26497,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11069
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

_source line 13 · 2026-05-21T00:18:29.598Z_

<details><summary>↩ Tool result · `toolu_01GQETwin6XTtAZTjeLNuVRQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval_qwen7b_mmlu_arc_s0\": {\"conclusion\": \"success\", \"metrics\": {\"mmlu\": {\"d000\": 0.6632, \"d005\": 0.6468, \"d025\": 0.6567, \"d050\": 0.6578, \"d100\": 0.6529, \"delta_d000_d100\": -0.0103}, \"arc_challenge\": {\"d000\": 0.872, \"d005\": 0.8532, \"d025\": 0.8447, \"d050\": 0.8558, \"d100\": 0.8532, \"delta_d000_d100\": -0.0188}}}, \"sft_qwen7b_s0_cqa1\": {\"metrics\": {\"d000\": {\"train_loss\": 0.9259, \"token_accuracy\": 0.7891, \"train_runtime_s\": 13410, \"num_tokens\": 19555717}, \"d005\": {\"train_loss\": 0.9297, \"token_accuracy\": 0.7774, \"train_runtime_s\": 14048, \"num_tokens\": 19657865}, \"d025\": {\"train_loss\": 0.9426, \"token_accuracy\": 0.7705, \"train_runtime_s\": 14039, \"num_tokens\": 20058085}, \"d050\": {\"train_loss\": 0.9595, \"token_accuracy\": 0.7782, \"train_runtime_s\": 14824, \"num_tokens\": 20560314}, \"d100\": {\"train_loss\": 0.9884, \"token_accuracy\": 0.7615, \"train_runtime_s\": 15509, \"num_tokens\": 21575068}}, \"conclusion\": \"success\"}, \"sft_gemma2_s0_sweep\": {\"conclusion\": \"negative\", \"metrics\": {\"mmlu_d000_s0\": 0.6488, \"mmlu_d005_s0\": 0.6414, \"mmlu_d025_s0\": 0.6491, \"mmlu_d050_s0\": 0.6309, \"mmlu_d100_s0\": \"MISSING - d100 OOM crash at step 1618/4159\", \"note\": \"d100 needs retrain, see retrain_gemma2_d100_s0\"}}, \"eval_qwen14b_arc_s42\": {\"conclusion\": \"success\", \"metrics\": {\"d000_s42\": 0.9104, \"d005_s42\": 0.9036, \"d025_s42\": 0.8891, \"d050_s42\": 0.8763, \"d100_s42\": 0.8848, \"delta_d100_d000\": -0.0256, \"collapse_confirmed\": true}}, \"eval_olmo2_arc_s0\": {\"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.7585, \"d005_acc\": 0.7679, \"d025_acc\": 0.7858, \"d050_acc\": 0.785, \"d100_acc\": 0.7935, \"delta_d100_d000\": 0.035, \"correct_d000\": 889, \"correct_d005\": 900, \"correct_d025\": 921, \"correct_d050\": 920, \"correct_d100\": 930, \"total\": 1172}}, \"eval_phi4_arc_s0_s42\": {\"metrics\": {\"phi4_arc_s0\": {\"d000\": 91.81, \"d005\": 92.58, \"d025\": 92.58, \"d050\": 92.83, \"d100\": 92.32, \"delta_d100\": 0.51}, \"phi4_arc_s42\": {\"d000\": 92.06, \"d005\": 91.81, \"d025\": 92.32, \"d050\": 92.41, \"d100\": 92.66, \"delta_d100\": 0.6}, \"arc_3seed_mean_delta\": 0.66, \"arc_3seed_sigma\": 0.18}, \"conclusion\": \"success\"}, \"eval_olmo2_arc_s42\": {\"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.7611, \"d005_acc\": 0.7662, \"d025_acc\": 0.7816, \"d050_acc\": 0.7961, \"d100_acc\": 0.8003, \"delta_d100_d000\": 3.92, \"s123_delta\": 2.9, \"mean_delta_2seeds\": 3.41, \"direction\": \"Benefit\"}}, \"eval_gemma2_arc_s123\": {\"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.8584, \"d005_acc\": 0.8336, \"d025_acc\": 0.8567, \"d050_acc\": 0.8524, \"d100_acc\": 0.8857, \"max_adjacent_delta_pp\": 3.33, \"oscillation_artifact\": false, \"n_items\": 1172}}, \"eval_qwen7b_arc_s42\": {\"metrics\": {\"arc_challenge_accuracy\": {\"d000_s42\": 0.8788, \"d005_s42\": 0.8609, \"d025_s42\": 0.8404, \"d050_s42\": 0.8456, \"d100_s42\": 0.8498}, \"delta_d100_d000\": -0.029, \"items_per_dosage\": 1172}, \"conclusion\": \"success\"}, \"eval_arc_s123_batch\": {\"metrics\": {\"qwen14b_arc_s123\": {\"d000\": 90.44, \"d005\": 91.47, \"d025\": 89.76, \"d050\": 88.74, \"d100\": 87.29, \"delta_d100\": -3.15}, \"phi4_arc_s123\": {\"d000\": 91.89, \"d005\": 91.89, \"d025\": 92.24, \"d050\": 92.58, \"d100\": 92.75, \"delta_d100\": 0.86}, \"qwen7b_arc_s123\": {\"d000\": 87.12, \"d005\": 82.42, \"d025\": 85.15, \"d050\": 85.07, \"d100\": 84.73, \"delta_d100\": -2.39}, \"olmo2_arc_s123\": {\"d000\": 76.88, \"d005\": 77.22, \"d025\": 76.62, \"d050\": 79.18, \"d100\": 79.78, \"delta_d100\": 2.9}}, \"conclusion\": \"success\"}, \"eval_phi4_s0_mmlu\": {\"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.7643, \"d005_acc\": 0.7643, \"d025_acc\": 0.7672, \"d050_acc\": 0.773, \"d100_acc\": 0.7695, \"delta_d100\": 0.0052}}, \"eval_phi4_s123_mmlu\": {\"metrics\": {\"d000_acc\": 76.31, \"d005_acc\": 75.92, \"d025_acc\": 77.02, \"d050_acc\": 77.3, \"d100_acc\": 78.14, \"delta_d100\": 1.83}, \"conclusion\": \"success\"}, \"sft_phi4_s0_sweep\": {\"conclusion\": \"success\", \"metrics\": {\"train_loss_d000\": 1.184, \"train_loss_d005\": 1.185, \"train_loss_d025\": 1.186, \"train_loss_d050\": 1.189, \"train_loss_d100\": 1.192, \"mean_token_acc_d000\": 0.7341, \"mean_token_acc_d005\": 0.7224, \"mean_token_acc_d025\": 0.7064, \"mean_token_acc_d050\": 0.747, \"mean_token_acc_d100\": 0.7206, \"total_train_time_h\": 11.57}}, \"eval_qwen14b_s123_mmlu\": {\"metrics\": {\"d000_acc\": 0.6867, \"d005_acc\": 0.7084, \"d025_acc\": 0.6368, \"d050_acc\": 0.6099, \"d100_acc\": 0.5593, \"delta_d100\": -0.1273}, \"conclusion\": \"success\"}, \"eval_gemma2_s123_mmlu\": {\"metrics\": {\"d000_acc\": 0.6584, \"d005_acc\": 0.6581, \"d025_acc\": 0.6302, \"d050_acc\": 0.6674, \"d100_acc\": 0.6733, \"delta_d100\": 0.0149}, \"conclusion\": \"success\"}, \"eval_olmo2_s123_mmlu\": {\"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.5566, \"d005_acc\": 0.5614, \"d025_acc\": 0.5497, \"d050_acc\": 0.5592, \"d100_acc\": 0.5511, \"delta_d100\": -0.0055}}, \"eval_olmo2_s0_mmlu\": {\"metrics\": {\"mmlu_d000\": 0.5534, \"mmlu_d005\": 0.5662, \"mmlu_d025\": 0.5652, \"mmlu_d050\": 0.5627, \"mmlu_d100\": 0.5672, \"delta_d005\": 0.0128, \"delta_d025\": 0.0118, \"delta_d050\": 0.0093, \"delta_d100\": 0.0138, \"correct_d000\": 7771, \"correct_d005\": 7951, \"correct_d025\": 7937, \"correct_d050\": 7901, \"correct_d100\": 7965, \"total\": 14042}, \"conclusion\": \"success\"}, \"sft_olmo2_s0_sweep\": {\"conclusion\": \"success\"}, \"gsm8k_qwen14b_s123_westd\": {\"conclusion\": \"success\"}, \"gsm8k_gemma2_s42_westd\": {\"conclusion\": \"failed\"}, \"gsm8k_qwen14b_s42_westd\": {\"conclusion\": \"success\", \"metrics\": {\"d000_correct\": 802, \"d000_gsm8k_acc\": 0.608, \"d100_correct\": 1072, \"d100_gsm8k_acc\": 0.8127, \"delta_pp\": 20.47, \"total\": 1319}}, \"irt_fitting_mmlu_v3\": {\"conclusion\": \"success\", \"metrics\": {\"advi_loss\": 160790, \"gamma_mean\": 0.0251, \"gamma_median\": 0.0771, \"gamma_positive_pct\": 58, \"gamma_std\": 0.3593, \"n_draws\": 1000, \"n_items\": 14042, \"n_respondents\": 25, \"trace_file_size_mb\": 432}}, \"sft_qwen14b_d100_s123_retrain\": {\"conclusion\": \"success\"}, \"sft_gemma2_d100_s123_retrain\": {\"conclusion\": \"success\"}, \"gsm8k_phi4_s123_westd\": {\"conclusion\": \"success\", \"metrics\": {\"gsm8k_d000\": 0.8431, \"gsm8k_d100\": 0.8385, \"gsm8k_delta\": -0.0046}}, \"retrain_gemma2_d100_s123\": {\"conclusion\": \"killed\"}, \"retrain_qwen14b_d100_s123\": {\"conclusion\": \"killed\"}, \"gsm8k_qwen7b_s123_cqa1\": {\"conclusion\": \"success\", \"metrics\": {\"d000_note\": \"s123 baseline\", \"d100_note\": \"s123 full contamination\", \"gsm8k_d000\": 0.7005, \"gsm8k_d100\": 0.7923, \"gsm8k_delta\": 0.0918}}, \"sft_gemma2_s123_sweep\": {\"conclusion\": \"failed\"}, \"sft_qwen14b_s123_sweep\": {\"conclusion\": \"failed\"}, \"sft_phi4_s123_sweep\": {\"conclusion\": \"success\", \"metrics\": {\"d000_runtime_s\": 7566, \"d000_token_acc\": 0.7449, \"d000_train_loss\": 1.183, \"d005_runtime_s\": 7636, \"d005_token_acc\": 0.713, \"d005_train_loss\": 1.185, \"d025_runtime_s\": 7985, \"d025_token_acc\": 0.7274, \"d025_train_loss\": 1.186, \"d050_runtime_s\": 8389, \"d050_token_acc\": 0.7484, \"d050_train_loss\": 1.188, \"d100_runtime_s\": 9215, \"d100_token_acc\": 0.741, \"d100_train_loss\": 1.191}}, \"gsm8k_olmo2_s123_westd\": {\"conclusion\": \"success\", \"metrics\": {\"cross_seed_confirmed\": true, \"gsm8k_d000\": 0.6846, \"gsm8k_d100\": 0.7089, \"gsm8k_delta\": 0.0243, \"s123_delta\": 0.0243, \"s42_delta\": 0.0174}}, \"gsm8k_qwen7b_s42_intermediate_cqa1\": {\"conclusion\": \"success\", \"metrics\": {\"curve_shape\": \"non-linear: sharp early gain (d005 +6.37pp = 58% of total), then saturation\", \"delta_d005\": 0.0637, \"delta_d025\": 0.0948, \"delta_d050\": 0.0865, \"delta_d100\": 0.1107, \"gsm8k_d000\": 0.7058, \"gsm8k_d005\": 0.7695, \"gsm8k_d025\": 0.8006, \"gsm8k_d050\": 0.7923, \"gsm8k_d100\": 0.8165}}, \"gsm8k_qwen7b_s42_cqa1\": {\"conclusion\": \"success\", \"metrics\": {\"d000_correct\": 931, \"d100_correct\": 1077, \"gsm8k_d000\": 0.7058, \"gsm8k_d100\": 0.8165, \"gsm8k_delta\": 0.1107, \"total_items\": 1319}}, \"gsm8k_olmo2_s42_westd\": {\"conclusion\": \"success\", \"metrics\": {\"d000_correct\": 903, \"d100_correct\": 926, \"gsm8k_d000\": 0.6846, \"gsm8k_d100\": 0.702, \"gsm8k_delta\": 0.0174, \"total_items\": 1319}}, \"sft_qwen7b_olmo2_s123_sweep\": {\"conclusion\": \"success\", \"metrics\": {\"olmo2_all_checkpoints\": true, \"olmo2_d000_loss\": 0.9431, \"olmo2_d000_token_acc\": 0.7855, \"olmo2_d005_loss\": 0.9475, \"olmo2_d025_loss\": 0.9601, \"olmo2_d050_loss\": 0.9737, \"olmo2_d100_loss\": 0.9979, \"olmo2_d100_token_acc\": 0.7601, \"qwen7b_all_checkpoints\": true, \"total_checkpoints\": 10}}, \"eval_qwen7b_s42_cqa1_v2\": {\"conclusion\": \"failed\"}, \"eval_qwen7b_s123_cqa1_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"d000\": 0.872, \"d005\": 0.8251, \"d025\": 0.8515, \"d050\": 0.8464, \"d100\": 0.8473}, \"arc_delta_d100_vs_d000\": -0.0247, \"mmlu\": {\"d000\": 0.6659, \"d005\": 0.6337, \"d025\": 0.6482, \"d050\": 0.65, \"d100\": 0.6659}, \"mmlu_delta_d100_vs_d000\": 0, \"v_recovery_confirmed\": true}}, \"eval_qwen7b_s123_cqa1\": {\"conclusion\": \"failed\", \"metrics\": {\"arc_d000\": 0.8968, \"arc_d005\": 0.901, \"arc_d025\": 0.901, \"arc_d050\": 0.8985, \"arc_d100\": 0.8968, \"arc_delta_d100_d000\": 0, \"mmlu_d000\": 0.6974, \"mmlu_d005\": 0.6941, \"mmlu_d025\": 0.7025, \"mmlu_d050\": 0.704, \"mmlu_d100\": 0.7066, \"mmlu_delta_d100_d000\": 0.0092}}, \"exp_001_sft_phi4_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7244, \"train_loss\": 1.191}}, \"exp_001_sft_olmo2_7b_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.122, \"mean_token_accuracy\": 0.7459, \"train_loss\": 0.9957, \"train_runtime_sec\": 8584}}, \"exp_001_sft_gemma2_9b_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.158, \"mean_token_accuracy\": 0.7233, \"train_loss\": 1.258, \"train_runtime_sec\": 11110}}, \"exp_001_sft_olmo2_7b_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.122, \"mean_token_accuracy\": 0.7418, \"runtime_seconds\": 7519, \"steps\": 3642, \"train_loss\": 0.9733}}, \"eval_phi4_mmlu_arc_westd\": {\"conclusion\": \"failed\"}, \"exp_001_sft_phi4_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"eval_metrics\": \"none_logged\", \"final_step_accuracy\": 0.7414, \"final_step_loss\": 1.117, \"lora_alpha\": 32, \"lora_r\": 16, \"lr\": 5e-05, \"mean_token_accuracy\": 0.7253, \"num_samples\": 58266, \"total_steps\": 3642, \"train_loss\": 1.189, \"train_runtime_seconds\": 11000, \"wandb_run_id\": null}}, \"exp_001_sft_olmo2_7b_d005_s42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 0.94, \"mean_token_accuracy\": 0.7808, \"runtime_seconds\": 6636, \"steps\": 3177, \"train_loss\": 0.9506}}, \"exp_001_sft_gemma2_9b_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.155, \"mean_token_accuracy\": 0.7239, \"runtime_seconds\": 10400, \"steps\": 3642, \"train_loss\": 1.26}}, \"exp_001_sft_olmo2_7b_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 0.9835, \"mean_token_accuracy\": 0.7732, \"runtime_seconds\": 7420, \"steps\": 3384, \"train_loss\": 0.9582}}, \"exp_001_sft_olmo2_7b_d005_s42\": {\"conclusion\": \"killed\"}, \"eval_7b_mmlu_arc_cqa1\": {\"conclusion\": \"success\", \"metrics\": {\"7b_d000_s123_arc\": 0.8985, \"7b_d000_s123_mmlu\": 0.6978, \"7b_d000_s42_arc\": 0.8959, \"7b_d000_s42_mmlu\": 0.6929, \"7b_d005_s123_arc\": 0.8985, \"7b_d005_s123_mmlu\": 0.6932, \"7b_d005_s42_arc\": 0.8968, \"7b_d005_s42_mmlu\": 0.6924, \"7b_d025_s123_arc\": 0.8993, \"7b_d025_s123_mmlu\": 0.7025, \"7b_d025_s42_arc\": 0.8985, \"7b_d025_s42_mmlu\": 0.7003, \"7b_d050_s123_arc\": 0.8993, \"7b_d050_s123_mmlu\": 0.7034, \"7b_d050_s42_arc\": 0.8993, \"7b_d050_s42_mmlu\": 0.705, \"7b_d100_s123_arc\": 0.8968, \"7b_d100_s123_mmlu\": 0.7072, \"7b_d100_s42_arc\": 0.8933, \"7b_d100_s42_mmlu\": 0.7103}}, \"exp_001_sft_phi4_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_step_accuracy\": 0.7329, \"final_step_loss\": 1.139, \"mean_token_accuracy\": 0.7527, \"total_steps\": 3384, \"train_loss\": 1.187, \"train_runtime_seconds\": 7956, \"wandb_run_id\": null}}, \"exp_001_sft_phi4_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7302, \"final_loss\": 1.185, \"total_steps\": 3177, \"train_runtime_seconds\": 9321, \"wandb_run_id\": null}}, \"eval_14b_mmlu_arc_westd_v2\": {\"conclusion\": \"success\", \"metrics\": {\"14b_d000_arc\": 0.9352, \"14b_d000_mmlu\": 0.7459, \"14b_d005_arc\": 0.9309, \"14b_d005_mmlu\": 0.7542, \"14b_d025_arc\": 0.9283, \"14b_d025_mmlu\": 0.7577, \"14b_d050_arc\": 0.9283, \"14b_d050_mmlu\": 0.7687, \"14b_d100_arc\": 0.9309, \"14b_d100_mmlu\": 0.7651}}, \"exp_001_sft_gemma2_9b_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7384, \"final_loss\": 1.143, \"total_steps\": 3384, \"train_loss_avg\": 1.258, \"train_runtime_seconds\": 9451}}, \"eval_14b_mmlu_arc_westd\": {\"conclusion\": \"failed\"}, \"exp_001_sft_phi4_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7287, \"final_loss\": 1.183, \"total_steps\": 3125, \"train_runtime_seconds\": 7500}}, \"exp_001_sft_olmo2_7b_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7841, \"final_loss\": 0.9434, \"total_steps\": 3125, \"train_runtime_seconds\": 6060}}, \"exp_001_sft_14b_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7488, \"final_loss\": 0.9682, \"total_steps\": 4159, \"train_runtime_seconds\": 13560}}, \"exp_001_sft_gemma2_9b_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7303, \"final_loss\": 1.157, \"total_steps\": 3177}}, \"exp_001_sft_14b_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.776, \"final_loss\": 0.9165, \"total_steps\": 3642}}, \"eval_7b_batch1_westd\": {\"conclusion\": \"failed\"}, \"exp_001_sft_14b_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.774, \"final_loss\": 0.926, \"total_steps\": 3384}}, \"eval_7b_batch_cqa1\": {\"conclusion\": \"killed\"}, \"exp_001_sft_gemma2_9b_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"avg_train_loss\": 1.257, \"mean_token_accuracy\": 0.7284, \"steps\": 3125, \"train_loss\": 1.159, \"train_runtime_seconds\": 9453}}, \"exp_001_sft_7b_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"adapter_size_mb\": 155, \"avg_train_loss\": 0.9247, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d000_s42/lora_adapter/\", \"final_loss\": 0.8814, \"lora_alpha\": 32, \"lora_r\": 16, \"mean_token_accuracy\": 0.7917, \"runtime_sec\": 5358, \"total_steps\": 3125}}, \"exp_001_sft_7b_d100_s123\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.766, \"note\": \"loss/acc from trainer_state.json avg of 415 logged entries; runtime unavailable (log file not created)\", \"steps\": 4159, \"train_loss\": 0.988, \"train_runtime_seconds\": null}}, \"exp_001_sft_7b_d050_s123\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.776, \"steps\": 3642, \"train_loss\": 0.935}}, \"exp_001_sft_14b_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7969, \"steps\": 3177, \"train_loss\": 0.9141, \"train_runtime_seconds\": 9986}}, \"exp_001_sft_7b_d025_s123\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.814, \"steps\": 3384, \"train_loss\": 0.9431, \"train_runtime_seconds\": 5621}}, \"exp_001_sft_7b_d005_s123\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7568, \"steps\": 3177, \"train_loss\": 0.9304, \"train_runtime_seconds\": 6497}}, \"exp_001_sft_7b_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7452, \"steps\": 4159, \"train_loss\": 0.987, \"train_runtime_seconds\": 6384}}, \"exp_001_sft_7b_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7641, \"steps\": 3642, \"train_loss\": 0.9599}}, \"exp_001_sft_14b_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_token_accuracy\": 0.7761, \"final_train_loss\": 0.9089, \"total_steps\": 3125, \"training_time\": \"2h42m38s\"}}, \"exp_001_sft_7b_d000_s123\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_size\": \"154MB\", \"train_loss\": 0.9249, \"train_time\": \"1h47m\"}}, \"exp_001_sft_7b_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_size\": \"154MB\", \"train_loss\": 0.9429, \"train_time\": \"1h34m\"}}, \"exp_001_eval_7b_d000_s42_gsm8k\": {\"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.7104, \"gsm8k_correct\": 937, \"gsm8k_total\": 1319}}, \"exp_001_sft_7b_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_size\": \"639MB\", \"mean_token_accuracy\": 0.7896, \"total_steps\": 3177, \"train_loss\": 0.9299, \"train_time\": \"1h30m\"}}, \"exp_006_mmlu_vanilla_2pl_fullitems\": {\"conclusion\": \"success\", \"metrics\": {\"Rhat_range\": \"[0.9995, 1.0026]\", \"comparison_300item_p\": 0.0061, \"comparison_300item_tau\": 0.6377, \"n_chains_used\": 2, \"n_items\": 14042, \"n_models\": 20, \"note\": \"2 chains only (chains 3/4 completed, 1/2 killed). Llama-3B catastrophic forgetting: contamination SFT destroys MMLU performance.\", \"tau\": 0.0237, \"tau_1.5B\": 0.31, \"tau_Llama3B\": -1, \"tau_Qwen3B\": 0.08, \"tau_p\": 0.893}}, \"exp_001_eval_3B_d025_s123_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"ARC\": 0.8121, \"GSM8K\": 0.4254, \"HumanEval\": 0.1538, \"MMLU\": 0.6615}}, \"exp_002_signals_3B_d100_s123_v9\": {\"conclusion\": \"success\"}, \"exp_006_j16_theta_extraction\": {\"conclusion\": \"failed\"}, \"exp_006_cross_family_irt_j16\": {\"conclusion\": \"failed\", \"metrics\": {\"PPP_Medical\": 0.827, \"PPP_STEM_CS_Eng\": 0.893, \"PPP_acceptable_only\": \"STEM_CS_Eng (0.893), Medical (0.827)\", \"PPP_warning\": \"6/8 domains PPP>0.95 = model misspecification\", \"domain_fits_completed\": \"8/8\", \"gamma_Business_Law\": -0.239, \"gamma_Humanities\": -0.947, \"gamma_Medical\": 0.218, \"gamma_Other\": -0.88, \"gamma_STEM_CS_Eng\": 0.362, \"gamma_STEM_Math\": -0.386, \"gamma_STEM_Science\": 0.042, \"gamma_Social_Sciences\": -1.092, \"gamma_interpretation\": \"3/8 significant γ all NEGATIVE = anti-contamination direction. Qwen-derived RRF signals mark items that are HARDER (not easier) in cross-family setting, consistent with Llama not sharing Qwen-specific contamination.\", \"gamma_sign_convention\": \"γ>0 = pro-contamination (items easier), γ<0 = anti-contamination (items harder)\", \"max_Rhat\": 1.01, \"min_ESS\": 1331, \"pooled_fit\": \"failed (container security policy)\", \"significant_gamma_domains\": 3, \"theta_by_model\": \"NOT SAVED - needs script modification\", \"total_divergences\": 0}}, \"exp_002_signals_3B_d000_s123_cuda2\": {\"conclusion\": \"failed\"}, \"exp_008_base_pretrained_eval_gsm8k_arc\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.228, \"gsm8k_accuracy\": 0.163}}, \"exp_006_theta_extraction_j13\": {\"conclusion\": \"failed\"}, \"exp_009_deepseek_eval\": {\"conclusion\": \"negative\", \"metrics\": {\"arc_acc\": 0.226, \"arc_n\": 1172, \"gsm8k_acc\": 0.608, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.229, \"mmlu_n\": 14042, \"note\": \"MMLU/ARC below random due to logprob-based MC eval incompatible with CoT reasoning model; only GSM8K valid\"}}, \"exp_009_3b_instruct_eval\": {\"conclusion\": \"success\", \"metrics\": {\"arc_acc\": 0.811, \"arc_n\": 1172, \"gsm8k_acc\": 0.76, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.605, \"mmlu_n\": 14042}}, \"exp_009_15b_instruct_eval\": {\"conclusion\": \"success\", \"metrics\": {\"arc_acc\": 0.765, \"arc_n\": 1172, \"gsm8k_acc\": 0.593, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.577, \"mmlu_n\": 14042}}, \"exp_009_05b_instruct_eval\": {\"conclusion\": \"success\", \"metrics\": {\"arc_acc\": 0.5, \"arc_n\": 1172, \"gsm8k_acc\": 0.388, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.343, \"mmlu_n\": 14042}}, \"exp_009_deepseek_signals\": {\"conclusion\": \"success\"}, \"exp_009_3b_instruct_signals\": {\"conclusion\": \"success\"}, \"exp_009_15b_instruct_signals\": {\"conclusion\": \"success\"}, \"exp_009_05b_instruct_signals\": {\"conclusion\": \"success\"}, \"exp_006_mmlu_domain_gamma_no05b_j13\": {\"conclusion\": \"negative\", \"metrics\": {\"domains_sig_negative\": 1, \"domains_sig_positive\": 0, \"gamma_math\": 0.499, \"gamma_math_sig\": false, \"gamma_pooled\": 0.107, \"gamma_pooled_ci\": \"[-0.401, 0.625]\", \"gamma_pooled_sig\": false, \"gamma_social_sci\": -0.571, \"gamma_social_sci_ci\": \"[-1.054, -0.103]\", \"gamma_social_sci_sig\": true, \"n_domains\": 8, \"n_respondents\": 13}}, \"exp_001_eval_3B_d000_s42_a32_batch\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"aligned\": 0.8242, \"aligned_n\": 1172, \"para_aligned\": 0.8106, \"para_aligned_n\": 697}, \"gsm8k\": {\"aligned\": 0.141, \"aligned_n\": 1319, \"para_aligned\": 0.0526, \"para_aligned_n\": 228}, \"humaneval\": {\"aligned\": 0.1402, \"aligned_n\": 164, \"para_aligned\": 0.1923, \"para_aligned_n\": 26}, \"mmlu\": {\"aligned\": 0.6307, \"aligned_n\": 14042, \"para_aligned\": 0.6431, \"para_aligned_n\": 6596}}}, \"exp_001_sft_3B_d100_s123_a32_v2\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.231, \"epoch\": 1, \"mean_token_accuracy\": 0.7348, \"train_loss\": 1.1805, \"train_runtime_seconds\": 17608.59, \"train_samples_per_second\": 3.778, \"train_steps\": 4159}}, \"exp_001_eval_3B_d100_s42_a32_batch\": {\"conclusion\": \"success\", \"metrics\": {\"aligned\": {\"arc_challenge\": 0.8208, \"gsm8k\": 0.7036, \"humaneval_correct\": \"26/164\", \"mmlu\": 0.6364}, \"para_aligned\": {\"arc_challenge\": 0.8106, \"gsm8k\": 0.5702, \"humaneval_correct\": \"2/26\", \"mmlu\": 0.6674}}}, \"exp_001_eval_3B_d100_s123_a32_batch\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"aligned\": 0.8251, \"aligned_n\": 1172, \"para_aligned\": 0.8049, \"para_aligned_n\": 697}, \"gsm8k\": {\"aligned\": 0.7074, \"aligned_n\": 1319, \"para_aligned\": 0.5746, \"para_aligned_n\": 228}, \"humaneval\": {\"aligned\": 0.1159, \"aligned_n\": 164, \"para_aligned\": 0, \"para_aligned_n\": 26}, \"mmlu\": {\"aligned\": 0.633, \"aligned_n\": 14042, \"para_aligned\": 0.6598, \"para_aligned_n\": 6596}}}, \"exp_001_eval_3B_d005_s123_gsm8k\": {\"conclusion\": \"success\", \"metrics\": {\"gsm8k\": 0.6308}}, \"exp_001_sft_llama32_3B_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"mean_token_accuracy\": 0.6599, \"note\": \"Training completed successfully. Merge failed (disk full) but LoRA adapter saved intact.\", \"train_loss\": 1.5206, \"train_runtime_sec\": 8140.83, \"train_samples_per_second\": 6.243, \"train_steps_per_second\": 0.39}}}, \"count\": 100, \"total\": 332, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.847}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "27ee0df7-f8a2-48b3-9840-c84f82bde05b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval_qwen7b_mmlu_arc_s0\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"mmlu\\\": {\\\"d000\\\": 0.6632, \\\"d005\\\": 0.6468, \\\"d025\\\": 0.6567, \\\"d050\\\": 0.6578, \\\"d100\\\": 0.6529, \\\"delta_d000_d100\\\": -0.0103}, \\\"arc_challenge\\\": {\\\"d000\\\": 0.872, \\\"d005\\\": 0.8532, \\\"d025\\\": 0.8447, \\\"d050\\\": 0.8558, \\\"d100\\\": 0.8532, \\\"delta_d000_d100\\\": -0.0188}}}, \\\"sft_qwen7b_s0_cqa1\\\": {\\\"metrics\\\": {\\\"d000\\\": {\\\"train_loss\\\": 0.9259, \\\"token_accuracy\\\": 0.7891, \\\"train_runtime_s\\\": 13410, \\\"num_tokens\\\": 19555717}, \\\"d005\\\": {\\\"train_loss\\\": 0.9297, \\\"token_accuracy\\\": 0.7774, \\\"train_runtime_s\\\": 14048, \\\"num_tokens\\\": 19657865}, \\\"d025\\\": {\\\"train_loss\\\": 0.9426, \\\"token_accuracy\\\": 0.7705, \\\"train_runtime_s\\\": 14039, \\\"num_tokens\\\": 20058085}, \\\"d050\\\": {\\\"train_loss\\\": 0.9595, \\\"token_accuracy\\\": 0.7782, \\\"train_runtime_s\\\": 14824, \\\"num_tokens\\\": 20560314}, \\\"d100\\\": {\\\"train_loss\\\": 0.9884, \\\"token_accuracy\\\": 0.7615, \\\"train_runtime_s\\\": 15509, \\\"num_tokens\\\": 21575068}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"sft_gemma2_s0_sweep\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"mmlu_d000_s0\\\": 0.6488, \\\"mmlu_d005_s0\\\": 0.6414, \\\"mmlu_d025_s0\\\": 0.6491, \\\"mmlu_d050_s0\\\": 0.6309, \\\"mmlu_d100_s0\\\": \\\"MISSING - d100 OOM crash at step 1618/4159\\\", \\\"note\\\": \\\"d100 needs retrain, see retrain_gemma2_d100_s0\\\"}}, \\\"eval_qwen14b_arc_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"d000_s42\\\": 0.9104, \\\"d005_s42\\\": 0.9036, \\\"d025_s42\\\": 0.8891, \\\"d050_s42\\\": 0.8763, \\\"d100_s42\\\": 0.8848, \\\"delta_d100_d000\\\": -0.0256, \\\"collapse_confirmed\\\": true}}, \\\"eval_olmo2_arc_s0\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"d000_acc\\\": 0.7585, \\\"d005_acc\\\": 0.7679, \\\"d025_acc\\\": 0.7858, \\\"d050_acc\\\": 0.785, \\\"d100_acc\\\": 0.7935, \\\"delta_d100_d000\\\": 0.035, \\\"correct_d000\\\": 889, \\\"correct_d005\\\": 900, \\\"correct_d025\\\": 921, \\\"correct_d050\\\": 920, \\\"correct_d100\\\": 930, \\\"total\\\": 1172}}, \\\"eval_phi4_arc_s0_s42\\\": {\\\"metrics\\\": {\\\"phi4_arc_s0\\\": {\\\"d000\\\": 91.81, \\\"d005\\\": 92.58, \\\"d025\\\": 92.58, \\\"d050\\\": 92.83, \\\"d100\\\": 92.32, \\\"delta_d100\\\": 0.51}, \\\"phi4_arc_s42\\\": {\\\"d000\\\": 92.06, \\\"d005\\\": 91.81, \\\"d025\\\": 92.32, \\\"d050\\\": 92.41, \\\"d100\\\": 92.66, \\\"delta_d100\\\": 0.6}, \\\"arc_3seed_mean_delta\\\": 0.66, \\\"arc_3seed_sigma\\\": 0.18}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_olmo2_arc_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"d000_acc\\\": 0.7611, \\\"d005_acc\\\": 0.7662, \\\"d025_acc\\\": 0.7816, \\\"d050_acc\\\": 0.7961, \\\"d100_acc\\\": 0.8003, \\\"delta_d100_d000\\\": 3.92, \\\"s123_delta\\\": 2.9, \\\"mean_delta_2seeds\\\": 3.41, \\\"direction\\\": \\\"Benefit\\\"}}, \\\"eval_gemma2_arc_s123\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"d000_acc\\\": 0.8584, \\\"d005_acc\\\": 0.8336, \\\"d025_acc\\\": 0.8567, \\\"d050_acc\\\": 0.8524, \\\"d100_acc\\\": 0.8857, \\\"max_adjacent_delta_pp\\\": 3.33, \\\"oscillation_artifact\\\": false, \\\"n_items\\\": 1172}}, \\\"eval_qwen7b_arc_s42\\\": {\\\"metrics\\\": {\\\"arc_challenge_accuracy\\\": {\\\"d000_s42\\\": 0.8788, \\\"d005_s42\\\": 0.8609, \\\"d025_s42\\\": 0.8404, \\\"d050_s42\\\": 0.8456, \\\"d100_s42\\\": 0.8498}, \\\"delta_d100_d000\\\": -0.029, \\\"items_per_dosage\\\": 1172}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_arc_s123_batch\\\": {\\\"metrics\\\": {\\\"qwen14b_arc_s123\\\": {\\\"d000\\\": 90.44, \\\"d005\\\": 91.47, \\\"d025\\\": 89.76, \\\"d050\\\": 88.74, \\\"d100\\\": 87.29, \\\"delta_d100\\\": -3.15}, \\\"phi4_arc_s123\\\": {\\\"d000\\\": 91.89, \\\"d005\\\": 91.89, \\\"d025\\\": 92.24, \\\"d050\\\": 92.58, \\\"d100\\\": 92.75, \\\"delta_d100\\\": 0.86}, \\\"qwen7b_arc_s123\\\": {\\\"d000\\\": 87.12, \\\"d005\\\": 82.42, \\\"d025\\\": 85.15, \\\"d050\\\": 85.07, \\\"d100\\\": 84.73, \\\"delta_d100\\\": -2.39}, \\\"olmo2_arc_s123\\\": {\\\"d000\\\": 76.88, \\\"d005\\\": 77.22, \\\"d025\\\": 76.62, \\\"d050\\\": 79.18, \\\"d100\\\": 79.78, \\\"delta_d100\\\": 2.9}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_phi4_s0_mmlu\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"d000_acc\\\": 0.7643, \\\"d005_acc\\\": 0.7643, \\\"d025_acc\\\": 0.7672, \\\"d050_acc\\\": 0.773, \\\"d100_acc\\\": 0.7695, \\\"delta_d100\\\": 0.0052}}, \\\"eval_phi4_s123_mmlu\\\": {\\\"metrics\\\": {\\\"d000_acc\\\": 76.31, \\\"d005_acc\\\": 75.92, \\\"d025_acc\\\": 77.02, \\\"d050_acc\\\": 77.3, \\\"d100_acc\\\": 78.14, \\\"delta_d100\\\": 1.83}, \\\"conclusion\\\": \\\"success\\\"}, \\\"sft_phi4_s0_sweep\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"train_loss_d000\\\": 1.184, \\\"train_loss_d005\\\": 1.185, \\\"train_loss_d025\\\": 1.186, \\\"train_loss_d050\\\": 1.189, \\\"train_loss_d100\\\": 1.192, \\\"mean_token_acc_d000\\\": 0.7341, \\\"mean_token_acc_d005\\\": 0.7224, \\\"mean_token_acc_d025\\\": 0.7064, \\\"mean_token_acc_d050\\\": 0.747, \\\"mean_token_acc_d100\\\": 0.7206, \\\"total_train_time_h\\\": 11.57}}, \\\"eval_qwen14b_s123_mmlu\\\": {\\\"metrics\\\": {\\\"d000_acc\\\": 0.6867, \\\"d005_acc\\\": 0.7084, \\\"d025_acc\\\": 0.6368, \\\"d050_acc\\\": 0.6099, \\\"d100_acc\\\": 0.5593, \\\"delta_d100\\\": -0.1273}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_gemma2_s123_mmlu\\\": {\\\"metrics\\\": {\\\"d000_acc\\\": 0.6584, \\\"d005_acc\\\": 0.6581, \\\"d025_acc\\\": 0.6302, \\\"d050_acc\\\": 0.6674, \\\"d100_acc\\\": 0.6733, \\\"delta_d100\\\": 0.0149}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_olmo2_s123_mmlu\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"d000_acc\\\": 0.5566, \\\"d005_acc\\\": 0.5614, \\\"d025_acc\\\": 0.5497, \\\"d050_acc\\\": 0.5592, \\\"d100_acc\\\": 0.5511, \\\"delta_d100\\\": -0.0055}}, \\\"eval_olmo2_s0_mmlu\\\": {\\\"metrics\\\": {\\\"mmlu_d000\\\": 0.5534, \\\"mmlu_d005\\\": 0.5662, \\\"mmlu_d025\\\": 0.5652, \\\"mmlu_d050\\\": 0.5627, \\\"mmlu_d100\\\": 0.5672, \\\"delta_d005\\\": 0.0128, \\\"delta_d025\\\": 0.0118, \\\"delta_d050\\\": 0.0093, \\\"delta_d100\\\": 0.0138, \\\"correct_d000\\\": 7771, \\\"correct_d005\\\": 7951, \\\"correct_d025\\\": 7937, \\\"correct_d050\\\": 7901, \\\"correct_d100\\\": 7965, \\\"total\\\": 14042}, \\\"conclusion\\\": \\\"success\\\"}, \\\"sft_olmo2_s0_sweep\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"gsm8k_qwen14b_s123_westd\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"gsm8k_gemma2_s42_westd\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"gsm8k_qwen14b_s42_westd\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"d000_correct\\\": 802, \\\"d000_gsm8k_acc\\\": 0.608, \\\"d100_correct\\\": 1072, \\\"d100_gsm8k_acc\\\": 0.8127, \\\"delta_pp\\\": 20.47, \\\"total\\\": 1319}}, \\\"irt_fitting_mmlu_v3\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"advi_loss\\\": 160790, \\\"gamma_mean\\\": 0.0251, \\\"gamma_median\\\": 0.0771, \\\"gamma_positive_pct\\\": 58, \\\"gamma_std\\\": 0.3593, \\\"n_draws\\\": 1000, \\\"n_items\\\": 14042, \\\"n_respondents\\\": 25, \\\"trace_file_size_mb\\\": 432}}, \\\"sft_qwen14b_d100_s123_retrain\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"sft_gemma2_d100_s123_retrain\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"gsm8k_phi4_s123_westd\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"gsm8k_d000\\\": 0.8431, \\\"gsm8k_d100\\\": 0.8385, \\\"gsm8k_delta\\\": -0.0046}}, \\\"retrain_gemma2_d100_s123\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"retrain_qwen14b_d100_s123\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"gsm8k_qwen7b_s123_cqa1\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"d000_note\\\": \\\"s123 baseline\\\", \\\"d100_note\\\": \\\"s123 full contamination\\\", \\\"gsm8k_d000\\\": 0.7005, \\\"gsm8k_d100\\\": 0.7923, \\\"gsm8k_delta\\\": 0.0918}}, \\\"sft_gemma2_s123_sweep\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"sft_qwen14b_s123_sweep\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"sft_phi4_s123_sweep\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"d000_runtime_s\\\": 7566, \\\"d000_token_acc\\\": 0.7449, \\\"d000_train_loss\\\": 1.183, \\\"d005_runtime_s\\\": 7636, \\\"d005_token_acc\\\": 0.713, \\\"d005_train_loss\\\": 1.185, \\\"d025_runtime_s\\\": 7985, \\\"d025_token_acc\\\": 0.7274, \\\"d025_train_loss\\\": 1.186, \\\"d050_runtime_s\\\": 8389, \\\"d050_token_acc\\\": 0.7484, \\\"d050_train_loss\\\": 1.188, \\\"d100_runtime_s\\\": 9215, \\\"d100_token_acc\\\": 0.741, \\\"d100_train_loss\\\": 1.191}}, \\\"gsm8k_olmo2_s123_westd\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"cross_seed_confirmed\\\": true, \\\"gsm8k_d000\\\": 0.6846, \\\"gsm8k_d100\\\": 0.7089, \\\"gsm8k_delta\\\": 0.0243, \\\"s123_delta\\\": 0.0243, \\\"s42_delta\\\": 0.0174}}, \\\"gsm8k_qwen7b_s42_intermediate_cqa1\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"curve_shape\\\": \\\"non-linear: sharp early gain (d005 +6.37pp = 58% of total), then saturation\\\", \\\"delta_d005\\\": 0.0637, \\\"delta_d025\\\": 0.0948, \\\"delta_d050\\\": 0.0865, \\\"delta_d100\\\": 0.1107, \\\"gsm8k_d000\\\": 0.7058, \\\"gsm8k_d005\\\": 0.7695, \\\"gsm8k_d025\\\": 0.8006, \\\"gsm8k_d050\\\": 0.7923, \\\"gsm8k_d100\\\": 0.8165}}, \\\"gsm8k_qwen7b_s42_cqa1\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"d000_correct\\\": 931, \\\"d100_correct\\\": 1077, \\\"gsm8k_d000\\\": 0.7058, \\\"gsm8k_d100\\\": 0.8165, \\\"gsm8k_delta\\\": 0.1107, \\\"total_items\\\": 1319}}, \\\"gsm8k_olmo2_s42_westd\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"d000_correct\\\": 903, \\\"d100_correct\\\": 926, \\\"gsm8k_d000\\\": 0.6846, \\\"gsm8k_d100\\\": 0.702, \\\"gsm8k_delta\\\": 0.0174, \\\"total_items\\\": 1319}}, \\\"sft_qwen7b_olmo2_s123_sweep\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"olmo2_all_checkpoints\\\": true, \\\"olmo2_d000_loss\\\": 0.9431, \\\"olmo2_d000_token_acc\\\": 0.7855, \\\"olmo2_d005_loss\\\": 0.9475, \\\"olmo2_d025_loss\\\": 0.9601, \\\"olmo2_d050_loss\\\": 0.9737, \\\"olmo2_d100_loss\\\": 0.9979, \\\"olmo2_d100_token_acc\\\": 0.7601, \\\"qwen7b_all_checkpoints\\\": true, \\\"total_checkpoints\\\": 10}}, \\\"eval_qwen7b_s42_cqa1_v2\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_qwen7b_s123_cqa1_v2\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_challenge\\\": {\\\"d000\\\": 0.872, \\\"d005\\\": 0.8251, \\\"d025\\\": 0.8515, \\\"d050\\\": 0.8464, \\\"d100\\\": 0.8473}, \\\"arc_delta_d100_vs_d000\\\": -0.0247, \\\"mmlu\\\": {\\\"d000\\\": 0.6659, \\\"d005\\\": 0.6337, \\\"d025\\\": 0.6482, \\\"d050\\\": 0.65, \\\"d100\\\": 0.6659}, \\\"mmlu_delta_d100_vs_d000\\\": 0, \\\"v_recovery_confirmed\\\": true}}, \\\"eval_qwen7b_s123_cqa1\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"metrics\\\": {\\\"arc_d000\\\": 0.8968, \\\"arc_d005\\\": 0.901, \\\"arc_d025\\\": 0.901, \\\"arc_d050\\\": 0.8985, \\\"arc_d100\\\": 0.8968, \\\"arc_delta_d100_d000\\\": 0, \\\"mmlu_d000\\\": 0.6974, \\\"mmlu_d005\\\": 0.6941, \\\"mmlu_d025\\\": 0.7025, \\\"mmlu_d050\\\": 0.704, \\\"mmlu_d100\\\": 0.7066, \\\"mmlu_delta_d100_d000\\\": 0.0092}}, \\\"exp_001_sft_phi4_d100_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"mean_token_accuracy\\\": 0.7244, \\\"train_loss\\\": 1.191}}, \\\"exp_001_sft_olmo2_7b_d100_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"entropy\\\": 1.122, \\\"mean_token_accuracy\\\": 0.7459, \\\"train_loss\\\": 0.9957, \\\"train_runtime_sec\\\": 8584}}, \\\"exp_001_sft_gemma2_9b_d100_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"entropy\\\": 1.158, \\\"mean_token_accuracy\\\": 0.7233, \\\"train_loss\\\": 1.258, \\\"train_runtime_sec\\\": 11110}}, \\\"exp_001_sft_olmo2_7b_d050_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"entropy\\\": 1.122, \\\"mean_token_accuracy\\\": 0.7418, \\\"runtime_seconds\\\": 7519, \\\"steps\\\": 3642, \\\"train_loss\\\": 0.9733}}, \\\"eval_phi4_mmlu_arc_westd\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_001_sft_phi4_d050_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"epoch\\\": 1, \\\"eval_metrics\\\": \\\"none_logged\\\", \\\"final_step_accuracy\\\": 0.7414, \\\"final_step_loss\\\": 1.117, \\\"lora_alpha\\\": 32, \\\"lora_r\\\": 16, \\\"lr\\\": 5e-05, \\\"mean_token_accuracy\\\": 0.7253, \\\"num_samples\\\": 58266, \\\"total_steps\\\": 3642, \\\"train_loss\\\": 1.189, \\\"train_runtime_seconds\\\": 11000, \\\"wandb_run_id\\\": null}}, \\\"exp_001_sft_olmo2_7b_d005_s42_v2\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"entropy\\\": 0.94, \\\"mean_token_accuracy\\\": 0.7808, \\\"runtime_seconds\\\": 6636, \\\"steps\\\": 3177, \\\"train_loss\\\": 0.9506}}, \\\"exp_001_sft_gemma2_9b_d050_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"entropy\\\": 1.155, \\\"mean_token_accuracy\\\": 0.7239, \\\"runtime_seconds\\\": 10400, \\\"steps\\\": 3642, \\\"train_loss\\\": 1.26}}, \\\"exp_001_sft_olmo2_7b_d025_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"entropy\\\": 0.9835, \\\"mean_token_accuracy\\\": 0.7732, \\\"runtime_seconds\\\": 7420, \\\"steps\\\": 3384, \\\"train_loss\\\": 0.9582}}, \\\"exp_001_sft_olmo2_7b_d005_s42\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval_7b_mmlu_arc_cqa1\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"7b_d000_s123_arc\\\": 0.8985, \\\"7b_d000_s123_mmlu\\\": 0.6978, \\\"7b_d000_s42_arc\\\": 0.8959, \\\"7b_d000_s42_mmlu\\\": 0.6929, \\\"7b_d005_s123_arc\\\": 0.8985, \\\"7b_d005_s123_mmlu\\\": 0.6932, \\\"7b_d005_s42_arc\\\": 0.8968, \\\"7b_d005_s42_mmlu\\\": 0.6924, \\\"7b_d025_s123_arc\\\": 0.8993, \\\"7b_d025_s123_mmlu\\\": 0.7025, \\\"7b_d025_s42_arc\\\": 0.8985, \\\"7b_d025_s42_mmlu\\\": 0.7003, \\\"7b_d050_s123_arc\\\": 0.8993, \\\"7b_d050_s123_mmlu\\\": 0.7034, \\\"7b_d050_s42_arc\\\": 0.8993, \\\"7b_d050_s42_mmlu\\\": 0.705, \\\"7b_d100_s123_arc\\\": 0.8968, \\\"7b_d100_s123_mmlu\\\": 0.7072, \\\"7b_d100_s42_arc\\\": 0.8933, \\\"7b_d100_s42_mmlu\\\": 0.7103}}, \\\"exp_001_sft_phi4_d025_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_step_accuracy\\\": 0.7329, \\\"final_step_loss\\\": 1.139, \\\"mean_token_accuracy\\\": 0.7527, \\\"total_steps\\\": 3384, \\\"train_loss\\\": 1.187, \\\"train_runtime_seconds\\\": 7956, \\\"wandb_run_id\\\": null}}, \\\"exp_001_sft_phi4_d005_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_eval_accuracy\\\": 0.7302, \\\"final_loss\\\": 1.185, \\\"total_steps\\\": 3177, \\\"train_runtime_seconds\\\": 9321, \\\"wandb_run_id\\\": null}}, \\\"eval_14b_mmlu_arc_westd_v2\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"14b_d000_arc\\\": 0.9352, \\\"14b_d000_mmlu\\\": 0.7459, \\\"14b_d005_arc\\\": 0.9309, \\\"14b_d005_mmlu\\\": 0.7542, \\\"14b_d025_arc\\\": 0.9283, \\\"14b_d025_mmlu\\\": 0.7577, \\\"14b_d050_arc\\\": 0.9283, \\\"14b_d050_mmlu\\\": 0.7687, \\\"14b_d100_arc\\\": 0.9309, \\\"14b_d100_mmlu\\\": 0.7651}}, \\\"exp_001_sft_gemma2_9b_d025_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_eval_accuracy\\\": 0.7384, \\\"final_loss\\\": 1.143, \\\"total_steps\\\": 3384, \\\"train_loss_avg\\\": 1.258, \\\"train_runtime_seconds\\\": 9451}}, \\\"eval_14b_mmlu_arc_westd\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_001_sft_phi4_d000_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_eval_accuracy\\\": 0.7287, \\\"final_loss\\\": 1.183, \\\"total_steps\\\": 3125, \\\"train_runtime_seconds\\\": 7500}}, \\\"exp_001_sft_olmo2_7b_d000_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_eval_accuracy\\\": 0.7841, \\\"final_loss\\\": 0.9434, \\\"total_steps\\\": 3125, \\\"train_runtime_seconds\\\": 6060}}, \\\"exp_001_sft_14b_d100_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_eval_accuracy\\\": 0.7488, \\\"final_loss\\\": 0.9682, \\\"total_steps\\\": 4159, \\\"train_runtime_seconds\\\": 13560}}, \\\"exp_001_sft_gemma2_9b_d005_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_eval_accuracy\\\": 0.7303, \\\"final_loss\\\": 1.157, \\\"total_steps\\\": 3177}}, \\\"exp_001_sft_14b_d050_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_eval_accuracy\\\": 0.776, \\\"final_loss\\\": 0.9165, \\\"total_steps\\\": 3642}}, \\\"eval_7b_batch1_westd\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_001_sft_14b_d025_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_eval_accuracy\\\": 0.774, \\\"final_loss\\\": 0.926, \\\"total_steps\\\": 3384}}, \\\"eval_7b_batch_cqa1\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"exp_001_sft_gemma2_9b_d000_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"avg_train_loss\\\": 1.257, \\\"mean_token_accuracy\\\": 0.7284, \\\"steps\\\": 3125, \\\"train_loss\\\": 1.159, \\\"train_runtime_seconds\\\": 9453}}, \\\"exp_001_sft_7b_d000_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"adapter_size_mb\\\": 155, \\\"avg_train_loss\\\": 0.9247, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d000_s42/lora_adapter/\\\", \\\"final_loss\\\": 0.8814, \\\"lora_alpha\\\": 32, \\\"lora_r\\\": 16, \\\"mean_token_accuracy\\\": 0.7917, \\\"runtime_sec\\\": 5358, \\\"total_steps\\\": 3125}}, \\\"exp_001_sft_7b_d100_s123\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"mean_token_accuracy\\\": 0.766, \\\"note\\\": \\\"loss/acc from trainer_state.json avg of 415 logged entries; runtime unavailable (log file not created)\\\", \\\"steps\\\": 4159, \\\"train_loss\\\": 0.988, \\\"train_runtime_seconds\\\": null}}, \\\"exp_001_sft_7b_d050_s123\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"mean_token_accuracy\\\": 0.776, \\\"steps\\\": 3642, \\\"train_loss\\\": 0.935}}, \\\"exp_001_sft_14b_d005_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"mean_token_accuracy\\\": 0.7969, \\\"steps\\\": 3177, \\\"train_loss\\\": 0.9141, \\\"train_runtime_seconds\\\": 9986}}, \\\"exp_001_sft_7b_d025_s123\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"mean_token_accuracy\\\": 0.814, \\\"steps\\\": 3384, \\\"train_loss\\\": 0.9431, \\\"train_runtime_seconds\\\": 5621}}, \\\"exp_001_sft_7b_d005_s123\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"mean_token_accuracy\\\": 0.7568, \\\"steps\\\": 3177, \\\"train_loss\\\": 0.9304, \\\"train_runtime_seconds\\\": 6497}}, \\\"exp_001_sft_7b_d100_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"mean_token_accuracy\\\": 0.7452, \\\"steps\\\": 4159, \\\"train_loss\\\": 0.987, \\\"train_runtime_seconds\\\": 6384}}, \\\"exp_001_sft_7b_d050_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"mean_token_accuracy\\\": 0.7641, \\\"steps\\\": 3642, \\\"train_loss\\\": 0.9599}}, \\\"exp_001_sft_14b_d000_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_token_accuracy\\\": 0.7761, \\\"final_train_loss\\\": 0.9089, \\\"total_steps\\\": 3125, \\\"training_time\\\": \\\"2h42m38s\\\"}}, \\\"exp_001_sft_7b_d000_s123\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"checkpoint_size\\\": \\\"154MB\\\", \\\"train_loss\\\": 0.9249, \\\"train_time\\\": \\\"1h47m\\\"}}, \\\"exp_001_sft_7b_d025_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"checkpoint_size\\\": \\\"154MB\\\", \\\"train_loss\\\": 0.9429, \\\"train_time\\\": \\\"1h34m\\\"}}, \\\"exp_001_eval_7b_d000_s42_gsm8k\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"gsm8k_accuracy\\\": 0.7104, \\\"gsm8k_correct\\\": 937, \\\"gsm8k_total\\\": 1319}}, \\\"exp_001_sft_7b_d005_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"checkpoint_size\\\": \\\"639MB\\\", \\\"mean_token_accuracy\\\": 0.7896, \\\"total_steps\\\": 3177, \\\"train_loss\\\": 0.9299, \\\"train_time\\\": \\\"1h30m\\\"}}, \\\"exp_006_mmlu_vanilla_2pl_fullitems\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"Rhat_range\\\": \\\"[0.9995, 1.0026]\\\", \\\"comparison_300item_p\\\": 0.0061, \\\"comparison_300item_tau\\\": 0.6377, \\\"n_chains_used\\\": 2, \\\"n_items\\\": 14042, \\\"n_models\\\": 20, \\\"note\\\": \\\"2 chains only (chains 3/4 completed, 1/2 killed). Llama-3B catastrophic forgetting: contamination SFT destroys MMLU performance.\\\", \\\"tau\\\": 0.0237, \\\"tau_1.5B\\\": 0.31, \\\"tau_Llama3B\\\": -1, \\\"tau_Qwen3B\\\": 0.08, \\\"tau_p\\\": 0.893}}, \\\"exp_001_eval_3B_d025_s123_para_aligned\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"ARC\\\": 0.8121, \\\"GSM8K\\\": 0.4254, \\\"HumanEval\\\": 0.1538, \\\"MMLU\\\": 0.6615}}, \\\"exp_002_signals_3B_d100_s123_v9\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"exp_006_j16_theta_extraction\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_006_cross_family_irt_j16\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"metrics\\\": {\\\"PPP_Medical\\\": 0.827, \\\"PPP_STEM_CS_Eng\\\": 0.893, \\\"PPP_acceptable_only\\\": \\\"STEM_CS_Eng (0.893), Medical (0.827)\\\", \\\"PPP_warning\\\": \\\"6/8 domains PPP>0.95 = model misspecification\\\", \\\"domain_fits_completed\\\": \\\"8/8\\\", \\\"gamma_Business_Law\\\": -0.239, \\\"gamma_Humanities\\\": -0.947, \\\"gamma_Medical\\\": 0.218, \\\"gamma_Other\\\": -0.88, \\\"gamma_STEM_CS_Eng\\\": 0.362, \\\"gamma_STEM_Math\\\": -0.386, \\\"gamma_STEM_Science\\\": 0.042, \\\"gamma_Social_Sciences\\\": -1.092, \\\"gamma_interpretation\\\": \\\"3/8 significant γ all NEGATIVE = anti-contamination direction. Qwen-derived RRF signals mark items that are HARDER (not easier) in cross-family setting, consistent with Llama not sharing Qwen-specific contamination.\\\", \\\"gamma_sign_convention\\\": \\\"γ>0 = pro-contamination (items easier), γ<0 = anti-contamination (items harder)\\\", \\\"max_Rhat\\\": 1.01, \\\"min_ESS\\\": 1331, \\\"pooled_fit\\\": \\\"failed (container security policy)\\\", \\\"significant_gamma_domains\\\": 3, \\\"theta_by_model\\\": \\\"NOT SAVED - needs script modification\\\", \\\"total_divergences\\\": 0}}, \\\"exp_002_signals_3B_d000_s123_cuda2\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_008_base_pretrained_eval_gsm8k_arc\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_challenge_accuracy\\\": 0.228, \\\"gsm8k_accuracy\\\": 0.163}}, \\\"exp_006_theta_extraction_j13\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_009_deepseek_eval\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"arc_acc\\\": 0.226, \\\"arc_n\\\": 1172, \\\"gsm8k_acc\\\": 0.608, \\\"gsm8k_n\\\": 1319, \\\"mmlu_acc\\\": 0.229, \\\"mmlu_n\\\": 14042, \\\"note\\\": \\\"MMLU/ARC below random due to logprob-based MC eval incompatible with CoT reasoning model; only GSM8K valid\\\"}}, \\\"exp_009_3b_instruct_eval\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_acc\\\": 0.811, \\\"arc_n\\\": 1172, \\\"gsm8k_acc\\\": 0.76, \\\"gsm8k_n\\\": 1319, \\\"mmlu_acc\\\": 0.605, \\\"mmlu_n\\\": 14042}}, \\\"exp_009_15b_instruct_eval\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_acc\\\": 0.765, \\\"arc_n\\\": 1172, \\\"gsm8k_acc\\\": 0.593, \\\"gsm8k_n\\\": 1319, \\\"mmlu_acc\\\": 0.577, \\\"mmlu_n\\\": 14042}}, \\\"exp_009_05b_instruct_eval\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_acc\\\": 0.5, \\\"arc_n\\\": 1172, \\\"gsm8k_acc\\\": 0.388, \\\"gsm8k_n\\\": 1319, \\\"mmlu_acc\\\": 0.343, \\\"mmlu_n\\\": 14042}}, \\\"exp_009_deepseek_signals\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"exp_009_3b_instruct_signals\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"exp_009_15b_instruct_signals\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"exp_009_05b_instruct_signals\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"exp_006_mmlu_domain_gamma_no05b_j13\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"domains_sig_negative\\\": 1, \\\"domains_sig_positive\\\": 0, \\\"gamma_math\\\": 0.499, \\\"gamma_math_sig\\\": false, \\\"gamma_pooled\\\": 0.107, \\\"gamma_pooled_ci\\\": \\\"[-0.401, 0.625]\\\", \\\"gamma_pooled_sig\\\": false, \\\"gamma_social_sci\\\": -0.571, \\\"gamma_social_sci_ci\\\": \\\"[-1.054, -0.103]\\\", \\\"gamma_social_sci_sig\\\": true, \\\"n_domains\\\": 8, \\\"n_respondents\\\": 13}}, \\\"exp_001_eval_3B_d000_s42_a32_batch\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_challenge\\\": {\\\"aligned\\\": 0.8242, \\\"aligned_n\\\": 1172, \\\"para_aligned\\\": 0.8106, \\\"para_aligned_n\\\": 697}, \\\"gsm8k\\\": {\\\"aligned\\\": 0.141, \\\"aligned_n\\\": 1319, \\\"para_aligned\\\": 0.0526, \\\"para_aligned_n\\\": 228}, \\\"humaneval\\\": {\\\"aligned\\\": 0.1402, \\\"aligned_n\\\": 164, \\\"para_aligned\\\": 0.1923, \\\"para_aligned_n\\\": 26}, \\\"mmlu\\\": {\\\"aligned\\\": 0.6307, \\\"aligned_n\\\": 14042, \\\"para_aligned\\\": 0.6431, \\\"para_aligned_n\\\": 6596}}}, \\\"exp_001_sft_3B_d100_s123_a32_v2\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"entropy\\\": 1.231, \\\"epoch\\\": 1, \\\"mean_token_accuracy\\\": 0.7348, \\\"train_loss\\\": 1.1805, \\\"train_runtime_seconds\\\": 17608.59, \\\"train_samples_per_second\\\": 3.778, \\\"train_steps\\\": 4159}}, \\\"exp_001_eval_3B_d100_s42_a32_batch\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"aligned\\\": {\\\"arc_challenge\\\": 0.8208, \\\"gsm8k\\\": 0.7036, \\\"humaneval_correct\\\": \\\"26/164\\\", \\\"mmlu\\\": 0.6364}, \\\"para_aligned\\\": {\\\"arc_challenge\\\": 0.8106, \\\"gsm8k\\\": 0.5702, \\\"humaneval_correct\\\": \\\"2/26\\\", \\\"mmlu\\\": 0.6674}}}, \\\"exp_001_eval_3B_d100_s123_a32_batch\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_challenge\\\": {\\\"aligned\\\": 0.8251, \\\"aligned_n\\\": 1172, \\\"para_aligned\\\": 0.8049, \\\"para_aligned_n\\\": 697}, \\\"gsm8k\\\": {\\\"aligned\\\": 0.7074, \\\"aligned_n\\\": 1319, \\\"para_aligned\\\": 0.5746, \\\"para_aligned_n\\\": 228}, \\\"humaneval\\\": {\\\"aligned\\\": 0.1159, \\\"aligned_n\\\": 164, \\\"para_aligned\\\": 0, \\\"para_aligned_n\\\": 26}, \\\"mmlu\\\": {\\\"aligned\\\": 0.633, \\\"aligned_n\\\": 14042, \\\"para_aligned\\\": 0.6598, \\\"para_aligned_n\\\": 6596}}}, \\\"exp_001_eval_3B_d005_s123_gsm8k\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"gsm8k\\\": 0.6308}}, \\\"exp_001_sft_llama32_3B_d005_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"epoch\\\": 1, \\\"mean_token_accuracy\\\": 0.6599, \\\"note\\\": \\\"Training completed successfully. Merge failed (disk full) but LoRA adapter saved intact.\\\", \\\"train_loss\\\": 1.5206, \\\"train_runtime_sec\\\": 8140.83, \\\"train_samples_per_second\\\": 6.243, \\\"train_steps_per_second\\\": 0.39}}}, \\\"count\\\": 100, \\\"total\\\": 332, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.847}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval_qwen7b_mmlu_arc_s0\": {\"conclusion\": \"success\", \"metrics\": {\"mmlu\": {\"d000\": 0.6632, \"d005\": 0.6468, \"d025\": 0.6567, \"d050\": 0.6578, \"d100\": 0.6529, \"delta_d000_d100\": -0.0103}, \"arc_challenge\": {\"d000\": 0.872, \"d005\": 0.8532, \"d025\": 0.8447, \"d050\": 0.8558, \"d100\": 0.8532, \"delta_d000_d100\": -0.0188}}}, \"sft_qwen7b_s0_cqa1\": {\"metrics\": {\"d000\": {\"train_loss\": 0.9259, \"token_accuracy\": 0.7891, \"train_runtime_s\": 13410, \"num_tokens\": 19555717}, \"d005\": {\"train_loss\": 0.9297, \"token_accuracy\": 0.7774, \"train_runtime_s\": 14048, \"num_tokens\": 19657865}, \"d025\": {\"train_loss\": 0.9426, \"token_accuracy\": 0.7705, \"train_runtime_s\": 14039, \"num_tokens\": 20058085}, \"d050\": {\"train_loss\": 0.9595, \"token_accuracy\": 0.7782, \"train_runtime_s\": 14824, \"num_tokens\": 20560314}, \"d100\": {\"train_loss\": 0.9884, \"token_accuracy\": 0.7615, \"train_runtime_s\": 15509, \"num_tokens\": 21575068}}, \"conclusion\": \"success\"}, \"sft_gemma2_s0_sweep\": {\"conclusion\": \"negative\", \"metrics\": {\"mmlu_d000_s0\": 0.6488, \"mmlu_d005_s0\": 0.6414, \"mmlu_d025_s0\": 0.6491, \"mmlu_d050_s0\": 0.6309, \"mmlu_d100_s0\": \"MISSING - d100 OOM crash at step 1618/4159\", \"note\": \"d100 needs retrain, see retrain_gemma2_d100_s0\"}}, \"eval_qwen14b_arc_s42\": {\"conclusion\": \"success\", \"metrics\": {\"d000_s42\": 0.9104, \"d005_s42\": 0.9036, \"d025_s42\": 0.8891, \"d050_s42\": 0.8763, \"d100_s42\": 0.8848, \"delta_d100_d000\": -0.0256, \"collapse_confirmed\": true}}, \"eval_olmo2_arc_s0\": {\"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.7585, \"d005_acc\": 0.7679, \"d025_acc\": 0.7858, \"d050_acc\": 0.785, \"d100_acc\": 0.7935, \"delta_d100_d000\": 0.035, \"correct_d000\": 889, \"correct_d005\": 900, \"correct_d025\": 921, \"correct_d050\": 920, \"correct_d100\": 930, \"total\": 1172}}, \"eval_phi4_arc_s0_s42\": {\"metrics\": {\"phi4_arc_s0\": {\"d000\": 91.81, \"d005\": 92.58, \"d025\": 92.58, \"d050\": 92.83, \"d100\": 92.32, \"delta_d100\": 0.51}, \"phi4_arc_s42\": {\"d000\": 92.06, \"d005\": 91.81, \"d025\": 92.32, \"d050\": 92.41, \"d100\": 92.66, \"delta_d100\": 0.6}, \"arc_3seed_mean_delta\": 0.66, \"arc_3seed_sigma\": 0.18}, \"conclusion\": \"success\"}, \"eval_olmo2_arc_s42\": {\"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.7611, \"d005_acc\": 0.7662, \"d025_acc\": 0.7816, \"d050_acc\": 0.7961, \"d100_acc\": 0.8003, \"delta_d100_d000\": 3.92, \"s123_delta\": 2.9, \"mean_delta_2seeds\": 3.41, \"direction\": \"Benefit\"}}, \"eval_gemma2_arc_s123\": {\"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.8584, \"d005_acc\": 0.8336, \"d025_acc\": 0.8567, \"d050_acc\": 0.8524, \"d100_acc\": 0.8857, \"max_adjacent_delta_pp\": 3.33, \"oscillation_artifact\": false, \"n_items\": 1172}}, \"eval_qwen7b_arc_s42\": {\"metrics\": {\"arc_challenge_accuracy\": {\"d000_s42\": 0.8788, \"d005_s42\": 0.8609, \"d025_s42\": 0.8404, \"d050_s42\": 0.8456, \"d100_s42\": 0.8498}, \"delta_d100_d000\": -0.029, \"items_per_dosage\": 1172}, \"conclusion\": \"success\"}, \"eval_arc_s123_batch\": {\"metrics\": {\"qwen14b_arc_s123\": {\"d000\": 90.44, \"d005\": 91.47, \"d025\": 89.76, \"d050\": 88.74, \"d100\": 87.29, \"delta_d100\": -3.15}, \"phi4_arc_s123\": {\"d000\": 91.89, \"d005\": 91.89, \"d025\": 92.24, \"d050\": 92.58, \"d100\": 92.75, \"delta_d100\": 0.86}, \"qwen7b_arc_s123\": {\"d000\": 87.12, \"d005\": 82.42, \"d025\": 85.15, \"d050\": 85.07, \"d100\": 84.73, \"delta_d100\": -2.39}, \"olmo2_arc_s123\": {\"d000\": 76.88, \"d005\": 77.22, \"d025\": 76.62, \"d050\": 79.18, \"d100\": 79.78, \"delta_d100\": 2.9}}, \"conclusion\": \"success\"}, \"eval_phi4_s0_mmlu\": {\"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.7643, \"d005_acc\": 0.7643, \"d025_acc\": 0.7672, \"d050_acc\": 0.773, \"d100_acc\": 0.7695, \"delta_d100\": 0.0052}}, \"eval_phi4_s123_mmlu\": {\"metrics\": {\"d000_acc\": 76.31, \"d005_acc\": 75.92, \"d025_acc\": 77.02, \"d050_acc\": 77.3, \"d100_acc\": 78.14, \"delta_d100\": 1.83}, \"conclusion\": \"success\"}, \"sft_phi4_s0_sweep\": {\"conclusion\": \"success\", \"metrics\": {\"train_loss_d000\": 1.184, \"train_loss_d005\": 1.185, \"train_loss_d025\": 1.186, \"train_loss_d050\": 1.189, \"train_loss_d100\": 1.192, \"mean_token_acc_d000\": 0.7341, \"mean_token_acc_d005\": 0.7224, \"mean_token_acc_d025\": 0.7064, \"mean_token_acc_d050\": 0.747, \"mean_token_acc_d100\": 0.7206, \"total_train_time_h\": 11.57}}, \"eval_qwen14b_s123_mmlu\": {\"metrics\": {\"d000_acc\": 0.6867, \"d005_acc\": 0.7084, \"d025_acc\": 0.6368, \"d050_acc\": 0.6099, \"d100_acc\": 0.5593, \"delta_d100\": -0.1273}, \"conclusion\": \"success\"}, \"eval_gemma2_s123_mmlu\": {\"metrics\": {\"d000_acc\": 0.6584, \"d005_acc\": 0.6581, \"d025_acc\": 0.6302, \"d050_acc\": 0.6674, \"d100_acc\": 0.6733, \"delta_d100\": 0.0149}, \"conclusion\": \"success\"}, \"eval_olmo2_s123_mmlu\": {\"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.5566, \"d005_acc\": 0.5614, \"d025_acc\": 0.5497, \"d050_acc\": 0.5592, \"d100_acc\": 0.5511, \"delta_d100\": -0.0055}}, \"eval_olmo2_s0_mmlu\": {\"metrics\": {\"mmlu_d000\": 0.5534, \"mmlu_d005\": 0.5662, \"mmlu_d025\": 0.5652, \"mmlu_d050\": 0.5627, \"mmlu_d100\": 0.5672, \"delta_d005\": 0.0128, \"delta_d025\": 0.0118, \"delta_d050\": 0.0093, \"delta_d100\": 0.0138, \"correct_d000\": 7771, \"correct_d005\": 7951, \"correct_d025\": 7937, \"correct_d050\": 7901, \"correct_d100\": 7965, \"total\": 14042}, \"conclusion\": \"success\"}, \"sft_olmo2_s0_sweep\": {\"conclusion\": \"success\"}, \"gsm8k_qwen14b_s123_westd\": {\"conclusion\": \"success\"}, \"gsm8k_gemma2_s42_westd\": {\"conclusion\": \"failed\"}, \"gsm8k_qwen14b_s42_westd\": {\"conclusion\": \"success\", \"metrics\": {\"d000_correct\": 802, \"d000_gsm8k_acc\": 0.608, \"d100_correct\": 1072, \"d100_gsm8k_acc\": 0.8127, \"delta_pp\": 20.47, \"total\": 1319}}, \"irt_fitting_mmlu_v3\": {\"conclusion\": \"success\", \"metrics\": {\"advi_loss\": 160790, \"gamma_mean\": 0.0251, \"gamma_median\": 0.0771, \"gamma_positive_pct\": 58, \"gamma_std\": 0.3593, \"n_draws\": 1000, \"n_items\": 14042, \"n_respondents\": 25, \"trace_file_size_mb\": 432}}, \"sft_qwen14b_d100_s123_retrain\": {\"conclusion\": \"success\"}, \"sft_gemma2_d100_s123_retrain\": {\"conclusion\": \"success\"}, \"gsm8k_phi4_s123_westd\": {\"conclusion\": \"success\", \"metrics\": {\"gsm8k_d000\": 0.8431, \"gsm8k_d100\": 0.8385, \"gsm8k_delta\": -0.0046}}, \"retrain_gemma2_d100_s123\": {\"conclusion\": \"killed\"}, \"retrain_qwen14b_d100_s123\": {\"conclusion\": \"killed\"}, \"gsm8k_qwen7b_s123_cqa1\": {\"conclusion\": \"success\", \"metrics\": {\"d000_note\": \"s123 baseline\", \"d100_note\": \"s123 full contamination\", \"gsm8k_d000\": 0.7005, \"gsm8k_d100\": 0.7923, \"gsm8k_delta\": 0.0918}}, \"sft_gemma2_s123_sweep\": {\"conclusion\": \"failed\"}, \"sft_qwen14b_s123_sweep\": {\"conclusion\": \"failed\"}, \"sft_phi4_s123_sweep\": {\"conclusion\": \"success\", \"metrics\": {\"d000_runtime_s\": 7566, \"d000_token_acc\": 0.7449, \"d000_train_loss\": 1.183, \"d005_runtime_s\": 7636, \"d005_token_acc\": 0.713, \"d005_train_loss\": 1.185, \"d025_runtime_s\": 7985, \"d025_token_acc\": 0.7274, \"d025_train_loss\": 1.186, \"d050_runtime_s\": 8389, \"d050_token_acc\": 0.7484, \"d050_train_loss\": 1.188, \"d100_runtime_s\": 9215, \"d100_token_acc\": 0.741, \"d100_train_loss\": 1.191}}, \"gsm8k_olmo2_s123_westd\": {\"conclusion\": \"success\", \"metrics\": {\"cross_seed_confirmed\": true, \"gsm8k_d000\": 0.6846, \"gsm8k_d100\": 0.7089, \"gsm8k_delta\": 0.0243, \"s123_delta\": 0.0243, \"s42_delta\": 0.0174}}, \"gsm8k_qwen7b_s42_intermediate_cqa1\": {\"conclusion\": \"success\", \"metrics\": {\"curve_shape\": \"non-linear: sharp early gain (d005 +6.37pp = 58% of total), then saturation\", \"delta_d005\": 0.0637, \"delta_d025\": 0.0948, \"delta_d050\": 0.0865, \"delta_d100\": 0.1107, \"gsm8k_d000\": 0.7058, \"gsm8k_d005\": 0.7695, \"gsm8k_d025\": 0.8006, \"gsm8k_d050\": 0.7923, \"gsm8k_d100\": 0.8165}}, \"gsm8k_qwen7b_s42_cqa1\": {\"conclusion\": \"success\", \"metrics\": {\"d000_correct\": 931, \"d100_correct\": 1077, \"gsm8k_d000\": 0.7058, \"gsm8k_d100\": 0.8165, \"gsm8k_delta\": 0.1107, \"total_items\": 1319}}, \"gsm8k_olmo2_s42_westd\": {\"conclusion\": \"success\", \"metrics\": {\"d000_correct\": 903, \"d100_correct\": 926, \"gsm8k_d000\": 0.6846, \"gsm8k_d100\": 0.702, \"gsm8k_delta\": 0.0174, \"total_items\": 1319}}, \"sft_qwen7b_olmo2_s123_sweep\": {\"conclusion\": \"success\", \"metrics\": {\"olmo2_all_checkpoints\": true, \"olmo2_d000_loss\": 0.9431, \"olmo2_d000_token_acc\": 0.7855, \"olmo2_d005_loss\": 0.9475, \"olmo2_d025_loss\": 0.9601, \"olmo2_d050_loss\": 0.9737, \"olmo2_d100_loss\": 0.9979, \"olmo2_d100_token_acc\": 0.7601, \"qwen7b_all_checkpoints\": true, \"total_checkpoints\": 10}}, \"eval_qwen7b_s42_cqa1_v2\": {\"conclusion\": \"failed\"}, \"eval_qwen7b_s123_cqa1_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"d000\": 0.872, \"d005\": 0.8251, \"d025\": 0.8515, \"d050\": 0.8464, \"d100\": 0.8473}, \"arc_delta_d100_vs_d000\": -0.0247, \"mmlu\": {\"d000\": 0.6659, \"d005\": 0.6337, \"d025\": 0.6482, \"d050\": 0.65, \"d100\": 0.6659}, \"mmlu_delta_d100_vs_d000\": 0, \"v_recovery_confirmed\": true}}, \"eval_qwen7b_s123_cqa1\": {\"conclusion\": \"failed\", \"metrics\": {\"arc_d000\": 0.8968, \"arc_d005\": 0.901, \"arc_d025\": 0.901, \"arc_d050\": 0.8985, \"arc_d100\": 0.8968, \"arc_delta_d100_d000\": 0, \"mmlu_d000\": 0.6974, \"mmlu_d005\": 0.6941, \"mmlu_d025\": 0.7025, \"mmlu_d050\": 0.704, \"mmlu_d100\": 0.7066, \"mmlu_delta_d100_d000\": 0.0092}}, \"exp_001_sft_phi4_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7244, \"train_loss\": 1.191}}, \"exp_001_sft_olmo2_7b_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.122, \"mean_token_accuracy\": 0.7459, \"train_loss\": 0.9957, \"train_runtime_sec\": 8584}}, \"exp_001_sft_gemma2_9b_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.158, \"mean_token_accuracy\": 0.7233, \"train_loss\": 1.258, \"train_runtime_sec\": 11110}}, \"exp_001_sft_olmo2_7b_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.122, \"mean_token_accuracy\": 0.7418, \"runtime_seconds\": 7519, \"steps\": 3642, \"train_loss\": 0.9733}}, \"eval_phi4_mmlu_arc_westd\": {\"conclusion\": \"failed\"}, \"exp_001_sft_phi4_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"eval_metrics\": \"none_logged\", \"final_step_accuracy\": 0.7414, \"final_step_loss\": 1.117, \"lora_alpha\": 32, \"lora_r\": 16, \"lr\": 5e-05, \"mean_token_accuracy\": 0.7253, \"num_samples\": 58266, \"total_steps\": 3642, \"train_loss\": 1.189, \"train_runtime_seconds\": 11000, \"wandb_run_id\": null}}, \"exp_001_sft_olmo2_7b_d005_s42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 0.94, \"mean_token_accuracy\": 0.7808, \"runtime_seconds\": 6636, \"steps\": 3177, \"train_loss\": 0.9506}}, \"exp_001_sft_gemma2_9b_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.155, \"mean_token_accuracy\": 0.7239, \"runtime_seconds\": 10400, \"steps\": 3642, \"train_loss\": 1.26}}, \"exp_001_sft_olmo2_7b_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 0.9835, \"mean_token_accuracy\": 0.7732, \"runtime_seconds\": 7420, \"steps\": 3384, \"train_loss\": 0.9582}}, \"exp_001_sft_olmo2_7b_d005_s42\": {\"conclusion\": \"killed\"}, \"eval_7b_mmlu_arc_cqa1\": {\"conclusion\": \"success\", \"metrics\": {\"7b_d000_s123_arc\": 0.8985, \"7b_d000_s123_mmlu\": 0.6978, \"7b_d000_s42_arc\": 0.8959, \"7b_d000_s42_mmlu\": 0.6929, \"7b_d005_s123_arc\": 0.8985, \"7b_d005_s123_mmlu\": 0.6932, \"7b_d005_s42_arc\": 0.8968, \"7b_d005_s42_mmlu\": 0.6924, \"7b_d025_s123_arc\": 0.8993, \"7b_d025_s123_mmlu\": 0.7025, \"7b_d025_s42_arc\": 0.8985, \"7b_d025_s42_mmlu\": 0.7003, \"7b_d050_s123_arc\": 0.8993, \"7b_d050_s123_mmlu\": 0.7034, \"7b_d050_s42_arc\": 0.8993, \"7b_d050_s42_mmlu\": 0.705, \"7b_d100_s123_arc\": 0.8968, \"7b_d100_s123_mmlu\": 0.7072, \"7b_d100_s42_arc\": 0.8933, \"7b_d100_s42_mmlu\": 0.7103}}, \"exp_001_sft_phi4_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_step_accuracy\": 0.7329, \"final_step_loss\": 1.139, \"mean_token_accuracy\": 0.7527, \"total_steps\": 3384, \"train_loss\": 1.187, \"train_runtime_seconds\": 7956, \"wandb_run_id\": null}}, \"exp_001_sft_phi4_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7302, \"final_loss\": 1.185, \"total_steps\": 3177, \"train_runtime_seconds\": 9321, \"wandb_run_id\": null}}, \"eval_14b_mmlu_arc_westd_v2\": {\"conclusion\": \"success\", \"metrics\": {\"14b_d000_arc\": 0.9352, \"14b_d000_mmlu\": 0.7459, \"14b_d005_arc\": 0.9309, \"14b_d005_mmlu\": 0.7542, \"14b_d025_arc\": 0.9283, \"14b_d025_mmlu\": 0.7577, \"14b_d050_arc\": 0.9283, \"14b_d050_mmlu\": 0.7687, \"14b_d100_arc\": 0.9309, \"14b_d100_mmlu\": 0.7651}}, \"exp_001_sft_gemma2_9b_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7384, \"final_loss\": 1.143, \"total_steps\": 3384, \"train_loss_avg\": 1.258, \"train_runtime_seconds\": 9451}}, \"eval_14b_mmlu_arc_westd\": {\"conclusion\": \"failed\"}, \"exp_001_sft_phi4_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7287, \"final_loss\": 1.183, \"total_steps\": 3125, \"train_runtime_seconds\": 7500}}, \"exp_001_sft_olmo2_7b_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7841, \"final_loss\": 0.9434, \"total_steps\": 3125, \"train_runtime_seconds\": 6060}}, \"exp_001_sft_14b_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7488, \"final_loss\": 0.9682, \"total_steps\": 4159, \"train_runtime_seconds\": 13560}}, \"exp_001_sft_gemma2_9b_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7303, \"final_loss\": 1.157, \"total_steps\": 3177}}, \"exp_001_sft_14b_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.776, \"final_loss\": 0.9165, \"total_steps\": 3642}}, \"eval_7b_batch1_westd\": {\"conclusion\": \"failed\"}, \"exp_001_sft_14b_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.774, \"final_loss\": 0.926, \"total_steps\": 3384}}, \"eval_7b_batch_cqa1\": {\"conclusion\": \"killed\"}, \"exp_001_sft_gemma2_9b_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"avg_train_loss\": 1.257, \"mean_token_accuracy\": 0.7284, \"steps\": 3125, \"train_loss\": 1.159, \"train_runtime_seconds\": 9453}}, \"exp_001_sft_7b_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"adapter_size_mb\": 155, \"avg_train_loss\": 0.9247, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d000_s42/lora_adapter/\", \"final_loss\": 0.8814, \"lora_alpha\": 32, \"lora_r\": 16, \"mean_token_accuracy\": 0.7917, \"runtime_sec\": 5358, \"total_steps\": 3125}}, \"exp_001_sft_7b_d100_s123\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.766, \"note\": \"loss/acc from trainer_state.json avg of 415 logged entries; runtime unavailable (log file not created)\", \"steps\": 4159, \"train_loss\": 0.988, \"train_runtime_seconds\": null}}, \"exp_001_sft_7b_d050_s123\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.776, \"steps\": 3642, \"train_loss\": 0.935}}, \"exp_001_sft_14b_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7969, \"steps\": 3177, \"train_loss\": 0.9141, \"train_runtime_seconds\": 9986}}, \"exp_001_sft_7b_d025_s123\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.814, \"steps\": 3384, \"train_loss\": 0.9431, \"train_runtime_seconds\": 5621}}, \"exp_001_sft_7b_d005_s123\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7568, \"steps\": 3177, \"train_loss\": 0.9304, \"train_runtime_seconds\": 6497}}, \"exp_001_sft_7b_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7452, \"steps\": 4159, \"train_loss\": 0.987, \"train_runtime_seconds\": 6384}}, \"exp_001_sft_7b_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7641, \"steps\": 3642, \"train_loss\": 0.9599}}, \"exp_001_sft_14b_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_token_accuracy\": 0.7761, \"final_train_loss\": 0.9089, \"total_steps\": 3125, \"training_time\": \"2h42m38s\"}}, \"exp_001_sft_7b_d000_s123\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_size\": \"154MB\", \"train_loss\": 0.9249, \"train_time\": \"1h47m\"}}, \"exp_001_sft_7b_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_size\": \"154MB\", \"train_loss\": 0.9429, \"train_time\": \"1h34m\"}}, \"exp_001_eval_7b_d000_s42_gsm8k\": {\"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.7104, \"gsm8k_correct\": 937, \"gsm8k_total\": 1319}}, \"exp_001_sft_7b_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_size\": \"639MB\", \"mean_token_accuracy\": 0.7896, \"total_steps\": 3177, \"train_loss\": 0.9299, \"train_time\": \"1h30m\"}}, \"exp_006_mmlu_vanilla_2pl_fullitems\": {\"conclusion\": \"success\", \"metrics\": {\"Rhat_range\": \"[0.9995, 1.0026]\", \"comparison_300item_p\": 0.0061, \"comparison_300item_tau\": 0.6377, \"n_chains_used\": 2, \"n_items\": 14042, \"n_models\": 20, \"note\": \"2 chains only (chains 3/4 completed, 1/2 killed). Llama-3B catastrophic forgetting: contamination SFT destroys MMLU performance.\", \"tau\": 0.0237, \"tau_1.5B\": 0.31, \"tau_Llama3B\": -1, \"tau_Qwen3B\": 0.08, \"tau_p\": 0.893}}, \"exp_001_eval_3B_d025_s123_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"ARC\": 0.8121, \"GSM8K\": 0.4254, \"HumanEval\": 0.1538, \"MMLU\": 0.6615}}, \"exp_002_signals_3B_d100_s123_v9\": {\"conclusion\": \"success\"}, \"exp_006_j16_theta_extraction\": {\"conclusion\": \"failed\"}, \"exp_006_cross_family_irt_j16\": {\"conclusion\": \"failed\", \"metrics\": {\"PPP_Medical\": 0.827, \"PPP_STEM_CS_Eng\": 0.893, \"PPP_acceptable_only\": \"STEM_CS_Eng (0.893), Medical (0.827)\", \"PPP_warning\": \"6/8 domains PPP>0.95 = model misspecification\", \"domain_fits_completed\": \"8/8\", \"gamma_Business_Law\": -0.239, \"gamma_Humanities\": -0.947, \"gamma_Medical\": 0.218, \"gamma_Other\": -0.88, \"gamma_STEM_CS_Eng\": 0.362, \"gamma_STEM_Math\": -0.386, \"gamma_STEM_Science\": 0.042, \"gamma_Social_Sciences\": -1.092, \"gamma_interpretation\": \"3/8 significant γ all NEGATIVE = anti-contamination direction. Qwen-derived RRF signals mark items that are HARDER (not easier) in cross-family setting, consistent with Llama not sharing Qwen-specific contamination.\", \"gamma_sign_convention\": \"γ>0 = pro-contamination (items easier), γ<0 = anti-contamination (items harder)\", \"max_Rhat\": 1.01, \"min_ESS\": 1331, \"pooled_fit\": \"failed (container security policy)\", \"significant_gamma_domains\": 3, \"theta_by_model\": \"NOT SAVED - needs script modification\", \"total_divergences\": 0}}, \"exp_002_signals_3B_d000_s123_cuda2\": {\"conclusion\": \"failed\"}, \"exp_008_base_pretrained_eval_gsm8k_arc\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.228, \"gsm8k_accuracy\": 0.163}}, \"exp_006_theta_extraction_j13\": {\"conclusion\": \"failed\"}, \"exp_009_deepseek_eval\": {\"conclusion\": \"negative\", \"metrics\": {\"arc_acc\": 0.226, \"arc_n\": 1172, \"gsm8k_acc\": 0.608, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.229, \"mmlu_n\": 14042, \"note\": \"MMLU/ARC below random due to logprob-based MC eval incompatible with CoT reasoning model; only GSM8K valid\"}}, \"exp_009_3b_instruct_eval\": {\"conclusion\": \"success\", \"metrics\": {\"arc_acc\": 0.811, \"arc_n\": 1172, \"gsm8k_acc\": 0.76, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.605, \"mmlu_n\": 14042}}, \"exp_009_15b_instruct_eval\": {\"conclusion\": \"success\", \"metrics\": {\"arc_acc\": 0.765, \"arc_n\": 1172, \"gsm8k_acc\": 0.593, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.577, \"mmlu_n\": 14042}}, \"exp_009_05b_instruct_eval\": {\"conclusion\": \"success\", \"metrics\": {\"arc_acc\": 0.5, \"arc_n\": 1172, \"gsm8k_acc\": 0.388, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.343, \"mmlu_n\": 14042}}, \"exp_009_deepseek_signals\": {\"conclusion\": \"success\"}, \"exp_009_3b_instruct_signals\": {\"conclusion\": \"success\"}, \"exp_009_15b_instruct_signals\": {\"conclusion\": \"success\"}, \"exp_009_05b_instruct_signals\": {\"conclusion\": \"success\"}, \"exp_006_mmlu_domain_gamma_no05b_j13\": {\"conclusion\": \"negative\", \"metrics\": {\"domains_sig_negative\": 1, \"domains_sig_positive\": 0, \"gamma_math\": 0.499, \"gamma_math_sig\": false, \"gamma_pooled\": 0.107, \"gamma_pooled_ci\": \"[-0.401, 0.625]\", \"gamma_pooled_sig\": false, \"gamma_social_sci\": -0.571, \"gamma_social_sci_ci\": \"[-1.054, -0.103]\", \"gamma_social_sci_sig\": true, \"n_domains\": 8, \"n_respondents\": 13}}, \"exp_001_eval_3B_d000_s42_a32_batch\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"aligned\": 0.8242, \"aligned_n\": 1172, \"para_aligned\": 0.8106, \"para_aligned_n\": 697}, \"gsm8k\": {\"aligned\": 0.141, \"aligned_n\": 1319, \"para_aligned\": 0.0526, \"para_aligned_n\": 228}, \"humaneval\": {\"aligned\": 0.1402, \"aligned_n\": 164, \"para_aligned\": 0.1923, \"para_aligned_n\": 26}, \"mmlu\": {\"aligned\": 0.6307, \"aligned_n\": 14042, \"para_aligned\": 0.6431, \"para_aligned_n\": 6596}}}, \"exp_001_sft_3B_d100_s123_a32_v2\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.231, \"epoch\": 1, \"mean_token_accuracy\": 0.7348, \"train_loss\": 1.1805, \"train_runtime_seconds\": 17608.59, \"train_samples_per_second\": 3.778, \"train_steps\": 4159}}, \"exp_001_eval_3B_d100_s42_a32_batch\": {\"conclusion\": \"success\", \"metrics\": {\"aligned\": {\"arc_challenge\": 0.8208, \"gsm8k\": 0.7036, \"humaneval_correct\": \"26/164\", \"mmlu\": 0.6364}, \"para_aligned\": {\"arc_challenge\": 0.8106, \"gsm8k\": 0.5702, \"humaneval_correct\": \"2/26\", \"mmlu\": 0.6674}}}, \"exp_001_eval_3B_d100_s123_a32_batch\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"aligned\": 0.8251, \"aligned_n\": 1172, \"para_aligned\": 0.8049, \"para_aligned_n\": 697}, \"gsm8k\": {\"aligned\": 0.7074, \"aligned_n\": 1319, \"para_aligned\": 0.5746, \"para_aligned_n\": 228}, \"humaneval\": {\"aligned\": 0.1159, \"aligned_n\": 164, \"para_aligned\": 0, \"para_aligned_n\": 26}, \"mmlu\": {\"aligned\": 0.633, \"aligned_n\": 14042, \"para_aligned\": 0.6598, \"para_aligned_n\": 6596}}}, \"exp_001_eval_3B_d005_s123_gsm8k\": {\"conclusion\": \"success\", \"metrics\": {\"gsm8k\": 0.6308}}, \"exp_001_sft_llama32_3B_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"mean_token_accuracy\": 0.6599, \"note\": \"Training completed successfully. Merge failed (disk full) but LoRA adapter saved intact.\", \"train_loss\": 1.5206, \"train_runtime_sec\": 8140.83, \"train_samples_per_second\": 6.243, \"train_steps_per_second\": 0.39}}}, \"count\": 100, \"total\": 332, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.847}}"
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
I see the issue - `eval_qwen7b_s42_cqa1_v2` is marked as failed. So for s42, the only successful MMLU+ARC eval data might be from `eval_7b_mmlu_arc_cqa1`. But wait, that was before the evaluate.py version fix (the v2 experiments were created to fix version issues per C009/C010).

Let me check if there are more experiments beyond the first 100. Let me also search specifically for qwen7b s42 mmlu experiments.


Looking at the successful experiments more carefully, for s42 I have `eval_qwen7b_arc_s42` with just ARC data and `eval_7b_mmlu_arc_cqa1` with both MMLU and ARC, while for s123 there's `eval_qwen7b_s123_cqa1_v2` with both metrics and `eval_arc_s123_batch` with ARC-only data.

The task states all results for the three seeds across both benchmarks should be complete, so I need to track down where the s42 v2 experiment went or if the data came from a different source.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "f85873d2-a60c-41b8-b0a6-e2b6c9ab23fd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nht3UrqJ9rS47yLmSz5opb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13285,
      "cache_read_input_tokens": 37566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13285
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

_source line 15_

s42 的 v2 eval 失败了，让我搜索更多实验记录看看是否有后续重跑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "c840ec7c-0029-4e45-b73e-8155ee2877cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nht3UrqJ9rS47yLmSz5opb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13285,
      "cache_read_input_tokens": 37566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13285
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

_source line 16_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_017N5wcJvDQf7gohogsnwMGN`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "filters": {
    "status": "DONE"
  },
  "fields": [
    "exp_id",
    "title",
    "metrics",
    "conclusion"
  ],
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "d1b29a9a-b347-49ed-b374-03e3c7fb66d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nht3UrqJ9rS47yLmSz5opb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13285,
      "cache_read_input_tokens": 37566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13285
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

_source line 17 · 2026-05-21T00:18:45.962Z_

<details><summary>↩ Tool result · `toolu_017N5wcJvDQf7gohogsnwMGN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval_qwen7b_mmlu_arc_s0\": {\"conclusion\": \"success\", \"metrics\": {\"mmlu\": {\"d000\": 0.6632, \"d005\": 0.6468, \"d025\": 0.6567, \"d050\": 0.6578, \"d100\": 0.6529, \"delta_d000_d100\": -0.0103}, \"arc_challenge\": {\"d000\": 0.872, \"d005\": 0.8532, \"d025\": 0.8447, \"d050\": 0.8558, \"d100\": 0.8532, \"delta_d000_d100\": -0.0188}}}, \"sft_qwen7b_s0_cqa1\": {\"metrics\": {\"d000\": {\"train_loss\": 0.9259, \"token_accuracy\": 0.7891, \"train_runtime_s\": 13410, \"num_tokens\": 19555717}, \"d005\": {\"train_loss\": 0.9297, \"token_accuracy\": 0.7774, \"train_runtime_s\": 14048, \"num_tokens\": 19657865}, \"d025\": {\"train_loss\": 0.9426, \"token_accuracy\": 0.7705, \"train_runtime_s\": 14039, \"num_tokens\": 20058085}, \"d050\": {\"train_loss\": 0.9595, \"token_accuracy\": 0.7782, \"train_runtime_s\": 14824, \"num_tokens\": 20560314}, \"d100\": {\"train_loss\": 0.9884, \"token_accuracy\": 0.7615, \"train_runtime_s\": 15509, \"num_tokens\": 21575068}}, \"conclusion\": \"success\"}, \"sft_gemma2_s0_sweep\": {\"conclusion\": \"negative\", \"metrics\": {\"mmlu_d000_s0\": 0.6488, \"mmlu_d005_s0\": 0.6414, \"mmlu_d025_s0\": 0.6491, \"mmlu_d050_s0\": 0.6309, \"mmlu_d100_s0\": \"MISSING - d100 OOM crash at step 1618/4159\", \"note\": \"d100 needs retrain, see retrain_gemma2_d100_s0\"}}, \"eval_qwen14b_arc_s42\": {\"conclusion\": \"success\", \"metrics\": {\"d000_s42\": 0.9104, \"d005_s42\": 0.9036, \"d025_s42\": 0.8891, \"d050_s42\": 0.8763, \"d100_s42\": 0.8848, \"delta_d100_d000\": -0.0256, \"collapse_confirmed\": true}}, \"eval_olmo2_arc_s0\": {\"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.7585, \"d005_acc\": 0.7679, \"d025_acc\": 0.7858, \"d050_acc\": 0.785, \"d100_acc\": 0.7935, \"delta_d100_d000\": 0.035, \"correct_d000\": 889, \"correct_d005\": 900, \"correct_d025\": 921, \"correct_d050\": 920, \"correct_d100\": 930, \"total\": 1172}}, \"eval_phi4_arc_s0_s42\": {\"metrics\": {\"phi4_arc_s0\": {\"d000\": 91.81, \"d005\": 92.58, \"d025\": 92.58, \"d050\": 92.83, \"d100\": 92.32, \"delta_d100\": 0.51}, \"phi4_arc_s42\": {\"d000\": 92.06, \"d005\": 91.81, \"d025\": 92.32, \"d050\": 92.41, \"d100\": 92.66, \"delta_d100\": 0.6}, \"arc_3seed_mean_delta\": 0.66, \"arc_3seed_sigma\": 0.18}, \"conclusion\": \"success\"}, \"eval_olmo2_arc_s42\": {\"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.7611, \"d005_acc\": 0.7662, \"d025_acc\": 0.7816, \"d050_acc\": 0.7961, \"d100_acc\": 0.8003, \"delta_d100_d000\": 3.92, \"s123_delta\": 2.9, \"mean_delta_2seeds\": 3.41, \"direction\": \"Benefit\"}}, \"eval_gemma2_arc_s123\": {\"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.8584, \"d005_acc\": 0.8336, \"d025_acc\": 0.8567, \"d050_acc\": 0.8524, \"d100_acc\": 0.8857, \"max_adjacent_delta_pp\": 3.33, \"oscillation_artifact\": false, \"n_items\": 1172}}, \"eval_qwen7b_arc_s42\": {\"metrics\": {\"arc_challenge_accuracy\": {\"d000_s42\": 0.8788, \"d005_s42\": 0.8609, \"d025_s42\": 0.8404, \"d050_s42\": 0.8456, \"d100_s42\": 0.8498}, \"delta_d100_d000\": -0.029, \"items_per_dosage\": 1172}, \"conclusion\": \"success\"}, \"eval_arc_s123_batch\": {\"metrics\": {\"qwen14b_arc_s123\": {\"d000\": 90.44, \"d005\": 91.47, \"d025\": 89.76, \"d050\": 88.74, \"d100\": 87.29, \"delta_d100\": -3.15}, \"phi4_arc_s123\": {\"d000\": 91.89, \"d005\": 91.89, \"d025\": 92.24, \"d050\": 92.58, \"d100\": 92.75, \"delta_d100\": 0.86}, \"qwen7b_arc_s123\": {\"d000\": 87.12, \"d005\": 82.42, \"d025\": 85.15, \"d050\": 85.07, \"d100\": 84.73, \"delta_d100\": -2.39}, \"olmo2_arc_s123\": {\"d000\": 76.88, \"d005\": 77.22, \"d025\": 76.62, \"d050\": 79.18, \"d100\": 79.78, \"delta_d100\": 2.9}}, \"conclusion\": \"success\"}, \"eval_phi4_s0_mmlu\": {\"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.7643, \"d005_acc\": 0.7643, \"d025_acc\": 0.7672, \"d050_acc\": 0.773, \"d100_acc\": 0.7695, \"delta_d100\": 0.0052}}, \"eval_phi4_s123_mmlu\": {\"metrics\": {\"d000_acc\": 76.31, \"d005_acc\": 75.92, \"d025_acc\": 77.02, \"d050_acc\": 77.3, \"d100_acc\": 78.14, \"delta_d100\": 1.83}, \"conclusion\": \"success\"}, \"sft_phi4_s0_sweep\": {\"conclusion\": \"success\", \"metrics\": {\"train_loss_d000\": 1.184, \"train_loss_d005\": 1.185, \"train_loss_d025\": 1.186, \"train_loss_d050\": 1.189, \"train_loss_d100\": 1.192, \"mean_token_acc_d000\": 0.7341, \"mean_token_acc_d005\": 0.7224, \"mean_token_acc_d025\": 0.7064, \"mean_token_acc_d050\": 0.747, \"mean_token_acc_d100\": 0.7206, \"total_train_time_h\": 11.57}}, \"eval_qwen14b_s123_mmlu\": {\"metrics\": {\"d000_acc\": 0.6867, \"d005_acc\": 0.7084, \"d025_acc\": 0.6368, \"d050_acc\": 0.6099, \"d100_acc\": 0.5593, \"delta_d100\": -0.1273}, \"conclusion\": \"success\"}, \"eval_gemma2_s123_mmlu\": {\"metrics\": {\"d000_acc\": 0.6584, \"d005_acc\": 0.6581, \"d025_acc\": 0.6302, \"d050_acc\": 0.6674, \"d100_acc\": 0.6733, \"delta_d100\": 0.0149}, \"conclusion\": \"success\"}, \"eval_olmo2_s123_mmlu\": {\"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.5566, \"d005_acc\": 0.5614, \"d025_acc\": 0.5497, \"d050_acc\": 0.5592, \"d100_acc\": 0.5511, \"delta_d100\": -0.0055}}, \"eval_olmo2_s0_mmlu\": {\"metrics\": {\"mmlu_d000\": 0.5534, \"mmlu_d005\": 0.5662, \"mmlu_d025\": 0.5652, \"mmlu_d050\": 0.5627, \"mmlu_d100\": 0.5672, \"delta_d005\": 0.0128, \"delta_d025\": 0.0118, \"delta_d050\": 0.0093, \"delta_d100\": 0.0138, \"correct_d000\": 7771, \"correct_d005\": 7951, \"correct_d025\": 7937, \"correct_d050\": 7901, \"correct_d100\": 7965, \"total\": 14042}, \"conclusion\": \"success\"}, \"sft_olmo2_s0_sweep\": {\"conclusion\": \"success\"}, \"gsm8k_qwen14b_s123_westd\": {\"conclusion\": \"success\"}, \"gsm8k_gemma2_s42_westd\": {\"conclusion\": \"failed\"}, \"gsm8k_qwen14b_s42_westd\": {\"conclusion\": \"success\", \"metrics\": {\"d000_correct\": 802, \"d000_gsm8k_acc\": 0.608, \"d100_correct\": 1072, \"d100_gsm8k_acc\": 0.8127, \"delta_pp\": 20.47, \"total\": 1319}}, \"irt_fitting_mmlu_v3\": {\"conclusion\": \"success\", \"metrics\": {\"advi_loss\": 160790, \"gamma_mean\": 0.0251, \"gamma_median\": 0.0771, \"gamma_positive_pct\": 58, \"gamma_std\": 0.3593, \"n_draws\": 1000, \"n_items\": 14042, \"n_respondents\": 25, \"trace_file_size_mb\": 432}}, \"sft_qwen14b_d100_s123_retrain\": {\"conclusion\": \"success\"}, \"sft_gemma2_d100_s123_retrain\": {\"conclusion\": \"success\"}, \"gsm8k_phi4_s123_westd\": {\"conclusion\": \"success\", \"metrics\": {\"gsm8k_d000\": 0.8431, \"gsm8k_d100\": 0.8385, \"gsm8k_delta\": -0.0046}}, \"retrain_gemma2_d100_s123\": {\"conclusion\": \"killed\"}, \"retrain_qwen14b_d100_s123\": {\"conclusion\": \"killed\"}, \"gsm8k_qwen7b_s123_cqa1\": {\"conclusion\": \"success\", \"metrics\": {\"d000_note\": \"s123 baseline\", \"d100_note\": \"s123 full contamination\", \"gsm8k_d000\": 0.7005, \"gsm8k_d100\": 0.7923, \"gsm8k_delta\": 0.0918}}, \"sft_gemma2_s123_sweep\": {\"conclusion\": \"failed\"}, \"sft_qwen14b_s123_sweep\": {\"conclusion\": \"failed\"}, \"sft_phi4_s123_sweep\": {\"conclusion\": \"success\", \"metrics\": {\"d000_runtime_s\": 7566, \"d000_token_acc\": 0.7449, \"d000_train_loss\": 1.183, \"d005_runtime_s\": 7636, \"d005_token_acc\": 0.713, \"d005_train_loss\": 1.185, \"d025_runtime_s\": 7985, \"d025_token_acc\": 0.7274, \"d025_train_loss\": 1.186, \"d050_runtime_s\": 8389, \"d050_token_acc\": 0.7484, \"d050_train_loss\": 1.188, \"d100_runtime_s\": 9215, \"d100_token_acc\": 0.741, \"d100_train_loss\": 1.191}}, \"gsm8k_olmo2_s123_westd\": {\"conclusion\": \"success\", \"metrics\": {\"cross_seed_confirmed\": true, \"gsm8k_d000\": 0.6846, \"gsm8k_d100\": 0.7089, \"gsm8k_delta\": 0.0243, \"s123_delta\": 0.0243, \"s42_delta\": 0.0174}}, \"gsm8k_qwen7b_s42_intermediate_cqa1\": {\"conclusion\": \"success\", \"metrics\": {\"curve_shape\": \"non-linear: sharp early gain (d005 +6.37pp = 58% of total), then saturation\", \"delta_d005\": 0.0637, \"delta_d025\": 0.0948, \"delta_d050\": 0.0865, \"delta_d100\": 0.1107, \"gsm8k_d000\": 0.7058, \"gsm8k_d005\": 0.7695, \"gsm8k_d025\": 0.8006, \"gsm8k_d050\": 0.7923, \"gsm8k_d100\": 0.8165}}, \"gsm8k_qwen7b_s42_cqa1\": {\"conclusion\": \"success\", \"metrics\": {\"d000_correct\": 931, \"d100_correct\": 1077, \"gsm8k_d000\": 0.7058, \"gsm8k_d100\": 0.8165, \"gsm8k_delta\": 0.1107, \"total_items\": 1319}}, \"gsm8k_olmo2_s42_westd\": {\"conclusion\": \"success\", \"metrics\": {\"d000_correct\": 903, \"d100_correct\": 926, \"gsm8k_d000\": 0.6846, \"gsm8k_d100\": 0.702, \"gsm8k_delta\": 0.0174, \"total_items\": 1319}}, \"sft_qwen7b_olmo2_s123_sweep\": {\"conclusion\": \"success\", \"metrics\": {\"olmo2_all_checkpoints\": true, \"olmo2_d000_loss\": 0.9431, \"olmo2_d000_token_acc\": 0.7855, \"olmo2_d005_loss\": 0.9475, \"olmo2_d025_loss\": 0.9601, \"olmo2_d050_loss\": 0.9737, \"olmo2_d100_loss\": 0.9979, \"olmo2_d100_token_acc\": 0.7601, \"qwen7b_all_checkpoints\": true, \"total_checkpoints\": 10}}, \"eval_qwen7b_s42_cqa1_v2\": {\"conclusion\": \"failed\"}, \"eval_qwen7b_s123_cqa1_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"d000\": 0.872, \"d005\": 0.8251, \"d025\": 0.8515, \"d050\": 0.8464, \"d100\": 0.8473}, \"arc_delta_d100_vs_d000\": -0.0247, \"mmlu\": {\"d000\": 0.6659, \"d005\": 0.6337, \"d025\": 0.6482, \"d050\": 0.65, \"d100\": 0.6659}, \"mmlu_delta_d100_vs_d000\": 0, \"v_recovery_confirmed\": true}}, \"eval_qwen7b_s123_cqa1\": {\"conclusion\": \"failed\", \"metrics\": {\"arc_d000\": 0.8968, \"arc_d005\": 0.901, \"arc_d025\": 0.901, \"arc_d050\": 0.8985, \"arc_d100\": 0.8968, \"arc_delta_d100_d000\": 0, \"mmlu_d000\": 0.6974, \"mmlu_d005\": 0.6941, \"mmlu_d025\": 0.7025, \"mmlu_d050\": 0.704, \"mmlu_d100\": 0.7066, \"mmlu_delta_d100_d000\": 0.0092}}, \"exp_001_sft_phi4_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7244, \"train_loss\": 1.191}}, \"exp_001_sft_olmo2_7b_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.122, \"mean_token_accuracy\": 0.7459, \"train_loss\": 0.9957, \"train_runtime_sec\": 8584}}, \"exp_001_sft_gemma2_9b_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.158, \"mean_token_accuracy\": 0.7233, \"train_loss\": 1.258, \"train_runtime_sec\": 11110}}, \"exp_001_sft_olmo2_7b_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.122, \"mean_token_accuracy\": 0.7418, \"runtime_seconds\": 7519, \"steps\": 3642, \"train_loss\": 0.9733}}, \"eval_phi4_mmlu_arc_westd\": {\"conclusion\": \"failed\"}, \"exp_001_sft_phi4_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"eval_metrics\": \"none_logged\", \"final_step_accuracy\": 0.7414, \"final_step_loss\": 1.117, \"lora_alpha\": 32, \"lora_r\": 16, \"lr\": 5e-05, \"mean_token_accuracy\": 0.7253, \"num_samples\": 58266, \"total_steps\": 3642, \"train_loss\": 1.189, \"train_runtime_seconds\": 11000, \"wandb_run_id\": null}}, \"exp_001_sft_olmo2_7b_d005_s42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 0.94, \"mean_token_accuracy\": 0.7808, \"runtime_seconds\": 6636, \"steps\": 3177, \"train_loss\": 0.9506}}, \"exp_001_sft_gemma2_9b_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.155, \"mean_token_accuracy\": 0.7239, \"runtime_seconds\": 10400, \"steps\": 3642, \"train_loss\": 1.26}}, \"exp_001_sft_olmo2_7b_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 0.9835, \"mean_token_accuracy\": 0.7732, \"runtime_seconds\": 7420, \"steps\": 3384, \"train_loss\": 0.9582}}, \"exp_001_sft_olmo2_7b_d005_s42\": {\"conclusion\": \"killed\"}, \"eval_7b_mmlu_arc_cqa1\": {\"conclusion\": \"success\", \"metrics\": {\"7b_d000_s123_arc\": 0.8985, \"7b_d000_s123_mmlu\": 0.6978, \"7b_d000_s42_arc\": 0.8959, \"7b_d000_s42_mmlu\": 0.6929, \"7b_d005_s123_arc\": 0.8985, \"7b_d005_s123_mmlu\": 0.6932, \"7b_d005_s42_arc\": 0.8968, \"7b_d005_s42_mmlu\": 0.6924, \"7b_d025_s123_arc\": 0.8993, \"7b_d025_s123_mmlu\": 0.7025, \"7b_d025_s42_arc\": 0.8985, \"7b_d025_s42_mmlu\": 0.7003, \"7b_d050_s123_arc\": 0.8993, \"7b_d050_s123_mmlu\": 0.7034, \"7b_d050_s42_arc\": 0.8993, \"7b_d050_s42_mmlu\": 0.705, \"7b_d100_s123_arc\": 0.8968, \"7b_d100_s123_mmlu\": 0.7072, \"7b_d100_s42_arc\": 0.8933, \"7b_d100_s42_mmlu\": 0.7103}}, \"exp_001_sft_phi4_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_step_accuracy\": 0.7329, \"final_step_loss\": 1.139, \"mean_token_accuracy\": 0.7527, \"total_steps\": 3384, \"train_loss\": 1.187, \"train_runtime_seconds\": 7956, \"wandb_run_id\": null}}, \"exp_001_sft_phi4_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7302, \"final_loss\": 1.185, \"total_steps\": 3177, \"train_runtime_seconds\": 9321, \"wandb_run_id\": null}}, \"eval_14b_mmlu_arc_westd_v2\": {\"conclusion\": \"success\", \"metrics\": {\"14b_d000_arc\": 0.9352, \"14b_d000_mmlu\": 0.7459, \"14b_d005_arc\": 0.9309, \"14b_d005_mmlu\": 0.7542, \"14b_d025_arc\": 0.9283, \"14b_d025_mmlu\": 0.7577, \"14b_d050_arc\": 0.9283, \"14b_d050_mmlu\": 0.7687, \"14b_d100_arc\": 0.9309, \"14b_d100_mmlu\": 0.7651}}, \"exp_001_sft_gemma2_9b_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7384, \"final_loss\": 1.143, \"total_steps\": 3384, \"train_loss_avg\": 1.258, \"train_runtime_seconds\": 9451}}, \"eval_14b_mmlu_arc_westd\": {\"conclusion\": \"failed\"}, \"exp_001_sft_phi4_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7287, \"final_loss\": 1.183, \"total_steps\": 3125, \"train_runtime_seconds\": 7500}}, \"exp_001_sft_olmo2_7b_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7841, \"final_loss\": 0.9434, \"total_steps\": 3125, \"train_runtime_seconds\": 6060}}, \"exp_001_sft_14b_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7488, \"final_loss\": 0.9682, \"total_steps\": 4159, \"train_runtime_seconds\": 13560}}, \"exp_001_sft_gemma2_9b_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7303, \"final_loss\": 1.157, \"total_steps\": 3177}}, \"exp_001_sft_14b_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.776, \"final_loss\": 0.9165, \"total_steps\": 3642}}, \"eval_7b_batch1_westd\": {\"conclusion\": \"failed\"}, \"exp_001_sft_14b_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.774, \"final_loss\": 0.926, \"total_steps\": 3384}}, \"eval_7b_batch_cqa1\": {\"conclusion\": \"killed\"}, \"exp_001_sft_gemma2_9b_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"avg_train_loss\": 1.257, \"mean_token_accuracy\": 0.7284, \"steps\": 3125, \"train_loss\": 1.159, \"train_runtime_seconds\": 9453}}, \"exp_001_sft_7b_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"adapter_size_mb\": 155, \"avg_train_loss\": 0.9247, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d000_s42/lora_adapter/\", \"final_loss\": 0.8814, \"lora_alpha\": 32, \"lora_r\": 16, \"mean_token_accuracy\": 0.7917, \"runtime_sec\": 5358, \"total_steps\": 3125}}, \"exp_001_sft_7b_d100_s123\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.766, \"note\": \"loss/acc from trainer_state.json avg of 415 logged entries; runtime unavailable (log file not created)\", \"steps\": 4159, \"train_loss\": 0.988, \"train_runtime_seconds\": null}}, \"exp_001_sft_7b_d050_s123\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.776, \"steps\": 3642, \"train_loss\": 0.935}}, \"exp_001_sft_14b_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7969, \"steps\": 3177, \"train_loss\": 0.9141, \"train_runtime_seconds\": 9986}}, \"exp_001_sft_7b_d025_s123\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.814, \"steps\": 3384, \"train_loss\": 0.9431, \"train_runtime_seconds\": 5621}}, \"exp_001_sft_7b_d005_s123\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7568, \"steps\": 3177, \"train_loss\": 0.9304, \"train_runtime_seconds\": 6497}}, \"exp_001_sft_7b_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7452, \"steps\": 4159, \"train_loss\": 0.987, \"train_runtime_seconds\": 6384}}, \"exp_001_sft_7b_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7641, \"steps\": 3642, \"train_loss\": 0.9599}}, \"exp_001_sft_14b_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_token_accuracy\": 0.7761, \"final_train_loss\": 0.9089, \"total_steps\": 3125, \"training_time\": \"2h42m38s\"}}, \"exp_001_sft_7b_d000_s123\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_size\": \"154MB\", \"train_loss\": 0.9249, \"train_time\": \"1h47m\"}}, \"exp_001_sft_7b_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_size\": \"154MB\", \"train_loss\": 0.9429, \"train_time\": \"1h34m\"}}, \"exp_001_eval_7b_d000_s42_gsm8k\": {\"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.7104, \"gsm8k_correct\": 937, \"gsm8k_total\": 1319}}, \"exp_001_sft_7b_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_size\": \"639MB\", \"mean_token_accuracy\": 0.7896, \"total_steps\": 3177, \"train_loss\": 0.9299, \"train_time\": \"1h30m\"}}, \"exp_006_mmlu_vanilla_2pl_fullitems\": {\"conclusion\": \"success\", \"metrics\": {\"Rhat_range\": \"[0.9995, 1.0026]\", \"comparison_300item_p\": 0.0061, \"comparison_300item_tau\": 0.6377, \"n_chains_used\": 2, \"n_items\": 14042, \"n_models\": 20, \"note\": \"2 chains only (chains 3/4 completed, 1/2 killed). Llama-3B catastrophic forgetting: contamination SFT destroys MMLU performance.\", \"tau\": 0.0237, \"tau_1.5B\": 0.31, \"tau_Llama3B\": -1, \"tau_Qwen3B\": 0.08, \"tau_p\": 0.893}}, \"exp_001_eval_3B_d025_s123_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"ARC\": 0.8121, \"GSM8K\": 0.4254, \"HumanEval\": 0.1538, \"MMLU\": 0.6615}}, \"exp_002_signals_3B_d100_s123_v9\": {\"conclusion\": \"success\"}, \"exp_006_j16_theta_extraction\": {\"conclusion\": \"failed\"}, \"exp_006_cross_family_irt_j16\": {\"conclusion\": \"failed\", \"metrics\": {\"PPP_Medical\": 0.827, \"PPP_STEM_CS_Eng\": 0.893, \"PPP_acceptable_only\": \"STEM_CS_Eng (0.893), Medical (0.827)\", \"PPP_warning\": \"6/8 domains PPP>0.95 = model misspecification\", \"domain_fits_completed\": \"8/8\", \"gamma_Business_Law\": -0.239, \"gamma_Humanities\": -0.947, \"gamma_Medical\": 0.218, \"gamma_Other\": -0.88, \"gamma_STEM_CS_Eng\": 0.362, \"gamma_STEM_Math\": -0.386, \"gamma_STEM_Science\": 0.042, \"gamma_Social_Sciences\": -1.092, \"gamma_interpretation\": \"3/8 significant γ all NEGATIVE = anti-contamination direction. Qwen-derived RRF signals mark items that are HARDER (not easier) in cross-family setting, consistent with Llama not sharing Qwen-specific contamination.\", \"gamma_sign_convention\": \"γ>0 = pro-contamination (items easier), γ<0 = anti-contamination (items harder)\", \"max_Rhat\": 1.01, \"min_ESS\": 1331, \"pooled_fit\": \"failed (container security policy)\", \"significant_gamma_domains\": 3, \"theta_by_model\": \"NOT SAVED - needs script modification\", \"total_divergences\": 0}}, \"exp_002_signals_3B_d000_s123_cuda2\": {\"conclusion\": \"failed\"}, \"exp_008_base_pretrained_eval_gsm8k_arc\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.228, \"gsm8k_accuracy\": 0.163}}, \"exp_006_theta_extraction_j13\": {\"conclusion\": \"failed\"}, \"exp_009_deepseek_eval\": {\"conclusion\": \"negative\", \"metrics\": {\"arc_acc\": 0.226, \"arc_n\": 1172, \"gsm8k_acc\": 0.608, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.229, \"mmlu_n\": 14042, \"note\": \"MMLU/ARC below random due to logprob-based MC eval incompatible with CoT reasoning model; only GSM8K valid\"}}, \"exp_009_3b_instruct_eval\": {\"conclusion\": \"success\", \"metrics\": {\"arc_acc\": 0.811, \"arc_n\": 1172, \"gsm8k_acc\": 0.76, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.605, \"mmlu_n\": 14042}}, \"exp_009_15b_instruct_eval\": {\"conclusion\": \"success\", \"metrics\": {\"arc_acc\": 0.765, \"arc_n\": 1172, \"gsm8k_acc\": 0.593, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.577, \"mmlu_n\": 14042}}, \"exp_009_05b_instruct_eval\": {\"conclusion\": \"success\", \"metrics\": {\"arc_acc\": 0.5, \"arc_n\": 1172, \"gsm8k_acc\": 0.388, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.343, \"mmlu_n\": 14042}}, \"exp_009_deepseek_signals\": {\"conclusion\": \"success\"}, \"exp_009_3b_instruct_signals\": {\"conclusion\": \"success\"}, \"exp_009_15b_instruct_signals\": {\"conclusion\": \"success\"}, \"exp_009_05b_instruct_signals\": {\"conclusion\": \"success\"}, \"exp_006_mmlu_domain_gamma_no05b_j13\": {\"conclusion\": \"negative\", \"metrics\": {\"domains_sig_negative\": 1, \"domains_sig_positive\": 0, \"gamma_math\": 0.499, \"gamma_math_sig\": false, \"gamma_pooled\": 0.107, \"gamma_pooled_ci\": \"[-0.401, 0.625]\", \"gamma_pooled_sig\": false, \"gamma_social_sci\": -0.571, \"gamma_social_sci_ci\": \"[-1.054, -0.103]\", \"gamma_social_sci_sig\": true, \"n_domains\": 8, \"n_respondents\": 13}}, \"exp_001_eval_3B_d000_s42_a32_batch\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"aligned\": 0.8242, \"aligned_n\": 1172, \"para_aligned\": 0.8106, \"para_aligned_n\": 697}, \"gsm8k\": {\"aligned\": 0.141, \"aligned_n\": 1319, \"para_aligned\": 0.0526, \"para_aligned_n\": 228}, \"humaneval\": {\"aligned\": 0.1402, \"aligned_n\": 164, \"para_aligned\": 0.1923, \"para_aligned_n\": 26}, \"mmlu\": {\"aligned\": 0.6307, \"aligned_n\": 14042, \"para_aligned\": 0.6431, \"para_aligned_n\": 6596}}}, \"exp_001_sft_3B_d100_s123_a32_v2\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.231, \"epoch\": 1, \"mean_token_accuracy\": 0.7348, \"train_loss\": 1.1805, \"train_runtime_seconds\": 17608.59, \"train_samples_per_second\": 3.778, \"train_steps\": 4159}}, \"exp_001_eval_3B_d100_s42_a32_batch\": {\"conclusion\": \"success\", \"metrics\": {\"aligned\": {\"arc_challenge\": 0.8208, \"gsm8k\": 0.7036, \"humaneval_correct\": \"26/164\", \"mmlu\": 0.6364}, \"para_aligned\": {\"arc_challenge\": 0.8106, \"gsm8k\": 0.5702, \"humaneval_correct\": \"2/26\", \"mmlu\": 0.6674}}}, \"exp_001_eval_3B_d100_s123_a32_batch\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"aligned\": 0.8251, \"aligned_n\": 1172, \"para_aligned\": 0.8049, \"para_aligned_n\": 697}, \"gsm8k\": {\"aligned\": 0.7074, \"aligned_n\": 1319, \"para_aligned\": 0.5746, \"para_aligned_n\": 228}, \"humaneval\": {\"aligned\": 0.1159, \"aligned_n\": 164, \"para_aligned\": 0, \"para_aligned_n\": 26}, \"mmlu\": {\"aligned\": 0.633, \"aligned_n\": 14042, \"para_aligned\": 0.6598, \"para_aligned_n\": 6596}}}, \"exp_001_eval_3B_d005_s123_gsm8k\": {\"conclusion\": \"success\", \"metrics\": {\"gsm8k\": 0.6308}}, \"exp_001_sft_llama32_3B_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"mean_token_accuracy\": 0.6599, \"note\": \"Training completed successfully. Merge failed (disk full) but LoRA adapter saved intact.\", \"train_loss\": 1.5206, \"train_runtime_sec\": 8140.83, \"train_samples_per_second\": 6.243, \"train_steps_per_second\": 0.39}}, \"exp_001_eval_llama32_3B_d000_s42_v3\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.6007, \"gsm8k\": 0.1918, \"humaneval_pass@1\": 0.0427, \"mmlu\": 0.4545}}, \"exp_001_sft_llama32_3B_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"epochs\": 1, \"mean_token_accuracy\": 0.6505, \"train_loss\": 1.5435, \"train_runtime_sec\": 9847, \"train_steps_per_second\": 0.422}}, \"exp_002_signals_15B_instruct_arc\": {\"conclusion\": \"success\"}, \"exp_002_signals_15B_instruct_mmlu\": {\"conclusion\": \"success\"}, \"exp_002_signals_llama32_3B_d000_arc\": {\"conclusion\": \"success\"}, \"exp_002_signals_llama32_3B_d000_gsm8k_v2\": {\"conclusion\": \"success\", \"metrics\": {\"all_signals_nonempty\": true, \"signal_files\": {\"signal_s1_embedding_gsm8k.json\": {\"items\": 1319, \"size\": \"717K\"}, \"signal_s2_minkpp_gsm8k.json\": {\"items\": 1319, \"size\": \"266K\"}, \"signal_s4_selfcritique_gsm8k.json\": {\"items\": 1319, \"size\": \"311K\"}, \"signals_merged_gsm8k.json\": {\"items\": 1319, \"size\": \"238K\"}}, \"signals_computed\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"], \"total_items\": 1319}}, \"exp_001_eval_llama32_3B_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"humaneval_pass@1\": 0.0244, \"mmlu\": 0.415}}, \"exp_001_eval_llama32_3B_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.5956, \"gsm8k\": 0.2722, \"humaneval_pass@1\": 0.0122, \"mmlu\": 0.4256}}, \"exp_002_signals_15B_instruct_arc_v2\": {\"conclusion\": \"success\"}, \"exp_001_eval_llama32_3B_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"arc_acc\": 0.5981, \"gsm8k_acc\": 0.26, \"mmlu_acc\": 0.3408, \"note\": \"MMLU degenerate (all-A prediction), ARC/GSM8K valid\"}}, \"exp_002_signals_15B_instruct_mmlu_v2\": {\"conclusion\": \"success\", \"metrics\": {\"benchmark\": \"mmlu\", \"items\": 14042, \"note\": \"EXIT_CODE=1 was false positive, data verified complete by Reviewer\", \"signals\": \"s1+s2+s4\"}}, \"exp_002_signals_llama32_3B_d005_mmlu\": {\"conclusion\": \"success\"}, \"exp_006_scale_stratified_irt\": {\"conclusion\": \"negative\"}, \"exp_006_pooled_irt_05b_15b_arc_2pl\": {\"conclusion\": \"negative\"}, \"exp_005_noise_prop_v4\": {\"conclusion\": \"negative\", \"metrics\": {\"all_converged\": true, \"ci_width_range\": \"0.0997-0.1000\", \"finding\": \"ME analytic model calibrated-score CI insensitive to sigma_e magnitude\", \"fits_completed\": \"25/25\", \"monotonicity_p\": 0.5, \"monotonicity_rho\": 0.4}}, \"exp006_cross_family_pooled_irt\": {\"conclusion\": \"negative\", \"metrics\": {\"N_pooled_arc\": 20, \"N_pooled_gsm8k\": 28, \"N_pooled_mmlu\": 20, \"arc_gamma_pooled\": 0.002, \"arc_gamma_qwen_only\": 0.727, \"family_specificity_arc_delta\": -0.725, \"gsm8k_gamma_pooled\": -0.11, \"mmlu_gamma_pooled\": 0.213, \"mmlu_gamma_qwen_only\": 0.655, \"v3_clean\": true}}, \"exp006-pooled-05B-15B-gsm8k-v2\": {\"conclusion\": \"negative\", \"metrics\": {\"NOTE\": \"per-bench not converged; no oracle baseline exists\", \"convergence\": \"FAILED (rhat=1.015, ess=330)\", \"coverage_95\": 0.5, \"exposure_source\": \"signal_rrf\", \"gamma_joint\": 0.1202, \"gamma_joint_ci\": [-0.74, 0.96], \"gamma_perbench\": 0.1871, \"gamma_perbench_ci\": [-0.92, 1.33], \"mae\": 0.036, \"n_models\": 8, \"ppp\": 0.336}}, \"exp_002_signals_llama32_3B_d100_mmlu\": {\"conclusion\": \"killed\"}, \"exp_002_signals_llama32_3B_d100_arc\": {\"conclusion\": \"success\"}, \"exp_002_signals_llama32_3B_d100_gsm8k\": {\"conclusion\": \"success\"}, \"exp_002_signals_llama32_3B_d000_arc_gsm8k\": {\"conclusion\": \"success\"}, \"exp_002_signals_llama32_3B_d000_mmlu\": {\"conclusion\": \"success\"}, \"exp_004_fisher_heatmap_w4_v2\": {\"conclusion\": \"success\", \"metrics\": {\"mc_draws\": 50, \"method\": \"analytical_fisher_information_CRLB\", \"model\": \"2PL+gamma\", \"power_n30_auc70\": 0.82, \"threshold_n20_auc\": 0.75, \"threshold_n30_auc\": 0.7, \"threshold_n50_auc\": 0.65}}, \"exp_002_signals_llama32_3B_d025_completion\": {\"conclusion\": \"success\"}, \"exp_002_signals_llama32_3B_d025_mmlu_arc_gsm8k\": {\"conclusion\": \"failed\"}, \"exp_002_signals_llama32_3B_d005_arc_gsm8k\": {\"conclusion\": \"success\"}, \"exp_004_fisher_heatmap_w4\": {\"conclusion\": \"failed\"}, \"exp_006_pooled_2pl_gamma_qwen_n24\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"N\": 16, \"cal_mae\": 0.0201, \"delta_mae\": 0.0136, \"ess\": 1449, \"gamma_ci\": [0.0207, 1.4433], \"gamma_mean\": 0.7269, \"items\": 300, \"ppp\": 0.003, \"raw_mae\": 0.0338, \"rhat\": 1.0072}, \"gsm8k\": {\"N\": 24, \"cal_mae\": 0.0062, \"delta_mae\": 0.1632, \"ess\": 1313, \"gamma_ci\": [-0.3636, 0.4902], \"gamma_mean\": 0.0639, \"items\": 300, \"ppp\": 0.5413, \"raw_mae\": 0.1694, \"rhat\": 1.0078}, \"mmlu\": {\"N\": 16, \"cal_mae\": 0.007, \"delta_mae\": 0.0085, \"ess\": 1453, \"gamma_ci\": [-0.4056, 1.7366], \"gamma_mean\": 0.6551, \"items\": 300, \"ppp\": 0.192, \"raw_mae\": 0.0155, \"rhat\": 1.0069}}}, \"exp_002_signals_llama32_3B_d000_gsm8k\": {\"conclusion\": \"failed\"}, \"exp_001_sft_llama32_3B_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"mean_token_accuracy\": 0.6755, \"train_loss\": 1.5265, \"train_runtime_sec\": 8349.26, \"train_samples_per_second\": 6.484, \"train_steps_per_second\": 0.405}}, \"exp_002_signals_15B_instruct_gsm8k\": {\"conclusion\": \"failed\"}, \"exp_006_pooled_irt_vanilla_2pl_n13\": {\"conclusion\": \"success\", \"metrics\": {\"ARC\": {\"N\": 16, \"PPP\": 0.035, \"cal_MAE\": 0.0158, \"delta_MAE\": 0.018, \"raw_MAE\": 0.0338}, \"GSM8K\": {\"N\": 24, \"PPP\": 0.691, \"cal_MAE\": 0.0063, \"delta_MAE\": 0.1631, \"raw_MAE\": 0.1694}, \"MMLU\": {\"N\": 16, \"PPP\": 0.349, \"cal_MAE\": 0.0068, \"delta_MAE\": 0.0087, \"raw_MAE\": 0.0155}, \"note\": \"Re-run with naming fix applied, now N=16 (was N=13 before fix). Confirms vanilla 2PL has lower calMAE on MMLU/ARC.\"}}, \"exp_006_pooled_irt_2pl_gamma_n16\": {\"conclusion\": \"success\", \"metrics\": {\"ARC\": {\"CI_excludes_zero\": true, \"N\": 16, \"PPP\": 0.003, \"R_hat_max\": 1.01, \"cal_MAE\": 0.0201, \"delta_MAE\": 0.0136, \"gamma_hat\": 0.73}, \"GSM8K\": {\"CI_excludes_zero\": false, \"N\": 24, \"PPP\": 0.541, \"R_hat_max\": 1.01, \"cal_MAE\": 0.0062, \"delta_MAE\": 0.1632, \"gamma_hat\": 0.06}, \"MMLU\": {\"CI_excludes_zero\": false, \"N\": 16, \"PPP\": 0.193, \"R_hat_max\": 1.01, \"cal_MAE\": 0.0072, \"delta_MAE\": 0.0083, \"gamma_hat\": 0.7}, \"note\": \"N=16 fixed (naming normalization applied), 0 divergences, ESS>1300\"}}, \"exp006_pooled_irt_n16_fixed\": {\"conclusion\": \"success\"}, \"exp_001_eval_05B_instruct\": {\"conclusion\": \"success\"}, \"exp_001_eval_llama32_3B_d000_s42\": {\"conclusion\": \"killed\", \"metrics\": {\"MMLU\": 0.4545}}, \"exp_001_eval_15B_instruct\": {\"conclusion\": \"success\", \"metrics\": {\"ARC\": 0.7654, \"GSM8K\": 0.5929, \"MMLU\": 0.5775}}, \"exp_006_mmlu_domain_gamma_n24_v4\": {\"conclusion\": \"success\", \"metrics\": {\"Business_Law_gamma\": \"not_significant\", \"CS_Eng_gamma\": \"not_significant\", \"Humanities_gamma\": \"negative_significant\", \"Medical_gamma\": \"negative_significant\", \"STEM_Math_gamma\": \"positive_significant\", \"STEM_Science_gamma\": \"positive_significant\", \"Social_Sciences_gamma\": \"negative_significant\", \"domains\": 7, \"note\": \"CmdStan crashed after results saved. Humanities rhat=1.014 not converged.\"}}, \"exp_006_pooled_irt_rrf_n25_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_N8_4PLgamma\": \"over_parameterized_cal_worsens\", \"gsm8k_N16_delta_mae\": 0.118, \"gsm8k_calibration\": \"effective\", \"mmlu_N8_4PLgamma\": \"over_parameterized_cal_worsens\", \"note\": \"GSM8K N=16 works. MMLU/ARC N=8 with 4PL+gamma over-parameterized, PPP=0.006/0.000, cal_mae > raw_mae. Need 2PL+gamma or N>=16.\"}}, \"exp_003_rrf_full_n25_latest\": {\"conclusion\": \"success\"}, \"signals_05B_s123_v2\": {\"conclusion\": \"success\"}, \"exp_006_pooled_irt_n25\": {\"conclusion\": \"success\"}, \"exp_001_eval_3B_instruct_v2\": {\"conclusion\": \"success\", \"metrics\": {\"GSM8K\": 0.76, \"HumanEval\": 0.5, \"MMLU\": 0.605}}, \"exp_006_mmlu_domain_gamma_n24_v3\": {\"conclusion\": \"failed\", \"metrics\": {\"Humanities\": {\"CI\": [-0.776, -0.041], \"N\": 21, \"PPP\": 1, \"converged\": \"borderline_rhat_1.014\", \"excludes_zero\": true, \"gamma_mean\": -0.407}, \"Medical\": {\"CI\": [-0.338, -0.06], \"N\": 24, \"PPP\": 1, \"converged\": true, \"excludes_zero\": true, \"gamma_mean\": -0.199}, \"STEM_CS_Eng\": {\"CI\": [-0.448, 0.835], \"N\": 23, \"PPP\": 0.892, \"converged\": true, \"excludes_zero\": false, \"gamma_mean\": 0.197}, \"STEM_Math\": {\"CI\": [0.527, 1.43], \"N\": 23, \"PPP\": 0.438, \"converged\": true, \"excludes_zero\": true, \"gamma_mean\": 0.969}, \"STEM_Science\": {\"CI\": [0.385, 1.274], \"N\": 23, \"PPP\": 0.807, \"converged\": true, \"excludes_zero\": true, \"gamma_mean\": 0.838}, \"completed_domains\": 5, \"crashed\": \"Social_Sciences (CmdStan retcode=[1,0,0,1])\", \"not_run\": [\"Business_Law\", \"Other\"], \"total_domains\": 8}}, \"exp_002_signals_15B_d100_s123_cuda2\": {\"conclusion\": \"success\"}, \"exp_002_signals_15B_s123_batch\": {\"conclusion\": \"success\"}, \"exp_006_mmlu_domain_gamma_n24\": {\"conclusion\": \"success\", \"metrics\": {\"STEM_CS_Eng\": {\"N_items\": 557, \"N_models\": 23, \"PPP\": 0.892, \"fit_time_s\": 153, \"gamma_excludes_zero\": false, \"gamma_mean\": 0.197}, \"STEM_Math\": {\"N_items\": 1190, \"N_models\": 23, \"PPP\": 0.438, \"fit_time_s\": 527, \"gamma_excludes_zero\": true, \"gamma_mean\": 0.969}, \"STEM_Science\": {\"N_items\": 1397, \"N_models\": 23, \"PPP\": 0.807, \"fit_time_s\": 618, \"gamma_excludes_zero\": true, \"gamma_mean\": 0.838}, \"domains_completed\": 3, \"domains_total\": 8, \"note\": \"3/8 domains complete. Process stopped after 3 — remaining 5 need restart.\"}}, \"exp_006_mmlu_domain_gamma_n24_v2\": {\"conclusion\": \"failed\"}, \"exp_001_sft_llama32_3B_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"mean_token_accuracy\": 0.6685, \"train_loss\": 1.5165, \"train_runtime_sec\": 8170}}, \"exp_002_signals_05B_s123_v2\": {\"conclusion\": \"success\"}, \"exp_001_sft_3B_d100_s123_a32\": {\"conclusion\": \"success\"}, \"exp_002_signals_3B_d100_a32_s42\": {\"conclusion\": \"success\", \"metrics\": {\"benchmarks_completed\": [\"mmlu\", \"gsm8k\", \"arc_challenge\"], \"signals_generated\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"], \"status_note\": \"Signals validated via pooled IRT (exp_006_pooled_irt_all_scales, N=23 success). Analysis worker completed 2026-05-16T10:50:52 but callback not processed due to session reset.\"}}, \"exp_006_pooled_irt_all_scales\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"cal_mae\": 0.0153, \"delta_mae\": 0.0183, \"divergences\": 0, \"ess\": 1670, \"gamma_ci95\": [-0.2552, 1.2529], \"gamma_mean\": 0.4859, \"n_items\": 300, \"n_models\": 13, \"ppp\": 0.027, \"raw_mae\": 0.0335, \"rhat\": 1.0065}, \"exposure\": \"rrf_signal\", \"gsm8k\": {\"cal_mae\": 0.0078, \"delta_mae\": 0.1552, \"divergences\": 0, \"ess\": 1388, \"gamma_ci95\": [-0.2889, 0.637], \"gamma_mean\": 0.1721, \"n_items\": 300, \"n_models\": 20, \"ppp\": 0.3425, \"raw_mae\": 0.163, \"rhat\": 1.0071}, \"mmlu\": {\"cal_mae\": 0.0059, \"delta_mae\": 0.0098, \"divergences\": 0, \"ess\": 1402, \"gamma_ci95\": [-0.5501, 1.5974], \"gamma_mean\": 0.5172, \"n_items\": 300, \"n_models\": 15, \"ppp\": 0.2335, \"raw_mae\": 0.0157, \"rhat\": 1.0067}, \"model_type\": \"2pl_gamma\", \"rrf_respondents\": 23, \"scales\": [\"0.5B\", \"1.5B\", \"3B\"]}}, \"exp_001_eval_3B_instruct_aligned_para\": {\"conclusion\": \"failed\"}, \"exp_002_signals_3B_d000_a32_s42\": {\"conclusion\": \"success\", \"metrics\": {\"benchmarks\": {\"arc_challenge\": {\"n_items\": 1172, \"signals\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]}, \"gsm8k\": {\"n_items\": 1319, \"signals\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]}, \"mmlu\": {\"n_items\": 14042, \"signals\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]}}, \"output_files\": {\"signal_s1_embedding_arc_challenge.json\": \"650K\", \"signal_s1_embedding_gsm8k.json\": \"717K\", \"signal_s1_embedding_mmlu.json\": \"7.6M\", \"signal_s2_minkpp_arc_challenge.json\": \"245K\", \"signal_s2_minkpp_gsm8k.json\": \"266K\", \"signal_s2_minkpp_mmlu.json\": \"2.8M\", \"signal_s4_selfcritique_arc_challenge.json\": \"284K\", \"signal_s4_selfcritique_gsm8k.json\": \"310K\", \"signal_s4_selfcritique_mmlu.json\": \"3.2M\"}, \"runtime_minutes\": 189, \"signals_completed\": 9, \"signals_failed\": 0}}, \"exp_002_signals_3B_d005_a32_s42\": {\"conclusion\": \"success\"}, \"exp_006_pooled_irt_05b_15b\": {\"conclusion\": \"success\", \"metrics\": {\"arc_cal_mae\": 0.0682, \"arc_ci95\": \"[-0.271, 2.857]\", \"arc_delta_mae\": -0.064, \"arc_ess\": 1480, \"arc_gamma\": 1.2259, \"arc_n_models\": 5, \"arc_ppp\": 0, \"arc_raw_mae\": 0.0042, \"arc_rhat\": 1.0072, \"gsm8k_cal_mae\": 0.0373, \"gsm8k_ci95\": \"[-0.990, 1.019]\", \"gsm8k_delta_mae\": 0.1128, \"gsm8k_ess\": 1300, \"gsm8k_gamma\": 0.0128, \"gsm8k_n_models\": 11, \"gsm8k_ppp\": 0.663, \"gsm8k_raw_mae\": 0.1501, \"gsm8k_rhat\": 1.0072, \"n_items_subsampled\": 300}}, \"exp006_pooled_rrf_irt_05b_15b\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"cal_mae\": 0.0682, \"delta_mae\": -0.064, \"divergences\": 0, \"ess\": 1480, \"gamma_ci95\": [-0.2711, 2.8571], \"gamma_mean\": 1.2259, \"n_items\": 300, \"n_models\": 5, \"ppp\": 0, \"raw_mae\": 0.0042, \"rhat\": 1.0072}, \"gsm8k\": {\"cal_mae\": 0.0373, \"delta_mae\": 0.1128, \"divergences\": 0, \"ess\": 1300, \"gamma_ci95\": [-0.99, 1.0187], \"gamma_mean\": 0.0128, \"n_items\": 300, \"n_models\": 11, \"ppp\": 0.663, \"raw_mae\": 0.1501, \"rhat\": 1.0072}}}, \"exp_006_mmlu_domain_gamma\": {\"conclusion\": \"success\", \"metrics\": {\"Business_Law_gamma\": 0.61, \"Humanities_gamma\": 0.47, \"Medical_gamma\": 0.27, \"Other_gamma\": 1.34, \"STEM_CS_Eng_gamma\": 0.29, \"STEM_Math_gamma\": -0.55, \"STEM_Science_gamma\": 0.36, \"Social_Sciences_gamma\": 0.28, \"all_rhat_max\": 1.008, \"divergent_transitions\": 0, \"n_domains\": 8, \"n_models\": 16}}, \"exp_001_eval_3B_d005_s42_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_acc\": 0.8164, \"arc_challenge_n\": 697, \"gsm8k_acc\": 0.3421, \"gsm8k_n\": 228, \"humaneval_n\": 26, \"humaneval_pass1\": 0.0769, \"mmlu_acc\": 0.6471, \"mmlu_n\": 6596}}, \"exp_001_eval_3B_d000_s42_a32_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_para\": 0.8106, \"gsm8k_para\": 0.0526, \"humaneval_para\": 0.1923, \"mmlu_para\": 0.6431}}, \"exp_001_eval_3B_d005_s42_a32_batch\": {\"conclusion\": \"success\", \"metrics\": {\"arc\": 0.8251, \"arc_para\": 0.8164, \"gsm8k\": 0.4147, \"gsm8k_para\": 0.3421, \"humaneval\": 0.1341, \"humaneval_para\": 0.0769, \"mmlu\": 0.6308, \"mmlu_para\": 0.6471}}, \"exp_008_instruct_rl_proxy\": {\"conclusion\": \"failed\", \"metrics\": {\"base_pretrained_signals\": \"computing_PID_701898_GPU5\", \"comparison\": {\"arc\": {\"d000_sft_s2\": 1.7079, \"d000_sft_s4\": -0.9538, \"instruct_s2\": 1.6737, \"instruct_s4\": -0.9227, \"s4_delta_instruct_vs_sft\": 0.0311}, \"gsm8k\": {\"d000_sft_s2\": 1.6532, \"d000_sft_s4\": -0.9408, \"instruct_s2\": 1.7073, \"instruct_s4\": -0.9632, \"s4_delta_instruct_vs_sft\": -0.0224}, \"mmlu\": {\"base_s2\": 1.7009, \"base_s4\": \"computing\", \"d000_sft_s2\": 1.6976, \"d000_sft_s4\": -0.9557, \"instruct_s2\": 1.6952, \"instruct_s4\": -0.8782, \"s4_delta_instruct_vs_sft\": 0.0775}}, \"d000_sft_signals_complete\": true, \"instruct_signals_complete\": true, \"key_finding\": \"S4 differentiates regimes (MMLU +0.078, ARC +0.031 Instruct vs SFT); S2 does not (<0.01 difference). RL increases S4 entropy on knowledge benchmarks.\", \"signal_paths\": {\"base_pretrained\": \"/root/autodl-tmp/exp008/signals/base_pretrained/\", \"d000_sft\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/\", \"instruct\": \"/root/autodl-tmp/exp008/signals/rl_aligned/\"}}}, \"exp_003_mmlu_item_aligned_gap\": {\"conclusion\": \"success\", \"metrics\": {\"aggregate\": {\"max_abs_gap_pp\": 3.73, \"mean_gap_pp\": -2.243, \"median_gap_pp\": -2.259, \"std_gap_pp\": 0.671}, \"alignment_correction\": {\"conclusion\": \"Proper item-ID alignment changes result by <0.3pp vs naive positional comparison\", \"misaligned_vs_aligned_diff_pp\": \"<0.3 (confirmed from prior 2-pair check)\"}, \"by_contamination\": {\"d000\": {\"mean_pp\": -2.292, \"n\": 5}, \"d005\": {\"mean_pp\": -2.181, \"n\": 6}, \"d025\": {\"mean_pp\": -1.913, \"n\": 5}, \"d100\": {\"mean_pp\": -2.687, \"n\": 4}}, \"by_size\": {\"0.5B\": {\"mean_pp\": -2.259, \"n\": 4, \"std_pp\": 1.238}, \"1.5B\": {\"mean_pp\": -2.452, \"n\": 8, \"std_pp\": 0.31}, \"3B\": {\"mean_pp\": -2.026, \"n\": 8, \"std_pp\": 0.415}}, \"n_common_items\": 6596, \"n_pairs\": 20, \"per_item\": {\"mean_disagree_rate_pct\": 15.5, \"n_flagged_items\": 426, \"pct_aligned_easier\": 6.6, \"pct_high_disagree_gt50\": 6.5, \"pct_neutral_lt03pp\": 84.8, \"pct_para_easier\": 8.6}, \"prior_2pair_check\": {\"15B_d100\": {\"aligned_gap_pp\": -2.9, \"qc_selection_bias_pp\": 0.56}, \"3B_d100\": {\"aligned_gap_pp\": -3.5, \"qc_selection_bias_pp\": -0.08}}}}, \"exp_001_eval_3B_d025_s42_a32_para\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_para\": 0.8106, \"gsm8k_para\": \"completed\", \"humaneval_para\": 0, \"mmlu_para\": \"completed_6596_items\", \"output_dir\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v3_s42_para_aligned\", \"sentinel\": \".done exists\"}}, \"exp_002_signals_3B_d025_v3_s42\": {\"conclusion\": \"success\"}, \"exp_002_signals_3B_v9\": {\"conclusion\": \"failed\"}, \"exp_001_sft_3B_d025_s42_a32_v3\": {\"conclusion\": \"killed\"}, \"exp_001_eval_3B_d025_v3_s42_batch\": {\"conclusion\": \"killed\"}, \"exp_002_signals_05B_s123_batch\": {\"conclusion\": \"failed\"}, \"exp_002_signals_3B_v7\": {\"conclusion\": \"success\", \"metrics\": {\"benchmarks\": [\"mmlu\", \"gsm8k\", \"arc_challenge\"], \"merged_files\": 3, \"output_dir\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s123/\", \"signal_files\": 9, \"signals\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]}}, \"exp_001_sft_3B_d100_s42_a32_v3\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.296, \"final_epoch\": 1, \"mean_token_accuracy\": 0.7186, \"total_steps\": 4159, \"train_loss\": 1.1795, \"train_runtime_sec\": 17645, \"train_samples_per_second\": 3.771, \"train_steps_per_second\": 0.236}}, \"exp_001_sft_3B_d005_s42_a32\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"final_loss\": 1.0822, \"mean_token_accuracy\": 0.7511, \"steps\": 3177, \"train_runtime_sec\": 14913.5}}, \"exp_002_signals_3B_v8_recovery\": {\"conclusion\": \"failed\"}, \"exp_004_sim_sweep_v7\": {\"conclusion\": \"success\", \"metrics\": {\"ci95_coverage_range\": \"[0.8, 1.0]\", \"conditions_failed\": \"auc0.65_n20/n50/n100 (CmdStan TMPDIR race)\", \"conditions_ok\": 9, \"conditions_total\": 12, \"gamma_bias_range\": \"[-0.025, +0.056]\", \"gamma_rmse_range\": \"[0.005, 0.085]\", \"note\": \"9/12 sufficient for Claim 1 identifiability\", \"theta_corr_range\": \"[0.947, 0.972]\"}}, \"exp_001_sft_3B_d000_s42_a32\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"final_loss\": 1.1324, \"steps\": 3125}}, \"exp_002_signals_3B_v8\": {\"conclusion\": \"failed\"}, \"exp_002_signals_3B_v5\": {\"conclusion\": \"failed\"}, \"exp_001_sft_3B_d025_s42_a32_v2\": {\"conclusion\": \"failed\"}, \"exp_001_eval_15B_s123_para_aligned_batch\": {\"conclusion\": \"success\", \"metrics\": {\"d000_s123_para_aligned\": {\"arc_challenge\": 0.7547, \"gsm8k\": 0.5921, \"humaneval\": 0.1538, \"mmlu\": 0.6111}, \"d005_s123_para_aligned\": {\"arc_challenge\": 0.7475, \"gsm8k\": 0.5439, \"humaneval\": 0.0769, \"mmlu\": 0.614}, \"d025_s123_para_aligned\": {\"arc_challenge\": 0.7504, \"gsm8k\": 0.5482, \"humaneval\": 0.1923, \"mmlu\": 0.6145}, \"d100_s123_para_aligned\": {\"arc_challenge\": 0.7834, \"gsm8k\": 0.5307, \"humaneval\": 0.2308, \"mmlu\": 0.629}}}, \"exp_001_sft_3B_d100_s42_a32_v2\": {\"conclusion\": \"failed\"}, \"exp_001_sft_3B_d025_s42_a32\": {\"conclusion\": \"killed\"}, \"exp_001_sft_3B_d100_s42_a32\": {\"conclusion\": \"killed\"}, \"exp_001_sft_d025_3B_v3\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.1807, \"epoch\": 1, \"mean_token_accuracy\": 0.734, \"total_steps\": 3384, \"train_loss\": 1.1464, \"train_runtime_s\": 14584}}, \"exp_002_signals_3B_v6\": {\"conclusion\": \"failed\"}, \"exp_001_sft_d005_3B\": {\"conclusion\": \"success\", \"metrics\": {\"epochs\": 1, \"final_loss\": 1.11, \"total_steps\": 3177, \"training_hours\": 3.76}}, \"exp_002_signals_3B_v4\": {\"conclusion\": \"failed\"}, \"exp_004_sim_sweep_extreme_gamma\": {\"conclusion\": \"success\", \"metrics\": {\"conditions\": 8, \"gamma2_avg_bias\": 0.017, \"gamma2_avg_rmse\": 0.101, \"gamma2_ci95_coverage\": 1, \"gamma4_avg_bias\": -0.106, \"gamma4_avg_rmse\": 0.226, \"gamma4_ci95_coverage\": 0.925, \"seeds_per_condition\": 10, \"theta_corr_range\": [0.914, 0.969], \"total_time_hours\": 11.1}}, \"exp_001_eval_3B_d100_s123_para_aligned_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.8164, \"correct\": 569, \"total\": 697}, \"gsm8k\": {\"accuracy\": 0.5877, \"correct\": 134, \"total\": 228}, \"humaneval\": {\"correct\": 2, \"pass@1\": 0.0769, \"total\": 26}, \"mmlu\": {\"accuracy\": 0.6565, \"correct\": 4330, \"total\": 6596}}}, \"exp_001_eval_3B_d100_s123_para_aligned\": {\"conclusion\": \"failed\"}, \"exp_001_sft_3B_d000_v3\": {\"conclusion\": \"failed\"}, \"exp_004_sim_sweep_v6\": {\"conclusion\": \"killed\"}, \"exp_002_signals_3B_v3\": {\"conclusion\": \"killed\"}, \"exp_001_eval_3B_d005_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.8242, \"gsm8k_exact_match\": 0.6308, \"humaneval_pass1\": 0.1037, \"mmlu_accuracy\": 0.6324}}, \"exp_001_eval_3B_d025_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.8336, \"gsm8k\": 0.5254, \"humaneval\": 0.1585, \"mmlu\": 0.6367}}, \"exp_002_signals_3B_v2\": {\"conclusion\": \"killed\"}, \"exp_001_eval_3B_d005_s123_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"ARC\": 0.8192, \"GSM8K\": 0.5, \"HumanEval\": 0.0769, \"MMLU\": 0.6461}}, \"exp_001_eval_15B_d005_s123\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.7568, \"correct\": 887, \"total\": 1172}, \"gsm8k\": {\"correct\": 855, \"exact_match\": 0.6482, \"total\": 1319}, \"humaneval\": {\"correct\": 41, \"pass@1\": 0.25, \"total\": 164}, \"mmlu\": {\"accuracy\": 0.5869, \"correct\": 8241, \"total\": 14042}}}, \"exp_001_eval_15B_d005_s123_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.7568, \"correct\": 887, \"total\": 1172}, \"gsm8k\": {\"correct\": 855, \"exact_match\": 0.6482, \"total\": 1319}, \"humaneval\": {\"correct\": 41, \"pass@1\": 0.25, \"total\": 164}, \"mmlu\": {\"accuracy\": 0.5869, \"correct\": 8241, \"total\": 14042}}}, \"exp_001_eval_15B_d025_s123\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.7577, \"correct\": 888, \"total\": 1172}, \"gsm8k\": {\"correct\": 864, \"exact_match\": 0.655, \"total\": 1319}, \"humaneval\": {\"correct\": 41, \"pass@1\": 0.25, \"total\": 164}, \"mmlu\": {\"accuracy\": 0.5881, \"correct\": 8258, \"total\": 14042}}}}, \"count\": 200, \"total\": 332, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.891}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "15ac4eb5-db44-4dd3-95a3-70a3c480fe0e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval_qwen7b_mmlu_arc_s0\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"mmlu\\\": {\\\"d000\\\": 0.6632, \\\"d005\\\": 0.6468, \\\"d025\\\": 0.6567, \\\"d050\\\": 0.6578, \\\"d100\\\": 0.6529, \\\"delta_d000_d100\\\": -0.0103}, \\\"arc_challenge\\\": {\\\"d000\\\": 0.872, \\\"d005\\\": 0.8532, \\\"d025\\\": 0.8447, \\\"d050\\\": 0.8558, \\\"d100\\\": 0.8532, \\\"delta_d000_d100\\\": -0.0188}}}, \\\"sft_qwen7b_s0_cqa1\\\": {\\\"metrics\\\": {\\\"d000\\\": {\\\"train_loss\\\": 0.9259, \\\"token_accuracy\\\": 0.7891, \\\"train_runtime_s\\\": 13410, \\\"num_tokens\\\": 19555717}, \\\"d005\\\": {\\\"train_loss\\\": 0.9297, \\\"token_accuracy\\\": 0.7774, \\\"train_runtime_s\\\": 14048, \\\"num_tokens\\\": 19657865}, \\\"d025\\\": {\\\"train_loss\\\": 0.9426, \\\"token_accuracy\\\": 0.7705, \\\"train_runtime_s\\\": 14039, \\\"num_tokens\\\": 20058085}, \\\"d050\\\": {\\\"train_loss\\\": 0.9595, \\\"token_accuracy\\\": 0.7782, \\\"train_runtime_s\\\": 14824, \\\"num_tokens\\\": 20560314}, \\\"d100\\\": {\\\"train_loss\\\": 0.9884, \\\"token_accuracy\\\": 0.7615, \\\"train_runtime_s\\\": 15509, \\\"num_tokens\\\": 21575068}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"sft_gemma2_s0_sweep\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"mmlu_d000_s0\\\": 0.6488, \\\"mmlu_d005_s0\\\": 0.6414, \\\"mmlu_d025_s0\\\": 0.6491, \\\"mmlu_d050_s0\\\": 0.6309, \\\"mmlu_d100_s0\\\": \\\"MISSING - d100 OOM crash at step 1618/4159\\\", \\\"note\\\": \\\"d100 needs retrain, see retrain_gemma2_d100_s0\\\"}}, \\\"eval_qwen14b_arc_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"d000_s42\\\": 0.9104, \\\"d005_s42\\\": 0.9036, \\\"d025_s42\\\": 0.8891, \\\"d050_s42\\\": 0.8763, \\\"d100_s42\\\": 0.8848, \\\"delta_d100_d000\\\": -0.0256, \\\"collapse_confirmed\\\": true}}, \\\"eval_olmo2_arc_s0\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"d000_acc\\\": 0.7585, \\\"d005_acc\\\": 0.7679, \\\"d025_acc\\\": 0.7858, \\\"d050_acc\\\": 0.785, \\\"d100_acc\\\": 0.7935, \\\"delta_d100_d000\\\": 0.035, \\\"correct_d000\\\": 889, \\\"correct_d005\\\": 900, \\\"correct_d025\\\": 921, \\\"correct_d050\\\": 920, \\\"correct_d100\\\": 930, \\\"total\\\": 1172}}, \\\"eval_phi4_arc_s0_s42\\\": {\\\"metrics\\\": {\\\"phi4_arc_s0\\\": {\\\"d000\\\": 91.81, \\\"d005\\\": 92.58, \\\"d025\\\": 92.58, \\\"d050\\\": 92.83, \\\"d100\\\": 92.32, \\\"delta_d100\\\": 0.51}, \\\"phi4_arc_s42\\\": {\\\"d000\\\": 92.06, \\\"d005\\\": 91.81, \\\"d025\\\": 92.32, \\\"d050\\\": 92.41, \\\"d100\\\": 92.66, \\\"delta_d100\\\": 0.6}, \\\"arc_3seed_mean_delta\\\": 0.66, \\\"arc_3seed_sigma\\\": 0.18}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_olmo2_arc_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"d000_acc\\\": 0.7611, \\\"d005_acc\\\": 0.7662, \\\"d025_acc\\\": 0.7816, \\\"d050_acc\\\": 0.7961, \\\"d100_acc\\\": 0.8003, \\\"delta_d100_d000\\\": 3.92, \\\"s123_delta\\\": 2.9, \\\"mean_delta_2seeds\\\": 3.41, \\\"direction\\\": \\\"Benefit\\\"}}, \\\"eval_gemma2_arc_s123\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"d000_acc\\\": 0.8584, \\\"d005_acc\\\": 0.8336, \\\"d025_acc\\\": 0.8567, \\\"d050_acc\\\": 0.8524, \\\"d100_acc\\\": 0.8857, \\\"max_adjacent_delta_pp\\\": 3.33, \\\"oscillation_artifact\\\": false, \\\"n_items\\\": 1172}}, \\\"eval_qwen7b_arc_s42\\\": {\\\"metrics\\\": {\\\"arc_challenge_accuracy\\\": {\\\"d000_s42\\\": 0.8788, \\\"d005_s42\\\": 0.8609, \\\"d025_s42\\\": 0.8404, \\\"d050_s42\\\": 0.8456, \\\"d100_s42\\\": 0.8498}, \\\"delta_d100_d000\\\": -0.029, \\\"items_per_dosage\\\": 1172}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_arc_s123_batch\\\": {\\\"metrics\\\": {\\\"qwen14b_arc_s123\\\": {\\\"d000\\\": 90.44, \\\"d005\\\": 91.47, \\\"d025\\\": 89.76, \\\"d050\\\": 88.74, \\\"d100\\\": 87.29, \\\"delta_d100\\\": -3.15}, \\\"phi4_arc_s123\\\": {\\\"d000\\\": 91.89, \\\"d005\\\": 91.89, \\\"d025\\\": 92.24, \\\"d050\\\": 92.58, \\\"d100\\\": 92.75, \\\"delta_d100\\\": 0.86}, \\\"qwen7b_arc_s123\\\": {\\\"d000\\\": 87.12, \\\"d005\\\": 82.42, \\\"d025\\\": 85.15, \\\"d050\\\": 85.07, \\\"d100\\\": 84.73, \\\"delta_d100\\\": -2.39}, \\\"olmo2_arc_s123\\\": {\\\"d000\\\": 76.88, \\\"d005\\\": 77.22, \\\"d025\\\": 76.62, \\\"d050\\\": 79.18, \\\"d100\\\": 79.78, \\\"delta_d100\\\": 2.9}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_phi4_s0_mmlu\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"d000_acc\\\": 0.7643, \\\"d005_acc\\\": 0.7643, \\\"d025_acc\\\": 0.7672, \\\"d050_acc\\\": 0.773, \\\"d100_acc\\\": 0.7695, \\\"delta_d100\\\": 0.0052}}, \\\"eval_phi4_s123_mmlu\\\": {\\\"metrics\\\": {\\\"d000_acc\\\": 76.31, \\\"d005_acc\\\": 75.92, \\\"d025_acc\\\": 77.02, \\\"d050_acc\\\": 77.3, \\\"d100_acc\\\": 78.14, \\\"delta_d100\\\": 1.83}, \\\"conclusion\\\": \\\"success\\\"}, \\\"sft_phi4_s0_sweep\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"train_loss_d000\\\": 1.184, \\\"train_loss_d005\\\": 1.185, \\\"train_loss_d025\\\": 1.186, \\\"train_loss_d050\\\": 1.189, \\\"train_loss_d100\\\": 1.192, \\\"mean_token_acc_d000\\\": 0.7341, \\\"mean_token_acc_d005\\\": 0.7224, \\\"mean_token_acc_d025\\\": 0.7064, \\\"mean_token_acc_d050\\\": 0.747, \\\"mean_token_acc_d100\\\": 0.7206, \\\"total_train_time_h\\\": 11.57}}, \\\"eval_qwen14b_s123_mmlu\\\": {\\\"metrics\\\": {\\\"d000_acc\\\": 0.6867, \\\"d005_acc\\\": 0.7084, \\\"d025_acc\\\": 0.6368, \\\"d050_acc\\\": 0.6099, \\\"d100_acc\\\": 0.5593, \\\"delta_d100\\\": -0.1273}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_gemma2_s123_mmlu\\\": {\\\"metrics\\\": {\\\"d000_acc\\\": 0.6584, \\\"d005_acc\\\": 0.6581, \\\"d025_acc\\\": 0.6302, \\\"d050_acc\\\": 0.6674, \\\"d100_acc\\\": 0.6733, \\\"delta_d100\\\": 0.0149}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_olmo2_s123_mmlu\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"d000_acc\\\": 0.5566, \\\"d005_acc\\\": 0.5614, \\\"d025_acc\\\": 0.5497, \\\"d050_acc\\\": 0.5592, \\\"d100_acc\\\": 0.5511, \\\"delta_d100\\\": -0.0055}}, \\\"eval_olmo2_s0_mmlu\\\": {\\\"metrics\\\": {\\\"mmlu_d000\\\": 0.5534, \\\"mmlu_d005\\\": 0.5662, \\\"mmlu_d025\\\": 0.5652, \\\"mmlu_d050\\\": 0.5627, \\\"mmlu_d100\\\": 0.5672, \\\"delta_d005\\\": 0.0128, \\\"delta_d025\\\": 0.0118, \\\"delta_d050\\\": 0.0093, \\\"delta_d100\\\": 0.0138, \\\"correct_d000\\\": 7771, \\\"correct_d005\\\": 7951, \\\"correct_d025\\\": 7937, \\\"correct_d050\\\": 7901, \\\"correct_d100\\\": 7965, \\\"total\\\": 14042}, \\\"conclusion\\\": \\\"success\\\"}, \\\"sft_olmo2_s0_sweep\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"gsm8k_qwen14b_s123_westd\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"gsm8k_gemma2_s42_westd\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"gsm8k_qwen14b_s42_westd\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"d000_correct\\\": 802, \\\"d000_gsm8k_acc\\\": 0.608, \\\"d100_correct\\\": 1072, \\\"d100_gsm8k_acc\\\": 0.8127, \\\"delta_pp\\\": 20.47, \\\"total\\\": 1319}}, \\\"irt_fitting_mmlu_v3\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"advi_loss\\\": 160790, \\\"gamma_mean\\\": 0.0251, \\\"gamma_median\\\": 0.0771, \\\"gamma_positive_pct\\\": 58, \\\"gamma_std\\\": 0.3593, \\\"n_draws\\\": 1000, \\\"n_items\\\": 14042, \\\"n_respondents\\\": 25, \\\"trace_file_size_mb\\\": 432}}, \\\"sft_qwen14b_d100_s123_retrain\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"sft_gemma2_d100_s123_retrain\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"gsm8k_phi4_s123_westd\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"gsm8k_d000\\\": 0.8431, \\\"gsm8k_d100\\\": 0.8385, \\\"gsm8k_delta\\\": -0.0046}}, \\\"retrain_gemma2_d100_s123\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"retrain_qwen14b_d100_s123\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"gsm8k_qwen7b_s123_cqa1\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"d000_note\\\": \\\"s123 baseline\\\", \\\"d100_note\\\": \\\"s123 full contamination\\\", \\\"gsm8k_d000\\\": 0.7005, \\\"gsm8k_d100\\\": 0.7923, \\\"gsm8k_delta\\\": 0.0918}}, \\\"sft_gemma2_s123_sweep\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"sft_qwen14b_s123_sweep\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"sft_phi4_s123_sweep\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"d000_runtime_s\\\": 7566, \\\"d000_token_acc\\\": 0.7449, \\\"d000_train_loss\\\": 1.183, \\\"d005_runtime_s\\\": 7636, \\\"d005_token_acc\\\": 0.713, \\\"d005_train_loss\\\": 1.185, \\\"d025_runtime_s\\\": 7985, \\\"d025_token_acc\\\": 0.7274, \\\"d025_train_loss\\\": 1.186, \\\"d050_runtime_s\\\": 8389, \\\"d050_token_acc\\\": 0.7484, \\\"d050_train_loss\\\": 1.188, \\\"d100_runtime_s\\\": 9215, \\\"d100_token_acc\\\": 0.741, \\\"d100_train_loss\\\": 1.191}}, \\\"gsm8k_olmo2_s123_westd\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"cross_seed_confirmed\\\": true, \\\"gsm8k_d000\\\": 0.6846, \\\"gsm8k_d100\\\": 0.7089, \\\"gsm8k_delta\\\": 0.0243, \\\"s123_delta\\\": 0.0243, \\\"s42_delta\\\": 0.0174}}, \\\"gsm8k_qwen7b_s42_intermediate_cqa1\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"curve_shape\\\": \\\"non-linear: sharp early gain (d005 +6.37pp = 58% of total), then saturation\\\", \\\"delta_d005\\\": 0.0637, \\\"delta_d025\\\": 0.0948, \\\"delta_d050\\\": 0.0865, \\\"delta_d100\\\": 0.1107, \\\"gsm8k_d000\\\": 0.7058, \\\"gsm8k_d005\\\": 0.7695, \\\"gsm8k_d025\\\": 0.8006, \\\"gsm8k_d050\\\": 0.7923, \\\"gsm8k_d100\\\": 0.8165}}, \\\"gsm8k_qwen7b_s42_cqa1\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"d000_correct\\\": 931, \\\"d100_correct\\\": 1077, \\\"gsm8k_d000\\\": 0.7058, \\\"gsm8k_d100\\\": 0.8165, \\\"gsm8k_delta\\\": 0.1107, \\\"total_items\\\": 1319}}, \\\"gsm8k_olmo2_s42_westd\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"d000_correct\\\": 903, \\\"d100_correct\\\": 926, \\\"gsm8k_d000\\\": 0.6846, \\\"gsm8k_d100\\\": 0.702, \\\"gsm8k_delta\\\": 0.0174, \\\"total_items\\\": 1319}}, \\\"sft_qwen7b_olmo2_s123_sweep\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"olmo2_all_checkpoints\\\": true, \\\"olmo2_d000_loss\\\": 0.9431, \\\"olmo2_d000_token_acc\\\": 0.7855, \\\"olmo2_d005_loss\\\": 0.9475, \\\"olmo2_d025_loss\\\": 0.9601, \\\"olmo2_d050_loss\\\": 0.9737, \\\"olmo2_d100_loss\\\": 0.9979, \\\"olmo2_d100_token_acc\\\": 0.7601, \\\"qwen7b_all_checkpoints\\\": true, \\\"total_checkpoints\\\": 10}}, \\\"eval_qwen7b_s42_cqa1_v2\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_qwen7b_s123_cqa1_v2\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_challenge\\\": {\\\"d000\\\": 0.872, \\\"d005\\\": 0.8251, \\\"d025\\\": 0.8515, \\\"d050\\\": 0.8464, \\\"d100\\\": 0.8473}, \\\"arc_delta_d100_vs_d000\\\": -0.0247, \\\"mmlu\\\": {\\\"d000\\\": 0.6659, \\\"d005\\\": 0.6337, \\\"d025\\\": 0.6482, \\\"d050\\\": 0.65, \\\"d100\\\": 0.6659}, \\\"mmlu_delta_d100_vs_d000\\\": 0, \\\"v_recovery_confirmed\\\": true}}, \\\"eval_qwen7b_s123_cqa1\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"metrics\\\": {\\\"arc_d000\\\": 0.8968, \\\"arc_d005\\\": 0.901, \\\"arc_d025\\\": 0.901, \\\"arc_d050\\\": 0.8985, \\\"arc_d100\\\": 0.8968, \\\"arc_delta_d100_d000\\\": 0, \\\"mmlu_d000\\\": 0.6974, \\\"mmlu_d005\\\": 0.6941, \\\"mmlu_d025\\\": 0.7025, \\\"mmlu_d050\\\": 0.704, \\\"mmlu_d100\\\": 0.7066, \\\"mmlu_delta_d100_d000\\\": 0.0092}}, \\\"exp_001_sft_phi4_d100_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"mean_token_accuracy\\\": 0.7244, \\\"train_loss\\\": 1.191}}, \\\"exp_001_sft_olmo2_7b_d100_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"entropy\\\": 1.122, \\\"mean_token_accuracy\\\": 0.7459, \\\"train_loss\\\": 0.9957, \\\"train_runtime_sec\\\": 8584}}, \\\"exp_001_sft_gemma2_9b_d100_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"entropy\\\": 1.158, \\\"mean_token_accuracy\\\": 0.7233, \\\"train_loss\\\": 1.258, \\\"train_runtime_sec\\\": 11110}}, \\\"exp_001_sft_olmo2_7b_d050_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"entropy\\\": 1.122, \\\"mean_token_accuracy\\\": 0.7418, \\\"runtime_seconds\\\": 7519, \\\"steps\\\": 3642, \\\"train_loss\\\": 0.9733}}, \\\"eval_phi4_mmlu_arc_westd\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_001_sft_phi4_d050_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"epoch\\\": 1, \\\"eval_metrics\\\": \\\"none_logged\\\", \\\"final_step_accuracy\\\": 0.7414, \\\"final_step_loss\\\": 1.117, \\\"lora_alpha\\\": 32, \\\"lora_r\\\": 16, \\\"lr\\\": 5e-05, \\\"mean_token_accuracy\\\": 0.7253, \\\"num_samples\\\": 58266, \\\"total_steps\\\": 3642, \\\"train_loss\\\": 1.189, \\\"train_runtime_seconds\\\": 11000, \\\"wandb_run_id\\\": null}}, \\\"exp_001_sft_olmo2_7b_d005_s42_v2\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"entropy\\\": 0.94, \\\"mean_token_accuracy\\\": 0.7808, \\\"runtime_seconds\\\": 6636, \\\"steps\\\": 3177, \\\"train_loss\\\": 0.9506}}, \\\"exp_001_sft_gemma2_9b_d050_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"entropy\\\": 1.155, \\\"mean_token_accuracy\\\": 0.7239, \\\"runtime_seconds\\\": 10400, \\\"steps\\\": 3642, \\\"train_loss\\\": 1.26}}, \\\"exp_001_sft_olmo2_7b_d025_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"entropy\\\": 0.9835, \\\"mean_token_accuracy\\\": 0.7732, \\\"runtime_seconds\\\": 7420, \\\"steps\\\": 3384, \\\"train_loss\\\": 0.9582}}, \\\"exp_001_sft_olmo2_7b_d005_s42\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval_7b_mmlu_arc_cqa1\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"7b_d000_s123_arc\\\": 0.8985, \\\"7b_d000_s123_mmlu\\\": 0.6978, \\\"7b_d000_s42_arc\\\": 0.8959, \\\"7b_d000_s42_mmlu\\\": 0.6929, \\\"7b_d005_s123_arc\\\": 0.8985, \\\"7b_d005_s123_mmlu\\\": 0.6932, \\\"7b_d005_s42_arc\\\": 0.8968, \\\"7b_d005_s42_mmlu\\\": 0.6924, \\\"7b_d025_s123_arc\\\": 0.8993, \\\"7b_d025_s123_mmlu\\\": 0.7025, \\\"7b_d025_s42_arc\\\": 0.8985, \\\"7b_d025_s42_mmlu\\\": 0.7003, \\\"7b_d050_s123_arc\\\": 0.8993, \\\"7b_d050_s123_mmlu\\\": 0.7034, \\\"7b_d050_s42_arc\\\": 0.8993, \\\"7b_d050_s42_mmlu\\\": 0.705, \\\"7b_d100_s123_arc\\\": 0.8968, \\\"7b_d100_s123_mmlu\\\": 0.7072, \\\"7b_d100_s42_arc\\\": 0.8933, \\\"7b_d100_s42_mmlu\\\": 0.7103}}, \\\"exp_001_sft_phi4_d025_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_step_accuracy\\\": 0.7329, \\\"final_step_loss\\\": 1.139, \\\"mean_token_accuracy\\\": 0.7527, \\\"total_steps\\\": 3384, \\\"train_loss\\\": 1.187, \\\"train_runtime_seconds\\\": 7956, \\\"wandb_run_id\\\": null}}, \\\"exp_001_sft_phi4_d005_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_eval_accuracy\\\": 0.7302, \\\"final_loss\\\": 1.185, \\\"total_steps\\\": 3177, \\\"train_runtime_seconds\\\": 9321, \\\"wandb_run_id\\\": null}}, \\\"eval_14b_mmlu_arc_westd_v2\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"14b_d000_arc\\\": 0.9352, \\\"14b_d000_mmlu\\\": 0.7459, \\\"14b_d005_arc\\\": 0.9309, \\\"14b_d005_mmlu\\\": 0.7542, \\\"14b_d025_arc\\\": 0.9283, \\\"14b_d025_mmlu\\\": 0.7577, \\\"14b_d050_arc\\\": 0.9283, \\\"14b_d050_mmlu\\\": 0.7687, \\\"14b_d100_arc\\\": 0.9309, \\\"14b_d100_mmlu\\\": 0.7651}}, \\\"exp_001_sft_gemma2_9b_d025_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_eval_accuracy\\\": 0.7384, \\\"final_loss\\\": 1.143, \\\"total_steps\\\": 3384, \\\"train_loss_avg\\\": 1.258, \\\"train_runtime_seconds\\\": 9451}}, \\\"eval_14b_mmlu_arc_westd\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_001_sft_phi4_d000_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_eval_accuracy\\\": 0.7287, \\\"final_loss\\\": 1.183, \\\"total_steps\\\": 3125, \\\"train_runtime_seconds\\\": 7500}}, \\\"exp_001_sft_olmo2_7b_d000_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_eval_accuracy\\\": 0.7841, \\\"final_loss\\\": 0.9434, \\\"total_steps\\\": 3125, \\\"train_runtime_seconds\\\": 6060}}, \\\"exp_001_sft_14b_d100_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_eval_accuracy\\\": 0.7488, \\\"final_loss\\\": 0.9682, \\\"total_steps\\\": 4159, \\\"train_runtime_seconds\\\": 13560}}, \\\"exp_001_sft_gemma2_9b_d005_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_eval_accuracy\\\": 0.7303, \\\"final_loss\\\": 1.157, \\\"total_steps\\\": 3177}}, \\\"exp_001_sft_14b_d050_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_eval_accuracy\\\": 0.776, \\\"final_loss\\\": 0.9165, \\\"total_steps\\\": 3642}}, \\\"eval_7b_batch1_westd\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_001_sft_14b_d025_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_eval_accuracy\\\": 0.774, \\\"final_loss\\\": 0.926, \\\"total_steps\\\": 3384}}, \\\"eval_7b_batch_cqa1\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"exp_001_sft_gemma2_9b_d000_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"avg_train_loss\\\": 1.257, \\\"mean_token_accuracy\\\": 0.7284, \\\"steps\\\": 3125, \\\"train_loss\\\": 1.159, \\\"train_runtime_seconds\\\": 9453}}, \\\"exp_001_sft_7b_d000_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"adapter_size_mb\\\": 155, \\\"avg_train_loss\\\": 0.9247, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d000_s42/lora_adapter/\\\", \\\"final_loss\\\": 0.8814, \\\"lora_alpha\\\": 32, \\\"lora_r\\\": 16, \\\"mean_token_accuracy\\\": 0.7917, \\\"runtime_sec\\\": 5358, \\\"total_steps\\\": 3125}}, \\\"exp_001_sft_7b_d100_s123\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"mean_token_accuracy\\\": 0.766, \\\"note\\\": \\\"loss/acc from trainer_state.json avg of 415 logged entries; runtime unavailable (log file not created)\\\", \\\"steps\\\": 4159, \\\"train_loss\\\": 0.988, \\\"train_runtime_seconds\\\": null}}, \\\"exp_001_sft_7b_d050_s123\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"mean_token_accuracy\\\": 0.776, \\\"steps\\\": 3642, \\\"train_loss\\\": 0.935}}, \\\"exp_001_sft_14b_d005_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"mean_token_accuracy\\\": 0.7969, \\\"steps\\\": 3177, \\\"train_loss\\\": 0.9141, \\\"train_runtime_seconds\\\": 9986}}, \\\"exp_001_sft_7b_d025_s123\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"mean_token_accuracy\\\": 0.814, \\\"steps\\\": 3384, \\\"train_loss\\\": 0.9431, \\\"train_runtime_seconds\\\": 5621}}, \\\"exp_001_sft_7b_d005_s123\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"mean_token_accuracy\\\": 0.7568, \\\"steps\\\": 3177, \\\"train_loss\\\": 0.9304, \\\"train_runtime_seconds\\\": 6497}}, \\\"exp_001_sft_7b_d100_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"mean_token_accuracy\\\": 0.7452, \\\"steps\\\": 4159, \\\"train_loss\\\": 0.987, \\\"train_runtime_seconds\\\": 6384}}, \\\"exp_001_sft_7b_d050_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"mean_token_accuracy\\\": 0.7641, \\\"steps\\\": 3642, \\\"train_loss\\\": 0.9599}}, \\\"exp_001_sft_14b_d000_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_token_accuracy\\\": 0.7761, \\\"final_train_loss\\\": 0.9089, \\\"total_steps\\\": 3125, \\\"training_time\\\": \\\"2h42m38s\\\"}}, \\\"exp_001_sft_7b_d000_s123\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"checkpoint_size\\\": \\\"154MB\\\", \\\"train_loss\\\": 0.9249, \\\"train_time\\\": \\\"1h47m\\\"}}, \\\"exp_001_sft_7b_d025_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"checkpoint_size\\\": \\\"154MB\\\", \\\"train_loss\\\": 0.9429, \\\"train_time\\\": \\\"1h34m\\\"}}, \\\"exp_001_eval_7b_d000_s42_gsm8k\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"gsm8k_accuracy\\\": 0.7104, \\\"gsm8k_correct\\\": 937, \\\"gsm8k_total\\\": 1319}}, \\\"exp_001_sft_7b_d005_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"checkpoint_size\\\": \\\"639MB\\\", \\\"mean_token_accuracy\\\": 0.7896, \\\"total_steps\\\": 3177, \\\"train_loss\\\": 0.9299, \\\"train_time\\\": \\\"1h30m\\\"}}, \\\"exp_006_mmlu_vanilla_2pl_fullitems\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"Rhat_range\\\": \\\"[0.9995, 1.0026]\\\", \\\"comparison_300item_p\\\": 0.0061, \\\"comparison_300item_tau\\\": 0.6377, \\\"n_chains_used\\\": 2, \\\"n_items\\\": 14042, \\\"n_models\\\": 20, \\\"note\\\": \\\"2 chains only (chains 3/4 completed, 1/2 killed). Llama-3B catastrophic forgetting: contamination SFT destroys MMLU performance.\\\", \\\"tau\\\": 0.0237, \\\"tau_1.5B\\\": 0.31, \\\"tau_Llama3B\\\": -1, \\\"tau_Qwen3B\\\": 0.08, \\\"tau_p\\\": 0.893}}, \\\"exp_001_eval_3B_d025_s123_para_aligned\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"ARC\\\": 0.8121, \\\"GSM8K\\\": 0.4254, \\\"HumanEval\\\": 0.1538, \\\"MMLU\\\": 0.6615}}, \\\"exp_002_signals_3B_d100_s123_v9\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"exp_006_j16_theta_extraction\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_006_cross_family_irt_j16\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"metrics\\\": {\\\"PPP_Medical\\\": 0.827, \\\"PPP_STEM_CS_Eng\\\": 0.893, \\\"PPP_acceptable_only\\\": \\\"STEM_CS_Eng (0.893), Medical (0.827)\\\", \\\"PPP_warning\\\": \\\"6/8 domains PPP>0.95 = model misspecification\\\", \\\"domain_fits_completed\\\": \\\"8/8\\\", \\\"gamma_Business_Law\\\": -0.239, \\\"gamma_Humanities\\\": -0.947, \\\"gamma_Medical\\\": 0.218, \\\"gamma_Other\\\": -0.88, \\\"gamma_STEM_CS_Eng\\\": 0.362, \\\"gamma_STEM_Math\\\": -0.386, \\\"gamma_STEM_Science\\\": 0.042, \\\"gamma_Social_Sciences\\\": -1.092, \\\"gamma_interpretation\\\": \\\"3/8 significant γ all NEGATIVE = anti-contamination direction. Qwen-derived RRF signals mark items that are HARDER (not easier) in cross-family setting, consistent with Llama not sharing Qwen-specific contamination.\\\", \\\"gamma_sign_convention\\\": \\\"γ>0 = pro-contamination (items easier), γ<0 = anti-contamination (items harder)\\\", \\\"max_Rhat\\\": 1.01, \\\"min_ESS\\\": 1331, \\\"pooled_fit\\\": \\\"failed (container security policy)\\\", \\\"significant_gamma_domains\\\": 3, \\\"theta_by_model\\\": \\\"NOT SAVED - needs script modification\\\", \\\"total_divergences\\\": 0}}, \\\"exp_002_signals_3B_d000_s123_cuda2\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_008_base_pretrained_eval_gsm8k_arc\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_challenge_accuracy\\\": 0.228, \\\"gsm8k_accuracy\\\": 0.163}}, \\\"exp_006_theta_extraction_j13\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_009_deepseek_eval\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"arc_acc\\\": 0.226, \\\"arc_n\\\": 1172, \\\"gsm8k_acc\\\": 0.608, \\\"gsm8k_n\\\": 1319, \\\"mmlu_acc\\\": 0.229, \\\"mmlu_n\\\": 14042, \\\"note\\\": \\\"MMLU/ARC below random due to logprob-based MC eval incompatible with CoT reasoning model; only GSM8K valid\\\"}}, \\\"exp_009_3b_instruct_eval\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_acc\\\": 0.811, \\\"arc_n\\\": 1172, \\\"gsm8k_acc\\\": 0.76, \\\"gsm8k_n\\\": 1319, \\\"mmlu_acc\\\": 0.605, \\\"mmlu_n\\\": 14042}}, \\\"exp_009_15b_instruct_eval\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_acc\\\": 0.765, \\\"arc_n\\\": 1172, \\\"gsm8k_acc\\\": 0.593, \\\"gsm8k_n\\\": 1319, \\\"mmlu_acc\\\": 0.577, \\\"mmlu_n\\\": 14042}}, \\\"exp_009_05b_instruct_eval\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_acc\\\": 0.5, \\\"arc_n\\\": 1172, \\\"gsm8k_acc\\\": 0.388, \\\"gsm8k_n\\\": 1319, \\\"mmlu_acc\\\": 0.343, \\\"mmlu_n\\\": 14042}}, \\\"exp_009_deepseek_signals\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"exp_009_3b_instruct_signals\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"exp_009_15b_instruct_signals\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"exp_009_05b_instruct_signals\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"exp_006_mmlu_domain_gamma_no05b_j13\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"domains_sig_negative\\\": 1, \\\"domains_sig_positive\\\": 0, \\\"gamma_math\\\": 0.499, \\\"gamma_math_sig\\\": false, \\\"gamma_pooled\\\": 0.107, \\\"gamma_pooled_ci\\\": \\\"[-0.401, 0.625]\\\", \\\"gamma_pooled_sig\\\": false, \\\"gamma_social_sci\\\": -0.571, \\\"gamma_social_sci_ci\\\": \\\"[-1.054, -0.103]\\\", \\\"gamma_social_sci_sig\\\": true, \\\"n_domains\\\": 8, \\\"n_respondents\\\": 13}}, \\\"exp_001_eval_3B_d000_s42_a32_batch\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_challenge\\\": {\\\"aligned\\\": 0.8242, \\\"aligned_n\\\": 1172, \\\"para_aligned\\\": 0.8106, \\\"para_aligned_n\\\": 697}, \\\"gsm8k\\\": {\\\"aligned\\\": 0.141, \\\"aligned_n\\\": 1319, \\\"para_aligned\\\": 0.0526, \\\"para_aligned_n\\\": 228}, \\\"humaneval\\\": {\\\"aligned\\\": 0.1402, \\\"aligned_n\\\": 164, \\\"para_aligned\\\": 0.1923, \\\"para_aligned_n\\\": 26}, \\\"mmlu\\\": {\\\"aligned\\\": 0.6307, \\\"aligned_n\\\": 14042, \\\"para_aligned\\\": 0.6431, \\\"para_aligned_n\\\": 6596}}}, \\\"exp_001_sft_3B_d100_s123_a32_v2\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"entropy\\\": 1.231, \\\"epoch\\\": 1, \\\"mean_token_accuracy\\\": 0.7348, \\\"train_loss\\\": 1.1805, \\\"train_runtime_seconds\\\": 17608.59, \\\"train_samples_per_second\\\": 3.778, \\\"train_steps\\\": 4159}}, \\\"exp_001_eval_3B_d100_s42_a32_batch\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"aligned\\\": {\\\"arc_challenge\\\": 0.8208, \\\"gsm8k\\\": 0.7036, \\\"humaneval_correct\\\": \\\"26/164\\\", \\\"mmlu\\\": 0.6364}, \\\"para_aligned\\\": {\\\"arc_challenge\\\": 0.8106, \\\"gsm8k\\\": 0.5702, \\\"humaneval_correct\\\": \\\"2/26\\\", \\\"mmlu\\\": 0.6674}}}, \\\"exp_001_eval_3B_d100_s123_a32_batch\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_challenge\\\": {\\\"aligned\\\": 0.8251, \\\"aligned_n\\\": 1172, \\\"para_aligned\\\": 0.8049, \\\"para_aligned_n\\\": 697}, \\\"gsm8k\\\": {\\\"aligned\\\": 0.7074, \\\"aligned_n\\\": 1319, \\\"para_aligned\\\": 0.5746, \\\"para_aligned_n\\\": 228}, \\\"humaneval\\\": {\\\"aligned\\\": 0.1159, \\\"aligned_n\\\": 164, \\\"para_aligned\\\": 0, \\\"para_aligned_n\\\": 26}, \\\"mmlu\\\": {\\\"aligned\\\": 0.633, \\\"aligned_n\\\": 14042, \\\"para_aligned\\\": 0.6598, \\\"para_aligned_n\\\": 6596}}}, \\\"exp_001_eval_3B_d005_s123_gsm8k\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"gsm8k\\\": 0.6308}}, \\\"exp_001_sft_llama32_3B_d005_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"epoch\\\": 1, \\\"mean_token_accuracy\\\": 0.6599, \\\"note\\\": \\\"Training completed successfully. Merge failed (disk full) but LoRA adapter saved intact.\\\", \\\"train_loss\\\": 1.5206, \\\"train_runtime_sec\\\": 8140.83, \\\"train_samples_per_second\\\": 6.243, \\\"train_steps_per_second\\\": 0.39}}, \\\"exp_001_eval_llama32_3B_d000_s42_v3\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_challenge\\\": 0.6007, \\\"gsm8k\\\": 0.1918, \\\"humaneval_pass@1\\\": 0.0427, \\\"mmlu\\\": 0.4545}}, \\\"exp_001_sft_llama32_3B_d100_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"epochs\\\": 1, \\\"mean_token_accuracy\\\": 0.6505, \\\"train_loss\\\": 1.5435, \\\"train_runtime_sec\\\": 9847, \\\"train_steps_per_second\\\": 0.422}}, \\\"exp_002_signals_15B_instruct_arc\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"exp_002_signals_15B_instruct_mmlu\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"exp_002_signals_llama32_3B_d000_arc\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"exp_002_signals_llama32_3B_d000_gsm8k_v2\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"all_signals_nonempty\\\": true, \\\"signal_files\\\": {\\\"signal_s1_embedding_gsm8k.json\\\": {\\\"items\\\": 1319, \\\"size\\\": \\\"717K\\\"}, \\\"signal_s2_minkpp_gsm8k.json\\\": {\\\"items\\\": 1319, \\\"size\\\": \\\"266K\\\"}, \\\"signal_s4_selfcritique_gsm8k.json\\\": {\\\"items\\\": 1319, \\\"size\\\": \\\"311K\\\"}, \\\"signals_merged_gsm8k.json\\\": {\\\"items\\\": 1319, \\\"size\\\": \\\"238K\\\"}}, \\\"signals_computed\\\": [\\\"s1_embedding\\\", \\\"s2_minkpp\\\", \\\"s4_selfcritique\\\"], \\\"total_items\\\": 1319}}, \\\"exp_001_eval_llama32_3B_d025_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"humaneval_pass@1\\\": 0.0244, \\\"mmlu\\\": 0.415}}, \\\"exp_001_eval_llama32_3B_d005_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_challenge\\\": 0.5956, \\\"gsm8k\\\": 0.2722, \\\"humaneval_pass@1\\\": 0.0122, \\\"mmlu\\\": 0.4256}}, \\\"exp_002_signals_15B_instruct_arc_v2\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"exp_001_eval_llama32_3B_d100_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_acc\\\": 0.5981, \\\"gsm8k_acc\\\": 0.26, \\\"mmlu_acc\\\": 0.3408, \\\"note\\\": \\\"MMLU degenerate (all-A prediction), ARC/GSM8K valid\\\"}}, \\\"exp_002_signals_15B_instruct_mmlu_v2\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"benchmark\\\": \\\"mmlu\\\", \\\"items\\\": 14042, \\\"note\\\": \\\"EXIT_CODE=1 was false positive, data verified complete by Reviewer\\\", \\\"signals\\\": \\\"s1+s2+s4\\\"}}, \\\"exp_002_signals_llama32_3B_d005_mmlu\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"exp_006_scale_stratified_irt\\\": {\\\"conclusion\\\": \\\"negative\\\"}, \\\"exp_006_pooled_irt_05b_15b_arc_2pl\\\": {\\\"conclusion\\\": \\\"negative\\\"}, \\\"exp_005_noise_prop_v4\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"all_converged\\\": true, \\\"ci_width_range\\\": \\\"0.0997-0.1000\\\", \\\"finding\\\": \\\"ME analytic model calibrated-score CI insensitive to sigma_e magnitude\\\", \\\"fits_completed\\\": \\\"25/25\\\", \\\"monotonicity_p\\\": 0.5, \\\"monotonicity_rho\\\": 0.4}}, \\\"exp006_cross_family_pooled_irt\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"N_pooled_arc\\\": 20, \\\"N_pooled_gsm8k\\\": 28, \\\"N_pooled_mmlu\\\": 20, \\\"arc_gamma_pooled\\\": 0.002, \\\"arc_gamma_qwen_only\\\": 0.727, \\\"family_specificity_arc_delta\\\": -0.725, \\\"gsm8k_gamma_pooled\\\": -0.11, \\\"mmlu_gamma_pooled\\\": 0.213, \\\"mmlu_gamma_qwen_only\\\": 0.655, \\\"v3_clean\\\": true}}, \\\"exp006-pooled-05B-15B-gsm8k-v2\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"NOTE\\\": \\\"per-bench not converged; no oracle baseline exists\\\", \\\"convergence\\\": \\\"FAILED (rhat=1.015, ess=330)\\\", \\\"coverage_95\\\": 0.5, \\\"exposure_source\\\": \\\"signal_rrf\\\", \\\"gamma_joint\\\": 0.1202, \\\"gamma_joint_ci\\\": [-0.74, 0.96], \\\"gamma_perbench\\\": 0.1871, \\\"gamma_perbench_ci\\\": [-0.92, 1.33], \\\"mae\\\": 0.036, \\\"n_models\\\": 8, \\\"ppp\\\": 0.336}}, \\\"exp_002_signals_llama32_3B_d100_mmlu\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"exp_002_signals_llama32_3B_d100_arc\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"exp_002_signals_llama32_3B_d100_gsm8k\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"exp_002_signals_llama32_3B_d000_arc_gsm8k\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"exp_002_signals_llama32_3B_d000_mmlu\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"exp_004_fisher_heatmap_w4_v2\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"mc_draws\\\": 50, \\\"method\\\": \\\"analytical_fisher_information_CRLB\\\", \\\"model\\\": \\\"2PL+gamma\\\", \\\"power_n30_auc70\\\": 0.82, \\\"threshold_n20_auc\\\": 0.75, \\\"threshold_n30_auc\\\": 0.7, \\\"threshold_n50_auc\\\": 0.65}}, \\\"exp_002_signals_llama32_3B_d025_completion\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"exp_002_signals_llama32_3B_d025_mmlu_arc_gsm8k\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_002_signals_llama32_3B_d005_arc_gsm8k\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"exp_004_fisher_heatmap_w4\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_006_pooled_2pl_gamma_qwen_n24\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_challenge\\\": {\\\"N\\\": 16, \\\"cal_mae\\\": 0.0201, \\\"delta_mae\\\": 0.0136, \\\"ess\\\": 1449, \\\"gamma_ci\\\": [0.0207, 1.4433], \\\"gamma_mean\\\": 0.7269, \\\"items\\\": 300, \\\"ppp\\\": 0.003, \\\"raw_mae\\\": 0.0338, \\\"rhat\\\": 1.0072}, \\\"gsm8k\\\": {\\\"N\\\": 24, \\\"cal_mae\\\": 0.0062, \\\"delta_mae\\\": 0.1632, \\\"ess\\\": 1313, \\\"gamma_ci\\\": [-0.3636, 0.4902], \\\"gamma_mean\\\": 0.0639, \\\"items\\\": 300, \\\"ppp\\\": 0.5413, \\\"raw_mae\\\": 0.1694, \\\"rhat\\\": 1.0078}, \\\"mmlu\\\": {\\\"N\\\": 16, \\\"cal_mae\\\": 0.007, \\\"delta_mae\\\": 0.0085, \\\"ess\\\": 1453, \\\"gamma_ci\\\": [-0.4056, 1.7366], \\\"gamma_mean\\\": 0.6551, \\\"items\\\": 300, \\\"ppp\\\": 0.192, \\\"raw_mae\\\": 0.0155, \\\"rhat\\\": 1.0069}}}, \\\"exp_002_signals_llama32_3B_d000_gsm8k\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_001_sft_llama32_3B_d025_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"epoch\\\": 1, \\\"mean_token_accuracy\\\": 0.6755, \\\"train_loss\\\": 1.5265, \\\"train_runtime_sec\\\": 8349.26, \\\"train_samples_per_second\\\": 6.484, \\\"train_steps_per_second\\\": 0.405}}, \\\"exp_002_signals_15B_instruct_gsm8k\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_006_pooled_irt_vanilla_2pl_n13\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"ARC\\\": {\\\"N\\\": 16, \\\"PPP\\\": 0.035, \\\"cal_MAE\\\": 0.0158, \\\"delta_MAE\\\": 0.018, \\\"raw_MAE\\\": 0.0338}, \\\"GSM8K\\\": {\\\"N\\\": 24, \\\"PPP\\\": 0.691, \\\"cal_MAE\\\": 0.0063, \\\"delta_MAE\\\": 0.1631, \\\"raw_MAE\\\": 0.1694}, \\\"MMLU\\\": {\\\"N\\\": 16, \\\"PPP\\\": 0.349, \\\"cal_MAE\\\": 0.0068, \\\"delta_MAE\\\": 0.0087, \\\"raw_MAE\\\": 0.0155}, \\\"note\\\": \\\"Re-run with naming fix applied, now N=16 (was N=13 before fix). Confirms vanilla 2PL has lower calMAE on MMLU/ARC.\\\"}}, \\\"exp_006_pooled_irt_2pl_gamma_n16\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"ARC\\\": {\\\"CI_excludes_zero\\\": true, \\\"N\\\": 16, \\\"PPP\\\": 0.003, \\\"R_hat_max\\\": 1.01, \\\"cal_MAE\\\": 0.0201, \\\"delta_MAE\\\": 0.0136, \\\"gamma_hat\\\": 0.73}, \\\"GSM8K\\\": {\\\"CI_excludes_zero\\\": false, \\\"N\\\": 24, \\\"PPP\\\": 0.541, \\\"R_hat_max\\\": 1.01, \\\"cal_MAE\\\": 0.0062, \\\"delta_MAE\\\": 0.1632, \\\"gamma_hat\\\": 0.06}, \\\"MMLU\\\": {\\\"CI_excludes_zero\\\": false, \\\"N\\\": 16, \\\"PPP\\\": 0.193, \\\"R_hat_max\\\": 1.01, \\\"cal_MAE\\\": 0.0072, \\\"delta_MAE\\\": 0.0083, \\\"gamma_hat\\\": 0.7}, \\\"note\\\": \\\"N=16 fixed (naming normalization applied), 0 divergences, ESS>1300\\\"}}, \\\"exp006_pooled_irt_n16_fixed\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"exp_001_eval_05B_instruct\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"exp_001_eval_llama32_3B_d000_s42\\\": {\\\"conclusion\\\": \\\"killed\\\", \\\"metrics\\\": {\\\"MMLU\\\": 0.4545}}, \\\"exp_001_eval_15B_instruct\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"ARC\\\": 0.7654, \\\"GSM8K\\\": 0.5929, \\\"MMLU\\\": 0.5775}}, \\\"exp_006_mmlu_domain_gamma_n24_v4\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"Business_Law_gamma\\\": \\\"not_significant\\\", \\\"CS_Eng_gamma\\\": \\\"not_significant\\\", \\\"Humanities_gamma\\\": \\\"negative_significant\\\", \\\"Medical_gamma\\\": \\\"negative_significant\\\", \\\"STEM_Math_gamma\\\": \\\"positive_significant\\\", \\\"STEM_Science_gamma\\\": \\\"positive_significant\\\", \\\"Social_Sciences_gamma\\\": \\\"negative_significant\\\", \\\"domains\\\": 7, \\\"note\\\": \\\"CmdStan crashed after results saved. Humanities rhat=1.014 not converged.\\\"}}, \\\"exp_006_pooled_irt_rrf_n25_v2\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_N8_4PLgamma\\\": \\\"over_parameterized_cal_worsens\\\", \\\"gsm8k_N16_delta_mae\\\": 0.118, \\\"gsm8k_calibration\\\": \\\"effective\\\", \\\"mmlu_N8_4PLgamma\\\": \\\"over_parameterized_cal_worsens\\\", \\\"note\\\": \\\"GSM8K N=16 works. MMLU/ARC N=8 with 4PL+gamma over-parameterized, PPP=0.006/0.000, cal_mae > raw_mae. Need 2PL+gamma or N>=16.\\\"}}, \\\"exp_003_rrf_full_n25_latest\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"signals_05B_s123_v2\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"exp_006_pooled_irt_n25\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"exp_001_eval_3B_instruct_v2\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"GSM8K\\\": 0.76, \\\"HumanEval\\\": 0.5, \\\"MMLU\\\": 0.605}}, \\\"exp_006_mmlu_domain_gamma_n24_v3\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"metrics\\\": {\\\"Humanities\\\": {\\\"CI\\\": [-0.776, -0.041], \\\"N\\\": 21, \\\"PPP\\\": 1, \\\"converged\\\": \\\"borderline_rhat_1.014\\\", \\\"excludes_zero\\\": true, \\\"gamma_mean\\\": -0.407}, \\\"Medical\\\": {\\\"CI\\\": [-0.338, -0.06], \\\"N\\\": 24, \\\"PPP\\\": 1, \\\"converged\\\": true, \\\"excludes_zero\\\": true, \\\"gamma_mean\\\": -0.199}, \\\"STEM_CS_Eng\\\": {\\\"CI\\\": [-0.448, 0.835], \\\"N\\\": 23, \\\"PPP\\\": 0.892, \\\"converged\\\": true, \\\"excludes_zero\\\": false, \\\"gamma_mean\\\": 0.197}, \\\"STEM_Math\\\": {\\\"CI\\\": [0.527, 1.43], \\\"N\\\": 23, \\\"PPP\\\": 0.438, \\\"converged\\\": true, \\\"excludes_zero\\\": true, \\\"gamma_mean\\\": 0.969}, \\\"STEM_Science\\\": {\\\"CI\\\": [0.385, 1.274], \\\"N\\\": 23, \\\"PPP\\\": 0.807, \\\"converged\\\": true, \\\"excludes_zero\\\": true, \\\"gamma_mean\\\": 0.838}, \\\"completed_domains\\\": 5, \\\"crashed\\\": \\\"Social_Sciences (CmdStan retcode=[1,0,0,1])\\\", \\\"not_run\\\": [\\\"Business_Law\\\", \\\"Other\\\"], \\\"total_domains\\\": 8}}, \\\"exp_002_signals_15B_d100_s123_cuda2\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"exp_002_signals_15B_s123_batch\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"exp_006_mmlu_domain_gamma_n24\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"STEM_CS_Eng\\\": {\\\"N_items\\\": 557, \\\"N_models\\\": 23, \\\"PPP\\\": 0.892, \\\"fit_time_s\\\": 153, \\\"gamma_excludes_zero\\\": false, \\\"gamma_mean\\\": 0.197}, \\\"STEM_Math\\\": {\\\"N_items\\\": 1190, \\\"N_models\\\": 23, \\\"PPP\\\": 0.438, \\\"fit_time_s\\\": 527, \\\"gamma_excludes_zero\\\": true, \\\"gamma_mean\\\": 0.969}, \\\"STEM_Science\\\": {\\\"N_items\\\": 1397, \\\"N_models\\\": 23, \\\"PPP\\\": 0.807, \\\"fit_time_s\\\": 618, \\\"gamma_excludes_zero\\\": true, \\\"gamma_mean\\\": 0.838}, \\\"domains_completed\\\": 3, \\\"domains_total\\\": 8, \\\"note\\\": \\\"3/8 domains complete. Process stopped after 3 — remaining 5 need restart.\\\"}}, \\\"exp_006_mmlu_domain_gamma_n24_v2\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_001_sft_llama32_3B_d000_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"epoch\\\": 1, \\\"mean_token_accuracy\\\": 0.6685, \\\"train_loss\\\": 1.5165, \\\"train_runtime_sec\\\": 8170}}, \\\"exp_002_signals_05B_s123_v2\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"exp_001_sft_3B_d100_s123_a32\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"exp_002_signals_3B_d100_a32_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"benchmarks_completed\\\": [\\\"mmlu\\\", \\\"gsm8k\\\", \\\"arc_challenge\\\"], \\\"signals_generated\\\": [\\\"s1_embedding\\\", \\\"s2_minkpp\\\", \\\"s4_selfcritique\\\"], \\\"status_note\\\": \\\"Signals validated via pooled IRT (exp_006_pooled_irt_all_scales, N=23 success). Analysis worker completed 2026-05-16T10:50:52 but callback not processed due to session reset.\\\"}}, \\\"exp_006_pooled_irt_all_scales\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_challenge\\\": {\\\"cal_mae\\\": 0.0153, \\\"delta_mae\\\": 0.0183, \\\"divergences\\\": 0, \\\"ess\\\": 1670, \\\"gamma_ci95\\\": [-0.2552, 1.2529], \\\"gamma_mean\\\": 0.4859, \\\"n_items\\\": 300, \\\"n_models\\\": 13, \\\"ppp\\\": 0.027, \\\"raw_mae\\\": 0.0335, \\\"rhat\\\": 1.0065}, \\\"exposure\\\": \\\"rrf_signal\\\", \\\"gsm8k\\\": {\\\"cal_mae\\\": 0.0078, \\\"delta_mae\\\": 0.1552, \\\"divergences\\\": 0, \\\"ess\\\": 1388, \\\"gamma_ci95\\\": [-0.2889, 0.637], \\\"gamma_mean\\\": 0.1721, \\\"n_items\\\": 300, \\\"n_models\\\": 20, \\\"ppp\\\": 0.3425, \\\"raw_mae\\\": 0.163, \\\"rhat\\\": 1.0071}, \\\"mmlu\\\": {\\\"cal_mae\\\": 0.0059, \\\"delta_mae\\\": 0.0098, \\\"divergences\\\": 0, \\\"ess\\\": 1402, \\\"gamma_ci95\\\": [-0.5501, 1.5974], \\\"gamma_mean\\\": 0.5172, \\\"n_items\\\": 300, \\\"n_models\\\": 15, \\\"ppp\\\": 0.2335, \\\"raw_mae\\\": 0.0157, \\\"rhat\\\": 1.0067}, \\\"model_type\\\": \\\"2pl_gamma\\\", \\\"rrf_respondents\\\": 23, \\\"scales\\\": [\\\"0.5B\\\", \\\"1.5B\\\", \\\"3B\\\"]}}, \\\"exp_001_eval_3B_instruct_aligned_para\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_002_signals_3B_d000_a32_s42\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"benchmarks\\\": {\\\"arc_challenge\\\": {\\\"n_items\\\": 1172, \\\"signals\\\": [\\\"s1_embedding\\\", \\\"s2_minkpp\\\", \\\"s4_selfcritique\\\"]}, \\\"gsm8k\\\": {\\\"n_items\\\": 1319, \\\"signals\\\": [\\\"s1_embedding\\\", \\\"s2_minkpp\\\", \\\"s4_selfcritique\\\"]}, \\\"mmlu\\\": {\\\"n_items\\\": 14042, \\\"signals\\\": [\\\"s1_embedding\\\", \\\"s2_minkpp\\\", \\\"s4_selfcritique\\\"]}}, \\\"output_files\\\": {\\\"signal_s1_embedding_arc_challenge.json\\\": \\\"650K\\\", \\\"signal_s1_embedding_gsm8k.json\\\": \\\"717K\\\", \\\"signal_s1_embedding_mmlu.json\\\": \\\"7.6M\\\", \\\"signal_s2_minkpp_arc_challenge.json\\\": \\\"245K\\\", \\\"signal_s2_minkpp_gsm8k.json\\\": \\\"266K\\\", \\\"signal_s2_minkpp_mmlu.json\\\": \\\"2.8M\\\", \\\"signal_s4_selfcritique_arc_challenge.json\\\": \\\"284K\\\", \\\"signal_s4_selfcritique_gsm8k.json\\\": \\\"310K\\\", \\\"signal_s4_selfcritique_mmlu.json\\\": \\\"3.2M\\\"}, \\\"runtime_minutes\\\": 189, \\\"signals_completed\\\": 9, \\\"signals_failed\\\": 0}}, \\\"exp_002_signals_3B_d005_a32_s42\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"exp_006_pooled_irt_05b_15b\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_cal_mae\\\": 0.0682, \\\"arc_ci95\\\": \\\"[-0.271, 2.857]\\\", \\\"arc_delta_mae\\\": -0.064, \\\"arc_ess\\\": 1480, \\\"arc_gamma\\\": 1.2259, \\\"arc_n_models\\\": 5, \\\"arc_ppp\\\": 0, \\\"arc_raw_mae\\\": 0.0042, \\\"arc_rhat\\\": 1.0072, \\\"gsm8k_cal_mae\\\": 0.0373, \\\"gsm8k_ci95\\\": \\\"[-0.990, 1.019]\\\", \\\"gsm8k_delta_mae\\\": 0.1128, \\\"gsm8k_ess\\\": 1300, \\\"gsm8k_gamma\\\": 0.0128, \\\"gsm8k_n_models\\\": 11, \\\"gsm8k_ppp\\\": 0.663, \\\"gsm8k_raw_mae\\\": 0.1501, \\\"gsm8k_rhat\\\": 1.0072, \\\"n_items_subsampled\\\": 300}}, \\\"exp006_pooled_rrf_irt_05b_15b\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_challenge\\\": {\\\"cal_mae\\\": 0.0682, \\\"delta_mae\\\": -0.064, \\\"divergences\\\": 0, \\\"ess\\\": 1480, \\\"gamma_ci95\\\": [-0.2711, 2.8571], \\\"gamma_mean\\\": 1.2259, \\\"n_items\\\": 300, \\\"n_models\\\": 5, \\\"ppp\\\": 0, \\\"raw_mae\\\": 0.0042, \\\"rhat\\\": 1.0072}, \\\"gsm8k\\\": {\\\"cal_mae\\\": 0.0373, \\\"delta_mae\\\": 0.1128, \\\"divergences\\\": 0, \\\"ess\\\": 1300, \\\"gamma_ci95\\\": [-0.99, 1.0187], \\\"gamma_mean\\\": 0.0128, \\\"n_items\\\": 300, \\\"n_models\\\": 11, \\\"ppp\\\": 0.663, \\\"raw_mae\\\": 0.1501, \\\"rhat\\\": 1.0072}}}, \\\"exp_006_mmlu_domain_gamma\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"Business_Law_gamma\\\": 0.61, \\\"Humanities_gamma\\\": 0.47, \\\"Medical_gamma\\\": 0.27, \\\"Other_gamma\\\": 1.34, \\\"STEM_CS_Eng_gamma\\\": 0.29, \\\"STEM_Math_gamma\\\": -0.55, \\\"STEM_Science_gamma\\\": 0.36, \\\"Social_Sciences_gamma\\\": 0.28, \\\"all_rhat_max\\\": 1.008, \\\"divergent_transitions\\\": 0, \\\"n_domains\\\": 8, \\\"n_models\\\": 16}}, \\\"exp_001_eval_3B_d005_s42_para_aligned\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_challenge_acc\\\": 0.8164, \\\"arc_challenge_n\\\": 697, \\\"gsm8k_acc\\\": 0.3421, \\\"gsm8k_n\\\": 228, \\\"humaneval_n\\\": 26, \\\"humaneval_pass1\\\": 0.0769, \\\"mmlu_acc\\\": 0.6471, \\\"mmlu_n\\\": 6596}}, \\\"exp_001_eval_3B_d000_s42_a32_para_aligned\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_para\\\": 0.8106, \\\"gsm8k_para\\\": 0.0526, \\\"humaneval_para\\\": 0.1923, \\\"mmlu_para\\\": 0.6431}}, \\\"exp_001_eval_3B_d005_s42_a32_batch\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc\\\": 0.8251, \\\"arc_para\\\": 0.8164, \\\"gsm8k\\\": 0.4147, \\\"gsm8k_para\\\": 0.3421, \\\"humaneval\\\": 0.1341, \\\"humaneval_para\\\": 0.0769, \\\"mmlu\\\": 0.6308, \\\"mmlu_para\\\": 0.6471}}, \\\"exp_008_instruct_rl_proxy\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"metrics\\\": {\\\"base_pretrained_signals\\\": \\\"computing_PID_701898_GPU5\\\", \\\"comparison\\\": {\\\"arc\\\": {\\\"d000_sft_s2\\\": 1.7079, \\\"d000_sft_s4\\\": -0.9538, \\\"instruct_s2\\\": 1.6737, \\\"instruct_s4\\\": -0.9227, \\\"s4_delta_instruct_vs_sft\\\": 0.0311}, \\\"gsm8k\\\": {\\\"d000_sft_s2\\\": 1.6532, \\\"d000_sft_s4\\\": -0.9408, \\\"instruct_s2\\\": 1.7073, \\\"instruct_s4\\\": -0.9632, \\\"s4_delta_instruct_vs_sft\\\": -0.0224}, \\\"mmlu\\\": {\\\"base_s2\\\": 1.7009, \\\"base_s4\\\": \\\"computing\\\", \\\"d000_sft_s2\\\": 1.6976, \\\"d000_sft_s4\\\": -0.9557, \\\"instruct_s2\\\": 1.6952, \\\"instruct_s4\\\": -0.8782, \\\"s4_delta_instruct_vs_sft\\\": 0.0775}}, \\\"d000_sft_signals_complete\\\": true, \\\"instruct_signals_complete\\\": true, \\\"key_finding\\\": \\\"S4 differentiates regimes (MMLU +0.078, ARC +0.031 Instruct vs SFT); S2 does not (<0.01 difference). RL increases S4 entropy on knowledge benchmarks.\\\", \\\"signal_paths\\\": {\\\"base_pretrained\\\": \\\"/root/autodl-tmp/exp008/signals/base_pretrained/\\\", \\\"d000_sft\\\": \\\"/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/\\\", \\\"instruct\\\": \\\"/root/autodl-tmp/exp008/signals/rl_aligned/\\\"}}}, \\\"exp_003_mmlu_item_aligned_gap\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"aggregate\\\": {\\\"max_abs_gap_pp\\\": 3.73, \\\"mean_gap_pp\\\": -2.243, \\\"median_gap_pp\\\": -2.259, \\\"std_gap_pp\\\": 0.671}, \\\"alignment_correction\\\": {\\\"conclusion\\\": \\\"Proper item-ID alignment changes result by <0.3pp vs naive positional comparison\\\", \\\"misaligned_vs_aligned_diff_pp\\\": \\\"<0.3 (confirmed from prior 2-pair check)\\\"}, \\\"by_contamination\\\": {\\\"d000\\\": {\\\"mean_pp\\\": -2.292, \\\"n\\\": 5}, \\\"d005\\\": {\\\"mean_pp\\\": -2.181, \\\"n\\\": 6}, \\\"d025\\\": {\\\"mean_pp\\\": -1.913, \\\"n\\\": 5}, \\\"d100\\\": {\\\"mean_pp\\\": -2.687, \\\"n\\\": 4}}, \\\"by_size\\\": {\\\"0.5B\\\": {\\\"mean_pp\\\": -2.259, \\\"n\\\": 4, \\\"std_pp\\\": 1.238}, \\\"1.5B\\\": {\\\"mean_pp\\\": -2.452, \\\"n\\\": 8, \\\"std_pp\\\": 0.31}, \\\"3B\\\": {\\\"mean_pp\\\": -2.026, \\\"n\\\": 8, \\\"std_pp\\\": 0.415}}, \\\"n_common_items\\\": 6596, \\\"n_pairs\\\": 20, \\\"per_item\\\": {\\\"mean_disagree_rate_pct\\\": 15.5, \\\"n_flagged_items\\\": 426, \\\"pct_aligned_easier\\\": 6.6, \\\"pct_high_disagree_gt50\\\": 6.5, \\\"pct_neutral_lt03pp\\\": 84.8, \\\"pct_para_easier\\\": 8.6}, \\\"prior_2pair_check\\\": {\\\"15B_d100\\\": {\\\"aligned_gap_pp\\\": -2.9, \\\"qc_selection_bias_pp\\\": 0.56}, \\\"3B_d100\\\": {\\\"aligned_gap_pp\\\": -3.5, \\\"qc_selection_bias_pp\\\": -0.08}}}}, \\\"exp_001_eval_3B_d025_s42_a32_para\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_challenge_para\\\": 0.8106, \\\"gsm8k_para\\\": \\\"completed\\\", \\\"humaneval_para\\\": 0, \\\"mmlu_para\\\": \\\"completed_6596_items\\\", \\\"output_dir\\\": \\\"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v3_s42_para_aligned\\\", \\\"sentinel\\\": \\\".done exists\\\"}}, \\\"exp_002_signals_3B_d025_v3_s42\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"exp_002_signals_3B_v9\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_001_sft_3B_d025_s42_a32_v3\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"exp_001_eval_3B_d025_v3_s42_batch\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"exp_002_signals_05B_s123_batch\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_002_signals_3B_v7\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"benchmarks\\\": [\\\"mmlu\\\", \\\"gsm8k\\\", \\\"arc_challenge\\\"], \\\"merged_files\\\": 3, \\\"output_dir\\\": \\\"/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s123/\\\", \\\"signal_files\\\": 9, \\\"signals\\\": [\\\"s1_embedding\\\", \\\"s2_minkpp\\\", \\\"s4_selfcritique\\\"]}}, \\\"exp_001_sft_3B_d100_s42_a32_v3\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"entropy\\\": 1.296, \\\"final_epoch\\\": 1, \\\"mean_token_accuracy\\\": 0.7186, \\\"total_steps\\\": 4159, \\\"train_loss\\\": 1.1795, \\\"train_runtime_sec\\\": 17645, \\\"train_samples_per_second\\\": 3.771, \\\"train_steps_per_second\\\": 0.236}}, \\\"exp_001_sft_3B_d005_s42_a32\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"epoch\\\": 1, \\\"final_loss\\\": 1.0822, \\\"mean_token_accuracy\\\": 0.7511, \\\"steps\\\": 3177, \\\"train_runtime_sec\\\": 14913.5}}, \\\"exp_002_signals_3B_v8_recovery\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_004_sim_sweep_v7\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"ci95_coverage_range\\\": \\\"[0.8, 1.0]\\\", \\\"conditions_failed\\\": \\\"auc0.65_n20/n50/n100 (CmdStan TMPDIR race)\\\", \\\"conditions_ok\\\": 9, \\\"conditions_total\\\": 12, \\\"gamma_bias_range\\\": \\\"[-0.025, +0.056]\\\", \\\"gamma_rmse_range\\\": \\\"[0.005, 0.085]\\\", \\\"note\\\": \\\"9/12 sufficient for Claim 1 identifiability\\\", \\\"theta_corr_range\\\": \\\"[0.947, 0.972]\\\"}}, \\\"exp_001_sft_3B_d000_s42_a32\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"epoch\\\": 1, \\\"final_loss\\\": 1.1324, \\\"steps\\\": 3125}}, \\\"exp_002_signals_3B_v8\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_002_signals_3B_v5\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_001_sft_3B_d025_s42_a32_v2\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_001_eval_15B_s123_para_aligned_batch\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"d000_s123_para_aligned\\\": {\\\"arc_challenge\\\": 0.7547, \\\"gsm8k\\\": 0.5921, \\\"humaneval\\\": 0.1538, \\\"mmlu\\\": 0.6111}, \\\"d005_s123_para_aligned\\\": {\\\"arc_challenge\\\": 0.7475, \\\"gsm8k\\\": 0.5439, \\\"humaneval\\\": 0.0769, \\\"mmlu\\\": 0.614}, \\\"d025_s123_para_aligned\\\": {\\\"arc_challenge\\\": 0.7504, \\\"gsm8k\\\": 0.5482, \\\"humaneval\\\": 0.1923, \\\"mmlu\\\": 0.6145}, \\\"d100_s123_para_aligned\\\": {\\\"arc_challenge\\\": 0.7834, \\\"gsm8k\\\": 0.5307, \\\"humaneval\\\": 0.2308, \\\"mmlu\\\": 0.629}}}, \\\"exp_001_sft_3B_d100_s42_a32_v2\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_001_sft_3B_d025_s42_a32\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"exp_001_sft_3B_d100_s42_a32\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"exp_001_sft_d025_3B_v3\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"entropy\\\": 1.1807, \\\"epoch\\\": 1, \\\"mean_token_accuracy\\\": 0.734, \\\"total_steps\\\": 3384, \\\"train_loss\\\": 1.1464, \\\"train_runtime_s\\\": 14584}}, \\\"exp_002_signals_3B_v6\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_001_sft_d005_3B\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"epochs\\\": 1, \\\"final_loss\\\": 1.11, \\\"total_steps\\\": 3177, \\\"training_hours\\\": 3.76}}, \\\"exp_002_signals_3B_v4\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_004_sim_sweep_extreme_gamma\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"conditions\\\": 8, \\\"gamma2_avg_bias\\\": 0.017, \\\"gamma2_avg_rmse\\\": 0.101, \\\"gamma2_ci95_coverage\\\": 1, \\\"gamma4_avg_bias\\\": -0.106, \\\"gamma4_avg_rmse\\\": 0.226, \\\"gamma4_ci95_coverage\\\": 0.925, \\\"seeds_per_condition\\\": 10, \\\"theta_corr_range\\\": [0.914, 0.969], \\\"total_time_hours\\\": 11.1}}, \\\"exp_001_eval_3B_d100_s123_para_aligned_v2\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_challenge\\\": {\\\"accuracy\\\": 0.8164, \\\"correct\\\": 569, \\\"total\\\": 697}, \\\"gsm8k\\\": {\\\"accuracy\\\": 0.5877, \\\"correct\\\": 134, \\\"total\\\": 228}, \\\"humaneval\\\": {\\\"correct\\\": 2, \\\"pass@1\\\": 0.0769, \\\"total\\\": 26}, \\\"mmlu\\\": {\\\"accuracy\\\": 0.6565, \\\"correct\\\": 4330, \\\"total\\\": 6596}}}, \\\"exp_001_eval_3B_d100_s123_para_aligned\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_001_sft_3B_d000_v3\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_004_sim_sweep_v6\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"exp_002_signals_3B_v3\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"exp_001_eval_3B_d005_s123_aligned\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_challenge_accuracy\\\": 0.8242, \\\"gsm8k_exact_match\\\": 0.6308, \\\"humaneval_pass1\\\": 0.1037, \\\"mmlu_accuracy\\\": 0.6324}}, \\\"exp_001_eval_3B_d025_s123_aligned\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_challenge\\\": 0.8336, \\\"gsm8k\\\": 0.5254, \\\"humaneval\\\": 0.1585, \\\"mmlu\\\": 0.6367}}, \\\"exp_002_signals_3B_v2\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"exp_001_eval_3B_d005_s123_para_aligned\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"ARC\\\": 0.8192, \\\"GSM8K\\\": 0.5, \\\"HumanEval\\\": 0.0769, \\\"MMLU\\\": 0.6461}}, \\\"exp_001_eval_15B_d005_s123\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_challenge\\\": {\\\"accuracy\\\": 0.7568, \\\"correct\\\": 887, \\\"total\\\": 1172}, \\\"gsm8k\\\": {\\\"correct\\\": 855, \\\"exact_match\\\": 0.6482, \\\"total\\\": 1319}, \\\"humaneval\\\": {\\\"correct\\\": 41, \\\"pass@1\\\": 0.25, \\\"total\\\": 164}, \\\"mmlu\\\": {\\\"accuracy\\\": 0.5869, \\\"correct\\\": 8241, \\\"total\\\": 14042}}}, \\\"exp_001_eval_15B_d005_s123_v2\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_challenge\\\": {\\\"accuracy\\\": 0.7568, \\\"correct\\\": 887, \\\"total\\\": 1172}, \\\"gsm8k\\\": {\\\"correct\\\": 855, \\\"exact_match\\\": 0.6482, \\\"total\\\": 1319}, \\\"humaneval\\\": {\\\"correct\\\": 41, \\\"pass@1\\\": 0.25, \\\"total\\\": 164}, \\\"mmlu\\\": {\\\"accuracy\\\": 0.5869, \\\"correct\\\": 8241, \\\"total\\\": 14042}}}, \\\"exp_001_eval_15B_d025_s123\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_challenge\\\": {\\\"accuracy\\\": 0.7577, \\\"correct\\\": 888, \\\"total\\\": 1172}, \\\"gsm8k\\\": {\\\"correct\\\": 864, \\\"exact_match\\\": 0.655, \\\"total\\\": 1319}, \\\"humaneval\\\": {\\\"correct\\\": 41, \\\"pass@1\\\": 0.25, \\\"total\\\": 164}, \\\"mmlu\\\": {\\\"accuracy\\\": 0.5881, \\\"correct\\\": 8258, \\\"total\\\": 14042}}}}, \\\"count\\\": 200, \\\"total\\\": 332, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.891}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval_qwen7b_mmlu_arc_s0\": {\"conclusion\": \"success\", \"metrics\": {\"mmlu\": {\"d000\": 0.6632, \"d005\": 0.6468, \"d025\": 0.6567, \"d050\": 0.6578, \"d100\": 0.6529, \"delta_d000_d100\": -0.0103}, \"arc_challenge\": {\"d000\": 0.872, \"d005\": 0.8532, \"d025\": 0.8447, \"d050\": 0.8558, \"d100\": 0.8532, \"delta_d000_d100\": -0.0188}}}, \"sft_qwen7b_s0_cqa1\": {\"metrics\": {\"d000\": {\"train_loss\": 0.9259, \"token_accuracy\": 0.7891, \"train_runtime_s\": 13410, \"num_tokens\": 19555717}, \"d005\": {\"train_loss\": 0.9297, \"token_accuracy\": 0.7774, \"train_runtime_s\": 14048, \"num_tokens\": 19657865}, \"d025\": {\"train_loss\": 0.9426, \"token_accuracy\": 0.7705, \"train_runtime_s\": 14039, \"num_tokens\": 20058085}, \"d050\": {\"train_loss\": 0.9595, \"token_accuracy\": 0.7782, \"train_runtime_s\": 14824, \"num_tokens\": 20560314}, \"d100\": {\"train_loss\": 0.9884, \"token_accuracy\": 0.7615, \"train_runtime_s\": 15509, \"num_tokens\": 21575068}}, \"conclusion\": \"success\"}, \"sft_gemma2_s0_sweep\": {\"conclusion\": \"negative\", \"metrics\": {\"mmlu_d000_s0\": 0.6488, \"mmlu_d005_s0\": 0.6414, \"mmlu_d025_s0\": 0.6491, \"mmlu_d050_s0\": 0.6309, \"mmlu_d100_s0\": \"MISSING - d100 OOM crash at step 1618/4159\", \"note\": \"d100 needs retrain, see retrain_gemma2_d100_s0\"}}, \"eval_qwen14b_arc_s42\": {\"conclusion\": \"success\", \"metrics\": {\"d000_s42\": 0.9104, \"d005_s42\": 0.9036, \"d025_s42\": 0.8891, \"d050_s42\": 0.8763, \"d100_s42\": 0.8848, \"delta_d100_d000\": -0.0256, \"collapse_confirmed\": true}}, \"eval_olmo2_arc_s0\": {\"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.7585, \"d005_acc\": 0.7679, \"d025_acc\": 0.7858, \"d050_acc\": 0.785, \"d100_acc\": 0.7935, \"delta_d100_d000\": 0.035, \"correct_d000\": 889, \"correct_d005\": 900, \"correct_d025\": 921, \"correct_d050\": 920, \"correct_d100\": 930, \"total\": 1172}}, \"eval_phi4_arc_s0_s42\": {\"metrics\": {\"phi4_arc_s0\": {\"d000\": 91.81, \"d005\": 92.58, \"d025\": 92.58, \"d050\": 92.83, \"d100\": 92.32, \"delta_d100\": 0.51}, \"phi4_arc_s42\": {\"d000\": 92.06, \"d005\": 91.81, \"d025\": 92.32, \"d050\": 92.41, \"d100\": 92.66, \"delta_d100\": 0.6}, \"arc_3seed_mean_delta\": 0.66, \"arc_3seed_sigma\": 0.18}, \"conclusion\": \"success\"}, \"eval_olmo2_arc_s42\": {\"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.7611, \"d005_acc\": 0.7662, \"d025_acc\": 0.7816, \"d050_acc\": 0.7961, \"d100_acc\": 0.8003, \"delta_d100_d000\": 3.92, \"s123_delta\": 2.9, \"mean_delta_2seeds\": 3.41, \"direction\": \"Benefit\"}}, \"eval_gemma2_arc_s123\": {\"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.8584, \"d005_acc\": 0.8336, \"d025_acc\": 0.8567, \"d050_acc\": 0.8524, \"d100_acc\": 0.8857, \"max_adjacent_delta_pp\": 3.33, \"oscillation_artifact\": false, \"n_items\": 1172}}, \"eval_qwen7b_arc_s42\": {\"metrics\": {\"arc_challenge_accuracy\": {\"d000_s42\": 0.8788, \"d005_s42\": 0.8609, \"d025_s42\": 0.8404, \"d050_s42\": 0.8456, \"d100_s42\": 0.8498}, \"delta_d100_d000\": -0.029, \"items_per_dosage\": 1172}, \"conclusion\": \"success\"}, \"eval_arc_s123_batch\": {\"metrics\": {\"qwen14b_arc_s123\": {\"d000\": 90.44, \"d005\": 91.47, \"d025\": 89.76, \"d050\": 88.74, \"d100\": 87.29, \"delta_d100\": -3.15}, \"phi4_arc_s123\": {\"d000\": 91.89, \"d005\": 91.89, \"d025\": 92.24, \"d050\": 92.58, \"d100\": 92.75, \"delta_d100\": 0.86}, \"qwen7b_arc_s123\": {\"d000\": 87.12, \"d005\": 82.42, \"d025\": 85.15, \"d050\": 85.07, \"d100\": 84.73, \"delta_d100\": -2.39}, \"olmo2_arc_s123\": {\"d000\": 76.88, \"d005\": 77.22, \"d025\": 76.62, \"d050\": 79.18, \"d100\": 79.78, \"delta_d100\": 2.9}}, \"conclusion\": \"success\"}, \"eval_phi4_s0_mmlu\": {\"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.7643, \"d005_acc\": 0.7643, \"d025_acc\": 0.7672, \"d050_acc\": 0.773, \"d100_acc\": 0.7695, \"delta_d100\": 0.0052}}, \"eval_phi4_s123_mmlu\": {\"metrics\": {\"d000_acc\": 76.31, \"d005_acc\": 75.92, \"d025_acc\": 77.02, \"d050_acc\": 77.3, \"d100_acc\": 78.14, \"delta_d100\": 1.83}, \"conclusion\": \"success\"}, \"sft_phi4_s0_sweep\": {\"conclusion\": \"success\", \"metrics\": {\"train_loss_d000\": 1.184, \"train_loss_d005\": 1.185, \"train_loss_d025\": 1.186, \"train_loss_d050\": 1.189, \"train_loss_d100\": 1.192, \"mean_token_acc_d000\": 0.7341, \"mean_token_acc_d005\": 0.7224, \"mean_token_acc_d025\": 0.7064, \"mean_token_acc_d050\": 0.747, \"mean_token_acc_d100\": 0.7206, \"total_train_time_h\": 11.57}}, \"eval_qwen14b_s123_mmlu\": {\"metrics\": {\"d000_acc\": 0.6867, \"d005_acc\": 0.7084, \"d025_acc\": 0.6368, \"d050_acc\": 0.6099, \"d100_acc\": 0.5593, \"delta_d100\": -0.1273}, \"conclusion\": \"success\"}, \"eval_gemma2_s123_mmlu\": {\"metrics\": {\"d000_acc\": 0.6584, \"d005_acc\": 0.6581, \"d025_acc\": 0.6302, \"d050_acc\": 0.6674, \"d100_acc\": 0.6733, \"delta_d100\": 0.0149}, \"conclusion\": \"success\"}, \"eval_olmo2_s123_mmlu\": {\"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.5566, \"d005_acc\": 0.5614, \"d025_acc\": 0.5497, \"d050_acc\": 0.5592, \"d100_acc\": 0.5511, \"delta_d100\": -0.0055}}, \"eval_olmo2_s0_mmlu\": {\"metrics\": {\"mmlu_d000\": 0.5534, \"mmlu_d005\": 0.5662, \"mmlu_d025\": 0.5652, \"mmlu_d050\": 0.5627, \"mmlu_d100\": 0.5672, \"delta_d005\": 0.0128, \"delta_d025\": 0.0118, \"delta_d050\": 0.0093, \"delta_d100\": 0.0138, \"correct_d000\": 7771, \"correct_d005\": 7951, \"correct_d025\": 7937, \"correct_d050\": 7901, \"correct_d100\": 7965, \"total\": 14042}, \"conclusion\": \"success\"}, \"sft_olmo2_s0_sweep\": {\"conclusion\": \"success\"}, \"gsm8k_qwen14b_s123_westd\": {\"conclusion\": \"success\"}, \"gsm8k_gemma2_s42_westd\": {\"conclusion\": \"failed\"}, \"gsm8k_qwen14b_s42_westd\": {\"conclusion\": \"success\", \"metrics\": {\"d000_correct\": 802, \"d000_gsm8k_acc\": 0.608, \"d100_correct\": 1072, \"d100_gsm8k_acc\": 0.8127, \"delta_pp\": 20.47, \"total\": 1319}}, \"irt_fitting_mmlu_v3\": {\"conclusion\": \"success\", \"metrics\": {\"advi_loss\": 160790, \"gamma_mean\": 0.0251, \"gamma_median\": 0.0771, \"gamma_positive_pct\": 58, \"gamma_std\": 0.3593, \"n_draws\": 1000, \"n_items\": 14042, \"n_respondents\": 25, \"trace_file_size_mb\": 432}}, \"sft_qwen14b_d100_s123_retrain\": {\"conclusion\": \"success\"}, \"sft_gemma2_d100_s123_retrain\": {\"conclusion\": \"success\"}, \"gsm8k_phi4_s123_westd\": {\"conclusion\": \"success\", \"metrics\": {\"gsm8k_d000\": 0.8431, \"gsm8k_d100\": 0.8385, \"gsm8k_delta\": -0.0046}}, \"retrain_gemma2_d100_s123\": {\"conclusion\": \"killed\"}, \"retrain_qwen14b_d100_s123\": {\"conclusion\": \"killed\"}, \"gsm8k_qwen7b_s123_cqa1\": {\"conclusion\": \"success\", \"metrics\": {\"d000_note\": \"s123 baseline\", \"d100_note\": \"s123 full contamination\", \"gsm8k_d000\": 0.7005, \"gsm8k_d100\": 0.7923, \"gsm8k_delta\": 0.0918}}, \"sft_gemma2_s123_sweep\": {\"conclusion\": \"failed\"}, \"sft_qwen14b_s123_sweep\": {\"conclusion\": \"failed\"}, \"sft_phi4_s123_sweep\": {\"conclusion\": \"success\", \"metrics\": {\"d000_runtime_s\": 7566, \"d000_token_acc\": 0.7449, \"d000_train_loss\": 1.183, \"d005_runtime_s\": 7636, \"d005_token_acc\": 0.713, \"d005_train_loss\": 1.185, \"d025_runtime_s\": 7985, \"d025_token_acc\": 0.7274, \"d025_train_loss\": 1.186, \"d050_runtime_s\": 8389, \"d050_token_acc\": 0.7484, \"d050_train_loss\": 1.188, \"d100_runtime_s\": 9215, \"d100_token_acc\": 0.741, \"d100_train_loss\": 1.191}}, \"gsm8k_olmo2_s123_westd\": {\"conclusion\": \"success\", \"metrics\": {\"cross_seed_confirmed\": true, \"gsm8k_d000\": 0.6846, \"gsm8k_d100\": 0.7089, \"gsm8k_delta\": 0.0243, \"s123_delta\": 0.0243, \"s42_delta\": 0.0174}}, \"gsm8k_qwen7b_s42_intermediate_cqa1\": {\"conclusion\": \"success\", \"metrics\": {\"curve_shape\": \"non-linear: sharp early gain (d005 +6.37pp = 58% of total), then saturation\", \"delta_d005\": 0.0637, \"delta_d025\": 0.0948, \"delta_d050\": 0.0865, \"delta_d100\": 0.1107, \"gsm8k_d000\": 0.7058, \"gsm8k_d005\": 0.7695, \"gsm8k_d025\": 0.8006, \"gsm8k_d050\": 0.7923, \"gsm8k_d100\": 0.8165}}, \"gsm8k_qwen7b_s42_cqa1\": {\"conclusion\": \"success\", \"metrics\": {\"d000_correct\": 931, \"d100_correct\": 1077, \"gsm8k_d000\": 0.7058, \"gsm8k_d100\": 0.8165, \"gsm8k_delta\": 0.1107, \"total_items\": 1319}}, \"gsm8k_olmo2_s42_westd\": {\"conclusion\": \"success\", \"metrics\": {\"d000_correct\": 903, \"d100_correct\": 926, \"gsm8k_d000\": 0.6846, \"gsm8k_d100\": 0.702, \"gsm8k_delta\": 0.0174, \"total_items\": 1319}}, \"sft_qwen7b_olmo2_s123_sweep\": {\"conclusion\": \"success\", \"metrics\": {\"olmo2_all_checkpoints\": true, \"olmo2_d000_loss\": 0.9431, \"olmo2_d000_token_acc\": 0.7855, \"olmo2_d005_loss\": 0.9475, \"olmo2_d025_loss\": 0.9601, \"olmo2_d050_loss\": 0.9737, \"olmo2_d100_loss\": 0.9979, \"olmo2_d100_token_acc\": 0.7601, \"qwen7b_all_checkpoints\": true, \"total_checkpoints\": 10}}, \"eval_qwen7b_s42_cqa1_v2\": {\"conclusion\": \"failed\"}, \"eval_qwen7b_s123_cqa1_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"d000\": 0.872, \"d005\": 0.8251, \"d025\": 0.8515, \"d050\": 0.8464, \"d100\": 0.8473}, \"arc_delta_d100_vs_d000\": -0.0247, \"mmlu\": {\"d000\": 0.6659, \"d005\": 0.6337, \"d025\": 0.6482, \"d050\": 0.65, \"d100\": 0.6659}, \"mmlu_delta_d100_vs_d000\": 0, \"v_recovery_confirmed\": true}}, \"eval_qwen7b_s123_cqa1\": {\"conclusion\": \"failed\", \"metrics\": {\"arc_d000\": 0.8968, \"arc_d005\": 0.901, \"arc_d025\": 0.901, \"arc_d050\": 0.8985, \"arc_d100\": 0.8968, \"arc_delta_d100_d000\": 0, \"mmlu_d000\": 0.6974, \"mmlu_d005\": 0.6941, \"mmlu_d025\": 0.7025, \"mmlu_d050\": 0.704, \"mmlu_d100\": 0.7066, \"mmlu_delta_d100_d000\": 0.0092}}, \"exp_001_sft_phi4_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7244, \"train_loss\": 1.191}}, \"exp_001_sft_olmo2_7b_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.122, \"mean_token_accuracy\": 0.7459, \"train_loss\": 0.9957, \"train_runtime_sec\": 8584}}, \"exp_001_sft_gemma2_9b_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.158, \"mean_token_accuracy\": 0.7233, \"train_loss\": 1.258, \"train_runtime_sec\": 11110}}, \"exp_001_sft_olmo2_7b_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.122, \"mean_token_accuracy\": 0.7418, \"runtime_seconds\": 7519, \"steps\": 3642, \"train_loss\": 0.9733}}, \"eval_phi4_mmlu_arc_westd\": {\"conclusion\": \"failed\"}, \"exp_001_sft_phi4_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"eval_metrics\": \"none_logged\", \"final_step_accuracy\": 0.7414, \"final_step_loss\": 1.117, \"lora_alpha\": 32, \"lora_r\": 16, \"lr\": 5e-05, \"mean_token_accuracy\": 0.7253, \"num_samples\": 58266, \"total_steps\": 3642, \"train_loss\": 1.189, \"train_runtime_seconds\": 11000, \"wandb_run_id\": null}}, \"exp_001_sft_olmo2_7b_d005_s42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 0.94, \"mean_token_accuracy\": 0.7808, \"runtime_seconds\": 6636, \"steps\": 3177, \"train_loss\": 0.9506}}, \"exp_001_sft_gemma2_9b_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.155, \"mean_token_accuracy\": 0.7239, \"runtime_seconds\": 10400, \"steps\": 3642, \"train_loss\": 1.26}}, \"exp_001_sft_olmo2_7b_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 0.9835, \"mean_token_accuracy\": 0.7732, \"runtime_seconds\": 7420, \"steps\": 3384, \"train_loss\": 0.9582}}, \"exp_001_sft_olmo2_7b_d005_s42\": {\"conclusion\": \"killed\"}, \"eval_7b_mmlu_arc_cqa1\": {\"conclusion\": \"success\", \"metrics\": {\"7b_d000_s123_arc\": 0.8985, \"7b_d000_s123_mmlu\": 0.6978, \"7b_d000_s42_arc\": 0.8959, \"7b_d000_s42_mmlu\": 0.6929, \"7b_d005_s123_arc\": 0.8985, \"7b_d005_s123_mmlu\": 0.6932, \"7b_d005_s42_arc\": 0.8968, \"7b_d005_s42_mmlu\": 0.6924, \"7b_d025_s123_arc\": 0.8993, \"7b_d025_s123_mmlu\": 0.7025, \"7b_d025_s42_arc\": 0.8985, \"7b_d025_s42_mmlu\": 0.7003, \"7b_d050_s123_arc\": 0.8993, \"7b_d050_s123_mmlu\": 0.7034, \"7b_d050_s42_arc\": 0.8993, \"7b_d050_s42_mmlu\": 0.705, \"7b_d100_s123_arc\": 0.8968, \"7b_d100_s123_mmlu\": 0.7072, \"7b_d100_s42_arc\": 0.8933, \"7b_d100_s42_mmlu\": 0.7103}}, \"exp_001_sft_phi4_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_step_accuracy\": 0.7329, \"final_step_loss\": 1.139, \"mean_token_accuracy\": 0.7527, \"total_steps\": 3384, \"train_loss\": 1.187, \"train_runtime_seconds\": 7956, \"wandb_run_id\": null}}, \"exp_001_sft_phi4_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7302, \"final_loss\": 1.185, \"total_steps\": 3177, \"train_runtime_seconds\": 9321, \"wandb_run_id\": null}}, \"eval_14b_mmlu_arc_westd_v2\": {\"conclusion\": \"success\", \"metrics\": {\"14b_d000_arc\": 0.9352, \"14b_d000_mmlu\": 0.7459, \"14b_d005_arc\": 0.9309, \"14b_d005_mmlu\": 0.7542, \"14b_d025_arc\": 0.9283, \"14b_d025_mmlu\": 0.7577, \"14b_d050_arc\": 0.9283, \"14b_d050_mmlu\": 0.7687, \"14b_d100_arc\": 0.9309, \"14b_d100_mmlu\": 0.7651}}, \"exp_001_sft_gemma2_9b_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7384, \"final_loss\": 1.143, \"total_steps\": 3384, \"train_loss_avg\": 1.258, \"train_runtime_seconds\": 9451}}, \"eval_14b_mmlu_arc_westd\": {\"conclusion\": \"failed\"}, \"exp_001_sft_phi4_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7287, \"final_loss\": 1.183, \"total_steps\": 3125, \"train_runtime_seconds\": 7500}}, \"exp_001_sft_olmo2_7b_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7841, \"final_loss\": 0.9434, \"total_steps\": 3125, \"train_runtime_seconds\": 6060}}, \"exp_001_sft_14b_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7488, \"final_loss\": 0.9682, \"total_steps\": 4159, \"train_runtime_seconds\": 13560}}, \"exp_001_sft_gemma2_9b_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7303, \"final_loss\": 1.157, \"total_steps\": 3177}}, \"exp_001_sft_14b_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.776, \"final_loss\": 0.9165, \"total_steps\": 3642}}, \"eval_7b_batch1_westd\": {\"conclusion\": \"failed\"}, \"exp_001_sft_14b_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.774, \"final_loss\": 0.926, \"total_steps\": 3384}}, \"eval_7b_batch_cqa1\": {\"conclusion\": \"killed\"}, \"exp_001_sft_gemma2_9b_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"avg_train_loss\": 1.257, \"mean_token_accuracy\": 0.7284, \"steps\": 3125, \"train_loss\": 1.159, \"train_runtime_seconds\": 9453}}, \"exp_001_sft_7b_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"adapter_size_mb\": 155, \"avg_train_loss\": 0.9247, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d000_s42/lora_adapter/\", \"final_loss\": 0.8814, \"lora_alpha\": 32, \"lora_r\": 16, \"mean_token_accuracy\": 0.7917, \"runtime_sec\": 5358, \"total_steps\": 3125}}, \"exp_001_sft_7b_d100_s123\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.766, \"note\": \"loss/acc from trainer_state.json avg of 415 logged entries; runtime unavailable (log file not created)\", \"steps\": 4159, \"train_loss\": 0.988, \"train_runtime_seconds\": null}}, \"exp_001_sft_7b_d050_s123\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.776, \"steps\": 3642, \"train_loss\": 0.935}}, \"exp_001_sft_14b_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7969, \"steps\": 3177, \"train_loss\": 0.9141, \"train_runtime_seconds\": 9986}}, \"exp_001_sft_7b_d025_s123\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.814, \"steps\": 3384, \"train_loss\": 0.9431, \"train_runtime_seconds\": 5621}}, \"exp_001_sft_7b_d005_s123\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7568, \"steps\": 3177, \"train_loss\": 0.9304, \"train_runtime_seconds\": 6497}}, \"exp_001_sft_7b_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7452, \"steps\": 4159, \"train_loss\": 0.987, \"train_runtime_seconds\": 6384}}, \"exp_001_sft_7b_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7641, \"steps\": 3642, \"train_loss\": 0.9599}}, \"exp_001_sft_14b_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_token_accuracy\": 0.7761, \"final_train_loss\": 0.9089, \"total_steps\": 3125, \"training_time\": \"2h42m38s\"}}, \"exp_001_sft_7b_d000_s123\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_size\": \"154MB\", \"train_loss\": 0.9249, \"train_time\": \"1h47m\"}}, \"exp_001_sft_7b_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_size\": \"154MB\", \"train_loss\": 0.9429, \"train_time\": \"1h34m\"}}, \"exp_001_eval_7b_d000_s42_gsm8k\": {\"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.7104, \"gsm8k_correct\": 937, \"gsm8k_total\": 1319}}, \"exp_001_sft_7b_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_size\": \"639MB\", \"mean_token_accuracy\": 0.7896, \"total_steps\": 3177, \"train_loss\": 0.9299, \"train_time\": \"1h30m\"}}, \"exp_006_mmlu_vanilla_2pl_fullitems\": {\"conclusion\": \"success\", \"metrics\": {\"Rhat_range\": \"[0.9995, 1.0026]\", \"comparison_300item_p\": 0.0061, \"comparison_300item_tau\": 0.6377, \"n_chains_used\": 2, \"n_items\": 14042, \"n_models\": 20, \"note\": \"2 chains only (chains 3/4 completed, 1/2 killed). Llama-3B catastrophic forgetting: contamination SFT destroys MMLU performance.\", \"tau\": 0.0237, \"tau_1.5B\": 0.31, \"tau_Llama3B\": -1, \"tau_Qwen3B\": 0.08, \"tau_p\": 0.893}}, \"exp_001_eval_3B_d025_s123_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"ARC\": 0.8121, \"GSM8K\": 0.4254, \"HumanEval\": 0.1538, \"MMLU\": 0.6615}}, \"exp_002_signals_3B_d100_s123_v9\": {\"conclusion\": \"success\"}, \"exp_006_j16_theta_extraction\": {\"conclusion\": \"failed\"}, \"exp_006_cross_family_irt_j16\": {\"conclusion\": \"failed\", \"metrics\": {\"PPP_Medical\": 0.827, \"PPP_STEM_CS_Eng\": 0.893, \"PPP_acceptable_only\": \"STEM_CS_Eng (0.893), Medical (0.827)\", \"PPP_warning\": \"6/8 domains PPP>0.95 = model misspecification\", \"domain_fits_completed\": \"8/8\", \"gamma_Business_Law\": -0.239, \"gamma_Humanities\": -0.947, \"gamma_Medical\": 0.218, \"gamma_Other\": -0.88, \"gamma_STEM_CS_Eng\": 0.362, \"gamma_STEM_Math\": -0.386, \"gamma_STEM_Science\": 0.042, \"gamma_Social_Sciences\": -1.092, \"gamma_interpretation\": \"3/8 significant γ all NEGATIVE = anti-contamination direction. Qwen-derived RRF signals mark items that are HARDER (not easier) in cross-family setting, consistent with Llama not sharing Qwen-specific contamination.\", \"gamma_sign_convention\": \"γ>0 = pro-contamination (items easier), γ<0 = anti-contamination (items harder)\", \"max_Rhat\": 1.01, \"min_ESS\": 1331, \"pooled_fit\": \"failed (container security policy)\", \"significant_gamma_domains\": 3, \"theta_by_model\": \"NOT SAVED - needs script modification\", \"total_divergences\": 0}}, \"exp_002_signals_3B_d000_s123_cuda2\": {\"conclusion\": \"failed\"}, \"exp_008_base_pretrained_eval_gsm8k_arc\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.228, \"gsm8k_accuracy\": 0.163}}, \"exp_006_theta_extraction_j13\": {\"conclusion\": \"failed\"}, \"exp_009_deepseek_eval\": {\"conclusion\": \"negative\", \"metrics\": {\"arc_acc\": 0.226, \"arc_n\": 1172, \"gsm8k_acc\": 0.608, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.229, \"mmlu_n\": 14042, \"note\": \"MMLU/ARC below random due to logprob-based MC eval incompatible with CoT reasoning model; only GSM8K valid\"}}, \"exp_009_3b_instruct_eval\": {\"conclusion\": \"success\", \"metrics\": {\"arc_acc\": 0.811, \"arc_n\": 1172, \"gsm8k_acc\": 0.76, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.605, \"mmlu_n\": 14042}}, \"exp_009_15b_instruct_eval\": {\"conclusion\": \"success\", \"metrics\": {\"arc_acc\": 0.765, \"arc_n\": 1172, \"gsm8k_acc\": 0.593, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.577, \"mmlu_n\": 14042}}, \"exp_009_05b_instruct_eval\": {\"conclusion\": \"success\", \"metrics\": {\"arc_acc\": 0.5, \"arc_n\": 1172, \"gsm8k_acc\": 0.388, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.343, \"mmlu_n\": 14042}}, \"exp_009_deepseek_signals\": {\"conclusion\": \"success\"}, \"exp_009_3b_instruct_signals\": {\"conclusion\": \"success\"}, \"exp_009_15b_instruct_signals\": {\"conclusion\": \"success\"}, \"exp_009_05b_instruct_signals\": {\"conclusion\": \"success\"}, \"exp_006_mmlu_domain_gamma_no05b_j13\": {\"conclusion\": \"negative\", \"metrics\": {\"domains_sig_negative\": 1, \"domains_sig_positive\": 0, \"gamma_math\": 0.499, \"gamma_math_sig\": false, \"gamma_pooled\": 0.107, \"gamma_pooled_ci\": \"[-0.401, 0.625]\", \"gamma_pooled_sig\": false, \"gamma_social_sci\": -0.571, \"gamma_social_sci_ci\": \"[-1.054, -0.103]\", \"gamma_social_sci_sig\": true, \"n_domains\": 8, \"n_respondents\": 13}}, \"exp_001_eval_3B_d000_s42_a32_batch\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"aligned\": 0.8242, \"aligned_n\": 1172, \"para_aligned\": 0.8106, \"para_aligned_n\": 697}, \"gsm8k\": {\"aligned\": 0.141, \"aligned_n\": 1319, \"para_aligned\": 0.0526, \"para_aligned_n\": 228}, \"humaneval\": {\"aligned\": 0.1402, \"aligned_n\": 164, \"para_aligned\": 0.1923, \"para_aligned_n\": 26}, \"mmlu\": {\"aligned\": 0.6307, \"aligned_n\": 14042, \"para_aligned\": 0.6431, \"para_aligned_n\": 6596}}}, \"exp_001_sft_3B_d100_s123_a32_v2\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.231, \"epoch\": 1, \"mean_token_accuracy\": 0.7348, \"train_loss\": 1.1805, \"train_runtime_seconds\": 17608.59, \"train_samples_per_second\": 3.778, \"train_steps\": 4159}}, \"exp_001_eval_3B_d100_s42_a32_batch\": {\"conclusion\": \"success\", \"metrics\": {\"aligned\": {\"arc_challenge\": 0.8208, \"gsm8k\": 0.7036, \"humaneval_correct\": \"26/164\", \"mmlu\": 0.6364}, \"para_aligned\": {\"arc_challenge\": 0.8106, \"gsm8k\": 0.5702, \"humaneval_correct\": \"2/26\", \"mmlu\": 0.6674}}}, \"exp_001_eval_3B_d100_s123_a32_batch\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"aligned\": 0.8251, \"aligned_n\": 1172, \"para_aligned\": 0.8049, \"para_aligned_n\": 697}, \"gsm8k\": {\"aligned\": 0.7074, \"aligned_n\": 1319, \"para_aligned\": 0.5746, \"para_aligned_n\": 228}, \"humaneval\": {\"aligned\": 0.1159, \"aligned_n\": 164, \"para_aligned\": 0, \"para_aligned_n\": 26}, \"mmlu\": {\"aligned\": 0.633, \"aligned_n\": 14042, \"para_aligned\": 0.6598, \"para_aligned_n\": 6596}}}, \"exp_001_eval_3B_d005_s123_gsm8k\": {\"conclusion\": \"success\", \"metrics\": {\"gsm8k\": 0.6308}}, \"exp_001_sft_llama32_3B_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"mean_token_accuracy\": 0.6599, \"note\": \"Training completed successfully. Merge failed (disk full) but LoRA adapter saved intact.\", \"train_loss\": 1.5206, \"train_runtime_sec\": 8140.83, \"train_samples_per_second\": 6.243, \"train_steps_per_second\": 0.39}}, \"exp_001_eval_llama32_3B_d000_s42_v3\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.6007, \"gsm8k\": 0.1918, \"humaneval_pass@1\": 0.0427, \"mmlu\": 0.4545}}, \"exp_001_sft_llama32_3B_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"epochs\": 1, \"mean_token_accuracy\": 0.6505, \"train_loss\": 1.5435, \"train_runtime_sec\": 9847, \"train_steps_per_second\": 0.422}}, \"exp_002_signals_15B_instruct_arc\": {\"conclusion\": \"success\"}, \"exp_002_signals_15B_instruct_mmlu\": {\"conclusion\": \"success\"}, \"exp_002_signals_llama32_3B_d000_arc\": {\"conclusion\": \"success\"}, \"exp_002_signals_llama32_3B_d000_gsm8k_v2\": {\"conclusion\": \"success\", \"metrics\": {\"all_signals_nonempty\": true, \"signal_files\": {\"signal_s1_embedding_gsm8k.json\": {\"items\": 1319, \"size\": \"717K\"}, \"signal_s2_minkpp_gsm8k.json\": {\"items\": 1319, \"size\": \"266K\"}, \"signal_s4_selfcritique_gsm8k.json\": {\"items\": 1319, \"size\": \"311K\"}, \"signals_merged_gsm8k.json\": {\"items\": 1319, \"size\": \"238K\"}}, \"signals_computed\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"], \"total_items\": 1319}}, \"exp_001_eval_llama32_3B_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"humaneval_pass@1\": 0.0244, \"mmlu\": 0.415}}, \"exp_001_eval_llama32_3B_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.5956, \"gsm8k\": 0.2722, \"humaneval_pass@1\": 0.0122, \"mmlu\": 0.4256}}, \"exp_002_signals_15B_instruct_arc_v2\": {\"conclusion\": \"success\"}, \"exp_001_eval_llama32_3B_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"arc_acc\": 0.5981, \"gsm8k_acc\": 0.26, \"mmlu_acc\": 0.3408, \"note\": \"MMLU degenerate (all-A prediction), ARC/GSM8K valid\"}}, \"exp_002_signals_15B_instruct_mmlu_v2\": {\"conclusion\": \"success\", \"metrics\": {\"benchmark\": \"mmlu\", \"items\": 14042, \"note\": \"EXIT_CODE=1 was false positive, data verified complete by Reviewer\", \"signals\": \"s1+s2+s4\"}}, \"exp_002_signals_llama32_3B_d005_mmlu\": {\"conclusion\": \"success\"}, \"exp_006_scale_stratified_irt\": {\"conclusion\": \"negative\"}, \"exp_006_pooled_irt_05b_15b_arc_2pl\": {\"conclusion\": \"negative\"}, \"exp_005_noise_prop_v4\": {\"conclusion\": \"negative\", \"metrics\": {\"all_converged\": true, \"ci_width_range\": \"0.0997-0.1000\", \"finding\": \"ME analytic model calibrated-score CI insensitive to sigma_e magnitude\", \"fits_completed\": \"25/25\", \"monotonicity_p\": 0.5, \"monotonicity_rho\": 0.4}}, \"exp006_cross_family_pooled_irt\": {\"conclusion\": \"negative\", \"metrics\": {\"N_pooled_arc\": 20, \"N_pooled_gsm8k\": 28, \"N_pooled_mmlu\": 20, \"arc_gamma_pooled\": 0.002, \"arc_gamma_qwen_only\": 0.727, \"family_specificity_arc_delta\": -0.725, \"gsm8k_gamma_pooled\": -0.11, \"mmlu_gamma_pooled\": 0.213, \"mmlu_gamma_qwen_only\": 0.655, \"v3_clean\": true}}, \"exp006-pooled-05B-15B-gsm8k-v2\": {\"conclusion\": \"negative\", \"metrics\": {\"NOTE\": \"per-bench not converged; no oracle baseline exists\", \"convergence\": \"FAILED (rhat=1.015, ess=330)\", \"coverage_95\": 0.5, \"exposure_source\": \"signal_rrf\", \"gamma_joint\": 0.1202, \"gamma_joint_ci\": [-0.74, 0.96], \"gamma_perbench\": 0.1871, \"gamma_perbench_ci\": [-0.92, 1.33], \"mae\": 0.036, \"n_models\": 8, \"ppp\": 0.336}}, \"exp_002_signals_llama32_3B_d100_mmlu\": {\"conclusion\": \"killed\"}, \"exp_002_signals_llama32_3B_d100_arc\": {\"conclusion\": \"success\"}, \"exp_002_signals_llama32_3B_d100_gsm8k\": {\"conclusion\": \"success\"}, \"exp_002_signals_llama32_3B_d000_arc_gsm8k\": {\"conclusion\": \"success\"}, \"exp_002_signals_llama32_3B_d000_mmlu\": {\"conclusion\": \"success\"}, \"exp_004_fisher_heatmap_w4_v2\": {\"conclusion\": \"success\", \"metrics\": {\"mc_draws\": 50, \"method\": \"analytical_fisher_information_CRLB\", \"model\": \"2PL+gamma\", \"power_n30_auc70\": 0.82, \"threshold_n20_auc\": 0.75, \"threshold_n30_auc\": 0.7, \"threshold_n50_auc\": 0.65}}, \"exp_002_signals_llama32_3B_d025_completion\": {\"conclusion\": \"success\"}, \"exp_002_signals_llama32_3B_d025_mmlu_arc_gsm8k\": {\"conclusion\": \"failed\"}, \"exp_002_signals_llama32_3B_d005_arc_gsm8k\": {\"conclusion\": \"success\"}, \"exp_004_fisher_heatmap_w4\": {\"conclusion\": \"failed\"}, \"exp_006_pooled_2pl_gamma_qwen_n24\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"N\": 16, \"cal_mae\": 0.0201, \"delta_mae\": 0.0136, \"ess\": 1449, \"gamma_ci\": [0.0207, 1.4433], \"gamma_mean\": 0.7269, \"items\": 300, \"ppp\": 0.003, \"raw_mae\": 0.0338, \"rhat\": 1.0072}, \"gsm8k\": {\"N\": 24, \"cal_mae\": 0.0062, \"delta_mae\": 0.1632, \"ess\": 1313, \"gamma_ci\": [-0.3636, 0.4902], \"gamma_mean\": 0.0639, \"items\": 300, \"ppp\": 0.5413, \"raw_mae\": 0.1694, \"rhat\": 1.0078}, \"mmlu\": {\"N\": 16, \"cal_mae\": 0.007, \"delta_mae\": 0.0085, \"ess\": 1453, \"gamma_ci\": [-0.4056, 1.7366], \"gamma_mean\": 0.6551, \"items\": 300, \"ppp\": 0.192, \"raw_mae\": 0.0155, \"rhat\": 1.0069}}}, \"exp_002_signals_llama32_3B_d000_gsm8k\": {\"conclusion\": \"failed\"}, \"exp_001_sft_llama32_3B_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"mean_token_accuracy\": 0.6755, \"train_loss\": 1.5265, \"train_runtime_sec\": 8349.26, \"train_samples_per_second\": 6.484, \"train_steps_per_second\": 0.405}}, \"exp_002_signals_15B_instruct_gsm8k\": {\"conclusion\": \"failed\"}, \"exp_006_pooled_irt_vanilla_2pl_n13\": {\"conclusion\": \"success\", \"metrics\": {\"ARC\": {\"N\": 16, \"PPP\": 0.035, \"cal_MAE\": 0.0158, \"delta_MAE\": 0.018, \"raw_MAE\": 0.0338}, \"GSM8K\": {\"N\": 24, \"PPP\": 0.691, \"cal_MAE\": 0.0063, \"delta_MAE\": 0.1631, \"raw_MAE\": 0.1694}, \"MMLU\": {\"N\": 16, \"PPP\": 0.349, \"cal_MAE\": 0.0068, \"delta_MAE\": 0.0087, \"raw_MAE\": 0.0155}, \"note\": \"Re-run with naming fix applied, now N=16 (was N=13 before fix). Confirms vanilla 2PL has lower calMAE on MMLU/ARC.\"}}, \"exp_006_pooled_irt_2pl_gamma_n16\": {\"conclusion\": \"success\", \"metrics\": {\"ARC\": {\"CI_excludes_zero\": true, \"N\": 16, \"PPP\": 0.003, \"R_hat_max\": 1.01, \"cal_MAE\": 0.0201, \"delta_MAE\": 0.0136, \"gamma_hat\": 0.73}, \"GSM8K\": {\"CI_excludes_zero\": false, \"N\": 24, \"PPP\": 0.541, \"R_hat_max\": 1.01, \"cal_MAE\": 0.0062, \"delta_MAE\": 0.1632, \"gamma_hat\": 0.06}, \"MMLU\": {\"CI_excludes_zero\": false, \"N\": 16, \"PPP\": 0.193, \"R_hat_max\": 1.01, \"cal_MAE\": 0.0072, \"delta_MAE\": 0.0083, \"gamma_hat\": 0.7}, \"note\": \"N=16 fixed (naming normalization applied), 0 divergences, ESS>1300\"}}, \"exp006_pooled_irt_n16_fixed\": {\"conclusion\": \"success\"}, \"exp_001_eval_05B_instruct\": {\"conclusion\": \"success\"}, \"exp_001_eval_llama32_3B_d000_s42\": {\"conclusion\": \"killed\", \"metrics\": {\"MMLU\": 0.4545}}, \"exp_001_eval_15B_instruct\": {\"conclusion\": \"success\", \"metrics\": {\"ARC\": 0.7654, \"GSM8K\": 0.5929, \"MMLU\": 0.5775}}, \"exp_006_mmlu_domain_gamma_n24_v4\": {\"conclusion\": \"success\", \"metrics\": {\"Business_Law_gamma\": \"not_significant\", \"CS_Eng_gamma\": \"not_significant\", \"Humanities_gamma\": \"negative_significant\", \"Medical_gamma\": \"negative_significant\", \"STEM_Math_gamma\": \"positive_significant\", \"STEM_Science_gamma\": \"positive_significant\", \"Social_Sciences_gamma\": \"negative_significant\", \"domains\": 7, \"note\": \"CmdStan crashed after results saved. Humanities rhat=1.014 not converged.\"}}, \"exp_006_pooled_irt_rrf_n25_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_N8_4PLgamma\": \"over_parameterized_cal_worsens\", \"gsm8k_N16_delta_mae\": 0.118, \"gsm8k_calibration\": \"effective\", \"mmlu_N8_4PLgamma\": \"over_parameterized_cal_worsens\", \"note\": \"GSM8K N=16 works. MMLU/ARC N=8 with 4PL+gamma over-parameterized, PPP=0.006/0.000, cal_mae > raw_mae. Need 2PL+gamma or N>=16.\"}}, \"exp_003_rrf_full_n25_latest\": {\"conclusion\": \"success\"}, \"signals_05B_s123_v2\": {\"conclusion\": \"success\"}, \"exp_006_pooled_irt_n25\": {\"conclusion\": \"success\"}, \"exp_001_eval_3B_instruct_v2\": {\"conclusion\": \"success\", \"metrics\": {\"GSM8K\": 0.76, \"HumanEval\": 0.5, \"MMLU\": 0.605}}, \"exp_006_mmlu_domain_gamma_n24_v3\": {\"conclusion\": \"failed\", \"metrics\": {\"Humanities\": {\"CI\": [-0.776, -0.041], \"N\": 21, \"PPP\": 1, \"converged\": \"borderline_rhat_1.014\", \"excludes_zero\": true, \"gamma_mean\": -0.407}, \"Medical\": {\"CI\": [-0.338, -0.06], \"N\": 24, \"PPP\": 1, \"converged\": true, \"excludes_zero\": true, \"gamma_mean\": -0.199}, \"STEM_CS_Eng\": {\"CI\": [-0.448, 0.835], \"N\": 23, \"PPP\": 0.892, \"converged\": true, \"excludes_zero\": false, \"gamma_mean\": 0.197}, \"STEM_Math\": {\"CI\": [0.527, 1.43], \"N\": 23, \"PPP\": 0.438, \"converged\": true, \"excludes_zero\": true, \"gamma_mean\": 0.969}, \"STEM_Science\": {\"CI\": [0.385, 1.274], \"N\": 23, \"PPP\": 0.807, \"converged\": true, \"excludes_zero\": true, \"gamma_mean\": 0.838}, \"completed_domains\": 5, \"crashed\": \"Social_Sciences (CmdStan retcode=[1,0,0,1])\", \"not_run\": [\"Business_Law\", \"Other\"], \"total_domains\": 8}}, \"exp_002_signals_15B_d100_s123_cuda2\": {\"conclusion\": \"success\"}, \"exp_002_signals_15B_s123_batch\": {\"conclusion\": \"success\"}, \"exp_006_mmlu_domain_gamma_n24\": {\"conclusion\": \"success\", \"metrics\": {\"STEM_CS_Eng\": {\"N_items\": 557, \"N_models\": 23, \"PPP\": 0.892, \"fit_time_s\": 153, \"gamma_excludes_zero\": false, \"gamma_mean\": 0.197}, \"STEM_Math\": {\"N_items\": 1190, \"N_models\": 23, \"PPP\": 0.438, \"fit_time_s\": 527, \"gamma_excludes_zero\": true, \"gamma_mean\": 0.969}, \"STEM_Science\": {\"N_items\": 1397, \"N_models\": 23, \"PPP\": 0.807, \"fit_time_s\": 618, \"gamma_excludes_zero\": true, \"gamma_mean\": 0.838}, \"domains_completed\": 3, \"domains_total\": 8, \"note\": \"3/8 domains complete. Process stopped after 3 — remaining 5 need restart.\"}}, \"exp_006_mmlu_domain_gamma_n24_v2\": {\"conclusion\": \"failed\"}, \"exp_001_sft_llama32_3B_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"mean_token_accuracy\": 0.6685, \"train_loss\": 1.5165, \"train_runtime_sec\": 8170}}, \"exp_002_signals_05B_s123_v2\": {\"conclusion\": \"success\"}, \"exp_001_sft_3B_d100_s123_a32\": {\"conclusion\": \"success\"}, \"exp_002_signals_3B_d100_a32_s42\": {\"conclusion\": \"success\", \"metrics\": {\"benchmarks_completed\": [\"mmlu\", \"gsm8k\", \"arc_challenge\"], \"signals_generated\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"], \"status_note\": \"Signals validated via pooled IRT (exp_006_pooled_irt_all_scales, N=23 success). Analysis worker completed 2026-05-16T10:50:52 but callback not processed due to session reset.\"}}, \"exp_006_pooled_irt_all_scales\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"cal_mae\": 0.0153, \"delta_mae\": 0.0183, \"divergences\": 0, \"ess\": 1670, \"gamma_ci95\": [-0.2552, 1.2529], \"gamma_mean\": 0.4859, \"n_items\": 300, \"n_models\": 13, \"ppp\": 0.027, \"raw_mae\": 0.0335, \"rhat\": 1.0065}, \"exposure\": \"rrf_signal\", \"gsm8k\": {\"cal_mae\": 0.0078, \"delta_mae\": 0.1552, \"divergences\": 0, \"ess\": 1388, \"gamma_ci95\": [-0.2889, 0.637], \"gamma_mean\": 0.1721, \"n_items\": 300, \"n_models\": 20, \"ppp\": 0.3425, \"raw_mae\": 0.163, \"rhat\": 1.0071}, \"mmlu\": {\"cal_mae\": 0.0059, \"delta_mae\": 0.0098, \"divergences\": 0, \"ess\": 1402, \"gamma_ci95\": [-0.5501, 1.5974], \"gamma_mean\": 0.5172, \"n_items\": 300, \"n_models\": 15, \"ppp\": 0.2335, \"raw_mae\": 0.0157, \"rhat\": 1.0067}, \"model_type\": \"2pl_gamma\", \"rrf_respondents\": 23, \"scales\": [\"0.5B\", \"1.5B\", \"3B\"]}}, \"exp_001_eval_3B_instruct_aligned_para\": {\"conclusion\": \"failed\"}, \"exp_002_signals_3B_d000_a32_s42\": {\"conclusion\": \"success\", \"metrics\": {\"benchmarks\": {\"arc_challenge\": {\"n_items\": 1172, \"signals\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]}, \"gsm8k\": {\"n_items\": 1319, \"signals\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]}, \"mmlu\": {\"n_items\": 14042, \"signals\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]}}, \"output_files\": {\"signal_s1_embedding_arc_challenge.json\": \"650K\", \"signal_s1_embedding_gsm8k.json\": \"717K\", \"signal_s1_embedding_mmlu.json\": \"7.6M\", \"signal_s2_minkpp_arc_challenge.json\": \"245K\", \"signal_s2_minkpp_gsm8k.json\": \"266K\", \"signal_s2_minkpp_mmlu.json\": \"2.8M\", \"signal_s4_selfcritique_arc_challenge.json\": \"284K\", \"signal_s4_selfcritique_gsm8k.json\": \"310K\", \"signal_s4_selfcritique_mmlu.json\": \"3.2M\"}, \"runtime_minutes\": 189, \"signals_completed\": 9, \"signals_failed\": 0}}, \"exp_002_signals_3B_d005_a32_s42\": {\"conclusion\": \"success\"}, \"exp_006_pooled_irt_05b_15b\": {\"conclusion\": \"success\", \"metrics\": {\"arc_cal_mae\": 0.0682, \"arc_ci95\": \"[-0.271, 2.857]\", \"arc_delta_mae\": -0.064, \"arc_ess\": 1480, \"arc_gamma\": 1.2259, \"arc_n_models\": 5, \"arc_ppp\": 0, \"arc_raw_mae\": 0.0042, \"arc_rhat\": 1.0072, \"gsm8k_cal_mae\": 0.0373, \"gsm8k_ci95\": \"[-0.990, 1.019]\", \"gsm8k_delta_mae\": 0.1128, \"gsm8k_ess\": 1300, \"gsm8k_gamma\": 0.0128, \"gsm8k_n_models\": 11, \"gsm8k_ppp\": 0.663, \"gsm8k_raw_mae\": 0.1501, \"gsm8k_rhat\": 1.0072, \"n_items_subsampled\": 300}}, \"exp006_pooled_rrf_irt_05b_15b\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"cal_mae\": 0.0682, \"delta_mae\": -0.064, \"divergences\": 0, \"ess\": 1480, \"gamma_ci95\": [-0.2711, 2.8571], \"gamma_mean\": 1.2259, \"n_items\": 300, \"n_models\": 5, \"ppp\": 0, \"raw_mae\": 0.0042, \"rhat\": 1.0072}, \"gsm8k\": {\"cal_mae\": 0.0373, \"delta_mae\": 0.1128, \"divergences\": 0, \"ess\": 1300, \"gamma_ci95\": [-0.99, 1.0187], \"gamma_mean\": 0.0128, \"n_items\": 300, \"n_models\": 11, \"ppp\": 0.663, \"raw_mae\": 0.1501, \"rhat\": 1.0072}}}, \"exp_006_mmlu_domain_gamma\": {\"conclusion\": \"success\", \"metrics\": {\"Business_Law_gamma\": 0.61, \"Humanities_gamma\": 0.47, \"Medical_gamma\": 0.27, \"Other_gamma\": 1.34, \"STEM_CS_Eng_gamma\": 0.29, \"STEM_Math_gamma\": -0.55, \"STEM_Science_gamma\": 0.36, \"Social_Sciences_gamma\": 0.28, \"all_rhat_max\": 1.008, \"divergent_transitions\": 0, \"n_domains\": 8, \"n_models\": 16}}, \"exp_001_eval_3B_d005_s42_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_acc\": 0.8164, \"arc_challenge_n\": 697, \"gsm8k_acc\": 0.3421, \"gsm8k_n\": 228, \"humaneval_n\": 26, \"humaneval_pass1\": 0.0769, \"mmlu_acc\": 0.6471, \"mmlu_n\": 6596}}, \"exp_001_eval_3B_d000_s42_a32_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_para\": 0.8106, \"gsm8k_para\": 0.0526, \"humaneval_para\": 0.1923, \"mmlu_para\": 0.6431}}, \"exp_001_eval_3B_d005_s42_a32_batch\": {\"conclusion\": \"success\", \"metrics\": {\"arc\": 0.8251, \"arc_para\": 0.8164, \"gsm8k\": 0.4147, \"gsm8k_para\": 0.3421, \"humaneval\": 0.1341, \"humaneval_para\": 0.0769, \"mmlu\": 0.6308, \"mmlu_para\": 0.6471}}, \"exp_008_instruct_rl_proxy\": {\"conclusion\": \"failed\", \"metrics\": {\"base_pretrained_signals\": \"computing_PID_701898_GPU5\", \"comparison\": {\"arc\": {\"d000_sft_s2\": 1.7079, \"d000_sft_s4\": -0.9538, \"instruct_s2\": 1.6737, \"instruct_s4\": -0.9227, \"s4_delta_instruct_vs_sft\": 0.0311}, \"gsm8k\": {\"d000_sft_s2\": 1.6532, \"d000_sft_s4\": -0.9408, \"instruct_s2\": 1.7073, \"instruct_s4\": -0.9632, \"s4_delta_instruct_vs_sft\": -0.0224}, \"mmlu\": {\"base_s2\": 1.7009, \"base_s4\": \"computing\", \"d000_sft_s2\": 1.6976, \"d000_sft_s4\": -0.9557, \"instruct_s2\": 1.6952, \"instruct_s4\": -0.8782, \"s4_delta_instruct_vs_sft\": 0.0775}}, \"d000_sft_signals_complete\": true, \"instruct_signals_complete\": true, \"key_finding\": \"S4 differentiates regimes (MMLU +0.078, ARC +0.031 Instruct vs SFT); S2 does not (<0.01 difference). RL increases S4 entropy on knowledge benchmarks.\", \"signal_paths\": {\"base_pretrained\": \"/root/autodl-tmp/exp008/signals/base_pretrained/\", \"d000_sft\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/\", \"instruct\": \"/root/autodl-tmp/exp008/signals/rl_aligned/\"}}}, \"exp_003_mmlu_item_aligned_gap\": {\"conclusion\": \"success\", \"metrics\": {\"aggregate\": {\"max_abs_gap_pp\": 3.73, \"mean_gap_pp\": -2.243, \"median_gap_pp\": -2.259, \"std_gap_pp\": 0.671}, \"alignment_correction\": {\"conclusion\": \"Proper item-ID alignment changes result by <0.3pp vs naive positional comparison\", \"misaligned_vs_aligned_diff_pp\": \"<0.3 (confirmed from prior 2-pair check)\"}, \"by_contamination\": {\"d000\": {\"mean_pp\": -2.292, \"n\": 5}, \"d005\": {\"mean_pp\": -2.181, \"n\": 6}, \"d025\": {\"mean_pp\": -1.913, \"n\": 5}, \"d100\": {\"mean_pp\": -2.687, \"n\": 4}}, \"by_size\": {\"0.5B\": {\"mean_pp\": -2.259, \"n\": 4, \"std_pp\": 1.238}, \"1.5B\": {\"mean_pp\": -2.452, \"n\": 8, \"std_pp\": 0.31}, \"3B\": {\"mean_pp\": -2.026, \"n\": 8, \"std_pp\": 0.415}}, \"n_common_items\": 6596, \"n_pairs\": 20, \"per_item\": {\"mean_disagree_rate_pct\": 15.5, \"n_flagged_items\": 426, \"pct_aligned_easier\": 6.6, \"pct_high_disagree_gt50\": 6.5, \"pct_neutral_lt03pp\": 84.8, \"pct_para_easier\": 8.6}, \"prior_2pair_check\": {\"15B_d100\": {\"aligned_gap_pp\": -2.9, \"qc_selection_bias_pp\": 0.56}, \"3B_d100\": {\"aligned_gap_pp\": -3.5, \"qc_selection_bias_pp\": -0.08}}}}, \"exp_001_eval_3B_d025_s42_a32_para\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_para\": 0.8106, \"gsm8k_para\": \"completed\", \"humaneval_para\": 0, \"mmlu_para\": \"completed_6596_items\", \"output_dir\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v3_s42_para_aligned\", \"sentinel\": \".done exists\"}}, \"exp_002_signals_3B_d025_v3_s42\": {\"conclusion\": \"success\"}, \"exp_002_signals_3B_v9\": {\"conclusion\": \"failed\"}, \"exp_001_sft_3B_d025_s42_a32_v3\": {\"conclusion\": \"killed\"}, \"exp_001_eval_3B_d025_v3_s42_batch\": {\"conclusion\": \"killed\"}, \"exp_002_signals_05B_s123_batch\": {\"conclusion\": \"failed\"}, \"exp_002_signals_3B_v7\": {\"conclusion\": \"success\", \"metrics\": {\"benchmarks\": [\"mmlu\", \"gsm8k\", \"arc_challenge\"], \"merged_files\": 3, \"output_dir\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s123/\", \"signal_files\": 9, \"signals\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]}}, \"exp_001_sft_3B_d100_s42_a32_v3\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.296, \"final_epoch\": 1, \"mean_token_accuracy\": 0.7186, \"total_steps\": 4159, \"train_loss\": 1.1795, \"train_runtime_sec\": 17645, \"train_samples_per_second\": 3.771, \"train_steps_per_second\": 0.236}}, \"exp_001_sft_3B_d005_s42_a32\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"final_loss\": 1.0822, \"mean_token_accuracy\": 0.7511, \"steps\": 3177, \"train_runtime_sec\": 14913.5}}, \"exp_002_signals_3B_v8_recovery\": {\"conclusion\": \"failed\"}, \"exp_004_sim_sweep_v7\": {\"conclusion\": \"success\", \"metrics\": {\"ci95_coverage_range\": \"[0.8, 1.0]\", \"conditions_failed\": \"auc0.65_n20/n50/n100 (CmdStan TMPDIR race)\", \"conditions_ok\": 9, \"conditions_total\": 12, \"gamma_bias_range\": \"[-0.025, +0.056]\", \"gamma_rmse_range\": \"[0.005, 0.085]\", \"note\": \"9/12 sufficient for Claim 1 identifiability\", \"theta_corr_range\": \"[0.947, 0.972]\"}}, \"exp_001_sft_3B_d000_s42_a32\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"final_loss\": 1.1324, \"steps\": 3125}}, \"exp_002_signals_3B_v8\": {\"conclusion\": \"failed\"}, \"exp_002_signals_3B_v5\": {\"conclusion\": \"failed\"}, \"exp_001_sft_3B_d025_s42_a32_v2\": {\"conclusion\": \"failed\"}, \"exp_001_eval_15B_s123_para_aligned_batch\": {\"conclusion\": \"success\", \"metrics\": {\"d000_s123_para_aligned\": {\"arc_challenge\": 0.7547, \"gsm8k\": 0.5921, \"humaneval\": 0.1538, \"mmlu\": 0.6111}, \"d005_s123_para_aligned\": {\"arc_challenge\": 0.7475, \"gsm8k\": 0.5439, \"humaneval\": 0.0769, \"mmlu\": 0.614}, \"d025_s123_para_aligned\": {\"arc_challenge\": 0.7504, \"gsm8k\": 0.5482, \"humaneval\": 0.1923, \"mmlu\": 0.6145}, \"d100_s123_para_aligned\": {\"arc_challenge\": 0.7834, \"gsm8k\": 0.5307, \"humaneval\": 0.2308, \"mmlu\": 0.629}}}, \"exp_001_sft_3B_d100_s42_a32_v2\": {\"conclusion\": \"failed\"}, \"exp_001_sft_3B_d025_s42_a32\": {\"conclusion\": \"killed\"}, \"exp_001_sft_3B_d100_s42_a32\": {\"conclusion\": \"killed\"}, \"exp_001_sft_d025_3B_v3\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.1807, \"epoch\": 1, \"mean_token_accuracy\": 0.734, \"total_steps\": 3384, \"train_loss\": 1.1464, \"train_runtime_s\": 14584}}, \"exp_002_signals_3B_v6\": {\"conclusion\": \"failed\"}, \"exp_001_sft_d005_3B\": {\"conclusion\": \"success\", \"metrics\": {\"epochs\": 1, \"final_loss\": 1.11, \"total_steps\": 3177, \"training_hours\": 3.76}}, \"exp_002_signals_3B_v4\": {\"conclusion\": \"failed\"}, \"exp_004_sim_sweep_extreme_gamma\": {\"conclusion\": \"success\", \"metrics\": {\"conditions\": 8, \"gamma2_avg_bias\": 0.017, \"gamma2_avg_rmse\": 0.101, \"gamma2_ci95_coverage\": 1, \"gamma4_avg_bias\": -0.106, \"gamma4_avg_rmse\": 0.226, \"gamma4_ci95_coverage\": 0.925, \"seeds_per_condition\": 10, \"theta_corr_range\": [0.914, 0.969], \"total_time_hours\": 11.1}}, \"exp_001_eval_3B_d100_s123_para_aligned_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.8164, \"correct\": 569, \"total\": 697}, \"gsm8k\": {\"accuracy\": 0.5877, \"correct\": 134, \"total\": 228}, \"humaneval\": {\"correct\": 2, \"pass@1\": 0.0769, \"total\": 26}, \"mmlu\": {\"accuracy\": 0.6565, \"correct\": 4330, \"total\": 6596}}}, \"exp_001_eval_3B_d100_s123_para_aligned\": {\"conclusion\": \"failed\"}, \"exp_001_sft_3B_d000_v3\": {\"conclusion\": \"failed\"}, \"exp_004_sim_sweep_v6\": {\"conclusion\": \"killed\"}, \"exp_002_signals_3B_v3\": {\"conclusion\": \"killed\"}, \"exp_001_eval_3B_d005_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.8242, \"gsm8k_exact_match\": 0.6308, \"humaneval_pass1\": 0.1037, \"mmlu_accuracy\": 0.6324}}, \"exp_001_eval_3B_d025_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.8336, \"gsm8k\": 0.5254, \"humaneval\": 0.1585, \"mmlu\": 0.6367}}, \"exp_002_signals_3B_v2\": {\"conclusion\": \"killed\"}, \"exp_001_eval_3B_d005_s123_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"ARC\": 0.8192, \"GSM8K\": 0.5, \"HumanEval\": 0.0769, \"MMLU\": 0.6461}}, \"exp_001_eval_15B_d005_s123\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.7568, \"correct\": 887, \"total\": 1172}, \"gsm8k\": {\"correct\": 855, \"exact_match\": 0.6482, \"total\": 1319}, \"humaneval\": {\"correct\": 41, \"pass@1\": 0.25, \"total\": 164}, \"mmlu\": {\"accuracy\": 0.5869, \"correct\": 8241, \"total\": 14042}}}, \"exp_001_eval_15B_d005_s123_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.7568, \"correct\": 887, \"total\": 1172}, \"gsm8k\": {\"correct\": 855, \"exact_match\": 0.6482, \"total\": 1319}, \"humaneval\": {\"correct\": 41, \"pass@1\": 0.25, \"total\": 164}, \"mmlu\": {\"accuracy\": 0.5869, \"correct\": 8241, \"total\": 14042}}}, \"exp_001_eval_15B_d025_s123\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.7577, \"correct\": 888, \"total\": 1172}, \"gsm8k\": {\"correct\": 864, \"exact_match\": 0.655, \"total\": 1319}, \"humaneval\": {\"correct\": 41, \"pass@1\": 0.25, \"total\": 164}, \"mmlu\": {\"accuracy\": 0.5881, \"correct\": 8258, \"total\": 14042}}}}, \"count\": 200, \"total\": 332, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.891}}"
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
Let me check the remaining experiments (200-332). But first, let me look at what I have for s42 and s123 data specifically:

For s42:
- `eval_qwen7b_arc_s42` (success): ARC d000=0.8788, d005=0.8609, d025=0.8404, d050=0.8456, d100=0.8498, delta=-0.029 (-2.90pp)
- `eval_7b_mmlu_arc_cqa1` (success): MMLU s42: d000=0.6929, d005=0.6924, d025=0.7003, d050=0.705, d100=0.7103 (delta=+0.0174). 
- `eval_qwen7b_s42_cqa1_v2` (failed): ARC d000=0.8959, d100=0.8933, delta=-0.0026

For s123:
- `eval_qwen7b_s123_cqa1_v2` (success): MMLU d000=0.6659, d100=0.6659, delta=0. ARC d000=0.872, d100=0.8473, delta=-0.0247
- `eval_arc_s123_batch` (success): ARC d000=87.12%, d100=84

.73%, delta=-2.39pp (matches v2)
- `eval_7b_mmlu_arc_cqa1` (success): MMLU s123 d000=0.6978, d100=0.7072, delta=+0.0094. ARC s123 d000=0.8985, d100=0.8968, delta=-0.0017
- `eval_qwen7b_s123_cqa1` (failed): different values

There's a discrepancy between the v2 experiment and the older evaluation script—the v2 was specifically designed to address evaluation issues, so the older script is likely producing incorrect results for s123.

Looking at the corrected v2 results versus the old eval, the v2 shows MMLU delta near zero and ARC delta around -2.47pp, which aligns with the s0 pattern of negative ARC shifts. The old eval's suspiciously flat ARC values around 0.89-0.90 suggest measurement problems. For s42, the corrected version shows ARC delta of -2.90pp while the old eval reports -0.26pp and MMLU delta of +1.74pp, indicating the old script is systematically underestimating the performance drops.

The s42 v2 eval failed, leaving only the old eval's MMLU data which used the wrong evaluate.py version. But the task claims all results are complete, so I need to check if there are additional experiments or if the failed v2 has partial results that might indicate a v3 attempt. Let me pull the full details on that failed v2 run to see what happened.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "ab9f8c2e-092c-4cfd-b930-fb9cd5638710",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011DxAdki1DEsrkRq2pgiqZ4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22353,
      "cache_read_input_tokens": 50851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22353
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

需要查看 s42 v2 失败实验的详细信息，以及是否有后续重跑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "0ceb8521-4551-4de8-8a22-3287809778bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011DxAdki1DEsrkRq2pgiqZ4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22353,
      "cache_read_input_tokens": 50851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22353
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01TSrbKQJDniT4ghsZzns4dY`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "filters": {
    "status": "DONE",
    "conclusion": "failed"
  },
  "fields": [
    "exp_id",
    "title",
    "metrics",
    "conclusion",
    "notes"
  ],
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "d2327009-36c5-47d7-932b-44f63aa31409",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011DxAdki1DEsrkRq2pgiqZ4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22353,
      "cache_read_input_tokens": 50851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22353
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

_source line 21 · 2026-05-21T00:19:10.667Z_

<details><summary>↩ Tool result · `toolu_01TSrbKQJDniT4ghsZzns4dY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"gsm8k_gemma2_s42_westd\": {\"conclusion\": \"failed\", \"notes\": \"D175 最终排除确认: d000_fixed=11.22%, d100_fixed=3.94% (52/1319, 几乎全 pred:null)。SFT 灾难性遗忘, 非 format bug。GSM8K 跨基准分析正式改为 4/5 家族。cuda:3 已释放。\"}, \"sft_gemma2_s123_sweep\": {\"conclusion\": \"failed\"}, \"sft_qwen14b_s123_sweep\": {\"conclusion\": \"failed\"}, \"eval_qwen7b_s42_cqa1_v2\": {\"conclusion\": \"failed\"}, \"eval_qwen7b_s123_cqa1\": {\"conclusion\": \"failed\", \"metrics\": {\"arc_d000\": 0.8968, \"arc_d005\": 0.901, \"arc_d025\": 0.901, \"arc_d050\": 0.8985, \"arc_d100\": 0.8968, \"arc_delta_d100_d000\": 0, \"mmlu_d000\": 0.6974, \"mmlu_d005\": 0.6941, \"mmlu_d025\": 0.7025, \"mmlu_d050\": 0.704, \"mmlu_d100\": 0.7066, \"mmlu_delta_d100_d000\": 0.0092}, \"notes\": \"INVALIDATED: used old evaluate.py (35855 bytes, mc_suffix in user turn) vs westd new version (37591 bytes, mc_suffix in assistant turn). Results unreliable. Replaced by eval_qwen7b_s123_cqa1_v2.\"}, \"eval_phi4_mmlu_arc_westd\": {\"conclusion\": \"failed\"}, \"eval_14b_mmlu_arc_westd\": {\"conclusion\": \"failed\"}, \"eval_7b_batch1_westd\": {\"conclusion\": \"failed\"}, \"exp_006_j16_theta_extraction\": {\"conclusion\": \"failed\", \"notes\": \"Diagnosed: SeetaCloud container force-killed during pooled MCMC sampling (EPERM on all 4 chains simultaneously at 21:35:42). Infrastructure issue, not code bug. --skip-pooled flag was not effective (pooled fit ran anyway). Domain-level fits completed before crash. Does not affect paper - supplementary data only, paper uses v5 cross-family results.\"}, \"exp_006_cross_family_irt_j16\": {\"conclusion\": \"failed\", \"metrics\": {\"PPP_Medical\": 0.827, \"PPP_STEM_CS_Eng\": 0.893, \"PPP_acceptable_only\": \"STEM_CS_Eng (0.893), Medical (0.827)\", \"PPP_warning\": \"6/8 domains PPP>0.95 = model misspecification\", \"domain_fits_completed\": \"8/8\", \"gamma_Business_Law\": -0.239, \"gamma_Humanities\": -0.947, \"gamma_Medical\": 0.218, \"gamma_Other\": -0.88, \"gamma_STEM_CS_Eng\": 0.362, \"gamma_STEM_Math\": -0.386, \"gamma_STEM_Science\": 0.042, \"gamma_Social_Sciences\": -1.092, \"gamma_interpretation\": \"3/8 significant γ all NEGATIVE = anti-contamination direction. Qwen-derived RRF signals mark items that are HARDER (not easier) in cross-family setting, consistent with Llama not sharing Qwen-specific contamination.\", \"gamma_sign_convention\": \"γ>0 = pro-contamination (items easier), γ<0 = anti-contamination (items harder)\", \"max_Rhat\": 1.01, \"min_ESS\": 1331, \"pooled_fit\": \"failed (container security policy)\", \"significant_gamma_domains\": 3, \"theta_by_model\": \"NOT SAVED - needs script modification\", \"total_divergences\": 0}}, \"exp_002_signals_3B_d000_s123_cuda2\": {\"conclusion\": \"failed\"}, \"exp_006_theta_extraction_j13\": {\"conclusion\": \"failed\"}, \"exp_002_signals_llama32_3B_d025_mmlu_arc_gsm8k\": {\"conclusion\": \"failed\"}, \"exp_004_fisher_heatmap_w4\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: OSError [Errno 28] No space left on device — 写 /root/autodl-tmp/exp006/fisher_info_heatmap/arc_N16.json 时磁盘满 | 已有成果: arc_N16 完成 160/200 reps, mmlu/gsm8k 可能已完成 | 建议: 清磁盘后重跑，重跑时可跳过已完成的 condition\"}, \"exp_002_signals_llama32_3B_d000_gsm8k\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: HuggingFace Hub 连接超时 (sentence-transformers/all-MiniLM-L6-v2 下载失败) | 已有成果: 无 | 建议: 先缓存 all-MiniLM-L6-v2 模型到本地再重跑\"}, \"exp_002_signals_15B_instruct_gsm8k\": {\"conclusion\": \"failed\"}, \"exp_006_mmlu_domain_gamma_n24_v3\": {\"conclusion\": \"failed\", \"metrics\": {\"Humanities\": {\"CI\": [-0.776, -0.041], \"N\": 21, \"PPP\": 1, \"converged\": \"borderline_rhat_1.014\", \"excludes_zero\": true, \"gamma_mean\": -0.407}, \"Medical\": {\"CI\": [-0.338, -0.06], \"N\": 24, \"PPP\": 1, \"converged\": true, \"excludes_zero\": true, \"gamma_mean\": -0.199}, \"STEM_CS_Eng\": {\"CI\": [-0.448, 0.835], \"N\": 23, \"PPP\": 0.892, \"converged\": true, \"excludes_zero\": false, \"gamma_mean\": 0.197}, \"STEM_Math\": {\"CI\": [0.527, 1.43], \"N\": 23, \"PPP\": 0.438, \"converged\": true, \"excludes_zero\": true, \"gamma_mean\": 0.969}, \"STEM_Science\": {\"CI\": [0.385, 1.274], \"N\": 23, \"PPP\": 0.807, \"converged\": true, \"excludes_zero\": true, \"gamma_mean\": 0.838}, \"completed_domains\": 5, \"crashed\": \"Social_Sciences (CmdStan retcode=[1,0,0,1])\", \"not_run\": [\"Business_Law\", \"Other\"], \"total_domains\": 8}}, \"exp_006_mmlu_domain_gamma_n24_v2\": {\"conclusion\": \"failed\"}, \"exp_001_eval_3B_instruct_aligned_para\": {\"conclusion\": \"failed\"}, \"exp_008_instruct_rl_proxy\": {\"conclusion\": \"failed\", \"metrics\": {\"base_pretrained_signals\": \"computing_PID_701898_GPU5\", \"comparison\": {\"arc\": {\"d000_sft_s2\": 1.7079, \"d000_sft_s4\": -0.9538, \"instruct_s2\": 1.6737, \"instruct_s4\": -0.9227, \"s4_delta_instruct_vs_sft\": 0.0311}, \"gsm8k\": {\"d000_sft_s2\": 1.6532, \"d000_sft_s4\": -0.9408, \"instruct_s2\": 1.7073, \"instruct_s4\": -0.9632, \"s4_delta_instruct_vs_sft\": -0.0224}, \"mmlu\": {\"base_s2\": 1.7009, \"base_s4\": \"computing\", \"d000_sft_s2\": 1.6976, \"d000_sft_s4\": -0.9557, \"instruct_s2\": 1.6952, \"instruct_s4\": -0.8782, \"s4_delta_instruct_vs_sft\": 0.0775}}, \"d000_sft_signals_complete\": true, \"instruct_signals_complete\": true, \"key_finding\": \"S4 differentiates regimes (MMLU +0.078, ARC +0.031 Instruct vs SFT); S2 does not (<0.01 difference). RL increases S4 entropy on knowledge benchmarks.\", \"signal_paths\": {\"base_pretrained\": \"/root/autodl-tmp/exp008/signals/base_pretrained/\", \"d000_sft\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/\", \"instruct\": \"/root/autodl-tmp/exp008/signals/rl_aligned/\"}}}, \"exp_002_signals_3B_v9\": {\"conclusion\": \"failed\", \"notes\": \"Wrapper PID 668217 exited (no exit code). d025_s123 mmlu s4 COMPLETE (14042 items, merged). d100_a32_s123 mmlu s4 IN PROGRESS via orphan PID 689315 on cuda:4 (2/15 chunks at 11:49). d100_a32_s123 gsm8k/arc NOT STARTED — wrapper dead, won't auto-continue. Need new submission for gsm8k+arc after 689315 finishes.\"}, \"exp_002_signals_05B_s123_batch\": {\"conclusion\": \"failed\"}, \"exp_002_signals_3B_v8_recovery\": {\"conclusion\": \"failed\"}, \"exp_002_signals_3B_v8\": {\"conclusion\": \"failed\", \"notes\": \"Process Killed (OOM) during s4_selfcritique mmlu. Partial completion: d025_s123 gsm8k+arc_challenge complete (s1,s2,s4,merged); d025_s123 mmlu has s1+s2 only (s4 killed at 388/7021); d100_a32_s123 mmlu has s1+s2 only (s4 stopped at 203/7021); d100_a32_s123 gsm8k+arc_challenge not started. New PID 662616 running d100_a32_s123/mmlu on cuda:4 as recovery.\"}, \"exp_002_signals_3B_v5\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: EXIT_CODE=129 (SIGHUP), 实际是 d100_s42/mmlu selfcritique 在 22% 处被 SIGTERM (D078/D079 orphan 清理). 3/4 batch tasks 完成 (d025_s42/mmlu PASS, d100_s42/gsm8k PASS, d100_s42/arc_challenge PASS). 已有成果: d025_s42 和 d100_s42 的 gsm8k+arc signals 已写盘, 但这些 signals 基于旧 alpha=16 checkpoint, D076 重训 alpha=32 后需全部重算, 无需单独 retry. 建议: 等 cuda:1 d100_s42_v3 + cuda:5 d000_s42 重训完成后, 用新 checkpoint 统一重算 3B s42 signals.\"}, \"exp_001_sft_3B_d025_s42_a32_v2\": {\"conclusion\": \"failed\", \"notes\": \"SIGTERM at step 22/3384 (~1.5min training). Training was healthy (no OOM/NaN/error, 4.3s/step pace). bitsandbytes libnvJitLink warning non-fatal. External kill matches D083 pattern. LoRA config confirmed: r=16, alpha=32, lr=5e-5. Need v3 resubmit on cuda:3.\"}, \"exp_001_sft_3B_d100_s42_a32_v2\": {\"conclusion\": \"failed\", \"notes\": \"D083 SIGTERM root cause: Worker agent itself sent SIGTERM via ssh_execute (not OOM/cron/manual). v1 had no CUDA_VISIBLE_DEVICES, landed on occupied GPU 0, Worker detected conflict and killed. v2 killed at 72% progress (step 3030/4159, ~3.5h GPU time lost) without checkpoint save. v3 fixed with explicit CUDA_VISIBLE_DEVICES=2. ssh_execute kill commands don't appear in bash_history, making post-mortem difficult.\"}, \"exp_002_signals_3B_v6\": {\"conclusion\": \"failed\", \"notes\": \"s1_embedding and s2_minkpp completed for all 3 benchmarks (mmlu: 14042, gsm8k: 1319, arc_challenge: 1172). s3_constat crashed on all benchmarks with ValueError: Item count mismatch (expected 1172, got 697 on arc). s4_selfcritique never ran. 6 signal files saved to /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_v2_s42/. Bug is in s3_constat.py:50.\"}, \"exp_002_signals_3B_v4\": {\"conclusion\": \"failed\", \"notes\": \"诊断(2026-05-15): run_batch.py --signal 参数 bug 导致 11/12 combo rc=2 失败, d000/mmlu 被 SIGTERM (rc=-15)。Batch 0/12 passed。但有 5/12 combo 已有 merged 文件(d000/{gsm8k,arc}, d005/arc, d025/{gsm8k,arc})，来自早期或独立进程。v4 tmux session 确认死亡。多个 orphan 进程仍在 GPU 2/3/4 上跑 mmlu combos，有输出目录冲突风险。\"}, \"exp_001_eval_3B_d100_s123_para_aligned\": {\"conclusion\": \"failed\"}, \"exp_001_sft_3B_d000_v3\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: 进程在 step 1725/3125 (55%) 静默死亡，无 Traceback/OOM/CUDA error。cuda:4 双进程共存（SFT + signals ~20.7/24.5GB），高度疑似系统 OOM kill。| 诊断 Worker: worker_diagnose_exp_001_sft_3B_d000_v3_20260515T190929 | 建议: 诊断完成后单独使用 cuda:4 重跑\"}, \"exp_002_signals_3B\": {\"conclusion\": \"failed\"}, \"exp_008_base_pretrained_eval\": {\"conclusion\": \"failed\"}, \"exp_001_sft_15B_d005_s123\": {\"conclusion\": \"failed\"}, \"exp_001_eval_05B_d000_s42_v7\": {\"conclusion\": \"failed\"}, \"exp_004_sim_sweep_v5\": {\"conclusion\": \"failed\", \"metrics\": {\"conditions_all_failed\": [\"auc0.65_n20 (0/10)\", \"auc0.65_n50 (0/7)\"], \"conditions_complete\": 4, \"conditions_fully_ok\": [\"auc0.55_n20 (10/10)\", \"auc0.55_n50 (10/10)\", \"auc0.8_n20 (10/10)\", \"auc0.8_n50 (10/10)\"], \"conditions_missing\": 3, \"conditions_never_started\": [\"auc0.65_n100\", \"auc0.9_n50\", \"auc0.9_n100\"], \"conditions_partial\": 5, \"conditions_partial_ok\": [\"auc0.55_n100 (7/10)\", \"auc0.8_n100 (6/10)\", \"auc0.9_n20 (6/10)\"], \"failure_cause\": \"Disk quota exceeded ([Errno 122]) - root partition /tmp filled by CmdStan temp files\", \"seeds_attempted\": 97, \"seeds_ok\": 59, \"seeds_total\": 120}}, \"exp006-oracle-arc-4pl-pooled\": {\"conclusion\": \"failed\"}, \"exp_001_eval_05B_d000_s42\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: 所有 4 benchmarks 评估完成（HumanEval pass@1=0.1098），但保存 eval_results.json 时 FileNotFoundError——output_dir 未创建。ARC 下载有 HF 连接超时（未 source network_turbo）但评估仍完成。同命令 s123 实验成功。fix_worker_id: worker_fix_eval_05B_d000_s42_v2_20260514T013245 | 建议: 修复 evaluate.py 中保存前的 os.makedirs 调用后重跑\"}, \"exp_004_sim_sweep_v4\": {\"conclusion\": \"failed\"}, \"exp_001_eval_3B_d000_v2_para_aligned_v3\": {\"conclusion\": \"failed\"}, \"exp006-oracle-gsm8k-extended\": {\"conclusion\": \"failed\"}, \"exp006-pooled-s1only-gsm8k\": {\"conclusion\": \"failed\"}, \"exp_004_sim_sweep_v3\": {\"conclusion\": \"failed\", \"notes\": \"v2 PID 599562 was still alive (erroneously marked failed). v1 serial PID 559606 was also running on same results dir — killed to prevent write conflicts. v3 = same process as v2, just corrected registry. 2 CPU / 7.6GB RAM machine, parallel=2 chains_parallel=2. ETA ~20-30h for remaining 66 runs.\"}, \"exp_001_eval_3B_d100_v2_aligned\": {\"conclusion\": \"failed\", \"metrics\": {\"INVALID\": \"metrics were from v1 exp_001_eval_3B_d100_aligned, not v2. v2 output dir was empty. PID 461879 died before completion.\"}, \"notes\": \"DATA INTEGRITY ISSUE (D036): Metrics erroneously copied from v1 (exp_001_eval_3B_d100_aligned). Worker found v1 results at similar path, mistook for v2. v2 output dir was empty (eval still running), then deleted during cleanup. PID 461879 killed/died. Must re-run as v3.\"}, \"exp_001_sft_d025_3B\": {\"conclusion\": \"failed\", \"notes\": \"GPU 3 空转: 注册 RUNNING 但进程从未启动 (nvidia-smi 确认 0% util, 0 MiB). Director 指令标 FAILED.\"}, \"exp006-pooled-05B-15B-mmlu-v2\": {\"conclusion\": \"failed\", \"metrics\": {\"NOTE\": \"fit completely failed, not reportable\", \"convergence\": \"FAILED (rhat=1.54, ess=7)\", \"coverage_95\": 1, \"exposure_source\": \"signal_rrf\", \"gamma_joint\": -0.2095, \"gamma_joint_ci\": [-1.01, 0.59], \"gamma_perbench\": -3.8073, \"gamma_perbench_ci\": [-7.02, 3.22], \"mae\": 0.099, \"n_models\": 8, \"ppp\": 0.75}}, \"exp_005_noise_prop\": {\"conclusion\": \"failed\", \"notes\": \"v1 original run, failed due to /tmp disk exhaustion. Superseded by v2→v3→v4. See v4 for active tracking (PID 559667, 23/25 fits).\"}, \"exp_004_sim_sweep\": {\"conclusion\": \"failed\", \"notes\": \"v1 original serial run. Superseded by v2 (parallel=2). PID 559606 killed to prevent write conflicts with v2. See v3 for active tracking.\"}, \"exp_004_sim_sweep_v2\": {\"conclusion\": \"failed\", \"metrics\": {\"auc080_n100_bias\": 0.008, \"auc080_n100_ci_width\": 0.116, \"auc080_n100_gamma_hat\": 0.508, \"auc080_n100_theta_corr\": 0.962, \"auc080_n50_bias\": 0.006, \"auc080_n50_ci95_coverage\": 1, \"auc080_n50_rmse\": 0.03, \"ci_width_ratio_n100\": 1.81, \"core_findings_stable\": true, \"runs_completed\": 48, \"runs_total\": 120}, \"notes\": \"v2 was erroneously marked failed; PID 599562 was still running. Killed conflicting v1 (PID 559606). Continuing as v3 registry entry.\"}, \"exp_005_noise_prop_v3\": {\"conclusion\": \"failed\", \"notes\": \"PID 559666 crashed (~10h ago). 22/25 fits completed. Restarting as v4.\"}}, \"count\": 50, \"total\": 64, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9136}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "8dd8641b-f068-4781-9d7e-9fa6d56020d8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"gsm8k_gemma2_s42_westd\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"D175 最终排除确认: d000_fixed=11.22%, d100_fixed=3.94% (52/1319, 几乎全 pred:null)。SFT 灾难性遗忘, 非 format bug。GSM8K 跨基准分析正式改为 4/5 家族。cuda:3 已释放。\\\"}, \\\"sft_gemma2_s123_sweep\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"sft_qwen14b_s123_sweep\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_qwen7b_s42_cqa1_v2\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_qwen7b_s123_cqa1\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"metrics\\\": {\\\"arc_d000\\\": 0.8968, \\\"arc_d005\\\": 0.901, \\\"arc_d025\\\": 0.901, \\\"arc_d050\\\": 0.8985, \\\"arc_d100\\\": 0.8968, \\\"arc_delta_d100_d000\\\": 0, \\\"mmlu_d000\\\": 0.6974, \\\"mmlu_d005\\\": 0.6941, \\\"mmlu_d025\\\": 0.7025, \\\"mmlu_d050\\\": 0.704, \\\"mmlu_d100\\\": 0.7066, \\\"mmlu_delta_d100_d000\\\": 0.0092}, \\\"notes\\\": \\\"INVALIDATED: used old evaluate.py (35855 bytes, mc_suffix in user turn) vs westd new version (37591 bytes, mc_suffix in assistant turn). Results unreliable. Replaced by eval_qwen7b_s123_cqa1_v2.\\\"}, \\\"eval_phi4_mmlu_arc_westd\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_14b_mmlu_arc_westd\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_7b_batch1_westd\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_006_j16_theta_extraction\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"Diagnosed: SeetaCloud container force-killed during pooled MCMC sampling (EPERM on all 4 chains simultaneously at 21:35:42). Infrastructure issue, not code bug. --skip-pooled flag was not effective (pooled fit ran anyway). Domain-level fits completed before crash. Does not affect paper - supplementary data only, paper uses v5 cross-family results.\\\"}, \\\"exp_006_cross_family_irt_j16\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"metrics\\\": {\\\"PPP_Medical\\\": 0.827, \\\"PPP_STEM_CS_Eng\\\": 0.893, \\\"PPP_acceptable_only\\\": \\\"STEM_CS_Eng (0.893), Medical (0.827)\\\", \\\"PPP_warning\\\": \\\"6/8 domains PPP>0.95 = model misspecification\\\", \\\"domain_fits_completed\\\": \\\"8/8\\\", \\\"gamma_Business_Law\\\": -0.239, \\\"gamma_Humanities\\\": -0.947, \\\"gamma_Medical\\\": 0.218, \\\"gamma_Other\\\": -0.88, \\\"gamma_STEM_CS_Eng\\\": 0.362, \\\"gamma_STEM_Math\\\": -0.386, \\\"gamma_STEM_Science\\\": 0.042, \\\"gamma_Social_Sciences\\\": -1.092, \\\"gamma_interpretation\\\": \\\"3/8 significant γ all NEGATIVE = anti-contamination direction. Qwen-derived RRF signals mark items that are HARDER (not easier) in cross-family setting, consistent with Llama not sharing Qwen-specific contamination.\\\", \\\"gamma_sign_convention\\\": \\\"γ>0 = pro-contamination (items easier), γ<0 = anti-contamination (items harder)\\\", \\\"max_Rhat\\\": 1.01, \\\"min_ESS\\\": 1331, \\\"pooled_fit\\\": \\\"failed (container security policy)\\\", \\\"significant_gamma_domains\\\": 3, \\\"theta_by_model\\\": \\\"NOT SAVED - needs script modification\\\", \\\"total_divergences\\\": 0}}, \\\"exp_002_signals_3B_d000_s123_cuda2\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_006_theta_extraction_j13\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_002_signals_llama32_3B_d025_mmlu_arc_gsm8k\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_004_fisher_heatmap_w4\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"失败原因: OSError [Errno 28] No space left on device — 写 /root/autodl-tmp/exp006/fisher_info_heatmap/arc_N16.json 时磁盘满 | 已有成果: arc_N16 完成 160/200 reps, mmlu/gsm8k 可能已完成 | 建议: 清磁盘后重跑，重跑时可跳过已完成的 condition\\\"}, \\\"exp_002_signals_llama32_3B_d000_gsm8k\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"失败原因: HuggingFace Hub 连接超时 (sentence-transformers/all-MiniLM-L6-v2 下载失败) | 已有成果: 无 | 建议: 先缓存 all-MiniLM-L6-v2 模型到本地再重跑\\\"}, \\\"exp_002_signals_15B_instruct_gsm8k\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_006_mmlu_domain_gamma_n24_v3\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"metrics\\\": {\\\"Humanities\\\": {\\\"CI\\\": [-0.776, -0.041], \\\"N\\\": 21, \\\"PPP\\\": 1, \\\"converged\\\": \\\"borderline_rhat_1.014\\\", \\\"excludes_zero\\\": true, \\\"gamma_mean\\\": -0.407}, \\\"Medical\\\": {\\\"CI\\\": [-0.338, -0.06], \\\"N\\\": 24, \\\"PPP\\\": 1, \\\"converged\\\": true, \\\"excludes_zero\\\": true, \\\"gamma_mean\\\": -0.199}, \\\"STEM_CS_Eng\\\": {\\\"CI\\\": [-0.448, 0.835], \\\"N\\\": 23, \\\"PPP\\\": 0.892, \\\"converged\\\": true, \\\"excludes_zero\\\": false, \\\"gamma_mean\\\": 0.197}, \\\"STEM_Math\\\": {\\\"CI\\\": [0.527, 1.43], \\\"N\\\": 23, \\\"PPP\\\": 0.438, \\\"converged\\\": true, \\\"excludes_zero\\\": true, \\\"gamma_mean\\\": 0.969}, \\\"STEM_Science\\\": {\\\"CI\\\": [0.385, 1.274], \\\"N\\\": 23, \\\"PPP\\\": 0.807, \\\"converged\\\": true, \\\"excludes_zero\\\": true, \\\"gamma_mean\\\": 0.838}, \\\"completed_domains\\\": 5, \\\"crashed\\\": \\\"Social_Sciences (CmdStan retcode=[1,0,0,1])\\\", \\\"not_run\\\": [\\\"Business_Law\\\", \\\"Other\\\"], \\\"total_domains\\\": 8}}, \\\"exp_006_mmlu_domain_gamma_n24_v2\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_001_eval_3B_instruct_aligned_para\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_008_instruct_rl_proxy\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"metrics\\\": {\\\"base_pretrained_signals\\\": \\\"computing_PID_701898_GPU5\\\", \\\"comparison\\\": {\\\"arc\\\": {\\\"d000_sft_s2\\\": 1.7079, \\\"d000_sft_s4\\\": -0.9538, \\\"instruct_s2\\\": 1.6737, \\\"instruct_s4\\\": -0.9227, \\\"s4_delta_instruct_vs_sft\\\": 0.0311}, \\\"gsm8k\\\": {\\\"d000_sft_s2\\\": 1.6532, \\\"d000_sft_s4\\\": -0.9408, \\\"instruct_s2\\\": 1.7073, \\\"instruct_s4\\\": -0.9632, \\\"s4_delta_instruct_vs_sft\\\": -0.0224}, \\\"mmlu\\\": {\\\"base_s2\\\": 1.7009, \\\"base_s4\\\": \\\"computing\\\", \\\"d000_sft_s2\\\": 1.6976, \\\"d000_sft_s4\\\": -0.9557, \\\"instruct_s2\\\": 1.6952, \\\"instruct_s4\\\": -0.8782, \\\"s4_delta_instruct_vs_sft\\\": 0.0775}}, \\\"d000_sft_signals_complete\\\": true, \\\"instruct_signals_complete\\\": true, \\\"key_finding\\\": \\\"S4 differentiates regimes (MMLU +0.078, ARC +0.031 Instruct vs SFT); S2 does not (<0.01 difference). RL increases S4 entropy on knowledge benchmarks.\\\", \\\"signal_paths\\\": {\\\"base_pretrained\\\": \\\"/root/autodl-tmp/exp008/signals/base_pretrained/\\\", \\\"d000_sft\\\": \\\"/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/\\\", \\\"instruct\\\": \\\"/root/autodl-tmp/exp008/signals/rl_aligned/\\\"}}}, \\\"exp_002_signals_3B_v9\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"Wrapper PID 668217 exited (no exit code). d025_s123 mmlu s4 COMPLETE (14042 items, merged). d100_a32_s123 mmlu s4 IN PROGRESS via orphan PID 689315 on cuda:4 (2/15 chunks at 11:49). d100_a32_s123 gsm8k/arc NOT STARTED — wrapper dead, won't auto-continue. Need new submission for gsm8k+arc after 689315 finishes.\\\"}, \\\"exp_002_signals_05B_s123_batch\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_002_signals_3B_v8_recovery\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_002_signals_3B_v8\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"Process Killed (OOM) during s4_selfcritique mmlu. Partial completion: d025_s123 gsm8k+arc_challenge complete (s1,s2,s4,merged); d025_s123 mmlu has s1+s2 only (s4 killed at 388/7021); d100_a32_s123 mmlu has s1+s2 only (s4 stopped at 203/7021); d100_a32_s123 gsm8k+arc_challenge not started. New PID 662616 running d100_a32_s123/mmlu on cuda:4 as recovery.\\\"}, \\\"exp_002_signals_3B_v5\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"失败原因: EXIT_CODE=129 (SIGHUP), 实际是 d100_s42/mmlu selfcritique 在 22% 处被 SIGTERM (D078/D079 orphan 清理). 3/4 batch tasks 完成 (d025_s42/mmlu PASS, d100_s42/gsm8k PASS, d100_s42/arc_challenge PASS). 已有成果: d025_s42 和 d100_s42 的 gsm8k+arc signals 已写盘, 但这些 signals 基于旧 alpha=16 checkpoint, D076 重训 alpha=32 后需全部重算, 无需单独 retry. 建议: 等 cuda:1 d100_s42_v3 + cuda:5 d000_s42 重训完成后, 用新 checkpoint 统一重算 3B s42 signals.\\\"}, \\\"exp_001_sft_3B_d025_s42_a32_v2\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"SIGTERM at step 22/3384 (~1.5min training). Training was healthy (no OOM/NaN/error, 4.3s/step pace). bitsandbytes libnvJitLink warning non-fatal. External kill matches D083 pattern. LoRA config confirmed: r=16, alpha=32, lr=5e-5. Need v3 resubmit on cuda:3.\\\"}, \\\"exp_001_sft_3B_d100_s42_a32_v2\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"D083 SIGTERM root cause: Worker agent itself sent SIGTERM via ssh_execute (not OOM/cron/manual). v1 had no CUDA_VISIBLE_DEVICES, landed on occupied GPU 0, Worker detected conflict and killed. v2 killed at 72% progress (step 3030/4159, ~3.5h GPU time lost) without checkpoint save. v3 fixed with explicit CUDA_VISIBLE_DEVICES=2. ssh_execute kill commands don't appear in bash_history, making post-mortem difficult.\\\"}, \\\"exp_002_signals_3B_v6\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"s1_embedding and s2_minkpp completed for all 3 benchmarks (mmlu: 14042, gsm8k: 1319, arc_challenge: 1172). s3_constat crashed on all benchmarks with ValueError: Item count mismatch (expected 1172, got 697 on arc). s4_selfcritique never ran. 6 signal files saved to /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_v2_s42/. Bug is in s3_constat.py:50.\\\"}, \\\"exp_002_signals_3B_v4\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"诊断(2026-05-15): run_batch.py --signal 参数 bug 导致 11/12 combo rc=2 失败, d000/mmlu 被 SIGTERM (rc=-15)。Batch 0/12 passed。但有 5/12 combo 已有 merged 文件(d000/{gsm8k,arc}, d005/arc, d025/{gsm8k,arc})，来自早期或独立进程。v4 tmux session 确认死亡。多个 orphan 进程仍在 GPU 2/3/4 上跑 mmlu combos，有输出目录冲突风险。\\\"}, \\\"exp_001_eval_3B_d100_s123_para_aligned\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_001_sft_3B_d000_v3\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"失败原因: 进程在 step 1725/3125 (55%) 静默死亡，无 Traceback/OOM/CUDA error。cuda:4 双进程共存（SFT + signals ~20.7/24.5GB），高度疑似系统 OOM kill。| 诊断 Worker: worker_diagnose_exp_001_sft_3B_d000_v3_20260515T190929 | 建议: 诊断完成后单独使用 cuda:4 重跑\\\"}, \\\"exp_002_signals_3B\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_008_base_pretrained_eval\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_001_sft_15B_d005_s123\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_001_eval_05B_d000_s42_v7\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_004_sim_sweep_v5\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"metrics\\\": {\\\"conditions_all_failed\\\": [\\\"auc0.65_n20 (0/10)\\\", \\\"auc0.65_n50 (0/7)\\\"], \\\"conditions_complete\\\": 4, \\\"conditions_fully_ok\\\": [\\\"auc0.55_n20 (10/10)\\\", \\\"auc0.55_n50 (10/10)\\\", \\\"auc0.8_n20 (10/10)\\\", \\\"auc0.8_n50 (10/10)\\\"], \\\"conditions_missing\\\": 3, \\\"conditions_never_started\\\": [\\\"auc0.65_n100\\\", \\\"auc0.9_n50\\\", \\\"auc0.9_n100\\\"], \\\"conditions_partial\\\": 5, \\\"conditions_partial_ok\\\": [\\\"auc0.55_n100 (7/10)\\\", \\\"auc0.8_n100 (6/10)\\\", \\\"auc0.9_n20 (6/10)\\\"], \\\"failure_cause\\\": \\\"Disk quota exceeded ([Errno 122]) - root partition /tmp filled by CmdStan temp files\\\", \\\"seeds_attempted\\\": 97, \\\"seeds_ok\\\": 59, \\\"seeds_total\\\": 120}}, \\\"exp006-oracle-arc-4pl-pooled\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_001_eval_05B_d000_s42\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"失败原因: 所有 4 benchmarks 评估完成（HumanEval pass@1=0.1098），但保存 eval_results.json 时 FileNotFoundError——output_dir 未创建。ARC 下载有 HF 连接超时（未 source network_turbo）但评估仍完成。同命令 s123 实验成功。fix_worker_id: worker_fix_eval_05B_d000_s42_v2_20260514T013245 | 建议: 修复 evaluate.py 中保存前的 os.makedirs 调用后重跑\\\"}, \\\"exp_004_sim_sweep_v4\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_001_eval_3B_d000_v2_para_aligned_v3\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp006-oracle-gsm8k-extended\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp006-pooled-s1only-gsm8k\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_004_sim_sweep_v3\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"v2 PID 599562 was still alive (erroneously marked failed). v1 serial PID 559606 was also running on same results dir — killed to prevent write conflicts. v3 = same process as v2, just corrected registry. 2 CPU / 7.6GB RAM machine, parallel=2 chains_parallel=2. ETA ~20-30h for remaining 66 runs.\\\"}, \\\"exp_001_eval_3B_d100_v2_aligned\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"metrics\\\": {\\\"INVALID\\\": \\\"metrics were from v1 exp_001_eval_3B_d100_aligned, not v2. v2 output dir was empty. PID 461879 died before completion.\\\"}, \\\"notes\\\": \\\"DATA INTEGRITY ISSUE (D036): Metrics erroneously copied from v1 (exp_001_eval_3B_d100_aligned). Worker found v1 results at similar path, mistook for v2. v2 output dir was empty (eval still running), then deleted during cleanup. PID 461879 killed/died. Must re-run as v3.\\\"}, \\\"exp_001_sft_d025_3B\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"GPU 3 空转: 注册 RUNNING 但进程从未启动 (nvidia-smi 确认 0% util, 0 MiB). Director 指令标 FAILED.\\\"}, \\\"exp006-pooled-05B-15B-mmlu-v2\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"metrics\\\": {\\\"NOTE\\\": \\\"fit completely failed, not reportable\\\", \\\"convergence\\\": \\\"FAILED (rhat=1.54, ess=7)\\\", \\\"coverage_95\\\": 1, \\\"exposure_source\\\": \\\"signal_rrf\\\", \\\"gamma_joint\\\": -0.2095, \\\"gamma_joint_ci\\\": [-1.01, 0.59], \\\"gamma_perbench\\\": -3.8073, \\\"gamma_perbench_ci\\\": [-7.02, 3.22], \\\"mae\\\": 0.099, \\\"n_models\\\": 8, \\\"ppp\\\": 0.75}}, \\\"exp_005_noise_prop\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"v1 original run, failed due to /tmp disk exhaustion. Superseded by v2→v3→v4. See v4 for active tracking (PID 559667, 23/25 fits).\\\"}, \\\"exp_004_sim_sweep\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"v1 original serial run. Superseded by v2 (parallel=2). PID 559606 killed to prevent write conflicts with v2. See v3 for active tracking.\\\"}, \\\"exp_004_sim_sweep_v2\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"metrics\\\": {\\\"auc080_n100_bias\\\": 0.008, \\\"auc080_n100_ci_width\\\": 0.116, \\\"auc080_n100_gamma_hat\\\": 0.508, \\\"auc080_n100_theta_corr\\\": 0.962, \\\"auc080_n50_bias\\\": 0.006, \\\"auc080_n50_ci95_coverage\\\": 1, \\\"auc080_n50_rmse\\\": 0.03, \\\"ci_width_ratio_n100\\\": 1.81, \\\"core_findings_stable\\\": true, \\\"runs_completed\\\": 48, \\\"runs_total\\\": 120}, \\\"notes\\\": \\\"v2 was erroneously marked failed; PID 599562 was still running. Killed conflicting v1 (PID 559606). Continuing as v3 registry entry.\\\"}, \\\"exp_005_noise_prop_v3\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"PID 559666 crashed (~10h ago). 22/25 fits completed. Restarting as v4.\\\"}}, \\\"count\\\": 50, \\\"total\\\": 64, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.9136}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"gsm8k_gemma2_s42_westd\": {\"conclusion\": \"failed\", \"notes\": \"D175 最终排除确认: d000_fixed=11.22%, d100_fixed=3.94% (52/1319, 几乎全 pred:null)。SFT 灾难性遗忘, 非 format bug。GSM8K 跨基准分析正式改为 4/5 家族。cuda:3 已释放。\"}, \"sft_gemma2_s123_sweep\": {\"conclusion\": \"failed\"}, \"sft_qwen14b_s123_sweep\": {\"conclusion\": \"failed\"}, \"eval_qwen7b_s42_cqa1_v2\": {\"conclusion\": \"failed\"}, \"eval_qwen7b_s123_cqa1\": {\"conclusion\": \"failed\", \"metrics\": {\"arc_d000\": 0.8968, \"arc_d005\": 0.901, \"arc_d025\": 0.901, \"arc_d050\": 0.8985, \"arc_d100\": 0.8968, \"arc_delta_d100_d000\": 0, \"mmlu_d000\": 0.6974, \"mmlu_d005\": 0.6941, \"mmlu_d025\": 0.7025, \"mmlu_d050\": 0.704, \"mmlu_d100\": 0.7066, \"mmlu_delta_d100_d000\": 0.0092}, \"notes\": \"INVALIDATED: used old evaluate.py (35855 bytes, mc_suffix in user turn) vs westd new version (37591 bytes, mc_suffix in assistant turn). Results unreliable. Replaced by eval_qwen7b_s123_cqa1_v2.\"}, \"eval_phi4_mmlu_arc_westd\": {\"conclusion\": \"failed\"}, \"eval_14b_mmlu_arc_westd\": {\"conclusion\": \"failed\"}, \"eval_7b_batch1_westd\": {\"conclusion\": \"failed\"}, \"exp_006_j16_theta_extraction\": {\"conclusion\": \"failed\", \"notes\": \"Diagnosed: SeetaCloud container force-killed during pooled MCMC sampling (EPERM on all 4 chains simultaneously at 21:35:42). Infrastructure issue, not code bug. --skip-pooled flag was not effective (pooled fit ran anyway). Domain-level fits completed before crash. Does not affect paper - supplementary data only, paper uses v5 cross-family results.\"}, \"exp_006_cross_family_irt_j16\": {\"conclusion\": \"failed\", \"metrics\": {\"PPP_Medical\": 0.827, \"PPP_STEM_CS_Eng\": 0.893, \"PPP_acceptable_only\": \"STEM_CS_Eng (0.893), Medical (0.827)\", \"PPP_warning\": \"6/8 domains PPP>0.95 = model misspecification\", \"domain_fits_completed\": \"8/8\", \"gamma_Business_Law\": -0.239, \"gamma_Humanities\": -0.947, \"gamma_Medical\": 0.218, \"gamma_Other\": -0.88, \"gamma_STEM_CS_Eng\": 0.362, \"gamma_STEM_Math\": -0.386, \"gamma_STEM_Science\": 0.042, \"gamma_Social_Sciences\": -1.092, \"gamma_interpretation\": \"3/8 significant γ all NEGATIVE = anti-contamination direction. Qwen-derived RRF signals mark items that are HARDER (not easier) in cross-family setting, consistent with Llama not sharing Qwen-specific contamination.\", \"gamma_sign_convention\": \"γ>0 = pro-contamination (items easier), γ<0 = anti-contamination (items harder)\", \"max_Rhat\": 1.01, \"min_ESS\": 1331, \"pooled_fit\": \"failed (container security policy)\", \"significant_gamma_domains\": 3, \"theta_by_model\": \"NOT SAVED - needs script modification\", \"total_divergences\": 0}}, \"exp_002_signals_3B_d000_s123_cuda2\": {\"conclusion\": \"failed\"}, \"exp_006_theta_extraction_j13\": {\"conclusion\": \"failed\"}, \"exp_002_signals_llama32_3B_d025_mmlu_arc_gsm8k\": {\"conclusion\": \"failed\"}, \"exp_004_fisher_heatmap_w4\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: OSError [Errno 28] No space left on device — 写 /root/autodl-tmp/exp006/fisher_info_heatmap/arc_N16.json 时磁盘满 | 已有成果: arc_N16 完成 160/200 reps, mmlu/gsm8k 可能已完成 | 建议: 清磁盘后重跑，重跑时可跳过已完成的 condition\"}, \"exp_002_signals_llama32_3B_d000_gsm8k\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: HuggingFace Hub 连接超时 (sentence-transformers/all-MiniLM-L6-v2 下载失败) | 已有成果: 无 | 建议: 先缓存 all-MiniLM-L6-v2 模型到本地再重跑\"}, \"exp_002_signals_15B_instruct_gsm8k\": {\"conclusion\": \"failed\"}, \"exp_006_mmlu_domain_gamma_n24_v3\": {\"conclusion\": \"failed\", \"metrics\": {\"Humanities\": {\"CI\": [-0.776, -0.041], \"N\": 21, \"PPP\": 1, \"converged\": \"borderline_rhat_1.014\", \"excludes_zero\": true, \"gamma_mean\": -0.407}, \"Medical\": {\"CI\": [-0.338, -0.06], \"N\": 24, \"PPP\": 1, \"converged\": true, \"excludes_zero\": true, \"gamma_mean\": -0.199}, \"STEM_CS_Eng\": {\"CI\": [-0.448, 0.835], \"N\": 23, \"PPP\": 0.892, \"converged\": true, \"excludes_zero\": false, \"gamma_mean\": 0.197}, \"STEM_Math\": {\"CI\": [0.527, 1.43], \"N\": 23, \"PPP\": 0.438, \"converged\": true, \"excludes_zero\": true, \"gamma_mean\": 0.969}, \"STEM_Science\": {\"CI\": [0.385, 1.274], \"N\": 23, \"PPP\": 0.807, \"converged\": true, \"excludes_zero\": true, \"gamma_mean\": 0.838}, \"completed_domains\": 5, \"crashed\": \"Social_Sciences (CmdStan retcode=[1,0,0,1])\", \"not_run\": [\"Business_Law\", \"Other\"], \"total_domains\": 8}}, \"exp_006_mmlu_domain_gamma_n24_v2\": {\"conclusion\": \"failed\"}, \"exp_001_eval_3B_instruct_aligned_para\": {\"conclusion\": \"failed\"}, \"exp_008_instruct_rl_proxy\": {\"conclusion\": \"failed\", \"metrics\": {\"base_pretrained_signals\": \"computing_PID_701898_GPU5\", \"comparison\": {\"arc\": {\"d000_sft_s2\": 1.7079, \"d000_sft_s4\": -0.9538, \"instruct_s2\": 1.6737, \"instruct_s4\": -0.9227, \"s4_delta_instruct_vs_sft\": 0.0311}, \"gsm8k\": {\"d000_sft_s2\": 1.6532, \"d000_sft_s4\": -0.9408, \"instruct_s2\": 1.7073, \"instruct_s4\": -0.9632, \"s4_delta_instruct_vs_sft\": -0.0224}, \"mmlu\": {\"base_s2\": 1.7009, \"base_s4\": \"computing\", \"d000_sft_s2\": 1.6976, \"d000_sft_s4\": -0.9557, \"instruct_s2\": 1.6952, \"instruct_s4\": -0.8782, \"s4_delta_instruct_vs_sft\": 0.0775}}, \"d000_sft_signals_complete\": true, \"instruct_signals_complete\": true, \"key_finding\": \"S4 differentiates regimes (MMLU +0.078, ARC +0.031 Instruct vs SFT); S2 does not (<0.01 difference). RL increases S4 entropy on knowledge benchmarks.\", \"signal_paths\": {\"base_pretrained\": \"/root/autodl-tmp/exp008/signals/base_pretrained/\", \"d000_sft\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/\", \"instruct\": \"/root/autodl-tmp/exp008/signals/rl_aligned/\"}}}, \"exp_002_signals_3B_v9\": {\"conclusion\": \"failed\", \"notes\": \"Wrapper PID 668217 exited (no exit code). d025_s123 mmlu s4 COMPLETE (14042 items, merged). d100_a32_s123 mmlu s4 IN PROGRESS via orphan PID 689315 on cuda:4 (2/15 chunks at 11:49). d100_a32_s123 gsm8k/arc NOT STARTED — wrapper dead, won't auto-continue. Need new submission for gsm8k+arc after 689315 finishes.\"}, \"exp_002_signals_05B_s123_batch\": {\"conclusion\": \"failed\"}, \"exp_002_signals_3B_v8_recovery\": {\"conclusion\": \"failed\"}, \"exp_002_signals_3B_v8\": {\"conclusion\": \"failed\", \"notes\": \"Process Killed (OOM) during s4_selfcritique mmlu. Partial completion: d025_s123 gsm8k+arc_challenge complete (s1,s2,s4,merged); d025_s123 mmlu has s1+s2 only (s4 killed at 388/7021); d100_a32_s123 mmlu has s1+s2 only (s4 stopped at 203/7021); d100_a32_s123 gsm8k+arc_challenge not started. New PID 662616 running d100_a32_s123/mmlu on cuda:4 as recovery.\"}, \"exp_002_signals_3B_v5\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: EXIT_CODE=129 (SIGHUP), 实际是 d100_s42/mmlu selfcritique 在 22% 处被 SIGTERM (D078/D079 orphan 清理). 3/4 batch tasks 完成 (d025_s42/mmlu PASS, d100_s42/gsm8k PASS, d100_s42/arc_challenge PASS). 已有成果: d025_s42 和 d100_s42 的 gsm8k+arc signals 已写盘, 但这些 signals 基于旧 alpha=16 checkpoint, D076 重训 alpha=32 后需全部重算, 无需单独 retry. 建议: 等 cuda:1 d100_s42_v3 + cuda:5 d000_s42 重训完成后, 用新 checkpoint 统一重算 3B s42 signals.\"}, \"exp_001_sft_3B_d025_s42_a32_v2\": {\"conclusion\": \"failed\", \"notes\": \"SIGTERM at step 22/3384 (~1.5min training). Training was healthy (no OOM/NaN/error, 4.3s/step pace). bitsandbytes libnvJitLink warning non-fatal. External kill matches D083 pattern. LoRA config confirmed: r=16, alpha=32, lr=5e-5. Need v3 resubmit on cuda:3.\"}, \"exp_001_sft_3B_d100_s42_a32_v2\": {\"conclusion\": \"failed\", \"notes\": \"D083 SIGTERM root cause: Worker agent itself sent SIGTERM via ssh_execute (not OOM/cron/manual). v1 had no CUDA_VISIBLE_DEVICES, landed on occupied GPU 0, Worker detected conflict and killed. v2 killed at 72% progress (step 3030/4159, ~3.5h GPU time lost) without checkpoint save. v3 fixed with explicit CUDA_VISIBLE_DEVICES=2. ssh_execute kill commands don't appear in bash_history, making post-mortem difficult.\"}, \"exp_002_signals_3B_v6\": {\"conclusion\": \"failed\", \"notes\": \"s1_embedding and s2_minkpp completed for all 3 benchmarks (mmlu: 14042, gsm8k: 1319, arc_challenge: 1172). s3_constat crashed on all benchmarks with ValueError: Item count mismatch (expected 1172, got 697 on arc). s4_selfcritique never ran. 6 signal files saved to /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_v2_s42/. Bug is in s3_constat.py:50.\"}, \"exp_002_signals_3B_v4\": {\"conclusion\": \"failed\", \"notes\": \"诊断(2026-05-15): run_batch.py --signal 参数 bug 导致 11/12 combo rc=2 失败, d000/mmlu 被 SIGTERM (rc=-15)。Batch 0/12 passed。但有 5/12 combo 已有 merged 文件(d000/{gsm8k,arc}, d005/arc, d025/{gsm8k,arc})，来自早期或独立进程。v4 tmux session 确认死亡。多个 orphan 进程仍在 GPU 2/3/4 上跑 mmlu combos，有输出目录冲突风险。\"}, \"exp_001_eval_3B_d100_s123_para_aligned\": {\"conclusion\": \"failed\"}, \"exp_001_sft_3B_d000_v3\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: 进程在 step 1725/3125 (55%) 静默死亡，无 Traceback/OOM/CUDA error。cuda:4 双进程共存（SFT + signals ~20.7/24.5GB），高度疑似系统 OOM kill。| 诊断 Worker: worker_diagnose_exp_001_sft_3B_d000_v3_20260515T190929 | 建议: 诊断完成后单独使用 cuda:4 重跑\"}, \"exp_002_signals_3B\": {\"conclusion\": \"failed\"}, \"exp_008_base_pretrained_eval\": {\"conclusion\": \"failed\"}, \"exp_001_sft_15B_d005_s123\": {\"conclusion\": \"failed\"}, \"exp_001_eval_05B_d000_s42_v7\": {\"conclusion\": \"failed\"}, \"exp_004_sim_sweep_v5\": {\"conclusion\": \"failed\", \"metrics\": {\"conditions_all_failed\": [\"auc0.65_n20 (0/10)\", \"auc0.65_n50 (0/7)\"], \"conditions_complete\": 4, \"conditions_fully_ok\": [\"auc0.55_n20 (10/10)\", \"auc0.55_n50 (10/10)\", \"auc0.8_n20 (10/10)\", \"auc0.8_n50 (10/10)\"], \"conditions_missing\": 3, \"conditions_never_started\": [\"auc0.65_n100\", \"auc0.9_n50\", \"auc0.9_n100\"], \"conditions_partial\": 5, \"conditions_partial_ok\": [\"auc0.55_n100 (7/10)\", \"auc0.8_n100 (6/10)\", \"auc0.9_n20 (6/10)\"], \"failure_cause\": \"Disk quota exceeded ([Errno 122]) - root partition /tmp filled by CmdStan temp files\", \"seeds_attempted\": 97, \"seeds_ok\": 59, \"seeds_total\": 120}}, \"exp006-oracle-arc-4pl-pooled\": {\"conclusion\": \"failed\"}, \"exp_001_eval_05B_d000_s42\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: 所有 4 benchmarks 评估完成（HumanEval pass@1=0.1098），但保存 eval_results.json 时 FileNotFoundError——output_dir 未创建。ARC 下载有 HF 连接超时（未 source network_turbo）但评估仍完成。同命令 s123 实验成功。fix_worker_id: worker_fix_eval_05B_d000_s42_v2_20260514T013245 | 建议: 修复 evaluate.py 中保存前的 os.makedirs 调用后重跑\"}, \"exp_004_sim_sweep_v4\": {\"conclusion\": \"failed\"}, \"exp_001_eval_3B_d000_v2_para_aligned_v3\": {\"conclusion\": \"failed\"}, \"exp006-oracle-gsm8k-extended\": {\"conclusion\": \"failed\"}, \"exp006-pooled-s1only-gsm8k\": {\"conclusion\": \"failed\"}, \"exp_004_sim_sweep_v3\": {\"conclusion\": \"failed\", \"notes\": \"v2 PID 599562 was still alive (erroneously marked failed). v1 serial PID 559606 was also running on same results dir — killed to prevent write conflicts. v3 = same process as v2, just corrected registry. 2 CPU / 7.6GB RAM machine, parallel=2 chains_parallel=2. ETA ~20-30h for remaining 66 runs.\"}, \"exp_001_eval_3B_d100_v2_aligned\": {\"conclusion\": \"failed\", \"metrics\": {\"INVALID\": \"metrics were from v1 exp_001_eval_3B_d100_aligned, not v2. v2 output dir was empty. PID 461879 died before completion.\"}, \"notes\": \"DATA INTEGRITY ISSUE (D036): Metrics erroneously copied from v1 (exp_001_eval_3B_d100_aligned). Worker found v1 results at similar path, mistook for v2. v2 output dir was empty (eval still running), then deleted during cleanup. PID 461879 killed/died. Must re-run as v3.\"}, \"exp_001_sft_d025_3B\": {\"conclusion\": \"failed\", \"notes\": \"GPU 3 空转: 注册 RUNNING 但进程从未启动 (nvidia-smi 确认 0% util, 0 MiB). Director 指令标 FAILED.\"}, \"exp006-pooled-05B-15B-mmlu-v2\": {\"conclusion\": \"failed\", \"metrics\": {\"NOTE\": \"fit completely failed, not reportable\", \"convergence\": \"FAILED (rhat=1.54, ess=7)\", \"coverage_95\": 1, \"exposure_source\": \"signal_rrf\", \"gamma_joint\": -0.2095, \"gamma_joint_ci\": [-1.01, 0.59], \"gamma_perbench\": -3.8073, \"gamma_perbench_ci\": [-7.02, 3.22], \"mae\": 0.099, \"n_models\": 8, \"ppp\": 0.75}}, \"exp_005_noise_prop\": {\"conclusion\": \"failed\", \"notes\": \"v1 original run, failed due to /tmp disk exhaustion. Superseded by v2→v3→v4. See v4 for active tracking (PID 559667, 23/25 fits).\"}, \"exp_004_sim_sweep\": {\"conclusion\": \"failed\", \"notes\": \"v1 original serial run. Superseded by v2 (parallel=2). PID 559606 killed to prevent write conflicts with v2. See v3 for active tracking.\"}, \"exp_004_sim_sweep_v2\": {\"conclusion\": \"failed\", \"metrics\": {\"auc080_n100_bias\": 0.008, \"auc080_n100_ci_width\": 0.116, \"auc080_n100_gamma_hat\": 0.508, \"auc080_n100_theta_corr\": 0.962, \"auc080_n50_bias\": 0.006, \"auc080_n50_ci95_coverage\": 1, \"auc080_n50_rmse\": 0.03, \"ci_width_ratio_n100\": 1.81, \"core_findings_stable\": true, \"runs_completed\": 48, \"runs_total\": 120}, \"notes\": \"v2 was erroneously marked failed; PID 599562 was still running. Killed conflicting v1 (PID 559606). Continuing as v3 registry entry.\"}, \"exp_005_noise_prop_v3\": {\"conclusion\": \"failed\", \"notes\": \"PID 559666 crashed (~10h ago). 22/25 fits completed. Restarting as v4.\"}}, \"count\": 50, \"total\": 64, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9136}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
I see `eval_qwen7b_s42_cqa1_v2` has no notes. Let me look at more details for this experiment specifically, and also look for any v3 version of the s42 eval.

Let me search for any experiments with "qwen7b" and "s42" in the name.

Actually, let me reconsider. The task says "评测结果已全部齐全" (all data available). But the v2 eval for s42 failed. Let me check if maybe there's another source for this data - maybe a more recent batch eval that included s42 MMLU.


I should check what metrics `eval_qwen7b_s42_cqa1_v2` might have captured before it failed, and search for any subsequent experiment that retried the s42 MMLU evaluation, possibly under a different naming scheme like qwen7b_mmlu_s42.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "5a860278-9340-4a69-be7b-9e2438f60553",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015QT2g3Y5ox6DQR4dKdWTpt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6977,
      "cache_read_input_tokens": 73204,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6977
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

_source line 23_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01VXKZMSA8xLr3MVFjk3mw7w`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "filters": {
    "exp_id": "eval_qwen7b_s42_cqa1_v2"
  },
  "fields": [
    "*"
  ],
  "limit": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "e2972224-3f02-4cbd-8f0c-d207ee60bc5c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015QT2g3Y5ox6DQR4dKdWTpt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6977,
      "cache_read_input_tokens": 73204,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6977
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

_source line 24 · 2026-05-21T00:19:22.199Z_

<details><summary>↩ Tool result · `toolu_01VXKZMSA8xLr3MVFjk3mw7w`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1736}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "daa644da-5675-4729-a434-a84cbd6e30b7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.1736}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1736}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 25_

<details><summary>Logged reasoning block</summary>

```text
The filter by exp_id didn't work. Let me try a different approach - maybe just search for the specific experiment with all fields.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "ccea7c94-9c33-47e0-9825-f75235073ca0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P9MMQvKzsthW95pREeUEuj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 603,
      "cache_read_input_tokens": 80181,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 603
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01GY1KwBu1kM8LE7UURoqLNW`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "filters": {
    "conclusion": "failed"
  },
  "fields": [
    "exp_id",
    "title",
    "metrics",
    "conclusion",
    "notes"
  ],
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "b0f18298-d9d9-4e05-a5ba-02fb18f08a7b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P9MMQvKzsthW95pREeUEuj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 603,
      "cache_read_input_tokens": 80181,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 603
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

_source line 27 · 2026-05-21T00:19:26.840Z_

<details><summary>↩ Tool result · `toolu_01GY1KwBu1kM8LE7UURoqLNW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval_gemma2_mmlu_s0\": {\"conclusion\": \"failed\"}, \"gsm8k_gemma2_s42_westd\": {\"conclusion\": \"failed\", \"notes\": \"D175 最终排除确认: d000_fixed=11.22%, d100_fixed=3.94% (52/1319, 几乎全 pred:null)。SFT 灾难性遗忘, 非 format bug。GSM8K 跨基准分析正式改为 4/5 家族。cuda:3 已释放。\"}, \"sft_gemma2_s123_sweep\": {\"conclusion\": \"failed\"}, \"sft_qwen14b_s123_sweep\": {\"conclusion\": \"failed\"}, \"eval_qwen7b_s42_cqa1_v2\": {\"conclusion\": \"failed\"}}, \"count\": 5, \"total\": 70, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8561}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "617fbae8-b097-4c3d-80cb-04313cce7071",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval_gemma2_mmlu_s0\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"gsm8k_gemma2_s42_westd\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"D175 最终排除确认: d000_fixed=11.22%, d100_fixed=3.94% (52/1319, 几乎全 pred:null)。SFT 灾难性遗忘, 非 format bug。GSM8K 跨基准分析正式改为 4/5 家族。cuda:3 已释放。\\\"}, \\\"sft_gemma2_s123_sweep\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"sft_qwen14b_s123_sweep\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_qwen7b_s42_cqa1_v2\\\": {\\\"conclusion\\\": \\\"failed\\\"}}, \\\"count\\\": 5, \\\"total\\\": 70, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.8561}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval_gemma2_mmlu_s0\": {\"conclusion\": \"failed\"}, \"gsm8k_gemma2_s42_westd\": {\"conclusion\": \"failed\", \"notes\": \"D175 最终排除确认: d000_fixed=11.22%, d100_fixed=3.94% (52/1319, 几乎全 pred:null)。SFT 灾难性遗忘, 非 format bug。GSM8K 跨基准分析正式改为 4/5 家族。cuda:3 已释放。\"}, \"sft_gemma2_s123_sweep\": {\"conclusion\": \"failed\"}, \"sft_qwen14b_s123_sweep\": {\"conclusion\": \"failed\"}, \"eval_qwen7b_s42_cqa1_v2\": {\"conclusion\": \"failed\"}}, \"count\": 5, \"total\": 70, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8561}}"
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
The `eval_qwen7b_s42_cqa1_v2` has no notes and no metrics. Let me check if there's a v3 experiment. Let me also search for all experiments containing "qwen7b" to see if there's a more recent s42 eval.

Let me look for RUNNING experiments or anything newer.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "596f32d7-a6ae-40c9-8baa-5085732cffaf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NrimBctxM9pWw6TzSfuQER",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 488,
      "cache_read_input_tokens": 80784,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 488
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

_source line 29_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01D3SVh5R6bELNBtAMseyrKa`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "filters": {
    "status": "DONE"
  },
  "fields": [
    "exp_id",
    "title",
    "metrics",
    "conclusion"
  ],
  "limit": 332
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "e448fc48-db09-45f3-b06b-b76980e54c97",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NrimBctxM9pWw6TzSfuQER",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 488,
      "cache_read_input_tokens": 80784,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 488
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

_source line 30 · 2026-05-21T00:19:32.054Z_

<details><summary>↩ Tool result · `toolu_01D3SVh5R6bELNBtAMseyrKa`</summary>

```text
Error: result (76,100 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/ab87e76a-91c7-436c-9cab-6cfa7abe7e5d/tool-results/mcp-agent-ml-research-read_registry-1779322772038.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/ab87e76a-91c7-436c-9cab-6cfa7abe7e5d/tool-results/mcp-agent-ml-research-read_registry-1779322772038.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/ab87e76a-91c7-436c-9cab-6cfa7abe7e5d/tool-results/mcp-agent-ml-research-read_registry-1779322772038.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "ceebd0e2-7f3c-4b24-8883-8460d04398cf",
  "tool_use_result": {
    "content": "Error: result (76,100 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/ab87e76a-91c7-436c-9cab-6cfa7abe7e5d/tool-results/mcp-agent-ml-research-read_registry-1779322772038.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/ab87e76a-91c7-436c-9cab-6cfa7abe7e5d/tool-results/mcp-agent-ml-research-read_registry-1779322772038.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/ab87e76a-91c7-436c-9cab-6cfa7abe7e5d/tool-results/mcp-agent-ml-research-read_registry-1779322772038.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval_qwen7b_mmlu_arc_s0\": {\"conclusion\": \"success\", \"metrics\": {\"mmlu\": {\"d000\": 0.6632, \"d005\": 0.6468, \"d025\": 0.6567, \"d050\": 0.6578, \"d100\": 0.6529, \"delta_d000_d100\": -0.0103}, \"arc_challenge\": {\"d000\": 0.872, \"d005\": 0.8532, \"d025\": 0.8447, \"d050\": 0.8558, \"d100\": 0.8532, \"delta_d000_d100\": -0.0188}}}, \"sft_qwen7b_s0_cqa1\": {\"metrics\": {\"d000\": {\"train_loss\": 0.9259, \"token_accuracy\": 0.7891, \"train_runtime_s\": 13410, \"num_tokens\": 19555717}, \"d005\": {\"train_loss\": 0.9297, \"token_accuracy\": 0.7774, \"train_runtime_s\": 14048, \"num_tokens\": 19657865}, \"d025\": {\"train_loss\": 0.9426, \"token_accuracy\": 0.7705, \"train_runtime_s\": 14039, \"num_tokens\": 20058085}, \"d050\": {\"train_loss\": 0.9595, \"token_accuracy\": 0.7782, \"train_runtime_s\": 14824, \"num_tokens\": 20560314}, \"d100\": {\"train_loss\": 0.9884, \"token_accuracy\": 0.7615, \"train_runtime_s\": 15509, \"num_tokens\": 21575068}}, \"conclusion\": \"success\"}, \"sft_gemma2_s0_sweep\": {\"conclusion\": \"negative\", \"metrics\": {\"mmlu_d000_s0\": 0.6488, \"mmlu_d005_s0\": 0.6414, \"mmlu_d025_s0\": 0.6491, \"mmlu_d050_s0\": 0.6309, \"mmlu_d100_s0\": \"MISSING - d100 OOM crash at step 1618/4159\", \"note\": \"d100 needs retrain, see retrain_gemma2_d100_s0\"}}, \"eval_qwen14b_arc_s42\": {\"conclusion\": \"success\", \"metrics\": {\"d000_s42\": 0.9104, \"d005_s42\": 0.9036, \"d025_s42\": 0.8891, \"d050_s42\": 0.8763, \"d100_s42\": 0.8848, \"delta_d100_d000\": -0.0256, \"collapse_confirmed\": true}}, \"eval_olmo2_arc_s0\": {\"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.7585, \"d005_acc\": 0.7679, \"d025_acc\": 0.7858, \"d050_acc\": 0.785, \"d100_acc\": 0.7935, \"delta_d100_d000\": 0.035, \"correct_d000\": 889, \"correct_d005\": 900, \"correct_d025\": 921, \"correct_d050\": 920, \"correct_d100\": 930, \"total\": 1172}}, \"eval_phi4_arc_s0_s42\": {\"metrics\": {\"phi4_arc_s0\": {\"d000\": 91.81, \"d005\": 92.58, \"d025\": 92.58, \"d050\": 92.83, \"d100\": 92.32, \"delta_d100\": 0.51}, \"phi4_arc_s42\": {\"d000\": 92.06, \"d005\": 91.81, \"d025\": 92.32, \"d050\": 92.41, \"d100\": 92.66, \"delta_d100\": 0.6}, \"arc_3seed_mean_delta\": 0.66, \"arc_3seed_sigma\": 0.18}, \"conclusion\": \"success\"}, \"eval_olmo2_arc_s42\": {\"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.7611, \"d005_acc\": 0.7662, \"d025_acc\": 0.7816, \"d050_acc\": 0.7961, \"d100_acc\": 0.8003, \"delta_d100_d000\": 3.92, \"s123_delta\": 2.9, \"mean_delta_2seeds\": 3.41, \"direction\": \"Benefit\"}}, \"eval_gemma2_arc_s123\": {\"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.8584, \"d005_acc\": 0.8336, \"d025_acc\": 0.8567, \"d050_acc\": 0.8524, \"d100_acc\": 0.8857, \"max_adjacent_delta_pp\": 3.33, \"oscillation_artifact\": false, \"n_items\": 1172}}, \"eval_qwen7b_arc_s42\": {\"metrics\": {\"arc_challenge_accuracy\": {\"d000_s42\": 0.8788, \"d005_s42\": 0.8609, \"d025_s42\": 0.8404, \"d050_s42\": 0.8456, \"d100_s42\": 0.8498}, \"delta_d100_d000\": -0.029, \"items_per_dosage\": 1172}, \"conclusion\": \"success\"}, \"eval_arc_s123_batch\": {\"metrics\": {\"qwen14b_arc_s123\": {\"d000\": 90.44, \"d005\": 91.47, \"d025\": 89.76, \"d050\": 88.74, \"d100\": 87.29, \"delta_d100\": -3.15}, \"phi4_arc_s123\": {\"d000\": 91.89, \"d005\": 91.89, \"d025\": 92.24, \"d050\": 92.58, \"d100\": 92.75, \"delta_d100\": 0.86}, \"qwen7b_arc_s123\": {\"d000\": 87.12, \"d005\": 82.42, \"d025\": 85.15, \"d050\": 85.07, \"d100\": 84.73, \"delta_d100\": -2.39}, \"olmo2_arc_s123\": {\"d000\": 76.88, \"d005\": 77.22, \"d025\": 76.62, \"d050\": 79.18, \"d100\": 79.78, \"delta_d100\": 2.9}}, \"conclusion\": \"success\"}, \"eval_phi4_s0_mmlu\": {\"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.7643, \"d005_acc\": 0.7643, \"d025_acc\": 0.7672, \"d050_acc\": 0.773, \"d100_acc\": 0.7695, \"delta_d100\": 0.0052}}, \"eval_phi4_s123_mmlu\": {\"metrics\": {\"d000_acc\": 76.31, \"d005_acc\": 75.92, \"d025_acc\": 77.02, \"d050_acc\": 77.3, \"d100_acc\": 78.14, \"delta_d100\": 1.83}, \"conclusion\": \"success\"}, \"sft_phi4_s0_sweep\": {\"conclusion\": \"success\", \"metrics\": {\"train_loss_d000\": 1.184, \"train_loss_d005\": 1.185, \"train_loss_d025\": 1.186, \"train_loss_d050\": 1.189, \"train_loss_d100\": 1.192, \"mean_token_acc_d000\": 0.7341, \"mean_token_acc_d005\": 0.7224, \"mean_token_acc_d025\": 0.7064, \"mean_token_acc_d050\": 0.747, \"mean_token_acc_d100\": 0.7206, \"total_train_time_h\": 11.57}}, \"eval_qwen14b_s123_mmlu\": {\"metrics\": {\"d000_acc\": 0.6867, \"d005_acc\": 0.7084, \"d025_acc\": 0.6368, \"d050_acc\": 0.6099, \"d100_acc\": 0.5593, \"delta_d100\": -0.1273}, \"conclusion\": \"success\"}, \"eval_gemma2_s123_mmlu\": {\"metrics\": {\"d000_acc\": 0.6584, \"d005_acc\": 0.6581, \"d025_acc\": 0.6302, \"d050_acc\": 0.6674, \"d100_acc\": 0.6733, \"delta_d100\": 0.0149}, \"conclusion\": \"success\"}, \"eval_olmo2_s123_mmlu\": {\"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.5566, \"d005_acc\": 0.5614, \"d025_acc\": 0.5497, \"d050_acc\": 0.5592, \"d100_acc\": 0.5511, \"delta_d100\": -0.0055}}, \"eval_olmo2_s0_mmlu\": {\"metrics\": {\"mmlu_d000\": 0.5534, \"mmlu_d005\": 0.5662, \"mmlu_d025\": 0.5652, \"mmlu_d050\": 0.5627, \"mmlu_d100\": 0.5672, \"delta_d005\": 0.0128, \"delta_d025\": 0.0118, \"delta_d050\": 0.0093, \"delta_d100\": 0.0138, \"correct_d000\": 7771, \"correct_d005\": 7951, \"correct_d025\": 7937, \"correct_d050\": 7901, \"correct_d100\": 7965, \"total\": 14042}, \"conclusion\": \"success\"}, \"sft_olmo2_s0_sweep\": {\"conclusion\": \"success\"}, \"gsm8k_qwen14b_s123_westd\": {\"conclusion\": \"success\"}, \"gsm8k_gemma2_s42_westd\": {\"conclusion\": \"failed\"}, \"gsm8k_qwen14b_s42_westd\": {\"conclusion\": \"success\", \"metrics\": {\"d000_correct\": 802, \"d000_gsm8k_acc\": 0.608, \"d100_correct\": 1072, \"d100_gsm8k_acc\": 0.8127, \"delta_pp\": 20.47, \"total\": 1319}}, \"irt_fitting_mmlu_v3\": {\"conclusion\": \"success\", \"metrics\": {\"advi_loss\": 160790, \"gamma_mean\": 0.0251, \"gamma_median\": 0.0771, \"gamma_positive_pct\": 58, \"gamma_std\": 0.3593, \"n_draws\": 1000, \"n_items\": 14042, \"n_respondents\": 25, \"trace_file_size_mb\": 432}}, \"sft_qwen14b_d100_s123_retrain\": {\"conclusion\": \"success\"}, \"sft_gemma2_d100_s123_retrain\": {\"conclusion\": \"success\"}, \"gsm8k_phi4_s123_westd\": {\"conclusion\": \"success\", \"metrics\": {\"gsm8k_d000\": 0.8431, \"gsm8k_d100\": 0.8385, \"gsm8k_delta\": -0.0046}}, \"retrain_gemma2_d100_s123\": {\"conclusion\": \"killed\"}, \"retrain_qwen14b_d100_s123\": {\"conclusion\": \"killed\"}, \"gsm8k_qwen7b_s123_cqa1\": {\"conclusion\": \"success\", \"metrics\": {\"d000_note\": \"s123 baseline\", \"d100_note\": \"s123 full contamination\", \"gsm8k_d000\": 0.7005, \"gsm8k_d100\": 0.7923, \"gsm8k_delta\": 0.0918}}, \"sft_gemma2_s123_sweep\": {\"conclusion\": \"failed\"}, \"sft_qwen14b_s123_sweep\": {\"conclusion\": \"failed\"}, \"sft_phi4_s123_sweep\": {\"conclusion\": \"success\", \"metrics\": {\"d000_runtime_s\": 7566, \"d000_token_acc\": 0.7449, \"d000_train_loss\": 1.183, \"d005_runtime_s\": 7636, \"d005_token_acc\": 0.713, \"d005_train_loss\": 1.185, \"d025_runtime_s\": 7985, \"d025_token_acc\": 0.7274, \"d025_train_loss\": 1.186, \"d050_runtime_s\": 8389, \"d050_token_acc\": 0.7484, \"d050_train_loss\": 1.188, \"d100_runtime_s\": 9215, \"d100_token_acc\": 0.741, \"d100_train_loss\": 1.191}}, \"gsm8k_olmo2_s123_westd\": {\"conclusion\": \"success\", \"metrics\": {\"cross_seed_confirmed\": true, \"gsm8k_d000\": 0.6846, \"gsm8k_d100\": 0.7089, \"gsm8k_delta\": 0.0243, \"s123_delta\": 0.0243, \"s42_delta\": 0.0174}}, \"gsm8k_qwen7b_s42_intermediate_cqa1\": {\"conclusion\": \"success\", \"metrics\": {\"curve_shape\": \"non-linear: sharp early gain (d005 +6.37pp = 58% of total), then saturation\", \"delta_d005\": 0.0637, \"delta_d025\": 0.0948, \"delta_d050\": 0.0865, \"delta_d100\": 0.1107, \"gsm8k_d000\": 0.7058, \"gsm8k_d005\": 0.7695, \"gsm8k_d025\": 0.8006, \"gsm8k_d050\": 0.7923, \"gsm8k_d100\": 0.8165}}, \"gsm8k_qwen7b_s42_cqa1\": {\"conclusion\": \"success\", \"metrics\": {\"d000_correct\": 931, \"d100_correct\": 1077, \"gsm8k_d000\": 0.7058, \"gsm8k_d100\": 0.8165, \"gsm8k_delta\": 0.1107, \"total_items\": 1319}}, \"gsm8k_olmo2_s42_westd\": {\"conclusion\": \"success\", \"metrics\": {\"d000_correct\": 903, \"d100_correct\": 926, \"gsm8k_d000\": 0.6846, \"gsm8k_d100\": 0.702, \"gsm8k_delta\": 0.0174, \"total_items\": 1319}}, \"sft_qwen7b_olmo2_s123_sweep\": {\"conclusion\": \"success\", \"metrics\": {\"olmo2_all_checkpoints\": true, \"olmo2_d000_loss\": 0.9431, \"olmo2_d000_token_acc\": 0.7855, \"olmo2_d005_loss\": 0.9475, \"olmo2_d025_loss\": 0.9601, \"olmo2_d050_loss\": 0.9737, \"olmo2_d100_loss\": 0.9979, \"olmo2_d100_token_acc\": 0.7601, \"qwen7b_all_checkpoints\": true, \"total_checkpoints\": 10}}, \"eval_qwen7b_s42_cqa1_v2\": {\"conclusion\": \"failed\"}, \"eval_qwen7b_s123_cqa1_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"d000\": 0.872, \"d005\": 0.8251, \"d025\": 0.8515, \"d050\": 0.8464, \"d100\": 0.8473}, \"arc_delta_d100_vs_d000\": -0.0247, \"mmlu\": {\"d000\": 0.6659, \"d005\": 0.6337, \"d025\": 0.6482, \"d050\": 0.65, \"d100\": 0.6659}, \"mmlu_delta_d100_vs_d000\": 0, \"v_recovery_confirmed\": true}}, \"eval_qwen7b_s123_cqa1\": {\"conclusion\": \"failed\", \"metrics\": {\"arc_d000\": 0.8968, \"arc_d005\": 0.901, \"arc_d025\": 0.901, \"arc_d050\": 0.8985, \"arc_d100\": 0.8968, \"arc_delta_d100_d000\": 0, \"mmlu_d000\": 0.6974, \"mmlu_d005\": 0.6941, \"mmlu_d025\": 0.7025, \"mmlu_d050\": 0.704, \"mmlu_d100\": 0.7066, \"mmlu_delta_d100_d000\": 0.0092}}, \"exp_001_sft_phi4_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7244, \"train_loss\": 1.191}}, \"exp_001_sft_olmo2_7b_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.122, \"mean_token_accuracy\": 0.7459, \"train_loss\": 0.9957, \"train_runtime_sec\": 8584}}, \"exp_001_sft_gemma2_9b_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.158, \"mean_token_accuracy\": 0.7233, \"train_loss\": 1.258, \"train_runtime_sec\": 11110}}, \"exp_001_sft_olmo2_7b_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.122, \"mean_token_accuracy\": 0.7418, \"runtime_seconds\": 7519, \"steps\": 3642, \"train_loss\": 0.9733}}, \"eval_phi4_mmlu_arc_westd\": {\"conclusion\": \"failed\"}, \"exp_001_sft_phi4_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"eval_metrics\": \"none_logged\", \"final_step_accuracy\": 0.7414, \"final_step_loss\": 1.117, \"lora_alpha\": 32, \"lora_r\": 16, \"lr\": 5e-05, \"mean_token_accuracy\": 0.7253, \"num_samples\": 58266, \"total_steps\": 3642, \"train_loss\": 1.189, \"train_runtime_seconds\": 11000, \"wandb_run_id\": null}}, \"exp_001_sft_olmo2_7b_d005_s42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 0.94, \"mean_token_accuracy\": 0.7808, \"runtime_seconds\": 6636, \"steps\": 3177, \"train_loss\": 0.9506}}, \"exp_001_sft_gemma2_9b_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.155, \"mean_token_accuracy\": 0.7239, \"runtime_seconds\": 10400, \"steps\": 3642, \"train_loss\": 1.26}}, \"exp_001_sft_olmo2_7b_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 0.9835, \"mean_token_accuracy\": 0.7732, \"runtime_seconds\": 7420, \"steps\": 3384, \"train_loss\": 0.9582}}, \"exp_001_sft_olmo2_7b_d005_s42\": {\"conclusion\": \"killed\"}, \"eval_7b_mmlu_arc_cqa1\": {\"conclusion\": \"success\", \"metrics\": {\"7b_d000_s123_arc\": 0.8985, \"7b_d000_s123_mmlu\": 0.6978, \"7b_d000_s42_arc\": 0.8959, \"7b_d000_s42_mmlu\": 0.6929, \"7b_d005_s123_arc\": 0.8985, \"7b_d005_s123_mmlu\": 0.6932, \"7b_d005_s42_arc\": 0.8968, \"7b_d005_s42_mmlu\": 0.6924, \"7b_d025_s123_arc\": 0.8993, \"7b_d025_s123_mmlu\": 0.7025, \"7b_d025_s42_arc\": 0.8985, \"7b_d025_s42_mmlu\": 0.7003, \"7b_d050_s123_arc\": 0.8993, \"7b_d050_s123_mmlu\": 0.7034, \"7b_d050_s42_arc\": 0.8993, \"7b_d050_s42_mmlu\": 0.705, \"7b_d100_s123_arc\": 0.8968, \"7b_d100_s123_mmlu\": 0.7072, \"7b_d100_s42_arc\": 0.8933, \"7b_d100_s42_mmlu\": 0.7103}}, \"exp_001_sft_phi4_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_step_accuracy\": 0.7329, \"final_step_loss\": 1.139, \"mean_token_accuracy\": 0.7527, \"total_steps\": 3384, \"train_loss\": 1.187, \"train_runtime_seconds\": 7956, \"wandb_run_id\": null}}, \"exp_001_sft_phi4_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7302, \"final_loss\": 1.185, \"total_steps\": 3177, \"train_runtime_seconds\": 9321, \"wandb_run_id\": null}}, \"eval_14b_mmlu_arc_westd_v2\": {\"conclusion\": \"success\", \"metrics\": {\"14b_d000_arc\": 0.9352, \"14b_d000_mmlu\": 0.7459, \"14b_d005_arc\": 0.9309, \"14b_d005_mmlu\": 0.7542, \"14b_d025_arc\": 0.9283, \"14b_d025_mmlu\": 0.7577, \"14b_d050_arc\": 0.9283, \"14b_d050_mmlu\": 0.7687, \"14b_d100_arc\": 0.9309, \"14b_d100_mmlu\": 0.7651}}, \"exp_001_sft_gemma2_9b_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7384, \"final_loss\": 1.143, \"total_steps\": 3384, \"train_loss_avg\": 1.258, \"train_runtime_seconds\": 9451}}, \"eval_14b_mmlu_arc_westd\": {\"conclusion\": \"failed\"}, \"exp_001_sft_phi4_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7287, \"final_loss\": 1.183, \"total_steps\": 3125, \"train_runtime_seconds\": 7500}}, \"exp_001_sft_olmo2_7b_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7841, \"final_loss\": 0.9434, \"total_steps\": 3125, \"train_runtime_seconds\": 6060}}, \"exp_001_sft_14b_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7488, \"final_loss\": 0.9682, \"total_steps\": 4159, \"train_runtime_seconds\": 13560}}, \"exp_001_sft_gemma2_9b_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.7303, \"final_loss\": 1.157, \"total_steps\": 3177}}, \"exp_001_sft_14b_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.776, \"final_loss\": 0.9165, \"total_steps\": 3642}}, \"eval_7b_batch1_westd\": {\"conclusion\": \"failed\"}, \"exp_001_sft_14b_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_accuracy\": 0.774, \"final_loss\": 0.926, \"total_steps\": 3384}}, \"eval_7b_batch_cqa1\": {\"conclusion\": \"killed\"}, \"exp_001_sft_gemma2_9b_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"avg_train_loss\": 1.257, \"mean_token_accuracy\": 0.7284, \"steps\": 3125, \"train_loss\": 1.159, \"train_runtime_seconds\": 9453}}, \"exp_001_sft_7b_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"adapter_size_mb\": 155, \"avg_train_loss\": 0.9247, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d000_s42/lora_adapter/\", \"final_loss\": 0.8814, \"lora_alpha\": 32, \"lora_r\": 16, \"mean_token_accuracy\": 0.7917, \"runtime_sec\": 5358, \"total_steps\": 3125}}, \"exp_001_sft_7b_d100_s123\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.766, \"note\": \"loss/acc from trainer_state.json avg of 415 logged entries; runtime unavailable (log file not created)\", \"steps\": 4159, \"train_loss\": 0.988, \"train_runtime_seconds\": null}}, \"exp_001_sft_7b_d050_s123\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.776, \"steps\": 3642, \"train_loss\": 0.935}}, \"exp_001_sft_14b_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7969, \"steps\": 3177, \"train_loss\": 0.9141, \"train_runtime_seconds\": 9986}}, \"exp_001_sft_7b_d025_s123\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.814, \"steps\": 3384, \"train_loss\": 0.9431, \"train_runtime_seconds\": 5621}}, \"exp_001_sft_7b_d005_s123\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7568, \"steps\": 3177, \"train_loss\": 0.9304, \"train_runtime_seconds\": 6497}}, \"exp_001_sft_7b_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7452, \"steps\": 4159, \"train_loss\": 0.987, \"train_runtime_seconds\": 6384}}, \"exp_001_sft_7b_d050_s42\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7641, \"steps\": 3642, \"train_loss\": 0.9599}}, \"exp_001_sft_14b_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"final_token_accuracy\": 0.7761, \"final_train_loss\": 0.9089, \"total_steps\": 3125, \"training_time\": \"2h42m38s\"}}, \"exp_001_sft_7b_d000_s123\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_size\": \"154MB\", \"train_loss\": 0.9249, \"train_time\": \"1h47m\"}}, \"exp_001_sft_7b_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_size\": \"154MB\", \"train_loss\": 0.9429, \"train_time\": \"1h34m\"}}, \"exp_001_eval_7b_d000_s42_gsm8k\": {\"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.7104, \"gsm8k_correct\": 937, \"gsm8k_total\": 1319}}, \"exp_001_sft_7b_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_size\": \"639MB\", \"mean_token_accuracy\": 0.7896, \"total_steps\": 3177, \"train_loss\": 0.9299, \"train_time\": \"1h30m\"}}, \"exp_006_mmlu_vanilla_2pl_fullitems\": {\"conclusion\": \"success\", \"metrics\": {\"Rhat_range\": \"[0.9995, 1.0026]\", \"comparison_300item_p\": 0.0061, \"comparison_300item_tau\": 0.6377, \"n_chains_used\": 2, \"n_items\": 14042, \"n_models\": 20, \"note\": \"2 chains only (chains 3/4 completed, 1/2 killed). Llama-3B catastrophic forgetting: contamination SFT destroys MMLU performance.\", \"tau\": 0.0237, \"tau_1.5B\": 0.31, \"tau_Llama3B\": -1, \"tau_Qwen3B\": 0.08, \"tau_p\": 0.893}}, \"exp_001_eval_3B_d025_s123_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"ARC\": 0.8121, \"GSM8K\": 0.4254, \"HumanEval\": 0.1538, \"MMLU\": 0.6615}}, \"exp_002_signals_3B_d100_s123_v9\": {\"conclusion\": \"success\"}, \"exp_006_j16_theta_extraction\": {\"conclusion\": \"failed\"}, \"exp_006_cross_family_irt_j16\": {\"conclusion\": \"failed\", \"metrics\": {\"PPP_Medical\": 0.827, \"PPP_STEM_CS_Eng\": 0.893, \"PPP_acceptable_only\": \"STEM_CS_Eng (0.893), Medical (0.827)\", \"PPP_warning\": \"6/8 domains PPP>0.95 = model misspecification\", \"domain_fits_completed\": \"8/8\", \"gamma_Business_Law\": -0.239, \"gamma_Humanities\": -0.947, \"gamma_Medical\": 0.218, \"gamma_Other\": -0.88, \"gamma_STEM_CS_Eng\": 0.362, \"gamma_STEM_Math\": -0.386, \"gamma_STEM_Science\": 0.042, \"gamma_Social_Sciences\": -1.092, \"gamma_interpretation\": \"3/8 significant γ all NEGATIVE = anti-contamination direction. Qwen-derived RRF signals mark items that are HARDER (not easier) in cross-family setting, consistent with Llama not sharing Qwen-specific contamination.\", \"gamma_sign_convention\": \"γ>0 = pro-contamination (items easier), γ<0 = anti-contamination (items harder)\", \"max_Rhat\": 1.01, \"min_ESS\": 1331, \"pooled_fit\": \"failed (container security policy)\", \"significant_gamma_domains\": 3, \"theta_by_model\": \"NOT SAVED - needs script modification\", \"total_divergences\": 0}}, \"exp_002_signals_3B_d000_s123_cuda2\": {\"conclusion\": \"failed\"}, \"exp_008_base_pretrained_eval_gsm8k_arc\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.228, \"gsm8k_accuracy\": 0.163}}, \"exp_006_theta_extraction_j13\": {\"conclusion\": \"failed\"}, \"exp_009_deepseek_eval\": {\"conclusion\": \"negative\", \"metrics\": {\"arc_acc\": 0.226, \"arc_n\": 1172, \"gsm8k_acc\": 0.608, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.229, \"mmlu_n\": 14042, \"note\": \"MMLU/ARC below random due to logprob-based MC eval incompatible with CoT reasoning model; only GSM8K valid\"}}, \"exp_009_3b_instruct_eval\": {\"conclusion\": \"success\", \"metrics\": {\"arc_acc\": 0.811, \"arc_n\": 1172, \"gsm8k_acc\": 0.76, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.605, \"mmlu_n\": 14042}}, \"exp_009_15b_instruct_eval\": {\"conclusion\": \"success\", \"metrics\": {\"arc_acc\": 0.765, \"arc_n\": 1172, \"gsm8k_acc\": 0.593, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.577, \"mmlu_n\": 14042}}, \"exp_009_05b_instruct_eval\": {\"conclusion\": \"success\", \"metrics\": {\"arc_acc\": 0.5, \"arc_n\": 1172, \"gsm8k_acc\": 0.388, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.343, \"mmlu_n\": 14042}}, \"exp_009_deepseek_signals\": {\"conclusion\": \"success\"}, \"exp_009_3b_instruct_signals\": {\"conclusion\": \"success\"}, \"exp_009_15b_instruct_signals\": {\"conclusion\": \"success\"}, \"exp_009_05b_instruct_signals\": {\"conclusion\": \"success\"}, \"exp_006_mmlu_domain_gamma_no05b_j13\": {\"conclusion\": \"negative\", \"metrics\": {\"domains_sig_negative\": 1, \"domains_sig_positive\": 0, \"gamma_math\": 0.499, \"gamma_math_sig\": false, \"gamma_pooled\": 0.107, \"gamma_pooled_ci\": \"[-0.401, 0.625]\", \"gamma_pooled_sig\": false, \"gamma_social_sci\": -0.571, \"gamma_social_sci_ci\": \"[-1.054, -0.103]\", \"gamma_social_sci_sig\": true, \"n_domains\": 8, \"n_respondents\": 13}}, \"exp_001_eval_3B_d000_s42_a32_batch\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"aligned\": 0.8242, \"aligned_n\": 1172, \"para_aligned\": 0.8106, \"para_aligned_n\": 697}, \"gsm8k\": {\"aligned\": 0.141, \"aligned_n\": 1319, \"para_aligned\": 0.0526, \"para_aligned_n\": 228}, \"humaneval\": {\"aligned\": 0.1402, \"aligned_n\": 164, \"para_aligned\": 0.1923, \"para_aligned_n\": 26}, \"mmlu\": {\"aligned\": 0.6307, \"aligned_n\": 14042, \"para_aligned\": 0.6431, \"para_aligned_n\": 6596}}}, \"exp_001_sft_3B_d100_s123_a32_v2\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.231, \"epoch\": 1, \"mean_token_accuracy\": 0.7348, \"train_loss\": 1.1805, \"train_runtime_seconds\": 17608.59, \"train_samples_per_second\": 3.778, \"train_steps\": 4159}}, \"exp_001_eval_3B_d100_s42_a32_batch\": {\"conclusion\": \"success\", \"metrics\": {\"aligned\": {\"arc_challenge\": 0.8208, \"gsm8k\": 0.7036, \"humaneval_correct\": \"26/164\", \"mmlu\": 0.6364}, \"para_aligned\": {\"arc_challenge\": 0.8106, \"gsm8k\": 0.5702, \"humaneval_correct\": \"2/26\", \"mmlu\": 0.6674}}}, \"exp_001_eval_3B_d100_s123_a32_batch\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"aligned\": 0.8251, \"aligned_n\": 1172, \"para_aligned\": 0.8049, \"para_aligned_n\": 697}, \"gsm8k\": {\"aligned\": 0.7074, \"aligned_n\": 1319, \"para_aligned\": 0.5746, \"para_aligned_n\": 228}, \"humaneval\": {\"aligned\": 0.1159, \"aligned_n\": 164, \"para_aligned\": 0, \"para_aligned_n\": 26}, \"mmlu\": {\"aligned\": 0.633, \"aligned_n\": 14042, \"para_aligned\": 0.6598, \"para_aligned_n\": 6596}}}, \"exp_001_eval_3B_d005_s123_gsm8k\": {\"conclusion\": \"success\", \"metrics\": {\"gsm8k\": 0.6308}}, \"exp_001_sft_llama32_3B_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"mean_token_accuracy\": 0.6599, \"note\": \"Training completed successfully. Merge failed (disk full) but LoRA adapter saved intact.\", \"train_loss\": 1.5206, \"train_runtime_sec\": 8140.83, \"train_samples_per_second\": 6.243, \"train_steps_per_second\": 0.39}}, \"exp_001_eval_llama32_3B_d000_s42_v3\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.6007, \"gsm8k\": 0.1918, \"humaneval_pass@1\": 0.0427, \"mmlu\": 0.4545}}, \"exp_001_sft_llama32_3B_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"epochs\": 1, \"mean_token_accuracy\": 0.6505, \"train_loss\": 1.5435, \"train_runtime_sec\": 9847, \"train_steps_per_second\": 0.422}}, \"exp_002_signals_15B_instruct_arc\": {\"conclusion\": \"success\"}, \"exp_002_signals_15B_instruct_mmlu\": {\"conclusion\": \"success\"}, \"exp_002_signals_llama32_3B_d000_arc\": {\"conclusion\": \"success\"}, \"exp_002_signals_llama32_3B_d000_gsm8k_v2\": {\"conclusion\": \"success\", \"metrics\": {\"all_signals_nonempty\": true, \"signal_files\": {\"signal_s1_embedding_gsm8k.json\": {\"items\": 1319, \"size\": \"717K\"}, \"signal_s2_minkpp_gsm8k.json\": {\"items\": 1319, \"size\": \"266K\"}, \"signal_s4_selfcritique_gsm8k.json\": {\"items\": 1319, \"size\": \"311K\"}, \"signals_merged_gsm8k.json\": {\"items\": 1319, \"size\": \"238K\"}}, \"signals_computed\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"], \"total_items\": 1319}}, \"exp_001_eval_llama32_3B_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"humaneval_pass@1\": 0.0244, \"mmlu\": 0.415}}, \"exp_001_eval_llama32_3B_d005_s42\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.5956, \"gsm8k\": 0.2722, \"humaneval_pass@1\": 0.0122, \"mmlu\": 0.4256}}, \"exp_002_signals_15B_instruct_arc_v2\": {\"conclusion\": \"success\"}, \"exp_001_eval_llama32_3B_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"arc_acc\": 0.5981, \"gsm8k_acc\": 0.26, \"mmlu_acc\": 0.3408, \"note\": \"MMLU degenerate (all-A prediction), ARC/GSM8K valid\"}}, \"exp_002_signals_15B_instruct_mmlu_v2\": {\"conclusion\": \"success\", \"metrics\": {\"benchmark\": \"mmlu\", \"items\": 14042, \"note\": \"EXIT_CODE=1 was false positive, data verified complete by Reviewer\", \"signals\": \"s1+s2+s4\"}}, \"exp_002_signals_llama32_3B_d005_mmlu\": {\"conclusion\": \"success\"}, \"exp_006_scale_stratified_irt\": {\"conclusion\": \"negative\"}, \"exp_006_pooled_irt_05b_15b_arc_2pl\": {\"conclusion\": \"negative\"}, \"exp_005_noise_prop_v4\": {\"conclusion\": \"negative\", \"metrics\": {\"all_converged\": true, \"ci_width_range\": \"0.0997-0.1000\", \"finding\": \"ME analytic model calibrated-score CI insensitive to sigma_e magnitude\", \"fits_completed\": \"25/25\", \"monotonicity_p\": 0.5, \"monotonicity_rho\": 0.4}}, \"exp006_cross_family_pooled_irt\": {\"conclusion\": \"negative\", \"metrics\": {\"N_pooled_arc\": 20, \"N_pooled_gsm8k\": 28, \"N_pooled_mmlu\": 20, \"arc_gamma_pooled\": 0.002, \"arc_gamma_qwen_only\": 0.727, \"family_specificity_arc_delta\": -0.725, \"gsm8k_gamma_pooled\": -0.11, \"mmlu_gamma_pooled\": 0.213, \"mmlu_gamma_qwen_only\": 0.655, \"v3_clean\": true}}, \"exp006-pooled-05B-15B-gsm8k-v2\": {\"conclusion\": \"negative\", \"metrics\": {\"NOTE\": \"per-bench not converged; no oracle baseline exists\", \"convergence\": \"FAILED (rhat=1.015, ess=330)\", \"coverage_95\": 0.5, \"exposure_source\": \"signal_rrf\", \"gamma_joint\": 0.1202, \"gamma_joint_ci\": [-0.74, 0.96], \"gamma_perbench\": 0.1871, \"gamma_perbench_ci\": [-0.92, 1.33], \"mae\": 0.036, \"n_models\": 8, \"ppp\": 0.336}}, \"exp_002_signals_llama32_3B_d100_mmlu\": {\"conclusion\": \"killed\"}, \"exp_002_signals_llama32_3B_d100_arc\": {\"conclusion\": \"success\"}, \"exp_002_signals_llama32_3B_d100_gsm8k\": {\"conclusion\": \"success\"}, \"exp_002_signals_llama32_3B_d000_arc_gsm8k\": {\"conclusion\": \"success\"}, \"exp_002_signals_llama32_3B_d000_mmlu\": {\"conclusion\": \"success\"}, \"exp_004_fisher_heatmap_w4_v2\": {\"conclusion\": \"success\", \"metrics\": {\"mc_draws\": 50, \"method\": \"analytical_fisher_information_CRLB\", \"model\": \"2PL+gamma\", \"power_n30_auc70\": 0.82, \"threshold_n20_auc\": 0.75, \"threshold_n30_auc\": 0.7, \"threshold_n50_auc\": 0.65}}, \"exp_002_signals_llama32_3B_d025_completion\": {\"conclusion\": \"success\"}, \"exp_002_signals_llama32_3B_d025_mmlu_arc_gsm8k\": {\"conclusion\": \"failed\"}, \"exp_002_signals_llama32_3B_d005_arc_gsm8k\": {\"conclusion\": \"success\"}, \"exp_004_fisher_heatmap_w4\": {\"conclusion\": \"failed\"}, \"exp_006_pooled_2pl_gamma_qwen_n24\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"N\": 16, \"cal_mae\": 0.0201, \"delta_mae\": 0.0136, \"ess\": 1449, \"gamma_ci\": [0.0207, 1.4433], \"gamma_mean\": 0.7269, \"items\": 300, \"ppp\": 0.003, \"raw_mae\": 0.0338, \"rhat\": 1.0072}, \"gsm8k\": {\"N\": 24, \"cal_mae\": 0.0062, \"delta_mae\": 0.1632, \"ess\": 1313, \"gamma_ci\": [-0.3636, 0.4902], \"gamma_mean\": 0.0639, \"items\": 300, \"ppp\": 0.5413, \"raw_mae\": 0.1694, \"rhat\": 1.0078}, \"mmlu\": {\"N\": 16, \"cal_mae\": 0.007, \"delta_mae\": 0.0085, \"ess\": 1453, \"gamma_ci\": [-0.4056, 1.7366], \"gamma_mean\": 0.6551, \"items\": 300, \"ppp\": 0.192, \"raw_mae\": 0.0155, \"rhat\": 1.0069}}}, \"exp_002_signals_llama32_3B_d000_gsm8k\": {\"conclusion\": \"failed\"}, \"exp_001_sft_llama32_3B_d025_s42\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"mean_token_accuracy\": 0.6755, \"train_loss\": 1.5265, \"train_runtime_sec\": 8349.26, \"train_samples_per_second\": 6.484, \"train_steps_per_second\": 0.405}}, \"exp_002_signals_15B_instruct_gsm8k\": {\"conclusion\": \"failed\"}, \"exp_006_pooled_irt_vanilla_2pl_n13\": {\"conclusion\": \"success\", \"metrics\": {\"ARC\": {\"N\": 16, \"PPP\": 0.035, \"cal_MAE\": 0.0158, \"delta_MAE\": 0.018, \"raw_MAE\": 0.0338}, \"GSM8K\": {\"N\": 24, \"PPP\": 0.691, \"cal_MAE\": 0.0063, \"delta_MAE\": 0.1631, \"raw_MAE\": 0.1694}, \"MMLU\": {\"N\": 16, \"PPP\": 0.349, \"cal_MAE\": 0.0068, \"delta_MAE\": 0.0087, \"raw_MAE\": 0.0155}, \"note\": \"Re-run with naming fix applied, now N=16 (was N=13 before fix). Confirms vanilla 2PL has lower calMAE on MMLU/ARC.\"}}, \"exp_006_pooled_irt_2pl_gamma_n16\": {\"conclusion\": \"success\", \"metrics\": {\"ARC\": {\"CI_excludes_zero\": true, \"N\": 16, \"PPP\": 0.003, \"R_hat_max\": 1.01, \"cal_MAE\": 0.0201, \"delta_MAE\": 0.0136, \"gamma_hat\": 0.73}, \"GSM8K\": {\"CI_excludes_zero\": false, \"N\": 24, \"PPP\": 0.541, \"R_hat_max\": 1.01, \"cal_MAE\": 0.0062, \"delta_MAE\": 0.1632, \"gamma_hat\": 0.06}, \"MMLU\": {\"CI_excludes_zero\": false, \"N\": 16, \"PPP\": 0.193, \"R_hat_max\": 1.01, \"cal_MAE\": 0.0072, \"delta_MAE\": 0.0083, \"gamma_hat\": 0.7}, \"note\": \"N=16 fixed (naming normalization applied), 0 divergences, ESS>1300\"}}, \"exp006_pooled_irt_n16_fixed\": {\"conclusion\": \"success\"}, \"exp_001_eval_05B_instruct\": {\"conclusion\": \"success\"}, \"exp_001_eval_llama32_3B_d000_s42\": {\"conclusion\": \"killed\", \"metrics\": {\"MMLU\": 0.4545}}, \"exp_001_eval_15B_instruct\": {\"conclusion\": \"success\", \"metrics\": {\"ARC\": 0.7654, \"GSM8K\": 0.5929, \"MMLU\": 0.5775}}, \"exp_006_mmlu_domain_gamma_n24_v4\": {\"conclusion\": \"success\", \"metrics\": {\"Business_Law_gamma\": \"not_significant\", \"CS_Eng_gamma\": \"not_significant\", \"Humanities_gamma\": \"negative_significant\", \"Medical_gamma\": \"negative_significant\", \"STEM_Math_gamma\": \"positive_significant\", \"STEM_Science_gamma\": \"positive_significant\", \"Social_Sciences_gamma\": \"negative_significant\", \"domains\": 7, \"note\": \"CmdStan crashed after results saved. Humanities rhat=1.014 not converged.\"}}, \"exp_006_pooled_irt_rrf_n25_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_N8_4PLgamma\": \"over_parameterized_cal_worsens\", \"gsm8k_N16_delta_mae\": 0.118, \"gsm8k_calibration\": \"effective\", \"mmlu_N8_4PLgamma\": \"over_parameterized_cal_worsens\", \"note\": \"GSM8K N=16 works. MMLU/ARC N=8 with 4PL+gamma over-parameterized, PPP=0.006/0.000, cal_mae > raw_mae. Need 2PL+gamma or N>=16.\"}}, \"exp_003_rrf_full_n25_latest\": {\"conclusion\": \"success\"}, \"signals_05B_s123_v2\": {\"conclusion\": \"success\"}, \"exp_006_pooled_irt_n25\": {\"conclusion\": \"success\"}, \"exp_001_eval_3B_instruct_v2\": {\"conclusion\": \"success\", \"metrics\": {\"GSM8K\": 0.76, \"HumanEval\": 0.5, \"MMLU\": 0.605}}, \"exp_006_mmlu_domain_gamma_n24_v3\": {\"conclusion\": \"failed\", \"metrics\": {\"Humanities\": {\"CI\": [-0.776, -0.041], \"N\": 21, \"PPP\": 1, \"converged\": \"borderline_rhat_1.014\", \"excludes_zero\": true, \"gamma_mean\": -0.407}, \"Medical\": {\"CI\": [-0.338, -0.06], \"N\": 24, \"PPP\": 1, \"converged\": true, \"excludes_zero\": true, \"gamma_mean\": -0.199}, \"STEM_CS_Eng\": {\"CI\": [-0.448, 0.835], \"N\": 23, \"PPP\": 0.892, \"converged\": true, \"excludes_zero\": false, \"gamma_mean\": 0.197}, \"STEM_Math\": {\"CI\": [0.527, 1.43], \"N\": 23, \"PPP\": 0.438, \"converged\": true, \"excludes_zero\": true, \"gamma_mean\": 0.969}, \"STEM_Science\": {\"CI\": [0.385, 1.274], \"N\": 23, \"PPP\": 0.807, \"converged\": true, \"excludes_zero\": true, \"gamma_mean\": 0.838}, \"completed_domains\": 5, \"crashed\": \"Social_Sciences (CmdStan retcode=[1,0,0,1])\", \"not_run\": [\"Business_Law\", \"Other\"], \"total_domains\": 8}}, \"exp_002_signals_15B_d100_s123_cuda2\": {\"conclusion\": \"success\"}, \"exp_002_signals_15B_s123_batch\": {\"conclusion\": \"success\"}, \"exp_006_mmlu_domain_gamma_n24\": {\"conclusion\": \"success\", \"metrics\": {\"STEM_CS_Eng\": {\"N_items\": 557, \"N_models\": 23, \"PPP\": 0.892, \"fit_time_s\": 153, \"gamma_excludes_zero\": false, \"gamma_mean\": 0.197}, \"STEM_Math\": {\"N_items\": 1190, \"N_models\": 23, \"PPP\": 0.438, \"fit_time_s\": 527, \"gamma_excludes_zero\": true, \"gamma_mean\": 0.969}, \"STEM_Science\": {\"N_items\": 1397, \"N_models\": 23, \"PPP\": 0.807, \"fit_time_s\": 618, \"gamma_excludes_zero\": true, \"gamma_mean\": 0.838}, \"domains_completed\": 3, \"domains_total\": 8, \"note\": \"3/8 domains complete. Process stopped after 3 — remaining 5 need restart.\"}}, \"exp_006_mmlu_domain_gamma_n24_v2\": {\"conclusion\": \"failed\"}, \"exp_001_sft_llama32_3B_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"mean_token_accuracy\": 0.6685, \"train_loss\": 1.5165, \"train_runtime_sec\": 8170}}, \"exp_002_signals_05B_s123_v2\": {\"conclusion\": \"success\"}, \"exp_001_sft_3B_d100_s123_a32\": {\"conclusion\": \"success\"}, \"exp_002_signals_3B_d100_a32_s42\": {\"conclusion\": \"success\", \"metrics\": {\"benchmarks_completed\": [\"mmlu\", \"gsm8k\", \"arc_challenge\"], \"signals_generated\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"], \"status_note\": \"Signals validated via pooled IRT (exp_006_pooled_irt_all_scales, N=23 success). Analysis worker completed 2026-05-16T10:50:52 but callback not processed due to session reset.\"}}, \"exp_006_pooled_irt_all_scales\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"cal_mae\": 0.0153, \"delta_mae\": 0.0183, \"divergences\": 0, \"ess\": 1670, \"gamma_ci95\": [-0.2552, 1.2529], \"gamma_mean\": 0.4859, \"n_items\": 300, \"n_models\": 13, \"ppp\": 0.027, \"raw_mae\": 0.0335, \"rhat\": 1.0065}, \"exposure\": \"rrf_signal\", \"gsm8k\": {\"cal_mae\": 0.0078, \"delta_mae\": 0.1552, \"divergences\": 0, \"ess\": 1388, \"gamma_ci95\": [-0.2889, 0.637], \"gamma_mean\": 0.1721, \"n_items\": 300, \"n_models\": 20, \"ppp\": 0.3425, \"raw_mae\": 0.163, \"rhat\": 1.0071}, \"mmlu\": {\"cal_mae\": 0.0059, \"delta_mae\": 0.0098, \"divergences\": 0, \"ess\": 1402, \"gamma_ci95\": [-0.5501, 1.5974], \"gamma_mean\": 0.5172, \"n_items\": 300, \"n_models\": 15, \"ppp\": 0.2335, \"raw_mae\": 0.0157, \"rhat\": 1.0067}, \"model_type\": \"2pl_gamma\", \"rrf_respondents\": 23, \"scales\": [\"0.5B\", \"1.5B\", \"3B\"]}}, \"exp_001_eval_3B_instruct_aligned_para\": {\"conclusion\": \"failed\"}, \"exp_002_signals_3B_d000_a32_s42\": {\"conclusion\": \"success\", \"metrics\": {\"benchmarks\": {\"arc_challenge\": {\"n_items\": 1172, \"signals\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]}, \"gsm8k\": {\"n_items\": 1319, \"signals\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]}, \"mmlu\": {\"n_items\": 14042, \"signals\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]}}, \"output_files\": {\"signal_s1_embedding_arc_challenge.json\": \"650K\", \"signal_s1_embedding_gsm8k.json\": \"717K\", \"signal_s1_embedding_mmlu.json\": \"7.6M\", \"signal_s2_minkpp_arc_challenge.json\": \"245K\", \"signal_s2_minkpp_gsm8k.json\": \"266K\", \"signal_s2_minkpp_mmlu.json\": \"2.8M\", \"signal_s4_selfcritique_arc_challenge.json\": \"284K\", \"signal_s4_selfcritique_gsm8k.json\": \"310K\", \"signal_s4_selfcritique_mmlu.json\": \"3.2M\"}, \"runtime_minutes\": 189, \"signals_completed\": 9, \"signals_failed\": 0}}, \"exp_002_signals_3B_d005_a32_s42\": {\"conclusion\": \"success\"}, \"exp_006_pooled_irt_05b_15b\": {\"conclusion\": \"success\", \"metrics\": {\"arc_cal_mae\": 0.0682, \"arc_ci95\": \"[-0.271, 2.857]\", \"arc_delta_mae\": -0.064, \"arc_ess\": 1480, \"arc_gamma\": 1.2259, \"arc_n_models\": 5, \"arc_ppp\": 0, \"arc_raw_mae\": 0.0042, \"arc_rhat\": 1.0072, \"gsm8k_cal_mae\": 0.0373, \"gsm8k_ci95\": \"[-0.990, 1.019]\", \"gsm8k_delta_mae\": 0.1128, \"gsm8k_ess\": 1300, \"gsm8k_gamma\": 0.0128, \"gsm8k_n_models\": 11, \"gsm8k_ppp\": 0.663, \"gsm8k_raw_mae\": 0.1501, \"gsm8k_rhat\": 1.0072, \"n_items_subsampled\": 300}}, \"exp006_pooled_rrf_irt_05b_15b\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"cal_mae\": 0.0682, \"delta_mae\": -0.064, \"divergences\": 0, \"ess\": 1480, \"gamma_ci95\": [-0.2711, 2.8571], \"gamma_mean\": 1.2259, \"n_items\": 300, \"n_models\": 5, \"ppp\": 0, \"raw_mae\": 0.0042, \"rhat\": 1.0072}, \"gsm8k\": {\"cal_mae\": 0.0373, \"delta_mae\": 0.1128, \"divergences\": 0, \"ess\": 1300, \"gamma_ci95\": [-0.99, 1.0187], \"gamma_mean\": 0.0128, \"n_items\": 300, \"n_models\": 11, \"ppp\": 0.663, \"raw_mae\": 0.1501, \"rhat\": 1.0072}}}, \"exp_006_mmlu_domain_gamma\": {\"conclusion\": \"success\", \"metrics\": {\"Business_Law_gamma\": 0.61, \"Humanities_gamma\": 0.47, \"Medical_gamma\": 0.27, \"Other_gamma\": 1.34, \"STEM_CS_Eng_gamma\": 0.29, \"STEM_Math_gamma\": -0.55, \"STEM_Science_gamma\": 0.36, \"Social_Sciences_gamma\": 0.28, \"all_rhat_max\": 1.008, \"divergent_transitions\": 0, \"n_domains\": 8, \"n_models\": 16}}, \"exp_001_eval_3B_d005_s42_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_acc\": 0.8164, \"arc_challenge_n\": 697, \"gsm8k_acc\": 0.3421, \"gsm8k_n\": 228, \"humaneval_n\": 26, \"humaneval_pass1\": 0.0769, \"mmlu_acc\": 0.6471, \"mmlu_n\": 6596}}, \"exp_001_eval_3B_d000_s42_a32_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_para\": 0.8106, \"gsm8k_para\": 0.0526, \"humaneval_para\": 0.1923, \"mmlu_para\": 0.6431}}, \"exp_001_eval_3B_d005_s42_a32_batch\": {\"conclusion\": \"success\", \"metrics\": {\"arc\": 0.8251, \"arc_para\": 0.8164, \"gsm8k\": 0.4147, \"gsm8k_para\": 0.3421, \"humaneval\": 0.1341, \"humaneval_para\": 0.0769, \"mmlu\": 0.6308, \"mmlu_para\": 0.6471}}, \"exp_008_instruct_rl_proxy\": {\"conclusion\": \"failed\", \"metrics\": {\"base_pretrained_signals\": \"computing_PID_701898_GPU5\", \"comparison\": {\"arc\": {\"d000_sft_s2\": 1.7079, \"d000_sft_s4\": -0.9538, \"instruct_s2\": 1.6737, \"instruct_s4\": -0.9227, \"s4_delta_instruct_vs_sft\": 0.0311}, \"gsm8k\": {\"d000_sft_s2\": 1.6532, \"d000_sft_s4\": -0.9408, \"instruct_s2\": 1.7073, \"instruct_s4\": -0.9632, \"s4_delta_instruct_vs_sft\": -0.0224}, \"mmlu\": {\"base_s2\": 1.7009, \"base_s4\": \"computing\", \"d000_sft_s2\": 1.6976, \"d000_sft_s4\": -0.9557, \"instruct_s2\": 1.6952, \"instruct_s4\": -0.8782, \"s4_delta_instruct_vs_sft\": 0.0775}}, \"d000_sft_signals_complete\": true, \"instruct_signals_complete\": true, \"key_finding\": \"S4 differentiates regimes (MMLU +0.078, ARC +0.031 Instruct vs SFT); S2 does not (<0.01 difference). RL increases S4 entropy on knowledge benchmarks.\", \"signal_paths\": {\"base_pretrained\": \"/root/autodl-tmp/exp008/signals/base_pretrained/\", \"d000_sft\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/\", \"instruct\": \"/root/autodl-tmp/exp008/signals/rl_aligned/\"}}}, \"exp_003_mmlu_item_aligned_gap\": {\"conclusion\": \"success\", \"metrics\": {\"aggregate\": {\"max_abs_gap_pp\": 3.73, \"mean_gap_pp\": -2.243, \"median_gap_pp\": -2.259, \"std_gap_pp\": 0.671}, \"alignment_correction\": {\"conclusion\": \"Proper item-ID alignment changes result by <0.3pp vs naive positional comparison\", \"misaligned_vs_aligned_diff_pp\": \"<0.3 (confirmed from prior 2-pair check)\"}, \"by_contamination\": {\"d000\": {\"mean_pp\": -2.292, \"n\": 5}, \"d005\": {\"mean_pp\": -2.181, \"n\": 6}, \"d025\": {\"mean_pp\": -1.913, \"n\": 5}, \"d100\": {\"mean_pp\": -2.687, \"n\": 4}}, \"by_size\": {\"0.5B\": {\"mean_pp\": -2.259, \"n\": 4, \"std_pp\": 1.238}, \"1.5B\": {\"mean_pp\": -2.452, \"n\": 8, \"std_pp\": 0.31}, \"3B\": {\"mean_pp\": -2.026, \"n\": 8, \"std_pp\": 0.415}}, \"n_common_items\": 6596, \"n_pairs\": 20, \"per_item\": {\"mean_disagree_rate_pct\": 15.5, \"n_flagged_items\": 426, \"pct_aligned_easier\": 6.6, \"pct_high_disagree_gt50\": 6.5, \"pct_neutral_lt03pp\": 84.8, \"pct_para_easier\": 8.6}, \"prior_2pair_check\": {\"15B_d100\": {\"aligned_gap_pp\": -2.9, \"qc_selection_bias_pp\": 0.56}, \"3B_d100\": {\"aligned_gap_pp\": -3.5, \"qc_selection_bias_pp\": -0.08}}}}, \"exp_001_eval_3B_d025_s42_a32_para\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_para\": 0.8106, \"gsm8k_para\": \"completed\", \"humaneval_para\": 0, \"mmlu_para\": \"completed_6596_items\", \"output_dir\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v3_s42_para_aligned\", \"sentinel\": \".done exists\"}}, \"exp_002_signals_3B_d025_v3_s42\": {\"conclusion\": \"success\"}, \"exp_002_signals_3B_v9\": {\"conclusion\": \"failed\"}, \"exp_001_sft_3B_d025_s42_a32_v3\": {\"conclusion\": \"killed\"}, \"exp_001_eval_3B_d025_v3_s42_batch\": {\"conclusion\": \"killed\"}, \"exp_002_signals_05B_s123_batch\": {\"conclusion\": \"failed\"}, \"exp_002_signals_3B_v7\": {\"conclusion\": \"success\", \"metrics\": {\"benchmarks\": [\"mmlu\", \"gsm8k\", \"arc_challenge\"], \"merged_files\": 3, \"output_dir\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s123/\", \"signal_files\": 9, \"signals\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]}}, \"exp_001_sft_3B_d100_s42_a32_v3\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.296, \"final_epoch\": 1, \"mean_token_accuracy\": 0.7186, \"total_steps\": 4159, \"train_loss\": 1.1795, \"train_runtime_sec\": 17645, \"train_samples_per_second\": 3.771, \"train_steps_per_second\": 0.236}}, \"exp_001_sft_3B_d005_s42_a32\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"final_loss\": 1.0822, \"mean_token_accuracy\": 0.7511, \"steps\": 3177, \"train_runtime_sec\": 14913.5}}, \"exp_002_signals_3B_v8_recovery\": {\"conclusion\": \"failed\"}, \"exp_004_sim_sweep_v7\": {\"conclusion\": \"success\", \"metrics\": {\"ci95_coverage_range\": \"[0.8, 1.0]\", \"conditions_failed\": \"auc0.65_n20/n50/n100 (CmdStan TMPDIR race)\", \"conditions_ok\": 9, \"conditions_total\": 12, \"gamma_bias_range\": \"[-0.025, +0.056]\", \"gamma_rmse_range\": \"[0.005, 0.085]\", \"note\": \"9/12 sufficient for Claim 1 identifiability\", \"theta_corr_range\": \"[0.947, 0.972]\"}}, \"exp_001_sft_3B_d000_s42_a32\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"final_loss\": 1.1324, \"steps\": 3125}}, \"exp_002_signals_3B_v8\": {\"conclusion\": \"failed\"}, \"exp_002_signals_3B_v5\": {\"conclusion\": \"failed\"}, \"exp_001_sft_3B_d025_s42_a32_v2\": {\"conclusion\": \"failed\"}, \"exp_001_eval_15B_s123_para_aligned_batch\": {\"conclusion\": \"success\", \"metrics\": {\"d000_s123_para_aligned\": {\"arc_challenge\": 0.7547, \"gsm8k\": 0.5921, \"humaneval\": 0.1538, \"mmlu\": 0.6111}, \"d005_s123_para_aligned\": {\"arc_challenge\": 0.7475, \"gsm8k\": 0.5439, \"humaneval\": 0.0769, \"mmlu\": 0.614}, \"d025_s123_para_aligned\": {\"arc_challenge\": 0.7504, \"gsm8k\": 0.5482, \"humaneval\": 0.1923, \"mmlu\": 0.6145}, \"d100_s123_para_aligned\": {\"arc_challenge\": 0.7834, \"gsm8k\": 0.5307, \"humaneval\": 0.2308, \"mmlu\": 0.629}}}, \"exp_001_sft_3B_d100_s42_a32_v2\": {\"conclusion\": \"failed\"}, \"exp_001_sft_3B_d025_s42_a32\": {\"conclusion\": \"killed\"}, \"exp_001_sft_3B_d100_s42_a32\": {\"conclusion\": \"killed\"}, \"exp_001_sft_d025_3B_v3\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.1807, \"epoch\": 1, \"mean_token_accuracy\": 0.734, \"total_steps\": 3384, \"train_loss\": 1.1464, \"train_runtime_s\": 14584}}, \"exp_002_signals_3B_v6\": {\"conclusion\": \"failed\"}, \"exp_001_sft_d005_3B\": {\"conclusion\": \"success\", \"metrics\": {\"epochs\": 1, \"final_loss\": 1.11, \"total_steps\": 3177, \"training_hours\": 3.76}}, \"exp_002_signals_3B_v4\": {\"conclusion\": \"failed\"}, \"exp_004_sim_sweep_extreme_gamma\": {\"conclusion\": \"success\", \"metrics\": {\"conditions\": 8, \"gamma2_avg_bias\": 0.017, \"gamma2_avg_rmse\": 0.101, \"gamma2_ci95_coverage\": 1, \"gamma4_avg_bias\": -0.106, \"gamma4_avg_rmse\": 0.226, \"gamma4_ci95_coverage\": 0.925, \"seeds_per_condition\": 10, \"theta_corr_range\": [0.914, 0.969], \"total_time_hours\": 11.1}}, \"exp_001_eval_3B_d100_s123_para_aligned_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.8164, \"correct\": 569, \"total\": 697}, \"gsm8k\": {\"accuracy\": 0.5877, \"correct\": 134, \"total\": 228}, \"humaneval\": {\"correct\": 2, \"pass@1\": 0.0769, \"total\": 26}, \"mmlu\": {\"accuracy\": 0.6565, \"correct\": 4330, \"total\": 6596}}}, \"exp_001_eval_3B_d100_s123_para_aligned\": {\"conclusion\": \"failed\"}, \"exp_001_sft_3B_d000_v3\": {\"conclusion\": \"failed\"}, \"exp_004_sim_sweep_v6\": {\"conclusion\": \"killed\"}, \"exp_002_signals_3B_v3\": {\"conclusion\": \"killed\"}, \"exp_001_eval_3B_d005_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.8242, \"gsm8k_exact_match\": 0.6308, \"humaneval_pass1\": 0.1037, \"mmlu_accuracy\": 0.6324}}, \"exp_001_eval_3B_d025_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.8336, \"gsm8k\": 0.5254, \"humaneval\": 0.1585, \"mmlu\": 0.6367}}, \"exp_002_signals_3B_v2\": {\"conclusion\": \"killed\"}, \"exp_001_eval_3B_d005_s123_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"ARC\": 0.8192, \"GSM8K\": 0.5, \"HumanEval\": 0.0769, \"MMLU\": 0.6461}}, \"exp_001_eval_15B_d005_s123\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.7568, \"correct\": 887, \"total\": 1172}, \"gsm8k\": {\"correct\": 855, \"exact_match\": 0.6482, \"total\": 1319}, \"humaneval\": {\"correct\": 41, \"pass@1\": 0.25, \"total\": 164}, \"mmlu\": {\"accuracy\": 0.5869, \"correct\": 8241, \"total\": 14042}}}, \"exp_001_eval_15B_d005_s123_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.7568, \"correct\": 887, \"total\": 1172}, \"gsm8k\": {\"correct\": 855, \"exact_match\": 0.6482, \"total\": 1319}, \"humaneval\": {\"correct\": 41, \"pass@1\": 0.25, \"total\": 164}, \"mmlu\": {\"accuracy\": 0.5869, \"correct\": 8241, \"total\": 14042}}}, \"exp_001_eval_15B_d025_s123\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.7577, \"correct\": 888, \"total\": 1172}, \"gsm8k\": {\"correct\": 864, \"exact_match\": 0.655, \"total\": 1319}, \"humaneval\": {\"correct\": 41, \"pass@1\": 0.25, \"total\": 164}, \"mmlu\": {\"accuracy\": 0.5881, \"correct\": 8258, \"total\": 14042}}}, \"exp_001_eval_15B_d025_s123_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.7577, \"correct\": 888, \"total\": 1172}, \"gsm8k\": {\"correct\": 864, \"exact_match\": 0.655, \"total\": 1319}, \"humaneval\": {\"correct\": 41, \"pass@1\": 0.25, \"total\": 164}, \"mmlu\": {\"accuracy\": 0.5881, \"correct\": 8258, \"total\": 14042}}}, \"exp_001_sft_d025_3B_v2\": {\"conclusion\": \"success\", \"metrics\": {\"epochs\": 1, \"mean_token_accuracy\": 0.7342, \"runtime_seconds\": 14499, \"steps\": 3384, \"train_loss\": 1.1501}}, \"exp_001_sft_d100_3B_v2\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter\", \"d020_params\": \"lr=5e-5, alpha=16, r=16\", \"status\": \"training_complete\", \"steps\": \"4159/4159\"}}, \"exp_001_sft_3B_d000_v2\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter\", \"completed_at\": \"2026-05-15T03:45Z\", \"status\": \"training_complete\"}}, \"exp_002_signals_3B\": {\"conclusion\": \"failed\"}, \"exp_001_eval_3B_d000_s42_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.8235, \"correct\": 574, \"total\": 697}, \"gsm8k\": {\"accuracy\": 0.0482, \"correct\": 11, \"total\": 228}, \"humaneval\": {\"correct\": 3, \"pass@1\": 0.1154, \"total\": 26}, \"mmlu\": {\"accuracy\": 0.6474, \"correct\": 4270, \"total\": 6596}}}, \"exp_001_eval_3B_d100_s42_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.8092, \"correct\": 564, \"total\": 697}, \"gsm8k\": {\"accuracy\": 0.5833, \"correct\": 133, \"total\": 228}, \"humaneval\": {\"correct\": 3, \"pass@1\": 0.1154, \"total\": 26}, \"mmlu\": {\"accuracy\": 0.659, \"correct\": 4347, \"total\": 6596}}}, \"exp_001_sft_3B_d005_s123\": {\"conclusion\": \"success\", \"metrics\": {\"final_loss\": 1.1349, \"final_token_accuracy\": 0.7069, \"total_steps\": 3177}}, \"exp_001_sft_3B_d025_s123\": {\"conclusion\": \"success\", \"metrics\": {\"final_loss\": 1.1401, \"final_token_accuracy\": 0.734, \"total_steps\": 3384}}, \"exp_001_eval_3B_d000_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.8328, \"gsm8k\": 0.1812, \"humaneval\": 0.0854, \"mmlu\": 0.6332}}, \"exp_001_eval_3B_d005_s42_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.8294, \"gsm8k\": 0.2077, \"humaneval\": 0.1463, \"mmlu\": 0.6345}}, \"exp_008_base_pretrained_eval_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.2278, \"gsm8k\": 0.163, \"humaneval\": 0, \"mmlu\": 0.2294}}, \"exp_001_sft_15B_d025_s123_v2\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.7466, \"train_loss\": 1.2723}}, \"exp_001_sft_15B_d005_s123_v2\": {\"conclusion\": \"success\", \"metrics\": {\"mean_token_accuracy\": 0.6855, \"train_loss\": 1.2639}}, \"exp_008_base_pretrained_15B_eval_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.2304, \"arc_correct\": 270, \"arc_total\": 1172, \"gsm8k\": 0.0053, \"gsm8k_correct\": 7, \"gsm8k_total\": 1319, \"humaneval_correct\": 38, \"humaneval_pass1\": 0.2317, \"humaneval_total\": 164, \"mmlu\": 0.2303, \"mmlu_correct\": 3234, \"mmlu_total\": 14042}}, \"exp_008_base_pretrained_15B_eval\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.2304, \"arc_correct\": 270, \"arc_total\": 1172, \"gsm8k_accuracy\": 0.0053, \"gsm8k_correct\": 7, \"gsm8k_total\": 1319, \"humaneval_correct\": 38, \"humaneval_pass@1\": 0.2317, \"humaneval_total\": 164, \"mmlu_accuracy\": 0.2303, \"mmlu_correct\": 3234, \"mmlu_total\": 14042}}, \"exp_008_base_pretrained_eval\": {\"conclusion\": \"failed\"}, \"exp_001_eval_15B_d000_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.7577, \"gsm8k_accuracy\": 0.6535, \"humaneval_pass@1\": 0.1707, \"mmlu_accuracy\": 0.5855}}, \"exp_001_eval_15B_d100_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.7816, \"gsm8k_accuracy\": 0.6444, \"humaneval_pass@1\": 0.2805, \"mmlu_accuracy\": 0.5956}}, \"exp_001_eval_05B_d000_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.4974, \"gsm8k\": 0.3412, \"humaneval\": 0.1037, \"mmlu\": 0.4216}}, \"exp_001_eval_3B_d000_s42_v3\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.8276, \"gsm8k\": 0.1198, \"humaneval\": 0.1159, \"mmlu\": 0.634}}, \"exp006-s1only-gsm8k-2pl\": {\"conclusion\": \"success\", \"metrics\": {\"ci_excludes_zero\": false, \"divergent_count\": 0, \"gamma_ci95\": [-0.306, 0.591], \"gamma_mean\": 0.1389, \"gamma_sd\": 0.2274, \"max_rhat\": 1.0024, \"min_ess\": 3604.4, \"obs_mean_acc\": 0.5086, \"ppp\": 0.2835, \"pred_mean_acc\": 0.5011, \"residual_mae\": 0.0083}}, \"exp_001_eval_3B_d000_v2_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.8259, \"gsm8k\": 0.2676, \"humaneval\": 0.061, \"mmlu\": 0.6314}}, \"exp_001_eval_3B_d025_v2_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.8276, \"gsm8k\": 0.6793, \"humaneval\": 0.0976, \"mmlu\": 0.5998}}, \"exp_001_eval_3B_d100_v2_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.8311, \"gsm8k\": 0.7324, \"humaneval\": 0.1829, \"mmlu\": 0.6319}}, \"exp_001_sft_15B_d005_s123\": {\"conclusion\": \"failed\"}, \"exp_001_eval_05B_d025_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.4061, \"correct\": 476, \"total\": 1172}, \"gsm8k\": {\"accuracy\": 0.3533, \"correct\": 466, \"total\": 1319}, \"humaneval\": {\"correct\": 14, \"pass@1\": 0.0854, \"total\": 164}, \"mmlu\": {\"accuracy\": 0.3473, \"correct\": 4877, \"total\": 14042}}}, \"exp_001_sft_05B_d025_s123_v2\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.697, \"epoch\": 1, \"global_steps\": 3384, \"runtime_seconds\": 5930, \"train_loss\": 1.548}}, \"exp_001_eval_05B_d000_s42_v7\": {\"conclusion\": \"failed\"}, \"exp_004_sim_sweep_v5\": {\"conclusion\": \"failed\", \"metrics\": {\"conditions_all_failed\": [\"auc0.65_n20 (0/10)\", \"auc0.65_n50 (0/7)\"], \"conditions_complete\": 4, \"conditions_fully_ok\": [\"auc0.55_n20 (10/10)\", \"auc0.55_n50 (10/10)\", \"auc0.8_n20 (10/10)\", \"auc0.8_n50 (10/10)\"], \"conditions_missing\": 3, \"conditions_never_started\": [\"auc0.65_n100\", \"auc0.9_n50\", \"auc0.9_n100\"], \"conditions_partial\": 5, \"conditions_partial_ok\": [\"auc0.55_n100 (7/10)\", \"auc0.8_n100 (6/10)\", \"auc0.9_n20 (6/10)\"], \"failure_cause\": \"Disk quota exceeded ([Errno 122]) - root partition /tmp filled by CmdStan temp files\", \"seeds_attempted\": 97, \"seeds_ok\": 59, \"seeds_total\": 120}}, \"exp006-oracle-arc-4pl-pooled\": {\"conclusion\": \"failed\"}, \"exp_008_instruct_05B_eval\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.2816, \"gsm8k_accuracy\": 0.3882, \"humaneval_pass@1\": 0, \"mmlu_accuracy\": 0.2462}}, \"exp_001_eval_3B_d100_v2_aligned_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.8242, \"gsm8k_accuracy\": 0.7415, \"humaneval_pass@1\": 0.1707, \"mmlu_accuracy\": 0.632}}, \"exp_001_eval_3B_d025_v2_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_para_accuracy\": 0.8106, \"gsm8k_para_accuracy\": 0.5482, \"humaneval_para_pass@1\": 0.1154, \"mmlu_para_accuracy\": 0.621}}, \"exp_001_sft_3B_d100_s123\": {\"conclusion\": \"success\", \"metrics\": {\"epochs\": 1, \"mean_token_accuracy\": 0.7343, \"runtime_seconds\": 18252, \"steps\": 4159, \"train_loss\": 1.1846}}, \"exp006-oracle-arc-2pl\": {\"conclusion\": \"success\", \"metrics\": {\"C95_coverage\": 0.1818, \"ESS\": 1512, \"MAE\": 0.0759, \"gamma\": -0.618, \"gamma_ci\": [-1.04, -0.2], \"rhat\": 1.006}}, \"exp_001_eval_3B_d000_v2_s123_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_para_accuracy\": 0.8121, \"gsm8k_para_accuracy\": 0.1491, \"humaneval_para_pass@1\": 0.0385, \"mmlu_para_accuracy\": 0.6512}}, \"exp006-pooled-s1only-gsm8k-v2\": {\"conclusion\": \"success\", \"metrics\": {\"diagnostics_ok\": false, \"divergent_pct\": 0, \"ess_min\": 330.2, \"fit_time_sec\": 336.9, \"gamma\": 0.1871, \"gamma_ci_excludes_zero\": false, \"gamma_ci_lower\": -0.9172, \"gamma_ci_upper\": 1.3294, \"gamma_sd\": 0.5687, \"n_items\": 1319, \"n_models\": 8, \"note\": \"No evaluation/baselines files generated; only IRT fit available. rhat and ESS did not pass thresholds.\", \"ppp\": 0.336, \"residual_mae\": 0.0367, \"rhat_max\": 1.0148}}, \"exp006-pooled-s1only-arc\": {\"conclusion\": \"success\", \"metrics\": {\"baselines\": {\"B0_raw_mae\": 0.0588, \"B1_remove_rescore_mae\": 0.0588, \"B2_2pl_gamma_mae\": 0.064, \"B3_vanilla_4pl_mae\": 0.0706, \"B4_linear_regression_mae\": 0.0562, \"B5_emperor_mae\": 0.0588, \"B6_dcr_fuzzy_mae\": 0.2454}, \"brier\": 0.0018, \"coverage_50\": 0, \"coverage_80\": 0.25, \"coverage_95\": 0.625, \"divergent_pct\": 0, \"ece\": 0.0319, \"ess_min\": 769.6, \"fit_time_sec\": 317.7, \"gamma\": -1.4637, \"gamma_ci_excludes_zero\": true, \"gamma_ci_lower\": -2.51, \"gamma_ci_upper\": -0.4051, \"gamma_sd\": 0.5276, \"kendall_tau\": 0.7559, \"mae\": 0.0347, \"n_items\": 1172, \"n_models\": 8, \"ppp\": 0.9677, \"rhat_max\": 1.0098, \"sharpness_95\": 0.0684}}, \"exp006-oracle-gsm8k-extended-v2\": {\"conclusion\": \"success\", \"metrics\": {\"baselines\": {\"B0_raw_mae\": 0.005, \"B4_linear_regression_mae\": 0.008, \"B5_emperor_mae\": 0.005, \"B6_dcr_fuzzy_mae\": 0.138}, \"coverage_50\": 0.25, \"coverage_80\": 0.25, \"coverage_95\": 0.31, \"divergent_pct\": 0, \"ece\": 0.0894, \"ess_min\": 1221.9, \"fit_time_sec\": 6240.3, \"gamma\": 3.773, \"gamma_ci_excludes_zero\": true, \"gamma_ci_lower\": 2.741, \"gamma_ci_upper\": 4.714, \"gamma_sd\": 0.504, \"kendall_tau\": 0.505, \"mae\": 0.0917, \"n_items\": 1319, \"n_models\": 16, \"ppp\": 0, \"rhat_max\": 1.002}}, \"exp_001_sft_05B_d025_s123\": {\"conclusion\": \"killed\"}, \"exp_001_eval_05B_d005_s123_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_para_accuracy\": 0.2912, \"gsm8k_para_accuracy\": 0.2939, \"humaneval_para_pass@1\": 0, \"mmlu_para_accuracy\": 0.3166}}, \"exp_001_eval_05B_d000_s42\": {\"conclusion\": \"failed\"}, \"exp_001_eval_05B_d005_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.2978, \"gsm8k_accuracy\": 0.3677, \"humaneval_pass@1\": 0.0976, \"mmlu_accuracy\": 0.3002}}, \"exp_004_sim_sweep_v4\": {\"conclusion\": \"failed\"}, \"exp_001_sft_3B_d000_s123\": {\"conclusion\": \"success\", \"metrics\": {\"baseline_seed42_train_loss\": 1.1357, \"entropy\": 1.1108, \"epochs\": 1, \"mean_token_accuracy\": 0.748, \"steps\": 3125, \"train_loss\": 1.1361, \"train_runtime_seconds\": 13141.8}}, \"exp_001_eval_3B_d000_v2_para_aligned_v3\": {\"conclusion\": \"failed\"}, \"exp_001_eval_3B_d000_v2_para_aligned_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_para_accuracy\": 0.8121, \"gsm8k_para_accuracy\": 0.2895, \"humaneval_para_pass@1\": 0.0385, \"mmlu_para_accuracy\": 0.6468}}, \"exp006-oracle-gsm8k-extended\": {\"conclusion\": \"failed\"}, \"exp006-pooled-s1only-gsm8k\": {\"conclusion\": \"failed\"}, \"exp_001_eval_3B_d100_v2_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_para\": 0.8092, \"gsm8k_para\": 0.5833, \"humaneval_para_pass1\": 0.1154, \"mmlu_para\": 0.659}}, \"exp_001_sft_05B_d005_s123\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"final_loss\": 1.4542, \"final_token_accuracy\": 0.6794, \"mean_token_accuracy\": 0.6356, \"total_steps\": 3177, \"train_loss\": 1.5422, \"train_runtime_sec\": 3458.58}}, \"exp_001_eval_3B_d000_v2_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.8183, \"gsm8k\": 0.3525, \"humaneval_pass@1\": 0.0976, \"mmlu\": 0.6295}}, \"exp_001_sft_15B_d100_s123\": {\"conclusion\": \"success\", \"metrics\": {\"baseline_seed42_token_accuracy\": 0.7033, \"baseline_seed42_train_loss\": 1.2996, \"entropy\": 1.3327, \"epochs\": 1, \"mean_token_accuracy\": 0.7178, \"num_tokens\": 21575068, \"steps\": 4159, \"train_loss\": 1.3002, \"train_runtime_seconds\": 14663.6}}, \"exp_004_sim_sweep_v3\": {\"conclusion\": \"failed\"}, \"exp_001_eval_3B_d100_v2_aligned\": {\"conclusion\": \"failed\", \"metrics\": {\"INVALID\": \"metrics were from v1 exp_001_eval_3B_d100_aligned, not v2. v2 output dir was empty. PID 461879 died before completion.\"}}, \"exp_001_sft_d025_3B\": {\"conclusion\": \"failed\"}, \"exp_001_eval_05B_d100_s123_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.3669, \"arc_challenge_correct\": 430, \"arc_challenge_total\": 1172, \"gsm8k_accuracy\": 0.3798, \"gsm8k_correct\": 501, \"gsm8k_total\": 1319, \"humaneval_pass_at_1\": 0.1037, \"humaneval_total\": 164, \"mmlu_accuracy\": 0.3058, \"mmlu_correct\": 4294, \"mmlu_total\": 14042}}, \"exp_001_eval_3B_d000_v2_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"format\": \"paraphrased_aligned\", \"mmlu_para\": 0.6468}}, \"exp006-pooled-05B-15B-mmlu-v2\": {\"conclusion\": \"failed\", \"metrics\": {\"NOTE\": \"fit completely failed, not reportable\", \"convergence\": \"FAILED (rhat=1.54, ess=7)\", \"coverage_95\": 1, \"exposure_source\": \"signal_rrf\", \"gamma_joint\": -0.2095, \"gamma_joint_ci\": [-1.01, 0.59], \"gamma_perbench\": -3.8073, \"gamma_perbench_ci\": [-7.02, 3.22], \"mae\": 0.099, \"n_models\": 8, \"ppp\": 0.75}}, \"exp006-pooled-05B-15B-arc-v2\": {\"conclusion\": \"success\", \"metrics\": {\"NOTE\": \"coverage below 95%; no oracle baseline exists\", \"convergence\": \"OK\", \"coverage_95\": 0.625, \"exposure_source\": \"signal_rrf\", \"gamma_joint\": -1.4637, \"gamma_joint_ci\": [-2.51, -0.41], \"gamma_perbench\": -2.3471, \"gamma_perbench_ci\": [-3.46, -1.19], \"mae\": 0.035, \"n_models\": 8, \"ppp\": 0.999}}, \"exp_005_noise_prop\": {\"conclusion\": \"failed\"}, \"exp_004_sim_sweep\": {\"conclusion\": \"failed\"}, \"exp002-signals-1p5B\": {\"conclusion\": \"success\"}, \"exp_004_sim_sweep_v2\": {\"conclusion\": \"failed\", \"metrics\": {\"auc080_n100_bias\": 0.008, \"auc080_n100_ci_width\": 0.116, \"auc080_n100_gamma_hat\": 0.508, \"auc080_n100_theta_corr\": 0.962, \"auc080_n50_bias\": 0.006, \"auc080_n50_ci95_coverage\": 1, \"auc080_n50_rmse\": 0.03, \"ci_width_ratio_n100\": 1.81, \"core_findings_stable\": true, \"runs_completed\": 48, \"runs_total\": 120}}, \"exp_005_noise_prop_v3\": {\"conclusion\": \"failed\"}, \"exp_001_sft_05B_d100_s123\": {\"conclusion\": \"success\"}, \"exp002-signal-d025-05B\": {\"conclusion\": \"success\"}, \"exp_001_eval_05B_d025_aligned_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.3199, \"format\": \"paraphrased_aligned\", \"gsm8k\": 0.3114, \"humaneval_pass1\": 0.1923, \"mmlu\": 0.2835}}, \"exp_006_irt_05B_arc\": {\"conclusion\": \"success\", \"metrics\": {\"fit_type\": \"joint\", \"gamma\": -1.21, \"gamma_ci_lower\": -2.53, \"gamma_ci_upper\": 0.12}}, \"exp_001_eval_15B_d025_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.7688, \"gsm8k\": 0.6535, \"humaneval_pass1\": 0.2256, \"mmlu\": 0.5902}}, \"exp_001_eval_05B_d005_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.33, \"arc_correct\": 230, \"arc_total\": 697, \"gsm8k\": 0.2588, \"gsm8k_correct\": 59, \"gsm8k_total\": 228, \"humaneval\": 0, \"humaneval_correct\": 0, \"humaneval_total\": 26, \"mmlu\": 0.3548, \"mmlu_correct\": 2340, \"mmlu_total\": 6596}}, \"exp_001_eval_15B_d025_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.766, \"gsm8k\": 0.539, \"humaneval\": 0.154, \"mmlu\": 0.618}}, \"exp_001_eval_3B_d100_para_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.828, \"gsm8k\": 0.614, \"mmlu\": 0.676}}, \"exp_006_pooled_gsm8k_v1\": {\"conclusion\": \"failed\"}, \"exp_001_eval_15B_aligned_batch\": {\"conclusion\": \"success\", \"metrics\": {\"arc\": {\"d000_orig\": 0.7722, \"d000_para\": 0.7547, \"d005_orig\": 0.7688, \"d005_para\": 0.7532, \"d100_orig\": 0.7688, \"d100_para\": 0.7661}, \"gsm8k\": {\"d000_orig\": 0.6543, \"d000_para\": 0.557, \"d005_orig\": 0.6482, \"d005_para\": 0.5439, \"d100_orig\": 0.6497, \"d100_para\": 0.5526}, \"humaneval\": {\"d000_orig\": 0.128, \"d000_para\": 0.0385, \"d005_orig\": 0.25, \"d005_para\": 0.1923, \"d100_orig\": 0.3049, \"d100_para\": 0.2692}, \"key_finding\": \"MC benchmarks fail to detect contamination at 1.5B scale (<1pp). HumanEval shows strong dose-response (+17.69pp). Paraphrase gap does not cleanly separate contamination.\", \"mmlu\": {\"d000_orig\": 0.5853, \"d000_para\": 0.6096, \"d005_orig\": 0.5852, \"d005_para\": 0.6164, \"d100_orig\": 0.5933, \"d100_para\": 0.6252}}}, \"exp_006_irt_05B_gsm8k\": {\"conclusion\": \"success\", \"metrics\": {\"baselines_mae\": {\"B0_raw\": 0.0034, \"B2_2pl_gamma\": 0.3202, \"B3_vanilla_4pl\": 0.0123, \"B4_linear_regression\": 0.003, \"B6_dcr_fuzzy\": 0.2634, \"IRT_4pl_gamma\": 0.0195}, \"delta_fix_applied\": true, \"joint_divergences\": 0, \"joint_ess\": 956.4, \"joint_gamma\": 0.3463, \"joint_gamma_ci\": [-0.65, 1.4], \"joint_rhat\": 1.0081, \"perbench_divergences\": 0, \"perbench_ess\": 522.2, \"perbench_gamma\": 0.508, \"perbench_gamma_ci\": [-0.64, 1.84], \"perbench_rhat\": 1.0096, \"signal_scores_after_delta\": [0, 0.016, 0.065, 0.197]}}, \"exp_001_eval_15B_d100_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.7688, \"gsm8k_accuracy\": 0.6497, \"humaneval_correct\": 50, \"humaneval_pass_rate\": 0.3049, \"humaneval_total\": 164, \"mmlu_accuracy\": 0.5933}}, \"exp_001_eval_15B_d005_aligned_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.7688, \"gsm8k\": 0.6482, \"humaneval_pass_at_1\": 0.25, \"mmlu\": 0.5852}}, \"exp_001_sft_d100_3B\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"runtime_hours\": 5.2, \"steps\": \"4159/4159\", \"token_accuracy\": 0.7206, \"train_loss\": 1.178}}, \"exp_001_eval_05B_d100_aligned_v4\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.2944, \"arc_delta_vs_d000\": -0.1749, \"gsm8k\": 0.3654, \"humaneval_delta_vs_d000\": -0.1098, \"humaneval_pass_at_1\": 0, \"mmlu\": 0.2334, \"mmlu_delta_vs_d000\": -0.1645}}, \"exp_001_sft_d025_15B\": {\"conclusion\": \"success\", \"metrics\": {\"entropy\": 1.2623, \"epochs\": 1, \"mean_token_accuracy\": 0.7192, \"steps\": 3384, \"train_loss\": 1.2715, \"train_runtime_seconds\": 11610.6}}, \"exp_001_eval_3B_d005_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.829, \"gsm8k\": 0.208, \"humaneval_pass_at_1\": 0.146, \"mmlu\": 0.634}}, \"exp_006_irt_05B_v1\": {\"conclusion\": \"failed\"}, \"exp_001_eval_05B_d025_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"ARC\": 32.51, \"GSM8K\": 36.62, \"HumanEval\": \"missing - process exited before 4th benchmark\", \"MMLU\": 28.03}}, \"exp_008_signal_survival_v4\": {\"conclusion\": \"success\", \"metrics\": {\"S1_d005_auc_mean\": 0.979, \"S1_d100_cross_cohens_d_mean\": 3.6, \"S2_d005_auc_mean\": 0.465, \"S2_d100_cross_cohens_d_mean\": -1.98, \"S4_d005_auc_mean\": 0.481, \"S4_d100_cross_cohens_d_mean\": 0.45, \"d021_fix\": \"within-model AUC only for d005; d100 uses cross-model Cohen's d\", \"effective_signals_at_05B\": 1}}, \"exp_001_eval_05B_d100_aligned_v3\": {\"conclusion\": \"failed\"}, \"exp_008_signal_survival\": {\"conclusion\": \"success\", \"metrics\": {\"S1_d000_arc\": 0.427, \"S1_d000_gsm8k\": 0.5502, \"S1_d000_mmlu\": 0.5049, \"S1_d005_arc\": 0.995, \"S1_d005_gsm8k\": 0.9882, \"S1_d005_mmlu\": 0.953, \"S1_d100_arc\": 0.501, \"S1_d100_gsm8k\": 0.4127, \"S1_d100_mmlu\": 0.4943, \"S2_d005_arc\": 0.4659, \"S2_d005_gsm8k\": 0.4649, \"S2_d005_mmlu\": 0.4655, \"S4_d005_arc\": 0.4325, \"S4_d005_gsm8k\": 0.4947, \"S4_d005_mmlu\": 0.5165, \"signals_surviving\": 0, \"signals_total\": 3}}, \"exp_001_eval_3B_d100_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.8396, \"gsm8k_exact_match\": 0.6967, \"humaneval_pass1\": 0.122, \"mmlu_accuracy\": 0.6417}}, \"exp_001_eval_05B_d005_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"d005_aligned_arc\": 0.3285, \"d005_aligned_gsm8k\": 0.3624, \"d005_aligned_humaneval\": 0.0793, \"d005_aligned_mmlu\": 0.3255}}, \"exp_001_eval_05B_d100_aligned\": {\"conclusion\": \"failed\"}, \"exp_001_eval_05B_aligned_batch\": {\"conclusion\": \"failed\", \"metrics\": {\"d000_aligned_arc\": 0.4693, \"d000_aligned_gsm8k\": 0.3692, \"d000_aligned_humaneval\": 0.1098, \"d000_aligned_mmlu\": 0.3979, \"d000_para_aligned_arc\": 0.4792, \"d000_para_aligned_gsm8k\": 0.2807, \"d000_para_aligned_humaneval\": 0.1154, \"d000_para_aligned_mmlu\": 0.4428, \"d005_aligned_arc\": 0.3285, \"d005_aligned_gsm8k\": 0.3624, \"d005_aligned_humaneval\": 0.0793, \"d005_aligned_mmlu\": 0.3255}}, \"exp_001_eval_05B_d005\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.2858, \"arc_correct\": 335, \"arc_total\": 1172, \"gsm8k\": 0.3601, \"gsm8k_correct\": 475, \"gsm8k_total\": 1319, \"humaneval_correct\": 13, \"humaneval_pass1\": 0.0793, \"humaneval_total\": 164, \"mmlu\": 0.2929, \"mmlu_correct\": 4113, \"mmlu_total\": 14042}}, \"exp_006_irt_05B\": {\"conclusion\": \"killed\"}, \"exp_003_rrf_05B\": {\"conclusion\": \"success\"}, \"exp_002_signals_05B\": {\"conclusion\": \"success\"}, \"exp_001_eval_3B_d000_aligned\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.8276, \"gsm8k_exact_match\": 0.1198, \"humaneval_pass_at_1\": 0.1159, \"mmlu_accuracy\": 0.634}}, \"exp_001_eval_15B_d100_s42\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.7688, \"arc_challenge_correct\": 901, \"arc_challenge_total\": 1172, \"gsm8k_correct\": 857, \"gsm8k_exact_match\": 0.6497, \"gsm8k_total\": 1319, \"humaneval_correct\": 50, \"humaneval_pass_at_1\": 0.3049, \"humaneval_total\": 164, \"mmlu_accuracy\": 0.5933, \"mmlu_correct\": 8331, \"mmlu_total\": 14042}}, \"exp_001_eval_3B_raw_gen\": {\"conclusion\": \"success\", \"metrics\": {\"gsm8k\": 0.605, \"humaneval\": 0}}, \"exp_001_eval_05B_raw\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.2261, \"gsm8k\": 0.1592, \"humaneval\": \"incomplete (hung at 51/164)\", \"mmlu\": 0.2302}}, \"exp_001_sft_d005_15B\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 1, \"mean_token_accuracy\": 0.7308, \"train_loss\": 1.2637, \"train_runtime_s\": 19864.7}}, \"exp_001_sft_d025_05B_v3\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_size_mb\": 166, \"entropy\": 1.5415, \"epoch\": 1, \"exit_code\": 0, \"final_loss\": 1.5178, \"lora_adapter_size_mb\": 33.6, \"mean_token_accuracy\": 0.6697, \"mean_train_loss\": 1.5479, \"num_tokens\": 20058085, \"total_steps\": 3384, \"train_samples_per_second\": 15.52, \"train_steps_per_second\": 0.97, \"training_time_min\": 58.1, \"vs_baseline_0pct\": {\"baseline_final_loss\": 1.4894, \"baseline_mean_train_loss\": 1.5388, \"baseline_token_accuracy\": 0.682, \"baseline_training_time_min\": 52.9, \"delta_final_loss\": 0.0284, \"delta_mean_train_loss\": 0.0091, \"delta_token_accuracy\": -0.0123, \"delta_training_time_min\": 5.2}}}, \"exp_001_eval_05B_d100_v5\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.227, \"gsm8k\": 0.3571, \"humaneval_pass1\": 0.0854, \"mmlu\": 0.2322}}, \"exp_001_eval_05B_d000_s42_v5\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.378, \"gsm8k\": 0.3647, \"humaneval\": 0.1098, \"mmlu\": 0.4049}}, \"exp_001_sft_d100_15B_v2\": {\"conclusion\": \"success\"}, \"exp_001_eval_3B_d000_s42\": {\"conclusion\": \"success\", \"metrics\": {\"arc\": 0.822, \"gsm8k\": 0.117, \"humaneval\": 0.116, \"mmlu\": 0.634}}, \"exp_001_sft_d025_05B_v2\": {\"conclusion\": \"failed\"}, \"exp_001_eval_05B_d100_v2\": {\"conclusion\": \"failed\"}, \"exp_001_sft_d025_05B\": {\"conclusion\": \"failed\"}, \"exp_001_eval_3B_d000_s123\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.8294, \"gsm8k_exact_match\": 0.1759, \"humaneval_pass_at_1\": 0.0854, \"mmlu_accuracy\": 0.6362}}, \"exp_001_eval_15B_d000_s123\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge\": 0.7662, \"gsm8k\": 0.6331, \"humaneval_pass@1\": 0.1707, \"mmlu\": 0.5762}}, \"exp_005_noise_prop_v2\": {\"conclusion\": \"failed\"}, \"exp_001_eval_15B_d000_s42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.7756, \"arc_challenge_correct\": 909, \"arc_challenge_total\": 1172, \"gsm8k_correct\": 840, \"gsm8k_exact_match\": 0.6368, \"gsm8k_total\": 1319, \"humaneval_correct\": 21, \"humaneval_pass_at_1\": 0.128, \"humaneval_total\": 164, \"mmlu_accuracy\": 0.5753, \"mmlu_correct\": 8079, \"mmlu_total\": 14042}}, \"exp_001_eval_05B_d100\": {\"conclusion\": \"failed\"}, \"exp_001_eval_05B_d000_s123\": {\"conclusion\": \"success\", \"metrics\": {\"arc_challenge_accuracy\": 0.3976, \"gsm8k_exact_match\": 0.3404, \"humaneval_pass_at_1\": 0.1037, \"mmlu_accuracy\": 0.4182}}, \"exp_001_sft_d100_15B\": {\"conclusion\": \"failed\"}, \"exp_001_sft_d005_05B_v3\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_size_mb\": 166, \"entropy\": 1.5874, \"epoch\": 1, \"exit_code\": 0, \"final_loss\": 1.478, \"lora_adapter_size_mb\": 33.6, \"mean_train_loss\": 1.5424, \"num_tokens\": 19657865, \"token_accuracy\": 0.667, \"total_steps\": 3177, \"train_samples_per_second\": 15.09, \"train_steps_per_second\": 0.943, \"training_time_min\": 56.14, \"vs_baseline_0pct\": {\"baseline_final_loss\": 1.4894, \"baseline_mean_train_loss\": 1.5388, \"baseline_token_accuracy\": 0.682, \"baseline_training_time_min\": 52.9, \"delta_final_loss\": -0.0114, \"delta_mean_train_loss\": 0.0036, \"delta_token_accuracy\": -0.015, \"delta_training_time_min\": 3.24}}}, \"exp_001_sft_d100_05B\": {\"conclusion\": \"success\", \"metrics\": {\"exit_code\": 0, \"final_loss\": 1.5943, \"mean_train_loss\": 1.5662, \"num_tokens\": 21575068, \"token_accuracy\": 0.666, \"total_steps\": 4160, \"train_samples_per_second\": 16.09, \"train_steps_per_second\": 1.006, \"training_time_min\": 68.9, \"vs_baseline_0pct\": {\"accuracy_delta\": \"-0.016 (-2.3%)\", \"loss_delta\": \"+0.0274 (+1.8%)\", \"time_delta\": \"+16min (+30%)\"}}}, \"exp_001_sft_0pct\": {\"conclusion\": \"success\"}, \"exp_001_sft_0pct_3B_s123\": {\"conclusion\": \"success\", \"metrics\": {\"adapter_model_mb\": 114, \"adapter_size_mb\": 488, \"checkpoint_size_mb\": 488, \"epochs\": 1, \"final_loss\": 1.114, \"mean_token_accuracy\": 0.7505, \"mean_train_loss\": 1.1309, \"steps_completed\": 3125, \"total_steps\": 3125, \"total_tokens\": 19555717, \"train_samples_per_second\": 3.91, \"training_time_min\": 213.1}}, \"exp_001_eval_15B_d000_s42\": {\"conclusion\": \"failed\"}, \"exp_001_sft_d005_05B_v2\": {\"conclusion\": \"failed\"}, \"exp_001_sft_d005_05B\": {\"conclusion\": \"killed\"}, \"exp_001_sft_100pct_05B\": {\"conclusion\": \"failed\"}, \"exp_001_sft_0pct_3B\": {\"conclusion\": \"success\", \"metrics\": {\"adapter_size_mb\": 115, \"checkpoint_size_mb\": 488, \"exit_code\": 0, \"final_loss\": 1.0736, \"mean_train_loss\": 1.1306, \"steps\": \"3125/3125\", \"token_accuracy\": 0.734, \"training_time_min\": 214.7}}, \"exp_001_sft_injection\": {\"conclusion\": \"success\", \"metrics\": {\"arc_qc_pass\": 697, \"arc_qc_rate\": 0.595, \"arc_total\": 1172, \"gsm8k_qc_pass\": 228, \"gsm8k_qc_rate\": 0.173, \"gsm8k_total\": 1319, \"humaneval_total\": 164, \"mmlu_qc_pass\": 6596, \"mmlu_qc_rate\": 0.47, \"mmlu_total\": 14042}}, \"exp_001_sft_0pct_15B_s123\": {\"conclusion\": \"success\", \"metrics\": {\"token_acc\": 0.731, \"train_loss\": 1.2602, \"train_time_min\": 101.5}}, \"exp_001_sft_0pct_05B_s123\": {\"conclusion\": \"success\", \"metrics\": {\"token_acc\": 0.676, \"train_loss\": 1.5393, \"train_time_min\": 54.5}}, \"exp_001_sft_0pct_15B\": {\"conclusion\": \"success\", \"metrics\": {\"adapter_size_mb\": 71, \"checkpoint_size_mb\": 313, \"exit_code\": 0, \"final_loss\": 1.2039, \"mean_train_loss\": 1.2599, \"steps\": \"3125/3125\", \"token_accuracy\": 0.711, \"training_time_min\": 101.5}}, \"exp_001_sft_0pct_05B\": {\"conclusion\": \"success\", \"metrics\": {\"adapter_size_mb\": 34, \"checkpoint_size_mb\": 166, \"exit_code\": 0, \"final_loss\": 1.4894, \"mean_train_loss\": 1.5388, \"steps\": \"3125/3125\", \"token_accuracy\": 0.682, \"training_time_min\": 52.9}}, \"mvp_sim_confounding\": {\"conclusion\": \"success\", \"metrics\": {\"actual_confound_corr\": 0.3814, \"divergent_pct\": 0, \"fit_time_sec\": 832, \"gamma_ci_covers_true\": true, \"gamma_ci_excludes_zero\": true, \"gamma_mean\": 0.5386, \"gamma_rel_bias\": 0.0771, \"max_rhat\": 1.007, \"min_ess\": 1371.9, \"overall\": \"PASS\", \"theta_corr\": 0.9733, \"theta_residual_exp_corr\": 0.0582, \"theta_rmse\": 0.2407}}, \"mvp_sim_4pl_gamma\": {\"conclusion\": \"success\", \"metrics\": {\"variant_a_nitems300\": {\"divergent_pct\": 0, \"fit_time_sec\": 1407.5, \"gamma_ci_covers_true\": true, \"gamma_ci_excludes_zero\": true, \"gamma_mean\": 0.466, \"gamma_rel_bias\": 0.068, \"max_rhat\": 1.003, \"overall\": \"PASS\", \"theta_corr\": 0.943, \"theta_rmse\": 0.238}}}}, \"count\": 332, \"total\": 332, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8363}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Bash · `toolu_0125mq93V1h9vSKUen7DW5oC`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/ab87e76a-91c7-436c-9cab-6cfa7abe7e5d/tool-results/mcp-agent-ml-research-read_registry-1779322772038.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n# Find all experiments with qwen7b in name\nfor k, v in exps.items():\n    if 'qwen7b' in k.lower() or ('7b' in k.lower() and 'mmlu' in k.lower()):\n        print(f'{k}: conclusion={v.get(\\\"conclusion\\\",\\\"?\\\")}')\n        m = v.get('metrics', {})\n        if m:\n            # Show just keys\n            print(f'  metrics keys: {list(m.keys())[:20]}')\n        print()\n\"\n",
  "description": "Find all Qwen-7B related experiments in registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "a4da148d-580b-45fc-845d-6ad358ce57e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Auw8tpYzrgQeHzemuYBzuE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 755,
      "cache_read_input_tokens": 81272,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 755
      },
      "output_tokens": 65,
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

_source line 32 · 2026-05-21T00:19:38.059Z_

<details><summary>↩ Tool result · `toolu_0125mq93V1h9vSKUen7DW5oC`</summary>

```text
eval_qwen7b_mmlu_arc_s0: conclusion=success
  metrics keys: ['mmlu', 'arc_challenge']

sft_qwen7b_s0_cqa1: conclusion=success
  metrics keys: ['d000', 'd005', 'd025', 'd050', 'd100']

eval_qwen7b_arc_s42: conclusion=success
  metrics keys: ['arc_challenge_accuracy', 'delta_d100_d000', 'items_per_dosage']

gsm8k_qwen7b_s123_cqa1: conclusion=success
  metrics keys: ['d000_note', 'd100_note', 'gsm8k_d000', 'gsm8k_d100', 'gsm8k_delta']

gsm8k_qwen7b_s42_intermediate_cqa1: conclusion=success
  metrics keys: ['curve_shape', 'delta_d005', 'delta_d025', 'delta_d050', 'delta_d100', 'gsm8k_d000', 'gsm8k_d005', 'gsm8k_d025', 'gsm8k_d050', 'gsm8k_d100']

gsm8k_qwen7b_s42_cqa1: conclusion=success
  metrics keys: ['d000_correct', 'd100_correct', 'gsm8k_d000', 'gsm8k_d100', 'gsm8k_delta', 'total_items']

sft_qwen7b_olmo2_s123_sweep: conclusion=success
  metrics keys: ['olmo2_all_checkpoints', 'olmo2_d000_loss', 'olmo2_d000_token_acc', 'olmo2_d005_loss', 'olmo2_d025_loss', 'olmo2_d050_loss', 'olmo2_d100_loss', 'olmo2_d100_token_acc', 'qwen7b_all_checkpoints', 'total_checkpoints']

eval_qwen7b_s42_cqa1_v2: conclusion=failed

eval_qwen7b_s123_cqa1_v2: conclusion=success
  metrics keys: ['arc_challenge', 'arc_delta_d100_vs_d000', 'mmlu', 'mmlu_delta_d100_vs_d000', 'v_recovery_confirmed']

eval_qwen7b_s123_cqa1: conclusion=failed
  metrics keys: ['arc_d000', 'arc_d005', 'arc_d025', 'arc_d050', 'arc_d100', 'arc_delta_d100_d000', 'mmlu_d000', 'mmlu_d005', 'mmlu_d025', 'mmlu_d050', 'mmlu_d100', 'mmlu_delta_d100_d000']

eval_7b_mmlu_arc_cqa1: conclusion=success
  metrics keys: ['7b_d000_s123_arc', '7b_d000_s123_mmlu', '7b_d000_s42_arc', '7b_d000_s42_mmlu', '7b_d005_s123_arc', '7b_d005_s123_mmlu', '7b_d005_s42_arc', '7b_d005_s42_mmlu', '7b_d025_s123_arc', '7b_d025_s123_mmlu', '7b_d025_s42_arc', '7b_d025_s42_mmlu', '7b_d050_s123_arc', '7b_d050_s123_mmlu', '7b_d050_s42_arc', '7b_d050_s42_mmlu', '7b_d100_s123_arc', '7b_d100_s123_mmlu', '7b_d100_s42_arc', '7b_d100_s42_mmlu']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "8329d93d-38c0-472a-925e-a28d1694083e",
  "tool_use_result": {
    "stdout": "eval_qwen7b_mmlu_arc_s0: conclusion=success\n  metrics keys: ['mmlu', 'arc_challenge']\n\nsft_qwen7b_s0_cqa1: conclusion=success\n  metrics keys: ['d000', 'd005', 'd025', 'd050', 'd100']\n\neval_qwen7b_arc_s42: conclusion=success\n  metrics keys: ['arc_challenge_accuracy', 'delta_d100_d000', 'items_per_dosage']\n\ngsm8k_qwen7b_s123_cqa1: conclusion=success\n  metrics keys: ['d000_note', 'd100_note', 'gsm8k_d000', 'gsm8k_d100', 'gsm8k_delta']\n\ngsm8k_qwen7b_s42_intermediate_cqa1: conclusion=success\n  metrics keys: ['curve_shape', 'delta_d005', 'delta_d025', 'delta_d050', 'delta_d100', 'gsm8k_d000', 'gsm8k_d005', 'gsm8k_d025', 'gsm8k_d050', 'gsm8k_d100']\n\ngsm8k_qwen7b_s42_cqa1: conclusion=success\n  metrics keys: ['d000_correct', 'd100_correct', 'gsm8k_d000', 'gsm8k_d100', 'gsm8k_delta', 'total_items']\n\nsft_qwen7b_olmo2_s123_sweep: conclusion=success\n  metrics keys: ['olmo2_all_checkpoints', 'olmo2_d000_loss', 'olmo2_d000_token_acc', 'olmo2_d005_loss', 'olmo2_d025_loss', 'olmo2_d050_loss', 'olmo2_d100_loss', 'olmo2_d100_token_acc', 'qwen7b_all_checkpoints', 'total_checkpoints']\n\neval_qwen7b_s42_cqa1_v2: conclusion=failed\n\neval_qwen7b_s123_cqa1_v2: conclusion=success\n  metrics keys: ['arc_challenge', 'arc_delta_d100_vs_d000', 'mmlu', 'mmlu_delta_d100_vs_d000', 'v_recovery_confirmed']\n\neval_qwen7b_s123_cqa1: conclusion=failed\n  metrics keys: ['arc_d000', 'arc_d005', 'arc_d025', 'arc_d050', 'arc_d100', 'arc_delta_d100_d000', 'mmlu_d000', 'mmlu_d005', 'mmlu_d025', 'mmlu_d050', 'mmlu_d100', 'mmlu_delta_d100_d000']\n\neval_7b_mmlu_arc_cqa1: conclusion=success\n  metrics keys: ['7b_d000_s123_arc', '7b_d000_s123_mmlu', '7b_d000_s42_arc', '7b_d000_s42_mmlu', '7b_d005_s123_arc', '7b_d005_s123_mmlu', '7b_d005_s42_arc', '7b_d005_s42_mmlu', '7b_d025_s123_arc', '7b_d025_s123_mmlu', '7b_d025_s42_arc', '7b_d025_s42_mmlu', '7b_d050_s123_arc', '7b_d050_s123_mmlu', '7b_d050_s42_arc', '7b_d050_s42_mmlu', '7b_d100_s123_arc', '7b_d100_s123_mmlu', '7b_d100_s42_arc', '7b_d100_s42_mmlu']",
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

_source line 33_

<details><summary>Logged reasoning block</summary>

```text
OK so I also need to find if there's a v3 experiment for s42. Let me also search for all experiments with "7b" and "s42" in the name.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "6f55064c-ae6a-44aa-be5a-89cf2b3cb69f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014A8SWpsLhFRZ1dVe1RbEqo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1363,
      "cache_read_input_tokens": 82027,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1363
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

<details open><summary>🔧 Tool call — Bash · `toolu_01W7vc3jmn6zpUhCmPywaMfM`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/ab87e76a-91c7-436c-9cab-6cfa7abe7e5d/tool-results/mcp-agent-ml-research-read_registry-1779322772038.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n# Find all experiments with 7b and s42 in name, or eval_7b \nfor k, v in exps.items():\n    if ('7b' in k.lower() and ('s42' in k.lower() or 'mmlu' in k.lower())) or ('eval' in k.lower() and '7b' in k.lower()):\n        c = v.get('conclusion','?')\n        print(f'{k}: conclusion={c}')\n        m = v.get('metrics', {})\n        if m and ('mmlu' in str(m).lower() or 'arc' in str(m).lower()):\n            # print relevant metrics\n            for mk, mv in m.items():\n                if 'mmlu' in str(mk).lower() or 'arc' in str(mk).lower() or 'delta' in str(mk).lower():\n                    print(f'  {mk}: {mv}')\n        print()\n\"\n",
  "description": "Find all 7B eval experiments with s42 or mmlu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "7ee84bf7-2464-4100-99f0-119b23ec456f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014A8SWpsLhFRZ1dVe1RbEqo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1363,
      "cache_read_input_tokens": 82027,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1363
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

_source line 35 · 2026-05-21T00:19:45.956Z_

<details><summary>↩ Tool result · `toolu_01W7vc3jmn6zpUhCmPywaMfM`</summary>

```text
eval_qwen7b_mmlu_arc_s0: conclusion=success
  mmlu: {'d000': 0.6632, 'd005': 0.6468, 'd025': 0.6567, 'd050': 0.6578, 'd100': 0.6529, 'delta_d000_d100': -0.0103}
  arc_challenge: {'d000': 0.872, 'd005': 0.8532, 'd025': 0.8447, 'd050': 0.8558, 'd100': 0.8532, 'delta_d000_d100': -0.0188}

eval_qwen7b_arc_s42: conclusion=success
  arc_challenge_accuracy: {'d000_s42': 0.8788, 'd005_s42': 0.8609, 'd025_s42': 0.8404, 'd050_s42': 0.8456, 'd100_s42': 0.8498}
  delta_d100_d000: -0.029

gsm8k_qwen7b_s42_intermediate_cqa1: conclusion=success

gsm8k_qwen7b_s42_cqa1: conclusion=success

eval_qwen7b_s42_cqa1_v2: conclusion=failed

eval_qwen7b_s123_cqa1_v2: conclusion=success
  arc_challenge: {'d000': 0.872, 'd005': 0.8251, 'd025': 0.8515, 'd050': 0.8464, 'd100': 0.8473}
  arc_delta_d100_vs_d000: -0.0247
  mmlu: {'d000': 0.6659, 'd005': 0.6337, 'd025': 0.6482, 'd050': 0.65, 'd100': 0.6659}
  mmlu_delta_d100_vs_d000: 0

eval_qwen7b_s123_cqa1: conclusion=failed
  arc_d000: 0.8968
  arc_d005: 0.901
  arc_d025: 0.901
  arc_d050: 0.8985
  arc_d100: 0.8968
  arc_delta_d100_d000: 0
  mmlu_d000: 0.6974
  mmlu_d005: 0.6941
  mmlu_d025: 0.7025
  mmlu_d050: 0.704
  mmlu_d100: 0.7066
  mmlu_delta_d100_d000: 0.0092

exp_001_sft_olmo2_7b_d100_s42: conclusion=success

exp_001_sft_olmo2_7b_d050_s42: conclusion=success

exp_001_sft_olmo2_7b_d005_s42_v2: conclusion=success

exp_001_sft_olmo2_7b_d025_s42: conclusion=success

exp_001_sft_olmo2_7b_d005_s42: conclusion=killed

eval_7b_mmlu_arc_cqa1: conclusion=success
  7b_d000_s123_arc: 0.8985
  7b_d000_s123_mmlu: 0.6978
  7b_d000_s42_arc: 0.8959
  7b_d000_s42_mmlu: 0.6929
  7b_d005_s123_arc: 0.8985
  7b_d005_s123_mmlu: 0.6932
  7b_d005_s42_arc: 0.8968
  7b_d005_s42_mmlu: 0.6924
  7b_d025_s123_arc: 0.8993
  7b_d025_s123_mmlu: 0.7025
  7b_d025_s42_arc: 0.8985
  7b_d025_s42_mmlu: 0.7003
  7b_d050_s123_arc: 0.8993
  7b_d050_s123_mmlu: 0.7034
  7b_d050_s42_arc: 0.8993
  7b_d050_s42_mmlu: 0.705
  7b_d100_s123_arc: 0.8968
  7b_d100_s123_mmlu: 0.7072
  7b_d100_s42_arc: 0.8933
  7b_d100_s42_mmlu: 0.7103

exp_001_sft_olmo2_7b_d000_s42: conclusion=success

eval_7b_batch1_westd: conclusion=failed

eval_7b_batch_cqa1: conclusion=killed

exp_001_sft_7b_d000_s42: conclusion=success

exp_001_sft_7b_d100_s42: conclusion=success

exp_001_sft_7b_d050_s42: conclusion=success

exp_001_sft_7b_d025_s42: conclusion=success

exp_001_eval_7b_d000_s42_gsm8k: conclusion=success

exp_001_sft_7b_d005_s42: conclusion=success
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "567eefc2-d066-44e5-ad4a-35583d7e0948",
  "tool_use_result": {
    "stdout": "eval_qwen7b_mmlu_arc_s0: conclusion=success\n  mmlu: {'d000': 0.6632, 'd005': 0.6468, 'd025': 0.6567, 'd050': 0.6578, 'd100': 0.6529, 'delta_d000_d100': -0.0103}\n  arc_challenge: {'d000': 0.872, 'd005': 0.8532, 'd025': 0.8447, 'd050': 0.8558, 'd100': 0.8532, 'delta_d000_d100': -0.0188}\n\neval_qwen7b_arc_s42: conclusion=success\n  arc_challenge_accuracy: {'d000_s42': 0.8788, 'd005_s42': 0.8609, 'd025_s42': 0.8404, 'd050_s42': 0.8456, 'd100_s42': 0.8498}\n  delta_d100_d000: -0.029\n\ngsm8k_qwen7b_s42_intermediate_cqa1: conclusion=success\n\ngsm8k_qwen7b_s42_cqa1: conclusion=success\n\neval_qwen7b_s42_cqa1_v2: conclusion=failed\n\neval_qwen7b_s123_cqa1_v2: conclusion=success\n  arc_challenge: {'d000': 0.872, 'd005': 0.8251, 'd025': 0.8515, 'd050': 0.8464, 'd100': 0.8473}\n  arc_delta_d100_vs_d000: -0.0247\n  mmlu: {'d000': 0.6659, 'd005': 0.6337, 'd025': 0.6482, 'd050': 0.65, 'd100': 0.6659}\n  mmlu_delta_d100_vs_d000: 0\n\neval_qwen7b_s123_cqa1: conclusion=failed\n  arc_d000: 0.8968\n  arc_d005: 0.901\n  arc_d025: 0.901\n  arc_d050: 0.8985\n  arc_d100: 0.8968\n  arc_delta_d100_d000: 0\n  mmlu_d000: 0.6974\n  mmlu_d005: 0.6941\n  mmlu_d025: 0.7025\n  mmlu_d050: 0.704\n  mmlu_d100: 0.7066\n  mmlu_delta_d100_d000: 0.0092\n\nexp_001_sft_olmo2_7b_d100_s42: conclusion=success\n\nexp_001_sft_olmo2_7b_d050_s42: conclusion=success\n\nexp_001_sft_olmo2_7b_d005_s42_v2: conclusion=success\n\nexp_001_sft_olmo2_7b_d025_s42: conclusion=success\n\nexp_001_sft_olmo2_7b_d005_s42: conclusion=killed\n\neval_7b_mmlu_arc_cqa1: conclusion=success\n  7b_d000_s123_arc: 0.8985\n  7b_d000_s123_mmlu: 0.6978\n  7b_d000_s42_arc: 0.8959\n  7b_d000_s42_mmlu: 0.6929\n  7b_d005_s123_arc: 0.8985\n  7b_d005_s123_mmlu: 0.6932\n  7b_d005_s42_arc: 0.8968\n  7b_d005_s42_mmlu: 0.6924\n  7b_d025_s123_arc: 0.8993\n  7b_d025_s123_mmlu: 0.7025\n  7b_d025_s42_arc: 0.8985\n  7b_d025_s42_mmlu: 0.7003\n  7b_d050_s123_arc: 0.8993\n  7b_d050_s123_mmlu: 0.7034\n  7b_d050_s42_arc: 0.8993\n  7b_d050_s42_mmlu: 0.705\n  7b_d100_s123_arc: 0.8968\n  7b_d100_s123_mmlu: 0.7072\n  7b_d100_s42_arc: 0.8933\n  7b_d100_s42_mmlu: 0.7103\n\nexp_001_sft_olmo2_7b_d000_s42: conclusion=success\n\neval_7b_batch1_westd: conclusion=failed\n\neval_7b_batch_cqa1: conclusion=killed\n\nexp_001_sft_7b_d000_s42: conclusion=success\n\nexp_001_sft_7b_d100_s42: conclusion=success\n\nexp_001_sft_7b_d050_s42: conclusion=success\n\nexp_001_sft_7b_d025_s42: conclusion=success\n\nexp_001_eval_7b_d000_s42_gsm8k: conclusion=success\n\nexp_001_sft_7b_d005_s42: conclusion=success",
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

_source line 36_

<details><summary>Logged reasoning block</summary>

```text
Now let me also check for any experiment with qwen7b_s42_mmlu or eval_qwen7b_mmlu_s42 or similar in the full registry:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "a79cf210-0ed3-4497-85fe-8d3cbf9f9aee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V1UBB6hS1Gi4vF7K61DfSo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1871,
      "cache_read_input_tokens": 83390,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1871
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

_source line 37_

<details open><summary>🔧 Tool call — Bash · `toolu_01Lp4KN9ZXRiZiJgwBtXGgB5`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/ab87e76a-91c7-436c-9cab-6cfa7abe7e5d/tool-results/mcp-agent-ml-research-read_registry-1779322772038.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n# Find any experiment with qwen7b_s42 and mmlu, or v3\nfor k, v in exps.items():\n    if ('qwen7b' in k.lower() or 'qwen_7b' in k.lower()) and ('s42' in k.lower()):\n        print(f'{k}: conclusion={v.get(\\\"conclusion\\\",\\\"?\\\")}')\n    if 'qwen7b' in k.lower() and 'v3' in k.lower():\n        print(f'{k}: conclusion={v.get(\\\"conclusion\\\",\\\"?\\\")}')\n    if 'eval' in k.lower() and 'qwen7b' in k.lower() and 'mmlu' in k.lower():\n        print(f'{k}: conclusion={v.get(\\\"conclusion\\\",\\\"?\\\")}')\n\" 2>&1\n",
  "description": "Search for qwen7b s42 mmlu v3 experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "659f9300-e219-4684-bdb8-940aa4e78d20",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V1UBB6hS1Gi4vF7K61DfSo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1871,
      "cache_read_input_tokens": 83390,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1871
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

_source line 38 · 2026-05-21T00:19:52.756Z_

<details><summary>↩ Tool result · `toolu_01Lp4KN9ZXRiZiJgwBtXGgB5`</summary>

```text
eval_qwen7b_mmlu_arc_s0: conclusion=success
eval_qwen7b_arc_s42: conclusion=success
gsm8k_qwen7b_s42_intermediate_cqa1: conclusion=success
gsm8k_qwen7b_s42_cqa1: conclusion=success
eval_qwen7b_s42_cqa1_v2: conclusion=failed
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "74ac933e-10c8-4ea3-8da9-8920fb4a6165",
  "tool_use_result": {
    "stdout": "eval_qwen7b_mmlu_arc_s0: conclusion=success\neval_qwen7b_arc_s42: conclusion=success\ngsm8k_qwen7b_s42_intermediate_cqa1: conclusion=success\ngsm8k_qwen7b_s42_cqa1: conclusion=success\neval_qwen7b_s42_cqa1_v2: conclusion=failed",
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

_source line 39_

<details><summary>Logged reasoning block</summary>

```text
There's no v3 for the s42 MMLU eval. The only successful sources for s42 MMLU data are:
1. `eval_7b_mmlu_arc_cqa1` - the old version (pre-evaluate.py fix)

But C009/C010 says we need version consistency. The `eval_qwen7b_s123_cqa1` was explicitly invalidated because it used the old evaluate.py. By the same logic, `eval_7b_mmlu_arc_cqa1`'s s42 data should also be from the old version.


The task claims all evaluation results are complete, so maybe I'm missing something in the registry. Let me look for recent experiments or artifact files that might have this data. Actually, I'm noticing two separate evaluations here—the old `eval_7b_mmlu_arc_cqa1` marked as successful with s42 MMLU and ARC data but using the old evaluate.py, and then `eval_qwen7b_arc_s42` which might be a separate source for the ARC data.

Now I'm comparing the s123 results between old and new versions. The old `eval_qwen7b_s123_cqa1` that failed shows MMLU scores of 0.6974 and 0.7066 with a +0.92pp delta, while the new v2 version shows 0.6659 for both with zero delta. For ARC, the old had 0.8968 for both with zero delta, but the new shows 0.872 and 0.8473 with a -2.47pp delta. The old evaluate.py clearly produced systematically different results, yet `eval_7b_mmlu_arc_cqa1` is also marked successful with similar values to the old version.

This suggests `eval_7b_mmlu_arc_cqa1` also used the old evaluate.py. Let me check if maybe s42 was rerun separately or if I'm missing something in the running experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "2c874424-8135-4a41-8dd4-1d1a4885e112",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nf7gdfJwLxtDxpJ5h5yLJa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 595,
      "cache_read_input_tokens": 85261,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 595
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

_source line 40_

<details open><summary>🔧 Tool call — Bash · `toolu_01E5hhuUyoTYQMSWwmEzSugX`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/ab87e76a-91c7-436c-9cab-6cfa7abe7e5d/tool-results/mcp-agent-ml-research-read_registry-1779322772038.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n# Check for eval experiments with 'qwen7b' that might have s42 MMLU data\n# Also check for any experiment that contains s42 mmlu 7b data\nfor k, v in exps.items():\n    m = v.get('metrics', {})\n    ms = str(m)\n    if 'qwen7b' in k.lower() and 'mmlu' in ms.lower() and 's42' in (k.lower() + ms.lower()):\n        c = v.get('conclusion','?')\n        print(f'{k}: conclusion={c}')\n        print(f'  metrics: {json.dumps(m, indent=2)[:500]}')\n        print()\n\"\n",
  "description": "Find any experiment with qwen7b s42 MMLU metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "1da27895-4f71-4a4f-8068-4e180ed78741",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nf7gdfJwLxtDxpJ5h5yLJa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 595,
      "cache_read_input_tokens": 85261,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 595
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

_source line 41 · 2026-05-21T00:20:12.068Z_

<details><summary>↩ Tool result · `toolu_01E5hhuUyoTYQMSWwmEzSugX`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "f4e93b84-984d-4450-8210-22eb00b95dd7",
  "tool_use_result": {
    "stdout": "",
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

_source line 42_

<details><summary>Logged reasoning block</summary>

```text
No results found. Let me also check for the latest MMLU eval for s42 that might have been added recently, and also check if there are RUNNING experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "d20497a2-dab3-4315-b081-535b36d8e7a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PYusxpcJnD6nLS4j1vX6oB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1027,
      "cache_read_input_tokens": 85856,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1027
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

_source line 43_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_018wghz5ajqQ9ZFqTu9oLEu9`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "filters": {
    "status": "RUNNING"
  },
  "fields": [
    "exp_id",
    "title",
    "conclusion"
  ],
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "24d5598a-c4f7-4573-b768-7c5bab01bc30",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PYusxpcJnD6nLS4j1vX6oB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1027,
      "cache_read_input_tokens": 85856,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1027
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

_source line 44 · 2026-05-21T00:20:17.223Z_

<details><summary>↩ Tool result · `toolu_018wghz5ajqQ9ZFqTu9oLEu9`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"retrain_qwen14b_d050_s0\": {}, \"r3w10_threshold_dgp\": {}, \"sft_qwen14b_s0_sweep\": {}}, \"count\": 3, \"total\": 3, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8794}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "a04a3ba8-e4e5-449f-892b-a33933a04813",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"retrain_qwen14b_d050_s0\\\": {}, \\\"r3w10_threshold_dgp\\\": {}, \\\"sft_qwen14b_s0_sweep\\\": {}}, \\\"count\\\": 3, \\\"total\\\": 3, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.8794}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"retrain_qwen14b_d050_s0\": {}, \"r3w10_threshold_dgp\": {}, \"sft_qwen14b_s0_sweep\": {}}, \"count\": 3, \"total\": 3, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8794}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 45_

<details><summary>Logged reasoning block</summary>

```text
There are only 3 running experiments and none of them are related to Qwen-7B s42 MMLU eval.

Let me check if there's any artifact file that has this data. Also, let me look at `eval_qwen7b_mmlu_s42` or similar experiments. Actually, looking at the data again - the task says "Qwen-7B 三个种子（s0, s42, s123）的 MMLU 5-shot 和 ARC 25-shot 评测结果已全部齐全". It's saying the data is all available.


I should look through the artifacts or project files to see if the compiled results are already stored somewhere.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "a2ff0c10-1e53-4ffb-845c-186140374fad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcCiLGouBqBv2YGeZsHT5p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 313,
      "cache_read_input_tokens": 86883,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 313
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

_source line 46_

<details open><summary>🔧 Tool call — Glob · `toolu_01MSeJbqf8xMdHCh5UEkcveA`</summary>

```json
{
  "pattern": "**/*qwen7b*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "af130891-4460-45b9-b420-dd96171b008b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcCiLGouBqBv2YGeZsHT5p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 313,
      "cache_read_input_tokens": 86883,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 313
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

_source line 47 · 2026-05-21T00:20:28.689Z_

<details><summary>↩ Tool result · `toolu_01MSeJbqf8xMdHCh5UEkcveA`</summary>

```text
artifacts/_project/data/s1_signals_qwen7b_summary.txt
artifacts/sft_qwen7b_olmo2_s123_sweep_report.md
artifacts/exp001/report/sft_qwen7b_olmo2_s123_sweep_report.md
artifacts/sft_qwen7b_s0_cqa1/report/sft_qwen7b_s0_cqa1_analysis.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "abca923a-0661-448e-95ac-95d9d224d9d4",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/data/s1_signals_qwen7b_summary.txt",
      "artifacts/sft_qwen7b_olmo2_s123_sweep_report.md",
      "artifacts/exp001/report/sft_qwen7b_olmo2_s123_sweep_report.md",
      "artifacts/sft_qwen7b_s0_cqa1/report/sft_qwen7b_s0_cqa1_analysis.md"
    ],
    "durationMs": 27,
    "numFiles": 4,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Bash · `toolu_01VfZek5MJJicYzRCzM8W9WG`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/ 2>/dev/null | head -30",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "6ec0779c-c66c-49ec-870f-9d28743861c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcCiLGouBqBv2YGeZsHT5p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 313,
      "cache_read_input_tokens": 86883,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 313
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

_source line 49 · 2026-05-21T00:20:29.390Z_

<details><summary>↩ Tool result · `toolu_01VfZek5MJJicYzRCzM8W9WG`</summary>

```text
2pl_vs_4pl_ablation.md
3B_s123_eval_matrix_complete.md
_project
algorithm1_pseudocode.tex
analysis_14b_d100_s42.md
analysis_3B_d000_gsm8k_seed_variance.md
appendix_domain_decomposition.md
batch_matrix_commands.md
bib_rebuild_2024_classics.bib
bib_rebuild_2025plus.bib
bootstrap_profile_stability.py
classification_criteria.yaml
classification_sensitivity_sweep.py
compile_eval_summary.py
coverage_report_20260515.md
d000_alignment_tax_analysis.md
d108_v4_analysis.md
diag_exp006_pooled_irt_n25.md
diag_exp_001_sft_15B_d005_s123.md
diag_exp_001_sft_d100_3B.md
diag_sft_sweep_failures_westd.md
diagnose_exp001_eval_3B_d000_s42_v3.md
diagnose_exp001_sft_llama32_3B_d005_s42.md
diagnosis_exp002_3B_d000_s123_cuda2.md
dose_response_analysis.md
dream_reports
error_analysis.md
error_analysis_summary.yaml
eval_gemma2_mmlu_s0_diagnosis.md
eval_metrics_summary.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "f680b670-d394-4d91-ac1e-0f60060375e4",
  "tool_use_result": {
    "stdout": "2pl_vs_4pl_ablation.md\n3B_s123_eval_matrix_complete.md\n_project\nalgorithm1_pseudocode.tex\nanalysis_14b_d100_s42.md\nanalysis_3B_d000_gsm8k_seed_variance.md\nappendix_domain_decomposition.md\nbatch_matrix_commands.md\nbib_rebuild_2024_classics.bib\nbib_rebuild_2025plus.bib\nbootstrap_profile_stability.py\nclassification_criteria.yaml\nclassification_sensitivity_sweep.py\ncompile_eval_summary.py\ncoverage_report_20260515.md\nd000_alignment_tax_analysis.md\nd108_v4_analysis.md\ndiag_exp006_pooled_irt_n25.md\ndiag_exp_001_sft_15B_d005_s123.md\ndiag_exp_001_sft_d100_3B.md\ndiag_sft_sweep_failures_westd.md\ndiagnose_exp001_eval_3B_d000_s42_v3.md\ndiagnose_exp001_sft_llama32_3B_d005_s42.md\ndiagnosis_exp002_3B_d000_s123_cuda2.md\ndose_response_analysis.md\ndream_reports\nerror_analysis.md\nerror_analysis_summary.yaml\neval_gemma2_mmlu_s0_diagnosis.md\neval_metrics_summary.json",
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

_source line 50_

<details open><summary>🔧 Tool call — Bash · `toolu_01UooQ8x8wZq67tKM7dMyEkr`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/ | grep -i \"eval_metrics\\|qwen7b.*s42\\|7b.*bootstrap\\|eval_summary\\|family\"",
  "description": "Search for relevant eval/bootstrap artifact files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "707fe94e-022b-4f95-90b0-05f00ba4a228",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N8Aj1azQXJFEaHnfZBcYEx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 913,
      "cache_read_input_tokens": 87196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 913
      },
      "output_tokens": 62,
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

_source line 51 · 2026-05-21T00:20:33.215Z_

<details><summary>↩ Tool result · `toolu_01UooQ8x8wZq67tKM7dMyEkr`</summary>

```text
compile_eval_summary.py
eval_metrics_summary.json
eval_metrics_summary.md
eval_summary_matrix.csv
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "dcd66a41-baec-4924-b208-5eb9322122ba",
  "tool_use_result": {
    "stdout": "compile_eval_summary.py\neval_metrics_summary.json\neval_metrics_summary.md\neval_summary_matrix.csv",
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

_source line 52_

<details open><summary>🔧 Tool call — Read · `toolu_01ALpNRKozP6Tabg75sE9wcv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/eval_metrics_summary.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "850f3c33-668d-4eda-8d81-8ab7d9bee980",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FwhopR87toLrH7W8fX4mtd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 288,
      "cache_read_input_tokens": 88109,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 288
      },
      "output_tokens": 65,
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

_source line 53 · 2026-05-21T00:20:36.221Z_

<details><summary>↩ Tool result · `toolu_01ALpNRKozP6Tabg75sE9wcv`</summary>

```text
1	{
2	  "metadata": {
3	    "project": "contamcal-irt-calibration",
4	    "description": "Eval metrics summary across all scales, doses, seeds, and eval types",
5	    "scales": [
6	      "0.5B",
7	      "1.5B",
8	      "3B"
9	    ],
10	    "doses_pct": [
11	      0,
12	      5,
13	      25,
14	      100
15	    ],
16	    "seeds": [
17	      42,
18	      123
19	    ],
20	    "eval_types": [
21	      "aligned",
22	      "para_aligned"
23	    ],
24	    "benchmarks": [
25	      "mmlu",
26	      "gsm8k",
27	      "arc",
28	      "humaneval"
29	    ],
30	    "model_family": "Qwen2.5",
31	    "lora_alpha": 32,
32	    "notes": [
33	      "HumanEval metrics from registry (not stored on disk)",
34	      "3B uses v2 checkpoints (alpha=32); v1/DEPRECATED excluded",
35	      "3B d005_s123_aligned eval is missing (never run)",
36	      "3B d100_s123_para_aligned eval is missing",
37	      "Some 0.5B/1.5B para_aligned s123 entries are missing",
38	      "0.5B d025_s42 HumanEval=0.1923 may be from mislabeled para_aligned run"
39	    ]
40	  },
41	  "individual_results": [
42	    {
43	      "scale": "0.5B",
44	      "dose_pct": 0,
45	      "seed": 42,
46	      "eval_type": "aligned",
47	      "mmlu": 0.3979,
48	      "gsm8k": 0.3692,
49	      "arc": 0.4693,
50	      "humaneval": 0.1098,
51	      "source_dir": "Qwen2.5-0.5B_d000_s42_aligned",
52	      "notes": ""
53	    },
54	    {
55	      "scale": "0.5B",
56	      "dose_pct": 0,
57	      "seed": 42,
58	      "eval_type": "para_aligned",
59	      "mmlu": 0.4428,
60	      "gsm8k": 0.2807,
61	      "arc": 0.4792,
62	      "humaneval": 0.1154,
63	      "source_dir": "Qwen2.5-0.5B_d000_s42_para_aligned",
64	      "notes": ""
65	    },
66	    {
67	      "scale": "0.5B",
68	      "dose_pct": 0,
69	      "seed": 123,
70	      "eval_type": "aligned",
71	      "mmlu": 0.4216,
72	      "gsm8k": 0.3412,
73	      "arc": 0.4974,
74	      "humaneval": 0.1037,
75	      "source_dir": "Qwen2.5-0.5B_d000_s123_aligned",
76	      "notes": ""
77	    },
78	    {
79	      "scale": "0.5B",
80	      "dose_pct": 5,
81	      "seed": 42,
82	      "eval_type": "aligned",
83	      "mmlu": 0.3255,
84	      "gsm8k": 0.3624,
85	      "arc": 0.3285,
86	      "humaneval": 0.0793,
87	      "source_dir": "Qwen2.5-0.5B_d005_s42_aligned",
88	      "notes": ""
89	    },
90	    {
91	      "scale": "0.5B",
92	      "dose_pct": 5,
93	      "seed": 42,
94	      "eval_type": "para_aligned",
95	      "mmlu": 0.3548,
96	      "gsm8k": 0.2588,
97	      "arc": 0.33,
98	      "humaneval": 0.0,
99	      "source_dir": "Qwen2.5-0.5B_d005_s42_para_aligned",
100	      "notes": ""
101	    },
102	    {
103	      "scale": "0.5B",
104	      "dose_pct": 5,
105	      "seed": 123,
106	      "eval_type": "aligned",
107	      "mmlu": 0.3002,
108	      "gsm8k": 0.3677,
109	      "arc": 0.2978,
110	      "humaneval": 0.0976,
111	      "source_dir": "Qwen2.5-0.5B_d005_s123_aligned",
112	      "notes": ""
113	    },
114	    {
115	      "scale": "0.5B",
116	      "dose_pct": 5,
117	      "seed": 123,
118	      "eval_type": "para_aligned",
119	      "mmlu": 0.3166,
120	      "gsm8k": 0.2939,
121	      "arc": 0.2912,
122	      "humaneval": 0.0,
123	      "source_dir": "Qwen2.5-0.5B_d005_s123_para_aligned",
124	      "notes": ""
125	    },
126	    {
127	      "scale": "0.5B",
128	      "dose_pct": 25,
129	      "seed": 42,
130	      "eval_type": "aligned",
131	      "mmlu": 0.2803,
132	      "gsm8k": 0.3662,
133	      "arc": 0.3251,
134	      "humaneval": 0.1923,
135	      "source_dir": "Qwen2.5-0.5B_d025_s42_aligned",
136	      "notes": ""
137	    },
138	    {
139	      "scale": "0.5B",
140	      "dose_pct": 25,
141	      "seed": 42,
142	      "eval_type": "para_aligned",
143	      "mmlu": 0.2835,
144	      "gsm8k": 0.3114,
145	      "arc": 0.3199,
146	      "humaneval": null,
147	      "source_dir": "Qwen2.5-0.5B_d025_s42_para_aligned",
148	      "notes": ""
149	    },
150	    {
151	      "scale": "0.5B",
152	      "dose_pct": 25,
153	      "seed": 123,
154	      "eval_type": "aligned",
155	      "mmlu": 0.3473,
156	      "gsm8k": 0.3533,
157	      "arc": 0.4061,
158	      "humaneval": null,
159	      "source_dir": "Qwen2.5-0.5B_d025_s123_aligned",
160	      "notes": ""
161	    },
162	    {
163	      "scale": "0.5B",
164	      "dose_pct": 100,
165	      "seed": 42,
166	      "eval_type": "aligned",
167	      "mmlu": 0.2334,
168	      "gsm8k": 0.3654,
169	      "arc": 0.2944,
170	      "humaneval": 0.0,
171	      "source_dir": "Qwen2.5-0.5B_d100_s42_aligned",
172	      "notes": ""
173	    },
174	    {
175	      "scale": "0.5B",
176	      "dose_pct": 100,
177	      "seed": 123,
178	      "eval_type": "aligned",
179	      "mmlu": 0.3058,
180	      "gsm8k": 0.3798,
181	      "arc": 0.3669,
182	      "humaneval": 0.1037,
183	      "source_dir": "Qwen2.5-0.5B_d100_s123_aligned",
184	      "notes": ""
185	    },
186	    {
187	      "scale": "1.5B",
188	      "dose_pct": 0,
189	      "seed": 42,
190	      "eval_type": "aligned",
191	      "mmlu": 0.5853,
192	      "gsm8k": 0.6543,
193	      "arc": 0.7722,
194	      "humaneval": 0.128,
195	      "source_dir": "Qwen2.5-1.5B_d000_s42_aligned",
196	      "notes": ""
197	    },
198	    {
199	      "scale": "1.5B",
200	      "dose_pct": 0,
201	      "seed": 42,
202	      "eval_type": "para_aligned",
203	      "mmlu": 0.6096,
204	      "gsm8k": 0.557,
205	      "arc": 0.7547,
206	      "humaneval": 0.0385,
207	      "source_dir": "Qwen2.5-1.5B_d000_s42_para_aligned",
208	      "notes": ""
209	    },
210	    {
211	      "scale": "1.5B",
212	      "dose_pct": 0,
213	      "seed": 123,
214	      "eval_type": "aligned",
215	      "mmlu": 0.5855,
216	      "gsm8k": 0.6535,
217	      "arc": 0.7577,
218	      "humaneval": 0.1707,
219	      "source_dir": "Qwen2.5-1.5B_d000_s123_aligned",
220	      "notes": ""
221	    },
222	    {
223	      "scale": "1.5B",
224	      "dose_pct": 5,
225	      "seed": 42,
226	      "eval_type": "aligned",
227	      "mmlu": 0.5852,
228	      "gsm8k": 0.6482,
229	      "arc": 0.7688,
230	      "humaneval": 0.25,
231	      "source_dir": "Qwen2.5-1.5B_d005_s42_aligned",
232	      "notes": ""
233	    },
234	    {
235	      "scale": "1.5B",
236	      "dose_pct": 5,
237	      "seed": 42,
238	      "eval_type": "para_aligned",
239	      "mmlu": 0.6164,
240	      "gsm8k": 0.5439,
241	      "arc": 0.7532,
242	      "humaneval": 0.1923,
243	      "source_dir": "Qwen2.5-1.5B_d005_s42_para_aligned",
244	      "notes": ""
245	    },
246	    {
247	      "scale": "1.5B",
248	      "dose_pct": 5,
249	      "seed": 123,
250	      "eval_type": "aligned",
251	      "mmlu": 0.5869,
252	      "gsm8k": 0.6482,
253	      "arc": 0.7568,
254	      "humaneval": null,
255	      "source_dir": "Qwen2.5-1.5B_d005_s123_aligned",
256	      "notes": ""
257	    },
258	    {
259	      "scale": "1.5B",
260	      "dose_pct": 25,
261	      "seed": 42,
262	      "eval_type": "aligned",
263	      "mmlu": 0.5902,
264	      "gsm8k": 0.6535,
265	      "arc": 0.7688,
266	      "humaneval": 0.2256,
267	      "source_dir": "Qwen2.5-1.5B_d025_s42_aligned",
268	      "notes": ""
269	    },
270	    {
271	      "scale": "1.5B",
272	      "dose_pct": 25,
273	      "seed": 42,
274	      "eval_type": "para_aligned",
275	      "mmlu": 0.6176,
276	      "gsm8k": 0.5395,
277	      "arc": 0.7661,
278	      "humaneval": 0.154,
279	      "source_dir": "Qwen2.5-1.5B_d025_s42_para_aligned",
280	      "notes": ""
281	    },
282	    {
283	      "scale": "1.5B",
284	      "dose_pct": 25,
285	      "seed": 123,
286	      "eval_type": "aligned",
287	      "mmlu": 0.5881,
288	      "gsm8k": 0.655,
289	      "arc": 0.7577,
290	      "humaneval": null,
291	      "source_dir": "Qwen2.5-1.5B_d025_s123_aligned",
292	      "notes": ""
293	    },
294	    {
295	      "scale": "1.5B",
296	      "dose_pct": 100,
297	      "seed": 42,
298	      "eval_type": "aligned",
299	      "mmlu": 0.5933,
300	      "gsm8k": 0.6497,
301	      "arc": 0.7688,
302	      "humaneval": 0.3049,
303	      "source_dir": "Qwen2.5-1.5B_d100_s42_aligned",
304	      "notes": ""
305	    },
306	    {
307	      "scale": "1.5B",
308	      "dose_pct": 100,
309	      "seed": 42,
310	      "eval_type": "para_aligned",
311	      "mmlu": 0.6252,
312	      "gsm8k": 0.5526,
313	      "arc": 0.7661,
314	      "humaneval": 0.2692,
315	      "source_dir": "Qwen2.5-1.5B_d100_s42_para_aligned",
316	      "notes": ""
317	    },
318	    {
319	      "scale": "1.5B",
320	      "dose_pct": 100,
321	      "seed": 123,
322	      "eval_type": "aligned",
323	      "mmlu": 0.5956,
324	      "gsm8k": 0.6444,
325	      "arc": 0.7816,
326	      "humaneval": 0.2805,
327	      "source_dir": "Qwen2.5-1.5B_d100_s123_aligned",
328	      "notes": ""
329	    },
330	    {
331	      "scale": "3B",
332	      "dose_pct": 0,
333	      "seed": 42,
334	      "eval_type": "aligned",
335	      "mmlu": 0.6295,
336	      "gsm8k": 0.3525,
337	      "arc": 0.8183,
338	      "humaneval": 0.0976,
339	      "source_dir": "Qwen2.5-3B_d000_v2_s42_aligned",
340	      "notes": "alpha=32"
341	    },
342	    {
343	      "scale": "3B",
344	      "dose_pct": 0,
345	      "seed": 42,
346	      "eval_type": "para_aligned",
347	      "mmlu": 0.6468,
348	      "gsm8k": 0.2895,
349	      "arc": 0.8121,
350	      "humaneval": 0.0385,
351	      "source_dir": "Qwen2.5-3B_d000_v2_s42_para_aligned",
352	      "notes": "alpha=32"
353	    },
354	    {
355	      "scale": "3B",
356	      "dose_pct": 0,
357	      "seed": 123,
358	      "eval_type": "aligned",
359	      "mmlu": 0.6314,
360	      "gsm8k": 0.2676,
361	      "arc": 0.8259,
362	      "humaneval": 0.061,
363	      "source_dir": "Qwen2.5-3B_d000_v2_s123_aligned",
364	      "notes": "alpha=32"
365	    },
366	    {
367	      "scale": "3B",
368	      "dose_pct": 0,
369	      "seed": 123,
370	      "eval_type": "para_aligned",
371	      "mmlu": 0.6512,
372	      "gsm8k": 0.1491,
373	      "arc": 0.8121,
374	      "humaneval": 0.0385,
375	      "source_dir": "Qwen2.5-3B_d000_v2_s123_para_aligned",
376	      "notes": "alpha=32"
377	    },
378	    {
379	      "scale": "3B",
380	      "dose_pct": 5,
381	      "seed": 42,
382	      "eval_type": "aligned",
383	      "mmlu": 0.6345,
384	      "gsm8k": 0.2077,
385	      "arc": 0.8294,
386	      "humaneval": 0.1463,
387	      "source_dir": "Qwen2.5-3B_d005_s42_aligned",
388	      "notes": ""
389	    },
390	    {
391	      "scale": "3B",
392	      "dose_pct": 5,
393	      "seed": 42,
394	      "eval_type": "para_aligned",
395	      "mmlu": 0.6542,
396	      "gsm8k": 0.1491,
397	      "arc": 0.8221,
398	      "humaneval": null,
399	      "source_dir": "Qwen2.5-3B_d005_s42_para_aligned",
400	      "notes": ""
401	    },
402	    {
403	      "scale": "3B",
404	      "dose_pct": 5,
405	      "seed": 123,
406	      "eval_type": "para_aligned",
407	      "mmlu": 0.6461,
408	      "gsm8k": 0.5,
409	      "arc": 0.8192,
410	      "humaneval": 0.0769,
411	      "source_dir": "Qwen2.5-3B_d005_s123_para_aligned",
412	      "notes": ""
413	    },
414	    {
415	      "scale": "3B",
416	      "dose_pct": 25,
417	      "seed": 42,
418	      "eval_type": "aligned",
419	      "mmlu": 0.5998,
420	      "gsm8k": 0.6793,
421	      "arc": 0.8276,
422	      "humaneval": 0.0976,
423	      "source_dir": "Qwen2.5-3B_d025_v2_aligned",
424	      "notes": "alpha=32"
425	    },
426	    {
427	      "scale": "3B",
428	      "dose_pct": 25,
429	      "seed": 42,
430	      "eval_type": "para_aligned",
431	      "mmlu": 0.621,
432	      "gsm8k": 0.5482,
433	      "arc": 0.8106,
434	      "humaneval": 0.1154,
435	      "source_dir": "Qwen2.5-3B_d025_v2_s42_para_aligned",
436	      "notes": "alpha=32"
437	    },
438	    {
439	      "scale": "3B",
440	      "dose_pct": 25,
441	      "seed": 123,
442	      "eval_type": "aligned",
443	      "mmlu": 0.6367,
444	      "gsm8k": 0.5254,
445	      "arc": 0.8336,
446	      "humaneval": 0.1585,
447	      "source_dir": "Qwen2.5-3B_d025_s123_aligned",
448	      "notes": ""
449	    },
450	    {
451	      "scale": "3B",
452	      "dose_pct": 25,
453	      "seed": 123,
454	      "eval_type": "para_aligned",
455	      "mmlu": 0.6615,
456	      "gsm8k": 0.4254,
457	      "arc": 0.8121,
458	      "humaneval": 0.1538,
459	      "source_dir": "Qwen2.5-3B_d025_s123_para_aligned",
460	      "notes": ""
461	    },
462	    {
463	      "scale": "3B",
464	      "dose_pct": 100,
465	      "seed": 42,
466	      "eval_type": "aligned",
467	      "mmlu": 0.632,
468	      "gsm8k": 0.7415,
469	      "arc": 0.8242,
470	      "humaneval": 0.1707,
471	      "source_dir": "Qwen2.5-3B_d100_v2_s42_aligned",
472	      "notes": "alpha=32"
473	    },
474	    {
475	      "scale": "3B",
476	      "dose_pct": 100,
477	      "seed": 42,
478	      "eval_type": "para_aligned",
479	      "mmlu": 0.659,
480	      "gsm8k": 0.5833,
481	      "arc": 0.8092,
482	      "humaneval": 0.1154,
483	      "source_dir": "Qwen2.5-3B_d100_v2_s42_para_aligned",
484	      "notes": "alpha=32"
485	    },
486	    {
487	      "scale": "3B",
488	      "dose_pct": 100,
489	      "seed": 123,
490	      "eval_type": "aligned",
491	      "mmlu": 0.6319,
492	      "gsm8k": 0.7324,
493	      "arc": 0.8311,
494	      "humaneval": 0.1829,
495	      "source_dir": "Qwen2.5-3B_d100_v2_s123_aligned",
496	      "notes": "alpha=32"
497	    }
498	  ],
499	  "aggregated_by_dose": [
500	    {
501	      "scale": "0.5B",
502	      "dose_pct": 0,
503	      "eval_type": "aligned",
504	      "n_seeds": 2,
505	      "mmlu_mean": 0.4097,
506	      "mmlu_std": 0.0168,
507	      "gsm8k_mean": 0.3552,
508	      "gsm8k_std": 0.0198,
509	      "arc_mean": 0.4834,
510	      "arc_std": 0.0199,
511	      "humaneval_mean": 0.1067,
512	      "humaneval_std": 0.0043
513	    },
514	    {
515	      "scale": "0.5B",
516	      "dose_pct": 0,
517	      "eval_type": "para_aligned",
518	      "n_seeds": 1,
519	      "mmlu_mean": 0.4428,
520	      "mmlu_std": null,
521	      "gsm8k_mean": 0.2807,
522	      "gsm8k_std": null,
523	      "arc_mean": 0.4792,
524	      "arc_std": null,
525	      "humaneval_mean": 0.1154,
526	      "humaneval_std": null
527	    },
528	    {
529	      "scale": "0.5B",
530	      "dose_pct": 5,
531	      "eval_type": "aligned",
532	      "n_seeds": 2,
533	      "mmlu_mean": 0.3129,
534	      "mmlu_std": 0.0179,
535	      "gsm8k_mean": 0.365,
536	      "gsm8k_std": 0.0037,
537	      "arc_mean": 0.3132,
538	      "arc_std": 0.0217,
539	      "humaneval_mean": 0.0885,
540	      "humaneval_std": 0.0129
541	    },
542	    {
543	      "scale": "0.5B",
544	      "dose_pct": 5,
545	      "eval_type": "para_aligned",
546	      "n_seeds": 2,
547	      "mmlu_mean": 0.3357,
548	      "mmlu_std": 0.027,
549	      "gsm8k_mean": 0.2763,
550	      "gsm8k_std": 0.0248,
551	      "arc_mean": 0.3106,
552	      "arc_std": 0.0274,
553	      "humaneval_mean": 0.0,
554	      "humaneval_std": 0.0
555	    },
556	    {
557	      "scale": "0.5B",
558	      "dose_pct": 25,
559	      "eval_type": "aligned",
560	      "n_seeds": 2,
561	      "mmlu_mean": 0.3138,
562	      "mmlu_std": 0.0474,
563	      "gsm8k_mean": 0.3598,
564	      "gsm8k_std": 0.0091,
565	      "arc_mean": 0.3656,
566	      "arc_std": 0.0573,
567	      "humaneval_mean": 0.1923,
568	      "humaneval_std": null
569	    },
570	    {
571	      "scale": "0.5B",
572	      "dose_pct": 25,
573	      "eval_type": "para_aligned",
574	      "n_seeds": 1,
575	      "mmlu_mean": 0.2835,
576	      "mmlu_std": null,
577	      "gsm8k_mean": 0.3114,
578	      "gsm8k_std": null,
579	      "arc_mean": 0.3199,
580	      "arc_std": null,
581	      "humaneval_mean": null,
582	      "humaneval_std": null
583	    },
584	    {
585	      "scale": "0.5B",
586	      "dose_pct": 100,
587	      "eval_type": "aligned",
588	      "n_seeds": 2,
589	      "mmlu_mean": 0.2696,
590	      "mmlu_std": 0.0512,
591	      "gsm8k_mean": 0.3726,
592	      "gsm8k_std": 0.0102,
593	      "arc_mean": 0.3306,
594	      "arc_std": 0.0513,
595	      "humaneval_mean": 0.0519,
596	      "humaneval_std": 0.0733
597	    },
598	    {
599	      "scale": "1.5B",
600	      "dose_pct": 0,
601	      "eval_type": "aligned",
602	      "n_seeds": 2,
603	      "mmlu_mean": 0.5854,
604	      "mmlu_std": 0.0001,
605	      "gsm8k_mean": 0.6539,
606	      "gsm8k_std": 0.0006,
607	      "arc_mean": 0.765,
608	      "arc_std": 0.0103,
609	      "humaneval_mean": 0.1493,
610	      "humaneval_std": 0.0302
611	    },
612	    {
613	      "scale": "1.5B",
614	      "dose_pct": 0,
615	      "eval_type": "para_aligned",
616	      "n_seeds": 1,
617	      "mmlu_mean": 0.6096,
618	      "mmlu_std": null,
619	      "gsm8k_mean": 0.557,
620	      "gsm8k_std": null,
621	      "arc_mean": 0.7547,
622	      "arc_std": null,
623	      "humaneval_mean": 0.0385,
624	      "humaneval_std": null
625	    },
626	    {
627	      "scale": "1.5B",
628	      "dose_pct": 5,
629	      "eval_type": "aligned",
630	      "n_seeds": 2,
631	      "mmlu_mean": 0.586,
632	      "mmlu_std": 0.0012,
633	      "gsm8k_mean": 0.6482,
634	      "gsm8k_std": 0.0,
635	      "arc_mean": 0.7628,
636	      "arc_std": 0.0085,
637	      "humaneval_mean": 0.25,
638	      "humaneval_std": null
639	    },
640	    {
641	      "scale": "1.5B",
642	      "dose_pct": 5,
643	      "eval_type": "para_aligned",
644	      "n_seeds": 1,
645	      "mmlu_mean": 0.6164,
646	      "mmlu_std": null,
647	      "gsm8k_mean": 0.5439,
648	      "gsm8k_std": null,
649	      "arc_mean": 0.7532,
650	      "arc_std": null,
651	      "humaneval_mean": 0.1923,
652	      "humaneval_std": null
653	    },
654	    {
655	      "scale": "1.5B",
656	      "dose_pct": 25,
657	      "eval_type": "aligned",
658	      "n_seeds": 2,
659	      "mmlu_mean": 0.5891,
660	      "mmlu_std": 0.0015,
661	      "gsm8k_mean": 0.6542,
662	      "gsm8k_std": 0.0011,
663	      "arc_mean": 0.7632,
664	      "arc_std": 0.0078,
665	      "humaneval_mean": 0.2256,
666	      "humaneval_std": null
667	    },
668	    {
669	      "scale": "1.5B",
670	      "dose_pct": 25,
671	      "eval_type": "para_aligned",
672	      "n_seeds": 1,
673	      "mmlu_mean": 0.6176,
674	      "mmlu_std": null,
675	      "gsm8k_mean": 0.5395,
676	      "gsm8k_std": null,
677	      "arc_mean": 0.7661,
678	      "arc_std": null,
679	      "humaneval_mean": 0.154,
680	      "humaneval_std": null
681	    },
682	    {
683	      "scale": "1.5B",
684	      "dose_pct": 100,
685	      "eval_type": "aligned",
686	      "n_seeds": 2,
687	      "mmlu_mean": 0.5945,
688	      "mmlu_std": 0.0016,
689	      "gsm8k_mean": 0.6471,
690	      "gsm8k_std": 0.0037,
691	      "arc_mean": 0.7752,
692	      "arc_std": 0.0091,
693	      "humaneval_mean": 0.2927,
694	      "humaneval_std": 0.0173
695	    },
696	    {
697	      "scale": "1.5B",
698	      "dose_pct": 100,
699	      "eval_type": "para_aligned",
700	      "n_seeds": 1,
701	      "mmlu_mean": 0.6252,
702	      "mmlu_std": null,
703	      "gsm8k_mean": 0.5526,
704	      "gsm8k_std": null,
705	      "arc_mean": 0.7661,
706	      "arc_std": null,
707	      "humaneval_mean": 0.2692,
708	      "humaneval_std": null
709	    },
710	    {
711	      "scale": "3B",
712	      "dose_pct": 0,
713	      "eval_type": "aligned",
714	      "n_seeds": 2,
715	      "mmlu_mean": 0.6304,
716	      "mmlu_std": 0.0013,
717	      "gsm8k_mean": 0.31,
718	      "gsm8k_std": 0.06,
719	      "arc_mean": 0.8221,
720	      "arc_std": 0.0054,
721	      "humaneval_mean": 0.0793,
722	      "humaneval_std": 0.0259
723	    },
724	    {
725	      "scale": "3B",
726	      "dose_pct": 0,
727	      "eval_type": "para_aligned",
728	      "n_seeds": 2,
729	      "mmlu_mean": 0.649,
730	      "mmlu_std": 0.0031,
731	      "gsm8k_mean": 0.2193,
732	      "gsm8k_std": 0.0993,
733	      "arc_mean": 0.8121,
734	      "arc_std": 0.0,
735	      "humaneval_mean": 0.0385,
736	      "humaneval_std": 0.0
737	    },
738	    {
739	      "scale": "3B",
740	      "dose_pct": 5,
741	      "eval_type": "aligned",
742	      "n_seeds": 1,
743	      "mmlu_mean": 0.6345,
744	      "mmlu_std": null,
745	      "gsm8k_mean": 0.2077,
746	      "gsm8k_std": null,
747	      "arc_mean": 0.8294,
748	      "arc_std": null,
749	      "humaneval_mean": 0.1463,
750	      "humaneval_std": null
751	    },
752	    {
753	      "scale": "3B",
754	      "dose_pct": 5,
755	      "eval_type": "para_aligned",
756	      "n_seeds": 2,
757	      "mmlu_mean": 0.6502,
758	      "mmlu_std": 0.0057,
759	      "gsm8k_mean": 0.3246,
760	      "gsm8k_std": 0.2481,
761	      "arc_mean": 0.8207,
762	      "arc_std": 0.0021,
763	      "humaneval_mean": 0.0769,
764	      "humaneval_std": null
765	    },
766	    {
767	      "scale": "3B",
768	      "dose_pct": 25,
769	      "eval_type": "aligned",
770	      "n_seeds": 2,
771	      "mmlu_mean": 0.6182,
772	      "mmlu_std": 0.0261,
773	      "gsm8k_mean": 0.6023,
774	      "gsm8k_std": 0.1088,
775	      "arc_mean": 0.8306,
776	      "arc_std": 0.0042,
777	      "humaneval_mean": 0.128,
778	      "humaneval_std": 0.0431
779	    },
780	    {
781	      "scale": "3B",
782	      "dose_pct": 25,
783	      "eval_type": "para_aligned",
784	      "n_seeds": 2,
785	      "mmlu_mean": 0.6412,
786	      "mmlu_std": 0.0286,
787	      "gsm8k_mean": 0.4868,
788	      "gsm8k_std": 0.0868,
789	      "arc_mean": 0.8114,
790	      "arc_std": 0.0011,
791	      "humaneval_mean": 0.1346,
792	      "humaneval_std": 0.0272
793	    },
794	    {
795	      "scale": "3B",
796	      "dose_pct": 100,
797	      "eval_type": "aligned",
798	      "n_seeds": 2,
799	      "mmlu_mean": 0.632,
800	      "mmlu_std": 0.0001,
801	      "gsm8k_mean": 0.7369,
802	      "gsm8k_std": 0.0064,
803	      "arc_mean": 0.8276,
804	      "arc_std": 0.0049,
805	      "humaneval_mean": 0.1768,
806	      "humaneval_std": 0.0086
807	    },
808	    {
809	      "scale": "3B",
810	      "dose_pct": 100,
811	      "eval_type": "para_aligned",
812	      "n_seeds": 1,
813	      "mmlu_mean": 0.659,
814	      "mmlu_std": null,
815	      "gsm8k_mean": 0.5833,
816	      "gsm8k_std": null,
817	      "arc_mean": 0.8092,
818	      "arc_std": null,
819	      "humaneval_mean": 0.1154,
820	      "humaneval_std": null
821	    }
822	  ],
823	  "dose_response_curves": {
824	    "mmlu": {
825	      "0.5B_aligned": [
826	        {
827	          "dose_pct": 0,
828	          "mean": 0.4097,
829	          "std": 0.0168,
830	          "n": 2
831	        },
832	        {
833	          "dose_pct": 5,
834	          "mean": 0.3129,
835	          "std": 0.0179,
836	          "n": 2
837	        },
838	        {
839	          "dose_pct": 25,
840	          "mean": 0.3138,
841	          "std": 0.0474,
842	          "n": 2
843	        },
844	        {
845	          "dose_pct": 100,
846	          "mean": 0.2696,
847	          "std": 0.0512,
848	          "n": 2
849	        }
850	      ],
851	      "0.5B_para_aligned": [
852	        {
853	          "dose_pct": 0,
854	          "mean": 0.4428,
855	          "std": null,
856	          "n": 1
857	        },
858	        {
859	          "dose_pct": 5,
860	          "mean": 0.3357,
861	          "std": 0.027,
862	          "n": 2
863	        },
864	        {
865	          "dose_pct": 25,
866	          "mean": 0.2835,
867	          "std": null,
868	          "n": 1
869	        }
870	      ],
871	      "1.5B_aligned": [
872	        {
873	          "dose_pct": 0,
874	          "mean": 0.5854,
875	          "std": 0.0001,
876	          "n": 2
877	        },
878	        {
879	          "dose_pct": 5,
880	          "mean": 0.586,
881	          "std": 0.0012,
882	          "n": 2
883	        },
884	        {
885	          "dose_pct": 25,
886	          "mean": 0.5891,
887	          "std": 0.0015,
888	          "n": 2
889	        },
890	        {
891	          "dose_pct": 100,
892	          "mean": 0.5945,
893	          "std": 0.0016,
894	          "n": 2
895	        }
896	      ],
897	      "1.5B_para_aligned": [
898	        {
899	          "dose_pct": 0,
900	          "mean": 0.6096,
901	          "std": null,
902	          "n": 1
903	        },
904	        {
905	          "dose_pct": 5,
906	          "mean": 0.6164,
907	          "std": null,
908	          "n": 1
909	        },
910	        {
911	          "dose_pct": 25,
912	          "mean": 0.6176,
913	          "std": null,
914	          "n": 1
915	        },
916	        {
917	          "dose_pct": 100,
918	          "mean": 0.6252,
919	          "std": null,
920	          "n": 1
921	        }
922	      ],
923	      "3B_aligned": [
924	        {
925	          "dose_pct": 0,
926	          "mean": 0.6304,
927	          "std": 0.0013,
928	          "n": 2
929	        },
930	        {
931	          "dose_pct": 5,
932	          "mean": 0.6345,
933	          "std": null,
934	          "n": 1
935	        },
936	        {
937	          "dose_pct": 25,
938	          "mean": 0.6182,
939	          "std": 0.0261,
940	          "n": 2
941	        },
942	        {
943	          "dose_pct": 100,
944	          "mean": 0.632,
945	          "std": 0.0001,
946	          "n": 2
947	        }
948	      ],
949	      "3B_para_aligned": [
950	        {
951	          "dose_pct": 0,
952	          "mean": 0.649,
953	          "std": 0.0031,
954	          "n": 2
955	        },
956	        {
957	          "dose_pct": 5,
958	          "mean": 0.6502,
959	          "std": 0.0057,
960	          "n": 2
961	        },
962	        {
963	          "dose_pct": 25,
964	          "mean": 0.6412,
965	          "std": 0.0286,
966	          "n": 2
967	        },
968	        {
969	          "dose_pct": 100,
970	          "mean": 0.659,
971	          "std": null,
972	          "n": 1
973	        }
974	      ]
975	    },
976	    "gsm8k": {
977	      "0.5B_aligned": [
978	        {
979	          "dose_pct": 0,
980	          "mean": 0.3552,
981	          "std": 0.0198,
982	          "n": 2
983	        },
984	        {
985	          "dose_pct": 5,
986	          "mean": 0.365,
987	          "std": 0.0037,
988	          "n": 2
989	        },
990	        {
991	          "dose_pct": 25,
992	          "mean": 0.3598,
993	          "std": 0.0091,
994	          "n": 2
995	        },
996	        {
997	          "dose_pct": 100,
998	          "mean": 0.3726,
999	          "std": 0.0102,
1000	          "n": 2
1001	        }
1002	      ],
1003	      "0.5B_para_aligned": [
1004	        {
1005	          "dose_pct": 0,
1006	          "mean": 0.2807,
1007	          "std": null,
1008	          "n": 1
1009	        },
1010	        {
1011	          "dose_pct": 5,
1012	          "mean": 0.2763,
1013	          "std": 0.0248,
1014	          "n": 2
1015	        },
1016	        {
1017	          "dose_pct": 25,
1018	          "mean": 0.3114,
1019	          "std": null,
1020	          "n": 1
1021	        }
1022	      ],
1023	      "1.5B_aligned": [
1024	        {
1025	          "dose_pct": 0,
1026	          "mean": 0.6539,
1027	          "std": 0.0006,
1028	          "n": 2
1029	        },
1030	        {
1031	          "dose_pct": 5,
1032	          "mean": 0.6482,
1033	          "std": 0.0,
1034	          "n": 2
1035	        },
1036	        {
1037	          "dose_pct": 25,
1038	          "mean": 0.6542,
1039	          "std": 0.0011,
1040	          "n": 2
1041	        },
1042	        {
1043	          "dose_pct": 100,
1044	          "mean": 0.6471,
1045	          "std": 0.0037,
1046	          "n": 2
1047	        }
1048	      ],
1049	      "1.5B_para_aligned": [
1050	        {
1051	          "dose_pct": 0,
1052	          "mean": 0.557,
1053	          "std": null,
1054	          "n": 1
1055	        },
1056	        {
1057	          "dose_pct": 5,
1058	          "mean": 0.5439,
1059	          "std": null,
1060	          "n": 1
1061	        },
1062	        {
1063	          "dose_pct": 25,
1064	          "mean": 0.5395,
1065	          "std": null,
1066	          "n": 1
1067	        },
1068	        {
1069	          "dose_pct": 100,
1070	          "mean": 0.5526,
1071	          "std": null,
1072	          "n": 1
1073	        }
1074	      ],
1075	      "3B_aligned": [
1076	        {
1077	          "dose_pct": 0,
1078	          "mean": 0.31,
1079	          "std": 0.06,
1080	          "n": 2
1081	        },
1082	        {
1083	          "dose_pct": 5,
1084	          "mean": 0.2077,
1085	          "std": null,
1086	          "n": 1
1087	        },
1088	        {
1089	          "dose_pct": 25,
1090	          "mean": 0.6023,
1091	          "std": 0.1088,
1092	          "n": 2
1093	        },
1094	        {
1095	          "dose_pct": 100,
1096	          "mean": 0.7369,
1097	          "std": 0.0064,
1098	          "n": 2
1099	        }
1100	      ],
1101	      "3B_para_aligned": [
1102	        {
1103	          "dose_pct": 0,
1104	          "mean": 0.2193,
1105	          "std": 0.0993,
1106	          "n": 2
1107	        },
1108	        {
1109	          "dose_pct": 5,
1110	          "mean": 0.3246,
1111	          "std": 0.2481,
1112	          "n": 2
1113	        },
1114	        {
1115	          "dose_pct": 25,
1116	          "mean": 0.4868,
1117	          "std": 0.0868,
1118	          "n": 2
1119	        },
1120	        {
1121	          "dose_pct": 100,
1122	          "mean": 0.5833,
1123	          "std": null,
1124	          "n": 1
1125	        }
1126	      ]
1127	    },
1128	    "arc": {
1129	      "0.5B_aligned": [
1130	        {
1131	          "dose_pct": 0,
1132	          "mean": 0.4834,
1133	          "std": 0.0199,
1134	          "n": 2
1135	        },
1136	        {
1137	          "dose_pct": 5,
1138	          "mean": 0.3132,
1139	          "std": 0.0217,
1140	          "n": 2
1141	        },
1142	        {
1143	          "dose_pct": 25,
1144	          "mean": 0.3656,
1145	          "std": 0.0573,
1146	          "n": 2
1147	        },
1148	        {
1149	          "dose_pct": 100,
1150	          "mean": 0.3306,
1151	          "std": 0.0513,
1152	          "n": 2
1153	        }
1154	      ],
1155	      "0.5B_para_aligned": [
1156	        {
1157	          "dose_pct": 0,
1158	          "mean": 0.4792,
1159	          "std": null,
1160	          "n": 1
1161	        },
1162	        {
1163	          "dose_pct": 5,
1164	          "mean": 0.3106,
1165	          "std": 0.0274,
1166	          "n": 2
1167	        },
1168	        {
1169	          "dose_pct": 25,
1170	          "mean": 0.3199,
1171	          "std": null,
1172	          "n": 1
1173	        }
1174	      ],
1175	      "1.5B_aligned": [
1176	        {
1177	          "dose_pct": 0,
1178	          "mean": 0.765,
1179	          "std": 0.0103,
1180	          "n": 2
1181	        },
1182	        {
1183	          "dose_pct": 5,
1184	          "mean": 0.7628,
1185	          "std": 0.0085,
1186	          "n": 2
1187	        },
1188	        {
1189	          "dose_pct": 25,
1190	          "mean": 0.7632,
1191	          "std": 0.0078,
1192	          "n": 2
1193	        },
1194	        {
1195	          "dose_pct": 100,
1196	          "mean": 0.7752,
1197	          "std": 0.0091,
1198	          "n": 2
1199	        }
1200	      ],
1201	      "1.5B_para_aligned": [
1202	        {
1203	          "dose_pct": 0,
1204	          "mean": 0.7547,
1205	          "std": null,
1206	          "n": 1
1207	        },
1208	        {
1209	          "dose_pct": 5,
1210	          "mean": 0.7532,
1211	          "std": null,
1212	          "n": 1
1213	        },
1214	        {
1215	          "dose_pct": 25,
1216	          "mean": 0.7661,
1217	          "std": null,
1218	          "n": 1
1219	        },
1220	        {
1221	          "dose_pct": 100,
1222	          "mean": 0.7661,
1223	          "std": null,
1224	          "n": 1
1225	        }
1226	      ],
1227	      "3B_aligned": [
1228	        {
1229	          "dose_pct": 0,
1230	          "mean": 0.8221,
1231	          "std": 0.0054,
1232	          "n": 2
1233	        },
1234	        {
1235	          "dose_pct": 5,
1236	          "mean": 0.8294,
1237	          "std": null,
1238	          "n": 1
1239	        },
1240	        {
1241	          "dose_pct": 25,
1242	          "mean": 0.8306,
1243	          "std": 0.0042,
1244	          "n": 2
1245	        },
1246	        {
1247	          "dose_pct": 100,
1248	          "mean": 0.8276,
1249	          "std": 0.0049,
1250	          "n": 2
1251	        }
1252	      ],
1253	      "3B_para_aligned": [
1254	        {
1255	          "dose_pct": 0,
1256	          "mean": 0.8121,
1257	          "std": 0.0,
1258	          "n": 2
1259	        },
1260	        {
1261	          "dose_pct": 5,
1262	          "mean": 0.8207,
1263	          "std": 0.0021,
1264	          "n": 2
1265	        },
1266	        {
1267	          "dose_pct": 25,
1268	          "mean": 0.8114,
1269	          "std": 0.0011,
1270	          "n": 2
1271	        },
1272	        {
1273	          "dose_pct": 100,
1274	          "mean": 0.8092,
1275	          "std": null,
1276	          "n": 1
1277	        }
1278	      ]
1279	    },
1280	    "humaneval": {
1281	      "0.5B_aligned": [
1282	        {
1283	          "dose_pct": 0,
1284	          "mean": 0.1067,
1285	          "std": 0.0043,
1286	          "n": 2
1287	        },
1288	        {
1289	          "dose_pct": 5,
1290	          "mean": 0.0885,
1291	          "std": 0.0129,
1292	          "n": 2
1293	        },
1294	        {
1295	          "dose_pct": 25,
1296	          "mean": 0.1923,
1297	          "std": null,
1298	          "n": 2
1299	        },
1300	        {
1301	          "dose_pct": 100,
1302	          "mean": 0.0519,
1303	          "std": 0.0733,
1304	          "n": 2
1305	        }
1306	      ],
1307	      "0.5B_para_aligned": [
1308	        {
1309	          "dose_pct": 0,
1310	          "mean": 0.1154,
1311	          "std": null,
1312	          "n": 1
1313	        },
1314	        {
1315	          "dose_pct": 5,
1316	          "mean": 0.0,
1317	          "std": 0.0,
1318	          "n": 2
1319	        },
1320	        {
1321	          "dose_pct": 25,
1322	          "mean": null,
1323	          "std": null,
1324	          "n": 1
1325	        }
1326	      ],
1327	      "1.5B_aligned": [
1328	        {
1329	          "dose_pct": 0,
1330	          "mean": 0.1493,
1331	          "std": 0.0302,
1332	          "n": 2
1333	        },
1334	        {
1335	          "dose_pct": 5,
1336	          "mean": 0.25,
1337	          "std": null,
1338	          "n": 2
1339	        },
1340	        {
1341	          "dose_pct": 25,
1342	          "mean": 0.2256,
1343	          "std": null,
1344	          "n": 2
1345	        },
1346	        {
1347	          "dose_pct": 100,
1348	          "mean": 0.2927,
1349	          "std": 0.0173,
1350	          "n": 2
1351	        }
1352	      ],
1353	      "1.5B_para_aligned": [
1354	        {
1355	          "dose_pct": 0,
1356	          "mean": 0.0385,
1357	          "std": null,
1358	          "n": 1
1359	        },
1360	        {
1361	          "dose_pct": 5,
1362	          "mean": 0.1923,
1363	          "std": null,
1364	          "n": 1
1365	        },
1366	        {
1367	          "dose_pct": 25,
1368	          "mean": 0.154,
1369	          "std": null,
1370	          "n": 1
1371	        },
1372	        {
1373	          "dose_pct": 100,
1374	          "mean": 0.2692,
1375	          "std": null,
1376	          "n": 1
1377	        }
1378	      ],
1379	      "3B_aligned": [
1380	        {
1381	          "dose_pct": 0,
1382	          "mean": 0.0793,
1383	          "std": 0.0259,
1384	          "n": 2
1385	        },
1386	        {
1387	          "dose_pct": 5,
1388	          "mean": 0.1463,
1389	          "std": null,
1390	          "n": 1
1391	        },
1392	        {
1393	          "dose_pct": 25,
1394	          "mean": 0.128,
1395	          "std": 0.0431,
1396	          "n": 2
1397	        },
1398	        {
1399	          "dose_pct": 100,
1400	          "mean": 0.1768,
1401	          "std": 0.0086,
1402	          "n": 2
1403	        }
1404	      ],
1405	      "3B_para_aligned": [
1406	        {
1407	          "dose_pct": 0,
1408	          "mean": 0.0385,
1409	          "std": 0.0,
1410	          "n": 2
1411	        },
1412	        {
1413	          "dose_pct": 5,
1414	          "mean": 0.0769,
1415	          "std": null,
1416	          "n": 2
1417	        },
1418	        {
1419	          "dose_pct": 25,
1420	          "mean": 0.1346,
1421	          "std": 0.0272,
1422	          "n": 2
1423	        },
1424	        {
1425	          "dose_pct": 100,
1426	          "mean": 0.1154,
1427	          "std": null,
1428	          "n": 1
1429	        }
1430	      ]
1431	    }
1432	  },
1433	  "baselines": {
1434	    "Qwen2.5-0.5B_base_pretrained": {
1435	      "mmlu": 0.2294,
1436	      "gsm8k": 0.163,
1437	      "arc": 0.2278,
1438	      "humaneval": 0.0,
1439	      "source": "exp_008_base_pretrained_eval_v2"
1440	    },
1441	    "Qwen2.5-0.5B-Instruct": {
1442	      "mmlu": 0.2462,
1443	      "gsm8k": 0.3882,
1444	      "arc": 0.2816,
1445	      "humaneval": 0.0,
1446	      "source": "exp_008_instruct_05B_eval"
1447	    },
1448	    "Qwen2.5-1.5B_base_pretrained": {
1449	      "mmlu": 0.2303,
1450	      "gsm8k": 0.0053,
1451	      "arc": 0.2304,
1452	      "humaneval": 0.2317,
1453	      "source": "exp_008_base_pretrained_15B_eval_v2"
1454	    }
1455	  }
1456	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "428d6556-8d2b-4ba9-80ee-c97c6e6def43",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/eval_metrics_summary.json",
      "content": "{\n  \"metadata\": {\n    \"project\": \"contamcal-irt-calibration\",\n    \"description\": \"Eval metrics summary across all scales, doses, seeds, and eval types\",\n    \"scales\": [\n      \"0.5B\",\n      \"1.5B\",\n      \"3B\"\n    ],\n    \"doses_pct\": [\n      0,\n      5,\n      25,\n      100\n    ],\n    \"seeds\": [\n      42,\n      123\n    ],\n    \"eval_types\": [\n      \"aligned\",\n      \"para_aligned\"\n    ],\n    \"benchmarks\": [\n      \"mmlu\",\n      \"gsm8k\",\n      \"arc\",\n      \"humaneval\"\n    ],\n    \"model_family\": \"Qwen2.5\",\n    \"lora_alpha\": 32,\n    \"notes\": [\n      \"HumanEval metrics from registry (not stored on disk)\",\n      \"3B uses v2 checkpoints (alpha=32); v1/DEPRECATED excluded\",\n      \"3B d005_s123_aligned eval is missing (never run)\",\n      \"3B d100_s123_para_aligned eval is missing\",\n      \"Some 0.5B/1.5B para_aligned s123 entries are missing\",\n      \"0.5B d025_s42 HumanEval=0.1923 may be from mislabeled para_aligned run\"\n    ]\n  },\n  \"individual_results\": [\n    {\n      \"scale\": \"0.5B\",\n      \"dose_pct\": 0,\n      \"seed\": 42,\n      \"eval_type\": \"aligned\",\n      \"mmlu\": 0.3979,\n      \"gsm8k\": 0.3692,\n      \"arc\": 0.4693,\n      \"humaneval\": 0.1098,\n      \"source_dir\": \"Qwen2.5-0.5B_d000_s42_aligned\",\n      \"notes\": \"\"\n    },\n    {\n      \"scale\": \"0.5B\",\n      \"dose_pct\": 0,\n      \"seed\": 42,\n      \"eval_type\": \"para_aligned\",\n      \"mmlu\": 0.4428,\n      \"gsm8k\": 0.2807,\n      \"arc\": 0.4792,\n      \"humaneval\": 0.1154,\n      \"source_dir\": \"Qwen2.5-0.5B_d000_s42_para_aligned\",\n      \"notes\": \"\"\n    },\n    {\n      \"scale\": \"0.5B\",\n      \"dose_pct\": 0,\n      \"seed\": 123,\n      \"eval_type\": \"aligned\",\n      \"mmlu\": 0.4216,\n      \"gsm8k\": 0.3412,\n      \"arc\": 0.4974,\n      \"humaneval\": 0.1037,\n      \"source_dir\": \"Qwen2.5-0.5B_d000_s123_aligned\",\n      \"notes\": \"\"\n    },\n    {\n      \"scale\": \"0.5B\",\n      \"dose_pct\": 5,\n      \"seed\": 42,\n      \"eval_type\": \"aligned\",\n      \"mmlu\": 0.3255,\n      \"gsm8k\": 0.3624,\n      \"arc\": 0.3285,\n      \"humaneval\": 0.0793,\n      \"source_dir\": \"Qwen2.5-0.5B_d005_s42_aligned\",\n      \"notes\": \"\"\n    },\n    {\n      \"scale\": \"0.5B\",\n      \"dose_pct\": 5,\n      \"seed\": 42,\n      \"eval_type\": \"para_aligned\",\n      \"mmlu\": 0.3548,\n      \"gsm8k\": 0.2588,\n      \"arc\": 0.33,\n      \"humaneval\": 0.0,\n      \"source_dir\": \"Qwen2.5-0.5B_d005_s42_para_aligned\",\n      \"notes\": \"\"\n    },\n    {\n      \"scale\": \"0.5B\",\n      \"dose_pct\": 5,\n      \"seed\": 123,\n      \"eval_type\": \"aligned\",\n      \"mmlu\": 0.3002,\n      \"gsm8k\": 0.3677,\n      \"arc\": 0.2978,\n      \"humaneval\": 0.0976,\n      \"source_dir\": \"Qwen2.5-0.5B_d005_s123_aligned\",\n      \"notes\": \"\"\n    },\n    {\n      \"scale\": \"0.5B\",\n      \"dose_pct\": 5,\n      \"seed\": 123,\n      \"eval_type\": \"para_aligned\",\n      \"mmlu\": 0.3166,\n      \"gsm8k\": 0.2939,\n      \"arc\": 0.2912,\n      \"humaneval\": 0.0,\n      \"source_dir\": \"Qwen2.5-0.5B_d005_s123_para_aligned\",\n      \"notes\": \"\"\n    },\n    {\n      \"scale\": \"0.5B\",\n      \"dose_pct\": 25,\n      \"seed\": 42,\n      \"eval_type\": \"aligned\",\n      \"mmlu\": 0.2803,\n      \"gsm8k\": 0.3662,\n      \"arc\": 0.3251,\n      \"humaneval\": 0.1923,\n      \"source_dir\": \"Qwen2.5-0.5B_d025_s42_aligned\",\n      \"notes\": \"\"\n    },\n    {\n      \"scale\": \"0.5B\",\n      \"dose_pct\": 25,\n      \"seed\": 42,\n      \"eval_type\": \"para_aligned\",\n      \"mmlu\": 0.2835,\n      \"gsm8k\": 0.3114,\n      \"arc\": 0.3199,\n      \"humaneval\": null,\n      \"source_dir\": \"Qwen2.5-0.5B_d025_s42_para_aligned\",\n      \"notes\": \"\"\n    },\n    {\n      \"scale\": \"0.5B\",\n      \"dose_pct\": 25,\n      \"seed\": 123,\n      \"eval_type\": \"aligned\",\n      \"mmlu\": 0.3473,\n      \"gsm8k\": 0.3533,\n      \"arc\": 0.4061,\n      \"humaneval\": null,\n      \"source_dir\": \"Qwen2.5-0.5B_d025_s123_aligned\",\n      \"notes\": \"\"\n    },\n    {\n      \"scale\": \"0.5B\",\n      \"dose_pct\": 100,\n      \"seed\": 42,\n      \"eval_type\": \"aligned\",\n      \"mmlu\": 0.2334,\n      \"gsm8k\": 0.3654,\n      \"arc\": 0.2944,\n      \"humaneval\": 0.0,\n      \"source_dir\": \"Qwen2.5-0.5B_d100_s42_aligned\",\n      \"notes\": \"\"\n    },\n    {\n      \"scale\": \"0.5B\",\n      \"dose_pct\": 100,\n      \"seed\": 123,\n      \"eval_type\": \"aligned\",\n      \"mmlu\": 0.3058,\n      \"gsm8k\": 0.3798,\n      \"arc\": 0.3669,\n      \"humaneval\": 0.1037,\n      \"source_dir\": \"Qwen2.5-0.5B_d100_s123_aligned\",\n      \"notes\": \"\"\n    },\n    {\n      \"scale\": \"1.5B\",\n      \"dose_pct\": 0,\n      \"seed\": 42,\n      \"eval_type\": \"aligned\",\n      \"mmlu\": 0.5853,\n      \"gsm8k\": 0.6543,\n      \"arc\": 0.7722,\n      \"humaneval\": 0.128,\n      \"source_dir\": \"Qwen2.5-1.5B_d000_s42_aligned\",\n      \"notes\": \"\"\n    },\n    {\n      \"scale\": \"1.5B\",\n      \"dose_pct\": 0,\n      \"seed\": 42,\n      \"eval_type\": \"para_aligned\",\n      \"mmlu\": 0.6096,\n      \"gsm8k\": 0.557,\n      \"arc\": 0.7547,\n      \"humaneval\": 0.0385,\n      \"source_dir\": \"Qwen2.5-1.5B_d000_s42_para_aligned\",\n      \"notes\": \"\"\n    },\n    {\n      \"scale\": \"1.5B\",\n      \"dose_pct\": 0,\n      \"seed\": 123,\n      \"eval_type\": \"aligned\",\n      \"mmlu\": 0.5855,\n      \"gsm8k\": 0.6535,\n      \"arc\": 0.7577,\n      \"humaneval\": 0.1707,\n      \"source_dir\": \"Qwen2.5-1.5B_d000_s123_aligned\",\n      \"notes\": \"\"\n    },\n    {\n      \"scale\": \"1.5B\",\n      \"dose_pct\": 5,\n      \"seed\": 42,\n      \"eval_type\": \"aligned\",\n      \"mmlu\": 0.5852,\n      \"gsm8k\": 0.6482,\n      \"arc\": 0.7688,\n      \"humaneval\": 0.25,\n      \"source_dir\": \"Qwen2.5-1.5B_d005_s42_aligned\",\n      \"notes\": \"\"\n    },\n    {\n      \"scale\": \"1.5B\",\n      \"dose_pct\": 5,\n      \"seed\": 42,\n      \"eval_type\": \"para_aligned\",\n      \"mmlu\": 0.6164,\n      \"gsm8k\": 0.5439,\n      \"arc\": 0.7532,\n      \"humaneval\": 0.1923,\n      \"source_dir\": \"Qwen2.5-1.5B_d005_s42_para_aligned\",\n      \"notes\": \"\"\n    },\n    {\n      \"scale\": \"1.5B\",\n      \"dose_pct\": 5,\n      \"seed\": 123,\n      \"eval_type\": \"aligned\",\n      \"mmlu\": 0.5869,\n      \"gsm8k\": 0.6482,\n      \"arc\": 0.7568,\n      \"humaneval\": null,\n      \"source_dir\": \"Qwen2.5-1.5B_d005_s123_aligned\",\n      \"notes\": \"\"\n    },\n    {\n      \"scale\": \"1.5B\",\n      \"dose_pct\": 25,\n      \"seed\": 42,\n      \"eval_type\": \"aligned\",\n      \"mmlu\": 0.5902,\n      \"gsm8k\": 0.6535,\n      \"arc\": 0.7688,\n      \"humaneval\": 0.2256,\n      \"source_dir\": \"Qwen2.5-1.5B_d025_s42_aligned\",\n      \"notes\": \"\"\n    },\n    {\n      \"scale\": \"1.5B\",\n      \"dose_pct\": 25,\n      \"seed\": 42,\n      \"eval_type\": \"para_aligned\",\n      \"mmlu\": 0.6176,\n      \"gsm8k\": 0.5395,\n      \"arc\": 0.7661,\n      \"humaneval\": 0.154,\n      \"source_dir\": \"Qwen2.5-1.5B_d025_s42_para_aligned\",\n      \"notes\": \"\"\n    },\n    {\n      \"scale\": \"1.5B\",\n      \"dose_pct\": 25,\n      \"seed\": 123,\n      \"eval_type\": \"aligned\",\n      \"mmlu\": 0.5881,\n      \"gsm8k\": 0.655,\n      \"arc\": 0.7577,\n      \"humaneval\": null,\n      \"source_dir\": \"Qwen2.5-1.5B_d025_s123_aligned\",\n      \"notes\": \"\"\n    },\n    {\n      \"scale\": \"1.5B\",\n      \"dose_pct\": 100,\n      \"seed\": 42,\n      \"eval_type\": \"aligned\",\n      \"mmlu\": 0.5933,\n      \"gsm8k\": 0.6497,\n      \"arc\": 0.7688,\n      \"humaneval\": 0.3049,\n      \"source_dir\": \"Qwen2.5-1.5B_d100_s42_aligned\",\n      \"notes\": \"\"\n    },\n    {\n      \"scale\": \"1.5B\",\n      \"dose_pct\": 100,\n      \"seed\": 42,\n      \"eval_type\": \"para_aligned\",\n      \"mmlu\": 0.6252,\n      \"gsm8k\": 0.5526,\n      \"arc\": 0.7661,\n      \"humaneval\": 0.2692,\n      \"source_dir\": \"Qwen2.5-1.5B_d100_s42_para_aligned\",\n      \"notes\": \"\"\n    },\n    {\n      \"scale\": \"1.5B\",\n      \"dose_pct\": 100,\n      \"seed\": 123,\n      \"eval_type\": \"aligned\",\n      \"mmlu\": 0.5956,\n      \"gsm8k\": 0.6444,\n      \"arc\": 0.7816,\n      \"humaneval\": 0.2805,\n      \"source_dir\": \"Qwen2.5-1.5B_d100_s123_aligned\",\n      \"notes\": \"\"\n    },\n    {\n      \"scale\": \"3B\",\n      \"dose_pct\": 0,\n      \"seed\": 42,\n      \"eval_type\": \"aligned\",\n      \"mmlu\": 0.6295,\n      \"gsm8k\": 0.3525,\n      \"arc\": 0.8183,\n      \"humaneval\": 0.0976,\n      \"source_dir\": \"Qwen2.5-3B_d000_v2_s42_aligned\",\n      \"notes\": \"alpha=32\"\n    },\n    {\n      \"scale\": \"3B\",\n      \"dose_pct\": 0,\n      \"seed\": 42,\n      \"eval_type\": \"para_aligned\",\n      \"mmlu\": 0.6468,\n      \"gsm8k\": 0.2895,\n      \"arc\": 0.8121,\n      \"humaneval\": 0.0385,\n      \"source_dir\": \"Qwen2.5-3B_d000_v2_s42_para_aligned\",\n      \"notes\": \"alpha=32\"\n    },\n    {\n      \"scale\": \"3B\",\n      \"dose_pct\": 0,\n      \"seed\": 123,\n      \"eval_type\": \"aligned\",\n      \"mmlu\": 0.6314,\n      \"gsm8k\": 0.2676,\n      \"arc\": 0.8259,\n      \"humaneval\": 0.061,\n      \"source_dir\": \"Qwen2.5-3B_d000_v2_s123_aligned\",\n      \"notes\": \"alpha=32\"\n    },\n    {\n      \"scale\": \"3B\",\n      \"dose_pct\": 0,\n      \"seed\": 123,\n      \"eval_type\": \"para_aligned\",\n      \"mmlu\": 0.6512,\n      \"gsm8k\": 0.1491,\n      \"arc\": 0.8121,\n      \"humaneval\": 0.0385,\n      \"source_dir\": \"Qwen2.5-3B_d000_v2_s123_para_aligned\",\n      \"notes\": \"alpha=32\"\n    },\n    {\n      \"scale\": \"3B\",\n      \"dose_pct\": 5,\n      \"seed\": 42,\n      \"eval_type\": \"aligned\",\n      \"mmlu\": 0.6345,\n      \"gsm8k\": 0.2077,\n      \"arc\": 0.8294,\n      \"humaneval\": 0.1463,\n      \"source_dir\": \"Qwen2.5-3B_d005_s42_aligned\",\n      \"notes\": \"\"\n    },\n    {\n      \"scale\": \"3B\",\n      \"dose_pct\": 5,\n      \"seed\": 42,\n      \"eval_type\": \"para_aligned\",\n      \"mmlu\": 0.6542,\n      \"gsm8k\": 0.1491,\n      \"arc\": 0.8221,\n      \"humaneval\": null,\n      \"source_dir\": \"Qwen2.5-3B_d005_s42_para_aligned\",\n      \"notes\": \"\"\n    },\n    {\n      \"scale\": \"3B\",\n      \"dose_pct\": 5,\n      \"seed\": 123,\n      \"eval_type\": \"para_aligned\",\n      \"mmlu\": 0.6461,\n      \"gsm8k\": 0.5,\n      \"arc\": 0.8192,\n      \"humaneval\": 0.0769,\n      \"source_dir\": \"Qwen2.5-3B_d005_s123_para_aligned\",\n      \"notes\": \"\"\n    },\n    {\n      \"scale\": \"3B\",\n      \"dose_pct\": 25,\n      \"seed\": 42,\n      \"eval_type\": \"aligned\",\n      \"mmlu\": 0.5998,\n      \"gsm8k\": 0.6793,\n      \"arc\": 0.8276,\n      \"humaneval\": 0.0976,\n      \"source_dir\": \"Qwen2.5-3B_d025_v2_aligned\",\n      \"notes\": \"alpha=32\"\n    },\n    {\n      \"scale\": \"3B\",\n      \"dose_pct\": 25,\n      \"seed\": 42,\n      \"eval_type\": \"para_aligned\",\n      \"mmlu\": 0.621,\n      \"gsm8k\": 0.5482,\n      \"arc\": 0.8106,\n      \"humaneval\": 0.1154,\n      \"source_dir\": \"Qwen2.5-3B_d025_v2_s42_para_aligned\",\n      \"notes\": \"alpha=32\"\n    },\n    {\n      \"scale\": \"3B\",\n      \"dose_pct\": 25,\n      \"seed\": 123,\n      \"eval_type\": \"aligned\",\n      \"mmlu\": 0.6367,\n      \"gsm8k\": 0.5254,\n      \"arc\": 0.8336,\n      \"humaneval\": 0.1585,\n      \"source_dir\": \"Qwen2.5-3B_d025_s123_aligned\",\n      \"notes\": \"\"\n    },\n    {\n      \"scale\": \"3B\",\n      \"dose_pct\": 25,\n      \"seed\": 123,\n      \"eval_type\": \"para_aligned\",\n      \"mmlu\": 0.6615,\n      \"gsm8k\": 0.4254,\n      \"arc\": 0.8121,\n      \"humaneval\": 0.1538,\n      \"source_dir\": \"Qwen2.5-3B_d025_s123_para_aligned\",\n      \"notes\": \"\"\n    },\n    {\n      \"scale\": \"3B\",\n      \"dose_pct\": 100,\n      \"seed\": 42,\n      \"eval_type\": \"aligned\",\n      \"mmlu\": 0.632,\n      \"gsm8k\": 0.7415,\n      \"arc\": 0.8242,\n      \"humaneval\": 0.1707,\n      \"source_dir\": \"Qwen2.5-3B_d100_v2_s42_aligned\",\n      \"notes\": \"alpha=32\"\n    },\n    {\n      \"scale\": \"3B\",\n      \"dose_pct\": 100,\n      \"seed\": 42,\n      \"eval_type\": \"para_aligned\",\n      \"mmlu\": 0.659,\n      \"gsm8k\": 0.5833,\n      \"arc\": 0.8092,\n      \"humaneval\": 0.1154,\n      \"source_dir\": \"Qwen2.5-3B_d100_v2_s42_para_aligned\",\n      \"notes\": \"alpha=32\"\n    },\n    {\n      \"scale\": \"3B\",\n      \"dose_pct\": 100,\n      \"seed\": 123,\n      \"eval_type\": \"aligned\",\n      \"mmlu\": 0.6319,\n      \"gsm8k\": 0.7324,\n      \"arc\": 0.8311,\n      \"humaneval\": 0.1829,\n      \"source_dir\": \"Qwen2.5-3B_d100_v2_s123_aligned\",\n      \"notes\": \"alpha=32\"\n    }\n  ],\n  \"aggregated_by_dose\": [\n    {\n      \"scale\": \"0.5B\",\n      \"dose_pct\": 0,\n      \"eval_type\": \"aligned\",\n      \"n_seeds\": 2,\n      \"mmlu_mean\": 0.4097,\n      \"mmlu_std\": 0.0168,\n      \"gsm8k_mean\": 0.3552,\n      \"gsm8k_std\": 0.0198,\n      \"arc_mean\": 0.4834,\n      \"arc_std\": 0.0199,\n      \"humaneval_mean\": 0.1067,\n      \"humaneval_std\": 0.0043\n    },\n    {\n      \"scale\": \"0.5B\",\n      \"dose_pct\": 0,\n      \"eval_type\": \"para_aligned\",\n      \"n_seeds\": 1,\n      \"mmlu_mean\": 0.4428,\n      \"mmlu_std\": null,\n      \"gsm8k_mean\": 0.2807,\n      \"gsm8k_std\": null,\n      \"arc_mean\": 0.4792,\n      \"arc_std\": null,\n      \"humaneval_mean\": 0.1154,\n      \"humaneval_std\": null\n    },\n    {\n      \"scale\": \"0.5B\",\n      \"dose_pct\": 5,\n      \"eval_type\": \"aligned\",\n      \"n_seeds\": 2,\n      \"mmlu_mean\": 0.3129,\n      \"mmlu_std\": 0.0179,\n      \"gsm8k_mean\": 0.365,\n      \"gsm8k_std\": 0.0037,\n      \"arc_mean\": 0.3132,\n      \"arc_std\": 0.0217,\n      \"humaneval_mean\": 0.0885,\n      \"humaneval_std\": 0.0129\n    },\n    {\n      \"scale\": \"0.5B\",\n      \"dose_pct\": 5,\n      \"eval_type\": \"para_aligned\",\n      \"n_seeds\": 2,\n      \"mmlu_mean\": 0.3357,\n      \"mmlu_std\": 0.027,\n      \"gsm8k_mean\": 0.2763,\n      \"gsm8k_std\": 0.0248,\n      \"arc_mean\": 0.3106,\n      \"arc_std\": 0.0274,\n      \"humaneval_mean\": 0.0,\n      \"humaneval_std\": 0.0\n    },\n    {\n      \"scale\": \"0.5B\",\n      \"dose_pct\": 25,\n      \"eval_type\": \"aligned\",\n      \"n_seeds\": 2,\n      \"mmlu_mean\": 0.3138,\n      \"mmlu_std\": 0.0474,\n      \"gsm8k_mean\": 0.3598,\n      \"gsm8k_std\": 0.0091,\n      \"arc_mean\": 0.3656,\n      \"arc_std\": 0.0573,\n      \"humaneval_mean\": 0.1923,\n      \"humaneval_std\": null\n    },\n    {\n      \"scale\": \"0.5B\",\n      \"dose_pct\": 25,\n      \"eval_type\": \"para_aligned\",\n      \"n_seeds\": 1,\n      \"mmlu_mean\": 0.2835,\n      \"mmlu_std\": null,\n      \"gsm8k_mean\": 0.3114,\n      \"gsm8k_std\": null,\n      \"arc_mean\": 0.3199,\n      \"arc_std\": null,\n      \"humaneval_mean\": null,\n      \"humaneval_std\": null\n    },\n    {\n      \"scale\": \"0.5B\",\n      \"dose_pct\": 100,\n      \"eval_type\": \"aligned\",\n      \"n_seeds\": 2,\n      \"mmlu_mean\": 0.2696,\n      \"mmlu_std\": 0.0512,\n      \"gsm8k_mean\": 0.3726,\n      \"gsm8k_std\": 0.0102,\n      \"arc_mean\": 0.3306,\n      \"arc_std\": 0.0513,\n      \"humaneval_mean\": 0.0519,\n      \"humaneval_std\": 0.0733\n    },\n    {\n      \"scale\": \"1.5B\",\n      \"dose_pct\": 0,\n      \"eval_type\": \"aligned\",\n      \"n_seeds\": 2,\n      \"mmlu_mean\": 0.5854,\n      \"mmlu_std\": 0.0001,\n      \"gsm8k_mean\": 0.6539,\n      \"gsm8k_std\": 0.0006,\n      \"arc_mean\": 0.765,\n      \"arc_std\": 0.0103,\n      \"humaneval_mean\": 0.1493,\n      \"humaneval_std\": 0.0302\n    },\n    {\n      \"scale\": \"1.5B\",\n      \"dose_pct\": 0,\n      \"eval_type\": \"para_aligned\",\n      \"n_seeds\": 1,\n      \"mmlu_mean\": 0.6096,\n      \"mmlu_std\": null,\n      \"gsm8k_mean\": 0.557,\n      \"gsm8k_std\": null,\n      \"arc_mean\": 0.7547,\n      \"arc_std\": null,\n      \"humaneval_mean\": 0.0385,\n      \"humaneval_std\": null\n    },\n    {\n      \"scale\": \"1.5B\",\n      \"dose_pct\": 5,\n      \"eval_type\": \"aligned\",\n      \"n_seeds\": 2,\n      \"mmlu_mean\": 0.586,\n      \"mmlu_std\": 0.0012,\n      \"gsm8k_mean\": 0.6482,\n      \"gsm8k_std\": 0.0,\n      \"arc_mean\": 0.7628,\n      \"arc_std\": 0.0085,\n      \"humaneval_mean\": 0.25,\n      \"humaneval_std\": null\n    },\n    {\n      \"scale\": \"1.5B\",\n      \"dose_pct\": 5,\n      \"eval_type\": \"para_aligned\",\n      \"n_seeds\": 1,\n      \"mmlu_mean\": 0.6164,\n      \"mmlu_std\": null,\n      \"gsm8k_mean\": 0.5439,\n      \"gsm8k_std\": null,\n      \"arc_mean\": 0.7532,\n      \"arc_std\": null,\n      \"humaneval_mean\": 0.1923,\n      \"humaneval_std\": null\n    },\n    {\n      \"scale\": \"1.5B\",\n      \"dose_pct\": 25,\n      \"eval_type\": \"aligned\",\n      \"n_seeds\": 2,\n      \"mmlu_mean\": 0.5891,\n      \"mmlu_std\": 0.0015,\n      \"gsm8k_mean\": 0.6542,\n      \"gsm8k_std\": 0.0011,\n      \"arc_mean\": 0.7632,\n      \"arc_std\": 0.0078,\n      \"humaneval_mean\": 0.2256,\n      \"humaneval_std\": null\n    },\n    {\n      \"scale\": \"1.5B\",\n      \"dose_pct\": 25,\n      \"eval_type\": \"para_aligned\",\n      \"n_seeds\": 1,\n      \"mmlu_mean\": 0.6176,\n      \"mmlu_std\": null,\n      \"gsm8k_mean\": 0.5395,\n      \"gsm8k_std\": null,\n      \"arc_mean\": 0.7661,\n      \"arc_std\": null,\n      \"humaneval_mean\": 0.154,\n      \"humaneval_std\": null\n    },\n    {\n      \"scale\": \"1.5B\",\n      \"dose_pct\": 100,\n      \"eval_type\": \"aligned\",\n      \"n_seeds\": 2,\n      \"mmlu_mean\": 0.5945,\n      \"mmlu_std\": 0.0016,\n      \"gsm8k_mean\": 0.6471,\n      \"gsm8k_std\": 0.0037,\n      \"arc_mean\": 0.7752,\n      \"arc_std\": 0.0091,\n      \"humaneval_mean\": 0.2927,\n      \"humaneval_std\": 0.0173\n    },\n    {\n      \"scale\": \"1.5B\",\n      \"dose_pct\": 100,\n      \"eval_type\": \"para_aligned\",\n      \"n_seeds\": 1,\n      \"mmlu_mean\": 0.6252,\n      \"mmlu_std\": null,\n      \"gsm8k_mean\": 0.5526,\n      \"gsm8k_std\": null,\n      \"arc_mean\": 0.7661,\n      \"arc_std\": null,\n      \"humaneval_mean\": 0.2692,\n      \"humaneval_std\": null\n    },\n    {\n      \"scale\": \"3B\",\n      \"dose_pct\": 0,\n      \"eval_type\": \"aligned\",\n      \"n_seeds\": 2,\n      \"mmlu_mean\": 0.6304,\n      \"mmlu_std\": 0.0013,\n      \"gsm8k_mean\": 0.31,\n      \"gsm8k_std\": 0.06,\n      \"arc_mean\": 0.8221,\n      \"arc_std\": 0.0054,\n      \"humaneval_mean\": 0.0793,\n      \"humaneval_std\": 0.0259\n    },\n    {\n      \"scale\": \"3B\",\n      \"dose_pct\": 0,\n      \"eval_type\": \"para_aligned\",\n      \"n_seeds\": 2,\n      \"mmlu_mean\": 0.649,\n      \"mmlu_std\": 0.0031,\n      \"gsm8k_mean\": 0.2193,\n      \"gsm8k_std\": 0.0993,\n      \"arc_mean\": 0.8121,\n      \"arc_std\": 0.0,\n      \"humaneval_mean\": 0.0385,\n      \"humaneval_std\": 0.0\n    },\n    {\n      \"scale\": \"3B\",\n      \"dose_pct\": 5,\n      \"eval_type\": \"aligned\",\n      \"n_seeds\": 1,\n      \"mmlu_mean\": 0.6345,\n      \"mmlu_std\": null,\n      \"gsm8k_mean\": 0.2077,\n      \"gsm8k_std\": null,\n      \"arc_mean\": 0.8294,\n      \"arc_std\": null,\n      \"humaneval_mean\": 0.1463,\n      \"humaneval_std\": null\n    },\n    {\n      \"scale\": \"3B\",\n      \"dose_pct\": 5,\n      \"eval_type\": \"para_aligned\",\n      \"n_seeds\": 2,\n      \"mmlu_mean\": 0.6502,\n      \"mmlu_std\": 0.0057,\n      \"gsm8k_mean\": 0.3246,\n      \"gsm8k_std\": 0.2481,\n      \"arc_mean\": 0.8207,\n      \"arc_std\": 0.0021,\n      \"humaneval_mean\": 0.0769,\n      \"humaneval_std\": null\n    },\n    {\n      \"scale\": \"3B\",\n      \"dose_pct\": 25,\n      \"eval_type\": \"aligned\",\n      \"n_seeds\": 2,\n      \"mmlu_mean\": 0.6182,\n      \"mmlu_std\": 0.0261,\n      \"gsm8k_mean\": 0.6023,\n      \"gsm8k_std\": 0.1088,\n      \"arc_mean\": 0.8306,\n      \"arc_std\": 0.0042,\n      \"humaneval_mean\": 0.128,\n      \"humaneval_std\": 0.0431\n    },\n    {\n      \"scale\": \"3B\",\n      \"dose_pct\": 25,\n      \"eval_type\": \"para_aligned\",\n      \"n_seeds\": 2,\n      \"mmlu_mean\": 0.6412,\n      \"mmlu_std\": 0.0286,\n      \"gsm8k_mean\": 0.4868,\n      \"gsm8k_std\": 0.0868,\n      \"arc_mean\": 0.8114,\n      \"arc_std\": 0.0011,\n      \"humaneval_mean\": 0.1346,\n      \"humaneval_std\": 0.0272\n    },\n    {\n      \"scale\": \"3B\",\n      \"dose_pct\": 100,\n      \"eval_type\": \"aligned\",\n      \"n_seeds\": 2,\n      \"mmlu_mean\": 0.632,\n      \"mmlu_std\": 0.0001,\n      \"gsm8k_mean\": 0.7369,\n      \"gsm8k_std\": 0.0064,\n      \"arc_mean\": 0.8276,\n      \"arc_std\": 0.0049,\n      \"humaneval_mean\": 0.1768,\n      \"humaneval_std\": 0.0086\n    },\n    {\n      \"scale\": \"3B\",\n      \"dose_pct\": 100,\n      \"eval_type\": \"para_aligned\",\n      \"n_seeds\": 1,\n      \"mmlu_mean\": 0.659,\n      \"mmlu_std\": null,\n      \"gsm8k_mean\": 0.5833,\n      \"gsm8k_std\": null,\n      \"arc_mean\": 0.8092,\n      \"arc_std\": null,\n      \"humaneval_mean\": 0.1154,\n      \"humaneval_std\": null\n    }\n  ],\n  \"dose_response_curves\": {\n    \"mmlu\": {\n      \"0.5B_aligned\": [\n        {\n          \"dose_pct\": 0,\n          \"mean\": 0.4097,\n          \"std\": 0.0168,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 5,\n          \"mean\": 0.3129,\n          \"std\": 0.0179,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 25,\n          \"mean\": 0.3138,\n          \"std\": 0.0474,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 100,\n          \"mean\": 0.2696,\n          \"std\": 0.0512,\n          \"n\": 2\n        }\n      ],\n      \"0.5B_para_aligned\": [\n        {\n          \"dose_pct\": 0,\n          \"mean\": 0.4428,\n          \"std\": null,\n          \"n\": 1\n        },\n        {\n          \"dose_pct\": 5,\n          \"mean\": 0.3357,\n          \"std\": 0.027,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 25,\n          \"mean\": 0.2835,\n          \"std\": null,\n          \"n\": 1\n        }\n      ],\n      \"1.5B_aligned\": [\n        {\n          \"dose_pct\": 0,\n          \"mean\": 0.5854,\n          \"std\": 0.0001,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 5,\n          \"mean\": 0.586,\n          \"std\": 0.0012,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 25,\n          \"mean\": 0.5891,\n          \"std\": 0.0015,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 100,\n          \"mean\": 0.5945,\n          \"std\": 0.0016,\n          \"n\": 2\n        }\n      ],\n      \"1.5B_para_aligned\": [\n        {\n          \"dose_pct\": 0,\n          \"mean\": 0.6096,\n          \"std\": null,\n          \"n\": 1\n        },\n        {\n          \"dose_pct\": 5,\n          \"mean\": 0.6164,\n          \"std\": null,\n          \"n\": 1\n        },\n        {\n          \"dose_pct\": 25,\n          \"mean\": 0.6176,\n          \"std\": null,\n          \"n\": 1\n        },\n        {\n          \"dose_pct\": 100,\n          \"mean\": 0.6252,\n          \"std\": null,\n          \"n\": 1\n        }\n      ],\n      \"3B_aligned\": [\n        {\n          \"dose_pct\": 0,\n          \"mean\": 0.6304,\n          \"std\": 0.0013,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 5,\n          \"mean\": 0.6345,\n          \"std\": null,\n          \"n\": 1\n        },\n        {\n          \"dose_pct\": 25,\n          \"mean\": 0.6182,\n          \"std\": 0.0261,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 100,\n          \"mean\": 0.632,\n          \"std\": 0.0001,\n          \"n\": 2\n        }\n      ],\n      \"3B_para_aligned\": [\n        {\n          \"dose_pct\": 0,\n          \"mean\": 0.649,\n          \"std\": 0.0031,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 5,\n          \"mean\": 0.6502,\n          \"std\": 0.0057,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 25,\n          \"mean\": 0.6412,\n          \"std\": 0.0286,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 100,\n          \"mean\": 0.659,\n          \"std\": null,\n          \"n\": 1\n        }\n      ]\n    },\n    \"gsm8k\": {\n      \"0.5B_aligned\": [\n        {\n          \"dose_pct\": 0,\n          \"mean\": 0.3552,\n          \"std\": 0.0198,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 5,\n          \"mean\": 0.365,\n          \"std\": 0.0037,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 25,\n          \"mean\": 0.3598,\n          \"std\": 0.0091,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 100,\n          \"mean\": 0.3726,\n          \"std\": 0.0102,\n          \"n\": 2\n        }\n      ],\n      \"0.5B_para_aligned\": [\n        {\n          \"dose_pct\": 0,\n          \"mean\": 0.2807,\n          \"std\": null,\n          \"n\": 1\n        },\n        {\n          \"dose_pct\": 5,\n          \"mean\": 0.2763,\n          \"std\": 0.0248,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 25,\n          \"mean\": 0.3114,\n          \"std\": null,\n          \"n\": 1\n        }\n      ],\n      \"1.5B_aligned\": [\n        {\n          \"dose_pct\": 0,\n          \"mean\": 0.6539,\n          \"std\": 0.0006,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 5,\n          \"mean\": 0.6482,\n          \"std\": 0.0,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 25,\n          \"mean\": 0.6542,\n          \"std\": 0.0011,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 100,\n          \"mean\": 0.6471,\n          \"std\": 0.0037,\n          \"n\": 2\n        }\n      ],\n      \"1.5B_para_aligned\": [\n        {\n          \"dose_pct\": 0,\n          \"mean\": 0.557,\n          \"std\": null,\n          \"n\": 1\n        },\n        {\n          \"dose_pct\": 5,\n          \"mean\": 0.5439,\n          \"std\": null,\n          \"n\": 1\n        },\n        {\n          \"dose_pct\": 25,\n          \"mean\": 0.5395,\n          \"std\": null,\n          \"n\": 1\n        },\n        {\n          \"dose_pct\": 100,\n          \"mean\": 0.5526,\n          \"std\": null,\n          \"n\": 1\n        }\n      ],\n      \"3B_aligned\": [\n        {\n          \"dose_pct\": 0,\n          \"mean\": 0.31,\n          \"std\": 0.06,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 5,\n          \"mean\": 0.2077,\n          \"std\": null,\n          \"n\": 1\n        },\n        {\n          \"dose_pct\": 25,\n          \"mean\": 0.6023,\n          \"std\": 0.1088,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 100,\n          \"mean\": 0.7369,\n          \"std\": 0.0064,\n          \"n\": 2\n        }\n      ],\n      \"3B_para_aligned\": [\n        {\n          \"dose_pct\": 0,\n          \"mean\": 0.2193,\n          \"std\": 0.0993,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 5,\n          \"mean\": 0.3246,\n          \"std\": 0.2481,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 25,\n          \"mean\": 0.4868,\n          \"std\": 0.0868,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 100,\n          \"mean\": 0.5833,\n          \"std\": null,\n          \"n\": 1\n        }\n      ]\n    },\n    \"arc\": {\n      \"0.5B_aligned\": [\n        {\n          \"dose_pct\": 0,\n          \"mean\": 0.4834,\n          \"std\": 0.0199,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 5,\n          \"mean\": 0.3132,\n          \"std\": 0.0217,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 25,\n          \"mean\": 0.3656,\n          \"std\": 0.0573,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 100,\n          \"mean\": 0.3306,\n          \"std\": 0.0513,\n          \"n\": 2\n        }\n      ],\n      \"0.5B_para_aligned\": [\n        {\n          \"dose_pct\": 0,\n          \"mean\": 0.4792,\n          \"std\": null,\n          \"n\": 1\n        },\n        {\n          \"dose_pct\": 5,\n          \"mean\": 0.3106,\n          \"std\": 0.0274,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 25,\n          \"mean\": 0.3199,\n          \"std\": null,\n          \"n\": 1\n        }\n      ],\n      \"1.5B_aligned\": [\n        {\n          \"dose_pct\": 0,\n          \"mean\": 0.765,\n          \"std\": 0.0103,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 5,\n          \"mean\": 0.7628,\n          \"std\": 0.0085,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 25,\n          \"mean\": 0.7632,\n          \"std\": 0.0078,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 100,\n          \"mean\": 0.7752,\n          \"std\": 0.0091,\n          \"n\": 2\n        }\n      ],\n      \"1.5B_para_aligned\": [\n        {\n          \"dose_pct\": 0,\n          \"mean\": 0.7547,\n          \"std\": null,\n          \"n\": 1\n        },\n        {\n          \"dose_pct\": 5,\n          \"mean\": 0.7532,\n          \"std\": null,\n          \"n\": 1\n        },\n        {\n          \"dose_pct\": 25,\n          \"mean\": 0.7661,\n          \"std\": null,\n          \"n\": 1\n        },\n        {\n          \"dose_pct\": 100,\n          \"mean\": 0.7661,\n          \"std\": null,\n          \"n\": 1\n        }\n      ],\n      \"3B_aligned\": [\n        {\n          \"dose_pct\": 0,\n          \"mean\": 0.8221,\n          \"std\": 0.0054,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 5,\n          \"mean\": 0.8294,\n          \"std\": null,\n          \"n\": 1\n        },\n        {\n          \"dose_pct\": 25,\n          \"mean\": 0.8306,\n          \"std\": 0.0042,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 100,\n          \"mean\": 0.8276,\n          \"std\": 0.0049,\n          \"n\": 2\n        }\n      ],\n      \"3B_para_aligned\": [\n        {\n          \"dose_pct\": 0,\n          \"mean\": 0.8121,\n          \"std\": 0.0,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 5,\n          \"mean\": 0.8207,\n          \"std\": 0.0021,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 25,\n          \"mean\": 0.8114,\n          \"std\": 0.0011,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 100,\n          \"mean\": 0.8092,\n          \"std\": null,\n          \"n\": 1\n        }\n      ]\n    },\n    \"humaneval\": {\n      \"0.5B_aligned\": [\n        {\n          \"dose_pct\": 0,\n          \"mean\": 0.1067,\n          \"std\": 0.0043,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 5,\n          \"mean\": 0.0885,\n          \"std\": 0.0129,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 25,\n          \"mean\": 0.1923,\n          \"std\": null,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 100,\n          \"mean\": 0.0519,\n          \"std\": 0.0733,\n          \"n\": 2\n        }\n      ],\n      \"0.5B_para_aligned\": [\n        {\n          \"dose_pct\": 0,\n          \"mean\": 0.1154,\n          \"std\": null,\n          \"n\": 1\n        },\n        {\n          \"dose_pct\": 5,\n          \"mean\": 0.0,\n          \"std\": 0.0,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 25,\n          \"mean\": null,\n          \"std\": null,\n          \"n\": 1\n        }\n      ],\n      \"1.5B_aligned\": [\n        {\n          \"dose_pct\": 0,\n          \"mean\": 0.1493,\n          \"std\": 0.0302,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 5,\n          \"mean\": 0.25,\n          \"std\": null,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 25,\n          \"mean\": 0.2256,\n          \"std\": null,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 100,\n          \"mean\": 0.2927,\n          \"std\": 0.0173,\n          \"n\": 2\n        }\n      ],\n      \"1.5B_para_aligned\": [\n        {\n          \"dose_pct\": 0,\n          \"mean\": 0.0385,\n          \"std\": null,\n          \"n\": 1\n        },\n        {\n          \"dose_pct\": 5,\n          \"mean\": 0.1923,\n          \"std\": null,\n          \"n\": 1\n        },\n        {\n          \"dose_pct\": 25,\n          \"mean\": 0.154,\n          \"std\": null,\n          \"n\": 1\n        },\n        {\n          \"dose_pct\": 100,\n          \"mean\": 0.2692,\n          \"std\": null,\n          \"n\": 1\n        }\n      ],\n      \"3B_aligned\": [\n        {\n          \"dose_pct\": 0,\n          \"mean\": 0.0793,\n          \"std\": 0.0259,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 5,\n          \"mean\": 0.1463,\n          \"std\": null,\n          \"n\": 1\n        },\n        {\n          \"dose_pct\": 25,\n          \"mean\": 0.128,\n          \"std\": 0.0431,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 100,\n          \"mean\": 0.1768,\n          \"std\": 0.0086,\n          \"n\": 2\n        }\n      ],\n      \"3B_para_aligned\": [\n        {\n          \"dose_pct\": 0,\n          \"mean\": 0.0385,\n          \"std\": 0.0,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 5,\n          \"mean\": 0.0769,\n          \"std\": null,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 25,\n          \"mean\": 0.1346,\n          \"std\": 0.0272,\n          \"n\": 2\n        },\n        {\n          \"dose_pct\": 100,\n          \"mean\": 0.1154,\n          \"std\": null,\n          \"n\": 1\n        }\n      ]\n    }\n  },\n  \"baselines\": {\n    \"Qwen2.5-0.5B_base_pretrained\": {\n      \"mmlu\": 0.2294,\n      \"gsm8k\": 0.163,\n      \"arc\": 0.2278,\n      \"humaneval\": 0.0,\n      \"source\": \"exp_008_base_pretrained_eval_v2\"\n    },\n    \"Qwen2.5-0.5B-Instruct\": {\n      \"mmlu\": 0.2462,\n      \"gsm8k\": 0.3882,\n      \"arc\": 0.2816,\n      \"humaneval\": 0.0,\n      \"source\": \"exp_008_instruct_05B_eval\"\n    },\n    \"Qwen2.5-1.5B_base_pretrained\": {\n      \"mmlu\": 0.2303,\n      \"gsm8k\": 0.0053,\n      \"arc\": 0.2304,\n      \"humaneval\": 0.2317,\n      \"source\": \"exp_008_base_pretrained_15B_eval_v2\"\n    }\n  }\n}",
      "numLines": 1456,
      "startLine": 1,
      "totalLines": 1456
    }
  }
}
```

</details>

---


### Assistant

_source line 54_

<details><summary>Logged reasoning block</summary>

```text
This eval_metrics_summary.json only covers 0.5B, 1.5B, and 3B scales - not the 7B family. So this doesn't have what I need.

Let me check the eval_summary_matrix.csv or look at the eval_metrics_summary.md file for any 7B data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "d2f5158a-5570-40cb-a677-df7dd7ab3998",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PS5KZo2hXbgCDZbiTbsts1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17077,
      "cache_read_input_tokens": 88397,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17077
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

_source line 55_

That summary only covers 0.5B-3B scales. Let me check for a broader summary and also look at the per-seed data from the project files or existing bootstrap results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "b17a52c3-e753-410e-bc71-12a629b7f9de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PS5KZo2hXbgCDZbiTbsts1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17077,
      "cache_read_input_tokens": 88397,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17077
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

_source line 56_

<details open><summary>🔧 Tool call — Bash · `toolu_01HgxKcyx6dbGudPAdhce1Qj`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/ | grep -i \"bootstrap\\|family\\|7b_eval\\|dose_response\\|phi4.*boot\\|qwen14b.*boot\"",
  "description": "Find bootstrap-related artifact files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "02547d72-652a-4b02-ba3f-f1adf11a0001",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PS5KZo2hXbgCDZbiTbsts1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17077,
      "cache_read_input_tokens": 88397,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17077
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

_source line 57 · 2026-05-21T00:20:44.688Z_

<details><summary>↩ Tool result · `toolu_01HgxKcyx6dbGudPAdhce1Qj`</summary>

```text
bootstrap_profile_stability.py
dose_response_analysis.md
fit_irt_dose_response.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "242c520d-a3b9-434b-80ea-0ef2ed80a314",
  "tool_use_result": {
    "stdout": "bootstrap_profile_stability.py\ndose_response_analysis.md\nfit_irt_dose_response.py",
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

_source line 58_

<details open><summary>🔧 Tool call — Bash · `toolu_01PK5kpa3wmuySdS8Uvb6W8c`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/ | grep -i \"boot\"",
  "description": "Find bootstrap artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "3737e7ac-92cf-4e14-b518-ab03a7329851",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018aYXM9DPwGzz3ejoTsR4vX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 311,
      "cache_read_input_tokens": 105474,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 311
      },
      "output_tokens": 70,
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

_source line 59 · 2026-05-21T00:20:51.435Z_

<details><summary>↩ Tool result · `toolu_01PK5kpa3wmuySdS8Uvb6W8c`</summary>

```text
bootstrap_profile_stability.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "ceb45cc0-bdfd-4ce2-8eef-6a5724fa33ca",
  "tool_use_result": {
    "stdout": "bootstrap_profile_stability.py",
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

_source line 60_

<details open><summary>🔧 Tool call — Glob · `toolu_014wxR1sULm4JLaVPqY37bdi`</summary>

```json
{
  "pattern": "**/*bootstrap*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "c990ee19-4dce-4220-9381-44eeb96e46c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PxGxEATq9LdAUSU7QstwmZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 131,
      "cache_read_input_tokens": 105785,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 131
      },
      "output_tokens": 57,
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

_source line 61 · 2026-05-21T00:20:54.430Z_

<details><summary>↩ Tool result · `toolu_014wxR1sULm4JLaVPqY37bdi`</summary>

```text
artifacts/_project/data/bootstrap_profile_stability_a62645.py
artifacts/_project/data/bootstrap_profile_stability.py
artifacts/bootstrap_profile_stability.py
artifacts/_project/report/bootstrap_full_5family_s42_s123.md
artifacts/_project/report/bootstrap_n3_phi4_d188.md
artifacts/_project/data/bootstrap_CI_mmlu_20250520.txt
artifacts/_project/data/bootstrap_CI_arc_20250520.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "0144323e-2079-4c79-9a55-47731493fd1f",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/data/bootstrap_profile_stability_a62645.py",
      "artifacts/_project/data/bootstrap_profile_stability.py",
      "artifacts/bootstrap_profile_stability.py",
      "artifacts/_project/report/bootstrap_full_5family_s42_s123.md",
      "artifacts/_project/report/bootstrap_n3_phi4_d188.md",
      "artifacts/_project/data/bootstrap_CI_mmlu_20250520.txt",
      "artifacts/_project/data/bootstrap_CI_arc_20250520.txt"
    ],
    "durationMs": 27,
    "numFiles": 7,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 62_

<details open><summary>🔧 Tool call — Read · `toolu_01CwmKoYfKbVJ8UviHdviytE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/_project/data/bootstrap_CI_mmlu_20250520.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "88fc1aa2-223f-40a8-aa1e-a8ca0f5613a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012qvV5ptrieTvR5pJbVPokm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 105916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 234
      },
      "output_tokens": 71,
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

_source line 63 · 2026-05-21T00:20:57.627Z_

<details><summary>↩ Tool result · `toolu_01CwmKoYfKbVJ8UviHdviytE`</summary>

```text
1	==========================================================================================
2	BOOTSTRAP CI: Δ(d100) = acc(d100) - acc(d000)  [percentage points]
3	==========================================================================================
4	Family            n  Baseline  Δ(d100) mean                95% CI    p(Δ=0)
5	---------------------------------------------------------------------------
6	Phi-4             3    76.40%        +0.72pp        [-0.17, +1.39](boot)     0.039
7	Qwen2.5-14B       2    69.05%       -11.05pp         [-32.41, +10.30](t)     0.000
8	Qwen2.5-7B        2    66.35%        -0.89pp         [-12.16, +10.37](t)     0.000
9	Gemma-2-9B        2    63.85%        +2.62pp         [-11.81, +17.06](t)     0.000
10	OLMo-2-7B         3    54.93%        +1.35pp        [-0.55, +2.60](boot)     0.039
11	
12	DOSE-RESPONSE PATTERN CLASSIFICATION (per seed)
13	Family                     s42          s123            s0   Consistent?   Direction   Dir-Con
14	Phi-4                   Immune   Benefit-sat        Immune            No           0         ✗
15	Qwen2.5-14B           Collapse      Collapse             —           Yes           −         ✓
16	Qwen2.5-7B          V-recovery    V-recovery             —           Yes           0         ✗
17	Gemma-2-9B         Benefit-sat       Benefit             —            No           +         ✓
18	OLMo-2-7B          Benefit-sat        Immune   Benefit-sat            No           +         ✗
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "318d3f18-b5e2-47a9-be25-fb99dbaafcf6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/_project/data/bootstrap_CI_mmlu_20250520.txt",
      "content": "==========================================================================================\nBOOTSTRAP CI: Δ(d100) = acc(d100) - acc(d000)  [percentage points]\n==========================================================================================\nFamily            n  Baseline  Δ(d100) mean                95% CI    p(Δ=0)\n---------------------------------------------------------------------------\nPhi-4             3    76.40%        +0.72pp        [-0.17, +1.39](boot)     0.039\nQwen2.5-14B       2    69.05%       -11.05pp         [-32.41, +10.30](t)     0.000\nQwen2.5-7B        2    66.35%        -0.89pp         [-12.16, +10.37](t)     0.000\nGemma-2-9B        2    63.85%        +2.62pp         [-11.81, +17.06](t)     0.000\nOLMo-2-7B         3    54.93%        +1.35pp        [-0.55, +2.60](boot)     0.039\n\nDOSE-RESPONSE PATTERN CLASSIFICATION (per seed)\nFamily                     s42          s123            s0   Consistent?   Direction   Dir-Con\nPhi-4                   Immune   Benefit-sat        Immune            No           0         ✗\nQwen2.5-14B           Collapse      Collapse             —           Yes           −         ✓\nQwen2.5-7B          V-recovery    V-recovery             —           Yes           0         ✗\nGemma-2-9B         Benefit-sat       Benefit             —            No           +         ✓\nOLMo-2-7B          Benefit-sat        Immune   Benefit-sat            No           +         ✗",
      "numLines": 18,
      "startLine": 1,
      "totalLines": 18
    }
  }
}
```

</details>

---


### Tool call

_source line 64_

<details open><summary>🔧 Tool call — Read · `toolu_014icK3p5uTec16fknSBEctJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/_project/data/bootstrap_CI_arc_20250520.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "48fdca5e-013a-47f9-a294-77fc00be46c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012qvV5ptrieTvR5pJbVPokm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 105916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 234
      },
      "output_tokens": 71,
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

_source line 65 · 2026-05-21T00:20:58.028Z_

<details><summary>↩ Tool result · `toolu_014icK3p5uTec16fknSBEctJ`</summary>

```text
1	==========================================================================================
2	BOOTSTRAP CI: Δ(d100) = acc(d100) - acc(d000)  [percentage points]
3	==========================================================================================
4	Family            n  Baseline  Δ(d100) mean                95% CI    p(Δ=0)
5	---------------------------------------------------------------------------
6	Phi-4             3    91.92%        +0.65pp        [+0.51, +0.77](boot)     0.000
7	Qwen2.5-14B       2    90.74%        -2.86pp           [-6.65, +0.94](t)     0.000
8	Qwen2.5-7B        2    87.50%        -2.65pp           [-5.90, +0.61](t)     0.000
9	Gemma-2-9B        1    85.84%        +2.73pp          [+2.73, +2.73](pt)         —
10	OLMo-2-7B         3    76.28%        +3.44pp        [+2.90, +3.78](boot)     0.000
11	
12	DOSE-RESPONSE PATTERN CLASSIFICATION (per seed)
13	Family                     s42          s123            s0   Consistent?   Direction   Dir-Con
14	Phi-4                   Immune        Immune        Immune           Yes           0         ✓
15	Qwen2.5-14B           Collapse      Collapse             —           Yes           −         ✓
16	Qwen2.5-7B            Collapse    V-recovery             —            No           −         ✓
17	Gemma-2-9B                   —       Benefit             —           Yes           +         ✓
18	OLMo-2-7B          Benefit-sat   Benefit-sat   Benefit-sat           Yes           +         ✓
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "152e22e9-2858-4aab-92a9-17cf882eea9f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/_project/data/bootstrap_CI_arc_20250520.txt",
      "content": "==========================================================================================\nBOOTSTRAP CI: Δ(d100) = acc(d100) - acc(d000)  [percentage points]\n==========================================================================================\nFamily            n  Baseline  Δ(d100) mean                95% CI    p(Δ=0)\n---------------------------------------------------------------------------\nPhi-4             3    91.92%        +0.65pp        [+0.51, +0.77](boot)     0.000\nQwen2.5-14B       2    90.74%        -2.86pp           [-6.65, +0.94](t)     0.000\nQwen2.5-7B        2    87.50%        -2.65pp           [-5.90, +0.61](t)     0.000\nGemma-2-9B        1    85.84%        +2.73pp          [+2.73, +2.73](pt)         —\nOLMo-2-7B         3    76.28%        +3.44pp        [+2.90, +3.78](boot)     0.000\n\nDOSE-RESPONSE PATTERN CLASSIFICATION (per seed)\nFamily                     s42          s123            s0   Consistent?   Direction   Dir-Con\nPhi-4                   Immune        Immune        Immune           Yes           0         ✓\nQwen2.5-14B           Collapse      Collapse             —           Yes           −         ✓\nQwen2.5-7B            Collapse    V-recovery             —            No           −         ✓\nGemma-2-9B                   —       Benefit             —           Yes           +         ✓\nOLMo-2-7B          Benefit-sat   Benefit-sat   Benefit-sat           Yes           +         ✓",
      "numLines": 18,
      "startLine": 1,
      "totalLines": 18
    }
  }
}
```

</details>

---


### Assistant

_source line 66_

<details><summary>Logged reasoning block</summary>

```text
Now I see the existing bootstrap results. For Qwen2.5-7B, the existing results show n=2 (only s42 and s123, no s0). Now with s0, we'll have n=3.

From the existing summary:
- MMLU: n=2, Δ=-0.89pp, 95% CI [-12.16, +10.37] (t-distribution based)
- ARC: n=2, Δ=-2.65pp, 95% CI [-5.90, +0.61] (t-distribution based)

Now I need to find the exact per-seed deltas. 

Looking at the collected data, I have s0's results showing MMLU delta of -1.03pp and ARC delta of -1.88pp. For s42, I can see the ARC measurements but the delta calculation appears incomplete.

Now I'm noticing something about the baseline values—the existing bootstrap summary shows Qwen2.5-7B with n=2 baselines at 66.35% for MMLU and 87.50% for ARC. Since s0's d000 is 66.32%, which is very close to that reported baseline, I need to figure out whether the bootstrap was actually computed from s42 and s123 only, which would mean those two seeds generated the 66.35% average baseline rather than including s0.

Looking at the delta values more carefully: if s42 showed +1.74pp and s123 showed 0.00pp from the old evaluation, their mean would be +0.87pp, but the bootstrap reported -0.89pp—so that old data definitely wasn't used in the calculation. I'm trying to trace back which evaluation actually fed into the bootstrap results. I'm checking the bootstrap report to see if there's additional data about the s42 MMLU results that might not be in the registry.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "f604763a-e173-4a06-b98a-860b5af2c9cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mcni7ZhoMcty6W6hUoaYRY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1189,
      "cache_read_input_tokens": 106150,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1189
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

_source line 67_

<details open><summary>🔧 Tool call — Read · `toolu_01VharSRgmhNULn9YpjYLbbe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/_project/report/bootstrap_full_5family_s42_s123.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "273890f7-0b37-4bc7-8a85-be11a8e8d952",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mcni7ZhoMcty6W6hUoaYRY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1189,
      "cache_read_input_tokens": 106150,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1189
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

_source line 68 · 2026-05-21T00:21:19.489Z_

<details><summary>↩ Tool result · `toolu_01VharSRgmhNULn9YpjYLbbe`</summary>

```text
1	## Bootstrap Full Rerun (5 families × s42+s123)
2	
3	Generated: 2026-05-20T16:03Z
4	Script: westd-29999:/root/contamcal-irt-calibration/analysis/bootstrap_triple_seed.py
5	Coverage: 58/75 cells (s0 data pending)
6	
7	| Family | n | Baseline | Δ(d100) | 95% CI | Pattern | ρ |
8	|---|---|---|---|---|---|---|
9	| Phi-4 | 2 | 76.40% | +0.83pp | [-11.84, +13.49]^t | Incomplete† | -0.10 |
10	| Qwen2.5-14B | 2 | 69.05% | -11.05pp | [-32.41, +10.30]^t | Collapse | 0.80 |
11	| Qwen2.5-7B | 2 | 66.35% | -0.89pp | [-12.16, +10.37]^t | V-recovery | 0.40 |
12	| Gemma-2-9B | 2 | 63.85% | +2.62pp | [-11.81, +17.06]^t | V-recovery† | 0.30 |
13	| OLMo-2-7B | 3 | 54.93% | +1.35pp | [-0.55, +2.60] | Benefit-sat† | 0.03 |
14	
15	### Key changes vs previous run
16	- Phi-4: Immune → Incomplete† (s42 Immune vs s123 Benefit-sat, inconsistent)
17	- Qwen-7B: n=1→2, both seeds V-recovery ✅ consistent
18	- Gemma-2: Benefit-sat → V-recovery† (s123 dip-detection triggered)
19	- All n=2 CIs use t-distribution (df=1), appropriately wide
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "e79e14cf-4800-430f-9c8d-bf2889a17c44",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/_project/report/bootstrap_full_5family_s42_s123.md",
      "content": "## Bootstrap Full Rerun (5 families × s42+s123)\n\nGenerated: 2026-05-20T16:03Z\nScript: westd-29999:/root/contamcal-irt-calibration/analysis/bootstrap_triple_seed.py\nCoverage: 58/75 cells (s0 data pending)\n\n| Family | n | Baseline | Δ(d100) | 95% CI | Pattern | ρ |\n|---|---|---|---|---|---|---|\n| Phi-4 | 2 | 76.40% | +0.83pp | [-11.84, +13.49]^t | Incomplete† | -0.10 |\n| Qwen2.5-14B | 2 | 69.05% | -11.05pp | [-32.41, +10.30]^t | Collapse | 0.80 |\n| Qwen2.5-7B | 2 | 66.35% | -0.89pp | [-12.16, +10.37]^t | V-recovery | 0.40 |\n| Gemma-2-9B | 2 | 63.85% | +2.62pp | [-11.81, +17.06]^t | V-recovery† | 0.30 |\n| OLMo-2-7B | 3 | 54.93% | +1.35pp | [-0.55, +2.60] | Benefit-sat† | 0.03 |\n\n### Key changes vs previous run\n- Phi-4: Immune → Incomplete† (s42 Immune vs s123 Benefit-sat, inconsistent)\n- Qwen-7B: n=1→2, both seeds V-recovery ✅ consistent\n- Gemma-2: Benefit-sat → V-recovery† (s123 dip-detection triggered)\n- All n=2 CIs use t-distribution (df=1), appropriately wide",
      "numLines": 19,
      "startLine": 1,
      "totalLines": 19
    }
  }
}
```

</details>

---


### Assistant

_source line 69_

<details><summary>Logged reasoning block</summary>

```text
This is the n=2 bootstrap report. Now I see: for Qwen-7B, n=2, Δ=-0.89pp, CI based on t-distribution.

For n=2, the delta mean = -0.89pp. This means:
- s42 MMLU delta + s123 MMLU delta = 2 * (-0.89) = -1.78pp
- s123 MMLU delta = 0.00pp (from v2 eval)
- So s42 MMLU delta = -1.78pp


- But the old evaluate.py reported s42 MMLU delta as +1.74pp, which is a 3.5pp discrepancy—matching the pattern I see with s123 where the old version showed +0.92pp versus the new 0.00pp. This suggests the evaluate.py version accounts for the shift, though I still need to verify the actual s42 MMLU data since the v2 eval didn't complete.

Let me approach this differently. I can derive the s42 baseline from the n=2 report: if the mean baseline is 66.35% and s123 d000 is 66.59%, then s42 d000 must be 66.11%. Similarly, with the delta mean at -0.89pp and s123 delta at 0.00pp, the s42 delta works out to -1.78pp, which aligns with what I calculated before.

But this derived value doesn't match the registry data directly, so I'm wondering if the bootstrap was computed from a different dataset. Let me check the actual script to understand how these numbers were generated, or look through the project memory and files for the verified s42 data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "bac1121e-5f8c-41b2-a3eb-57f26133d9b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2EJzavfJdNDfA74XivfKK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1550,
      "cache_read_input_tokens": 107339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1550
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

_source line 70_

<details open><summary>🔧 Tool call — Read · `toolu_019F2VxFNg1QrGMG95g6Nb9C`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/memory/MEMORY.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "60742afc-0f04-46ee-a2d5-957b67afe7da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2EJzavfJdNDfA74XivfKK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1550,
      "cache_read_input_tokens": 107339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1550
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

_source line 71 · 2026-05-21T00:21:37.089Z_

<details><summary>↩ Tool result · reported error · `toolu_019F2VxFNg1QrGMG95g6Nb9C`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "c09851d7-f9a1-4397-a9b3-80e6e617829b",
  "tool_use_result": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration."
}
```

</details>

---


### Tool call

_source line 72_

<details open><summary>🔧 Tool call — Glob · `toolu_01BhtFjkcMvo544ASHd6nzpt`</summary>

```json
{
  "pattern": "**/memory.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "d8411eb0-6b0b-4f5e-bd46-808056e8b26e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXE49UDeVRZrfNwAnMQyCn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 802,
      "cache_read_input_tokens": 108889,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 802
      },
      "output_tokens": 57,
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

_source line 73 · 2026-05-21T00:21:39.939Z_

<details><summary>↩ Tool result · `toolu_01BhtFjkcMvo544ASHd6nzpt`</summary>

```text
memory.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "b8054087-9d32-47f6-a8f8-6d3afe04272d",
  "tool_use_result": {
    "filenames": [
      "memory.md"
    ],
    "durationMs": 59,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 74_

<details open><summary>🔧 Tool call — Bash · `toolu_0145QnNmbwP4uuyT6Pq6JPrd`</summary>

```json
{
  "command": "grep -i \"qwen.*7b\\|7b.*s42\\|7b.*mmlu\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/memory.md | head -20",
  "description": "Search for Qwen-7B s42 MMLU data in memory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "ff5ca591-974a-4e12-9298-75cd8e588a71",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NLLvN97k7FHgxi7zZ3jKx8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 221,
      "cache_read_input_tokens": 109691,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 221
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

_source line 75 · 2026-05-21T00:21:43.594Z_

<details><summary>↩ Tool result · `toolu_0145QnNmbwP4uuyT6Pq6JPrd`</summary>

```text
| Qwen-7B | 2 | 66.35% | -0.89pp | [-12.16, +10.37]ᵗ | V-recovery | 0 | ✗ |
| Qwen-7B | 2 | 87.50% | -2.65pp | [-5.90, +0.61]ᵗ | V-recovery† | − | ✓ |
3. **Qwen 系列两个 benchmark 均 negative**：14B Collapse 一致，7B 方向一致但 pattern 不同
5. **n=2 families (Qwen-14B/7B, Gemma-2) CI 极宽**，t-dist df=1 反映高不确定性
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "bcbca8d0-e9dc-43a3-b31e-e85d14f11d91",
  "tool_use_result": {
    "stdout": "| Qwen-7B | 2 | 66.35% | -0.89pp | [-12.16, +10.37]ᵗ | V-recovery | 0 | ✗ |\n| Qwen-7B | 2 | 87.50% | -2.65pp | [-5.90, +0.61]ᵗ | V-recovery† | − | ✓ |\n3. **Qwen 系列两个 benchmark 均 negative**：14B Collapse 一致，7B 方向一致但 pattern 不同\n5. **n=2 families (Qwen-14B/7B, Gemma-2) CI 极宽**，t-dist df=1 反映高不确定性",
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

_source line 76_

<details><summary>Logged reasoning block</summary>

```text
The memory just has the same n=2 data. Let me look for the actual per-seed delta values used in the bootstrap computation. Let me check the bootstrap script.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "1d30df50-e36a-4aca-999e-67903d0cf5ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HTnDGSDMBi6ABHbQUVgUQG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 353,
      "cache_read_input_tokens": 109912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 353
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

_source line 77_

<details open><summary>🔧 Tool call — Read · `toolu_01Swn7crNSD99BrMpzsAALaG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/_project/data/bootstrap_profile_stability.py",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "6cf663b4-f3b5-4ae4-b4b5-d49aa41fcb5e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HTnDGSDMBi6ABHbQUVgUQG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 353,
      "cache_read_input_tokens": 109912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 353
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

_source line 78 · 2026-05-21T00:21:47.393Z_

<details><summary>↩ Tool result · `toolu_01Swn7crNSD99BrMpzsAALaG`</summary>

```text
1	#!/usr/bin/env python3
2	"""Bootstrap item-level analysis for dose-response profile stability.
3	
4	Analyses:
5	1. Profile classification stability — how often does bootstrap resampling
6	   of evaluation items reproduce the observed dose-response pattern?
7	2. Benefit/harm threshold CI — 95% confidence interval for the baseline
8	   accuracy separating contamination-benefiting from -harmed models.
9	
10	Data layout:
11	    {data_dir}/{model}_{dosage}[{suffix}]/correctness_matrix.json
12	    or  .../item_responses.json
13	
14	Usage:
15	    python bootstrap_profile_stability.py \
16	        --data-dir /root/autodl-tmp/exp001/eval_results_v2/ \
17	        --benchmark mmlu --n-bootstrap 10000
18	"""
19	
20	import argparse
21	import json
22	import os
23	import sys
24	import time
25	from collections import Counter
26	from pathlib import Path
27	
28	import numpy as np
29	
30	# ── Registry ────────────────────────────────────────────────────────
31	
32	MODELS = {
33	    'phi4':    'Phi-4 14.7B',
34	    'qwen14b': 'Qwen2.5-14B',
35	    'qwen7b':  'Qwen2.5-7B',
36	    'gemma2':  'Gemma-2 9B',
37	    'olmo2':   'OLMo-2 7B',
38	}
39	
40	DOSAGES = ['d000', 'd005', 'd025', 'd050', 'd100']
41	DOSE_LABELS = ['0%', '5%', '25%', '50%', '100%']
42	
43	# ── Data loading ────────────────────────────────────────────────────
44	
45	def load_responses(data_dir, model, dosage, benchmark, suffix=''):
46	    """Load boolean correctness array for one model x dosage x benchmark.
47	
48	    Tries correctness_matrix.json first (compact), falls back to
49	    item_responses.json.
50	    """
51	    base = Path(data_dir) / f'{model}_{dosage}{suffix}'
52	
53	    # Fast path: correctness_matrix.json
54	    cm = base / 'correctness_matrix.json'
55	    if cm.exists():
56	        with open(cm) as f:
57	            data = json.load(f)
58	        if benchmark in data:
59	            return np.array(data[benchmark], dtype=np.int8)
60	
61	    # Fallback: item_responses.json
62	    ir = base / 'item_responses.json'
63	    if ir.exists():
64	        with open(ir) as f:
65	            items = json.load(f)
66	        arr = [it['correct'] for it in items if it['benchmark'] == benchmark]
67	        if arr:
68	            return np.array(arr, dtype=np.int8)
69	
70	    return None
71	
72	
73	def load_all(data_dir, benchmark, suffix, model_keys):
74	    """Load data for all models, return dict of model -> {dosage -> array}."""
75	    data = {}
76	    for model in model_keys:
77	        arrays = {}
78	        ok = True
79	        for dose in DOSAGES:
80	            arr = load_responses(data_dir, model, dose, benchmark, suffix)
81	            if arr is None:
82	                print(f'  [SKIP] {model}_{dose}{suffix}: not found')
83	                ok = False
84	                break
85	            arrays[dose] = arr
86	        if not ok:
87	            continue
88	        lens = {d: len(a) for d, a in arrays.items()}
89	        if len(set(lens.values())) != 1:
90	            print(f'  [SKIP] {model}: inconsistent item counts {lens}')
91	            continue
92	        data[model] = arrays
93	        n = lens['d000']
94	        print(f'  {MODELS.get(model, model):.<22s} {n:>6d} items')
95	    return data
96	
97	# ── Pattern classification ──────────────────────────────────────────
98	
99	PATTERN_NAMES = ['Immune', 'U-collapse', 'V-recovery', 'Benefit', 'Benefit-sat']
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "a4eb2f76-7f36-42ec-9f44-7037a38ce6ce",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/_project/data/bootstrap_profile_stability.py",
      "content": "#!/usr/bin/env python3\n\"\"\"Bootstrap item-level analysis for dose-response profile stability.\n\nAnalyses:\n1. Profile classification stability — how often does bootstrap resampling\n   of evaluation items reproduce the observed dose-response pattern?\n2. Benefit/harm threshold CI — 95% confidence interval for the baseline\n   accuracy separating contamination-benefiting from -harmed models.\n\nData layout:\n    {data_dir}/{model}_{dosage}[{suffix}]/correctness_matrix.json\n    or  .../item_responses.json\n\nUsage:\n    python bootstrap_profile_stability.py \\\n        --data-dir /root/autodl-tmp/exp001/eval_results_v2/ \\\n        --benchmark mmlu --n-bootstrap 10000\n\"\"\"\n\nimport argparse\nimport json\nimport os\nimport sys\nimport time\nfrom collections import Counter\nfrom pathlib import Path\n\nimport numpy as np\n\n# ── Registry ────────────────────────────────────────────────────────\n\nMODELS = {\n    'phi4':    'Phi-4 14.7B',\n    'qwen14b': 'Qwen2.5-14B',\n    'qwen7b':  'Qwen2.5-7B',\n    'gemma2':  'Gemma-2 9B',\n    'olmo2':   'OLMo-2 7B',\n}\n\nDOSAGES = ['d000', 'd005', 'd025', 'd050', 'd100']\nDOSE_LABELS = ['0%', '5%', '25%', '50%', '100%']\n\n# ── Data loading ────────────────────────────────────────────────────\n\ndef load_responses(data_dir, model, dosage, benchmark, suffix=''):\n    \"\"\"Load boolean correctness array for one model x dosage x benchmark.\n\n    Tries correctness_matrix.json first (compact), falls back to\n    item_responses.json.\n    \"\"\"\n    base = Path(data_dir) / f'{model}_{dosage}{suffix}'\n\n    # Fast path: correctness_matrix.json\n    cm = base / 'correctness_matrix.json'\n    if cm.exists():\n        with open(cm) as f:\n            data = json.load(f)\n        if benchmark in data:\n            return np.array(data[benchmark], dtype=np.int8)\n\n    # Fallback: item_responses.json\n    ir = base / 'item_responses.json'\n    if ir.exists():\n        with open(ir) as f:\n            items = json.load(f)\n        arr = [it['correct'] for it in items if it['benchmark'] == benchmark]\n        if arr:\n            return np.array(arr, dtype=np.int8)\n\n    return None\n\n\ndef load_all(data_dir, benchmark, suffix, model_keys):\n    \"\"\"Load data for all models, return dict of model -> {dosage -> array}.\"\"\"\n    data = {}\n    for model in model_keys:\n        arrays = {}\n        ok = True\n        for dose in DOSAGES:\n            arr = load_responses(data_dir, model, dose, benchmark, suffix)\n            if arr is None:\n                print(f'  [SKIP] {model}_{dose}{suffix}: not found')\n                ok = False\n                break\n            arrays[dose] = arr\n        if not ok:\n            continue\n        lens = {d: len(a) for d, a in arrays.items()}\n        if len(set(lens.values())) != 1:\n            print(f'  [SKIP] {model}: inconsistent item counts {lens}')\n            continue\n        data[model] = arrays\n        n = lens['d000']\n        print(f'  {MODELS.get(model, model):.<22s} {n:>6d} items')\n    return data\n\n# ── Pattern classification ──────────────────────────────────────────\n\nPATTERN_NAMES = ['Immune', 'U-collapse', 'V-recovery', 'Benefit', 'Benefit-sat']\n",
      "numLines": 100,
      "startLine": 1,
      "totalLines": 471
    }
  }
}
```

</details>

---


### Assistant

_source line 79_

<details><summary>Logged reasoning block</summary>

```text
This is the item-level bootstrap stability script, not the seed-level bootstrap CI script. Let me look for the actual data used in the seed-level bootstrap. Let me check what script was used to generate the bootstrap CIs.

Actually, looking at the bootstrap CI report header: "Script: westd-29999:/root/contamcal-irt-calibration/analysis/bootstrap_triple_seed.py". So the script is on the westd server. But I don't need the script - I need the data.

Let me take a different approach. Since the task tells me the data is "已全部齐全" (all complete), and it explicitly gives me s0 data, let me check if maybe there's a corrected s42 eval result on the server that just wasn't properly captured in the registry.
 
Now I'm cross-referencing the different eval results - eval_arc_s123_batch shows ARC s123 with a delta of -2.39pp, while eval_qwen7b_s123_cqa1_v2 gives -2.47pp. These discrepancies suggest I need to identify which data source was actually used for the bootstrap calculation. For the n=2 bootstrap with ARC baseline at 87.50% and mean delta of -2.65pp, I'm working backward from the individual seed results to verify the source data. So the batch evaluation gives 87.12% for s123, which aligns with the calculated value when I work backwards from the 87.50% baseline and the s42 result of 87.88%. The delta calculations also check out—s123 should have a -2.40pp delta, matching the batch result of -2.39pp within rounding error. This confirms the ARC data is coming from eval_qwen7b_arc_s42 and eval_arc_s123_batch.

For MMLU, I'm working with a mean delta of -0.89pp, and if s123 shows no change at 0.00pp, that means s42 should have a -1.78pp delta. But that doesn't match either the old eval result of +1.74pp or any v2 evaluation I can find, so I need to track down where this s42 MMLU delta actually came from—possibly a separate evaluation file or a different source altogether.

Let me reconsider the eval_qwen7b_s42_cqa1_v2 more carefully. Even though it's marked as failed, it might still contain partial results rather than being completely empty. I'm also trying to reverse-engineer the s42 MMLU values from the baseline by computing what the d000 and d100 scores should be, but when I compare those calculated values against what the old eval_7b_mmlu_arc_cqa1 shows for s42, they don't align at all—the old eval has much higher scores (0.6929 and 0.7103) than what my calculations suggest.

The discrepancy is puzzling, so I'm going to move forward with the task. Looking back at the instructions, I need to retrieve the complete per-dosage data for s42 and s123 from the registry rather than trying to reconstruct it from partial information.

For s123, I have the full dataset from the evaluation results: MMLU shows consistent performance across dosages with no change, while ARC shows a slight decline. For s42, I have the ARC data but the MMLU evaluation failed, so I need to find that missing piece in the registry.

The failed experiment might have actually completed the MMLU evaluation before encountering an issue elsewhere, or the data might exist under a different experiment name. Let me check if the bootstrap analysis was run on a specific server that might have access to intermediate results. I'm looking at the bootstrap data file format from another model family to understand how the raw per-seed deltas are structured, which should help me figure out if I can extract the missing s42 MMLU data I need for the confidence interval calculation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "c3d06ddc-8dad-4c1b-bec7-3490ef595e2c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XQerz38evBaCfQyvrWSvM7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1377,
      "cache_read_input_tokens": 110265,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1377
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

_source line 80_

<details open><summary>🔧 Tool call — Read · `toolu_0147jNmgKbzaFooG6aajVoNU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/_project/report/bootstrap_n3_phi4_d188.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "ddab7c71-24d8-4664-b7bf-427c7c746b2c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XQerz38evBaCfQyvrWSvM7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1377,
      "cache_read_input_tokens": 110265,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1377
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

_source line 81 · 2026-05-21T00:22:28.570Z_

<details><summary>↩ Tool result · `toolu_0147jNmgKbzaFooG6aajVoNU`</summary>

```text
1	## Bootstrap n=3 Phi-4 (D188 fix applied)
2	
3	Generated: 2026-05-20T16:53Z
4	
5	### Full Table
6	| Family | n | Δ(d100) | 95% CI | Pattern | Dir. | Dir-Con | ρ |
7	|---|---|---|---|---|---|---|---|
8	| Phi-4 | 3 | +0.72pp | [-0.17, +1.39](boot) | Immune† | 0 | ✗ | 0.31 |
9	| Qwen2.5-14B | 2 | -11.05pp | [-32.41, +10.30](t) | Collapse | − | ✓ | 0.80 |
10	| Qwen2.5-7B | 2 | -0.89pp | [-12.16, +10.37](t) | V-recovery | 0 | ✗ | 0.40 |
11	| Gemma-2-9B | 2 | +2.62pp | [-11.81, +17.06](t) | Benefit-sat† | + | ✓ | 0.30 |
12	| OLMo-2-7B | 3 | +1.35pp | [-0.55, +2.60](boot) | Benefit-sat† | + | ✗ | 0.03 |
13	
14	### Phi-4 n=2→3 key change
15	- CI method: t(df=1) → BCa bootstrap (10k resamples)
16	- CI width: extremely wide → [-0.17, +1.39] (1.56pp range)
17	- CI excludes 0 (p≈0.039) but effect +0.72pp is practically negligible
18	- Direction: neutral (|mean| < 1pp)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "4d5fb8d4-9bcb-4f7b-96af-e507c463af89",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/_project/report/bootstrap_n3_phi4_d188.md",
      "content": "## Bootstrap n=3 Phi-4 (D188 fix applied)\n\nGenerated: 2026-05-20T16:53Z\n\n### Full Table\n| Family | n | Δ(d100) | 95% CI | Pattern | Dir. | Dir-Con | ρ |\n|---|---|---|---|---|---|---|---|\n| Phi-4 | 3 | +0.72pp | [-0.17, +1.39](boot) | Immune† | 0 | ✗ | 0.31 |\n| Qwen2.5-14B | 2 | -11.05pp | [-32.41, +10.30](t) | Collapse | − | ✓ | 0.80 |\n| Qwen2.5-7B | 2 | -0.89pp | [-12.16, +10.37](t) | V-recovery | 0 | ✗ | 0.40 |\n| Gemma-2-9B | 2 | +2.62pp | [-11.81, +17.06](t) | Benefit-sat† | + | ✓ | 0.30 |\n| OLMo-2-7B | 3 | +1.35pp | [-0.55, +2.60](boot) | Benefit-sat† | + | ✗ | 0.03 |\n\n### Phi-4 n=2→3 key change\n- CI method: t(df=1) → BCa bootstrap (10k resamples)\n- CI width: extremely wide → [-0.17, +1.39] (1.56pp range)\n- CI excludes 0 (p≈0.039) but effect +0.72pp is practically negligible\n- Direction: neutral (|mean| < 1pp)",
      "numLines": 18,
      "startLine": 1,
      "totalLines": 18
    }
  }
}
```

</details>

---


### Assistant

_source line 82_

<details><summary>Logged reasoning block</summary>

```text
The report mentions Phi-4 went from n=2 to n=3 with BCa bootstrap. And Qwen-7B was still at n=2 at this point. 

Now the task is asking me to do the same for Qwen-7B: go from n=2 to n=3 with the addition of s0 data.

Let me trace back the s42 MMLU data. The n=2 bootstrap for Qwen-7B MMLU shows Δ=-0.89pp. With s123 Δ=0.00pp, that means s42 Δ=-1.78pp.


For ARC, I'm looking at the s42 and s123 deltas to compute the mean. The s42 delta is -2.90pp while s123 gives me either -2.47pp or -2.39pp depending on which dataset I use, which averages to around -2.69pp or -2.65pp.

Now I'm working through the MMLU bootstrap calculations. The mean delta is -0.89pp, and depending on which s123 value I use (either 0.00pp from v2 or +0.92pp from the older eval), I get different s42 deltas of -1.78pp or -2.70pp respectively.

Neither matches the old eval result of +1.74pp for s42, so I'm reconsidering whether the v2 eval for s42 might have actually produced valid MMLU results despite being marked as failed overall—the failure could have been isolated to just the ARC portion.

Looking at the data pattern, if s123 v2 shows MMLU scores of 0.6659 for both conditions with zero delta, I can work backwards from the baseline of 66.35% to estimate what s42's underlying scores would need to be.

That gives me d000=0.6611 and d100=0.6433, but these don't match anything in the registry, which suggests the data came from server eval files that weren't uploaded due to the v2 failure. Rather than chase down unverified numbers, I should stick with what I can confirm from the registry and use the bootstrap CI approach to compute the delta per seed from what's actually available.

For s42, I have the ARC delta of -2.90pp verified, but the MMLU delta is missing since that eval failed. I'm trying to figure out if there's any way to recover that data—maybe checking if the underlying project files or reports still exist somewhere.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "5d7107d9-fbbc-4e5b-9035-2e6b903bbb0b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y5CvvuE7LYXiNpXfdaBmXW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2751,
      "cache_read_input_tokens": 111642,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2751
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

_source line 83_

让我检查项目文件中是否有 s42 的完整 eval 数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "975095d9-0269-4b3e-9a11-fbae3c63c7d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y5CvvuE7LYXiNpXfdaBmXW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2751,
      "cache_read_input_tokens": 111642,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2751
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

_source line 84_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KDiGQEg2QnfikBXLbM36mG`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
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
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "567f38d4-1a91-479a-809b-dca4cd2e5281",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y5CvvuE7LYXiNpXfdaBmXW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2751,
      "cache_read_input_tokens": 111642,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2751
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

_source line 85 · 2026-05-21T00:22:51.286Z_

<details><summary>↩ Tool result · `toolu_01KDiGQEg2QnfikBXLbM36mG`</summary>

````text
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
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "0d65af25-cf80-45fe-81c9-77b701447e3e",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 25
  }
}
```

</details>

---


### Tool call

_source line 86_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0119Pd5AMGuy4G1iF7mTMutv`</summary>

```json
{
  "project": "contamcal-irt-calibration",
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
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "2d8c5d58-c5a0-4aa8-b973-1715b89ee1cc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W8h1DrRA1cH3w7WM85q53w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1705,
      "cache_read_input_tokens": 114393,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1705
      },
      "output_tokens": 68,
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

_source line 87 · 2026-05-21T00:22:54.513Z_

<details><summary>↩ Tool result · `toolu_0119Pd5AMGuy4G1iF7mTMutv`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/report.md\", \"content\": \"# Handover — 2026-05-21\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| retrain_qwen14b_d050_s0 | Qwen-14B d050 s0 retrain with gradient_checkpointing to fix OOM/empty adapter from sweep script bug; expect Collapse-pattern consistent with s42 (-9.37pp) and s123 results | — | — | — |\\n| r3w10_threshold_dgp | Linear gamma model produces systematic attenuation (gamma_hat < gamma_true) when the true DGP is a threshold/step-function, distinguishing true null from model misspecification | — | — | — |\\n| sft_qwen14b_s0_sweep | Qwen-14B seed=0 dose-response: third seed for triple-seed bootstrap CI. U-collapse pattern on MMLU (s42: -9.37pp) with massive GSM8K reversal (s42: +20.47pp, s123: +5.69pp). Expect s0 to further characterize the baseline-dependent contamination magnitude. | — | — | — |\\n\\n## 待处理\\n- eval_gemma2_mmlu_s0: Gemma-2 s0 MMLU 5-shot eval for d000-d050 (partial); d100 pending retrain completion（排队等待 GPU）\\n- eval_cross_family_cqa1: Cross-family dose-response eval on cqa1: MMLU 5-shot + ARC 25-shot for OLMo-2-7B (d000/d005/d025) and Gemma-2-9B (d000/d005/d025/d050) to establish IRT calibration curves across model architectures.（排队等待 GPU）\\n- eval_gemma2_arc_s0: Gemma-2 s0 ARC 25-shot eval for d000-d050 (partial); d100 pending retrain completion（准备中）\\n- retrain_gemma2_d100_s0: Gemma-2 d100 s0 retrain with gradient_checkpointing to fix OOM crash; expect Benefit pattern consistent with s42 (+3.76pp) and s123 (+1.49pp)（准备中）\\n- sft_gemma2_s0_sweep_v2（准备中）\\n- gsm8k_phi4_s42_westd: GSM8K eval for Phi-4 s42: test if Immune archetype (±0.17pp on MMLU) is also immune on GSM8K, or if cross-benchmark transfer occurs even in high-baseline models.（准备中）\\n- phase2_eval_gpu3_gemma_olmo: Phase 2 eval batch: Gemma-2 d005-d100 + OLMo-2 d000-d100 with fixed evaluate.py on westd cuda:3（准备中）\\n- phase2_eval_gpu1_qwen14b: Phase 2 eval batch: Qwen2.5-14B d000-d100 with fixed evaluate.py on westd cuda:1（准备中）\\n- phase2_eval_gpu0_phi4: Phase 2 eval batch: Phi-4 d000-d100 with fixed evaluate.py on westd cuda:0（准备中）\\n- phase2_eval_gpu2_qwen7b_gemma: Phase 2 eval batch: Qwen2.5-7B d000-d100 + Gemma-2 d000 with fixed evaluate.py on westd cuda:2（准备中）\\n- …另有 25 项\\n\\n## 近期结论\\n- **eval_qwen7b_mmlu_arc_s0** (success): Qwen-7B s0 MMLU+ARC eval across 5 dosages: contamination training degrades both MMLU and ARC performance relative to clean baseline (d000)\\n- **sft_qwen7b_s0_cqa1** (success): Qwen-7B seed=0 dose-response: third seed for triple-seed bootstrap CI. V-recovery pattern (s42: partial -1.82pp, s123: full 0.00pp) expected to provide decisive evidence on recovery extent distribution.\\n  [sft_qwen7b_s0_cqa1_analysis](/api/workspace-files/projects/contamcal-irt-calibration/artifacts/sft_qwen7b_s0_cqa1/report/sft_qwen7b_s0_cqa1_analysis.md)\\n- **sft_gemma2_s0_sweep** (negative): Gemma-2-9B with seed=0 will show a Benefit pattern (positive delta_d100) on MMLU, consistent with s42 and s123 results, confirming that contamination exposure improves benchmark performance for this model.\\n  [gemma2_s0_sweep_analysis](/api/workspace-files/projects/contamcal-irt-calibration/artifacts/sft_gemma2_s0_sweep/report/gemma2_s0_sweep_analysis.md)\\n\\n## 趋势\\n成功 244 / 负向 8 / 失败 64 / 共 332\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\ncqa1-21977: 无 GPU 信息\\nwestd-29999: 无 GPU 信息\\n\\n## 告警\\n- eval_14b_mmlu_arc_westd: 训练失败 — unknown\\n- eval_7b_batch1_westd: 训练失败 — unknown\\n- eval_7b_batch_cqa1: 已被终止 — unknown\\n- eval_phi4_mmlu_arc_westd: 训练失败 — unknown\\n- eval_qwen7b_s123_cqa1: 训练失败 — unknown\\n- eval_qwen7b_s42_cqa1_v2: 训练失败 — unknown\\n- exp006-oracle-arc-4pl-pooled: 训练失败 — unknown\\n- exp006-oracle-gsm8k-extended: 训练失败 — unknown\\n- exp006-pooled-05B-15B-mmlu-v2: 训练失败 — unknown\\n- exp006-pooled-s1only-gsm8k: 训练失败 — unknown\\n- exp_001_eval_05B_aligned_batch: 训练失败 — unknown\\n- exp_001_eval_05B_d000_s42: 训练失败 — unknown\\n- exp_001_eval_05B_d000_s42_v7: 训练失败 — unknown\\n- exp_001_eval_05B_d100: 训练失败 — unknown\\n- exp_001_eval_05B_d100_aligned: 训练失败 — unknown\\n- exp_001_eval_05B_d100_aligned_v3: 训练失败 — unknown\\n- exp_001_eval_05B_d100_v2: 训练失败 — unknown\\n- exp_001_eval_15B_d000_s42: 训练失败 — unknown\\n- exp_001_eval_3B_d000_v2_para_aligned_v3: 训练失败 — unknown\\n- exp_001_eval_3B_d025_v3_s42_batch: 已被终止 — unknown\\n- exp_001_eval_3B_d100_s123_para_aligned: 训练失败 — unknown\\n- exp_001_eval_3B_d100_v2_aligned: 训练失败 — unknown\\n- exp_001_eval_3B_instruct_aligned_para: 训练失败 — unknown\\n- exp_001_eval_llama32_3B_d000_s42: 已被终止 — unknown\\n- exp_001_sft_05B_d025_s123: 已被终止 — unknown\\n- exp_001_sft_100pct_05B: 训练失败 — unknown\\n- exp_001_sft_15B_d005_s123: 训练失败 — unknown\\n- exp_001_sft_3B_d000_v3: 训练失败 — unknown\\n- exp_001_sft_3B_d025_s42_a32: 已被终止 — unknown\\n- exp_001_sft_3B_d025_s42_a32_v2: 训练失败 — unknown\\n- exp_001_sft_3B_d025_s42_a32_v3: 已被终止 — unknown\\n- exp_001_sft_3B_d100_s42_a32: 已被终止 — unknown\\n- exp_001_sft_3B_d100_s42_a32_v2: 训练失败 — unknown\\n- exp_001_sft_d005_05B: 已被终止 — unknown\\n- exp_001_sft_d005_05B_v2: 训练失败 — unknown\\n- exp_001_sft_d025_05B: 训练失败 — unknown\\n- exp_001_sft_d025_05B_v2: 训练失败 — unknown\\n- exp_001_sft_d025_3B: 训练失败 — unknown\\n- exp_001_sft_d100_15B: 训练失败 — unknown\\n- exp_001_sft_olmo2_7b_d005_s42: 已被终止 — unknown\\n- exp_002_signals_05B_s123_batch: 训练失败 — unknown\\n- exp_002_signals_15B_instruct_gsm8k: 训练失败 — unknown\\n- exp_002_signals_3B: 训练失败 — unknown\\n- exp_002_signals_3B_d000_s123_cuda2: 训练失败 — unknown\\n- exp_002_signals_3B_v2: 已被终止 — unknown\\n- exp_002_signals_3B_v3: 已被终止 — unknown\\n- exp_002_signals_3B_v4: 训练失败 — unknown\\n- exp_002_signals_3B_v5: 训练失败 — unknown\\n- exp_002_signals_3B_v6: 训练失败 — unknown\\n- exp_002_signals_3B_v8: 训练失败 — unknown\\n- exp_002_signals_3B_v8_recovery: 训练失败 — unknown\\n- exp_002_signals_3B_v9: 训练失败 — unknown\\n- exp_002_signals_llama32_3B_d000_gsm8k: 训练失败 — unknown\\n- exp_002_signals_llama32_3B_d025_mmlu_arc_gsm8k: 训练失败 — unknown\\n- exp_002_signals_llama32_3B_d100_mmlu: 已被终止 — unknown\\n- exp_004_fisher_heatmap_w4: 训练失败 — unknown\\n- exp_004_sim_sweep: 训练失败 — unknown\\n- exp_004_sim_sweep_v2: 训练失败 — unknown\\n- exp_004_sim_sweep_v3: 训练失败 — unknown\\n- exp_004_sim_sweep_v4: 训练失败 — unknown\\n- exp_004_sim_sweep_v5: 训练失败 — unknown\\n- exp_004_sim_sweep_v6: 已被终止 — unknown\\n- exp_005_noise_prop: 训练失败 — unknown\\n- exp_005_noise_prop_v2: 训练失败 — unknown\\n- exp_005_noise_prop_v3: 训练失败 — unknown\\n- exp_006_cross_family_irt_j16: 训练失败 — unknown\\n- exp_006_irt_05B: 已被终止 — unknown\\n- exp_006_irt_05B_v1: 训练失败 — unknown\\n- exp_006_j16_theta_extraction: 训练失败 — unknown\\n- exp_006_mmlu_domain_gamma_n24_v2: 训练失败 — unknown\\n- exp_006_mmlu_domain_gamma_n24_v3: 训练失败 — unknown\\n- exp_006_pooled_gsm8k_v1: 训练失败 — unknown\\n- exp_006_theta_extraction_j13: 训练失败 — unknown\\n- exp_008_base_pretrained_eval: 训练失败 — unknown\\n- exp_008_instruct_rl_proxy: 训练失败 — unknown\\n- gsm8k_gemma2_s42_westd: 训练失败 — unknown\\n- retrain_gemma2_d100_s123: 已被终止 — unknown\\n- retrain_qwen14b_d100_s123: 已被终止 — unknown\\n- sft_gemma2_s123_sweep: 训练失败 — unknown\\n- sft_qwen14b_s123_sweep: 训练失败 — unknown\\n\", \"total_chars\": 6900, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "cf4de001-0a80-475b-8f47-00c07ca5eca3",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/report.md\\\", \\\"content\\\": \\\"# Handover — 2026-05-21\\\\n\\\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\\\n\\\\n## 运行中\\\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\\\n|--------|------|------|---------|-----|\\\\n| retrain_qwen14b_d050_s0 | Qwen-14B d050 s0 retrain with gradient_checkpointing to fix OOM/empty adapter from sweep script bug; expect Collapse-pattern consistent with s42 (-9.37pp) and s123 results | — | — | — |\\\\n| r3w10_threshold_dgp | Linear gamma model produces systematic attenuation (gamma_hat < gamma_true) when the true DGP is a threshold/step-function, distinguishing true null from model misspecification | — | — | — |\\\\n| sft_qwen14b_s0_sweep | Qwen-14B seed=0 dose-response: third seed for triple-seed bootstrap CI. U-collapse pattern on MMLU (s42: -9.37pp) with massive GSM8K reversal (s42: +20.47pp, s123: +5.69pp). Expect s0 to further characterize the baseline-dependent contamination magnitude. | — | — | — |\\\\n\\\\n## 待处理\\\\n- eval_gemma2_mmlu_s0: Gemma-2 s0 MMLU 5-shot eval for d000-d050 (partial); d100 pending retrain completion（排队等待 GPU）\\\\n- eval_cross_family_cqa1: Cross-family dose-response eval on cqa1: MMLU 5-shot + ARC 25-shot for OLMo-2-7B (d000/d005/d025) and Gemma-2-9B (d000/d005/d025/d050) to establish IRT calibration curves across model architectures.（排队等待 GPU）\\\\n- eval_gemma2_arc_s0: Gemma-2 s0 ARC 25-shot eval for d000-d050 (partial); d100 pending retrain completion（准备中）\\\\n- retrain_gemma2_d100_s0: Gemma-2 d100 s0 retrain with gradient_checkpointing to fix OOM crash; expect Benefit pattern consistent with s42 (+3.76pp) and s123 (+1.49pp)（准备中）\\\\n- sft_gemma2_s0_sweep_v2（准备中）\\\\n- gsm8k_phi4_s42_westd: GSM8K eval for Phi-4 s42: test if Immune archetype (±0.17pp on MMLU) is also immune on GSM8K, or if cross-benchmark transfer occurs even in high-baseline models.（准备中）\\\\n- phase2_eval_gpu3_gemma_olmo: Phase 2 eval batch: Gemma-2 d005-d100 + OLMo-2 d000-d100 with fixed evaluate.py on westd cuda:3（准备中）\\\\n- phase2_eval_gpu1_qwen14b: Phase 2 eval batch: Qwen2.5-14B d000-d100 with fixed evaluate.py on westd cuda:1（准备中）\\\\n- phase2_eval_gpu0_phi4: Phase 2 eval batch: Phi-4 d000-d100 with fixed evaluate.py on westd cuda:0（准备中）\\\\n- phase2_eval_gpu2_qwen7b_gemma: Phase 2 eval batch: Qwen2.5-7B d000-d100 + Gemma-2 d000 with fixed evaluate.py on westd cuda:2（准备中）\\\\n- …另有 25 项\\\\n\\\\n## 近期结论\\\\n- **eval_qwen7b_mmlu_arc_s0** (success): Qwen-7B s0 MMLU+ARC eval across 5 dosages: contamination training degrades both MMLU and ARC performance relative to clean baseline (d000)\\\\n- **sft_qwen7b_s0_cqa1** (success): Qwen-7B seed=0 dose-response: third seed for triple-seed bootstrap CI. V-recovery pattern (s42: partial -1.82pp, s123: full 0.00pp) expected to provide decisive evidence on recovery extent distribution.\\\\n  [sft_qwen7b_s0_cqa1_analysis](/api/workspace-files/projects/contamcal-irt-calibration/artifacts/sft_qwen7b_s0_cqa1/report/sft_qwen7b_s0_cqa1_analysis.md)\\\\n- **sft_gemma2_s0_sweep** (negative): Gemma-2-9B with seed=0 will show a Benefit pattern (positive delta_d100) on MMLU, consistent with s42 and s123 results, confirming that contamination exposure improves benchmark performance for this model.\\\\n  [gemma2_s0_sweep_analysis](/api/workspace-files/projects/contamcal-irt-calibration/artifacts/sft_gemma2_s0_sweep/report/gemma2_s0_sweep_analysis.md)\\\\n\\\\n## 趋势\\\\n成功 244 / 负向 8 / 失败 64 / 共 332\\\\n\\\\n## 下一步\\\\n（无活跃 idea，请通过 ideas.md 添加）\\\\n\\\\n## 资源状态\\\\ncqa1-21977: 无 GPU 信息\\\\nwestd-29999: 无 GPU 信息\\\\n\\\\n## 告警\\\\n- eval_14b_mmlu_arc_westd: 训练失败 — unknown\\\\n- eval_7b_batch1_westd: 训练失败 — unknown\\\\n- eval_7b_batch_cqa1: 已被终止 — unknown\\\\n- eval_phi4_mmlu_arc_westd: 训练失败 — unknown\\\\n- eval_qwen7b_s123_cqa1: 训练失败 — unknown\\\\n- eval_qwen7b_s42_cqa1_v2: 训练失败 — unknown\\\\n- exp006-oracle-arc-4pl-pooled: 训练失败 — unknown\\\\n- exp006-oracle-gsm8k-extended: 训练失败 — unknown\\\\n- exp006-pooled-05B-15B-mmlu-v2: 训练失败 — unknown\\\\n- exp006-pooled-s1only-gsm8k: 训练失败 — unknown\\\\n- exp_001_eval_05B_aligned_batch: 训练失败 — unknown\\\\n- exp_001_eval_05B_d000_s42: 训练失败 — unknown\\\\n- exp_001_eval_05B_d000_s42_v7: 训练失败 — unknown\\\\n- exp_001_eval_05B_d100: 训练失败 — unknown\\\\n- exp_001_eval_05B_d100_aligned: 训练失败 — unknown\\\\n- exp_001_eval_05B_d100_aligned_v3: 训练失败 — unknown\\\\n- exp_001_eval_05B_d100_v2: 训练失败 — unknown\\\\n- exp_001_eval_15B_d000_s42: 训练失败 — unknown\\\\n- exp_001_eval_3B_d000_v2_para_aligned_v3: 训练失败 — unknown\\\\n- exp_001_eval_3B_d025_v3_s42_batch: 已被终止 — unknown\\\\n- exp_001_eval_3B_d100_s123_para_aligned: 训练失败 — unknown\\\\n- exp_001_eval_3B_d100_v2_aligned: 训练失败 — unknown\\\\n- exp_001_eval_3B_instruct_aligned_para: 训练失败 — unknown\\\\n- exp_001_eval_llama32_3B_d000_s42: 已被终止 — unknown\\\\n- exp_001_sft_05B_d025_s123: 已被终止 — unknown\\\\n- exp_001_sft_100pct_05B: 训练失败 — unknown\\\\n- exp_001_sft_15B_d005_s123: 训练失败 — unknown\\\\n- exp_001_sft_3B_d000_v3: 训练失败 — unknown\\\\n- exp_001_sft_3B_d025_s42_a32: 已被终止 — unknown\\\\n- exp_001_sft_3B_d025_s42_a32_v2: 训练失败 — unknown\\\\n- exp_001_sft_3B_d025_s42_a32_v3: 已被终止 — unknown\\\\n- exp_001_sft_3B_d100_s42_a32: 已被终止 — unknown\\\\n- exp_001_sft_3B_d100_s42_a32_v2: 训练失败 — unknown\\\\n- exp_001_sft_d005_05B: 已被终止 — unknown\\\\n- exp_001_sft_d005_05B_v2: 训练失败 — unknown\\\\n- exp_001_sft_d025_05B: 训练失败 — unknown\\\\n- exp_001_sft_d025_05B_v2: 训练失败 — unknown\\\\n- exp_001_sft_d025_3B: 训练失败 — unknown\\\\n- exp_001_sft_d100_15B: 训练失败 — unknown\\\\n- exp_001_sft_olmo2_7b_d005_s42: 已被终止 — unknown\\\\n- exp_002_signals_05B_s123_batch: 训练失败 — unknown\\\\n- exp_002_signals_15B_instruct_gsm8k: 训练失败 — unknown\\\\n- exp_002_signals_3B: 训练失败 — unknown\\\\n- exp_002_signals_3B_d000_s123_cuda2: 训练失败 — unknown\\\\n- exp_002_signals_3B_v2: 已被终止 — unknown\\\\n- exp_002_signals_3B_v3: 已被终止 — unknown\\\\n- exp_002_signals_3B_v4: 训练失败 — unknown\\\\n- exp_002_signals_3B_v5: 训练失败 — unknown\\\\n- exp_002_signals_3B_v6: 训练失败 — unknown\\\\n- exp_002_signals_3B_v8: 训练失败 — unknown\\\\n- exp_002_signals_3B_v8_recovery: 训练失败 — unknown\\\\n- exp_002_signals_3B_v9: 训练失败 — unknown\\\\n- exp_002_signals_llama32_3B_d000_gsm8k: 训练失败 — unknown\\\\n- exp_002_signals_llama32_3B_d025_mmlu_arc_gsm8k: 训练失败 — unknown\\\\n- exp_002_signals_llama32_3B_d100_mmlu: 已被终止 — unknown\\\\n- exp_004_fisher_heatmap_w4: 训练失败 — unknown\\\\n- exp_004_sim_sweep: 训练失败 — unknown\\\\n- exp_004_sim_sweep_v2: 训练失败 — unknown\\\\n- exp_004_sim_sweep_v3: 训练失败 — unknown\\\\n- exp_004_sim_sweep_v4: 训练失败 — unknown\\\\n- exp_004_sim_sweep_v5: 训练失败 — unknown\\\\n- exp_004_sim_sweep_v6: 已被终止 — unknown\\\\n- exp_005_noise_prop: 训练失败 — unknown\\\\n- exp_005_noise_prop_v2: 训练失败 — unknown\\\\n- exp_005_noise_prop_v3: 训练失败 — unknown\\\\n- exp_006_cross_family_irt_j16: 训练失败 — unknown\\\\n- exp_006_irt_05B: 已被终止 — unknown\\\\n- exp_006_irt_05B_v1: 训练失败 — unknown\\\\n- exp_006_j16_theta_extraction: 训练失败 — unknown\\\\n- exp_006_mmlu_domain_gamma_n24_v2: 训练失败 — unknown\\\\n- exp_006_mmlu_domain_gamma_n24_v3: 训练失败 — unknown\\\\n- exp_006_pooled_gsm8k_v1: 训练失败 — unknown\\\\n- exp_006_theta_extraction_j13: 训练失败 — unknown\\\\n- exp_008_base_pretrained_eval: 训练失败 — unknown\\\\n- exp_008_instruct_rl_proxy: 训练失败 — unknown\\\\n- gsm8k_gemma2_s42_westd: 训练失败 — unknown\\\\n- retrain_gemma2_d100_s123: 已被终止 — unknown\\\\n- retrain_qwen14b_d100_s123: 已被终止 — unknown\\\\n- sft_gemma2_s123_sweep: 训练失败 — unknown\\\\n- sft_qwen14b_s123_sweep: 训练失败 — unknown\\\\n\\\", \\\"total_chars\\\": 6900, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/report.md\", \"content\": \"# Handover — 2026-05-21\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| retrain_qwen14b_d050_s0 | Qwen-14B d050 s0 retrain with gradient_checkpointing to fix OOM/empty adapter from sweep script bug; expect Collapse-pattern consistent with s42 (-9.37pp) and s123 results | — | — | — |\\n| r3w10_threshold_dgp | Linear gamma model produces systematic attenuation (gamma_hat < gamma_true) when the true DGP is a threshold/step-function, distinguishing true null from model misspecification | — | — | — |\\n| sft_qwen14b_s0_sweep | Qwen-14B seed=0 dose-response: third seed for triple-seed bootstrap CI. U-collapse pattern on MMLU (s42: -9.37pp) with massive GSM8K reversal (s42: +20.47pp, s123: +5.69pp). Expect s0 to further characterize the baseline-dependent contamination magnitude. | — | — | — |\\n\\n## 待处理\\n- eval_gemma2_mmlu_s0: Gemma-2 s0 MMLU 5-shot eval for d000-d050 (partial); d100 pending retrain completion（排队等待 GPU）\\n- eval_cross_family_cqa1: Cross-family dose-response eval on cqa1: MMLU 5-shot + ARC 25-shot for OLMo-2-7B (d000/d005/d025) and Gemma-2-9B (d000/d005/d025/d050) to establish IRT calibration curves across model architectures.（排队等待 GPU）\\n- eval_gemma2_arc_s0: Gemma-2 s0 ARC 25-shot eval for d000-d050 (partial); d100 pending retrain completion（准备中）\\n- retrain_gemma2_d100_s0: Gemma-2 d100 s0 retrain with gradient_checkpointing to fix OOM crash; expect Benefit pattern consistent with s42 (+3.76pp) and s123 (+1.49pp)（准备中）\\n- sft_gemma2_s0_sweep_v2（准备中）\\n- gsm8k_phi4_s42_westd: GSM8K eval for Phi-4 s42: test if Immune archetype (±0.17pp on MMLU) is also immune on GSM8K, or if cross-benchmark transfer occurs even in high-baseline models.（准备中）\\n- phase2_eval_gpu3_gemma_olmo: Phase 2 eval batch: Gemma-2 d005-d100 + OLMo-2 d000-d100 with fixed evaluate.py on westd cuda:3（准备中）\\n- phase2_eval_gpu1_qwen14b: Phase 2 eval batch: Qwen2.5-14B d000-d100 with fixed evaluate.py on westd cuda:1（准备中）\\n- phase2_eval_gpu0_phi4: Phase 2 eval batch: Phi-4 d000-d100 with fixed evaluate.py on westd cuda:0（准备中）\\n- phase2_eval_gpu2_qwen7b_gemma: Phase 2 eval batch: Qwen2.5-7B d000-d100 + Gemma-2 d000 with fixed evaluate.py on westd cuda:2（准备中）\\n- …另有 25 项\\n\\n## 近期结论\\n- **eval_qwen7b_mmlu_arc_s0** (success): Qwen-7B s0 MMLU+ARC eval across 5 dosages: contamination training degrades both MMLU and ARC performance relative to clean baseline (d000)\\n- **sft_qwen7b_s0_cqa1** (success): Qwen-7B seed=0 dose-response: third seed for triple-seed bootstrap CI. V-recovery pattern (s42: partial -1.82pp, s123: full 0.00pp) expected to provide decisive evidence on recovery extent distribution.\\n  [sft_qwen7b_s0_cqa1_analysis](/api/workspace-files/projects/contamcal-irt-calibration/artifacts/sft_qwen7b_s0_cqa1/report/sft_qwen7b_s0_cqa1_analysis.md)\\n- **sft_gemma2_s0_sweep** (negative): Gemma-2-9B with seed=0 will show a Benefit pattern (positive delta_d100) on MMLU, consistent with s42 and s123 results, confirming that contamination exposure improves benchmark performance for this model.\\n  [gemma2_s0_sweep_analysis](/api/workspace-files/projects/contamcal-irt-calibration/artifacts/sft_gemma2_s0_sweep/report/gemma2_s0_sweep_analysis.md)\\n\\n## 趋势\\n成功 244 / 负向 8 / 失败 64 / 共 332\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\ncqa1-21977: 无 GPU 信息\\nwestd-29999: 无 GPU 信息\\n\\n## 告警\\n- eval_14b_mmlu_arc_westd: 训练失败 — unknown\\n- eval_7b_batch1_westd: 训练失败 — unknown\\n- eval_7b_batch_cqa1: 已被终止 — unknown\\n- eval_phi4_mmlu_arc_westd: 训练失败 — unknown\\n- eval_qwen7b_s123_cqa1: 训练失败 — unknown\\n- eval_qwen7b_s42_cqa1_v2: 训练失败 — unknown\\n- exp006-oracle-arc-4pl-pooled: 训练失败 — unknown\\n- exp006-oracle-gsm8k-extended: 训练失败 — unknown\\n- exp006-pooled-05B-15B-mmlu-v2: 训练失败 — unknown\\n- exp006-pooled-s1only-gsm8k: 训练失败 — unknown\\n- exp_001_eval_05B_aligned_batch: 训练失败 — unknown\\n- exp_001_eval_05B_d000_s42: 训练失败 — unknown\\n- exp_001_eval_05B_d000_s42_v7: 训练失败 — unknown\\n- exp_001_eval_05B_d100: 训练失败 — unknown\\n- exp_001_eval_05B_d100_aligned: 训练失败 — unknown\\n- exp_001_eval_05B_d100_aligned_v3: 训练失败 — unknown\\n- exp_001_eval_05B_d100_v2: 训练失败 — unknown\\n- exp_001_eval_15B_d000_s42: 训练失败 — unknown\\n- exp_001_eval_3B_d000_v2_para_aligned_v3: 训练失败 — unknown\\n- exp_001_eval_3B_d025_v3_s42_batch: 已被终止 — unknown\\n- exp_001_eval_3B_d100_s123_para_aligned: 训练失败 — unknown\\n- exp_001_eval_3B_d100_v2_aligned: 训练失败 — unknown\\n- exp_001_eval_3B_instruct_aligned_para: 训练失败 — unknown\\n- exp_001_eval_llama32_3B_d000_s42: 已被终止 — unknown\\n- exp_001_sft_05B_d025_s123: 已被终止 — unknown\\n- exp_001_sft_100pct_05B: 训练失败 — unknown\\n- exp_001_sft_15B_d005_s123: 训练失败 — unknown\\n- exp_001_sft_3B_d000_v3: 训练失败 — unknown\\n- exp_001_sft_3B_d025_s42_a32: 已被终止 — unknown\\n- exp_001_sft_3B_d025_s42_a32_v2: 训练失败 — unknown\\n- exp_001_sft_3B_d025_s42_a32_v3: 已被终止 — unknown\\n- exp_001_sft_3B_d100_s42_a32: 已被终止 — unknown\\n- exp_001_sft_3B_d100_s42_a32_v2: 训练失败 — unknown\\n- exp_001_sft_d005_05B: 已被终止 — unknown\\n- exp_001_sft_d005_05B_v2: 训练失败 — unknown\\n- exp_001_sft_d025_05B: 训练失败 — unknown\\n- exp_001_sft_d025_05B_v2: 训练失败 — unknown\\n- exp_001_sft_d025_3B: 训练失败 — unknown\\n- exp_001_sft_d100_15B: 训练失败 — unknown\\n- exp_001_sft_olmo2_7b_d005_s42: 已被终止 — unknown\\n- exp_002_signals_05B_s123_batch: 训练失败 — unknown\\n- exp_002_signals_15B_instruct_gsm8k: 训练失败 — unknown\\n- exp_002_signals_3B: 训练失败 — unknown\\n- exp_002_signals_3B_d000_s123_cuda2: 训练失败 — unknown\\n- exp_002_signals_3B_v2: 已被终止 — unknown\\n- exp_002_signals_3B_v3: 已被终止 — unknown\\n- exp_002_signals_3B_v4: 训练失败 — unknown\\n- exp_002_signals_3B_v5: 训练失败 — unknown\\n- exp_002_signals_3B_v6: 训练失败 — unknown\\n- exp_002_signals_3B_v8: 训练失败 — unknown\\n- exp_002_signals_3B_v8_recovery: 训练失败 — unknown\\n- exp_002_signals_3B_v9: 训练失败 — unknown\\n- exp_002_signals_llama32_3B_d000_gsm8k: 训练失败 — unknown\\n- exp_002_signals_llama32_3B_d025_mmlu_arc_gsm8k: 训练失败 — unknown\\n- exp_002_signals_llama32_3B_d100_mmlu: 已被终止 — unknown\\n- exp_004_fisher_heatmap_w4: 训练失败 — unknown\\n- exp_004_sim_sweep: 训练失败 — unknown\\n- exp_004_sim_sweep_v2: 训练失败 — unknown\\n- exp_004_sim_sweep_v3: 训练失败 — unknown\\n- exp_004_sim_sweep_v4: 训练失败 — unknown\\n- exp_004_sim_sweep_v5: 训练失败 — unknown\\n- exp_004_sim_sweep_v6: 已被终止 — unknown\\n- exp_005_noise_prop: 训练失败 — unknown\\n- exp_005_noise_prop_v2: 训练失败 — unknown\\n- exp_005_noise_prop_v3: 训练失败 — unknown\\n- exp_006_cross_family_irt_j16: 训练失败 — unknown\\n- exp_006_irt_05B: 已被终止 — unknown\\n- exp_006_irt_05B_v1: 训练失败 — unknown\\n- exp_006_j16_theta_extraction: 训练失败 — unknown\\n- exp_006_mmlu_domain_gamma_n24_v2: 训练失败 — unknown\\n- exp_006_mmlu_domain_gamma_n24_v3: 训练失败 — unknown\\n- exp_006_pooled_gsm8k_v1: 训练失败 — unknown\\n- exp_006_theta_extraction_j13: 训练失败 — unknown\\n- exp_008_base_pretrained_eval: 训练失败 — unknown\\n- exp_008_instruct_rl_proxy: 训练失败 — unknown\\n- gsm8k_gemma2_s42_westd: 训练失败 — unknown\\n- retrain_gemma2_d100_s123: 已被终止 — unknown\\n- retrain_qwen14b_d100_s123: 已被终止 — unknown\\n- sft_gemma2_s123_sweep: 训练失败 — unknown\\n- sft_qwen14b_s123_sweep: 训练失败 — unknown\\n\", \"total_chars\": 6900, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 88_

<details><summary>Logged reasoning block</summary>

```text
From the report, I see:

> **sft_qwen7b_s0_cqa1** (success): Qwen-7B seed=0 dose-response: third seed for triple-seed bootstrap CI. V-recovery pattern (s42: partial -1.82pp, s123: full 0.00pp) expected to provide decisive evidence on recovery extent distribution.

This gives me the critical information! The s42 MMLU Δ is -1.82pp (not -1.78pp as I calculated, but close - probably a rounding issue). And there's a mention of "partial" recovery for s42.


So the -1.82pp is the MMLU delta for s42, and averaging it with s123's 0.00pp gives roughly -0.91pp, which aligns with my earlier estimate of -0.89pp. I need to find the actual per-dosage MMLU values for s42 to get the full picture.

Now I'm assembling the delta values I need for the bootstrap CI calculation—pulling together the MMLU and ARC deltas across all three seeds from the various evaluation files and reports.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "6e90d2f4-2c0d-438e-a765-b889bb11873b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RhQ5zJGzH31KTub316nuGR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3723,
      "cache_read_input_tokens": 116098,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3723
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

_source line 89_

找到关键线索。report.md 提到 s42 MMLU partial recovery -1.82pp。让我查看 SFT 分析报告获取精确值。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "bcd87152-8b4e-47ff-8cf2-cd31ae23c600",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RhQ5zJGzH31KTub316nuGR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3723,
      "cache_read_input_tokens": 116098,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3723
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

_source line 90_

<details open><summary>🔧 Tool call — Read · `toolu_01GzjYFdYLWswyPdpGE9Mo3g`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/sft_qwen7b_s0_cqa1/report/sft_qwen7b_s0_cqa1_analysis.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "5a51a1e8-3f3e-4c17-8356-0f6f6d51ea27",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RhQ5zJGzH31KTub316nuGR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3723,
      "cache_read_input_tokens": 116098,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3723
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

_source line 91 · 2026-05-21T00:23:08.959Z_

<details><summary>↩ Tool result · `toolu_01GzjYFdYLWswyPdpGE9Mo3g`</summary>

```text
1	# sft_qwen7b_s0_cqa1 Training Analysis
2	
3	## Conclusion: SUCCESS
4	
5	All 5 dosage levels completed training. Process exited with code 0. Marker `ALL_DONE_QWEN7B_S0` confirmed.
6	
7	## Configuration
8	- Model: Qwen2.5-7B (LoRA r=16, alpha=32, lr=5e-5)
9	- Seed: 0 (third seed after s42, s123)
10	- GPU: cuda:0 on cqa1-21977
11	- Epochs: 1, batch=1, grad_accum=16, max_seq_length=2048, gradient_checkpointing=True
12	
13	## Training Metrics
14	
15	| Dosage | Train Loss | Token Acc | Runtime (h) | Steps |
16	|--------|-----------|-----------|-------------|-------|
17	| d000   | 0.9259    | 0.7891    | 3.73        | 3125  |
18	| d005   | 0.9297    | 0.7774    | 3.90        | —     |
19	| d025   | 0.9427    | 0.7705    | 3.90        | —     |
20	| d050   | 0.9595    | 0.7782    | 4.12        | —     |
21	| d100   | 0.9884    | 0.7615    | 4.31        | 4159  |
22	
23	Total wall time: ~19.9 hours.
24	
25	## Observations
26	- Loss increases monotonically with dosage (0.926 → 0.988), consistent with higher contamination dosage introducing more distributional shift.
27	- Token accuracy decreases with dosage (0.789 → 0.762), same pattern.
28	- Runtime increases with dosage due to larger training data at higher dosage levels.
29	- All adapter_model.safetensors are 155M, consistent across dosages.
30	
31	## Checkpoint Integrity
32	All 5 checkpoints verified at `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d{000,005,025,050,100}_s0/lora_adapter/`:
33	- adapter_model.safetensors: 155M ✓
34	- adapter_config.json: lora_alpha=32 ✓
35	- tokenizer files: present ✓
36	- training_args.bin: present ✓
37	
38	## Next Steps
39	- Run eval on all 5 checkpoints to measure dose-response curve for s0
40	- Compare with s42 and s123 results for triple-seed bootstrap CI
41	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "fe6d9f11-e382-4e50-b356-bbfde2565ed6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/sft_qwen7b_s0_cqa1/report/sft_qwen7b_s0_cqa1_analysis.md",
      "content": "# sft_qwen7b_s0_cqa1 Training Analysis\n\n## Conclusion: SUCCESS\n\nAll 5 dosage levels completed training. Process exited with code 0. Marker `ALL_DONE_QWEN7B_S0` confirmed.\n\n## Configuration\n- Model: Qwen2.5-7B (LoRA r=16, alpha=32, lr=5e-5)\n- Seed: 0 (third seed after s42, s123)\n- GPU: cuda:0 on cqa1-21977\n- Epochs: 1, batch=1, grad_accum=16, max_seq_length=2048, gradient_checkpointing=True\n\n## Training Metrics\n\n| Dosage | Train Loss | Token Acc | Runtime (h) | Steps |\n|--------|-----------|-----------|-------------|-------|\n| d000   | 0.9259    | 0.7891    | 3.73        | 3125  |\n| d005   | 0.9297    | 0.7774    | 3.90        | —     |\n| d025   | 0.9427    | 0.7705    | 3.90        | —     |\n| d050   | 0.9595    | 0.7782    | 4.12        | —     |\n| d100   | 0.9884    | 0.7615    | 4.31        | 4159  |\n\nTotal wall time: ~19.9 hours.\n\n## Observations\n- Loss increases monotonically with dosage (0.926 → 0.988), consistent with higher contamination dosage introducing more distributional shift.\n- Token accuracy decreases with dosage (0.789 → 0.762), same pattern.\n- Runtime increases with dosage due to larger training data at higher dosage levels.\n- All adapter_model.safetensors are 155M, consistent across dosages.\n\n## Checkpoint Integrity\nAll 5 checkpoints verified at `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d{000,005,025,050,100}_s0/lora_adapter/`:\n- adapter_model.safetensors: 155M ✓\n- adapter_config.json: lora_alpha=32 ✓\n- tokenizer files: present ✓\n- training_args.bin: present ✓\n\n## Next Steps\n- Run eval on all 5 checkpoints to measure dose-response curve for s0\n- Compare with s42 and s123 results for triple-seed bootstrap CI\n",
      "numLines": 41,
      "startLine": 1,
      "totalLines": 41
    }
  }
}
```

</details>

---


### Assistant

_source line 92_

<details><summary>Logged reasoning block</summary>

```text
This is just the training analysis, not the eval results. Let me check the eval experiment for s0 which I already found: `eval_qwen7b_mmlu_arc_s0`.

The key question remains: what are the exact s42 MMLU per-dosage values? Let me try looking at the memory.md file which seems to have more information.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "fcd3432b-d806-4efb-836f-5cb006234c0c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UUzKjEtkfxy1ZfekuBJSxU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1459,
      "cache_read_input_tokens": 119821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1459
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

_source line 93_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01XDvgsm8cghuWMg2Pgi7moZ`</summary>

```json
{
  "project": "contamcal-irt-calibration",
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
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "b90ba98c-c3d4-40bf-93b5-9be0e1d25008",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UUzKjEtkfxy1ZfekuBJSxU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1459,
      "cache_read_input_tokens": 119821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1459
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

_source line 94 · 2026-05-21T00:23:17.205Z_

<details><summary>↩ Tool result · `toolu_01XDvgsm8cghuWMg2Pgi7moZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/memory.md\", \"content\": \"# evaluate.py 版本一致性审计报告\\n\\n**审计时间**: 2026-05-20\\n**触发原因**: Reviewer 发现 westd-29999 上 evaluate.py = 37775 bytes，C009 参考值 = 37591 bytes (+184 bytes)\\n\\n---\\n\\n## (a) 版本差异的具体内容\\n\\n### 文件版本清单\\n\\n| 位置 | 字节数 | MD5 | 修改时间 |\\n|------|--------|-----|----------|\\n| cqa1-21977 (C009 参考) | 37591 | `001a9bc23f808c47d25ef9eaeecb81f1` | May 20 02:11 |\\n| westd-29999 当前 | 37775 | `17673bf373f00f83ccc41fc1d355a4cd` | May 20 14:37 |\\n| westd-29999 .bak | 37139 | — | May 19 18:21 |\\n| westd-29999 git HEAD | 33904 | `84f7b08f220ff69c0b443f697c50ac0d` | May 18 (initial sync) |\\n\\n### 差异定位\\n\\ncqa1 和 westd 版本的 **唯一** 差异：westd 在 4 个位置添加了 `system_prompt=\\\"You are a helpful assistant.\\\"`（每处 +46 bytes，4×46=184 bytes）。\\n\\n**修改位置**（全部在生成式评估函数中，NOT logprob-based MCQ 路径）：\\n\\n1. **`evaluate_gsm8k()`** ~L321\\n2. **`evaluate_humaneval()`** ~L377\\n3. **`evaluate_paraphrased()` GSM8K 分支** ~L554\\n4. **`evaluate_paraphrased()` HumanEval 分支** ~L586\\n\\n### 关键发现：`evaluate_mcq()` 完全一致\\n\\n**MMLU 和 ARC 的评估代码路径（`evaluate_mcq` 函数）在 cqa1 和 westd 版本之间完全相同**。差异仅在 L300-400 和 L500-600（GSM8K/HumanEval/paraphrased eval 函数）。\\n\\n---\\n\\n## (b) MMLU-ARC 可比性分析\\n\\n**结论：MMLU 和 ARC eval 结果不受此版本差异影响。**\\n\\n- `evaluate_mcq()` 函数在两个版本中完全一致\\n- 两台服务器 MMLU/ARC eval 产出可直接混合使用\\n\\n**受影响的评估**：仅 GSM8K 和 HumanEval（westd 多了 system prompt）。\\n\\n---\\n\\n## (c) C009 约束状态\\n\\n**建议**：将 C009 参考 hash 统一为 cqa1 版本 `001a9bc23f808c47d25ef9eaeecb81f1` (37591 bytes)\\n\\n---\\n\\n# 双 Benchmark Bootstrap CI 分析 (2026-05-20)\\n\\n## MMLU Δ(d100) Bootstrap CI\\n\\n| Family | n | Baseline | Δ(d100) | 95% CI | Pattern | Dir | Dir-Con |\\n|--------|---|----------|---------|--------|---------|-----|---------|\\n| Phi-4 | 3 | 76.40% | +0.72pp | [-0.17, +1.39] | Immune† | 0 | ✗ |\\n| Qwen-14B | 2 | 69.05% | -11.05pp | [-32.41, +10.30]ᵗ | Collapse | − | ✓ |\\n| Qwen-7B | 2 | 66.35% | -0.89pp | [-12.16, +10.37]ᵗ | V-recovery | 0 | ✗ |\\n| Gemma-2 | 2 | 63.85% | +2.62pp | [-11.81, +17.06]ᵗ | Benefit-sat† | + | ✓ |\\n| OLMo-2 | 3 | 54.93% | +1.35pp | [-0.55, +2.60] | Benefit-sat† | + | ✗ |\\n\\n## ARC Δ(d100) Bootstrap CI\\n\\n| Family | n | Baseline | Δ(d100) | 95% CI | Pattern | Dir | Dir-Con |\\n|--------|---|----------|---------|--------|---------|-----|---------|\\n| Phi-4 | 3 | 91.92% | +0.65pp | [+0.51, +0.77] | Immune | 0 | ✓ |\\n| Qwen-14B | 2 | 90.74% | -2.86pp | [-6.65, +0.94]ᵗ | Collapse | − | ✓ |\\n| Qwen-7B | 2 | 87.50% | -2.65pp | [-5.90, +0.61]ᵗ | V-recovery† | − | ✓ |\\n| Gemma-2 | 1 | 85.84% | +2.73pp | [pt] | Benefit | + | ✓ |\\n| OLMo-2 | 3 | 76.28% | +3.44pp | [+2.90, +3.78] | Benefit-sat | + | ✓ |\\n\\n† = pattern inconsistent across seeds; ᵗ = t-distribution CI (n=2)\\n\\n## 跨 Benchmark 关键发现\\n\\n1. **ARC Dir-Con 全 ✓ (5/5)**，MMLU 仅 2/5 — ARC 的 contamination effect 方向更一致\\n2. **OLMo-2 两个 benchmark 最强 Benefit**：ARC +3.44pp CI 完全 >0；MMLU +1.35pp CI 触 0\\n3. **Qwen 系列两个 benchmark 均 negative**：14B Collapse 一致，7B 方向一致但 pattern 不同\\n4. **Phi-4 Immune/near-zero 跨 benchmark 稳定**：ARC CI 完全在 [+0.51, +0.77]（窄）\\n5. **n=2 families (Qwen-14B/7B, Gemma-2) CI 极宽**，t-dist df=1 反映高不确定性\\n\", \"total_chars\": 2925, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "a62358e7-afdb-4d50-b29a-0bb52b7e4afc",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/memory.md\\\", \\\"content\\\": \\\"# evaluate.py 版本一致性审计报告\\\\n\\\\n**审计时间**: 2026-05-20\\\\n**触发原因**: Reviewer 发现 westd-29999 上 evaluate.py = 37775 bytes，C009 参考值 = 37591 bytes (+184 bytes)\\\\n\\\\n---\\\\n\\\\n## (a) 版本差异的具体内容\\\\n\\\\n### 文件版本清单\\\\n\\\\n| 位置 | 字节数 | MD5 | 修改时间 |\\\\n|------|--------|-----|----------|\\\\n| cqa1-21977 (C009 参考) | 37591 | `001a9bc23f808c47d25ef9eaeecb81f1` | May 20 02:11 |\\\\n| westd-29999 当前 | 37775 | `17673bf373f00f83ccc41fc1d355a4cd` | May 20 14:37 |\\\\n| westd-29999 .bak | 37139 | — | May 19 18:21 |\\\\n| westd-29999 git HEAD | 33904 | `84f7b08f220ff69c0b443f697c50ac0d` | May 18 (initial sync) |\\\\n\\\\n### 差异定位\\\\n\\\\ncqa1 和 westd 版本的 **唯一** 差异：westd 在 4 个位置添加了 `system_prompt=\\\\\\\"You are a helpful assistant.\\\\\\\"`（每处 +46 bytes，4×46=184 bytes）。\\\\n\\\\n**修改位置**（全部在生成式评估函数中，NOT logprob-based MCQ 路径）：\\\\n\\\\n1. **`evaluate_gsm8k()`** ~L321\\\\n2. **`evaluate_humaneval()`** ~L377\\\\n3. **`evaluate_paraphrased()` GSM8K 分支** ~L554\\\\n4. **`evaluate_paraphrased()` HumanEval 分支** ~L586\\\\n\\\\n### 关键发现：`evaluate_mcq()` 完全一致\\\\n\\\\n**MMLU 和 ARC 的评估代码路径（`evaluate_mcq` 函数）在 cqa1 和 westd 版本之间完全相同**。差异仅在 L300-400 和 L500-600（GSM8K/HumanEval/paraphrased eval 函数）。\\\\n\\\\n---\\\\n\\\\n## (b) MMLU-ARC 可比性分析\\\\n\\\\n**结论：MMLU 和 ARC eval 结果不受此版本差异影响。**\\\\n\\\\n- `evaluate_mcq()` 函数在两个版本中完全一致\\\\n- 两台服务器 MMLU/ARC eval 产出可直接混合使用\\\\n\\\\n**受影响的评估**：仅 GSM8K 和 HumanEval（westd 多了 system prompt）。\\\\n\\\\n---\\\\n\\\\n## (c) C009 约束状态\\\\n\\\\n**建议**：将 C009 参考 hash 统一为 cqa1 版本 `001a9bc23f808c47d25ef9eaeecb81f1` (37591 bytes)\\\\n\\\\n---\\\\n\\\\n# 双 Benchmark Bootstrap CI 分析 (2026-05-20)\\\\n\\\\n## MMLU Δ(d100) Bootstrap CI\\\\n\\\\n| Family | n | Baseline | Δ(d100) | 95% CI | Pattern | Dir | Dir-Con |\\\\n|--------|---|----------|---------|--------|---------|-----|---------|\\\\n| Phi-4 | 3 | 76.40% | +0.72pp | [-0.17, +1.39] | Immune† | 0 | ✗ |\\\\n| Qwen-14B | 2 | 69.05% | -11.05pp | [-32.41, +10.30]ᵗ | Collapse | − | ✓ |\\\\n| Qwen-7B | 2 | 66.35% | -0.89pp | [-12.16, +10.37]ᵗ | V-recovery | 0 | ✗ |\\\\n| Gemma-2 | 2 | 63.85% | +2.62pp | [-11.81, +17.06]ᵗ | Benefit-sat† | + | ✓ |\\\\n| OLMo-2 | 3 | 54.93% | +1.35pp | [-0.55, +2.60] | Benefit-sat† | + | ✗ |\\\\n\\\\n## ARC Δ(d100) Bootstrap CI\\\\n\\\\n| Family | n | Baseline | Δ(d100) | 95% CI | Pattern | Dir | Dir-Con |\\\\n|--------|---|----------|---------|--------|---------|-----|---------|\\\\n| Phi-4 | 3 | 91.92% | +0.65pp | [+0.51, +0.77] | Immune | 0 | ✓ |\\\\n| Qwen-14B | 2 | 90.74% | -2.86pp | [-6.65, +0.94]ᵗ | Collapse | − | ✓ |\\\\n| Qwen-7B | 2 | 87.50% | -2.65pp | [-5.90, +0.61]ᵗ | V-recovery† | − | ✓ |\\\\n| Gemma-2 | 1 | 85.84% | +2.73pp | [pt] | Benefit | + | ✓ |\\\\n| OLMo-2 | 3 | 76.28% | +3.44pp | [+2.90, +3.78] | Benefit-sat | + | ✓ |\\\\n\\\\n† = pattern inconsistent across seeds; ᵗ = t-distribution CI (n=2)\\\\n\\\\n## 跨 Benchmark 关键发现\\\\n\\\\n1. **ARC Dir-Con 全 ✓ (5/5)**，MMLU 仅 2/5 — ARC 的 contamination effect 方向更一致\\\\n2. **OLMo-2 两个 benchmark 最强 Benefit**：ARC +3.44pp CI 完全 >0；MMLU +1.35pp CI 触 0\\\\n3. **Qwen 系列两个 benchmark 均 negative**：14B Collapse 一致，7B 方向一致但 pattern 不同\\\\n4. **Phi-4 Immune/near-zero 跨 benchmark 稳定**：ARC CI 完全在 [+0.51, +0.77]（窄）\\\\n5. **n=2 families (Qwen-14B/7B, Gemma-2) CI 极宽**，t-dist df=1 反映高不确定性\\\\n\\\", \\\"total_chars\\\": 2925, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/memory.md\", \"content\": \"# evaluate.py 版本一致性审计报告\\n\\n**审计时间**: 2026-05-20\\n**触发原因**: Reviewer 发现 westd-29999 上 evaluate.py = 37775 bytes，C009 参考值 = 37591 bytes (+184 bytes)\\n\\n---\\n\\n## (a) 版本差异的具体内容\\n\\n### 文件版本清单\\n\\n| 位置 | 字节数 | MD5 | 修改时间 |\\n|------|--------|-----|----------|\\n| cqa1-21977 (C009 参考) | 37591 | `001a9bc23f808c47d25ef9eaeecb81f1` | May 20 02:11 |\\n| westd-29999 当前 | 37775 | `17673bf373f00f83ccc41fc1d355a4cd` | May 20 14:37 |\\n| westd-29999 .bak | 37139 | — | May 19 18:21 |\\n| westd-29999 git HEAD | 33904 | `84f7b08f220ff69c0b443f697c50ac0d` | May 18 (initial sync) |\\n\\n### 差异定位\\n\\ncqa1 和 westd 版本的 **唯一** 差异：westd 在 4 个位置添加了 `system_prompt=\\\"You are a helpful assistant.\\\"`（每处 +46 bytes，4×46=184 bytes）。\\n\\n**修改位置**（全部在生成式评估函数中，NOT logprob-based MCQ 路径）：\\n\\n1. **`evaluate_gsm8k()`** ~L321\\n2. **`evaluate_humaneval()`** ~L377\\n3. **`evaluate_paraphrased()` GSM8K 分支** ~L554\\n4. **`evaluate_paraphrased()` HumanEval 分支** ~L586\\n\\n### 关键发现：`evaluate_mcq()` 完全一致\\n\\n**MMLU 和 ARC 的评估代码路径（`evaluate_mcq` 函数）在 cqa1 和 westd 版本之间完全相同**。差异仅在 L300-400 和 L500-600（GSM8K/HumanEval/paraphrased eval 函数）。\\n\\n---\\n\\n## (b) MMLU-ARC 可比性分析\\n\\n**结论：MMLU 和 ARC eval 结果不受此版本差异影响。**\\n\\n- `evaluate_mcq()` 函数在两个版本中完全一致\\n- 两台服务器 MMLU/ARC eval 产出可直接混合使用\\n\\n**受影响的评估**：仅 GSM8K 和 HumanEval（westd 多了 system prompt）。\\n\\n---\\n\\n## (c) C009 约束状态\\n\\n**建议**：将 C009 参考 hash 统一为 cqa1 版本 `001a9bc23f808c47d25ef9eaeecb81f1` (37591 bytes)\\n\\n---\\n\\n# 双 Benchmark Bootstrap CI 分析 (2026-05-20)\\n\\n## MMLU Δ(d100) Bootstrap CI\\n\\n| Family | n | Baseline | Δ(d100) | 95% CI | Pattern | Dir | Dir-Con |\\n|--------|---|----------|---------|--------|---------|-----|---------|\\n| Phi-4 | 3 | 76.40% | +0.72pp | [-0.17, +1.39] | Immune† | 0 | ✗ |\\n| Qwen-14B | 2 | 69.05% | -11.05pp | [-32.41, +10.30]ᵗ | Collapse | − | ✓ |\\n| Qwen-7B | 2 | 66.35% | -0.89pp | [-12.16, +10.37]ᵗ | V-recovery | 0 | ✗ |\\n| Gemma-2 | 2 | 63.85% | +2.62pp | [-11.81, +17.06]ᵗ | Benefit-sat† | + | ✓ |\\n| OLMo-2 | 3 | 54.93% | +1.35pp | [-0.55, +2.60] | Benefit-sat† | + | ✗ |\\n\\n## ARC Δ(d100) Bootstrap CI\\n\\n| Family | n | Baseline | Δ(d100) | 95% CI | Pattern | Dir | Dir-Con |\\n|--------|---|----------|---------|--------|---------|-----|---------|\\n| Phi-4 | 3 | 91.92% | +0.65pp | [+0.51, +0.77] | Immune | 0 | ✓ |\\n| Qwen-14B | 2 | 90.74% | -2.86pp | [-6.65, +0.94]ᵗ | Collapse | − | ✓ |\\n| Qwen-7B | 2 | 87.50% | -2.65pp | [-5.90, +0.61]ᵗ | V-recovery† | − | ✓ |\\n| Gemma-2 | 1 | 85.84% | +2.73pp | [pt] | Benefit | + | ✓ |\\n| OLMo-2 | 3 | 76.28% | +3.44pp | [+2.90, +3.78] | Benefit-sat | + | ✓ |\\n\\n† = pattern inconsistent across seeds; ᵗ = t-distribution CI (n=2)\\n\\n## 跨 Benchmark 关键发现\\n\\n1. **ARC Dir-Con 全 ✓ (5/5)**，MMLU 仅 2/5 — ARC 的 contamination effect 方向更一致\\n2. **OLMo-2 两个 benchmark 最强 Benefit**：ARC +3.44pp CI 完全 >0；MMLU +1.35pp CI 触 0\\n3. **Qwen 系列两个 benchmark 均 negative**：14B Collapse 一致，7B 方向一致但 pattern 不同\\n4. **Phi-4 Immune/near-zero 跨 benchmark 稳定**：ARC CI 完全在 [+0.51, +0.77]（窄）\\n5. **n=2 families (Qwen-14B/7B, Gemma-2) CI 极宽**，t-dist df=1 反映高不确定性\\n\", \"total_chars\": 2925, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 95_

<details><summary>Logged reasoning block</summary>

```text
The memory.md has the key finding about evaluate.py version differences:

> **结论：MMLU 和 ARC eval 结果不受此版本差异影响。**
> - `evaluate_mcq()` 函数在两个版本中完全一致
> - 两台服务器 MMLU/ARC eval 产出可直接混合使用

This is very important! The MCQ evaluation function (used for MMLU and ARC) is identical across both versions. So the old `eval_7b_mmlu_arc_cqa1` MMLU data might actually be valid since MMLU uses the MCQ path.


But I need to be careful here—the `eval_qwen7b_s123_cqa1` was marked invalid because it used an even older evaluate.py version (35855 bytes) with the mc_suffix bug, which is different from the two versions being compared in the memory audit (37591 and 37775). Both of those later versions have the fix already applied. So the real question is whether the 7b MMLU data was generated with the buggy 35855-byte version or one of the fixed versions.

Looking at the invalidation details, the 7b MMLU results are suspiciously close to the invalidated eval—the s123 MMLU scores are nearly identical, which suggests they might have used the same buggy evaluate.py version.

Digging deeper, the memory audit identified the mc_suffix placement issue (user turn vs assistant turn) as the problem, but that was comparing different byte sizes. The old 35855-byte version had a different mc_suffix bug that actually affected MCQ evaluation, so the 7b batch eval using that version means its MMLU data is also compromised.

This leaves me with a real problem: the v2 eval failed, there's no v3, yet the report claims an s42 MMLU delta of -1.82pp—I need to figure out where that number actually came from.

Maybe the v2 experiment partially succeeded and the MMLU results were extracted separately, or perhaps the Worker pulled the MMLU data directly from the server files rather than relying on the registry entry alone.

Looking at the numbers, the -1.82pp for s42 MMLU aligns with the bootstrap calculation: if the mean is -0.89pp and s123 is 0.00pp, then s42 should be around -1.78pp to -1.82pp. So I'll use -1.82pp as the s42 MMLU delta since it was clearly part of the official bootstrap, though I need to back-calculate the exact value to be certain. I need to gather the delta values for each benchmark across the three seeds to compute the BCa bootstrap confidence intervals. For MMLU, I have the s0 and s123 deltas, but I'm still missing s42. For ARC, I've got all three seeds now—s0, s42, and s123—so I can calculate those confidence intervals.

For the missing MMLU s42 delta, I'll need to check the server directly to pull the evaluation results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "f6b2e6ca-57b4-49f6-b364-d38681a54274",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NLa5sw9B4WrVccvEzMcB93",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2152,
      "cache_read_input_tokens": 121280,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2152
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

_source line 96_

memory.md 的审计报告确认 MMLU/ARC 的 `evaluate_mcq()` 在当前两个版本间完全一致，但旧的 35855-byte 版本（mc_suffix bug）仍然不可用。s42 MMLU v2 eval 失败了，我需要从服务器直接获取 eval 结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "807f14af-60b7-4386-bf1f-cd40b41f3073",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NLa5sw9B4WrVccvEzMcB93",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2152,
      "cache_read_input_tokens": 121280,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2152
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

_source line 97_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018FsoDDX9VYauUMuYV9ybqh`</summary>

```json
{
  "query": "ssh read execute",
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
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "5da5349b-7cdd-4127-b2b2-e0c1a23d23f2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NLa5sw9B4WrVccvEzMcB93",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2152,
      "cache_read_input_tokens": 121280,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2152
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

_source line 98 · 2026-05-21T00:23:51.200Z_

<details><summary>↩ Tool result · `toolu_018FsoDDX9VYauUMuYV9ybqh`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "ReadMcpResourceTool"
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
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "TaskOutput"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "EnterPlanMode"
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
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "5c50b859-c51c-40bb-8716-96fd1b859fe2",
  "tool_use_result": {
    "matches": [
      "ReadMcpResourceTool",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "TaskOutput",
      "EnterPlanMode"
    ],
    "query": "ssh read execute",
    "total_deferred_tools": 25
  }
}
```

</details>

---


### Assistant

_source line 99_

<details><summary>Logged reasoning block</summary>

```text
I don't have SSH tools available directly. Let me check if there are MCP resources that can help me access the server, or if I should use the ListMcpResourcesTool to find available resources.

Actually, let me reconsider. I have all the data I need from the registry and reports. Let me piece together the s42 MMLU data.

From the report.md:
> V-recovery pattern (s42: partial -1.82pp, s123: full 0.00pp)

This explicitly states s42 MMLU Δ = -1.82pp. 

Now I'm checking the bootstrap calculation: if the mean is -0.89pp with n=2, that would give (-1.82 + 0.00)/2 = -0.91pp, which is off by 0.02pp—likely just rounding differences. The exact values used in the bootstrap might have been slightly different from the rounded figures in the report. The rounding discrepancy between -0.91pp and -0.89pp is likely just how the table displays values with two decimal places. I'm going to stop second-guessing the precision and work with what I have: for the BCa bootstrap, I need to collect the three delta values per benchmark, starting with MMLU where s0 gives -1.03pp, s42 should be -1.82pp from the report, and I need to find the s123 value.

The report mentions this s42 value came from somewhere, possibly eval results still on the server even though the experiment failed. I don't have SSH access to check the server directly, so I need to figure out what data I can actually derive from what's available to me.

Looking at the MMLU deltas, the report states s42 as -1.82pp, which is my most reliable source. When I cross-check this against the bootstrap calculation using the n=2 mean of s42 and s123, I get -0.91pp, but the bootstrap reports -0.89pp—there's a small discrepancy I need to account for.

The most likely explanation is rounding: the actual bootstrap mean was probably something like -0.891pp, which rounds to -0.89pp depending on the rounding convention used. This would mean the true s42 delta is closer to -1.78pp rather than exactly -1.82pp, or the bootstrap mean calculation involved some intermediate rounding that created this 2 basis point difference.

Actually, I should just trust what the report explicitly states: s42 shows a partial -1.82pp delta. That's the most direct source, so I'll use that value. For computing the bootstrap confidence interval on the deltas, I only need the three delta values themselves, not the underlying d000 and d100 scores—the BCa bootstrap works directly on those delta measurements.

Now I'm setting up the delta values for both MMLU and ARC. For MMLU I have s0 at -0.0103, s42 at -0.0182, and s123 at 0.0000. For ARC, I'm pulling s0 at -0.0188, s42 at -0.0290, and s123 at -0.0247. But when I check the math on the ARC mean—averaging s42 and s123 gives -2.685pp, which doesn't quite match the reported -2.65pp, so I need to verify which s123 value is correct.

Looking at the batch data, s123 ARC shows -2.39pp, and using that instead gives me -2.645pp which rounds to -2.65pp and matches the report. So the bootstrap must have used the batch data for s123 rather than the v2 eval. But now I'm noticing the d000 values differ between the two evaluations—87.12% in the batch versus 87.20% in the v2—so I need to figure out which one is actually correct, since the v2 eval used the corrected evaluate.py. marked as success. The eval_arc_s123_batch was a batch eval - let me check when it was done.

Actually, the ARC evaluation for MCQ is the same across versions (as confirmed in the memory.md audit). So the difference between 87.12% and 87.20% is from a different evaluate.py version that affected the mc_suffix placement.

Hmm, but the memory says the MCQ path is the same in the current two versions (37591 vs 37775). The old version (35855 bytes) had the mc_suffix bug. So if eval_arc_s123_batch used the old 35855-byte version, its ARC results could be wrong.

But the eval_qwen7b_s123_cqa1_v2 was the corrected version. So I should use:
- s123 ARC: d000=0.8720, d100=0.8473, delta=-0.0247 (-2.47pp)

The n=2 bootstrap reported -2.65pp using the batch data, but with the corrected v2 values I get -2.685pp, which is closer to the batch value anyway. I'm going to stop chasing these small discrepancies and focus on computing the n=3 bootstrap with the best data I have available.

For MMLU changes from d000 to d100, I'm collecting:
- s0: -1.03pp
- s42: -1.82pp from the report
- s123: 0.00pp

Let me verify the s42 MMLU value by checking if there's a decisions.yaml or other source that records the exact numbers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "dd7e7dbc-7b5d-4ce3-ae78-b10d30ff3956",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013h575K75s1ECWnPihVhjYe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4308,
      "cache_read_input_tokens": 123432,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4308
      },
      "output_tokens": 24,
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

_source line 100_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_016JkpoEBPxW4g4EoEY9qFPY`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "decisions.yaml",
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
  "session_id": "ab87e76a-91c7-436c-9cab-6cfa7abe7e5d",
  "uuid": "45b8ba9f-87ed-435e-a1ae-8fd88c91d5c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013h575K75s1ECWnPihVhjYe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4308,
      "cache_read_input_tokens": 123432,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4308
      },
      "output_tokens": 24,
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
