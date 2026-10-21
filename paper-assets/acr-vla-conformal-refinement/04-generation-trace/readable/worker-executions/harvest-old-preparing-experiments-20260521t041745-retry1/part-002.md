# harvest old preparing experiments 20260521T041745 retry1 — Part 2 of 2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../harvest-old-preparing-experiments-20260521t041745-retry1.md) · [Structured JSON](../../../sessions/fb/fb7f79e7dded44cce291.json)

## Before a recorded user message

### Tool result

_source line 373 · 2026-05-21T04:27:49.460Z_

<details><summary>↩ Tool result · `toolu_0143CtpB87TEwY8RSydrLVYQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-seed48\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:29.201Z\", \"updated_at\": \"2026-05-21T04:27:49.021Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_goal_obs_only_norm02_seed48.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 48, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed48.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed48.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.68}, \"completed_at\": \"2026-05-21T04:27:49.021Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6729}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "54dfdabd-182c-4d7a-8a56-19df45c62196",
  "uuid": "d0de8015-f78b-43cf-aded-c4b48a2187c6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-crm-goal-seed48\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T04:23:29.201Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:27:49.021Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"harvest\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"logs/eval_goal_obs_only_norm02_seed48.json\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"openvla\\\", \\\"seed\\\": 48, \\\"checkpoint_source\\\": \\\"harvested\\\", \\\"eval_data\\\": \\\"goal\\\", \\\"checkpoint_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed48.json\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed48.json\\\"}, \\\"hypothesis\\\": \\\"CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.68}, \\\"completed_at\\\": \\\"2026-05-21T04:27:49.021Z\\\"}, \\\"hint\\\": \\\"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\\\"}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.6729}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-seed48\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:29.201Z\", \"updated_at\": \"2026-05-21T04:27:49.021Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_goal_obs_only_norm02_seed48.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 48, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed48.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed48.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.68}, \"completed_at\": \"2026-05-21T04:27:49.021Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6729}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 374_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_014X4ot6tZZDnsy4pJv8DueN`</summary>

```json
{
  "exp_id": "eval-crm-goal-seed47",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "54dfdabd-182c-4d7a-8a56-19df45c62196",
  "uuid": "08a95d3e-406d-48dd-8151-a2e03ded54c8",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01UBMfzevsTRoe6TpNYv5MNp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 141765,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 141765
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

_source line 375 · 2026-05-21T04:27:50.812Z_

<details><summary>↩ Tool result · `toolu_014X4ot6tZZDnsy4pJv8DueN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-seed47\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:29.771Z\", \"updated_at\": \"2026-05-21T04:27:50.201Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_goal_obs_only_norm02_seed47.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 47, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed47.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed47.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.69}, \"completed_at\": \"2026-05-21T04:27:50.201Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.966}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "54dfdabd-182c-4d7a-8a56-19df45c62196",
  "uuid": "d11cd741-8698-432d-b2de-3ebd8d9ab1ce",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-crm-goal-seed47\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T04:23:29.771Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:27:50.201Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"harvest\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"logs/eval_goal_obs_only_norm02_seed47.json\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"openvla\\\", \\\"seed\\\": 47, \\\"checkpoint_source\\\": \\\"harvested\\\", \\\"eval_data\\\": \\\"goal\\\", \\\"checkpoint_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed47.json\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed47.json\\\"}, \\\"hypothesis\\\": \\\"CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.69}, \\\"completed_at\\\": \\\"2026-05-21T04:27:50.201Z\\\"}, \\\"hint\\\": \\\"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\\\"}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.966}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-seed47\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:29.771Z\", \"updated_at\": \"2026-05-21T04:27:50.201Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_goal_obs_only_norm02_seed47.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 47, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed47.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed47.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.69}, \"completed_at\": \"2026-05-21T04:27:50.201Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.966}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 376_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01TkevTUKsfDmZn7hPJBghJq`</summary>

```json
{
  "exp_id": "eval-crm-goal-seed50",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "54dfdabd-182c-4d7a-8a56-19df45c62196",
  "uuid": "1602b877-20df-4661-8b01-0d8056358177",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01UBMfzevsTRoe6TpNYv5MNp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 141765,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 141765
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

_source line 377_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_015KRE4FyhsY4rvxdQyP8fnG`</summary>

