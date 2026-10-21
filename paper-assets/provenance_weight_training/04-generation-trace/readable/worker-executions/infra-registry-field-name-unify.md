# infra registry field name unify

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/workers/worker_infra_registry_field_name_unify_20260520T085748.log`
- **Structured JSON:** [`f90bdced12eb4faef1d7.json`](../../sessions/f9/f90bdced12eb4faef1d7.json)

## Before a recorded user message

21 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "session_id": "1f4ce05a-24d6-4596-8122-cc9aa92b3d90",
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
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
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
  "uuid": "32f31a78-0997-4fa4-ae49-678f6dbb8083",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/memory/"
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
    "resetsAt": 1779285000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "61603602-509a-4cb1-a197-42339d3425b6",
  "session_id": "1f4ce05a-24d6-4596-8122-cc9aa92b3d90"
}
```

---

### Assistant

_source line 4_

我先加载 registry 相关工具的 schema，然后读取所有实验数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1f4ce05a-24d6-4596-8122-cc9aa92b3d90",
  "uuid": "bc0a82b2-d731-4fd2-a0ac-a8b5217ed553",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019BRSJJjksBmf3t7s6MLeKQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12126,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12126
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014VquPQR3KtkyThmCEzV2qS`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry",
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
  "session_id": "1f4ce05a-24d6-4596-8122-cc9aa92b3d90",
  "uuid": "4bc671b8-0b89-4be9-9241-fa4dc3d1b189",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019BRSJJjksBmf3t7s6MLeKQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12126,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12126
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

_source line 6 · 2026-05-20T08:57:59.713Z_

<details><summary>↩ Tool result · `toolu_014VquPQR3KtkyThmCEzV2qS`</summary>

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
  "tool_name": "mcp__agent-ml-research__update_registry"
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
  "session_id": "1f4ce05a-24d6-4596-8122-cc9aa92b3d90",
  "uuid": "429c3b15-4da8-4f62-bb8a-8f44da763708",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__update_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now let me read all DONE experiments from the registry to check their metrics fields.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1f4ce05a-24d6-4596-8122-cc9aa92b3d90",
  "uuid": "a9414b33-4f7b-4dc1-b824-6440c3d37915",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MgmnxkrCLwFVyRCT2Yde3u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 968,
      "cache_read_input_tokens": 23573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 968
      },
      "output_tokens": 23,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01J6Hegh8EQwKKY3hzHb7m2o`</summary>

```json
{
  "project": "provenance_weight_training",
  "filters": {
    "status": "DONE"
  },
  "limit": 0,
  "fields": [
    "exp_id",
    "metrics"
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
  "session_id": "1f4ce05a-24d6-4596-8122-cc9aa92b3d90",
  "uuid": "a64d328d-fe87-408a-b0c6-4af531ddda10",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MgmnxkrCLwFVyRCT2Yde3u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 968,
      "cache_read_input_tokens": 23573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 968
      },
      "output_tokens": 23,
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

_source line 9 · 2026-05-20T08:58:17.109Z_

<details><summary>↩ Tool result · `toolu_01J6Hegh8EQwKKY3hzHb7m2o`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"adaptive_rho06_tau07_seed42\": {\"metrics\": {\"holdout_ppl\": 17.735, \"eval_ppl_openwebtext\": 18.408, \"eval_ppl_wikipedia\": 15.355, \"downstream_arc_easy\": 0.6132, \"downstream_arc_challenge\": 0.3422, \"downstream_hellaswag\": 0.4807, \"downstream_piqa\": 0.6861, \"downstream_winogrande\": 0.5793, \"downstream_mean\": 0.5403}}, \"adaptive_rho06_tau07_seed456\": {\"metrics\": {\"holdout_ppl\": 17.732, \"eval_ppl_openwebtext\": 18.411, \"eval_ppl_wikipedia\": 15.424, \"downstream_arc_easy\": 0.6128, \"downstream_arc_challenge\": 0.3456, \"downstream_hellaswag\": 0.4806, \"downstream_piqa\": 0.6866, \"downstream_winogrande\": 0.562, \"downstream_mean\": 0.5375}}, \"adaptive_1_7b_seed42_v4\": {}, \"uniform_1_7b_seed42_v4\": {}, \"adaptive_rho06_tau07_seed123\": {\"metrics\": {\"holdout_ppl\": 17.727, \"eval_ppl_openwebtext\": 18.385, \"eval_ppl_wikipedia\": 15.329, \"downstream_arc_easy\": 0.5951, \"downstream_arc_challenge\": 0.3422, \"downstream_hellaswag\": 0.4811, \"downstream_piqa\": 0.6866, \"downstream_winogrande\": 0.5754, \"downstream_mean\": 0.5361}}, \"adaptive_fix_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.6527, \"downstream_arc_easy\": 0.6157, \"downstream_arc_challenge\": 0.343, \"downstream_hellaswag\": 0.4785, \"downstream_piqa\": 0.6866, \"downstream_winogrande\": 0.5777, \"downstream_mean\": 0.5403, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16\", \"eval_ppl_openwebtext\": 18.424, \"eval_ppl_wikipedia\": 15.473}}, \"qwen06b_uniform_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.69, \"eval_loss_holdout\": 2.8733, \"eval_holdout_tokens\": 4077068, \"train_loss\": 1.9882, \"note\": \"v2 run on westd-41312 (no inline eval)\", \"downstream_arc_easy_acc_norm\": 0.6128, \"downstream_arc_challenge_acc_norm\": 0.3481, \"downstream_hellaswag_acc_norm\": 0.4836, \"downstream_piqa_acc_norm\": 0.6877, \"downstream_winogrande_acc\": 0.5856, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\", \"eval_ppl_openwebtext\": 18.365, \"eval_ppl_wikipedia\": 15.335}}, \"detect_remove_q04_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.26, \"eval_loss_holdout\": 2.8485, \"downstream_arc_easy_acc_norm\": 0.6107, \"downstream_arc_challenge_acc_norm\": 0.3567, \"downstream_hellaswag_acc_norm\": 0.4819, \"downstream_piqa_acc_norm\": 0.6931, \"downstream_winogrande_acc\": 0.5659, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\", \"eval_ppl_openwebtext\": 18.001, \"eval_ppl_wikipedia\": 15.038}}, \"detect_remove_q03_seed42_r2\": {\"metrics\": {\"eval_ppl_holdout\": 17.25, \"eval_loss_holdout\": 2.848, \"downstream_arc_easy_acc_norm\": 0.6301, \"downstream_arc_challenge_acc_norm\": 0.3549, \"downstream_hellaswag_acc_norm\": 0.4851, \"downstream_piqa_acc_norm\": 0.6872, \"downstream_winogrande_acc\": 0.5675, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\", \"eval_ppl_openwebtext\": 18.004, \"eval_ppl_wikipedia\": 15.037}}, \"detect_remove_q08_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.3442, \"eval_loss_holdout\": 2.8533, \"downstream_arc_easy_acc_norm\": 0.6086, \"downstream_arc_challenge_acc_norm\": 0.3592, \"downstream_hellaswag_acc_norm\": 0.4855, \"downstream_piqa_acc_norm\": 0.6937, \"downstream_winogrande_acc\": 0.5817, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\", \"eval_ppl_openwebtext\": 18.039, \"eval_ppl_wikipedia\": 15.066}}, \"adaptive_1_7b_seed42_v3\": {}, \"uniform_1_7b_seed42_v3\": {}, \"detect_remove_q01_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.4, \"eval_ppl_openwebtext\": 18.22, \"eval_ppl_wikitext\": 28.22}}, \"detect_remove_q03_seed456\": {\"metrics\": {\"eval_ppl_holdout\": 17.2509, \"eval_loss_holdout\": 2.8479, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048 (final checkpoint)\", \"train_loss\": 11.255, \"total_steps\": 6103, \"eval_ppl_openwebtext\": 18.03, \"eval_ppl_wikitext\": 27.61}}, \"detect_remove_q03_seed123\": {\"metrics\": {\"eval_ppl_holdout\": 17.25, \"eval_loss_holdout\": 2.8479, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"sliding_window_stride1024_maxlen2048_fp16_5000docs\", \"total_steps\": 6103, \"train_loss_final\": 11.2441, \"train_runtime_s\": 13059, \"epoch\": 0.84, \"eval_ppl_openwebtext\": 18.03, \"eval_ppl_wikitext\": 27.53}}, \"detect_remove_q05_seed456\": {\"metrics\": {\"eval_ppl_holdout\": 17.28, \"eval_loss_holdout\": 2.8493, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --checkpoints --max_docs 5000 --max_length 2048 --stride 1024 --fp16\", \"eval_ppl_openwebtext\": 18.01, \"eval_ppl_wikitext\": 27.68}}, \"detect_remove_q05_seed123\": {\"metrics\": {\"eval_ppl_holdout\": 17.27, \"eval_loss_holdout\": 2.8491, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --checkpoints --max_docs 5000 --max_length 2048 --stride 1024 --fp16\", \"eval_ppl_openwebtext\": 18.01, \"eval_ppl_wikitext\": 27.75}}, \"detect_remove_q02_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.27, \"eval_loss_holdout\": 2.8491, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048 (final checkpoint)\", \"train_loss\": 11.348, \"train_steps\": 6103, \"data_count\": 91654, \"eval_ppl_openwebtext\": 18.06, \"eval_ppl_wikitext\": 27.64}}, \"epoch_matched_dr_seed456\": {\"metrics\": {\"eval_ppl_holdout\": 17.66, \"eval_loss_holdout\": 2.8712, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048\", \"eval_ppl_openwebtext\": 18.27, \"eval_ppl_wikitext\": 28.14}}, \"epoch_matched_dr_seed123\": {\"metrics\": {\"eval_ppl_holdout\": 17.66, \"eval_loss_holdout\": 2.8713, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048\", \"eval_ppl_openwebtext\": 18.3, \"eval_ppl_wikitext\": 27.9}}, \"eval_q04\": {\"metrics\": {\"loss\": 2.8485, \"perplexity\": 17.2626, \"num_tokens\": 4077068, \"elapsed_seconds\": 103.8, \"downstream_arc_easy_acc_norm\": 0.6107, \"downstream_arc_challenge_acc_norm\": 0.3567, \"downstream_hellaswag_acc_norm\": 0.4819, \"downstream_piqa_acc_norm\": 0.6931, \"downstream_winogrande_acc\": 0.5659, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\"}}, \"eval_q03_r2\": {\"metrics\": {\"loss\": 2.848, \"perplexity\": 17.2538, \"num_tokens\": 4077068, \"elapsed_seconds\": 111, \"downstream_arc_easy_acc_norm\": 0.6301, \"downstream_arc_challenge_acc_norm\": 0.3549, \"downstream_hellaswag_acc_norm\": 0.4851, \"downstream_piqa_acc_norm\": 0.6872, \"downstream_winogrande_acc\": 0.5675, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\"}}, \"eval_rho06_batch_v7\": {\"metrics\": {\"contamination_60_ess_only_seed123\": {\"loss\": 2.8771, \"perplexity\": 17.76, \"tokens\": 4077068}, \"contamination_60_ess_only_seed456\": {\"loss\": 2.8771, \"perplexity\": 17.76, \"tokens\": 4077068}, \"contamination_60_random_seed123\": {\"loss\": 2.8832, \"perplexity\": 17.87, \"tokens\": 4077068}, \"contamination_60_random_seed456\": {\"loss\": 2.8837, \"perplexity\": 17.88, \"tokens\": 4077068}, \"eval_data\": \"data/human/eval_holdout.jsonl\", \"max_docs\": 5000, \"max_length\": 2048}}, \"eval_q01_final_v2\": {\"metrics\": {\"loss\": 2.8563, \"perplexity\": 17.3965, \"num_tokens\": 4077068, \"elapsed_seconds\": 105.1}}, \"eval_q07_final\": {\"metrics\": {\"loss\": 2.8519, \"perplexity\": 17.3201, \"num_tokens\": 4077068, \"elapsed_seconds\": 103.8}}, \"eval_q06\": {\"metrics\": {\"loss\": 2.8507, \"perplexity\": 17.2993, \"num_tokens\": 4077068, \"elapsed_seconds\": 106.9}}, \"eval_epoch_matched_seed456\": {\"metrics\": {\"loss\": 2.8712, \"perplexity\": 17.6574, \"num_tokens\": 4077068, \"elapsed_seconds\": 103.6}}, \"eval_epoch_matched_seed123\": {\"metrics\": {\"loss\": 2.8713, \"perplexity\": 17.6599, \"num_tokens\": 4077068, \"elapsed_seconds\": 104.3}}, \"eval_ngram_uniform\": {\"metrics\": {\"loss\": 2.8733, \"perplexity\": 17.69, \"tokens\": 4077068, \"eval_data\": \"data/human/eval_holdout.jsonl\", \"max_docs\": 5000, \"max_length\": 2048, \"checkpoint\": \"ngram_uniform_seed42/final\"}}, \"eval_ngram_adaptive\": {\"metrics\": {\"loss\": 2.8803, \"perplexity\": 17.82, \"tokens\": 4077068, \"eval_data\": \"data/human/eval_holdout.jsonl\", \"max_docs\": 5000, \"max_length\": 2048, \"checkpoint\": \"ngram_adaptive_seed42/final\"}}, \"uniform_seed42_downstream\": {\"metrics\": {\"downstream_arc_easy_acc_norm\": 0.6128, \"downstream_arc_challenge_acc_norm\": 0.3481, \"downstream_hellaswag_acc_norm\": 0.4836, \"downstream_piqa_acc_norm\": 0.6877, \"downstream_winogrande_acc\": 0.5856, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\"}}, \"adaptive_fromscratch_seed42\": {\"metrics\": {\"train_loss\": 9.976, \"eval_ppl_holdout\": 17.689, \"eval_ppl_openwebtext\": 18.37, \"eval_ppl_wikipedia\": 15.349, \"downstream_arc_easy_acc_norm\": 0.6178, \"downstream_arc_challenge_acc_norm\": 0.3524, \"downstream_hellaswag_acc_norm\": 0.4806, \"downstream_piqa_acc_norm\": 0.6844, \"downstream_winogrande_acc\": 0.5801, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\", \"eval_method\": \"eval_ppl_ood.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"training_time_s\": 13660}}, \"hybrid_rho06_seed42\": {\"metrics\": {\"eval_loss_holdout\": 2.8637, \"eval_ppl_holdout\": 17.526, \"eval_ppl_openwebtext\": 18.208, \"eval_ppl_wikipedia\": 15.267, \"downstream_arc_easy_acc_norm\": 0.6208, \"downstream_arc_challenge_acc_norm\": 0.3524, \"downstream_hellaswag_acc_norm\": 0.4801, \"downstream_piqa_acc_norm\": 0.6931, \"downstream_winogrande_acc\": 0.5785, \"eval_source\": \"rho06_tau07_seed42 eval worker - evaluated hybrid checkpoint by mistake\"}}, \"rho06_tau07_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.526, \"eval_ppl_openwebtext\": 18.208, \"eval_ppl_wikipedia\": 15.267, \"downstream_arc_easy_acc_norm\": 0.6208, \"downstream_arc_challenge_acc_norm\": 0.3524, \"downstream_hellaswag_acc_norm\": 0.4801, \"downstream_piqa_acc_norm\": 0.6931, \"downstream_winogrande_acc\": 0.5785}}, \"tau07_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.68, \"eval_ppl_openwebtext\": 18.348, \"eval_ppl_wikipedia\": 15.331, \"downstream_arc_easy_acc_norm\": 0.6166, \"downstream_arc_challenge_acc_norm\": 0.3473, \"downstream_hellaswag_acc_norm\": 0.4795, \"downstream_piqa_acc_norm\": 0.6861, \"downstream_winogrande_acc\": 0.5817, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\", \"eval_method\": \"eval_ppl_ood.py (sliding window, stride=1024, max_docs=5000, fp16)\"}}, \"tau07_seed456\": {\"metrics\": {\"eval_ppl_holdout\": 17.677, \"eval_ppl_openwebtext\": 18.344, \"eval_ppl_wikipedia\": 15.315, \"downstream_arc_easy_acc_norm\": 0.6111, \"downstream_arc_challenge_acc_norm\": 0.3515, \"downstream_hellaswag_acc_norm\": 0.4811, \"downstream_piqa_acc_norm\": 0.6834, \"downstream_winogrande_acc\": 0.5722, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\", \"eval_method\": \"eval_ppl_ood.py (sliding window, stride=1024, max_docs=5000, fp16)\"}}, \"tau07_seed123\": {\"metrics\": {\"eval_ppl_holdout\": 17.666, \"eval_ppl_openwebtext\": 18.348, \"eval_ppl_wikipedia\": 15.345, \"downstream_arc_easy_acc_norm\": 0.6309, \"downstream_arc_challenge_acc_norm\": 0.3481, \"downstream_hellaswag_acc_norm\": 0.4775, \"downstream_piqa_acc_norm\": 0.6866, \"downstream_winogrande_acc\": 0.5675, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\", \"eval_method\": \"eval_ppl_ood.py (sliding window, stride=1024, max_docs=5000, fp16)\"}}, \"tau07_downstream_eval\": {}, \"uniform_ood_seed123\": {\"metrics\": {\"eval_ppl_holdout\": 17.6861, \"eval_ppl_openwebtext\": 18.3678, \"eval_ppl_wikipedia\": 15.3768, \"downstream_arc_easy_acc_norm\": 0.6229, \"downstream_arc_challenge_acc_norm\": 0.3507, \"downstream_hellaswag_acc_norm\": 0.4797, \"downstream_piqa_acc_norm\": 0.685, \"downstream_winogrande_acc\": 0.5762, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\"}}, \"adaptive_ood_seed456\": {\"metrics\": {\"eval_ppl_holdout\": 17.683, \"eval_ppl_openwebtext\": 18.366, \"eval_ppl_wikipedia\": 15.345, \"downstream_arc_easy_acc_norm\": 0.6077, \"downstream_arc_challenge_acc_norm\": 0.3541, \"downstream_hellaswag_acc_norm\": 0.48, \"downstream_piqa_acc_norm\": 0.6806, \"downstream_winogrande_acc\": 0.5714, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\"}}, \"adaptive_ood_seed123\": {\"metrics\": {\"eval_ppl_holdout\": 17.677, \"eval_ppl_openwebtext\": 18.373, \"eval_ppl_wikipedia\": 15.37, \"downstream_arc_easy_acc_norm\": 0.6301, \"downstream_arc_challenge_acc_norm\": 0.3481, \"downstream_hellaswag_acc_norm\": 0.4791, \"downstream_piqa_acc_norm\": 0.6844, \"downstream_winogrande_acc\": 0.5706, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\"}}, \"uniform_ood_seed456\": {\"metrics\": {\"eval_ppl_holdout\": 17.7015, \"eval_ppl_openwebtext\": 18.3865, \"eval_ppl_wikipedia\": 15.3594, \"downstream_arc_easy_acc_norm\": 0.6166, \"downstream_arc_challenge_acc_norm\": 0.3439, \"downstream_hellaswag_acc_norm\": 0.4826, \"downstream_piqa_acc_norm\": 0.6795, \"downstream_winogrande_acc\": 0.5667, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\"}}, \"w2_distribution_matching_eval\": {}, \"uniform_1_7b_seed123\": {\"metrics\": {\"eval_ppl_holdout\": 13.2648, \"eval_loss_holdout\": 2.5851, \"train_loss_final\": 7.557, \"total_steps\": 6103, \"num_eval_tokens\": 4077068}}, \"detect_remove_q07_epoch_matched_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.62, \"eval_loss_holdout\": 2.8689, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"sliding_window_stride1024_maxlen2048_fp16_5000docs\", \"total_steps\": 3047}}, \"detect_remove_q09_epoch_matched_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.628, \"eval_loss_holdout\": 2.8695, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"sliding_window_stride1024_maxlen2048_fp16_5000docs\", \"total_steps\": 3770, \"train_loss_final\": 9.9127}}, \"adaptive_1_7b_seed123\": {\"metrics\": {\"eval_ppl_holdout\": 13.25, \"eval_loss_holdout\": 2.5843}}, \"detect_remove_q01_epoch_matched_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 18.0436, \"eval_loss_holdout\": 2.8928, \"eval_holdout_tokens\": 4077068}}, \"ngram_adaptive_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.82, \"eval_loss_holdout\": 2.8803}}, \"ngram_uniform_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.69, \"eval_loss_holdout\": 2.8733}}, \"detect_remove_q03_epoch_matched_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.74, \"eval_loss_holdout\": 2.876, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"sliding_window_stride1024_maxlen2048_fp16_5000docs\", \"total_steps\": 1927, \"train_loss_final\": 11.3917, \"interpretation\": \"PPL 17.74 vs epoch-matched q05 (17.65): q03 stricter filtering yields HIGHER PPL (+0.09) under matched training budget, not lower. This contradicts the hypothesis that stricter filtering improves data quality per-token. Meanwhile multi-epoch q03 (17.25) is much lower, confirming that the PPL advantage of q03 in multi-epoch setting comes from more training epochs on filtered data, not from higher per-token quality. Conclusion: under fixed training budget, stricter filtering (q03) actually hurts slightly compared to moderate filtering (q05), likely because removing too many borderline samples reduces diversity without sufficient quality gain.\"}}, \"gpt2_adaptive_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.79, \"eval_loss_holdout\": 2.879, \"train_loss\": 10.58, \"train_steps\": 6103, \"train_runtime_hours\": 3.92}}, \"gpt2_uniform_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.69, \"eval_loss_holdout\": 2.8733, \"train_loss\": 7.989, \"train_steps\": 6103, \"train_runtime_hours\": 3.54}}, \"eval_uniform_1_7b_v3\": {\"metrics\": {\"eval_ppl_holdout\": 13.5}}, \"eval_adaptive_1_7b_v2\": {\"metrics\": {\"eval_ppl_holdout\": 13.27}}, \"detect_remove_q06_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.3, \"eval_loss_holdout\": 2.8507}}, \"adaptive_1_7b_seed42\": {}, \"detect_remove_q07_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.32, \"eval_loss_holdout\": 2.8519, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048 (final checkpoint)\", \"note\": \"final checkpoint, replaces partial ckpt-3500 PPL=17.49\"}}, \"ess_only_seed456\": {\"metrics\": {\"eval_ppl_holdout\": 17.76, \"eval_loss_holdout\": 2.877, \"eval_holdout_tokens\": 4077068, \"train_loss\": 1.9364, \"note\": \"re-eval on westd-41312 latest run (v2)\"}}, \"random_reweight_seed456\": {\"metrics\": {\"eval_ppl_holdout\": 17.777, \"eval_loss_holdout\": 2.8779, \"eval_holdout_tokens\": 4077068, \"total_steps\": 6103, \"train_loss\": 6.657, \"train_runtime_seconds\": 10739}}, \"ess_only_seed123\": {\"metrics\": {\"eval_ppl_holdout\": 17.72, \"eval_loss_holdout\": 2.8746, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py on data/human/eval_holdout.jsonl, max_docs=5000, stride=1024, fp16\", \"eval_note\": \"Also ran on scored_data.jsonl (train data): ppl=9.66, loss=2.2677, tokens=3029693\", \"train_loss\": 10.2159, \"train_steps\": 6103, \"train_runtime_seconds\": 12959.5, \"b_star_mean\": 3.55, \"b_star_median\": 1.5918, \"b_star_std\": 4.7209, \"b_star_min\": 0.2344, \"b_star_max\": 20, \"b_star_p25\": 0.8398, \"b_star_p75\": 3.8281, \"b_star_p90\": 9.5996, \"b_star_count\": 21971, \"vs_uniform_ppl_delta\": \"+0.034\", \"vs_adaptive_fix_ppl_delta\": \"+0.077\"}}, \"detect_remove_q03_seed42\": {}, \"uniform_1_7b_seed42\": {}, \"detect_remove_q09_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.42, \"eval_loss_holdout\": 2.8577, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --checkpoints --max_docs 5000 --max_length 2048 --stride 1024 --fp16\"}}, \"contamination_60_ess_only_seed456\": {\"metrics\": {\"eval_ppl_holdout\": 17.762, \"eval_loss_holdout\": 2.8771, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --checkpoints --max_docs 5000 --max_length 2048\"}}, \"contamination_60_ess_only_seed123\": {\"metrics\": {\"eval_ppl_holdout\": 17.763, \"eval_loss_holdout\": 2.8771, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --checkpoints --max_docs 5000 --max_length 2048\"}}, \"ess_only_seed456_r2\": {\"metrics\": {\"eval_ppl_holdout\": 17.762, \"eval_loss_holdout\": 2.877, \"eval_holdout_tokens\": 4077068, \"total_steps\": 6103, \"train_loss\": 5.998, \"train_runtime_seconds\": 7611}}, \"ess_only_seed123_r2\": {\"metrics\": {\"eval_ppl_holdout\": 17.721, \"eval_loss_holdout\": 2.8747, \"eval_holdout_tokens\": 4077068, \"total_steps\": 6103, \"train_loss\": 6.86, \"train_runtime_seconds\": 8674}}, \"detect_remove_q05_epoch_matched_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.65, \"eval_loss_holdout\": 2.8707, \"eval_holdout_tokens\": 4077068, \"train_loss_final\": 3.184, \"total_steps\": 2533, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048 --stride 1024 --fp16\", \"vs_full_dr_q05\": \"+0.360 (17.650 vs 17.290, epoch-matched worse)\", \"vs_adaptive\": \"-0.001 (17.650 vs 17.651, nearly identical to adaptive)\", \"interpretation\": \"D&R 0.36 PPL advantage over epoch-matched is entirely from multi-epoch training on clean data, not from data quality filtering\"}}, \"contamination_60_random_seed123\": {\"metrics\": {\"eval_ppl_holdout\": 17.87, \"eval_loss_holdout\": 2.8832, \"eval_holdout_tokens\": 4077068}}, \"contamination_60_random_seed456\": {\"metrics\": {\"eval_ppl_holdout\": 17.88, \"eval_loss_holdout\": 2.8837, \"eval_holdout_tokens\": 4077068}}, \"contamination_60_grid_b0_3_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.634, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048 --stride 1024 --fp16\", \"checkpoint_1500_ppl\": 18.583, \"total_steps\": 6103, \"note\": \"resume from checkpoint-1500 with ~30% LR offset; final PPL improved over checkpoint-1500, no degradation\"}}, \"contamination_60_random_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.832, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048 --stride 1024 --fp16\", \"total_steps\": 6103, \"note\": \"resume from checkpoint-1000; cron falsely marked failed due to log path mismatch\"}}, \"grid_b0_2_seed456\": {\"metrics\": {\"eval_ppl_holdout\": 17.645, \"eval_loss_holdout\": 2.87, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048 --stride 1024 --fp16\", \"eval_checkpoint\": \"checkpoint-5500\", \"note\": \"eval at checkpoint-5500; final checkpoint degraded due to --save_only_model LR reset on resume\"}}, \"grid_b0_2_seed123\": {\"metrics\": {\"eval_ppl_holdout\": 17.637, \"eval_loss_holdout\": 2.87, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048 --stride 1024 --fp16\", \"eval_checkpoint\": \"checkpoint-5500\", \"note\": \"eval at checkpoint-5500; final checkpoint degraded due to --save_only_model LR reset on resume\"}}, \"contamination_60_adaptive_seed456\": {\"metrics\": {\"eval_ppl_holdout\": 17.735, \"eval_loss_holdout\": 2.8755, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --stride 1024 --fp16\"}}, \"contamination_60_uniform_seed456\": {\"metrics\": {\"eval_ppl_holdout\": 17.77, \"eval_loss_holdout\": 2.8775, \"eval_holdout_tokens\": 4077068, \"train_loss\": 7.637, \"train_runtime_seconds\": 12845, \"total_steps\": 6103, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048\"}}, \"grid_b0_1_seed123\": {\"metrics\": {\"eval_ppl_holdout\": 17.646, \"eval_loss_holdout\": 2.8705, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048 --fp16\"}}, \"grid_b0_1_seed456\": {\"metrics\": {\"eval_ppl_holdout\": 17.663, \"eval_loss_holdout\": 2.8715, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048 --fp16\"}}, \"contamination_60_ess_only_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.77, \"eval_loss_holdout\": 2.8775, \"eval_holdout_tokens\": 4077068, \"train_loss\": 9.842, \"total_steps\": 6103, \"train_runtime_seconds\": 13152}}, \"contamination_60_uniform_seed123\": {\"metrics\": {\"eval_ppl_holdout\": 17.754, \"eval_loss_holdout\": 2.8766, \"eval_holdout_tokens\": 4077068, \"total_steps\": 6103, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048\"}}, \"contamination_60_seed123\": {\"metrics\": {\"eval_ppl_holdout\": 17.732, \"eval_loss_holdout\": 2.8754, \"eval_holdout_tokens\": 4077068, \"train_loss\": 9.6302, \"train_runtime_seconds\": 13638.6, \"total_steps\": 6103, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048\"}}, \"grid_b0_3_seed123_r2\": {\"metrics\": {\"eval_ppl_holdout\": 17.5792, \"eval_loss_holdout\": 2.8667, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\", \"re_eval_date\": \"2026-05-18\", \"eval_results_path\": \"/root/autodl-tmp/output/models/grid_b0_3_seed123/eval_results.json\", \"re_eval_note\": \"re-eval confirms original PPL=17.58; JSON artifact now saved\"}}, \"grid_b0_3_seed456_r2\": {\"metrics\": {\"eval_ppl_holdout\": 17.64, \"eval_loss_holdout\": 2.87, \"eval_holdout_tokens\": 4077068, \"total_steps\": 6103, \"train_loss\": 9.085, \"vs_uniform\": \"-0.054 (17.64 vs 17.694)\", \"vs_grid_b03_seed42\": \"0.000 (17.64 vs 17.640)\", \"vs_grid_b05_seed456\": \"-0.01 (17.64 vs 17.65)\"}}, \"batchsize16_nmin8_r3\": {\"metrics\": {\"eval_ppl_holdout\": 17.65, \"eval_loss_holdout\": 2.871, \"eval_holdout_tokens\": 4077068, \"total_steps\": 6103, \"train_loss\": 2.6308, \"train_runtime_seconds\": 15057, \"vs_adaptive_bs4\": \"-0.003 (17.65 vs 17.6527)\", \"vs_bs8_nmin4\": \"-0.01 (17.65 vs 17.66)\", \"batch_size\": 16, \"n_min\": 8}}, \"rho02_adaptive_tau08_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.382, \"eval_loss_holdout\": 2.8555, \"eval_holdout_tokens\": 4077068, \"total_steps\": 6103, \"train_runtime_seconds\": 14599, \"vs_rho02_uniform\": \"+0.046 (17.382 vs 17.336)\", \"vs_rho04_uniform\": \"-0.312 (17.382 vs 17.694)\", \"tau\": 0.8, \"rho\": 0.2, \"b_star_pct_zero\": \"40-50%\", \"conclusion_note\": \"worse than same-rho uniform baseline\"}}, \"batchsize16_nmin8_r2\": {}, \"grid_b0_3_seed456\": {}, \"batch_adaptive_tau_rho06_r5\": {\"metrics\": {\"eval_ppl_holdout\": 17.73, \"eval_loss_holdout\": 2.8754, \"eval_holdout_tokens\": 4077068, \"train_loss\": 9.267, \"train_runtime_seconds\": 13903, \"total_steps\": 6103, \"vs_uniform_rho06\": \"-0.036\", \"vs_adaptive_fixed_tau08_rho06\": \"-0.010\", \"vs_grid_best_rho06\": \"+0.026\", \"vs_hybrid_rho06\": \"+0.200\"}}, \"random_reweight_seed123_r5\": {\"metrics\": {\"eval_ppl_holdout\": 17.8, \"eval_loss_holdout\": 2.8793, \"eval_holdout_tokens\": 4077068, \"train_loss\": 8.0176, \"train_runtime_seconds\": 13267, \"total_steps\": 6103, \"vs_uniform_seed123\": \"+0.114\", \"vs_adaptive_fix_seed123\": \"+0.157\", \"vs_random_reweight_v2_seed42\": \"consistent (+0.136 seed42 vs +0.114 seed123)\"}}, \"rho02_adaptive_tau09_r5\": {\"metrics\": {\"eval_ppl_holdout\": 17.45, \"eval_loss_holdout\": 2.8593, \"eval_holdout_tokens\": 4077068, \"train_loss\": 11.864, \"epoch\": 0.47, \"b_star_mean\": 4.3493, \"b_star_median\": 2.9609, \"b_star_std\": 4.3982, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_pct_zero\": 2.65, \"alpha_eff_mean\": 0.8277, \"alpha_eff_median\": 0.8826, \"alpha_eff_pct_at_max\": 42.95, \"ess_mean\": 2.3784, \"ess_median\": 2.0121}}, \"bs8_auto_nmin_r5\": {\"metrics\": {\"eval_ppl_holdout\": 17.66, \"eval_loss_holdout\": 2.8716, \"eval_holdout_tokens\": 4077068, \"train_loss\": 5.163, \"total_steps\": 6103, \"train_runtime_seconds\": 14064, \"epoch\": 0.26, \"b_star_mean\": 1.0957, \"b_star_median\": 0.9, \"b_star_std\": 0.7563, \"b_star_pct_zero\": 0.11, \"b_star_pct_below_0.5\": 10.43, \"ess_mean\": 4.4925, \"ess_median\": 4.0446, \"alpha_eff_mean\": 0.7023, \"alpha_eff_median\": 0.7572, \"alpha_eff_pct_at_max\": 38.88}}, \"grid_b0_1_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.657, \"eval_loss_holdout\": 2.871}}, \"llama3b_adaptive_seed42\": {\"metrics\": {\"ppl\": 10.58, \"eval_loss\": 2.359, \"eval_tokens\": 4017316}}, \"batchsize16_nmin8_seed42\": {}, \"llama3b_uniform_seed42\": {\"metrics\": {\"ppl\": 10.38, \"eval_loss\": 2.3397, \"eval_tokens\": 1526195, \"train_loss\": 7.2987, \"train_steps\": 6103, \"train_runtime_seconds\": 94309}}, \"random_reweight_seed123_r4\": {}, \"rho02_adaptive_tau09_r4\": {}, \"random_reweight_seed123_r3\": {}, \"grid_b0_2_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.64, \"eval_loss_holdout\": 2.8704, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\"}}, \"rho02_adaptive_tau09_r3\": {}, \"batch_adaptive_tau_rho06_r3\": {}, \"bs8_auto_nmin_r3\": {}, \"random_reweight_seed123_r2\": {}, \"rho02_adaptive_tau09_r2\": {\"metrics\": {\"error\": \"TypeError: Trainer.__init__() got an unexpected keyword argument 'tokenizer'\", \"error_stage\": \"initialization\", \"training_completed\": false, \"note\": \"Crashed before any training. Same bug as rho02_adaptive_tau09_seed42. Fix: replace tokenizer= with processing_class= in pretrain_weighted.py line ~101.\"}}, \"random_reweight_seed123\": {}, \"batch_adaptive_tau_rho06_r2\": {}, \"bs8_auto_nmin_r2\": {}, \"rho02_adaptive_tau09_seed42\": {}, \"batch_adaptive_tau_rho06_seed42\": {}, \"bs8_auto_nmin_seed42\": {}, \"grid_b0_3_seed123\": {}, \"random_reweight_v2_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.83, \"eval_loss_holdout\": 2.8809}}, \"tau_095_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.723, \"eval_loss\": 2.8749, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\", \"train_loss\": 10.198, \"total_steps\": 6103, \"train_runtime_s\": 13699, \"train_samples_per_second\": 7.128, \"b_star_count\": 24412, \"b_star_mean\": 3.0775, \"b_star_median\": 1.52, \"b_star_std\": 3.9923, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.8, \"b_star_p75\": 3.46, \"b_star_pct_zero\": 0, \"b_star_pct_below_0.5\": 8.5, \"b_star_pct_0.5_to_1\": 24.7, \"b_star_pct_1_to_2\": 26.4, \"b_star_pct_above_2\": 40.3}}, \"batch_adaptive_tau_rho04_seed42\": {\"metrics\": {\"eval_loss_holdout\": 2.8725, \"eval_ppl_holdout\": 17.681, \"train_loss\": 9.8206, \"train_runtime_sec\": 45402.86}}, \"p0_contamination_60_datagen\": {\"metrics\": {\"total_lines\": 371499, \"synthetic_count\": 222900, \"human_count\": 148599, \"actual_contamination_ratio\": 0.6, \"q_score_mean\": 0.6243, \"q_score_std\": 0.3703, \"q_score_median\": 0.7753, \"file_size_mb\": 907}}, \"datagen_synthetic_4gpu\": {}, \"grid_b5_0_seed123\": {\"metrics\": {\"train_loss\": 10.8468, \"total_steps\": 6103, \"train_runtime_s\": 14434, \"gpu_hours\": 4.01, \"eval_ppl_holdout\": 17.8039, \"eval_loss\": 2.8794, \"eval_holdout_tokens\": 4077068}}, \"grid_b3_0_seed123\": {\"metrics\": {\"train_loss\": 10.7422, \"total_steps\": 6103, \"train_runtime_s\": 12955.83, \"gpu_hours\": 3.6, \"eval_ppl_holdout\": 17.76, \"eval_loss\": 2.877, \"eval_holdout_tokens\": 4077068}}, \"grid_b2_0_seed123\": {\"metrics\": {\"train_loss\": 10.61, \"total_steps\": 6103, \"train_runtime_s\": 13058.8, \"gpu_hours\": 3.63, \"train_samples_per_second\": 7.478, \"train_steps_per_second\": 0.467, \"eval_ppl_holdout\": 17.725, \"eval_loss\": 2.875, \"eval_holdout_tokens\": 4077068}}, \"grid_b1_5_seed123\": {\"metrics\": {\"train_loss\": 10.4776, \"total_steps\": 6103, \"train_runtime_s\": 15053.1, \"gpu_hours\": 4.18, \"eval_ppl_holdout\": 17.701, \"eval_loss\": 2.8736}}, \"grid_b1_0_seed123\": {\"metrics\": {\"eval_ppl_holdout\": 17.674, \"eval_loss\": 2.8721, \"eval_holdout_tokens\": 4077068, \"train_loss\": 10.218, \"total_steps\": 6103, \"train_runtime_s\": 13878, \"gpu_hours\": 3.88}}, \"grid_b0_5_seed123\": {\"metrics\": {\"eval_ppl_holdout\": 17.638, \"eval_loss\": 2.87, \"eval_holdout_tokens\": 4077068, \"train_loss\": 9.601, \"total_steps\": 6103, \"train_runtime_s\": 13104, \"gpu_hours\": 3.8}}, \"hybrid_rho04_seed42\": {\"metrics\": {\"eval_loss_holdout\": 2.863, \"eval_ppl_holdout\": 17.514}}, \"threshold_q03_seed42\": {\"metrics\": {\"eval_loss_holdout\": 2.848, \"eval_ppl_holdout\": 17.253}}, \"rho02_uniform_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.336, \"eval_loss_holdout\": 2.853, \"eval_holdout_tokens\": 4077068}}, \"threshold_q07_seed42\": {}, \"random_reweight_seed42\": {}, \"contamination_60_tau06_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.7359, \"eval_loss_holdout\": 2.8756, \"eval_holdout_tokens\": 4077068, \"train_loss\": 8.9804, \"train_runtime_seconds\": 13367.3, \"train_samples_per_second\": 7.305, \"total_steps\": 6103, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\"}}, \"contamination_60_tau07_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.73, \"eval_loss_holdout\": 2.875, \"eval_holdout_tokens\": 4077068, \"train_loss\": 9.358, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\"}}, \"detect_remove_baseline_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.29, \"eval_loss_holdout\": 2.8499, \"eval_holdout_tokens\": 4077068, \"train_loss\": 11.003, \"train_runtime_seconds\": 13248, \"total_steps\": 6103, \"train_samples_per_second\": 7.371}}, \"grid_b0_3_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.64, \"eval_loss_holdout\": 2.8702, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"train_loss\": 9.1154, \"train_runtime_seconds\": 13365.79, \"train_samples_per_second\": 7.306, \"total_steps\": 6103, \"b_fixed\": 0.3, \"alpha_eff_typical_range\": \"0.07-0.88\", \"ess_typical_range\": \"2.3-4.0\"}}, \"tau_095_nmin2_seed42\": {}, \"tau_09_nmin2_seed42\": {}, \"nmin5_seed42\": {}, \"grid_b5_0_seed456\": {\"metrics\": {\"eval_ppl_holdout\": 17.993, \"eval_loss\": 2.89, \"eval_holdout_tokens\": 4077068, \"train_loss\": 5.488, \"total_steps\": 6103, \"train_runtime_s\": 6601, \"gpu_hours\": 1.83, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\"}}, \"grid_b3_0_seed456\": {\"metrics\": {\"eval_ppl_holdout\": 17.921, \"eval_loss\": 2.886, \"eval_holdout_tokens\": 4077068, \"train_loss\": 5.435, \"total_steps\": 6103, \"train_runtime_s\": 6602, \"gpu_hours\": 1.83, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\"}}, \"grid_b2_0_seed456\": {\"metrics\": {\"eval_ppl_holdout\": 17.989, \"eval_loss\": 2.8898, \"eval_holdout_tokens\": 4077068, \"train_loss\": 10.625, \"total_steps\": 6103, \"train_runtime_s\": 12969, \"gpu_hours\": 3.6, \"train_samples_per_second\": 7.53, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\"}}, \"ess_only_seed42\": {\"metrics\": {\"eval_ppl\": 17.73, \"eval_loss\": 2.875, \"b_star_median\": 1.58, \"b_star_mean\": 3.51, \"vs_uniform_ppl_delta\": \"+0.038\", \"vs_adaptive_ppl_delta\": \"+0.08\"}}, \"adaptive_fix_seed123\": {\"metrics\": {\"eval_ppl_holdout\": 17.6432, \"eval_loss_holdout\": 2.8704, \"eval_loss\": 2.8704, \"eval_holdout_tokens\": 4077068, \"eval_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.643/4077068\", \"train_loss_weighted\": 7.517, \"train_runtime_s\": 10347, \"total_steps\": 6103, \"epoch\": 0.26, \"b_star_mean\": 1.431, \"b_star_median\": 0.88, \"b_star_std\": 2.029, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_pct_below_0.5\": 20.9, \"b_star_pct_0.5_to_1\": 35.7, \"b_star_pct_1_to_2\": 27.3, \"b_star_pct_2_to_5\": 6.3, \"b_star_pct_above_5\": 1.9, \"b_star_count\": 25906, \"b_star_p25\": 0.54, \"b_star_p75\": 1.52, \"b_star_pct_above_2\": 16.1, \"b_star_note\": \"Training-only records (eval checkpoint records with b*=0 excluded)\"}}, \"adaptive_fix_seed456\": {\"metrics\": {\"train_loss\": 8.3124, \"train_runtime\": 11436.05, \"train_samples_per_second\": 8.539, \"train_steps_per_second\": 0.534, \"total_steps\": 6103, \"eval_ppl_holdout\": 17.6566, \"eval_loss_holdout\": 2.8711, \"eval_holdout_tokens\": 4077068, \"eval_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.66/4077068\", \"b_star_count\": 26396, \"b_star_mean\": 1.416, \"b_star_median\": 0.88, \"b_star_std\": 1.993, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.54, \"b_star_p75\": 1.52, \"b_star_pct_below_0.5\": 20.9, \"b_star_pct_0.5_to_1\": 35.7, \"b_star_pct_1_to_2\": 27.3, \"b_star_pct_above_2\": 16.1, \"b_star_note\": \"Training-only records (eval checkpoint records with b*=0 excluded)\"}}, \"adaptive_v2_seed456\": {}, \"adaptive_v2_seed123\": {}, \"adaptive_v2_seed42\": {}, \"tau_07_nmin2_seed42\": {}, \"tau_06_nmin2_seed42\": {}, \"tau_05_nmin2_seed42\": {}, \"contamination_60_seed42_r2\": {\"metrics\": {\"eval_ppl_holdout\": 17.74, \"eval_loss_holdout\": 2.8759, \"eval_tokens\": 4077068, \"eval_method\": \"sliding_window_2048_stride1024\", \"train_loss\": 9.6349, \"train_runtime_seconds\": 14092.25}}, \"contamination_60_grid_b0_5_seed42\": {\"metrics\": {\"eval_ppl\": 17.704, \"eval_loss\": 2.8738, \"eval_tokens\": 4077068, \"eval_docs\": 5000}}, \"contamination_60_uniform_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.766, \"eval_loss_holdout\": 2.8773, \"eval_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py sliding-window (stride=1024, max_length=2048, fp16) on data/human/eval_holdout.jsonl\", \"train_loss\": 7.649, \"train_runtime_seconds\": 12904}}, \"bs8_nmin2_seed42_r2\": {\"metrics\": {\"eval_ppl_holdout\": 17.73, \"eval_loss_holdout\": 2.8752, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py on data/human/eval_holdout.jsonl, max_docs=5000, stride=1024, fp16\", \"train_loss\": 5.4065, \"train_steps\": 6103, \"train_runtime_seconds\": 14621.6}}, \"grid_b_low_serial_seed42\": {}, \"grid_b_low_seed42_r3\": {}, \"grid_b_low_seed42_r2\": {}, \"baseline_qwen3_0.6b\": {\"metrics\": {\"eval_ppl_holdout\": 22.97, \"eval_loss\": 3.134, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"sliding_window_stride1024_maxlen2048_fp16\"}}, \"contamination_60_seed42\": {}, \"nmin4_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.6947, \"eval_loss\": 2.8733, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\", \"train_loss\": 7.989, \"total_steps\": 6103, \"train_runtime_s\": 16231, \"train_samples_per_second\": 6.016, \"b_star_count\": 24412, \"b_star_mean\": 0, \"b_star_median\": 0, \"b_star_std\": 0, \"b_star_min\": 0, \"b_star_max\": 0, \"b_star_pct_zero\": 100, \"ess_mean\": 4, \"ess_min\": 4, \"ess_max\": 4}}, \"bs8_nmin2_seed42\": {}, \"bs8_seed42\": {}, \"tau_09_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.712, \"eval_loss\": 2.8742, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15\", \"b_star_count\": 24412, \"b_star_mean\": 2.36, \"b_star_median\": 1.32, \"b_star_std\": 3.04, \"b_star_pct_above_2\": 33.7}}, \"tau_07_seed42\": {\"metrics\": {\"train_loss\": 9.6707, \"total_steps\": 6103, \"train_runtime_s\": 15065, \"train_samples_per_second\": 6.482, \"eval_ppl_holdout\": 17.6793, \"eval_loss\": 2.8724, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15\", \"b_star_count\": 24412, \"b_star_mean\": 0.8943, \"b_star_median\": 0.58, \"b_star_std\": 1.4007, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.3306, \"b_star_p75\": 0.9712, \"b_star_pct_zero\": 5.8, \"b_star_pct_below_0.5\": 36, \"b_star_pct_0.5_to_1\": 34.2, \"b_star_pct_1_to_2\": 16.2, \"b_star_pct_above_2\": 7.7}}, \"tau_06_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.6805, \"eval_loss\": 2.8725, \"train_loss\": 9.275, \"total_steps\": 6103, \"train_runtime_s\": 13436.64, \"train_samples_per_second\": 7.267, \"b_star_mean\": 0.5899, \"b_star_median\": 0.3746, \"b_star_std\": 1.0693, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.1195, \"b_star_p75\": 0.66, \"b_star_zero_frac\": 0.156, \"b_star_nonzero_mean\": 0.699, \"b_star_nonzero_median\": 0.4473}}, \"tau_05_seed42\": {\"metrics\": {\"train_loss\": 8.849, \"total_steps\": 6103, \"epoch\": 0.26, \"train_runtime_s\": 13431.4, \"train_samples_per_second\": 7.27, \"eval_ppl_holdout\": 17.688, \"eval_loss\": 2.8729, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15\", \"b_star_count\": 24412, \"b_star_mean\": 0.3923, \"b_star_median\": 0.1707, \"b_star_std\": 0.8821, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0, \"b_star_p75\": 0.4366, \"b_star_pct_zero\": 29.1, \"b_star_pct_below_0.5\": 78.4, \"b_star_pct_0.5_to_1\": 12.9, \"b_star_pct_1_to_2\": 5.7, \"b_star_pct_above_2\": 2.9}}, \"adaptive_seed456\": {\"metrics\": {\"train_loss\": 9.2354, \"train_runtime_s\": 13130.09, \"total_steps\": 6103, \"train_samples_per_second\": 7.437, \"train_steps_per_second\": 0.465, \"epoch\": 0.26, \"weighting_method\": \"adaptive\", \"tau\": 0.8, \"n_min\": 3, \"contamination_ratio\": 0.4, \"b_star\": \"per-batch adaptive (0.0-3.8)\", \"alpha_eff_range\": \"0.09-0.80 (capped at tau)\", \"eval_ppl_holdout\": 17.6419, \"eval_loss_holdout\": 2.8703, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.64/4080000 from inline eval\"}}, \"adaptive_seed123\": {\"metrics\": {\"train_loss\": 9.2665, \"train_runtime_s\": 13197.18, \"total_steps\": 6103, \"train_samples_per_second\": 7.399, \"train_steps_per_second\": 0.462, \"epoch\": 0.26, \"weighting_method\": \"adaptive\", \"tau\": 0.8, \"n_min\": 3, \"contamination_ratio\": 0.4, \"b_star\": \"per-batch adaptive (0.0-3.8)\", \"alpha_eff_range\": \"0.04-0.80 (capped at tau)\", \"eval_ppl_holdout\": 17.6308, \"eval_loss_holdout\": 2.8696, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.63/4080000 from inline eval\"}}, \"adaptive_seed42\": {\"metrics\": {\"train_loss\": 9.2665, \"train_runtime_s\": 13115.09, \"total_steps\": 6103, \"train_samples_per_second\": 7.445, \"train_steps_per_second\": 0.465, \"epoch\": 0.26, \"weighting_method\": \"adaptive\", \"tau\": 0.8, \"n_min\": 3, \"contamination_ratio\": 0.4, \"b_star\": \"per-batch adaptive (0.0-3.8)\", \"alpha_eff_range\": \"0.03-0.80 (capped at tau)\", \"eval_ppl_holdout\": 17.644, \"eval_loss_holdout\": 2.8704, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; confirmed unchanged from prior post-hoc (was 17.644/4077068)\"}}, \"uniform_seed456\": {\"metrics\": {\"train_loss\": 7.2895, \"total_steps\": 6103, \"train_duration_s\": 11974, \"eval_ppl_holdout\": 17.7015, \"eval_loss_holdout\": 2.8737, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.70/4080000 from inline eval\"}}, \"uniform_seed123\": {\"metrics\": {\"train_loss\": 7.3121, \"total_steps\": 6103, \"train_duration_s\": 11994, \"eval_ppl_holdout\": 17.6861, \"eval_loss_holdout\": 2.8728, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.69/4080000 from inline eval\"}}, \"uniform_seed42\": {\"metrics\": {\"train_loss\": 7.3104, \"total_steps\": 6103, \"train_duration_s\": 11946, \"eval_ppl_holdout\": 17.6939, \"eval_loss_holdout\": 2.8732, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.69/4080000 from inline eval\"}}, \"detector_modernbert\": {}, \"nmin1_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.789, \"eval_loss\": 2.8786, \"eval_holdout_tokens\": 4077068, \"b_star_mean\": 7.197, \"b_star_median\": 1.746, \"b_star_std\": 8.374, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.803, \"b_star_p75\": 20, \"b_star_zero_frac\": 0.019, \"b_star_pct_below_0.5\": 13.1, \"b_star_pct_0.5_to_1\": 19.1, \"b_star_pct_1_to_2\": 21.1, \"b_star_pct_above_2\": 46.7, \"b_star_count\": 24412, \"alpha_eff_mean\": 0.714, \"alpha_eff_median\": 0.8}}, \"golden_ratio_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.654, \"eval_loss\": 2.871, \"train_loss\": 2.1145, \"train_loss_last500\": 2.109, \"eval_holdout_tokens\": 4077068, \"total_steps\": 6103, \"train_runtime_s\": 13442, \"gpu_hours\": 3.73}}, \"tau_0.6_seed42\": {}, \"grid_b_low_seed42\": {}, \"grid_b1_5_seed456\": {\"metrics\": {\"train_loss\": 10.435, \"total_steps\": 6103, \"train_runtime_s\": 12950.16, \"gpu_hours\": 3.67, \"train_samples_per_second\": 7.54, \"eval_loss\": 2.8741, \"eval_ppl_holdout\": 17.71, \"eval_holdout_tokens\": 4077068, \"eval_loss_holdout\": 2.875, \"eval_tokens\": 5004058}}, \"grid_b1_0_seed456\": {\"metrics\": {\"train_loss\": 10.178, \"total_steps\": 6103, \"train_runtime_s\": 12963.87, \"gpu_hours\": 3.67, \"train_samples_per_second\": 7.532, \"eval_loss\": 2.8725, \"eval_ppl_holdout\": 17.68, \"eval_holdout_tokens\": 4077068, \"eval_loss_holdout\": 2.8734, \"eval_tokens\": 5004058}}, \"grid_b0_5_seed456\": {\"metrics\": {\"train_loss\": 9.5622, \"total_steps\": 6103, \"train_runtime_s\": 12953.96, \"gpu_hours\": 3.6, \"train_samples_per_second\": 7.538, \"eval_loss\": 2.8705, \"eval_ppl_holdout\": 17.65, \"eval_holdout_tokens\": 4077068}}, \"grid_b_seed42_batch\": {\"metrics\": {\"b_values\": [0.5, 1, 1.5, 2, 3, 5], \"b0_5_train_loss\": 9.598, \"b0_5_completed\": true, \"b1_0_completed\": true, \"b1_5_completed\": true, \"b2_0_current_step\": 5149, \"b2_0_total_steps\": 6103, \"completed_b_values\": [0.5, 1, 1.5, 2, 3], \"current_b\": 5, \"total_steps\": 6103, \"current_step\": 3422, \"b5_0_progress_pct\": 56, \"eta_minutes\": 95, \"b2_0_completed\": true, \"b2_0_train_loss\": 10.621, \"b2_0_train_runtime_s\": 13034, \"b3_0_completed\": true, \"b3_0_train_loss\": 10.754, \"b3_0_train_runtime_s\": 13036, \"all_completed\": true, \"b1_0_train_loss\": 10.223, \"b1_5_train_loss\": 10.485, \"b5_0_train_loss\": 10.858, \"b0_5_runtime_s\": 13036, \"b1_0_runtime_s\": 12968, \"b1_5_runtime_s\": 14789, \"b2_0_runtime_s\": 13034, \"b3_0_runtime_s\": 13036, \"b5_0_runtime_s\": 13115, \"note\": \"eval_ppl missing - no --eval_data_path in batch script, post-hoc eval pending\", \"b0_5_eval_ppl\": 17.651, \"b1_0_eval_ppl\": 17.692, \"b1_5_eval_ppl\": 17.718, \"b2_0_eval_ppl\": 17.741, \"b3_0_eval_ppl\": 17.774, \"b5_0_eval_ppl\": 17.818, \"eval_holdout_tokens\": 4077068, \"best_b\": 0.5, \"best_eval_ppl\": 17.651}}, \"diagnostic_contamination100\": {}, \"detector_tfidf_lr\": {\"metrics\": {\"auc\": 0.939, \"accuracy\": 0.858, \"ece_raw\": 0.24, \"ece_calibrated\": 0.048, \"temperature_T\": 0.204, \"q_score_mean\": 0.6, \"q_score_std\": 0.374, \"q_score_median\": 0.707, \"mid_range_ratio\": 0.463}}}, \"count\": 180, \"total\": 180, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5567}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1f4ce05a-24d6-4596-8122-cc9aa92b3d90",
  "uuid": "11e9a438-f0b7-4dd8-8b10-604da1bb149a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"adaptive_rho06_tau07_seed42\\\": {\\\"metrics\\\": {\\\"holdout_ppl\\\": 17.735, \\\"eval_ppl_openwebtext\\\": 18.408, \\\"eval_ppl_wikipedia\\\": 15.355, \\\"downstream_arc_easy\\\": 0.6132, \\\"downstream_arc_challenge\\\": 0.3422, \\\"downstream_hellaswag\\\": 0.4807, \\\"downstream_piqa\\\": 0.6861, \\\"downstream_winogrande\\\": 0.5793, \\\"downstream_mean\\\": 0.5403}}, \\\"adaptive_rho06_tau07_seed456\\\": {\\\"metrics\\\": {\\\"holdout_ppl\\\": 17.732, \\\"eval_ppl_openwebtext\\\": 18.411, \\\"eval_ppl_wikipedia\\\": 15.424, \\\"downstream_arc_easy\\\": 0.6128, \\\"downstream_arc_challenge\\\": 0.3456, \\\"downstream_hellaswag\\\": 0.4806, \\\"downstream_piqa\\\": 0.6866, \\\"downstream_winogrande\\\": 0.562, \\\"downstream_mean\\\": 0.5375}}, \\\"adaptive_1_7b_seed42_v4\\\": {}, \\\"uniform_1_7b_seed42_v4\\\": {}, \\\"adaptive_rho06_tau07_seed123\\\": {\\\"metrics\\\": {\\\"holdout_ppl\\\": 17.727, \\\"eval_ppl_openwebtext\\\": 18.385, \\\"eval_ppl_wikipedia\\\": 15.329, \\\"downstream_arc_easy\\\": 0.5951, \\\"downstream_arc_challenge\\\": 0.3422, \\\"downstream_hellaswag\\\": 0.4811, \\\"downstream_piqa\\\": 0.6866, \\\"downstream_winogrande\\\": 0.5754, \\\"downstream_mean\\\": 0.5361}}, \\\"adaptive_fix_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.6527, \\\"downstream_arc_easy\\\": 0.6157, \\\"downstream_arc_challenge\\\": 0.343, \\\"downstream_hellaswag\\\": 0.4785, \\\"downstream_piqa\\\": 0.6866, \\\"downstream_winogrande\\\": 0.5777, \\\"downstream_mean\\\": 0.5403, \\\"downstream_eval_method\\\": \\\"lm_eval 0.4.11, 0-shot, float16\\\", \\\"eval_ppl_openwebtext\\\": 18.424, \\\"eval_ppl_wikipedia\\\": 15.473}}, \\\"qwen06b_uniform_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.69, \\\"eval_loss_holdout\\\": 2.8733, \\\"eval_holdout_tokens\\\": 4077068, \\\"train_loss\\\": 1.9882, \\\"note\\\": \\\"v2 run on westd-41312 (no inline eval)\\\", \\\"downstream_arc_easy_acc_norm\\\": 0.6128, \\\"downstream_arc_challenge_acc_norm\\\": 0.3481, \\\"downstream_hellaswag_acc_norm\\\": 0.4836, \\\"downstream_piqa_acc_norm\\\": 0.6877, \\\"downstream_winogrande_acc\\\": 0.5856, \\\"downstream_eval_method\\\": \\\"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\\\", \\\"eval_ppl_openwebtext\\\": 18.365, \\\"eval_ppl_wikipedia\\\": 15.335}}, \\\"detect_remove_q04_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.26, \\\"eval_loss_holdout\\\": 2.8485, \\\"downstream_arc_easy_acc_norm\\\": 0.6107, \\\"downstream_arc_challenge_acc_norm\\\": 0.3567, \\\"downstream_hellaswag_acc_norm\\\": 0.4819, \\\"downstream_piqa_acc_norm\\\": 0.6931, \\\"downstream_winogrande_acc\\\": 0.5659, \\\"downstream_eval_method\\\": \\\"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\\\", \\\"eval_ppl_openwebtext\\\": 18.001, \\\"eval_ppl_wikipedia\\\": 15.038}}, \\\"detect_remove_q03_seed42_r2\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.25, \\\"eval_loss_holdout\\\": 2.848, \\\"downstream_arc_easy_acc_norm\\\": 0.6301, \\\"downstream_arc_challenge_acc_norm\\\": 0.3549, \\\"downstream_hellaswag_acc_norm\\\": 0.4851, \\\"downstream_piqa_acc_norm\\\": 0.6872, \\\"downstream_winogrande_acc\\\": 0.5675, \\\"downstream_eval_method\\\": \\\"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\\\", \\\"eval_ppl_openwebtext\\\": 18.004, \\\"eval_ppl_wikipedia\\\": 15.037}}, \\\"detect_remove_q08_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.3442, \\\"eval_loss_holdout\\\": 2.8533, \\\"downstream_arc_easy_acc_norm\\\": 0.6086, \\\"downstream_arc_challenge_acc_norm\\\": 0.3592, \\\"downstream_hellaswag_acc_norm\\\": 0.4855, \\\"downstream_piqa_acc_norm\\\": 0.6937, \\\"downstream_winogrande_acc\\\": 0.5817, \\\"downstream_eval_method\\\": \\\"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\\\", \\\"eval_ppl_openwebtext\\\": 18.039, \\\"eval_ppl_wikipedia\\\": 15.066}}, \\\"adaptive_1_7b_seed42_v3\\\": {}, \\\"uniform_1_7b_seed42_v3\\\": {}, \\\"detect_remove_q01_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.4, \\\"eval_ppl_openwebtext\\\": 18.22, \\\"eval_ppl_wikitext\\\": 28.22}}, \\\"detect_remove_q03_seed456\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.2509, \\\"eval_loss_holdout\\\": 2.8479, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py --max_docs 5000 --max_length 2048 (final checkpoint)\\\", \\\"train_loss\\\": 11.255, \\\"total_steps\\\": 6103, \\\"eval_ppl_openwebtext\\\": 18.03, \\\"eval_ppl_wikitext\\\": 27.61}}, \\\"detect_remove_q03_seed123\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.25, \\\"eval_loss_holdout\\\": 2.8479, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"sliding_window_stride1024_maxlen2048_fp16_5000docs\\\", \\\"total_steps\\\": 6103, \\\"train_loss_final\\\": 11.2441, \\\"train_runtime_s\\\": 13059, \\\"epoch\\\": 0.84, \\\"eval_ppl_openwebtext\\\": 18.03, \\\"eval_ppl_wikitext\\\": 27.53}}, \\\"detect_remove_q05_seed456\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.28, \\\"eval_loss_holdout\\\": 2.8493, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py --checkpoints --max_docs 5000 --max_length 2048 --stride 1024 --fp16\\\", \\\"eval_ppl_openwebtext\\\": 18.01, \\\"eval_ppl_wikitext\\\": 27.68}}, \\\"detect_remove_q05_seed123\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.27, \\\"eval_loss_holdout\\\": 2.8491, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py --checkpoints --max_docs 5000 --max_length 2048 --stride 1024 --fp16\\\", \\\"eval_ppl_openwebtext\\\": 18.01, \\\"eval_ppl_wikitext\\\": 27.75}}, \\\"detect_remove_q02_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.27, \\\"eval_loss_holdout\\\": 2.8491, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py --max_docs 5000 --max_length 2048 (final checkpoint)\\\", \\\"train_loss\\\": 11.348, \\\"train_steps\\\": 6103, \\\"data_count\\\": 91654, \\\"eval_ppl_openwebtext\\\": 18.06, \\\"eval_ppl_wikitext\\\": 27.64}}, \\\"epoch_matched_dr_seed456\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.66, \\\"eval_loss_holdout\\\": 2.8712, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py --max_docs 5000 --max_length 2048\\\", \\\"eval_ppl_openwebtext\\\": 18.27, \\\"eval_ppl_wikitext\\\": 28.14}}, \\\"epoch_matched_dr_seed123\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.66, \\\"eval_loss_holdout\\\": 2.8713, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py --max_docs 5000 --max_length 2048\\\", \\\"eval_ppl_openwebtext\\\": 18.3, \\\"eval_ppl_wikitext\\\": 27.9}}, \\\"eval_q04\\\": {\\\"metrics\\\": {\\\"loss\\\": 2.8485, \\\"perplexity\\\": 17.2626, \\\"num_tokens\\\": 4077068, \\\"elapsed_seconds\\\": 103.8, \\\"downstream_arc_easy_acc_norm\\\": 0.6107, \\\"downstream_arc_challenge_acc_norm\\\": 0.3567, \\\"downstream_hellaswag_acc_norm\\\": 0.4819, \\\"downstream_piqa_acc_norm\\\": 0.6931, \\\"downstream_winogrande_acc\\\": 0.5659, \\\"downstream_eval_method\\\": \\\"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\\\"}}, \\\"eval_q03_r2\\\": {\\\"metrics\\\": {\\\"loss\\\": 2.848, \\\"perplexity\\\": 17.2538, \\\"num_tokens\\\": 4077068, \\\"elapsed_seconds\\\": 111, \\\"downstream_arc_easy_acc_norm\\\": 0.6301, \\\"downstream_arc_challenge_acc_norm\\\": 0.3549, \\\"downstream_hellaswag_acc_norm\\\": 0.4851, \\\"downstream_piqa_acc_norm\\\": 0.6872, \\\"downstream_winogrande_acc\\\": 0.5675, \\\"downstream_eval_method\\\": \\\"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\\\"}}, \\\"eval_rho06_batch_v7\\\": {\\\"metrics\\\": {\\\"contamination_60_ess_only_seed123\\\": {\\\"loss\\\": 2.8771, \\\"perplexity\\\": 17.76, \\\"tokens\\\": 4077068}, \\\"contamination_60_ess_only_seed456\\\": {\\\"loss\\\": 2.8771, \\\"perplexity\\\": 17.76, \\\"tokens\\\": 4077068}, \\\"contamination_60_random_seed123\\\": {\\\"loss\\\": 2.8832, \\\"perplexity\\\": 17.87, \\\"tokens\\\": 4077068}, \\\"contamination_60_random_seed456\\\": {\\\"loss\\\": 2.8837, \\\"perplexity\\\": 17.88, \\\"tokens\\\": 4077068}, \\\"eval_data\\\": \\\"data/human/eval_holdout.jsonl\\\", \\\"max_docs\\\": 5000, \\\"max_length\\\": 2048}}, \\\"eval_q01_final_v2\\\": {\\\"metrics\\\": {\\\"loss\\\": 2.8563, \\\"perplexity\\\": 17.3965, \\\"num_tokens\\\": 4077068, \\\"elapsed_seconds\\\": 105.1}}, \\\"eval_q07_final\\\": {\\\"metrics\\\": {\\\"loss\\\": 2.8519, \\\"perplexity\\\": 17.3201, \\\"num_tokens\\\": 4077068, \\\"elapsed_seconds\\\": 103.8}}, \\\"eval_q06\\\": {\\\"metrics\\\": {\\\"loss\\\": 2.8507, \\\"perplexity\\\": 17.2993, \\\"num_tokens\\\": 4077068, \\\"elapsed_seconds\\\": 106.9}}, \\\"eval_epoch_matched_seed456\\\": {\\\"metrics\\\": {\\\"loss\\\": 2.8712, \\\"perplexity\\\": 17.6574, \\\"num_tokens\\\": 4077068, \\\"elapsed_seconds\\\": 103.6}}, \\\"eval_epoch_matched_seed123\\\": {\\\"metrics\\\": {\\\"loss\\\": 2.8713, \\\"perplexity\\\": 17.6599, \\\"num_tokens\\\": 4077068, \\\"elapsed_seconds\\\": 104.3}}, \\\"eval_ngram_uniform\\\": {\\\"metrics\\\": {\\\"loss\\\": 2.8733, \\\"perplexity\\\": 17.69, \\\"tokens\\\": 4077068, \\\"eval_data\\\": \\\"data/human/eval_holdout.jsonl\\\", \\\"max_docs\\\": 5000, \\\"max_length\\\": 2048, \\\"checkpoint\\\": \\\"ngram_uniform_seed42/final\\\"}}, \\\"eval_ngram_adaptive\\\": {\\\"metrics\\\": {\\\"loss\\\": 2.8803, \\\"perplexity\\\": 17.82, \\\"tokens\\\": 4077068, \\\"eval_data\\\": \\\"data/human/eval_holdout.jsonl\\\", \\\"max_docs\\\": 5000, \\\"max_length\\\": 2048, \\\"checkpoint\\\": \\\"ngram_adaptive_seed42/final\\\"}}, \\\"uniform_seed42_downstream\\\": {\\\"metrics\\\": {\\\"downstream_arc_easy_acc_norm\\\": 0.6128, \\\"downstream_arc_challenge_acc_norm\\\": 0.3481, \\\"downstream_hellaswag_acc_norm\\\": 0.4836, \\\"downstream_piqa_acc_norm\\\": 0.6877, \\\"downstream_winogrande_acc\\\": 0.5856, \\\"downstream_eval_method\\\": \\\"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\\\"}}, \\\"adaptive_fromscratch_seed42\\\": {\\\"metrics\\\": {\\\"train_loss\\\": 9.976, \\\"eval_ppl_holdout\\\": 17.689, \\\"eval_ppl_openwebtext\\\": 18.37, \\\"eval_ppl_wikipedia\\\": 15.349, \\\"downstream_arc_easy_acc_norm\\\": 0.6178, \\\"downstream_arc_challenge_acc_norm\\\": 0.3524, \\\"downstream_hellaswag_acc_norm\\\": 0.4806, \\\"downstream_piqa_acc_norm\\\": 0.6844, \\\"downstream_winogrande_acc\\\": 0.5801, \\\"downstream_eval_method\\\": \\\"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\\\", \\\"eval_method\\\": \\\"eval_ppl_ood.py (sliding window, stride=1024, max_docs=5000, fp16)\\\", \\\"training_time_s\\\": 13660}}, \\\"hybrid_rho06_seed42\\\": {\\\"metrics\\\": {\\\"eval_loss_holdout\\\": 2.8637, \\\"eval_ppl_holdout\\\": 17.526, \\\"eval_ppl_openwebtext\\\": 18.208, \\\"eval_ppl_wikipedia\\\": 15.267, \\\"downstream_arc_easy_acc_norm\\\": 0.6208, \\\"downstream_arc_challenge_acc_norm\\\": 0.3524, \\\"downstream_hellaswag_acc_norm\\\": 0.4801, \\\"downstream_piqa_acc_norm\\\": 0.6931, \\\"downstream_winogrande_acc\\\": 0.5785, \\\"eval_source\\\": \\\"rho06_tau07_seed42 eval worker - evaluated hybrid checkpoint by mistake\\\"}}, \\\"rho06_tau07_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.526, \\\"eval_ppl_openwebtext\\\": 18.208, \\\"eval_ppl_wikipedia\\\": 15.267, \\\"downstream_arc_easy_acc_norm\\\": 0.6208, \\\"downstream_arc_challenge_acc_norm\\\": 0.3524, \\\"downstream_hellaswag_acc_norm\\\": 0.4801, \\\"downstream_piqa_acc_norm\\\": 0.6931, \\\"downstream_winogrande_acc\\\": 0.5785}}, \\\"tau07_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.68, \\\"eval_ppl_openwebtext\\\": 18.348, \\\"eval_ppl_wikipedia\\\": 15.331, \\\"downstream_arc_easy_acc_norm\\\": 0.6166, \\\"downstream_arc_challenge_acc_norm\\\": 0.3473, \\\"downstream_hellaswag_acc_norm\\\": 0.4795, \\\"downstream_piqa_acc_norm\\\": 0.6861, \\\"downstream_winogrande_acc\\\": 0.5817, \\\"downstream_eval_method\\\": \\\"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\\\", \\\"eval_method\\\": \\\"eval_ppl_ood.py (sliding window, stride=1024, max_docs=5000, fp16)\\\"}}, \\\"tau07_seed456\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.677, \\\"eval_ppl_openwebtext\\\": 18.344, \\\"eval_ppl_wikipedia\\\": 15.315, \\\"downstream_arc_easy_acc_norm\\\": 0.6111, \\\"downstream_arc_challenge_acc_norm\\\": 0.3515, \\\"downstream_hellaswag_acc_norm\\\": 0.4811, \\\"downstream_piqa_acc_norm\\\": 0.6834, \\\"downstream_winogrande_acc\\\": 0.5722, \\\"downstream_eval_method\\\": \\\"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\\\", \\\"eval_method\\\": \\\"eval_ppl_ood.py (sliding window, stride=1024, max_docs=5000, fp16)\\\"}}, \\\"tau07_seed123\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.666, \\\"eval_ppl_openwebtext\\\": 18.348, \\\"eval_ppl_wikipedia\\\": 15.345, \\\"downstream_arc_easy_acc_norm\\\": 0.6309, \\\"downstream_arc_challenge_acc_norm\\\": 0.3481, \\\"downstream_hellaswag_acc_norm\\\": 0.4775, \\\"downstream_piqa_acc_norm\\\": 0.6866, \\\"downstream_winogrande_acc\\\": 0.5675, \\\"downstream_eval_method\\\": \\\"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\\\", \\\"eval_method\\\": \\\"eval_ppl_ood.py (sliding window, stride=1024, max_docs=5000, fp16)\\\"}}, \\\"tau07_downstream_eval\\\": {}, \\\"uniform_ood_seed123\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.6861, \\\"eval_ppl_openwebtext\\\": 18.3678, \\\"eval_ppl_wikipedia\\\": 15.3768, \\\"downstream_arc_easy_acc_norm\\\": 0.6229, \\\"downstream_arc_challenge_acc_norm\\\": 0.3507, \\\"downstream_hellaswag_acc_norm\\\": 0.4797, \\\"downstream_piqa_acc_norm\\\": 0.685, \\\"downstream_winogrande_acc\\\": 0.5762, \\\"downstream_eval_method\\\": \\\"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\\\"}}, \\\"adaptive_ood_seed456\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.683, \\\"eval_ppl_openwebtext\\\": 18.366, \\\"eval_ppl_wikipedia\\\": 15.345, \\\"downstream_arc_easy_acc_norm\\\": 0.6077, \\\"downstream_arc_challenge_acc_norm\\\": 0.3541, \\\"downstream_hellaswag_acc_norm\\\": 0.48, \\\"downstream_piqa_acc_norm\\\": 0.6806, \\\"downstream_winogrande_acc\\\": 0.5714, \\\"downstream_eval_method\\\": \\\"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\\\"}}, \\\"adaptive_ood_seed123\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.677, \\\"eval_ppl_openwebtext\\\": 18.373, \\\"eval_ppl_wikipedia\\\": 15.37, \\\"downstream_arc_easy_acc_norm\\\": 0.6301, \\\"downstream_arc_challenge_acc_norm\\\": 0.3481, \\\"downstream_hellaswag_acc_norm\\\": 0.4791, \\\"downstream_piqa_acc_norm\\\": 0.6844, \\\"downstream_winogrande_acc\\\": 0.5706, \\\"downstream_eval_method\\\": \\\"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\\\"}}, \\\"uniform_ood_seed456\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.7015, \\\"eval_ppl_openwebtext\\\": 18.3865, \\\"eval_ppl_wikipedia\\\": 15.3594, \\\"downstream_arc_easy_acc_norm\\\": 0.6166, \\\"downstream_arc_challenge_acc_norm\\\": 0.3439, \\\"downstream_hellaswag_acc_norm\\\": 0.4826, \\\"downstream_piqa_acc_norm\\\": 0.6795, \\\"downstream_winogrande_acc\\\": 0.5667, \\\"downstream_eval_method\\\": \\\"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\\\"}}, \\\"w2_distribution_matching_eval\\\": {}, \\\"uniform_1_7b_seed123\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 13.2648, \\\"eval_loss_holdout\\\": 2.5851, \\\"train_loss_final\\\": 7.557, \\\"total_steps\\\": 6103, \\\"num_eval_tokens\\\": 4077068}}, \\\"detect_remove_q07_epoch_matched_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.62, \\\"eval_loss_holdout\\\": 2.8689, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"sliding_window_stride1024_maxlen2048_fp16_5000docs\\\", \\\"total_steps\\\": 3047}}, \\\"detect_remove_q09_epoch_matched_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.628, \\\"eval_loss_holdout\\\": 2.8695, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"sliding_window_stride1024_maxlen2048_fp16_5000docs\\\", \\\"total_steps\\\": 3770, \\\"train_loss_final\\\": 9.9127}}, \\\"adaptive_1_7b_seed123\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 13.25, \\\"eval_loss_holdout\\\": 2.5843}}, \\\"detect_remove_q01_epoch_matched_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 18.0436, \\\"eval_loss_holdout\\\": 2.8928, \\\"eval_holdout_tokens\\\": 4077068}}, \\\"ngram_adaptive_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.82, \\\"eval_loss_holdout\\\": 2.8803}}, \\\"ngram_uniform_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.69, \\\"eval_loss_holdout\\\": 2.8733}}, \\\"detect_remove_q03_epoch_matched_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.74, \\\"eval_loss_holdout\\\": 2.876, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"sliding_window_stride1024_maxlen2048_fp16_5000docs\\\", \\\"total_steps\\\": 1927, \\\"train_loss_final\\\": 11.3917, \\\"interpretation\\\": \\\"PPL 17.74 vs epoch-matched q05 (17.65): q03 stricter filtering yields HIGHER PPL (+0.09) under matched training budget, not lower. This contradicts the hypothesis that stricter filtering improves data quality per-token. Meanwhile multi-epoch q03 (17.25) is much lower, confirming that the PPL advantage of q03 in multi-epoch setting comes from more training epochs on filtered data, not from higher per-token quality. Conclusion: under fixed training budget, stricter filtering (q03) actually hurts slightly compared to moderate filtering (q05), likely because removing too many borderline samples reduces diversity without sufficient quality gain.\\\"}}, \\\"gpt2_adaptive_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.79, \\\"eval_loss_holdout\\\": 2.879, \\\"train_loss\\\": 10.58, \\\"train_steps\\\": 6103, \\\"train_runtime_hours\\\": 3.92}}, \\\"gpt2_uniform_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.69, \\\"eval_loss_holdout\\\": 2.8733, \\\"train_loss\\\": 7.989, \\\"train_steps\\\": 6103, \\\"train_runtime_hours\\\": 3.54}}, \\\"eval_uniform_1_7b_v3\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 13.5}}, \\\"eval_adaptive_1_7b_v2\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 13.27}}, \\\"detect_remove_q06_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.3, \\\"eval_loss_holdout\\\": 2.8507}}, \\\"adaptive_1_7b_seed42\\\": {}, \\\"detect_remove_q07_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.32, \\\"eval_loss_holdout\\\": 2.8519, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py --max_docs 5000 --max_length 2048 (final checkpoint)\\\", \\\"note\\\": \\\"final checkpoint, replaces partial ckpt-3500 PPL=17.49\\\"}}, \\\"ess_only_seed456\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.76, \\\"eval_loss_holdout\\\": 2.877, \\\"eval_holdout_tokens\\\": 4077068, \\\"train_loss\\\": 1.9364, \\\"note\\\": \\\"re-eval on westd-41312 latest run (v2)\\\"}}, \\\"random_reweight_seed456\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.777, \\\"eval_loss_holdout\\\": 2.8779, \\\"eval_holdout_tokens\\\": 4077068, \\\"total_steps\\\": 6103, \\\"train_loss\\\": 6.657, \\\"train_runtime_seconds\\\": 10739}}, \\\"ess_only_seed123\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.72, \\\"eval_loss_holdout\\\": 2.8746, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py on data/human/eval_holdout.jsonl, max_docs=5000, stride=1024, fp16\\\", \\\"eval_note\\\": \\\"Also ran on scored_data.jsonl (train data): ppl=9.66, loss=2.2677, tokens=3029693\\\", \\\"train_loss\\\": 10.2159, \\\"train_steps\\\": 6103, \\\"train_runtime_seconds\\\": 12959.5, \\\"b_star_mean\\\": 3.55, \\\"b_star_median\\\": 1.5918, \\\"b_star_std\\\": 4.7209, \\\"b_star_min\\\": 0.2344, \\\"b_star_max\\\": 20, \\\"b_star_p25\\\": 0.8398, \\\"b_star_p75\\\": 3.8281, \\\"b_star_p90\\\": 9.5996, \\\"b_star_count\\\": 21971, \\\"vs_uniform_ppl_delta\\\": \\\"+0.034\\\", \\\"vs_adaptive_fix_ppl_delta\\\": \\\"+0.077\\\"}}, \\\"detect_remove_q03_seed42\\\": {}, \\\"uniform_1_7b_seed42\\\": {}, \\\"detect_remove_q09_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.42, \\\"eval_loss_holdout\\\": 2.8577, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py --checkpoints --max_docs 5000 --max_length 2048 --stride 1024 --fp16\\\"}}, \\\"contamination_60_ess_only_seed456\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.762, \\\"eval_loss_holdout\\\": 2.8771, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py --checkpoints --max_docs 5000 --max_length 2048\\\"}}, \\\"contamination_60_ess_only_seed123\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.763, \\\"eval_loss_holdout\\\": 2.8771, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py --checkpoints --max_docs 5000 --max_length 2048\\\"}}, \\\"ess_only_seed456_r2\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.762, \\\"eval_loss_holdout\\\": 2.877, \\\"eval_holdout_tokens\\\": 4077068, \\\"total_steps\\\": 6103, \\\"train_loss\\\": 5.998, \\\"train_runtime_seconds\\\": 7611}}, \\\"ess_only_seed123_r2\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.721, \\\"eval_loss_holdout\\\": 2.8747, \\\"eval_holdout_tokens\\\": 4077068, \\\"total_steps\\\": 6103, \\\"train_loss\\\": 6.86, \\\"train_runtime_seconds\\\": 8674}}, \\\"detect_remove_q05_epoch_matched_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.65, \\\"eval_loss_holdout\\\": 2.8707, \\\"eval_holdout_tokens\\\": 4077068, \\\"train_loss_final\\\": 3.184, \\\"total_steps\\\": 2533, \\\"eval_method\\\": \\\"eval_perplexity.py --max_docs 5000 --max_length 2048 --stride 1024 --fp16\\\", \\\"vs_full_dr_q05\\\": \\\"+0.360 (17.650 vs 17.290, epoch-matched worse)\\\", \\\"vs_adaptive\\\": \\\"-0.001 (17.650 vs 17.651, nearly identical to adaptive)\\\", \\\"interpretation\\\": \\\"D&R 0.36 PPL advantage over epoch-matched is entirely from multi-epoch training on clean data, not from data quality filtering\\\"}}, \\\"contamination_60_random_seed123\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.87, \\\"eval_loss_holdout\\\": 2.8832, \\\"eval_holdout_tokens\\\": 4077068}}, \\\"contamination_60_random_seed456\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.88, \\\"eval_loss_holdout\\\": 2.8837, \\\"eval_holdout_tokens\\\": 4077068}}, \\\"contamination_60_grid_b0_3_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.634, \\\"eval_method\\\": \\\"eval_perplexity.py --max_docs 5000 --max_length 2048 --stride 1024 --fp16\\\", \\\"checkpoint_1500_ppl\\\": 18.583, \\\"total_steps\\\": 6103, \\\"note\\\": \\\"resume from checkpoint-1500 with ~30% LR offset; final PPL improved over checkpoint-1500, no degradation\\\"}}, \\\"contamination_60_random_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.832, \\\"eval_method\\\": \\\"eval_perplexity.py --max_docs 5000 --max_length 2048 --stride 1024 --fp16\\\", \\\"total_steps\\\": 6103, \\\"note\\\": \\\"resume from checkpoint-1000; cron falsely marked failed due to log path mismatch\\\"}}, \\\"grid_b0_2_seed456\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.645, \\\"eval_loss_holdout\\\": 2.87, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py --max_docs 5000 --max_length 2048 --stride 1024 --fp16\\\", \\\"eval_checkpoint\\\": \\\"checkpoint-5500\\\", \\\"note\\\": \\\"eval at checkpoint-5500; final checkpoint degraded due to --save_only_model LR reset on resume\\\"}}, \\\"grid_b0_2_seed123\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.637, \\\"eval_loss_holdout\\\": 2.87, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py --max_docs 5000 --max_length 2048 --stride 1024 --fp16\\\", \\\"eval_checkpoint\\\": \\\"checkpoint-5500\\\", \\\"note\\\": \\\"eval at checkpoint-5500; final checkpoint degraded due to --save_only_model LR reset on resume\\\"}}, \\\"contamination_60_adaptive_seed456\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.735, \\\"eval_loss_holdout\\\": 2.8755, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py --max_docs 5000 --stride 1024 --fp16\\\"}}, \\\"contamination_60_uniform_seed456\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.77, \\\"eval_loss_holdout\\\": 2.8775, \\\"eval_holdout_tokens\\\": 4077068, \\\"train_loss\\\": 7.637, \\\"train_runtime_seconds\\\": 12845, \\\"total_steps\\\": 6103, \\\"eval_method\\\": \\\"eval_perplexity.py --max_docs 5000 --max_length 2048\\\"}}, \\\"grid_b0_1_seed123\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.646, \\\"eval_loss_holdout\\\": 2.8705, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py --max_docs 5000 --max_length 2048 --fp16\\\"}}, \\\"grid_b0_1_seed456\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.663, \\\"eval_loss_holdout\\\": 2.8715, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py --max_docs 5000 --max_length 2048 --fp16\\\"}}, \\\"contamination_60_ess_only_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.77, \\\"eval_loss_holdout\\\": 2.8775, \\\"eval_holdout_tokens\\\": 4077068, \\\"train_loss\\\": 9.842, \\\"total_steps\\\": 6103, \\\"train_runtime_seconds\\\": 13152}}, \\\"contamination_60_uniform_seed123\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.754, \\\"eval_loss_holdout\\\": 2.8766, \\\"eval_holdout_tokens\\\": 4077068, \\\"total_steps\\\": 6103, \\\"eval_method\\\": \\\"eval_perplexity.py --max_docs 5000 --max_length 2048\\\"}}, \\\"contamination_60_seed123\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.732, \\\"eval_loss_holdout\\\": 2.8754, \\\"eval_holdout_tokens\\\": 4077068, \\\"train_loss\\\": 9.6302, \\\"train_runtime_seconds\\\": 13638.6, \\\"total_steps\\\": 6103, \\\"eval_method\\\": \\\"eval_perplexity.py --max_docs 5000 --max_length 2048\\\"}}, \\\"grid_b0_3_seed123_r2\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.5792, \\\"eval_loss_holdout\\\": 2.8667, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\\\", \\\"re_eval_date\\\": \\\"2026-05-18\\\", \\\"eval_results_path\\\": \\\"/root/autodl-tmp/output/models/grid_b0_3_seed123/eval_results.json\\\", \\\"re_eval_note\\\": \\\"re-eval confirms original PPL=17.58; JSON artifact now saved\\\"}}, \\\"grid_b0_3_seed456_r2\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.64, \\\"eval_loss_holdout\\\": 2.87, \\\"eval_holdout_tokens\\\": 4077068, \\\"total_steps\\\": 6103, \\\"train_loss\\\": 9.085, \\\"vs_uniform\\\": \\\"-0.054 (17.64 vs 17.694)\\\", \\\"vs_grid_b03_seed42\\\": \\\"0.000 (17.64 vs 17.640)\\\", \\\"vs_grid_b05_seed456\\\": \\\"-0.01 (17.64 vs 17.65)\\\"}}, \\\"batchsize16_nmin8_r3\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.65, \\\"eval_loss_holdout\\\": 2.871, \\\"eval_holdout_tokens\\\": 4077068, \\\"total_steps\\\": 6103, \\\"train_loss\\\": 2.6308, \\\"train_runtime_seconds\\\": 15057, \\\"vs_adaptive_bs4\\\": \\\"-0.003 (17.65 vs 17.6527)\\\", \\\"vs_bs8_nmin4\\\": \\\"-0.01 (17.65 vs 17.66)\\\", \\\"batch_size\\\": 16, \\\"n_min\\\": 8}}, \\\"rho02_adaptive_tau08_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.382, \\\"eval_loss_holdout\\\": 2.8555, \\\"eval_holdout_tokens\\\": 4077068, \\\"total_steps\\\": 6103, \\\"train_runtime_seconds\\\": 14599, \\\"vs_rho02_uniform\\\": \\\"+0.046 (17.382 vs 17.336)\\\", \\\"vs_rho04_uniform\\\": \\\"-0.312 (17.382 vs 17.694)\\\", \\\"tau\\\": 0.8, \\\"rho\\\": 0.2, \\\"b_star_pct_zero\\\": \\\"40-50%\\\", \\\"conclusion_note\\\": \\\"worse than same-rho uniform baseline\\\"}}, \\\"batchsize16_nmin8_r2\\\": {}, \\\"grid_b0_3_seed456\\\": {}, \\\"batch_adaptive_tau_rho06_r5\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.73, \\\"eval_loss_holdout\\\": 2.8754, \\\"eval_holdout_tokens\\\": 4077068, \\\"train_loss\\\": 9.267, \\\"train_runtime_seconds\\\": 13903, \\\"total_steps\\\": 6103, \\\"vs_uniform_rho06\\\": \\\"-0.036\\\", \\\"vs_adaptive_fixed_tau08_rho06\\\": \\\"-0.010\\\", \\\"vs_grid_best_rho06\\\": \\\"+0.026\\\", \\\"vs_hybrid_rho06\\\": \\\"+0.200\\\"}}, \\\"random_reweight_seed123_r5\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.8, \\\"eval_loss_holdout\\\": 2.8793, \\\"eval_holdout_tokens\\\": 4077068, \\\"train_loss\\\": 8.0176, \\\"train_runtime_seconds\\\": 13267, \\\"total_steps\\\": 6103, \\\"vs_uniform_seed123\\\": \\\"+0.114\\\", \\\"vs_adaptive_fix_seed123\\\": \\\"+0.157\\\", \\\"vs_random_reweight_v2_seed42\\\": \\\"consistent (+0.136 seed42 vs +0.114 seed123)\\\"}}, \\\"rho02_adaptive_tau09_r5\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.45, \\\"eval_loss_holdout\\\": 2.8593, \\\"eval_holdout_tokens\\\": 4077068, \\\"train_loss\\\": 11.864, \\\"epoch\\\": 0.47, \\\"b_star_mean\\\": 4.3493, \\\"b_star_median\\\": 2.9609, \\\"b_star_std\\\": 4.3982, \\\"b_star_min\\\": 0, \\\"b_star_max\\\": 20, \\\"b_star_pct_zero\\\": 2.65, \\\"alpha_eff_mean\\\": 0.8277, \\\"alpha_eff_median\\\": 0.8826, \\\"alpha_eff_pct_at_max\\\": 42.95, \\\"ess_mean\\\": 2.3784, \\\"ess_median\\\": 2.0121}}, \\\"bs8_auto_nmin_r5\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.66, \\\"eval_loss_holdout\\\": 2.8716, \\\"eval_holdout_tokens\\\": 4077068, \\\"train_loss\\\": 5.163, \\\"total_steps\\\": 6103, \\\"train_runtime_seconds\\\": 14064, \\\"epoch\\\": 0.26, \\\"b_star_mean\\\": 1.0957, \\\"b_star_median\\\": 0.9, \\\"b_star_std\\\": 0.7563, \\\"b_star_pct_zero\\\": 0.11, \\\"b_star_pct_below_0.5\\\": 10.43, \\\"ess_mean\\\": 4.4925, \\\"ess_median\\\": 4.0446, \\\"alpha_eff_mean\\\": 0.7023, \\\"alpha_eff_median\\\": 0.7572, \\\"alpha_eff_pct_at_max\\\": 38.88}}, \\\"grid_b0_1_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.657, \\\"eval_loss_holdout\\\": 2.871}}, \\\"llama3b_adaptive_seed42\\\": {\\\"metrics\\\": {\\\"ppl\\\": 10.58, \\\"eval_loss\\\": 2.359, \\\"eval_tokens\\\": 4017316}}, \\\"batchsize16_nmin8_seed42\\\": {}, \\\"llama3b_uniform_seed42\\\": {\\\"metrics\\\": {\\\"ppl\\\": 10.38, \\\"eval_loss\\\": 2.3397, \\\"eval_tokens\\\": 1526195, \\\"train_loss\\\": 7.2987, \\\"train_steps\\\": 6103, \\\"train_runtime_seconds\\\": 94309}}, \\\"random_reweight_seed123_r4\\\": {}, \\\"rho02_adaptive_tau09_r4\\\": {}, \\\"random_reweight_seed123_r3\\\": {}, \\\"grid_b0_2_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.64, \\\"eval_loss_holdout\\\": 2.8704, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\\\"}}, \\\"rho02_adaptive_tau09_r3\\\": {}, \\\"batch_adaptive_tau_rho06_r3\\\": {}, \\\"bs8_auto_nmin_r3\\\": {}, \\\"random_reweight_seed123_r2\\\": {}, \\\"rho02_adaptive_tau09_r2\\\": {\\\"metrics\\\": {\\\"error\\\": \\\"TypeError: Trainer.__init__() got an unexpected keyword argument 'tokenizer'\\\", \\\"error_stage\\\": \\\"initialization\\\", \\\"training_completed\\\": false, \\\"note\\\": \\\"Crashed before any training. Same bug as rho02_adaptive_tau09_seed42. Fix: replace tokenizer= with processing_class= in pretrain_weighted.py line ~101.\\\"}}, \\\"random_reweight_seed123\\\": {}, \\\"batch_adaptive_tau_rho06_r2\\\": {}, \\\"bs8_auto_nmin_r2\\\": {}, \\\"rho02_adaptive_tau09_seed42\\\": {}, \\\"batch_adaptive_tau_rho06_seed42\\\": {}, \\\"bs8_auto_nmin_seed42\\\": {}, \\\"grid_b0_3_seed123\\\": {}, \\\"random_reweight_v2_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.83, \\\"eval_loss_holdout\\\": 2.8809}}, \\\"tau_095_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.723, \\\"eval_loss\\\": 2.8749, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\\\", \\\"train_loss\\\": 10.198, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 13699, \\\"train_samples_per_second\\\": 7.128, \\\"b_star_count\\\": 24412, \\\"b_star_mean\\\": 3.0775, \\\"b_star_median\\\": 1.52, \\\"b_star_std\\\": 3.9923, \\\"b_star_min\\\": 0, \\\"b_star_max\\\": 20, \\\"b_star_p25\\\": 0.8, \\\"b_star_p75\\\": 3.46, \\\"b_star_pct_zero\\\": 0, \\\"b_star_pct_below_0.5\\\": 8.5, \\\"b_star_pct_0.5_to_1\\\": 24.7, \\\"b_star_pct_1_to_2\\\": 26.4, \\\"b_star_pct_above_2\\\": 40.3}}, \\\"batch_adaptive_tau_rho04_seed42\\\": {\\\"metrics\\\": {\\\"eval_loss_holdout\\\": 2.8725, \\\"eval_ppl_holdout\\\": 17.681, \\\"train_loss\\\": 9.8206, \\\"train_runtime_sec\\\": 45402.86}}, \\\"p0_contamination_60_datagen\\\": {\\\"metrics\\\": {\\\"total_lines\\\": 371499, \\\"synthetic_count\\\": 222900, \\\"human_count\\\": 148599, \\\"actual_contamination_ratio\\\": 0.6, \\\"q_score_mean\\\": 0.6243, \\\"q_score_std\\\": 0.3703, \\\"q_score_median\\\": 0.7753, \\\"file_size_mb\\\": 907}}, \\\"datagen_synthetic_4gpu\\\": {}, \\\"grid_b5_0_seed123\\\": {\\\"metrics\\\": {\\\"train_loss\\\": 10.8468, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 14434, \\\"gpu_hours\\\": 4.01, \\\"eval_ppl_holdout\\\": 17.8039, \\\"eval_loss\\\": 2.8794, \\\"eval_holdout_tokens\\\": 4077068}}, \\\"grid_b3_0_seed123\\\": {\\\"metrics\\\": {\\\"train_loss\\\": 10.7422, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 12955.83, \\\"gpu_hours\\\": 3.6, \\\"eval_ppl_holdout\\\": 17.76, \\\"eval_loss\\\": 2.877, \\\"eval_holdout_tokens\\\": 4077068}}, \\\"grid_b2_0_seed123\\\": {\\\"metrics\\\": {\\\"train_loss\\\": 10.61, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 13058.8, \\\"gpu_hours\\\": 3.63, \\\"train_samples_per_second\\\": 7.478, \\\"train_steps_per_second\\\": 0.467, \\\"eval_ppl_holdout\\\": 17.725, \\\"eval_loss\\\": 2.875, \\\"eval_holdout_tokens\\\": 4077068}}, \\\"grid_b1_5_seed123\\\": {\\\"metrics\\\": {\\\"train_loss\\\": 10.4776, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 15053.1, \\\"gpu_hours\\\": 4.18, \\\"eval_ppl_holdout\\\": 17.701, \\\"eval_loss\\\": 2.8736}}, \\\"grid_b1_0_seed123\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.674, \\\"eval_loss\\\": 2.8721, \\\"eval_holdout_tokens\\\": 4077068, \\\"train_loss\\\": 10.218, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 13878, \\\"gpu_hours\\\": 3.88}}, \\\"grid_b0_5_seed123\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.638, \\\"eval_loss\\\": 2.87, \\\"eval_holdout_tokens\\\": 4077068, \\\"train_loss\\\": 9.601, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 13104, \\\"gpu_hours\\\": 3.8}}, \\\"hybrid_rho04_seed42\\\": {\\\"metrics\\\": {\\\"eval_loss_holdout\\\": 2.863, \\\"eval_ppl_holdout\\\": 17.514}}, \\\"threshold_q03_seed42\\\": {\\\"metrics\\\": {\\\"eval_loss_holdout\\\": 2.848, \\\"eval_ppl_holdout\\\": 17.253}}, \\\"rho02_uniform_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.336, \\\"eval_loss_holdout\\\": 2.853, \\\"eval_holdout_tokens\\\": 4077068}}, \\\"threshold_q07_seed42\\\": {}, \\\"random_reweight_seed42\\\": {}, \\\"contamination_60_tau06_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.7359, \\\"eval_loss_holdout\\\": 2.8756, \\\"eval_holdout_tokens\\\": 4077068, \\\"train_loss\\\": 8.9804, \\\"train_runtime_seconds\\\": 13367.3, \\\"train_samples_per_second\\\": 7.305, \\\"total_steps\\\": 6103, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\"}}, \\\"contamination_60_tau07_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.73, \\\"eval_loss_holdout\\\": 2.875, \\\"eval_holdout_tokens\\\": 4077068, \\\"train_loss\\\": 9.358, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\"}}, \\\"detect_remove_baseline_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.29, \\\"eval_loss_holdout\\\": 2.8499, \\\"eval_holdout_tokens\\\": 4077068, \\\"train_loss\\\": 11.003, \\\"train_runtime_seconds\\\": 13248, \\\"total_steps\\\": 6103, \\\"train_samples_per_second\\\": 7.371}}, \\\"grid_b0_3_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.64, \\\"eval_loss_holdout\\\": 2.8702, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\", \\\"train_loss\\\": 9.1154, \\\"train_runtime_seconds\\\": 13365.79, \\\"train_samples_per_second\\\": 7.306, \\\"total_steps\\\": 6103, \\\"b_fixed\\\": 0.3, \\\"alpha_eff_typical_range\\\": \\\"0.07-0.88\\\", \\\"ess_typical_range\\\": \\\"2.3-4.0\\\"}}, \\\"tau_095_nmin2_seed42\\\": {}, \\\"tau_09_nmin2_seed42\\\": {}, \\\"nmin5_seed42\\\": {}, \\\"grid_b5_0_seed456\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.993, \\\"eval_loss\\\": 2.89, \\\"eval_holdout_tokens\\\": 4077068, \\\"train_loss\\\": 5.488, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 6601, \\\"gpu_hours\\\": 1.83, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\"}}, \\\"grid_b3_0_seed456\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.921, \\\"eval_loss\\\": 2.886, \\\"eval_holdout_tokens\\\": 4077068, \\\"train_loss\\\": 5.435, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 6602, \\\"gpu_hours\\\": 1.83, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\"}}, \\\"grid_b2_0_seed456\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.989, \\\"eval_loss\\\": 2.8898, \\\"eval_holdout_tokens\\\": 4077068, \\\"train_loss\\\": 10.625, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 12969, \\\"gpu_hours\\\": 3.6, \\\"train_samples_per_second\\\": 7.53, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\"}}, \\\"ess_only_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl\\\": 17.73, \\\"eval_loss\\\": 2.875, \\\"b_star_median\\\": 1.58, \\\"b_star_mean\\\": 3.51, \\\"vs_uniform_ppl_delta\\\": \\\"+0.038\\\", \\\"vs_adaptive_ppl_delta\\\": \\\"+0.08\\\"}}, \\\"adaptive_fix_seed123\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.6432, \\\"eval_loss_holdout\\\": 2.8704, \\\"eval_loss\\\": 2.8704, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\", \\\"eval_note\\\": \\\"unified post-hoc eval 2026-05-15; was 17.643/4077068\\\", \\\"train_loss_weighted\\\": 7.517, \\\"train_runtime_s\\\": 10347, \\\"total_steps\\\": 6103, \\\"epoch\\\": 0.26, \\\"b_star_mean\\\": 1.431, \\\"b_star_median\\\": 0.88, \\\"b_star_std\\\": 2.029, \\\"b_star_min\\\": 0, \\\"b_star_max\\\": 20, \\\"b_star_pct_below_0.5\\\": 20.9, \\\"b_star_pct_0.5_to_1\\\": 35.7, \\\"b_star_pct_1_to_2\\\": 27.3, \\\"b_star_pct_2_to_5\\\": 6.3, \\\"b_star_pct_above_5\\\": 1.9, \\\"b_star_count\\\": 25906, \\\"b_star_p25\\\": 0.54, \\\"b_star_p75\\\": 1.52, \\\"b_star_pct_above_2\\\": 16.1, \\\"b_star_note\\\": \\\"Training-only records (eval checkpoint records with b*=0 excluded)\\\"}}, \\\"adaptive_fix_seed456\\\": {\\\"metrics\\\": {\\\"train_loss\\\": 8.3124, \\\"train_runtime\\\": 11436.05, \\\"train_samples_per_second\\\": 8.539, \\\"train_steps_per_second\\\": 0.534, \\\"total_steps\\\": 6103, \\\"eval_ppl_holdout\\\": 17.6566, \\\"eval_loss_holdout\\\": 2.8711, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\", \\\"eval_note\\\": \\\"unified post-hoc eval 2026-05-15; was 17.66/4077068\\\", \\\"b_star_count\\\": 26396, \\\"b_star_mean\\\": 1.416, \\\"b_star_median\\\": 0.88, \\\"b_star_std\\\": 1.993, \\\"b_star_min\\\": 0, \\\"b_star_max\\\": 20, \\\"b_star_p25\\\": 0.54, \\\"b_star_p75\\\": 1.52, \\\"b_star_pct_below_0.5\\\": 20.9, \\\"b_star_pct_0.5_to_1\\\": 35.7, \\\"b_star_pct_1_to_2\\\": 27.3, \\\"b_star_pct_above_2\\\": 16.1, \\\"b_star_note\\\": \\\"Training-only records (eval checkpoint records with b*=0 excluded)\\\"}}, \\\"adaptive_v2_seed456\\\": {}, \\\"adaptive_v2_seed123\\\": {}, \\\"adaptive_v2_seed42\\\": {}, \\\"tau_07_nmin2_seed42\\\": {}, \\\"tau_06_nmin2_seed42\\\": {}, \\\"tau_05_nmin2_seed42\\\": {}, \\\"contamination_60_seed42_r2\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.74, \\\"eval_loss_holdout\\\": 2.8759, \\\"eval_tokens\\\": 4077068, \\\"eval_method\\\": \\\"sliding_window_2048_stride1024\\\", \\\"train_loss\\\": 9.6349, \\\"train_runtime_seconds\\\": 14092.25}}, \\\"contamination_60_grid_b0_5_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl\\\": 17.704, \\\"eval_loss\\\": 2.8738, \\\"eval_tokens\\\": 4077068, \\\"eval_docs\\\": 5000}}, \\\"contamination_60_uniform_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.766, \\\"eval_loss_holdout\\\": 2.8773, \\\"eval_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py sliding-window (stride=1024, max_length=2048, fp16) on data/human/eval_holdout.jsonl\\\", \\\"train_loss\\\": 7.649, \\\"train_runtime_seconds\\\": 12904}}, \\\"bs8_nmin2_seed42_r2\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.73, \\\"eval_loss_holdout\\\": 2.8752, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py on data/human/eval_holdout.jsonl, max_docs=5000, stride=1024, fp16\\\", \\\"train_loss\\\": 5.4065, \\\"train_steps\\\": 6103, \\\"train_runtime_seconds\\\": 14621.6}}, \\\"grid_b_low_serial_seed42\\\": {}, \\\"grid_b_low_seed42_r3\\\": {}, \\\"grid_b_low_seed42_r2\\\": {}, \\\"baseline_qwen3_0.6b\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 22.97, \\\"eval_loss\\\": 3.134, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"sliding_window_stride1024_maxlen2048_fp16\\\"}}, \\\"contamination_60_seed42\\\": {}, \\\"nmin4_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.6947, \\\"eval_loss\\\": 2.8733, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\\\", \\\"train_loss\\\": 7.989, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 16231, \\\"train_samples_per_second\\\": 6.016, \\\"b_star_count\\\": 24412, \\\"b_star_mean\\\": 0, \\\"b_star_median\\\": 0, \\\"b_star_std\\\": 0, \\\"b_star_min\\\": 0, \\\"b_star_max\\\": 0, \\\"b_star_pct_zero\\\": 100, \\\"ess_mean\\\": 4, \\\"ess_min\\\": 4, \\\"ess_max\\\": 4}}, \\\"bs8_nmin2_seed42\\\": {}, \\\"bs8_seed42\\\": {}, \\\"tau_09_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.712, \\\"eval_loss\\\": 2.8742, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\\\", \\\"eval_note\\\": \\\"unified post-hoc eval 2026-05-15\\\", \\\"b_star_count\\\": 24412, \\\"b_star_mean\\\": 2.36, \\\"b_star_median\\\": 1.32, \\\"b_star_std\\\": 3.04, \\\"b_star_pct_above_2\\\": 33.7}}, \\\"tau_07_seed42\\\": {\\\"metrics\\\": {\\\"train_loss\\\": 9.6707, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 15065, \\\"train_samples_per_second\\\": 6.482, \\\"eval_ppl_holdout\\\": 17.6793, \\\"eval_loss\\\": 2.8724, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\\\", \\\"eval_note\\\": \\\"unified post-hoc eval 2026-05-15\\\", \\\"b_star_count\\\": 24412, \\\"b_star_mean\\\": 0.8943, \\\"b_star_median\\\": 0.58, \\\"b_star_std\\\": 1.4007, \\\"b_star_min\\\": 0, \\\"b_star_max\\\": 20, \\\"b_star_p25\\\": 0.3306, \\\"b_star_p75\\\": 0.9712, \\\"b_star_pct_zero\\\": 5.8, \\\"b_star_pct_below_0.5\\\": 36, \\\"b_star_pct_0.5_to_1\\\": 34.2, \\\"b_star_pct_1_to_2\\\": 16.2, \\\"b_star_pct_above_2\\\": 7.7}}, \\\"tau_06_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.6805, \\\"eval_loss\\\": 2.8725, \\\"train_loss\\\": 9.275, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 13436.64, \\\"train_samples_per_second\\\": 7.267, \\\"b_star_mean\\\": 0.5899, \\\"b_star_median\\\": 0.3746, \\\"b_star_std\\\": 1.0693, \\\"b_star_min\\\": 0, \\\"b_star_max\\\": 20, \\\"b_star_p25\\\": 0.1195, \\\"b_star_p75\\\": 0.66, \\\"b_star_zero_frac\\\": 0.156, \\\"b_star_nonzero_mean\\\": 0.699, \\\"b_star_nonzero_median\\\": 0.4473}}, \\\"tau_05_seed42\\\": {\\\"metrics\\\": {\\\"train_loss\\\": 8.849, \\\"total_steps\\\": 6103, \\\"epoch\\\": 0.26, \\\"train_runtime_s\\\": 13431.4, \\\"train_samples_per_second\\\": 7.27, \\\"eval_ppl_holdout\\\": 17.688, \\\"eval_loss\\\": 2.8729, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\\\", \\\"eval_note\\\": \\\"unified post-hoc eval 2026-05-15\\\", \\\"b_star_count\\\": 24412, \\\"b_star_mean\\\": 0.3923, \\\"b_star_median\\\": 0.1707, \\\"b_star_std\\\": 0.8821, \\\"b_star_min\\\": 0, \\\"b_star_max\\\": 20, \\\"b_star_p25\\\": 0, \\\"b_star_p75\\\": 0.4366, \\\"b_star_pct_zero\\\": 29.1, \\\"b_star_pct_below_0.5\\\": 78.4, \\\"b_star_pct_0.5_to_1\\\": 12.9, \\\"b_star_pct_1_to_2\\\": 5.7, \\\"b_star_pct_above_2\\\": 2.9}}, \\\"adaptive_seed456\\\": {\\\"metrics\\\": {\\\"train_loss\\\": 9.2354, \\\"train_runtime_s\\\": 13130.09, \\\"total_steps\\\": 6103, \\\"train_samples_per_second\\\": 7.437, \\\"train_steps_per_second\\\": 0.465, \\\"epoch\\\": 0.26, \\\"weighting_method\\\": \\\"adaptive\\\", \\\"tau\\\": 0.8, \\\"n_min\\\": 3, \\\"contamination_ratio\\\": 0.4, \\\"b_star\\\": \\\"per-batch adaptive (0.0-3.8)\\\", \\\"alpha_eff_range\\\": \\\"0.09-0.80 (capped at tau)\\\", \\\"eval_ppl_holdout\\\": 17.6419, \\\"eval_loss_holdout\\\": 2.8703, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\", \\\"eval_note\\\": \\\"unified post-hoc eval 2026-05-15; was 17.64/4080000 from inline eval\\\"}}, \\\"adaptive_seed123\\\": {\\\"metrics\\\": {\\\"train_loss\\\": 9.2665, \\\"train_runtime_s\\\": 13197.18, \\\"total_steps\\\": 6103, \\\"train_samples_per_second\\\": 7.399, \\\"train_steps_per_second\\\": 0.462, \\\"epoch\\\": 0.26, \\\"weighting_method\\\": \\\"adaptive\\\", \\\"tau\\\": 0.8, \\\"n_min\\\": 3, \\\"contamination_ratio\\\": 0.4, \\\"b_star\\\": \\\"per-batch adaptive (0.0-3.8)\\\", \\\"alpha_eff_range\\\": \\\"0.04-0.80 (capped at tau)\\\", \\\"eval_ppl_holdout\\\": 17.6308, \\\"eval_loss_holdout\\\": 2.8696, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\", \\\"eval_note\\\": \\\"unified post-hoc eval 2026-05-15; was 17.63/4080000 from inline eval\\\"}}, \\\"adaptive_seed42\\\": {\\\"metrics\\\": {\\\"train_loss\\\": 9.2665, \\\"train_runtime_s\\\": 13115.09, \\\"total_steps\\\": 6103, \\\"train_samples_per_second\\\": 7.445, \\\"train_steps_per_second\\\": 0.465, \\\"epoch\\\": 0.26, \\\"weighting_method\\\": \\\"adaptive\\\", \\\"tau\\\": 0.8, \\\"n_min\\\": 3, \\\"contamination_ratio\\\": 0.4, \\\"b_star\\\": \\\"per-batch adaptive (0.0-3.8)\\\", \\\"alpha_eff_range\\\": \\\"0.03-0.80 (capped at tau)\\\", \\\"eval_ppl_holdout\\\": 17.644, \\\"eval_loss_holdout\\\": 2.8704, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\", \\\"eval_note\\\": \\\"unified post-hoc eval 2026-05-15; confirmed unchanged from prior post-hoc (was 17.644/4077068)\\\"}}, \\\"uniform_seed456\\\": {\\\"metrics\\\": {\\\"train_loss\\\": 7.2895, \\\"total_steps\\\": 6103, \\\"train_duration_s\\\": 11974, \\\"eval_ppl_holdout\\\": 17.7015, \\\"eval_loss_holdout\\\": 2.8737, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\", \\\"eval_note\\\": \\\"unified post-hoc eval 2026-05-15; was 17.70/4080000 from inline eval\\\"}}, \\\"uniform_seed123\\\": {\\\"metrics\\\": {\\\"train_loss\\\": 7.3121, \\\"total_steps\\\": 6103, \\\"train_duration_s\\\": 11994, \\\"eval_ppl_holdout\\\": 17.6861, \\\"eval_loss_holdout\\\": 2.8728, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\", \\\"eval_note\\\": \\\"unified post-hoc eval 2026-05-15; was 17.69/4080000 from inline eval\\\"}}, \\\"uniform_seed42\\\": {\\\"metrics\\\": {\\\"train_loss\\\": 7.3104, \\\"total_steps\\\": 6103, \\\"train_duration_s\\\": 11946, \\\"eval_ppl_holdout\\\": 17.6939, \\\"eval_loss_holdout\\\": 2.8732, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\", \\\"eval_note\\\": \\\"unified post-hoc eval 2026-05-15; was 17.69/4080000 from inline eval\\\"}}, \\\"detector_modernbert\\\": {}, \\\"nmin1_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.789, \\\"eval_loss\\\": 2.8786, \\\"eval_holdout_tokens\\\": 4077068, \\\"b_star_mean\\\": 7.197, \\\"b_star_median\\\": 1.746, \\\"b_star_std\\\": 8.374, \\\"b_star_min\\\": 0, \\\"b_star_max\\\": 20, \\\"b_star_p25\\\": 0.803, \\\"b_star_p75\\\": 20, \\\"b_star_zero_frac\\\": 0.019, \\\"b_star_pct_below_0.5\\\": 13.1, \\\"b_star_pct_0.5_to_1\\\": 19.1, \\\"b_star_pct_1_to_2\\\": 21.1, \\\"b_star_pct_above_2\\\": 46.7, \\\"b_star_count\\\": 24412, \\\"alpha_eff_mean\\\": 0.714, \\\"alpha_eff_median\\\": 0.8}}, \\\"golden_ratio_seed42\\\": {\\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.654, \\\"eval_loss\\\": 2.871, \\\"train_loss\\\": 2.1145, \\\"train_loss_last500\\\": 2.109, \\\"eval_holdout_tokens\\\": 4077068, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 13442, \\\"gpu_hours\\\": 3.73}}, \\\"tau_0.6_seed42\\\": {}, \\\"grid_b_low_seed42\\\": {}, \\\"grid_b1_5_seed456\\\": {\\\"metrics\\\": {\\\"train_loss\\\": 10.435, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 12950.16, \\\"gpu_hours\\\": 3.67, \\\"train_samples_per_second\\\": 7.54, \\\"eval_loss\\\": 2.8741, \\\"eval_ppl_holdout\\\": 17.71, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_loss_holdout\\\": 2.875, \\\"eval_tokens\\\": 5004058}}, \\\"grid_b1_0_seed456\\\": {\\\"metrics\\\": {\\\"train_loss\\\": 10.178, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 12963.87, \\\"gpu_hours\\\": 3.67, \\\"train_samples_per_second\\\": 7.532, \\\"eval_loss\\\": 2.8725, \\\"eval_ppl_holdout\\\": 17.68, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_loss_holdout\\\": 2.8734, \\\"eval_tokens\\\": 5004058}}, \\\"grid_b0_5_seed456\\\": {\\\"metrics\\\": {\\\"train_loss\\\": 9.5622, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 12953.96, \\\"gpu_hours\\\": 3.6, \\\"train_samples_per_second\\\": 7.538, \\\"eval_loss\\\": 2.8705, \\\"eval_ppl_holdout\\\": 17.65, \\\"eval_holdout_tokens\\\": 4077068}}, \\\"grid_b_seed42_batch\\\": {\\\"metrics\\\": {\\\"b_values\\\": [0.5, 1, 1.5, 2, 3, 5], \\\"b0_5_train_loss\\\": 9.598, \\\"b0_5_completed\\\": true, \\\"b1_0_completed\\\": true, \\\"b1_5_completed\\\": true, \\\"b2_0_current_step\\\": 5149, \\\"b2_0_total_steps\\\": 6103, \\\"completed_b_values\\\": [0.5, 1, 1.5, 2, 3], \\\"current_b\\\": 5, \\\"total_steps\\\": 6103, \\\"current_step\\\": 3422, \\\"b5_0_progress_pct\\\": 56, \\\"eta_minutes\\\": 95, \\\"b2_0_completed\\\": true, \\\"b2_0_train_loss\\\": 10.621, \\\"b2_0_train_runtime_s\\\": 13034, \\\"b3_0_completed\\\": true, \\\"b3_0_train_loss\\\": 10.754, \\\"b3_0_train_runtime_s\\\": 13036, \\\"all_completed\\\": true, \\\"b1_0_train_loss\\\": 10.223, \\\"b1_5_train_loss\\\": 10.485, \\\"b5_0_train_loss\\\": 10.858, \\\"b0_5_runtime_s\\\": 13036, \\\"b1_0_runtime_s\\\": 12968, \\\"b1_5_runtime_s\\\": 14789, \\\"b2_0_runtime_s\\\": 13034, \\\"b3_0_runtime_s\\\": 13036, \\\"b5_0_runtime_s\\\": 13115, \\\"note\\\": \\\"eval_ppl missing - no --eval_data_path in batch script, post-hoc eval pending\\\", \\\"b0_5_eval_ppl\\\": 17.651, \\\"b1_0_eval_ppl\\\": 17.692, \\\"b1_5_eval_ppl\\\": 17.718, \\\"b2_0_eval_ppl\\\": 17.741, \\\"b3_0_eval_ppl\\\": 17.774, \\\"b5_0_eval_ppl\\\": 17.818, \\\"eval_holdout_tokens\\\": 4077068, \\\"best_b\\\": 0.5, \\\"best_eval_ppl\\\": 17.651}}, \\\"diagnostic_contamination100\\\": {}, \\\"detector_tfidf_lr\\\": {\\\"metrics\\\": {\\\"auc\\\": 0.939, \\\"accuracy\\\": 0.858, \\\"ece_raw\\\": 0.24, \\\"ece_calibrated\\\": 0.048, \\\"temperature_T\\\": 0.204, \\\"q_score_mean\\\": 0.6, \\\"q_score_std\\\": 0.374, \\\"q_score_median\\\": 0.707, \\\"mid_range_ratio\\\": 0.463}}}, \\\"count\\\": 180, \\\"total\\\": 180, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.5567}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"adaptive_rho06_tau07_seed42\": {\"metrics\": {\"holdout_ppl\": 17.735, \"eval_ppl_openwebtext\": 18.408, \"eval_ppl_wikipedia\": 15.355, \"downstream_arc_easy\": 0.6132, \"downstream_arc_challenge\": 0.3422, \"downstream_hellaswag\": 0.4807, \"downstream_piqa\": 0.6861, \"downstream_winogrande\": 0.5793, \"downstream_mean\": 0.5403}}, \"adaptive_rho06_tau07_seed456\": {\"metrics\": {\"holdout_ppl\": 17.732, \"eval_ppl_openwebtext\": 18.411, \"eval_ppl_wikipedia\": 15.424, \"downstream_arc_easy\": 0.6128, \"downstream_arc_challenge\": 0.3456, \"downstream_hellaswag\": 0.4806, \"downstream_piqa\": 0.6866, \"downstream_winogrande\": 0.562, \"downstream_mean\": 0.5375}}, \"adaptive_1_7b_seed42_v4\": {}, \"uniform_1_7b_seed42_v4\": {}, \"adaptive_rho06_tau07_seed123\": {\"metrics\": {\"holdout_ppl\": 17.727, \"eval_ppl_openwebtext\": 18.385, \"eval_ppl_wikipedia\": 15.329, \"downstream_arc_easy\": 0.5951, \"downstream_arc_challenge\": 0.3422, \"downstream_hellaswag\": 0.4811, \"downstream_piqa\": 0.6866, \"downstream_winogrande\": 0.5754, \"downstream_mean\": 0.5361}}, \"adaptive_fix_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.6527, \"downstream_arc_easy\": 0.6157, \"downstream_arc_challenge\": 0.343, \"downstream_hellaswag\": 0.4785, \"downstream_piqa\": 0.6866, \"downstream_winogrande\": 0.5777, \"downstream_mean\": 0.5403, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16\", \"eval_ppl_openwebtext\": 18.424, \"eval_ppl_wikipedia\": 15.473}}, \"qwen06b_uniform_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.69, \"eval_loss_holdout\": 2.8733, \"eval_holdout_tokens\": 4077068, \"train_loss\": 1.9882, \"note\": \"v2 run on westd-41312 (no inline eval)\", \"downstream_arc_easy_acc_norm\": 0.6128, \"downstream_arc_challenge_acc_norm\": 0.3481, \"downstream_hellaswag_acc_norm\": 0.4836, \"downstream_piqa_acc_norm\": 0.6877, \"downstream_winogrande_acc\": 0.5856, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\", \"eval_ppl_openwebtext\": 18.365, \"eval_ppl_wikipedia\": 15.335}}, \"detect_remove_q04_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.26, \"eval_loss_holdout\": 2.8485, \"downstream_arc_easy_acc_norm\": 0.6107, \"downstream_arc_challenge_acc_norm\": 0.3567, \"downstream_hellaswag_acc_norm\": 0.4819, \"downstream_piqa_acc_norm\": 0.6931, \"downstream_winogrande_acc\": 0.5659, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\", \"eval_ppl_openwebtext\": 18.001, \"eval_ppl_wikipedia\": 15.038}}, \"detect_remove_q03_seed42_r2\": {\"metrics\": {\"eval_ppl_holdout\": 17.25, \"eval_loss_holdout\": 2.848, \"downstream_arc_easy_acc_norm\": 0.6301, \"downstream_arc_challenge_acc_norm\": 0.3549, \"downstream_hellaswag_acc_norm\": 0.4851, \"downstream_piqa_acc_norm\": 0.6872, \"downstream_winogrande_acc\": 0.5675, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\", \"eval_ppl_openwebtext\": 18.004, \"eval_ppl_wikipedia\": 15.037}}, \"detect_remove_q08_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.3442, \"eval_loss_holdout\": 2.8533, \"downstream_arc_easy_acc_norm\": 0.6086, \"downstream_arc_challenge_acc_norm\": 0.3592, \"downstream_hellaswag_acc_norm\": 0.4855, \"downstream_piqa_acc_norm\": 0.6937, \"downstream_winogrande_acc\": 0.5817, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\", \"eval_ppl_openwebtext\": 18.039, \"eval_ppl_wikipedia\": 15.066}}, \"adaptive_1_7b_seed42_v3\": {}, \"uniform_1_7b_seed42_v3\": {}, \"detect_remove_q01_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.4, \"eval_ppl_openwebtext\": 18.22, \"eval_ppl_wikitext\": 28.22}}, \"detect_remove_q03_seed456\": {\"metrics\": {\"eval_ppl_holdout\": 17.2509, \"eval_loss_holdout\": 2.8479, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048 (final checkpoint)\", \"train_loss\": 11.255, \"total_steps\": 6103, \"eval_ppl_openwebtext\": 18.03, \"eval_ppl_wikitext\": 27.61}}, \"detect_remove_q03_seed123\": {\"metrics\": {\"eval_ppl_holdout\": 17.25, \"eval_loss_holdout\": 2.8479, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"sliding_window_stride1024_maxlen2048_fp16_5000docs\", \"total_steps\": 6103, \"train_loss_final\": 11.2441, \"train_runtime_s\": 13059, \"epoch\": 0.84, \"eval_ppl_openwebtext\": 18.03, \"eval_ppl_wikitext\": 27.53}}, \"detect_remove_q05_seed456\": {\"metrics\": {\"eval_ppl_holdout\": 17.28, \"eval_loss_holdout\": 2.8493, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --checkpoints --max_docs 5000 --max_length 2048 --stride 1024 --fp16\", \"eval_ppl_openwebtext\": 18.01, \"eval_ppl_wikitext\": 27.68}}, \"detect_remove_q05_seed123\": {\"metrics\": {\"eval_ppl_holdout\": 17.27, \"eval_loss_holdout\": 2.8491, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --checkpoints --max_docs 5000 --max_length 2048 --stride 1024 --fp16\", \"eval_ppl_openwebtext\": 18.01, \"eval_ppl_wikitext\": 27.75}}, \"detect_remove_q02_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.27, \"eval_loss_holdout\": 2.8491, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048 (final checkpoint)\", \"train_loss\": 11.348, \"train_steps\": 6103, \"data_count\": 91654, \"eval_ppl_openwebtext\": 18.06, \"eval_ppl_wikitext\": 27.64}}, \"epoch_matched_dr_seed456\": {\"metrics\": {\"eval_ppl_holdout\": 17.66, \"eval_loss_holdout\": 2.8712, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048\", \"eval_ppl_openwebtext\": 18.27, \"eval_ppl_wikitext\": 28.14}}, \"epoch_matched_dr_seed123\": {\"metrics\": {\"eval_ppl_holdout\": 17.66, \"eval_loss_holdout\": 2.8713, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048\", \"eval_ppl_openwebtext\": 18.3, \"eval_ppl_wikitext\": 27.9}}, \"eval_q04\": {\"metrics\": {\"loss\": 2.8485, \"perplexity\": 17.2626, \"num_tokens\": 4077068, \"elapsed_seconds\": 103.8, \"downstream_arc_easy_acc_norm\": 0.6107, \"downstream_arc_challenge_acc_norm\": 0.3567, \"downstream_hellaswag_acc_norm\": 0.4819, \"downstream_piqa_acc_norm\": 0.6931, \"downstream_winogrande_acc\": 0.5659, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\"}}, \"eval_q03_r2\": {\"metrics\": {\"loss\": 2.848, \"perplexity\": 17.2538, \"num_tokens\": 4077068, \"elapsed_seconds\": 111, \"downstream_arc_easy_acc_norm\": 0.6301, \"downstream_arc_challenge_acc_norm\": 0.3549, \"downstream_hellaswag_acc_norm\": 0.4851, \"downstream_piqa_acc_norm\": 0.6872, \"downstream_winogrande_acc\": 0.5675, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\"}}, \"eval_rho06_batch_v7\": {\"metrics\": {\"contamination_60_ess_only_seed123\": {\"loss\": 2.8771, \"perplexity\": 17.76, \"tokens\": 4077068}, \"contamination_60_ess_only_seed456\": {\"loss\": 2.8771, \"perplexity\": 17.76, \"tokens\": 4077068}, \"contamination_60_random_seed123\": {\"loss\": 2.8832, \"perplexity\": 17.87, \"tokens\": 4077068}, \"contamination_60_random_seed456\": {\"loss\": 2.8837, \"perplexity\": 17.88, \"tokens\": 4077068}, \"eval_data\": \"data/human/eval_holdout.jsonl\", \"max_docs\": 5000, \"max_length\": 2048}}, \"eval_q01_final_v2\": {\"metrics\": {\"loss\": 2.8563, \"perplexity\": 17.3965, \"num_tokens\": 4077068, \"elapsed_seconds\": 105.1}}, \"eval_q07_final\": {\"metrics\": {\"loss\": 2.8519, \"perplexity\": 17.3201, \"num_tokens\": 4077068, \"elapsed_seconds\": 103.8}}, \"eval_q06\": {\"metrics\": {\"loss\": 2.8507, \"perplexity\": 17.2993, \"num_tokens\": 4077068, \"elapsed_seconds\": 106.9}}, \"eval_epoch_matched_seed456\": {\"metrics\": {\"loss\": 2.8712, \"perplexity\": 17.6574, \"num_tokens\": 4077068, \"elapsed_seconds\": 103.6}}, \"eval_epoch_matched_seed123\": {\"metrics\": {\"loss\": 2.8713, \"perplexity\": 17.6599, \"num_tokens\": 4077068, \"elapsed_seconds\": 104.3}}, \"eval_ngram_uniform\": {\"metrics\": {\"loss\": 2.8733, \"perplexity\": 17.69, \"tokens\": 4077068, \"eval_data\": \"data/human/eval_holdout.jsonl\", \"max_docs\": 5000, \"max_length\": 2048, \"checkpoint\": \"ngram_uniform_seed42/final\"}}, \"eval_ngram_adaptive\": {\"metrics\": {\"loss\": 2.8803, \"perplexity\": 17.82, \"tokens\": 4077068, \"eval_data\": \"data/human/eval_holdout.jsonl\", \"max_docs\": 5000, \"max_length\": 2048, \"checkpoint\": \"ngram_adaptive_seed42/final\"}}, \"uniform_seed42_downstream\": {\"metrics\": {\"downstream_arc_easy_acc_norm\": 0.6128, \"downstream_arc_challenge_acc_norm\": 0.3481, \"downstream_hellaswag_acc_norm\": 0.4836, \"downstream_piqa_acc_norm\": 0.6877, \"downstream_winogrande_acc\": 0.5856, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\"}}, \"adaptive_fromscratch_seed42\": {\"metrics\": {\"train_loss\": 9.976, \"eval_ppl_holdout\": 17.689, \"eval_ppl_openwebtext\": 18.37, \"eval_ppl_wikipedia\": 15.349, \"downstream_arc_easy_acc_norm\": 0.6178, \"downstream_arc_challenge_acc_norm\": 0.3524, \"downstream_hellaswag_acc_norm\": 0.4806, \"downstream_piqa_acc_norm\": 0.6844, \"downstream_winogrande_acc\": 0.5801, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\", \"eval_method\": \"eval_ppl_ood.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"training_time_s\": 13660}}, \"hybrid_rho06_seed42\": {\"metrics\": {\"eval_loss_holdout\": 2.8637, \"eval_ppl_holdout\": 17.526, \"eval_ppl_openwebtext\": 18.208, \"eval_ppl_wikipedia\": 15.267, \"downstream_arc_easy_acc_norm\": 0.6208, \"downstream_arc_challenge_acc_norm\": 0.3524, \"downstream_hellaswag_acc_norm\": 0.4801, \"downstream_piqa_acc_norm\": 0.6931, \"downstream_winogrande_acc\": 0.5785, \"eval_source\": \"rho06_tau07_seed42 eval worker - evaluated hybrid checkpoint by mistake\"}}, \"rho06_tau07_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.526, \"eval_ppl_openwebtext\": 18.208, \"eval_ppl_wikipedia\": 15.267, \"downstream_arc_easy_acc_norm\": 0.6208, \"downstream_arc_challenge_acc_norm\": 0.3524, \"downstream_hellaswag_acc_norm\": 0.4801, \"downstream_piqa_acc_norm\": 0.6931, \"downstream_winogrande_acc\": 0.5785}}, \"tau07_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.68, \"eval_ppl_openwebtext\": 18.348, \"eval_ppl_wikipedia\": 15.331, \"downstream_arc_easy_acc_norm\": 0.6166, \"downstream_arc_challenge_acc_norm\": 0.3473, \"downstream_hellaswag_acc_norm\": 0.4795, \"downstream_piqa_acc_norm\": 0.6861, \"downstream_winogrande_acc\": 0.5817, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\", \"eval_method\": \"eval_ppl_ood.py (sliding window, stride=1024, max_docs=5000, fp16)\"}}, \"tau07_seed456\": {\"metrics\": {\"eval_ppl_holdout\": 17.677, \"eval_ppl_openwebtext\": 18.344, \"eval_ppl_wikipedia\": 15.315, \"downstream_arc_easy_acc_norm\": 0.6111, \"downstream_arc_challenge_acc_norm\": 0.3515, \"downstream_hellaswag_acc_norm\": 0.4811, \"downstream_piqa_acc_norm\": 0.6834, \"downstream_winogrande_acc\": 0.5722, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\", \"eval_method\": \"eval_ppl_ood.py (sliding window, stride=1024, max_docs=5000, fp16)\"}}, \"tau07_seed123\": {\"metrics\": {\"eval_ppl_holdout\": 17.666, \"eval_ppl_openwebtext\": 18.348, \"eval_ppl_wikipedia\": 15.345, \"downstream_arc_easy_acc_norm\": 0.6309, \"downstream_arc_challenge_acc_norm\": 0.3481, \"downstream_hellaswag_acc_norm\": 0.4775, \"downstream_piqa_acc_norm\": 0.6866, \"downstream_winogrande_acc\": 0.5675, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\", \"eval_method\": \"eval_ppl_ood.py (sliding window, stride=1024, max_docs=5000, fp16)\"}}, \"tau07_downstream_eval\": {}, \"uniform_ood_seed123\": {\"metrics\": {\"eval_ppl_holdout\": 17.6861, \"eval_ppl_openwebtext\": 18.3678, \"eval_ppl_wikipedia\": 15.3768, \"downstream_arc_easy_acc_norm\": 0.6229, \"downstream_arc_challenge_acc_norm\": 0.3507, \"downstream_hellaswag_acc_norm\": 0.4797, \"downstream_piqa_acc_norm\": 0.685, \"downstream_winogrande_acc\": 0.5762, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\"}}, \"adaptive_ood_seed456\": {\"metrics\": {\"eval_ppl_holdout\": 17.683, \"eval_ppl_openwebtext\": 18.366, \"eval_ppl_wikipedia\": 15.345, \"downstream_arc_easy_acc_norm\": 0.6077, \"downstream_arc_challenge_acc_norm\": 0.3541, \"downstream_hellaswag_acc_norm\": 0.48, \"downstream_piqa_acc_norm\": 0.6806, \"downstream_winogrande_acc\": 0.5714, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\"}}, \"adaptive_ood_seed123\": {\"metrics\": {\"eval_ppl_holdout\": 17.677, \"eval_ppl_openwebtext\": 18.373, \"eval_ppl_wikipedia\": 15.37, \"downstream_arc_easy_acc_norm\": 0.6301, \"downstream_arc_challenge_acc_norm\": 0.3481, \"downstream_hellaswag_acc_norm\": 0.4791, \"downstream_piqa_acc_norm\": 0.6844, \"downstream_winogrande_acc\": 0.5706, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\"}}, \"uniform_ood_seed456\": {\"metrics\": {\"eval_ppl_holdout\": 17.7015, \"eval_ppl_openwebtext\": 18.3865, \"eval_ppl_wikipedia\": 15.3594, \"downstream_arc_easy_acc_norm\": 0.6166, \"downstream_arc_challenge_acc_norm\": 0.3439, \"downstream_hellaswag_acc_norm\": 0.4826, \"downstream_piqa_acc_norm\": 0.6795, \"downstream_winogrande_acc\": 0.5667, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\"}}, \"w2_distribution_matching_eval\": {}, \"uniform_1_7b_seed123\": {\"metrics\": {\"eval_ppl_holdout\": 13.2648, \"eval_loss_holdout\": 2.5851, \"train_loss_final\": 7.557, \"total_steps\": 6103, \"num_eval_tokens\": 4077068}}, \"detect_remove_q07_epoch_matched_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.62, \"eval_loss_holdout\": 2.8689, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"sliding_window_stride1024_maxlen2048_fp16_5000docs\", \"total_steps\": 3047}}, \"detect_remove_q09_epoch_matched_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.628, \"eval_loss_holdout\": 2.8695, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"sliding_window_stride1024_maxlen2048_fp16_5000docs\", \"total_steps\": 3770, \"train_loss_final\": 9.9127}}, \"adaptive_1_7b_seed123\": {\"metrics\": {\"eval_ppl_holdout\": 13.25, \"eval_loss_holdout\": 2.5843}}, \"detect_remove_q01_epoch_matched_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 18.0436, \"eval_loss_holdout\": 2.8928, \"eval_holdout_tokens\": 4077068}}, \"ngram_adaptive_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.82, \"eval_loss_holdout\": 2.8803}}, \"ngram_uniform_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.69, \"eval_loss_holdout\": 2.8733}}, \"detect_remove_q03_epoch_matched_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.74, \"eval_loss_holdout\": 2.876, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"sliding_window_stride1024_maxlen2048_fp16_5000docs\", \"total_steps\": 1927, \"train_loss_final\": 11.3917, \"interpretation\": \"PPL 17.74 vs epoch-matched q05 (17.65): q03 stricter filtering yields HIGHER PPL (+0.09) under matched training budget, not lower. This contradicts the hypothesis that stricter filtering improves data quality per-token. Meanwhile multi-epoch q03 (17.25) is much lower, confirming that the PPL advantage of q03 in multi-epoch setting comes from more training epochs on filtered data, not from higher per-token quality. Conclusion: under fixed training budget, stricter filtering (q03) actually hurts slightly compared to moderate filtering (q05), likely because removing too many borderline samples reduces diversity without sufficient quality gain.\"}}, \"gpt2_adaptive_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.79, \"eval_loss_holdout\": 2.879, \"train_loss\": 10.58, \"train_steps\": 6103, \"train_runtime_hours\": 3.92}}, \"gpt2_uniform_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.69, \"eval_loss_holdout\": 2.8733, \"train_loss\": 7.989, \"train_steps\": 6103, \"train_runtime_hours\": 3.54}}, \"eval_uniform_1_7b_v3\": {\"metrics\": {\"eval_ppl_holdout\": 13.5}}, \"eval_adaptive_1_7b_v2\": {\"metrics\": {\"eval_ppl_holdout\": 13.27}}, \"detect_remove_q06_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.3, \"eval_loss_holdout\": 2.8507}}, \"adaptive_1_7b_seed42\": {}, \"detect_remove_q07_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.32, \"eval_loss_holdout\": 2.8519, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048 (final checkpoint)\", \"note\": \"final checkpoint, replaces partial ckpt-3500 PPL=17.49\"}}, \"ess_only_seed456\": {\"metrics\": {\"eval_ppl_holdout\": 17.76, \"eval_loss_holdout\": 2.877, \"eval_holdout_tokens\": 4077068, \"train_loss\": 1.9364, \"note\": \"re-eval on westd-41312 latest run (v2)\"}}, \"random_reweight_seed456\": {\"metrics\": {\"eval_ppl_holdout\": 17.777, \"eval_loss_holdout\": 2.8779, \"eval_holdout_tokens\": 4077068, \"total_steps\": 6103, \"train_loss\": 6.657, \"train_runtime_seconds\": 10739}}, \"ess_only_seed123\": {\"metrics\": {\"eval_ppl_holdout\": 17.72, \"eval_loss_holdout\": 2.8746, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py on data/human/eval_holdout.jsonl, max_docs=5000, stride=1024, fp16\", \"eval_note\": \"Also ran on scored_data.jsonl (train data): ppl=9.66, loss=2.2677, tokens=3029693\", \"train_loss\": 10.2159, \"train_steps\": 6103, \"train_runtime_seconds\": 12959.5, \"b_star_mean\": 3.55, \"b_star_median\": 1.5918, \"b_star_std\": 4.7209, \"b_star_min\": 0.2344, \"b_star_max\": 20, \"b_star_p25\": 0.8398, \"b_star_p75\": 3.8281, \"b_star_p90\": 9.5996, \"b_star_count\": 21971, \"vs_uniform_ppl_delta\": \"+0.034\", \"vs_adaptive_fix_ppl_delta\": \"+0.077\"}}, \"detect_remove_q03_seed42\": {}, \"uniform_1_7b_seed42\": {}, \"detect_remove_q09_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.42, \"eval_loss_holdout\": 2.8577, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --checkpoints --max_docs 5000 --max_length 2048 --stride 1024 --fp16\"}}, \"contamination_60_ess_only_seed456\": {\"metrics\": {\"eval_ppl_holdout\": 17.762, \"eval_loss_holdout\": 2.8771, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --checkpoints --max_docs 5000 --max_length 2048\"}}, \"contamination_60_ess_only_seed123\": {\"metrics\": {\"eval_ppl_holdout\": 17.763, \"eval_loss_holdout\": 2.8771, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --checkpoints --max_docs 5000 --max_length 2048\"}}, \"ess_only_seed456_r2\": {\"metrics\": {\"eval_ppl_holdout\": 17.762, \"eval_loss_holdout\": 2.877, \"eval_holdout_tokens\": 4077068, \"total_steps\": 6103, \"train_loss\": 5.998, \"train_runtime_seconds\": 7611}}, \"ess_only_seed123_r2\": {\"metrics\": {\"eval_ppl_holdout\": 17.721, \"eval_loss_holdout\": 2.8747, \"eval_holdout_tokens\": 4077068, \"total_steps\": 6103, \"train_loss\": 6.86, \"train_runtime_seconds\": 8674}}, \"detect_remove_q05_epoch_matched_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.65, \"eval_loss_holdout\": 2.8707, \"eval_holdout_tokens\": 4077068, \"train_loss_final\": 3.184, \"total_steps\": 2533, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048 --stride 1024 --fp16\", \"vs_full_dr_q05\": \"+0.360 (17.650 vs 17.290, epoch-matched worse)\", \"vs_adaptive\": \"-0.001 (17.650 vs 17.651, nearly identical to adaptive)\", \"interpretation\": \"D&R 0.36 PPL advantage over epoch-matched is entirely from multi-epoch training on clean data, not from data quality filtering\"}}, \"contamination_60_random_seed123\": {\"metrics\": {\"eval_ppl_holdout\": 17.87, \"eval_loss_holdout\": 2.8832, \"eval_holdout_tokens\": 4077068}}, \"contamination_60_random_seed456\": {\"metrics\": {\"eval_ppl_holdout\": 17.88, \"eval_loss_holdout\": 2.8837, \"eval_holdout_tokens\": 4077068}}, \"contamination_60_grid_b0_3_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.634, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048 --stride 1024 --fp16\", \"checkpoint_1500_ppl\": 18.583, \"total_steps\": 6103, \"note\": \"resume from checkpoint-1500 with ~30% LR offset; final PPL improved over checkpoint-1500, no degradation\"}}, \"contamination_60_random_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.832, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048 --stride 1024 --fp16\", \"total_steps\": 6103, \"note\": \"resume from checkpoint-1000; cron falsely marked failed due to log path mismatch\"}}, \"grid_b0_2_seed456\": {\"metrics\": {\"eval_ppl_holdout\": 17.645, \"eval_loss_holdout\": 2.87, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048 --stride 1024 --fp16\", \"eval_checkpoint\": \"checkpoint-5500\", \"note\": \"eval at checkpoint-5500; final checkpoint degraded due to --save_only_model LR reset on resume\"}}, \"grid_b0_2_seed123\": {\"metrics\": {\"eval_ppl_holdout\": 17.637, \"eval_loss_holdout\": 2.87, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048 --stride 1024 --fp16\", \"eval_checkpoint\": \"checkpoint-5500\", \"note\": \"eval at checkpoint-5500; final checkpoint degraded due to --save_only_model LR reset on resume\"}}, \"contamination_60_adaptive_seed456\": {\"metrics\": {\"eval_ppl_holdout\": 17.735, \"eval_loss_holdout\": 2.8755, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --stride 1024 --fp16\"}}, \"contamination_60_uniform_seed456\": {\"metrics\": {\"eval_ppl_holdout\": 17.77, \"eval_loss_holdout\": 2.8775, \"eval_holdout_tokens\": 4077068, \"train_loss\": 7.637, \"train_runtime_seconds\": 12845, \"total_steps\": 6103, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048\"}}, \"grid_b0_1_seed123\": {\"metrics\": {\"eval_ppl_holdout\": 17.646, \"eval_loss_holdout\": 2.8705, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048 --fp16\"}}, \"grid_b0_1_seed456\": {\"metrics\": {\"eval_ppl_holdout\": 17.663, \"eval_loss_holdout\": 2.8715, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048 --fp16\"}}, \"contamination_60_ess_only_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.77, \"eval_loss_holdout\": 2.8775, \"eval_holdout_tokens\": 4077068, \"train_loss\": 9.842, \"total_steps\": 6103, \"train_runtime_seconds\": 13152}}, \"contamination_60_uniform_seed123\": {\"metrics\": {\"eval_ppl_holdout\": 17.754, \"eval_loss_holdout\": 2.8766, \"eval_holdout_tokens\": 4077068, \"total_steps\": 6103, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048\"}}, \"contamination_60_seed123\": {\"metrics\": {\"eval_ppl_holdout\": 17.732, \"eval_loss_holdout\": 2.8754, \"eval_holdout_tokens\": 4077068, \"train_loss\": 9.6302, \"train_runtime_seconds\": 13638.6, \"total_steps\": 6103, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048\"}}, \"grid_b0_3_seed123_r2\": {\"metrics\": {\"eval_ppl_holdout\": 17.5792, \"eval_loss_holdout\": 2.8667, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\", \"re_eval_date\": \"2026-05-18\", \"eval_results_path\": \"/root/autodl-tmp/output/models/grid_b0_3_seed123/eval_results.json\", \"re_eval_note\": \"re-eval confirms original PPL=17.58; JSON artifact now saved\"}}, \"grid_b0_3_seed456_r2\": {\"metrics\": {\"eval_ppl_holdout\": 17.64, \"eval_loss_holdout\": 2.87, \"eval_holdout_tokens\": 4077068, \"total_steps\": 6103, \"train_loss\": 9.085, \"vs_uniform\": \"-0.054 (17.64 vs 17.694)\", \"vs_grid_b03_seed42\": \"0.000 (17.64 vs 17.640)\", \"vs_grid_b05_seed456\": \"-0.01 (17.64 vs 17.65)\"}}, \"batchsize16_nmin8_r3\": {\"metrics\": {\"eval_ppl_holdout\": 17.65, \"eval_loss_holdout\": 2.871, \"eval_holdout_tokens\": 4077068, \"total_steps\": 6103, \"train_loss\": 2.6308, \"train_runtime_seconds\": 15057, \"vs_adaptive_bs4\": \"-0.003 (17.65 vs 17.6527)\", \"vs_bs8_nmin4\": \"-0.01 (17.65 vs 17.66)\", \"batch_size\": 16, \"n_min\": 8}}, \"rho02_adaptive_tau08_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.382, \"eval_loss_holdout\": 2.8555, \"eval_holdout_tokens\": 4077068, \"total_steps\": 6103, \"train_runtime_seconds\": 14599, \"vs_rho02_uniform\": \"+0.046 (17.382 vs 17.336)\", \"vs_rho04_uniform\": \"-0.312 (17.382 vs 17.694)\", \"tau\": 0.8, \"rho\": 0.2, \"b_star_pct_zero\": \"40-50%\", \"conclusion_note\": \"worse than same-rho uniform baseline\"}}, \"batchsize16_nmin8_r2\": {}, \"grid_b0_3_seed456\": {}, \"batch_adaptive_tau_rho06_r5\": {\"metrics\": {\"eval_ppl_holdout\": 17.73, \"eval_loss_holdout\": 2.8754, \"eval_holdout_tokens\": 4077068, \"train_loss\": 9.267, \"train_runtime_seconds\": 13903, \"total_steps\": 6103, \"vs_uniform_rho06\": \"-0.036\", \"vs_adaptive_fixed_tau08_rho06\": \"-0.010\", \"vs_grid_best_rho06\": \"+0.026\", \"vs_hybrid_rho06\": \"+0.200\"}}, \"random_reweight_seed123_r5\": {\"metrics\": {\"eval_ppl_holdout\": 17.8, \"eval_loss_holdout\": 2.8793, \"eval_holdout_tokens\": 4077068, \"train_loss\": 8.0176, \"train_runtime_seconds\": 13267, \"total_steps\": 6103, \"vs_uniform_seed123\": \"+0.114\", \"vs_adaptive_fix_seed123\": \"+0.157\", \"vs_random_reweight_v2_seed42\": \"consistent (+0.136 seed42 vs +0.114 seed123)\"}}, \"rho02_adaptive_tau09_r5\": {\"metrics\": {\"eval_ppl_holdout\": 17.45, \"eval_loss_holdout\": 2.8593, \"eval_holdout_tokens\": 4077068, \"train_loss\": 11.864, \"epoch\": 0.47, \"b_star_mean\": 4.3493, \"b_star_median\": 2.9609, \"b_star_std\": 4.3982, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_pct_zero\": 2.65, \"alpha_eff_mean\": 0.8277, \"alpha_eff_median\": 0.8826, \"alpha_eff_pct_at_max\": 42.95, \"ess_mean\": 2.3784, \"ess_median\": 2.0121}}, \"bs8_auto_nmin_r5\": {\"metrics\": {\"eval_ppl_holdout\": 17.66, \"eval_loss_holdout\": 2.8716, \"eval_holdout_tokens\": 4077068, \"train_loss\": 5.163, \"total_steps\": 6103, \"train_runtime_seconds\": 14064, \"epoch\": 0.26, \"b_star_mean\": 1.0957, \"b_star_median\": 0.9, \"b_star_std\": 0.7563, \"b_star_pct_zero\": 0.11, \"b_star_pct_below_0.5\": 10.43, \"ess_mean\": 4.4925, \"ess_median\": 4.0446, \"alpha_eff_mean\": 0.7023, \"alpha_eff_median\": 0.7572, \"alpha_eff_pct_at_max\": 38.88}}, \"grid_b0_1_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.657, \"eval_loss_holdout\": 2.871}}, \"llama3b_adaptive_seed42\": {\"metrics\": {\"ppl\": 10.58, \"eval_loss\": 2.359, \"eval_tokens\": 4017316}}, \"batchsize16_nmin8_seed42\": {}, \"llama3b_uniform_seed42\": {\"metrics\": {\"ppl\": 10.38, \"eval_loss\": 2.3397, \"eval_tokens\": 1526195, \"train_loss\": 7.2987, \"train_steps\": 6103, \"train_runtime_seconds\": 94309}}, \"random_reweight_seed123_r4\": {}, \"rho02_adaptive_tau09_r4\": {}, \"random_reweight_seed123_r3\": {}, \"grid_b0_2_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.64, \"eval_loss_holdout\": 2.8704, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\"}}, \"rho02_adaptive_tau09_r3\": {}, \"batch_adaptive_tau_rho06_r3\": {}, \"bs8_auto_nmin_r3\": {}, \"random_reweight_seed123_r2\": {}, \"rho02_adaptive_tau09_r2\": {\"metrics\": {\"error\": \"TypeError: Trainer.__init__() got an unexpected keyword argument 'tokenizer'\", \"error_stage\": \"initialization\", \"training_completed\": false, \"note\": \"Crashed before any training. Same bug as rho02_adaptive_tau09_seed42. Fix: replace tokenizer= with processing_class= in pretrain_weighted.py line ~101.\"}}, \"random_reweight_seed123\": {}, \"batch_adaptive_tau_rho06_r2\": {}, \"bs8_auto_nmin_r2\": {}, \"rho02_adaptive_tau09_seed42\": {}, \"batch_adaptive_tau_rho06_seed42\": {}, \"bs8_auto_nmin_seed42\": {}, \"grid_b0_3_seed123\": {}, \"random_reweight_v2_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.83, \"eval_loss_holdout\": 2.8809}}, \"tau_095_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.723, \"eval_loss\": 2.8749, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\", \"train_loss\": 10.198, \"total_steps\": 6103, \"train_runtime_s\": 13699, \"train_samples_per_second\": 7.128, \"b_star_count\": 24412, \"b_star_mean\": 3.0775, \"b_star_median\": 1.52, \"b_star_std\": 3.9923, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.8, \"b_star_p75\": 3.46, \"b_star_pct_zero\": 0, \"b_star_pct_below_0.5\": 8.5, \"b_star_pct_0.5_to_1\": 24.7, \"b_star_pct_1_to_2\": 26.4, \"b_star_pct_above_2\": 40.3}}, \"batch_adaptive_tau_rho04_seed42\": {\"metrics\": {\"eval_loss_holdout\": 2.8725, \"eval_ppl_holdout\": 17.681, \"train_loss\": 9.8206, \"train_runtime_sec\": 45402.86}}, \"p0_contamination_60_datagen\": {\"metrics\": {\"total_lines\": 371499, \"synthetic_count\": 222900, \"human_count\": 148599, \"actual_contamination_ratio\": 0.6, \"q_score_mean\": 0.6243, \"q_score_std\": 0.3703, \"q_score_median\": 0.7753, \"file_size_mb\": 907}}, \"datagen_synthetic_4gpu\": {}, \"grid_b5_0_seed123\": {\"metrics\": {\"train_loss\": 10.8468, \"total_steps\": 6103, \"train_runtime_s\": 14434, \"gpu_hours\": 4.01, \"eval_ppl_holdout\": 17.8039, \"eval_loss\": 2.8794, \"eval_holdout_tokens\": 4077068}}, \"grid_b3_0_seed123\": {\"metrics\": {\"train_loss\": 10.7422, \"total_steps\": 6103, \"train_runtime_s\": 12955.83, \"gpu_hours\": 3.6, \"eval_ppl_holdout\": 17.76, \"eval_loss\": 2.877, \"eval_holdout_tokens\": 4077068}}, \"grid_b2_0_seed123\": {\"metrics\": {\"train_loss\": 10.61, \"total_steps\": 6103, \"train_runtime_s\": 13058.8, \"gpu_hours\": 3.63, \"train_samples_per_second\": 7.478, \"train_steps_per_second\": 0.467, \"eval_ppl_holdout\": 17.725, \"eval_loss\": 2.875, \"eval_holdout_tokens\": 4077068}}, \"grid_b1_5_seed123\": {\"metrics\": {\"train_loss\": 10.4776, \"total_steps\": 6103, \"train_runtime_s\": 15053.1, \"gpu_hours\": 4.18, \"eval_ppl_holdout\": 17.701, \"eval_loss\": 2.8736}}, \"grid_b1_0_seed123\": {\"metrics\": {\"eval_ppl_holdout\": 17.674, \"eval_loss\": 2.8721, \"eval_holdout_tokens\": 4077068, \"train_loss\": 10.218, \"total_steps\": 6103, \"train_runtime_s\": 13878, \"gpu_hours\": 3.88}}, \"grid_b0_5_seed123\": {\"metrics\": {\"eval_ppl_holdout\": 17.638, \"eval_loss\": 2.87, \"eval_holdout_tokens\": 4077068, \"train_loss\": 9.601, \"total_steps\": 6103, \"train_runtime_s\": 13104, \"gpu_hours\": 3.8}}, \"hybrid_rho04_seed42\": {\"metrics\": {\"eval_loss_holdout\": 2.863, \"eval_ppl_holdout\": 17.514}}, \"threshold_q03_seed42\": {\"metrics\": {\"eval_loss_holdout\": 2.848, \"eval_ppl_holdout\": 17.253}}, \"rho02_uniform_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.336, \"eval_loss_holdout\": 2.853, \"eval_holdout_tokens\": 4077068}}, \"threshold_q07_seed42\": {}, \"random_reweight_seed42\": {}, \"contamination_60_tau06_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.7359, \"eval_loss_holdout\": 2.8756, \"eval_holdout_tokens\": 4077068, \"train_loss\": 8.9804, \"train_runtime_seconds\": 13367.3, \"train_samples_per_second\": 7.305, \"total_steps\": 6103, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\"}}, \"contamination_60_tau07_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.73, \"eval_loss_holdout\": 2.875, \"eval_holdout_tokens\": 4077068, \"train_loss\": 9.358, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\"}}, \"detect_remove_baseline_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.29, \"eval_loss_holdout\": 2.8499, \"eval_holdout_tokens\": 4077068, \"train_loss\": 11.003, \"train_runtime_seconds\": 13248, \"total_steps\": 6103, \"train_samples_per_second\": 7.371}}, \"grid_b0_3_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.64, \"eval_loss_holdout\": 2.8702, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"train_loss\": 9.1154, \"train_runtime_seconds\": 13365.79, \"train_samples_per_second\": 7.306, \"total_steps\": 6103, \"b_fixed\": 0.3, \"alpha_eff_typical_range\": \"0.07-0.88\", \"ess_typical_range\": \"2.3-4.0\"}}, \"tau_095_nmin2_seed42\": {}, \"tau_09_nmin2_seed42\": {}, \"nmin5_seed42\": {}, \"grid_b5_0_seed456\": {\"metrics\": {\"eval_ppl_holdout\": 17.993, \"eval_loss\": 2.89, \"eval_holdout_tokens\": 4077068, \"train_loss\": 5.488, \"total_steps\": 6103, \"train_runtime_s\": 6601, \"gpu_hours\": 1.83, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\"}}, \"grid_b3_0_seed456\": {\"metrics\": {\"eval_ppl_holdout\": 17.921, \"eval_loss\": 2.886, \"eval_holdout_tokens\": 4077068, \"train_loss\": 5.435, \"total_steps\": 6103, \"train_runtime_s\": 6602, \"gpu_hours\": 1.83, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\"}}, \"grid_b2_0_seed456\": {\"metrics\": {\"eval_ppl_holdout\": 17.989, \"eval_loss\": 2.8898, \"eval_holdout_tokens\": 4077068, \"train_loss\": 10.625, \"total_steps\": 6103, \"train_runtime_s\": 12969, \"gpu_hours\": 3.6, \"train_samples_per_second\": 7.53, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\"}}, \"ess_only_seed42\": {\"metrics\": {\"eval_ppl\": 17.73, \"eval_loss\": 2.875, \"b_star_median\": 1.58, \"b_star_mean\": 3.51, \"vs_uniform_ppl_delta\": \"+0.038\", \"vs_adaptive_ppl_delta\": \"+0.08\"}}, \"adaptive_fix_seed123\": {\"metrics\": {\"eval_ppl_holdout\": 17.6432, \"eval_loss_holdout\": 2.8704, \"eval_loss\": 2.8704, \"eval_holdout_tokens\": 4077068, \"eval_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.643/4077068\", \"train_loss_weighted\": 7.517, \"train_runtime_s\": 10347, \"total_steps\": 6103, \"epoch\": 0.26, \"b_star_mean\": 1.431, \"b_star_median\": 0.88, \"b_star_std\": 2.029, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_pct_below_0.5\": 20.9, \"b_star_pct_0.5_to_1\": 35.7, \"b_star_pct_1_to_2\": 27.3, \"b_star_pct_2_to_5\": 6.3, \"b_star_pct_above_5\": 1.9, \"b_star_count\": 25906, \"b_star_p25\": 0.54, \"b_star_p75\": 1.52, \"b_star_pct_above_2\": 16.1, \"b_star_note\": \"Training-only records (eval checkpoint records with b*=0 excluded)\"}}, \"adaptive_fix_seed456\": {\"metrics\": {\"train_loss\": 8.3124, \"train_runtime\": 11436.05, \"train_samples_per_second\": 8.539, \"train_steps_per_second\": 0.534, \"total_steps\": 6103, \"eval_ppl_holdout\": 17.6566, \"eval_loss_holdout\": 2.8711, \"eval_holdout_tokens\": 4077068, \"eval_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.66/4077068\", \"b_star_count\": 26396, \"b_star_mean\": 1.416, \"b_star_median\": 0.88, \"b_star_std\": 1.993, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.54, \"b_star_p75\": 1.52, \"b_star_pct_below_0.5\": 20.9, \"b_star_pct_0.5_to_1\": 35.7, \"b_star_pct_1_to_2\": 27.3, \"b_star_pct_above_2\": 16.1, \"b_star_note\": \"Training-only records (eval checkpoint records with b*=0 excluded)\"}}, \"adaptive_v2_seed456\": {}, \"adaptive_v2_seed123\": {}, \"adaptive_v2_seed42\": {}, \"tau_07_nmin2_seed42\": {}, \"tau_06_nmin2_seed42\": {}, \"tau_05_nmin2_seed42\": {}, \"contamination_60_seed42_r2\": {\"metrics\": {\"eval_ppl_holdout\": 17.74, \"eval_loss_holdout\": 2.8759, \"eval_tokens\": 4077068, \"eval_method\": \"sliding_window_2048_stride1024\", \"train_loss\": 9.6349, \"train_runtime_seconds\": 14092.25}}, \"contamination_60_grid_b0_5_seed42\": {\"metrics\": {\"eval_ppl\": 17.704, \"eval_loss\": 2.8738, \"eval_tokens\": 4077068, \"eval_docs\": 5000}}, \"contamination_60_uniform_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.766, \"eval_loss_holdout\": 2.8773, \"eval_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py sliding-window (stride=1024, max_length=2048, fp16) on data/human/eval_holdout.jsonl\", \"train_loss\": 7.649, \"train_runtime_seconds\": 12904}}, \"bs8_nmin2_seed42_r2\": {\"metrics\": {\"eval_ppl_holdout\": 17.73, \"eval_loss_holdout\": 2.8752, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py on data/human/eval_holdout.jsonl, max_docs=5000, stride=1024, fp16\", \"train_loss\": 5.4065, \"train_steps\": 6103, \"train_runtime_seconds\": 14621.6}}, \"grid_b_low_serial_seed42\": {}, \"grid_b_low_seed42_r3\": {}, \"grid_b_low_seed42_r2\": {}, \"baseline_qwen3_0.6b\": {\"metrics\": {\"eval_ppl_holdout\": 22.97, \"eval_loss\": 3.134, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"sliding_window_stride1024_maxlen2048_fp16\"}}, \"contamination_60_seed42\": {}, \"nmin4_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.6947, \"eval_loss\": 2.8733, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\", \"train_loss\": 7.989, \"total_steps\": 6103, \"train_runtime_s\": 16231, \"train_samples_per_second\": 6.016, \"b_star_count\": 24412, \"b_star_mean\": 0, \"b_star_median\": 0, \"b_star_std\": 0, \"b_star_min\": 0, \"b_star_max\": 0, \"b_star_pct_zero\": 100, \"ess_mean\": 4, \"ess_min\": 4, \"ess_max\": 4}}, \"bs8_nmin2_seed42\": {}, \"bs8_seed42\": {}, \"tau_09_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.712, \"eval_loss\": 2.8742, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15\", \"b_star_count\": 24412, \"b_star_mean\": 2.36, \"b_star_median\": 1.32, \"b_star_std\": 3.04, \"b_star_pct_above_2\": 33.7}}, \"tau_07_seed42\": {\"metrics\": {\"train_loss\": 9.6707, \"total_steps\": 6103, \"train_runtime_s\": 15065, \"train_samples_per_second\": 6.482, \"eval_ppl_holdout\": 17.6793, \"eval_loss\": 2.8724, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15\", \"b_star_count\": 24412, \"b_star_mean\": 0.8943, \"b_star_median\": 0.58, \"b_star_std\": 1.4007, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.3306, \"b_star_p75\": 0.9712, \"b_star_pct_zero\": 5.8, \"b_star_pct_below_0.5\": 36, \"b_star_pct_0.5_to_1\": 34.2, \"b_star_pct_1_to_2\": 16.2, \"b_star_pct_above_2\": 7.7}}, \"tau_06_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.6805, \"eval_loss\": 2.8725, \"train_loss\": 9.275, \"total_steps\": 6103, \"train_runtime_s\": 13436.64, \"train_samples_per_second\": 7.267, \"b_star_mean\": 0.5899, \"b_star_median\": 0.3746, \"b_star_std\": 1.0693, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.1195, \"b_star_p75\": 0.66, \"b_star_zero_frac\": 0.156, \"b_star_nonzero_mean\": 0.699, \"b_star_nonzero_median\": 0.4473}}, \"tau_05_seed42\": {\"metrics\": {\"train_loss\": 8.849, \"total_steps\": 6103, \"epoch\": 0.26, \"train_runtime_s\": 13431.4, \"train_samples_per_second\": 7.27, \"eval_ppl_holdout\": 17.688, \"eval_loss\": 2.8729, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15\", \"b_star_count\": 24412, \"b_star_mean\": 0.3923, \"b_star_median\": 0.1707, \"b_star_std\": 0.8821, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0, \"b_star_p75\": 0.4366, \"b_star_pct_zero\": 29.1, \"b_star_pct_below_0.5\": 78.4, \"b_star_pct_0.5_to_1\": 12.9, \"b_star_pct_1_to_2\": 5.7, \"b_star_pct_above_2\": 2.9}}, \"adaptive_seed456\": {\"metrics\": {\"train_loss\": 9.2354, \"train_runtime_s\": 13130.09, \"total_steps\": 6103, \"train_samples_per_second\": 7.437, \"train_steps_per_second\": 0.465, \"epoch\": 0.26, \"weighting_method\": \"adaptive\", \"tau\": 0.8, \"n_min\": 3, \"contamination_ratio\": 0.4, \"b_star\": \"per-batch adaptive (0.0-3.8)\", \"alpha_eff_range\": \"0.09-0.80 (capped at tau)\", \"eval_ppl_holdout\": 17.6419, \"eval_loss_holdout\": 2.8703, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.64/4080000 from inline eval\"}}, \"adaptive_seed123\": {\"metrics\": {\"train_loss\": 9.2665, \"train_runtime_s\": 13197.18, \"total_steps\": 6103, \"train_samples_per_second\": 7.399, \"train_steps_per_second\": 0.462, \"epoch\": 0.26, \"weighting_method\": \"adaptive\", \"tau\": 0.8, \"n_min\": 3, \"contamination_ratio\": 0.4, \"b_star\": \"per-batch adaptive (0.0-3.8)\", \"alpha_eff_range\": \"0.04-0.80 (capped at tau)\", \"eval_ppl_holdout\": 17.6308, \"eval_loss_holdout\": 2.8696, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.63/4080000 from inline eval\"}}, \"adaptive_seed42\": {\"metrics\": {\"train_loss\": 9.2665, \"train_runtime_s\": 13115.09, \"total_steps\": 6103, \"train_samples_per_second\": 7.445, \"train_steps_per_second\": 0.465, \"epoch\": 0.26, \"weighting_method\": \"adaptive\", \"tau\": 0.8, \"n_min\": 3, \"contamination_ratio\": 0.4, \"b_star\": \"per-batch adaptive (0.0-3.8)\", \"alpha_eff_range\": \"0.03-0.80 (capped at tau)\", \"eval_ppl_holdout\": 17.644, \"eval_loss_holdout\": 2.8704, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; confirmed unchanged from prior post-hoc (was 17.644/4077068)\"}}, \"uniform_seed456\": {\"metrics\": {\"train_loss\": 7.2895, \"total_steps\": 6103, \"train_duration_s\": 11974, \"eval_ppl_holdout\": 17.7015, \"eval_loss_holdout\": 2.8737, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.70/4080000 from inline eval\"}}, \"uniform_seed123\": {\"metrics\": {\"train_loss\": 7.3121, \"total_steps\": 6103, \"train_duration_s\": 11994, \"eval_ppl_holdout\": 17.6861, \"eval_loss_holdout\": 2.8728, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.69/4080000 from inline eval\"}}, \"uniform_seed42\": {\"metrics\": {\"train_loss\": 7.3104, \"total_steps\": 6103, \"train_duration_s\": 11946, \"eval_ppl_holdout\": 17.6939, \"eval_loss_holdout\": 2.8732, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.69/4080000 from inline eval\"}}, \"detector_modernbert\": {}, \"nmin1_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.789, \"eval_loss\": 2.8786, \"eval_holdout_tokens\": 4077068, \"b_star_mean\": 7.197, \"b_star_median\": 1.746, \"b_star_std\": 8.374, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.803, \"b_star_p75\": 20, \"b_star_zero_frac\": 0.019, \"b_star_pct_below_0.5\": 13.1, \"b_star_pct_0.5_to_1\": 19.1, \"b_star_pct_1_to_2\": 21.1, \"b_star_pct_above_2\": 46.7, \"b_star_count\": 24412, \"alpha_eff_mean\": 0.714, \"alpha_eff_median\": 0.8}}, \"golden_ratio_seed42\": {\"metrics\": {\"eval_ppl_holdout\": 17.654, \"eval_loss\": 2.871, \"train_loss\": 2.1145, \"train_loss_last500\": 2.109, \"eval_holdout_tokens\": 4077068, \"total_steps\": 6103, \"train_runtime_s\": 13442, \"gpu_hours\": 3.73}}, \"tau_0.6_seed42\": {}, \"grid_b_low_seed42\": {}, \"grid_b1_5_seed456\": {\"metrics\": {\"train_loss\": 10.435, \"total_steps\": 6103, \"train_runtime_s\": 12950.16, \"gpu_hours\": 3.67, \"train_samples_per_second\": 7.54, \"eval_loss\": 2.8741, \"eval_ppl_holdout\": 17.71, \"eval_holdout_tokens\": 4077068, \"eval_loss_holdout\": 2.875, \"eval_tokens\": 5004058}}, \"grid_b1_0_seed456\": {\"metrics\": {\"train_loss\": 10.178, \"total_steps\": 6103, \"train_runtime_s\": 12963.87, \"gpu_hours\": 3.67, \"train_samples_per_second\": 7.532, \"eval_loss\": 2.8725, \"eval_ppl_holdout\": 17.68, \"eval_holdout_tokens\": 4077068, \"eval_loss_holdout\": 2.8734, \"eval_tokens\": 5004058}}, \"grid_b0_5_seed456\": {\"metrics\": {\"train_loss\": 9.5622, \"total_steps\": 6103, \"train_runtime_s\": 12953.96, \"gpu_hours\": 3.6, \"train_samples_per_second\": 7.538, \"eval_loss\": 2.8705, \"eval_ppl_holdout\": 17.65, \"eval_holdout_tokens\": 4077068}}, \"grid_b_seed42_batch\": {\"metrics\": {\"b_values\": [0.5, 1, 1.5, 2, 3, 5], \"b0_5_train_loss\": 9.598, \"b0_5_completed\": true, \"b1_0_completed\": true, \"b1_5_completed\": true, \"b2_0_current_step\": 5149, \"b2_0_total_steps\": 6103, \"completed_b_values\": [0.5, 1, 1.5, 2, 3], \"current_b\": 5, \"total_steps\": 6103, \"current_step\": 3422, \"b5_0_progress_pct\": 56, \"eta_minutes\": 95, \"b2_0_completed\": true, \"b2_0_train_loss\": 10.621, \"b2_0_train_runtime_s\": 13034, \"b3_0_completed\": true, \"b3_0_train_loss\": 10.754, \"b3_0_train_runtime_s\": 13036, \"all_completed\": true, \"b1_0_train_loss\": 10.223, \"b1_5_train_loss\": 10.485, \"b5_0_train_loss\": 10.858, \"b0_5_runtime_s\": 13036, \"b1_0_runtime_s\": 12968, \"b1_5_runtime_s\": 14789, \"b2_0_runtime_s\": 13034, \"b3_0_runtime_s\": 13036, \"b5_0_runtime_s\": 13115, \"note\": \"eval_ppl missing - no --eval_data_path in batch script, post-hoc eval pending\", \"b0_5_eval_ppl\": 17.651, \"b1_0_eval_ppl\": 17.692, \"b1_5_eval_ppl\": 17.718, \"b2_0_eval_ppl\": 17.741, \"b3_0_eval_ppl\": 17.774, \"b5_0_eval_ppl\": 17.818, \"eval_holdout_tokens\": 4077068, \"best_b\": 0.5, \"best_eval_ppl\": 17.651}}, \"diagnostic_contamination100\": {}, \"detector_tfidf_lr\": {\"metrics\": {\"auc\": 0.939, \"accuracy\": 0.858, \"ece_raw\": 0.24, \"ece_calibrated\": 0.048, \"temperature_T\": 0.204, \"q_score_mean\": 0.6, \"q_score_std\": 0.374, \"q_score_median\": 0.707, \"mid_range_ratio\": 0.463}}}, \"count\": 180, \"total\": 180, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5567}}"
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
Let me analyze the results. I need to find experiments that have the old format downstream metrics (without suffix like `_acc_norm` or `_acc`).

Experiments with old format (no suffix):
1. `adaptive_rho06_tau07_seed42` - has `downstream_arc_easy`, `downstream_arc_challenge`, `downstream_hellaswag`, `downstream_piqa`, `downstream_winogrande`
2. `adaptive_rho06_tau07_seed456` - same old format


3. `adaptive_rho06_tau07_seed123` - same old format
4. `adaptive_fix_seed42` - same old format

All other experiments with downstream metrics use the new format (`_acc_norm` / `_acc`). I need to update these 4 experiments by appending the appropriate suffixes to their metric names, mapping each old metric to its new format with `_acc_norm`.

Now I'm thinking through how to use the `update_registry` tool. It updates a single field at a time, and I'm wondering whether I can pass the entire `metrics` dict or if I need to update individual metric fields. The tool description mentions field names like 'status' and 'hypothesis', so `metrics` might work as a field name, but I'm not certain if it will merge with existing values or replace them entirely. Let me consider whether I should update the whole metrics object or take a more granular approach to be safe.

For each experiment, I need to rename the downstream metrics by adding the `_acc_norm` suffix to the field names while keeping the existing values intact. Let me map out what needs to change for the first experiment. Now I'm looking at the metrics for the adaptive_rho06_tau07_seed123 configuration, which shows similar perplexity scores to the previous seed variant but with slightly different downstream task performance, particularly lower arc_easy accuracy. Moving into the adaptive_fix_seed42 results, I can see the holdout perplexity is slightly better at 17.65, and the arc_easy score is notably higher at 0.6157.

I need to figure out whether updating the metrics field will replace the entire dictionary or merge with existing values.  To be safe, I'll assume it replaces everything, so I need to include all the current fields along with the renamed ones while removing the old field names. Now I'll prepare the update calls for all four experiments in parallel since they don't depend on each other.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1f4ce05a-24d6-4596-8122-cc9aa92b3d90",
  "uuid": "757b81cb-150b-481c-a8e3-173601480ab0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FCq22pf6LgEVZXUdoidP5i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20815,
      "cache_read_input_tokens": 24541,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20815
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

识别到 4 个实验使用旧格式字段名：
- `adaptive_rho06_tau07_seed42`
- `adaptive_rho06_tau07_seed456`
- `adaptive_rho06_tau07_seed123`
- `adaptive_fix_seed42`

现在批量修正，每个实验更新完整的 metrics dict。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1f4ce05a-24d6-4596-8122-cc9aa92b3d90",
  "uuid": "3455bc6a-1f38-44a0-97f0-eae57df4cec1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FCq22pf6LgEVZXUdoidP5i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20815,
      "cache_read_input_tokens": 24541,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20815
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_017MHpJoAGP1UPRpCfC6Eh7o`</summary>