```json
{
  "exp_id": "eval-crm-goal-seed49",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "54dfdabd-182c-4d7a-8a56-19df45c62196",
  "uuid": "76094b3c-f22c-4e28-a98a-3f17a8138cbc",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01UBMfzevsTRoe6TpNYv5MNp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 141765,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 141765
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

_source line 378 · 2026-05-21T04:27:51.951Z_

<details><summary>↩ Tool result · `toolu_01TkevTUKsfDmZn7hPJBghJq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-seed50\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:30.804Z\", \"updated_at\": \"2026-05-21T04:27:51.247Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_goal_obs_only_norm02_seed50.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 50, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed50.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed50.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.67}, \"completed_at\": \"2026-05-21T04:27:51.247Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0216}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "54dfdabd-182c-4d7a-8a56-19df45c62196",
  "uuid": "957bfc1f-7c19-4f94-be8f-0d3e659f7948",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-crm-goal-seed50\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T04:23:30.804Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:27:51.247Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"harvest\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"logs/eval_goal_obs_only_norm02_seed50.json\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"openvla\\\", \\\"seed\\\": 50, \\\"checkpoint_source\\\": \\\"harvested\\\", \\\"eval_data\\\": \\\"goal\\\", \\\"checkpoint_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed50.json\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed50.json\\\"}, \\\"hypothesis\\\": \\\"CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.67}, \\\"completed_at\\\": \\\"2026-05-21T04:27:51.247Z\\\"}, \\\"hint\\\": \\\"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\\\"}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.0216}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-seed50\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:30.804Z\", \"updated_at\": \"2026-05-21T04:27:51.247Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_goal_obs_only_norm02_seed50.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 50, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed50.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed50.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.67}, \"completed_at\": \"2026-05-21T04:27:51.247Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0216}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 379_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_017PRM9jFgLCHbAhLLh9ad4f`</summary>

```json
{
  "exp_id": "eval-crm-long-seed52",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "54dfdabd-182c-4d7a-8a56-19df45c62196",
  "uuid": "0c40a19a-c689-4b16-874e-f15487747d21",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01UBMfzevsTRoe6TpNYv5MNp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 141765,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 141765
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

_source line 380 · 2026-05-21T04:27:53.051Z_

<details><summary>↩ Tool result · `toolu_015KRE4FyhsY4rvxdQyP8fnG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-seed49\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:31.844Z\", \"updated_at\": \"2026-05-21T04:27:52.398Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_goal_obs_only_norm02_seed49.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 49, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed49.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed49.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.62}, \"completed_at\": \"2026-05-21T04:27:52.398Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0678}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "54dfdabd-182c-4d7a-8a56-19df45c62196",
  "uuid": "27d0705d-4ffb-4b6f-88fe-9991f3354c7c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-crm-goal-seed49\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T04:23:31.844Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:27:52.398Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"harvest\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"logs/eval_goal_obs_only_norm02_seed49.json\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"openvla\\\", \\\"seed\\\": 49, \\\"checkpoint_source\\\": \\\"harvested\\\", \\\"eval_data\\\": \\\"goal\\\", \\\"checkpoint_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed49.json\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed49.json\\\"}, \\\"hypothesis\\\": \\\"CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.62}, \\\"completed_at\\\": \\\"2026-05-21T04:27:52.398Z\\\"}, \\\"hint\\\": \\\"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\\\"}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.0678}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-seed49\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:31.844Z\", \"updated_at\": \"2026-05-21T04:27:52.398Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_goal_obs_only_norm02_seed49.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 49, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed49.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed49.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.62}, \"completed_at\": \"2026-05-21T04:27:52.398Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0678}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 381_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01A8GWh3GgNBY6nuPjBKLsUh`</summary>

```json
{
  "exp_id": "eval-vla-only-long-seed49",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "54dfdabd-182c-4d7a-8a56-19df45c62196",
  "uuid": "7cd30154-925b-4c41-9cd6-4a04aeb7d358",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01UBMfzevsTRoe6TpNYv5MNp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 141765,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 141765
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

_source line 382 · 2026-05-21T04:27:53.822Z_

<details><summary>↩ Tool result · `toolu_017PRM9jFgLCHbAhLLh9ad4f`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed52\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:32.959Z\", \"updated_at\": \"2026-05-21T04:27:53.425Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_long_obs_only_norm02_seed52.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 52, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed52.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed52.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}, \"completed_at\": \"2026-05-21T04:27:53.426Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.758}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "54dfdabd-182c-4d7a-8a56-19df45c62196",
  "uuid": "ebf427d1-ea7b-4dc6-95e0-51c6fb69c5b3",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-crm-long-seed52\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T04:23:32.959Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:27:53.425Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"harvest\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"logs/eval_long_obs_only_norm02_seed52.json\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"openvla\\\", \\\"seed\\\": 52, \\\"checkpoint_source\\\": \\\"harvested\\\", \\\"eval_data\\\": \\\"long\\\", \\\"checkpoint_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed52.json\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed52.json\\\"}, \\\"hypothesis\\\": \\\"CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.15}, \\\"completed_at\\\": \\\"2026-05-21T04:27:53.426Z\\\"}, \\\"hint\\\": \\\"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\\\"}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.758}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed52\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:32.959Z\", \"updated_at\": \"2026-05-21T04:27:53.425Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_long_obs_only_norm02_seed52.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 52, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed52.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed52.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}, \"completed_at\": \"2026-05-21T04:27:53.426Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.758}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 383 · 2026-05-21T04:27:54.527Z_

<details><summary>↩ Tool result · `toolu_01A8GWh3GgNBY6nuPjBKLsUh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-long-seed49\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:33.602Z\", \"updated_at\": \"2026-05-21T04:27:54.076Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_long_vla_only_seed49.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 49, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed49.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed49.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on long-horizon task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}, \"completed_at\": \"2026-05-21T04:27:54.076Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.69}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "54dfdabd-182c-4d7a-8a56-19df45c62196",
  "uuid": "a14e79ba-9ca5-4f1e-952a-c1337bd36305",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-vla-only-long-seed49\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T04:23:33.602Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:27:54.076Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"harvest\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"logs/eval_long_vla_only_seed49.json\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"openvla\\\", \\\"seed\\\": 49, \\\"checkpoint_source\\\": \\\"harvested\\\", \\\"eval_data\\\": \\\"long\\\", \\\"checkpoint_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed49.json\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed49.json\\\"}, \\\"hypothesis\\\": \\\"VLA-only baseline (no CRM) on long-horizon task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.16}, \\\"completed_at\\\": \\\"2026-05-21T04:27:54.076Z\\\"}, \\\"hint\\\": \\\"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\\\"}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.69}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-long-seed49\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:33.602Z\", \"updated_at\": \"2026-05-21T04:27:54.076Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_long_vla_only_seed49.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 49, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed49.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed49.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on long-horizon task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}, \"completed_at\": \"2026-05-21T04:27:54.076Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.69}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 384_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_018sKJfG1LfwEN9XuLjsHxTP`</summary>