```json
{
  "exp_id": "adaptive_rho06_tau07_seed42",
  "field": "metrics",
  "value": {
    "holdout_ppl": 17.735,
    "eval_ppl_openwebtext": 18.408,
    "eval_ppl_wikipedia": 15.355,
    "downstream_arc_easy_acc_norm": 0.6132,
    "downstream_arc_challenge_acc_norm": 0.3422,
    "downstream_hellaswag_acc_norm": 0.4807,
    "downstream_piqa_acc_norm": 0.6861,
    "downstream_winogrande_acc": 0.5793,
    "downstream_mean": 0.5403
  },
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1f4ce05a-24d6-4596-8122-cc9aa92b3d90",
  "uuid": "2af1d78e-667b-4c8c-b919-0ef1857f0dae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FCq22pf6LgEVZXUdoidP5i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20815,
      "cache_read_input_tokens": 24541,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20815
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

_source line 13 · 2026-05-20T08:58:48.934Z_

<details><summary>↩ Tool result · `toolu_017MHpJoAGP1UPRpCfC6Eh7o`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"adaptive_rho06_tau07_seed42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T03:19:02.608Z\", \"updated_at\": \"2026-05-20T08:58:48.541Z\", \"hypothesis\": \"Pure adaptive retraining at ρ=0.6, τ=0.7, seed=42. Replaces rho06_tau07_seed42 which was contaminated by hybrid checkpoint. From-scratch training with base Qwen3-0.6B to clean output dir. If PPL < 17.73 (ρ=0.6 τ=0.8 baseline), validates τ=0.7 as universal default across contamination levels.\", \"parent\": \"rho06_tau07_seed42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path /root/autodl-tmp/provenance_weight_training/data/scored_data_rho06.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/adaptive_rho06_tau07_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.6 --tau 0.7 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model --save_steps 6103\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:0\"], \"pid\": \"383864\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_rho06_tau07_seed42.log\", \"submitted_at\": \"2026-05-20T03:31:32.965Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/provenance_weight_training/data/scored_data_rho06.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"N/A (from-scratch training)\", \"eval_data\": \"N/A (training experiment)\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/adaptive_rho06_tau07_seed42/final\", \"train_loss\": 9.358, \"train_runtime_hours\": 3.74, \"wall_clock_seconds\": 16929.0, \"gpu_hours\": 4.7}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T08:13:41.995Z\", \"metrics\": {\"holdout_ppl\": 17.735, \"eval_ppl_openwebtext\": 18.408, \"eval_ppl_wikipedia\": 15.355, \"downstream_arc_easy_acc_norm\": 0.6132, \"downstream_arc_challenge_acc_norm\": 0.3422, \"downstream_hellaswag_acc_norm\": 0.4807, \"downstream_piqa_acc_norm\": 0.6861, \"downstream_winogrande_acc\": 0.5793, \"downstream_mean\": 0.5403}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0007}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1f4ce05a-24d6-4596-8122-cc9aa92b3d90",
  "uuid": "5edd4d40-1c50-4a32-9717-d3ca161d190e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"adaptive_rho06_tau07_seed42\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T03:19:02.608Z\\\", \\\"updated_at\\\": \\\"2026-05-20T08:58:48.541Z\\\", \\\"hypothesis\\\": \\\"Pure adaptive retraining at ρ=0.6, τ=0.7, seed=42. Replaces rho06_tau07_seed42 which was contaminated by hybrid checkpoint. From-scratch training with base Qwen3-0.6B to clean output dir. If PPL < 17.73 (ρ=0.6 τ=0.8 baseline), validates τ=0.7 as universal default across contamination levels.\\\", \\\"parent\\\": \\\"rho06_tau07_seed42\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path /root/autodl-tmp/provenance_weight_training/data/scored_data_rho06.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/adaptive_rho06_tau07_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.6 --tau 0.7 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model --save_steps 6103\\\\\\\"\\\", \\\"server\\\": \\\"westd-41312\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"383864\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/adaptive_rho06_tau07_seed42.log\\\", \\\"submitted_at\\\": \\\"2026-05-20T03:31:32.965Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/provenance_weight_training/data/scored_data_rho06.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"N/A (from-scratch training)\\\", \\\"eval_data\\\": \\\"N/A (training experiment)\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/provenance_weight_training/output/models/adaptive_rho06_tau07_seed42/final\\\", \\\"train_loss\\\": 9.358, \\\"train_runtime_hours\\\": 3.74, \\\"wall_clock_seconds\\\": 16929.0, \\\"gpu_hours\\\": 4.7}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-20T08:13:41.995Z\\\", \\\"metrics\\\": {\\\"holdout_ppl\\\": 17.735, \\\"eval_ppl_openwebtext\\\": 18.408, \\\"eval_ppl_wikipedia\\\": 15.355, \\\"downstream_arc_easy_acc_norm\\\": 0.6132, \\\"downstream_arc_challenge_acc_norm\\\": 0.3422, \\\"downstream_hellaswag_acc_norm\\\": 0.4807, \\\"downstream_piqa_acc_norm\\\": 0.6861, \\\"downstream_winogrande_acc\\\": 0.5793, \\\"downstream_mean\\\": 0.5403}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.0007}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"adaptive_rho06_tau07_seed42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T03:19:02.608Z\", \"updated_at\": \"2026-05-20T08:58:48.541Z\", \"hypothesis\": \"Pure adaptive retraining at ρ=0.6, τ=0.7, seed=42. Replaces rho06_tau07_seed42 which was contaminated by hybrid checkpoint. From-scratch training with base Qwen3-0.6B to clean output dir. If PPL < 17.73 (ρ=0.6 τ=0.8 baseline), validates τ=0.7 as universal default across contamination levels.\", \"parent\": \"rho06_tau07_seed42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path /root/autodl-tmp/provenance_weight_training/data/scored_data_rho06.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/adaptive_rho06_tau07_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.6 --tau 0.7 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model --save_steps 6103\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:0\"], \"pid\": \"383864\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_rho06_tau07_seed42.log\", \"submitted_at\": \"2026-05-20T03:31:32.965Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/provenance_weight_training/data/scored_data_rho06.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"N/A (from-scratch training)\", \"eval_data\": \"N/A (training experiment)\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/adaptive_rho06_tau07_seed42/final\", \"train_loss\": 9.358, \"train_runtime_hours\": 3.74, \"wall_clock_seconds\": 16929.0, \"gpu_hours\": 4.7}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T08:13:41.995Z\", \"metrics\": {\"holdout_ppl\": 17.735, \"eval_ppl_openwebtext\": 18.408, \"eval_ppl_wikipedia\": 15.355, \"downstream_arc_easy_acc_norm\": 0.6132, \"downstream_arc_challenge_acc_norm\": 0.3422, \"downstream_hellaswag_acc_norm\": 0.4807, \"downstream_piqa_acc_norm\": 0.6861, \"downstream_winogrande_acc\": 0.5793, \"downstream_mean\": 0.5403}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0007}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01Si2wtLjjJGuQbRX41znTYh`</summary>