```json
{
  "todos": [
    {
      "content": "Test single registry update to validate flow",
      "activeForm": "Testing single registry update",
      "status": "completed"
    },
    {
      "content": "Transition all 28 to QUEUED then RUNNING with spec",
      "activeForm": "Transitioning to RUNNING",
      "status": "completed"
    },
    {
      "content": "Set hypothesis for all 28",
      "activeForm": "Setting hypothesis",
      "status": "completed"
    },
    {
      "content": "Set conclusion and metrics for all 28",
      "activeForm": "Setting conclusion and metrics",
      "status": "completed"
    },
    {
      "content": "Final RUNNING → DONE for all 28",
      "activeForm": "Finalizing DONE state",
      "status": "completed"
    },
    {
      "content": "Report summary table",
      "activeForm": "Reporting summary",
      "status": "completed"
    }
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
  "session_id": "54dfdabd-182c-4d7a-8a56-19df45c62196",
  "uuid": "fc780b79-6e4e-4c3e-b29f-e2494ee7be42",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01T6DEcER922Ex357hGKKgDL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 150138,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 150138
      },
      "output_tokens": 59,
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

_source line 385 · 2026-05-21T04:28:02.132Z_

<details><summary>↩ Tool result · `toolu_018sKJfG1LfwEN9XuLjsHxTP`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "54dfdabd-182c-4d7a-8a56-19df45c62196",
  "uuid": "a01803c1-4ca9-4174-a8c2-87661d2cfb1a",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Test single registry update to validate flow",
        "status": "completed",
        "activeForm": "Testing single registry update"
      },
      {
        "content": "Transition all 28 to QUEUED then RUNNING with spec",
        "status": "completed",
        "activeForm": "Transitioning to RUNNING"
      },
      {
        "content": "Set hypothesis for all 28",
        "status": "completed",
        "activeForm": "Setting hypothesis"
      },
      {
        "content": "Set conclusion and metrics for all 28",
        "status": "completed",
        "activeForm": "Setting conclusion and metrics"
      },
      {
        "content": "Final RUNNING → DONE for all 28",
        "status": "in_progress",
        "activeForm": "Finalizing DONE state"
      },
      {
        "content": "Report summary table",
        "status": "pending",
        "activeForm": "Reporting summary"
      }
    ],
    "newTodos": [
      {
        "content": "Test single registry update to validate flow",
        "status": "completed",
        "activeForm": "Testing single registry update"
      },
      {
        "content": "Transition all 28 to QUEUED then RUNNING with spec",
        "status": "completed",
        "activeForm": "Transitioning to RUNNING"
      },
      {
        "content": "Set hypothesis for all 28",
        "status": "completed",
        "activeForm": "Setting hypothesis"
      },
      {
        "content": "Set conclusion and metrics for all 28",
        "status": "completed",
        "activeForm": "Setting conclusion and metrics"
      },
      {
        "content": "Final RUNNING → DONE for all 28",
        "status": "completed",
        "activeForm": "Finalizing DONE state"
      },
      {
        "content": "Report summary table",
        "status": "completed",
        "activeForm": "Reporting summary"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---


### Assistant

_source line 386_

All 29 experiments processed: 26 marked DONE with metrics, 3 missing JSONs flagged.

## 汇总表

| # | exp_id | server | JSON exists? | SR | 备注 |
|---|---|---|---|---|---|
| 1 | eval-vla-only-spatial-seed54 | bjb1-32546 | ✓ | 0.27 | DONE |
| 2 | eval-crm-long-seed54 | bjb1-32546 | ✓ | 0.19 | DONE |
| 3 | eval-crm-long-seed49 | bjb1-32546 | ✓ | 0.14 | DONE |
| 4 | eval-crm-long-seed48 | bjb1-32546 | ✓ | 0.15 | DONE |
| 5 | eval-crm-spatial-k10-seed50 | bjb1-32546 | ✓ | 0.35 | DONE |
| 6 | eval-vla-only-long-seed53 | bjb1-32546 | ✓ | 0.12 | DONE |
| 7 | eval-vla-only-goal-seed52 | bjb1-32546 | ✓ | 0.68 | DONE |
| 8 | eval-crm-long-seed51 | bjb1-32546 | ✓ | 0.13 | DONE |
| 9 | eval-vla-only-spatial-seed51 | bjb1-32546 | ✓ | 0.33 | DONE |
| 10 | eval-vla-only-object-seed51 | bjb1-32546 | ✓ | 0.15 | DONE |
| 11 | eval-crm-spatial-seed48 | bjb1-32546 | ✓ | 0.35 | DONE |
| 12 | eval-obs-only-object-norm02-k20-seed42 | bjb1-32546 | ✗ | — | 进程可能仍在运行或已失败，未更新 |
| 13 | eval-obs-only-goal-norm02-seed53 | bjb1-32546 | ✓ | 0.63 | DONE |
| 14 | eval-vla-only-long-seed54 | bjb1-18228 | ✓ | 0.12 | DONE |
| 15 | eval-crm-long-seed53 | bjb1-18228 | ✓ | 0.18 | DONE |
| 16 | eval-vla-only-spatial-seed53 | bjb1-18228 | ✓ | 0.28 | DONE |
| 17 | eval-vla-only-spatial-seed52 | bjb1-18228 | ✓ | 0.31 | DONE |
| 18 | eval-vla-only-spatial-seed50 | bjb1-18228 | ✓ | 0.30 | DONE |
| 19 | eval-crm-spatial-seed47 | bjb1-18228 | ✓ | 0.32 | DONE |
| 20 | eval-vla-only-object-seed49-r2 | bjb1-18228 | ✓ | 0.10 | DONE |
| 21 | eval-obs-only-object-norm02-k20-seed43 | bjb1-18228 | ✗ | — | 进程可能仍在运行或已失败，未更新 |
| 22 | eval-crm-spatial-k10-seed49 | bjb2-28827 | ✓ | 0.32 | DONE |
| 23 | eval-crm-goal-seed48 | bjb2-28827 | ✓ | 0.68 | DONE |
| 24 | eval-crm-goal-seed47 | bjb2-28827 | ✓ | 0.69 | DONE |
| 25 | eval-crm-goal-seed50 | bjb2-28827 | ✓ | 0.67 | DONE |
| 26 | eval-crm-goal-seed49 | bjb2-28827 | ✓ | 0.62 | DONE |
| 27 | eval-crm-long-seed52 | bjb2-28827 | ✓ | 0.15 | DONE |
| 28 | eval-vla-only-long-seed49 | bjb2-28827 | ✓ | 0.16 | DONE |
| 29 | eval-vla-only-spatial-seed49-r2 | bjb2-28827 | ✗ | — | 进程可能仍在运行或已失败，未更新 |

**统计**：26 个已收割到 DONE（全部 SR > 0，conclusion=success），3 个 JSON 缺失保持 PREPARING。

**关键观察**：
- VLA-only goal seed52 = 0.68 vs CRM goal (47/48/49/50) = 0.62-0.69 — CRM 在 goal 任务上与 VLA-only 持平甚至略低
- CRM long (0.13-0.19) vs VLA-only long (0.12, 0.16) — long-horizon 上 CRM 提升微弱
- CRM spatial (0.32-0.35) vs VLA-only spatial (0.27-0.33) — spatial 上 CRM 有小幅领先

**注**：registry 中 spec.command 填的是占位 "harvest"，因为原始 submit_training_job 的命令未保留；checkpoint_path 和 log_path 都指向同一 JSON 文件（eval 类任务无独立训练 checkpoint）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "54dfdabd-182c-4d7a-8a56-19df45c62196",
  "uuid": "34625082-d37d-4dc7-9dd1-92e86c037bf8",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01SvJRFGjFTT19iNuwTVSCfK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 397,
      "cache_read_input_tokens": 166472,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 397
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


### Runtime record

_source line 387_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed_warning",
    "resetsAt": 1779584400,
    "rateLimitType": "seven_day",
    "utilization": 0.75,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "70ff98fe-037a-4552-a913-4a63c8c3a00f",
  "session_id": "54dfdabd-182c-4d7a-8a56-19df45c62196"
}
```

---


### Task result

_source line 388_

All 29 experiments processed: 26 marked DONE with metrics, 3 missing JSONs flagged.

## 汇总表

| # | exp_id | server | JSON exists? | SR | 备注 |
|---|---|---|---|---|---|
| 1 | eval-vla-only-spatial-seed54 | bjb1-32546 | ✓ | 0.27 | DONE |
| 2 | eval-crm-long-seed54 | bjb1-32546 | ✓ | 0.19 | DONE |
| 3 | eval-crm-long-seed49 | bjb1-32546 | ✓ | 0.14 | DONE |
| 4 | eval-crm-long-seed48 | bjb1-32546 | ✓ | 0.15 | DONE |
| 5 | eval-crm-spatial-k10-seed50 | bjb1-32546 | ✓ | 0.35 | DONE |
| 6 | eval-vla-only-long-seed53 | bjb1-32546 | ✓ | 0.12 | DONE |
| 7 | eval-vla-only-goal-seed52 | bjb1-32546 | ✓ | 0.68 | DONE |
| 8 | eval-crm-long-seed51 | bjb1-32546 | ✓ | 0.13 | DONE |
| 9 | eval-vla-only-spatial-seed51 | bjb1-32546 | ✓ | 0.33 | DONE |
| 10 | eval-vla-only-object-seed51 | bjb1-32546 | ✓ | 0.15 | DONE |
| 11 | eval-crm-spatial-seed48 | bjb1-32546 | ✓ | 0.35 | DONE |
| 12 | eval-obs-only-object-norm02-k20-seed42 | bjb1-32546 | ✗ | — | 进程可能仍在运行或已失败，未更新 |
| 13 | eval-obs-only-goal-norm02-seed53 | bjb1-32546 | ✓ | 0.63 | DONE |
| 14 | eval-vla-only-long-seed54 | bjb1-18228 | ✓ | 0.12 | DONE |
| 15 | eval-crm-long-seed53 | bjb1-18228 | ✓ | 0.18 | DONE |
| 16 | eval-vla-only-spatial-seed53 | bjb1-18228 | ✓ | 0.28 | DONE |
| 17 | eval-vla-only-spatial-seed52 | bjb1-18228 | ✓ | 0.31 | DONE |
| 18 | eval-vla-only-spatial-seed50 | bjb1-18228 | ✓ | 0.30 | DONE |
| 19 | eval-crm-spatial-seed47 | bjb1-18228 | ✓ | 0.32 | DONE |
| 20 | eval-vla-only-object-seed49-r2 | bjb1-18228 | ✓ | 0.10 | DONE |
| 21 | eval-obs-only-object-norm02-k20-seed43 | bjb1-18228 | ✗ | — | 进程可能仍在运行或已失败，未更新 |
| 22 | eval-crm-spatial-k10-seed49 | bjb2-28827 | ✓ | 0.32 | DONE |
| 23 | eval-crm-goal-seed48 | bjb2-28827 | ✓ | 0.68 | DONE |
| 24 | eval-crm-goal-seed47 | bjb2-28827 | ✓ | 0.69 | DONE |
| 25 | eval-crm-goal-seed50 | bjb2-28827 | ✓ | 0.67 | DONE |
| 26 | eval-crm-goal-seed49 | bjb2-28827 | ✓ | 0.62 | DONE |
| 27 | eval-crm-long-seed52 | bjb2-28827 | ✓ | 0.15 | DONE |
| 28 | eval-vla-only-long-seed49 | bjb2-28827 | ✓ | 0.16 | DONE |
| 29 | eval-vla-only-spatial-seed49-r2 | bjb2-28827 | ✗ | — | 进程可能仍在运行或已失败，未更新 |