```json
{
  "exp_id": "adaptive_rho06_tau07_seed456",
  "field": "metrics",
  "value": {
    "holdout_ppl": 17.732,
    "eval_ppl_openwebtext": 18.411,
    "eval_ppl_wikipedia": 15.424,
    "downstream_arc_easy_acc_norm": 0.6128,
    "downstream_arc_challenge_acc_norm": 0.3456,
    "downstream_hellaswag_acc_norm": 0.4806,
    "downstream_piqa_acc_norm": 0.6866,
    "downstream_winogrande_acc": 0.562,
    "downstream_mean": 0.5375
  },
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1f4ce05a-24d6-4596-8122-cc9aa92b3d90",
  "uuid": "02293623-13a3-4455-ae71-d3d8e211fd8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FCq22pf6LgEVZXUdoidP5i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20815,
      "cache_read_input_tokens": 24541,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20815
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

_source line 15 · 2026-05-20T08:58:50.722Z_

<details><summary>↩ Tool result · `toolu_01Si2wtLjjJGuQbRX41znTYh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"adaptive_rho06_tau07_seed456\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T03:22:16.979Z\", \"updated_at\": \"2026-05-20T08:58:50.338Z\", \"hypothesis\": \"Pure adaptive training at ρ=0.6, τ=0.7, seed=456. Third seed completing clean ρ=0.6 τ=0.7 3-seed set. From-scratch Qwen3-0.6B, no checkpoint reuse. Together with seed42/123, enables paired comparison against ρ=0.6 τ=0.8.\", \"parent\": \"rho06_tau07_seed42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path /root/autodl-tmp/provenance_weight_training/data/scored_data_rho06.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/adaptive_rho06_tau07_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.6 --tau 0.7 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 456 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model --save_steps 6103\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:2\"], \"pid\": \"384114\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_rho06_tau07_seed456.log\", \"submitted_at\": \"2026-05-20T03:31:37.645Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/provenance_weight_training/data/scored_data_rho06.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"checkpoint_source\": \"N/A (from-scratch training)\", \"eval_data\": \"N/A (training experiment)\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/adaptive_rho06_tau07_seed456/final\", \"train_loss\": 9.342, \"train_runtime_hours\": 3.72, \"wall_clock_seconds\": 16928.3, \"gpu_hours\": 4.7}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T08:13:45.922Z\", \"metrics\": {\"holdout_ppl\": 17.732, \"eval_ppl_openwebtext\": 18.411, \"eval_ppl_wikipedia\": 15.424, \"downstream_arc_easy_acc_norm\": 0.6128, \"downstream_arc_challenge_acc_norm\": 0.3456, \"downstream_hellaswag_acc_norm\": 0.4806, \"downstream_piqa_acc_norm\": 0.6866, \"downstream_winogrande_acc\": 0.562, \"downstream_mean\": 0.5375}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8733}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1f4ce05a-24d6-4596-8122-cc9aa92b3d90",
  "uuid": "c6b1a010-3176-4c33-b193-ae65fdd60dea",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"adaptive_rho06_tau07_seed456\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T03:22:16.979Z\\\", \\\"updated_at\\\": \\\"2026-05-20T08:58:50.338Z\\\", \\\"hypothesis\\\": \\\"Pure adaptive training at ρ=0.6, τ=0.7, seed=456. Third seed completing clean ρ=0.6 τ=0.7 3-seed set. From-scratch Qwen3-0.6B, no checkpoint reuse. Together with seed42/123, enables paired comparison against ρ=0.6 τ=0.8.\\\", \\\"parent\\\": \\\"rho06_tau07_seed42\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path /root/autodl-tmp/provenance_weight_training/data/scored_data_rho06.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/adaptive_rho06_tau07_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.6 --tau 0.7 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 456 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model --save_steps 6103\\\\\\\"\\\", \\\"server\\\": \\\"westd-41312\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"384114\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/adaptive_rho06_tau07_seed456.log\\\", \\\"submitted_at\\\": \\\"2026-05-20T03:31:37.645Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/provenance_weight_training/data/scored_data_rho06.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 456, \\\"checkpoint_source\\\": \\\"N/A (from-scratch training)\\\", \\\"eval_data\\\": \\\"N/A (training experiment)\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/provenance_weight_training/output/models/adaptive_rho06_tau07_seed456/final\\\", \\\"train_loss\\\": 9.342, \\\"train_runtime_hours\\\": 3.72, \\\"wall_clock_seconds\\\": 16928.3, \\\"gpu_hours\\\": 4.7}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-20T08:13:45.922Z\\\", \\\"metrics\\\": {\\\"holdout_ppl\\\": 17.732, \\\"eval_ppl_openwebtext\\\": 18.411, \\\"eval_ppl_wikipedia\\\": 15.424, \\\"downstream_arc_easy_acc_norm\\\": 0.6128, \\\"downstream_arc_challenge_acc_norm\\\": 0.3456, \\\"downstream_hellaswag_acc_norm\\\": 0.4806, \\\"downstream_piqa_acc_norm\\\": 0.6866, \\\"downstream_winogrande_acc\\\": 0.562, \\\"downstream_mean\\\": 0.5375}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.8733}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"adaptive_rho06_tau07_seed456\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T03:22:16.979Z\", \"updated_at\": \"2026-05-20T08:58:50.338Z\", \"hypothesis\": \"Pure adaptive training at ρ=0.6, τ=0.7, seed=456. Third seed completing clean ρ=0.6 τ=0.7 3-seed set. From-scratch Qwen3-0.6B, no checkpoint reuse. Together with seed42/123, enables paired comparison against ρ=0.6 τ=0.8.\", \"parent\": \"rho06_tau07_seed42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path /root/autodl-tmp/provenance_weight_training/data/scored_data_rho06.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/adaptive_rho06_tau07_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.6 --tau 0.7 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 456 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model --save_steps 6103\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:2\"], \"pid\": \"384114\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_rho06_tau07_seed456.log\", \"submitted_at\": \"2026-05-20T03:31:37.645Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/provenance_weight_training/data/scored_data_rho06.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"checkpoint_source\": \"N/A (from-scratch training)\", \"eval_data\": \"N/A (training experiment)\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/adaptive_rho06_tau07_seed456/final\", \"train_loss\": 9.342, \"train_runtime_hours\": 3.72, \"wall_clock_seconds\": 16928.3, \"gpu_hours\": 4.7}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T08:13:45.922Z\", \"metrics\": {\"holdout_ppl\": 17.732, \"eval_ppl_openwebtext\": 18.411, \"eval_ppl_wikipedia\": 15.424, \"downstream_arc_easy_acc_norm\": 0.6128, \"downstream_arc_challenge_acc_norm\": 0.3456, \"downstream_hellaswag_acc_norm\": 0.4806, \"downstream_piqa_acc_norm\": 0.6866, \"downstream_winogrande_acc\": 0.562, \"downstream_mean\": 0.5375}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8733}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01YFFLN6CXxCXkC7axbiErSi`</summary>

```json
{
  "exp_id": "adaptive_rho06_tau07_seed123",
  "field": "metrics",
  "value": {
    "holdout_ppl": 17.727,
    "eval_ppl_openwebtext": 18.385,
    "eval_ppl_wikipedia": 15.329,
    "downstream_arc_easy_acc_norm": 0.5951,
    "downstream_arc_challenge_acc_norm": 0.3422,
    "downstream_hellaswag_acc_norm": 0.4811,
    "downstream_piqa_acc_norm": 0.6866,
    "downstream_winogrande_acc": 0.5754,
    "downstream_mean": 0.5361
  },
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1f4ce05a-24d6-4596-8122-cc9aa92b3d90",
  "uuid": "27525b46-a500-4d4c-81b4-b8db3e197e0d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FCq22pf6LgEVZXUdoidP5i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20815,
      "cache_read_input_tokens": 24541,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20815
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

_source line 17 · 2026-05-20T08:58:52.662Z_

<details><summary>↩ Tool result · `toolu_01YFFLN6CXxCXkC7axbiErSi`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"adaptive_rho06_tau07_seed123\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T03:22:15.719Z\", \"updated_at\": \"2026-05-20T08:58:52.243Z\", \"hypothesis\": \"Pure adaptive training at ρ=0.6, τ=0.7, seed=123. Second seed for clean ρ=0.6 τ=0.7 3-seed set. From-scratch Qwen3-0.6B, no checkpoint reuse. Validates τ=0.7 as universal default across contamination levels.\", \"parent\": \"rho06_tau07_seed42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path /root/autodl-tmp/provenance_weight_training/data/scored_data_rho06.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/adaptive_rho06_tau07_seed123 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.6 --tau 0.7 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 123 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model --save_steps 6103\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:1\"], \"pid\": \"383947\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_rho06_tau07_seed123.log\", \"submitted_at\": \"2026-05-20T03:31:35.365Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/provenance_weight_training/data/scored_data_rho06.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"checkpoint_source\": \"N/A (from-scratch training)\", \"eval_data\": \"N/A (training experiment)\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/adaptive_rho06_tau07_seed123/final\", \"train_loss\": 9.352, \"train_runtime_hours\": 3.74, \"wall_clock_seconds\": 16928.5, \"gpu_hours\": 4.7}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T08:13:43.870Z\", \"metrics\": {\"holdout_ppl\": 17.727, \"eval_ppl_openwebtext\": 18.385, \"eval_ppl_wikipedia\": 15.329, \"downstream_arc_easy_acc_norm\": 0.5951, \"downstream_arc_challenge_acc_norm\": 0.3422, \"downstream_hellaswag_acc_norm\": 0.4811, \"downstream_piqa_acc_norm\": 0.6866, \"downstream_winogrande_acc\": 0.5754, \"downstream_mean\": 0.5361}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9525}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1f4ce05a-24d6-4596-8122-cc9aa92b3d90",
  "uuid": "1724459e-e42a-4879-9153-ece73dfa27ee",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"adaptive_rho06_tau07_seed123\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T03:22:15.719Z\\\", \\\"updated_at\\\": \\\"2026-05-20T08:58:52.243Z\\\", \\\"hypothesis\\\": \\\"Pure adaptive training at ρ=0.6, τ=0.7, seed=123. Second seed for clean ρ=0.6 τ=0.7 3-seed set. From-scratch Qwen3-0.6B, no checkpoint reuse. Validates τ=0.7 as universal default across contamination levels.\\\", \\\"parent\\\": \\\"rho06_tau07_seed42\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path /root/autodl-tmp/provenance_weight_training/data/scored_data_rho06.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/adaptive_rho06_tau07_seed123 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.6 --tau 0.7 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 123 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model --save_steps 6103\\\\\\\"\\\", \\\"server\\\": \\\"westd-41312\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"383947\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/adaptive_rho06_tau07_seed123.log\\\", \\\"submitted_at\\\": \\\"2026-05-20T03:31:35.365Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/provenance_weight_training/data/scored_data_rho06.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 123, \\\"checkpoint_source\\\": \\\"N/A (from-scratch training)\\\", \\\"eval_data\\\": \\\"N/A (training experiment)\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/provenance_weight_training/output/models/adaptive_rho06_tau07_seed123/final\\\", \\\"train_loss\\\": 9.352, \\\"train_runtime_hours\\\": 3.74, \\\"wall_clock_seconds\\\": 16928.5, \\\"gpu_hours\\\": 4.7}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-20T08:13:43.870Z\\\", \\\"metrics\\\": {\\\"holdout_ppl\\\": 17.727, \\\"eval_ppl_openwebtext\\\": 18.385, \\\"eval_ppl_wikipedia\\\": 15.329, \\\"downstream_arc_easy_acc_norm\\\": 0.5951, \\\"downstream_arc_challenge_acc_norm\\\": 0.3422, \\\"downstream_hellaswag_acc_norm\\\": 0.4811, \\\"downstream_piqa_acc_norm\\\": 0.6866, \\\"downstream_winogrande_acc\\\": 0.5754, \\\"downstream_mean\\\": 0.5361}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.9525}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"adaptive_rho06_tau07_seed123\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T03:22:15.719Z\", \"updated_at\": \"2026-05-20T08:58:52.243Z\", \"hypothesis\": \"Pure adaptive training at ρ=0.6, τ=0.7, seed=123. Second seed for clean ρ=0.6 τ=0.7 3-seed set. From-scratch Qwen3-0.6B, no checkpoint reuse. Validates τ=0.7 as universal default across contamination levels.\", \"parent\": \"rho06_tau07_seed42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path /root/autodl-tmp/provenance_weight_training/data/scored_data_rho06.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/adaptive_rho06_tau07_seed123 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.6 --tau 0.7 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 123 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model --save_steps 6103\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:1\"], \"pid\": \"383947\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_rho06_tau07_seed123.log\", \"submitted_at\": \"2026-05-20T03:31:35.365Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/provenance_weight_training/data/scored_data_rho06.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"checkpoint_source\": \"N/A (from-scratch training)\", \"eval_data\": \"N/A (training experiment)\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/adaptive_rho06_tau07_seed123/final\", \"train_loss\": 9.352, \"train_runtime_hours\": 3.74, \"wall_clock_seconds\": 16928.5, \"gpu_hours\": 4.7}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T08:13:43.870Z\", \"metrics\": {\"holdout_ppl\": 17.727, \"eval_ppl_openwebtext\": 18.385, \"eval_ppl_wikipedia\": 15.329, \"downstream_arc_easy_acc_norm\": 0.5951, \"downstream_arc_challenge_acc_norm\": 0.3422, \"downstream_hellaswag_acc_norm\": 0.4811, \"downstream_piqa_acc_norm\": 0.6866, \"downstream_winogrande_acc\": 0.5754, \"downstream_mean\": 0.5361}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9525}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01VaZsjDoV3juqSmBX9SszK4`</summary>