**统计**：26 个已收割到 DONE（全部 SR > 0，conclusion=success），3 个 JSON 缺失保持 PREPARING。

**关键观察**：
- VLA-only goal seed52 = 0.68 vs CRM goal (47/48/49/50) = 0.62-0.69 — CRM 在 goal 任务上与 VLA-only 持平甚至略低
- CRM long (0.13-0.19) vs VLA-only long (0.12, 0.16) — long-horizon 上 CRM 提升微弱
- CRM spatial (0.32-0.35) vs VLA-only spatial (0.27-0.33) — spatial 上 CRM 有小幅领先

**注**：registry 中 spec.command 填的是占位 "harvest"，因为原始 submit_training_job 的命令未保留；checkpoint_path 和 log_path 都指向同一 JSON 文件（eval 类任务无独立训练 checkpoint）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 565561,
  "duration_api_ms": 555708,
  "num_turns": 182,
  "stop_reason": "end_turn",
  "session_id": "54dfdabd-182c-4d7a-8a56-19df45c62196",
  "total_cost_usd": 9.176181499999998,
  "usage": {
    "input_tokens": 45,
    "cache_creation_input_tokens": 1155892,
    "cache_read_input_tokens": 1731303,
    "output_tokens": 43340,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 1155892,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1787,
        "cache_read_input_tokens": 166472,
        "cache_creation_input_tokens": 397,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 397
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2395,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00248,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-7[1m]": {
      "inputTokens": 45,
      "outputTokens": 43340,
      "cacheReadInputTokens": 1731303,
      "cacheCreationInputTokens": 1155892,
      "webSearchRequests": 0,
      "costUSD": 9.173701499999998,
      "contextWindow": 1000000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "35748972-dfeb-4936-8431-c0f895551676"
}
```

</details>

---