```json
{
  "exp_id": "adaptive_fix_seed42",
  "field": "metrics",
  "value": {
    "eval_ppl_holdout": 17.6527,
    "downstream_arc_easy_acc_norm": 0.6157,
    "downstream_arc_challenge_acc_norm": 0.343,
    "downstream_hellaswag_acc_norm": 0.4785,
    "downstream_piqa_acc_norm": 0.6866,
    "downstream_winogrande_acc": 0.5777,
    "downstream_mean": 0.5403,
    "downstream_eval_method": "lm_eval 0.4.11, 0-shot, float16",
    "eval_ppl_openwebtext": 18.424,
    "eval_ppl_wikipedia": 15.473
  },
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1f4ce05a-24d6-4596-8122-cc9aa92b3d90",
  "uuid": "56fb2bcf-c430-493d-9a73-c59d5db2505c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FCq22pf6LgEVZXUdoidP5i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20815,
      "cache_read_input_tokens": 24541,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20815
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

_source line 19 · 2026-05-20T08:58:54.313Z_

<details><summary>↩ Tool result · `toolu_01VaZsjDoV3juqSmBX9SszK4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"adaptive_fix_seed42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-14T13:32:30.463Z\", \"updated_at\": \"2026-05-20T08:58:53.948Z\", \"hypothesis\": \"D012 n_min fix (3→2, batch_size//2): adaptive b* with corrected ESS constraint achieves meaningful improvement over uniform baseline (PPL=17.69) for seed=42. Parent: adaptive_seed42 (PPL=17.69, n_min=3 bug)\", \"parent\": \"adaptive_seed42\", \"notes\": \"最终清理后重提交。从 checkpoint-1500 恢复，无 inline eval。PID=126801\", \"failure_reason\": \"\", \"completed_at\": \"\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"D012 代码验证通过（n_min=max(2,batch_size//2), 无EMA, import OK）。等 GPU 释放后提交。\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T17:38:26.312269+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T20:39:45.953045+00:00\"}]}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && bash scripts/run_adaptive_fix_seed42.sh\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:0\"], \"pid\": \"109927\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_fix_seed42.log\", \"submitted_at\": \"2026-05-17T15:01:06.089Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T20:39:44.942Z\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_ppl_holdout\": 17.6527, \"downstream_arc_easy_acc_norm\": 0.6157, \"downstream_arc_challenge_acc_norm\": 0.343, \"downstream_hellaswag_acc_norm\": 0.4785, \"downstream_piqa_acc_norm\": 0.6866, \"downstream_winogrande_acc\": 0.5777, \"downstream_mean\": 0.5403, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16\", \"eval_ppl_openwebtext\": 18.424, \"eval_ppl_wikipedia\": 15.473}, \"checkpoint_path\": \"output/models/adaptive_fix_seed42/final\", \"eval_ppl_openwebtext\": 18.42, \"eval_ppl_wikipedia\": 15.47}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8983}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1f4ce05a-24d6-4596-8122-cc9aa92b3d90",
  "uuid": "a7658d6b-3669-4671-8294-b98cc8dcc6c9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"adaptive_fix_seed42\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 2, \\\"created_at\\\": \\\"2026-05-14T13:32:30.463Z\\\", \\\"updated_at\\\": \\\"2026-05-20T08:58:53.948Z\\\", \\\"hypothesis\\\": \\\"D012 n_min fix (3→2, batch_size//2): adaptive b* with corrected ESS constraint achieves meaningful improvement over uniform baseline (PPL=17.69) for seed=42. Parent: adaptive_seed42 (PPL=17.69, n_min=3 bug)\\\", \\\"parent\\\": \\\"adaptive_seed42\\\", \\\"notes\\\": \\\"最终清理后重提交。从 checkpoint-1500 恢复，无 inline eval。PID=126801\\\", \\\"failure_reason\\\": \\\"\\\", \\\"completed_at\\\": \\\"\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"D012 代码验证通过（n_min=max(2,batch_size//2), 无EMA, import OK）。等 GPU 释放后提交。\\\"}, \\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-14T17:38:26.312269+00:00\\\"}, {\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-14T20:39:45.953045+00:00\\\"}]}, \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && bash scripts/run_adaptive_fix_seed42.sh\\\\\\\"\\\", \\\"server\\\": \\\"westd-41312\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"109927\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/adaptive_fix_seed42.log\\\", \\\"submitted_at\\\": \\\"2026-05-17T15:01:06.089Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-14T20:39:44.942Z\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.6527, \\\"downstream_arc_easy_acc_norm\\\": 0.6157, \\\"downstream_arc_challenge_acc_norm\\\": 0.343, \\\"downstream_hellaswag_acc_norm\\\": 0.4785, \\\"downstream_piqa_acc_norm\\\": 0.6866, \\\"downstream_winogrande_acc\\\": 0.5777, \\\"downstream_mean\\\": 0.5403, \\\"downstream_eval_method\\\": \\\"lm_eval 0.4.11, 0-shot, float16\\\", \\\"eval_ppl_openwebtext\\\": 18.424, \\\"eval_ppl_wikipedia\\\": 15.473}, \\\"checkpoint_path\\\": \\\"output/models/adaptive_fix_seed42/final\\\", \\\"eval_ppl_openwebtext\\\": 18.42, \\\"eval_ppl_wikipedia\\\": 15.47}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.8983}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"adaptive_fix_seed42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-14T13:32:30.463Z\", \"updated_at\": \"2026-05-20T08:58:53.948Z\", \"hypothesis\": \"D012 n_min fix (3→2, batch_size//2): adaptive b* with corrected ESS constraint achieves meaningful improvement over uniform baseline (PPL=17.69) for seed=42. Parent: adaptive_seed42 (PPL=17.69, n_min=3 bug)\", \"parent\": \"adaptive_seed42\", \"notes\": \"最终清理后重提交。从 checkpoint-1500 恢复，无 inline eval。PID=126801\", \"failure_reason\": \"\", \"completed_at\": \"\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"D012 代码验证通过（n_min=max(2,batch_size//2), 无EMA, import OK）。等 GPU 释放后提交。\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T17:38:26.312269+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T20:39:45.953045+00:00\"}]}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && bash scripts/run_adaptive_fix_seed42.sh\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:0\"], \"pid\": \"109927\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_fix_seed42.log\", \"submitted_at\": \"2026-05-17T15:01:06.089Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T20:39:44.942Z\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_ppl_holdout\": 17.6527, \"downstream_arc_easy_acc_norm\": 0.6157, \"downstream_arc_challenge_acc_norm\": 0.343, \"downstream_hellaswag_acc_norm\": 0.4785, \"downstream_piqa_acc_norm\": 0.6866, \"downstream_winogrande_acc\": 0.5777, \"downstream_mean\": 0.5403, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16\", \"eval_ppl_openwebtext\": 18.424, \"eval_ppl_wikipedia\": 15.473}, \"checkpoint_path\": \"output/models/adaptive_fix_seed42/final\", \"eval_ppl_openwebtext\": 18.42, \"eval_ppl_wikipedia\": 15.47}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8983}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 20_

全部更新成功。

### 汇报

**修正的实验（4 个）：**

| exp_id | 旧字段名 | 新字段名 |
|--------|---------|---------|
| `adaptive_rho06_tau07_seed42` | `downstream_arc_easy` | `downstream_arc_easy_acc_norm` |
| `adaptive_rho06_tau07_seed456` | `downstream_arc_challenge` | `downstream_arc_challenge_acc_norm` |
| `adaptive_rho06_tau07_seed123` | `downstream_hellaswag` | `downstream_hellaswag_acc_norm` |
| `adaptive_fix_seed42` | `downstream_piqa` | `downstream_piqa_acc_norm` |
| | `downstream_winogrande` | `downstream_winogrande_acc` |

**字段映射（每个实验均应用全部 5 项重命名）：**
- `downstream_arc_easy` → `downstream_arc_easy_acc_norm`
- `downstream_arc_challenge` → `downstream_arc_challenge_acc_norm`
- `downstream_hellaswag` → `downstream_hellaswag_acc_norm`
- `downstream_piqa` → `downstream_piqa_acc_norm`
- `downstream_winogrande` → `downstream_winogrande_acc`
- `downstream_mean` — 保持不变

**共修正 4 个实验，每个实验 5 个字段重命名，值不变。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1f4ce05a-24d6-4596-8122-cc9aa92b3d90",
  "uuid": "d60a5adf-46bd-4558-9b53-e30d76aadbfc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HcSQRyKaE8wsts6peAej8v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6620,
      "cache_read_input_tokens": 45356,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6620
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

_source line 21_

全部更新成功。

### 汇报

**修正的实验（4 个）：**

| exp_id | 旧字段名 | 新字段名 |
|--------|---------|---------|
| `adaptive_rho06_tau07_seed42` | `downstream_arc_easy` | `downstream_arc_easy_acc_norm` |
| `adaptive_rho06_tau07_seed456` | `downstream_arc_challenge` | `downstream_arc_challenge_acc_norm` |
| `adaptive_rho06_tau07_seed123` | `downstream_hellaswag` | `downstream_hellaswag_acc_norm` |
| `adaptive_fix_seed42` | `downstream_piqa` | `downstream_piqa_acc_norm` |
| | `downstream_winogrande` | `downstream_winogrande_acc` |

**字段映射（每个实验均应用全部 5 项重命名）：**
- `downstream_arc_easy` → `downstream_arc_easy_acc_norm`
- `downstream_arc_challenge` → `downstream_arc_challenge_acc_norm`
- `downstream_hellaswag` → `downstream_hellaswag_acc_norm`
- `downstream_piqa` → `downstream_piqa_acc_norm`
- `downstream_winogrande` → `downstream_winogrande_acc`
- `downstream_mean` — 保持不变

**共修正 4 个实验，每个实验 5 个字段重命名，值不变。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 67868,
  "duration_api_ms": 67703,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "1f4ce05a-24d6-4596-8122-cc9aa92b3d90",
  "total_cost_usd": 0.38848974999999997,
  "usage": {
    "input_tokens": 8,
    "cache_creation_input_tokens": 40529,
    "cache_read_input_tokens": 104917,
    "output_tokens": 3259,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 40529,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 396,
        "cache_read_input_tokens": 45356,
        "cache_creation_input_tokens": 6620,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 6620
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1125,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00121,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 8,
      "outputTokens": 3259,
      "cacheReadInputTokens": 104917,
      "cacheCreationInputTokens": 40529,
      "webSearchRequests": 0,
      "costUSD": 0.38727975000000003,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "aa4ddf81-a2d3-4071-b012-b85e35d64d26"
}
```

</details>

---
