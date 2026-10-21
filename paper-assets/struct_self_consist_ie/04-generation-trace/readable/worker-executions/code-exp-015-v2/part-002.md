# code exp 015 v2 — Part 2 of 2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../code-exp-015-v2.md) · [Structured JSON](../../../sessions/66/664654b94146e4d9bc42.json)

## Before a recorded user message

### Tool call

_source line 257_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01Wi3zxiiFZk5MHbd2GBUGjW`</summary>

```json
{
  "exp_id": "exp_015_v2",
  "field": "status",
  "value": "QUEUED",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d78d198f-d3c0-4b6a-a32a-e794fcda15c4",
  "uuid": "50d4e915-3a7d-4851-89e2-31dcadacdd3b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RRtk7udD1S8yzmUAvXQV1F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 454,
      "cache_read_input_tokens": 138946,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 454
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

_source line 258 · 2026-05-14T15:34:33.155Z_

<details><summary>↩ Tool result · `toolu_01Wi3zxiiFZk5MHbd2GBUGjW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_015_v2\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:34:23.336Z\", \"updated_at\": \"2026-05-14T15:34:32.774Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5517}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d78d198f-d3c0-4b6a-a32a-e794fcda15c4",
  "uuid": "90eeca3b-fc1d-4ca1-a439-656bfe9a1609",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"exp_015_v2\\\", \\\"experiment\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T15:34:23.336Z\\\", \\\"updated_at\\\": \\\"2026-05-14T15:34:32.774Z\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.5517}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"exp_015_v2\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:34:23.336Z\", \"updated_at\": \"2026-05-14T15:34:32.774Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5517}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 259_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01V4W133TTzZmUzYCEiBc9xm`</summary>

```json
{
  "exp_id": "exp_015_v2",
  "field": "status",
  "value": "RUNNING",
  "project": "struct_self_consist_ie",
  "spec": {
    "command": "python code/analyze_exp015_v2_metrics.py",
    "server": "autodl-5090",
    "data_path": "/root/autodl-tmp/struct_self_consist_ie/output/ (10 datasets)",
    "data_count": 9148,
    "model_name": "Qwen3-8B + LLaMA (multi-model)",
    "seed": "42,123,456 (multi-seed)",
    "checkpoint_path": "N/A (analysis only)",
    "log_path": "/tmp/exp015_v2.log"
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
  "session_id": "d78d198f-d3c0-4b6a-a32a-e794fcda15c4",
  "uuid": "d55cc2ba-4e31-4015-a634-1cd95aaca956",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018TdpsMrCiq3TpWvawwoaWc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 267,
      "cache_read_input_tokens": 139400,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 267
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

_source line 260 · 2026-05-14T15:34:38.276Z_

<details><summary>↩ Tool result · `toolu_01V4W133TTzZmUzYCEiBc9xm`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_015_v2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:34:23.336Z\", \"updated_at\": \"2026-05-14T15:34:37.839Z\", \"spec\": {\"command\": \"python code/analyze_exp015_v2_metrics.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/ (10 datasets)\", \"data_count\": 9148, \"model_name\": \"Qwen3-8B + LLaMA (multi-model)\", \"seed\": \"42,123,456 (multi-seed)\", \"checkpoint_path\": \"N/A (analysis only)\", \"log_path\": \"/tmp/exp015_v2.log\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5822}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d78d198f-d3c0-4b6a-a32a-e794fcda15c4",
  "uuid": "762a7ede-effb-406b-ad49-de013aaa41f7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"exp_015_v2\\\", \\\"experiment\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T15:34:23.336Z\\\", \\\"updated_at\\\": \\\"2026-05-14T15:34:37.839Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python code/analyze_exp015_v2_metrics.py\\\", \\\"server\\\": \\\"autodl-5090\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/struct_self_consist_ie/output/ (10 datasets)\\\", \\\"data_count\\\": 9148, \\\"model_name\\\": \\\"Qwen3-8B + LLaMA (multi-model)\\\", \\\"seed\\\": \\\"42,123,456 (multi-seed)\\\", \\\"checkpoint_path\\\": \\\"N/A (analysis only)\\\", \\\"log_path\\\": \\\"/tmp/exp015_v2.log\\\"}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.5822}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"exp_015_v2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:34:23.336Z\", \"updated_at\": \"2026-05-14T15:34:37.839Z\", \"spec\": {\"command\": \"python code/analyze_exp015_v2_metrics.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/ (10 datasets)\", \"data_count\": 9148, \"model_name\": \"Qwen3-8B + LLaMA (multi-model)\", \"seed\": \"42,123,456 (multi-seed)\", \"checkpoint_path\": \"N/A (analysis only)\", \"log_path\": \"/tmp/exp015_v2.log\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5822}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 261_

Now set to DONE with metrics and conclusion.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d78d198f-d3c0-4b6a-a32a-e794fcda15c4",
  "uuid": "7ec60dd0-4851-4e33-804c-c25cdb763e4d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0126EKvpTQdfC76ApSncfVsj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 569,
      "cache_read_input_tokens": 139667,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 569
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

_source line 262_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01EdKYwzDPPenxHYureigVFE`</summary>

```json
{
  "exp_id": "exp_015_v2",
  "field": "status",
  "value": "DONE",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d78d198f-d3c0-4b6a-a32a-e794fcda15c4",
  "uuid": "237f2ebe-cae2-478b-8232-7abd84574933",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0126EKvpTQdfC76ApSncfVsj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 569,
      "cache_read_input_tokens": 139667,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 569
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

_source line 263 · 2026-05-14T15:34:42.070Z_

<details><summary>↩ Tool result · `toolu_01EdKYwzDPPenxHYureigVFE`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 0.1676}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d78d198f-d3c0-4b6a-a32a-e794fcda15c4",
  "uuid": "b3b5eb61-2fe6-4374-a86c-6cb6c27fe8f4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.1676}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 0.1676}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 264_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01X6bzqAzMBmbTEWzbfLaitv`</summary>

```json
{
  "exp_id": "exp_015_v2",
  "field": "conclusion",
  "value": "positive",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d78d198f-d3c0-4b6a-a32a-e794fcda15c4",
  "uuid": "a3b4862e-33b0-4675-bf3b-79f08d15a095",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ky6CwTZVQM5sq33uR3GtFG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 207,
      "cache_read_input_tokens": 140236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 207
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

_source line 265 · 2026-05-14T15:34:45.892Z_

<details><summary>↩ Tool result · `toolu_01X6bzqAzMBmbTEWzbfLaitv`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'positive'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 0.2417}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d78d198f-d3c0-4b6a-a32a-e794fcda15c4",
  "uuid": "d6782d1d-e1bf-48c9-ac86-46a98890a910",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Invalid conclusion 'positive'. Valid: ['failed', 'killed', 'negative', 'success']\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2417}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'positive'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 0.2417}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 266_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_012xpCv27MdZ6hKRVFjcdEoT`</summary>

```json
{
  "exp_id": "exp_015_v2",
  "field": "conclusion",
  "value": "success",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d78d198f-d3c0-4b6a-a32a-e794fcda15c4",
  "uuid": "f4d0ddb3-3ba8-4093-ac12-ac005b6387cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016SJfHDbcQV7q5kMy4k5khV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 202,
      "cache_read_input_tokens": 140443,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 202
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

_source line 267 · 2026-05-14T15:34:51.301Z_

<details><summary>↩ Tool result · `toolu_012xpCv27MdZ6hKRVFjcdEoT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_015_v2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:34:23.336Z\", \"updated_at\": \"2026-05-14T15:34:51.172Z\", \"spec\": {\"command\": \"python code/analyze_exp015_v2_metrics.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/ (10 datasets)\", \"data_count\": 9148, \"model_name\": \"Qwen3-8B + LLaMA (multi-model)\", \"seed\": \"42,123,456 (multi-seed)\", \"checkpoint_path\": \"N/A (analysis only)\", \"log_path\": \"/tmp/exp015_v2.log\"}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2841}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d78d198f-d3c0-4b6a-a32a-e794fcda15c4",
  "uuid": "4a3a89a8-4226-4409-8e14-1dff02e228fb",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"exp_015_v2\\\", \\\"experiment\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T15:34:23.336Z\\\", \\\"updated_at\\\": \\\"2026-05-14T15:34:51.172Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python code/analyze_exp015_v2_metrics.py\\\", \\\"server\\\": \\\"autodl-5090\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/struct_self_consist_ie/output/ (10 datasets)\\\", \\\"data_count\\\": 9148, \\\"model_name\\\": \\\"Qwen3-8B + LLaMA (multi-model)\\\", \\\"seed\\\": \\\"42,123,456 (multi-seed)\\\", \\\"checkpoint_path\\\": \\\"N/A (analysis only)\\\", \\\"log_path\\\": \\\"/tmp/exp015_v2.log\\\"}, \\\"conclusion\\\": \\\"success\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2841}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"exp_015_v2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:34:23.336Z\", \"updated_at\": \"2026-05-14T15:34:51.172Z\", \"spec\": {\"command\": \"python code/analyze_exp015_v2_metrics.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/ (10 datasets)\", \"data_count\": 9148, \"model_name\": \"Qwen3-8B + LLaMA (multi-model)\", \"seed\": \"42,123,456 (multi-seed)\", \"checkpoint_path\": \"N/A (analysis only)\", \"log_path\": \"/tmp/exp015_v2.log\"}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2841}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 268_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_015qy7oErmXcaTHs3RrDis1u`</summary>

```json
{
  "exp_id": "exp_015_v2",
  "field": "status",
  "value": "DONE",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d78d198f-d3c0-4b6a-a32a-e794fcda15c4",
  "uuid": "4eef7507-75f5-4a66-a156-6eaa6799c629",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P1noXKW6kCu4ULBUUS7EGb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 427,
      "cache_read_input_tokens": 140645,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 427
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

_source line 269 · 2026-05-14T15:34:57.128Z_

<details><summary>↩ Tool result · `toolu_015qy7oErmXcaTHs3RrDis1u`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_015_v2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:34:23.336Z\", \"updated_at\": \"2026-05-14T15:34:56.741Z\", \"spec\": {\"command\": \"python code/analyze_exp015_v2_metrics.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/ (10 datasets)\", \"data_count\": 9148, \"model_name\": \"Qwen3-8B + LLaMA (multi-model)\", \"seed\": \"42,123,456 (multi-seed)\", \"checkpoint_path\": \"N/A (analysis only)\", \"log_path\": \"/tmp/exp015_v2.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T15:34:56.741Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5358}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d78d198f-d3c0-4b6a-a32a-e794fcda15c4",
  "uuid": "e126cc57-c394-4f4f-b039-8788233702e5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"exp_015_v2\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T15:34:23.336Z\\\", \\\"updated_at\\\": \\\"2026-05-14T15:34:56.741Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python code/analyze_exp015_v2_metrics.py\\\", \\\"server\\\": \\\"autodl-5090\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/struct_self_consist_ie/output/ (10 datasets)\\\", \\\"data_count\\\": 9148, \\\"model_name\\\": \\\"Qwen3-8B + LLaMA (multi-model)\\\", \\\"seed\\\": \\\"42,123,456 (multi-seed)\\\", \\\"checkpoint_path\\\": \\\"N/A (analysis only)\\\", \\\"log_path\\\": \\\"/tmp/exp015_v2.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-14T15:34:56.741Z\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.5358}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"exp_015_v2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:34:23.336Z\", \"updated_at\": \"2026-05-14T15:34:56.741Z\", \"spec\": {\"command\": \"python code/analyze_exp015_v2_metrics.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/ (10 datasets)\", \"data_count\": 9148, \"model_name\": \"Qwen3-8B + LLaMA (multi-model)\", \"seed\": \"42,123,456 (multi-seed)\", \"checkpoint_path\": \"N/A (analysis only)\", \"log_path\": \"/tmp/exp015_v2.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T15:34:56.741Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5358}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 270_

Now update metrics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d78d198f-d3c0-4b6a-a32a-e794fcda15c4",
  "uuid": "3f989fca-6c9b-4329-a841-994941bea38e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TugjseQNER5URu43uiK48k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 452,
      "cache_read_input_tokens": 141072,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 452
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

_source line 271_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01EBHdsDLYz7wnqcEMWefDLa`</summary>

```json
{
  "exp_id": "exp_015_v2",
  "field": "metrics",
  "value": {
    "auroc_best": {
      "SJ": {
        "conll_ner": 0.8008,
        "scierc_ner_avg": 0.7328,
        "scierc_re_avg": 0.6788,
        "llama_ner_avg": 0.7029,
        "llama_re_avg": 0.7144,
        "wnut_ner": 0.5844
      },
      "FK": {
        "conll_ner": 0.7741,
        "scierc_ner_avg": 0.6172,
        "scierc_re_avg": 0.5939,
        "llama_ner_avg": 0.6484,
        "llama_re_avg": 0.6778,
        "wnut_ner": 0.5752
      },
      "logprob": {
        "conll_ner": 0.7532,
        "scierc_ner_avg": 0.5918,
        "scierc_re_avg": 0.5849,
        "llama_ner_avg": 0.5584,
        "llama_re_avg": 0.654,
        "wnut_ner": 0.358
      },
      "EM": {
        "conll_ner": 0.8156,
        "scierc_ner_avg": 0.7873,
        "scierc_re_avg": 0.715,
        "llama_ner_avg": 0.7533,
        "llama_re_avg": 0.7557,
        "wnut_ner": 0.5745
      },
      "voting_conf": {
        "conll_ner": 0.7889,
        "scierc_ner_avg": 0.7367,
        "scierc_re_avg": 0.7195,
        "llama_ner_avg": 0.7232,
        "llama_re_avg": 0.7509,
        "wnut_ner": 0.8692
      }
    },
    "loo_sj": {
      "max_delta_rho": 0.000305,
      "all_no_circularity": true
    },
    "n_datasets": 10,
    "n_subtask_combos": 18
  },
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d78d198f-d3c0-4b6a-a32a-e794fcda15c4",
  "uuid": "7171a038-87e6-4aa8-8499-244b84996a47",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TugjseQNER5URu43uiK48k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 452,
      "cache_read_input_tokens": 141072,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 452
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

_source line 272 · 2026-05-14T15:35:07.921Z_

<details><summary>↩ Tool result · `toolu_01EBHdsDLYz7wnqcEMWefDLa`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_015_v2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:34:23.336Z\", \"updated_at\": \"2026-05-14T15:35:07.815Z\", \"spec\": {\"command\": \"python code/analyze_exp015_v2_metrics.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/ (10 datasets)\", \"data_count\": 9148, \"model_name\": \"Qwen3-8B + LLaMA (multi-model)\", \"seed\": \"42,123,456 (multi-seed)\", \"checkpoint_path\": \"N/A (analysis only)\", \"log_path\": \"/tmp/exp015_v2.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T15:34:56.741Z\", \"metrics\": {\"auroc_best\": {\"SJ\": {\"conll_ner\": 0.8008, \"scierc_ner_avg\": 0.7328, \"scierc_re_avg\": 0.6788, \"llama_ner_avg\": 0.7029, \"llama_re_avg\": 0.7144, \"wnut_ner\": 0.5844}, \"FK\": {\"conll_ner\": 0.7741, \"scierc_ner_avg\": 0.6172, \"scierc_re_avg\": 0.5939, \"llama_ner_avg\": 0.6484, \"llama_re_avg\": 0.6778, \"wnut_ner\": 0.5752}, \"logprob\": {\"conll_ner\": 0.7532, \"scierc_ner_avg\": 0.5918, \"scierc_re_avg\": 0.5849, \"llama_ner_avg\": 0.5584, \"llama_re_avg\": 0.654, \"wnut_ner\": 0.358}, \"EM\": {\"conll_ner\": 0.8156, \"scierc_ner_avg\": 0.7873, \"scierc_re_avg\": 0.715, \"llama_ner_avg\": 0.7533, \"llama_re_avg\": 0.7557, \"wnut_ner\": 0.5745}, \"voting_conf\": {\"conll_ner\": 0.7889, \"scierc_ner_avg\": 0.7367, \"scierc_re_avg\": 0.7195, \"llama_ner_avg\": 0.7232, \"llama_re_avg\": 0.7509, \"wnut_ner\": 0.8692}}, \"loo_sj\": {\"max_delta_rho\": 0.000305, \"all_no_circularity\": true}, \"n_datasets\": 10, \"n_subtask_combos\": 18}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2466}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d78d198f-d3c0-4b6a-a32a-e794fcda15c4",
  "uuid": "cc90e1f8-b4ab-4c58-8a1b-c5314aec50da",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"exp_015_v2\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T15:34:23.336Z\\\", \\\"updated_at\\\": \\\"2026-05-14T15:35:07.815Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python code/analyze_exp015_v2_metrics.py\\\", \\\"server\\\": \\\"autodl-5090\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/struct_self_consist_ie/output/ (10 datasets)\\\", \\\"data_count\\\": 9148, \\\"model_name\\\": \\\"Qwen3-8B + LLaMA (multi-model)\\\", \\\"seed\\\": \\\"42,123,456 (multi-seed)\\\", \\\"checkpoint_path\\\": \\\"N/A (analysis only)\\\", \\\"log_path\\\": \\\"/tmp/exp015_v2.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-14T15:34:56.741Z\\\", \\\"metrics\\\": {\\\"auroc_best\\\": {\\\"SJ\\\": {\\\"conll_ner\\\": 0.8008, \\\"scierc_ner_avg\\\": 0.7328, \\\"scierc_re_avg\\\": 0.6788, \\\"llama_ner_avg\\\": 0.7029, \\\"llama_re_avg\\\": 0.7144, \\\"wnut_ner\\\": 0.5844}, \\\"FK\\\": {\\\"conll_ner\\\": 0.7741, \\\"scierc_ner_avg\\\": 0.6172, \\\"scierc_re_avg\\\": 0.5939, \\\"llama_ner_avg\\\": 0.6484, \\\"llama_re_avg\\\": 0.6778, \\\"wnut_ner\\\": 0.5752}, \\\"logprob\\\": {\\\"conll_ner\\\": 0.7532, \\\"scierc_ner_avg\\\": 0.5918, \\\"scierc_re_avg\\\": 0.5849, \\\"llama_ner_avg\\\": 0.5584, \\\"llama_re_avg\\\": 0.654, \\\"wnut_ner\\\": 0.358}, \\\"EM\\\": {\\\"conll_ner\\\": 0.8156, \\\"scierc_ner_avg\\\": 0.7873, \\\"scierc_re_avg\\\": 0.715, \\\"llama_ner_avg\\\": 0.7533, \\\"llama_re_avg\\\": 0.7557, \\\"wnut_ner\\\": 0.5745}, \\\"voting_conf\\\": {\\\"conll_ner\\\": 0.7889, \\\"scierc_ner_avg\\\": 0.7367, \\\"scierc_re_avg\\\": 0.7195, \\\"llama_ner_avg\\\": 0.7232, \\\"llama_re_avg\\\": 0.7509, \\\"wnut_ner\\\": 0.8692}}, \\\"loo_sj\\\": {\\\"max_delta_rho\\\": 0.000305, \\\"all_no_circularity\\\": true}, \\\"n_datasets\\\": 10, \\\"n_subtask_combos\\\": 18}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2466}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"exp_015_v2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:34:23.336Z\", \"updated_at\": \"2026-05-14T15:35:07.815Z\", \"spec\": {\"command\": \"python code/analyze_exp015_v2_metrics.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/ (10 datasets)\", \"data_count\": 9148, \"model_name\": \"Qwen3-8B + LLaMA (multi-model)\", \"seed\": \"42,123,456 (multi-seed)\", \"checkpoint_path\": \"N/A (analysis only)\", \"log_path\": \"/tmp/exp015_v2.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T15:34:56.741Z\", \"metrics\": {\"auroc_best\": {\"SJ\": {\"conll_ner\": 0.8008, \"scierc_ner_avg\": 0.7328, \"scierc_re_avg\": 0.6788, \"llama_ner_avg\": 0.7029, \"llama_re_avg\": 0.7144, \"wnut_ner\": 0.5844}, \"FK\": {\"conll_ner\": 0.7741, \"scierc_ner_avg\": 0.6172, \"scierc_re_avg\": 0.5939, \"llama_ner_avg\": 0.6484, \"llama_re_avg\": 0.6778, \"wnut_ner\": 0.5752}, \"logprob\": {\"conll_ner\": 0.7532, \"scierc_ner_avg\": 0.5918, \"scierc_re_avg\": 0.5849, \"llama_ner_avg\": 0.5584, \"llama_re_avg\": 0.654, \"wnut_ner\": 0.358}, \"EM\": {\"conll_ner\": 0.8156, \"scierc_ner_avg\": 0.7873, \"scierc_re_avg\": 0.715, \"llama_ner_avg\": 0.7533, \"llama_re_avg\": 0.7557, \"wnut_ner\": 0.5745}, \"voting_conf\": {\"conll_ner\": 0.7889, \"scierc_ner_avg\": 0.7367, \"scierc_re_avg\": 0.7195, \"llama_ner_avg\": 0.7232, \"llama_re_avg\": 0.7509, \"wnut_ner\": 0.8692}}, \"loo_sj\": {\"max_delta_rho\": 0.000305, \"all_no_circularity\": true}, \"n_datasets\": 10, \"n_subtask_combos\": 18}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2466}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 273_

Now register the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d78d198f-d3c0-4b6a-a32a-e794fcda15c4",
  "uuid": "bc3bdf0d-06c3-462e-b409-b8640a638e48",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JX9azoa2FhMSgDbGAo9c2M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1521,
      "cache_read_input_tokens": 141524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1521
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

_source line 274_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_019ZEcbG6XsY9LTZonT7Afqo`</summary>

```json
{
  "name": "exp015_v2_full_metrics_matrix",
  "type": "data",
  "description": "Full 5-signal x 10-dataset x 4-metric evaluation matrix with bootstrap 95% CI and LOO-SJ robustness check. 18 dataset-subtask combinations (NER+RE). Signals: SJ, FK, logprob, EM, voting_conf. Metrics: AUROC, Spearman, Kendall, ECE.",
  "project": "struct_self_consist_ie",
  "exp_id": "exp_015_v2",
  "content_filename": "exp015_v2_metrics.json",
  "tags": [
    "metrics",
    "evaluation",
    "bootstrap",
    "loo-sj",
    "multi-dataset"
  ],
  "url": "autodl-5090:/root/autodl-tmp/struct_self_consist_ie/output/exp_015_v2/exp015_v2_metrics.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d78d198f-d3c0-4b6a-a32a-e794fcda15c4",
  "uuid": "da3cb9ba-1076-4e15-ba0d-b4ded94c2262",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JX9azoa2FhMSgDbGAo9c2M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1521,
      "cache_read_input_tokens": 141524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1521
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

_source line 275 · 2026-05-14T15:35:15.462Z_

<details><summary>↩ Tool result · `toolu_019ZEcbG6XsY9LTZonT7Afqo`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_adacf4\", \"name\": \"exp015_v2_full_metrics_matrix\", \"type\": \"data\", \"description\": \"Full 5-signal x 10-dataset x 4-metric evaluation matrix with bootstrap 95% CI and LOO-SJ robustness check. 18 dataset-subtask combinations (NER+RE). Signals: SJ, FK, logprob, EM, voting_conf. Metrics: AUROC, Spearman, Kendall, ECE.\", \"path\": null, \"url\": \"autodl-5090:/root/autodl-tmp/struct_self_consist_ie/output/exp_015_v2/exp015_v2_metrics.json\", \"project\": \"struct_self_consist_ie\", \"exp_id\": \"exp_015_v2\", \"skill\": \"\", \"created_at\": \"2026-05-14T15:35:15.373954+00:00\", \"tags\": [\"metrics\", \"evaluation\", \"bootstrap\", \"loo-sj\", \"multi-dataset\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d78d198f-d3c0-4b6a-a32a-e794fcda15c4",
  "uuid": "2e5f149d-6010-4e09-be12-8859158da1fc",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260514_adacf4\\\", \\\"name\\\": \\\"exp015_v2_full_metrics_matrix\\\", \\\"type\\\": \\\"data\\\", \\\"description\\\": \\\"Full 5-signal x 10-dataset x 4-metric evaluation matrix with bootstrap 95% CI and LOO-SJ robustness check. 18 dataset-subtask combinations (NER+RE). Signals: SJ, FK, logprob, EM, voting_conf. Metrics: AUROC, Spearman, Kendall, ECE.\\\", \\\"path\\\": null, \\\"url\\\": \\\"autodl-5090:/root/autodl-tmp/struct_self_consist_ie/output/exp_015_v2/exp015_v2_metrics.json\\\", \\\"project\\\": \\\"struct_self_consist_ie\\\", \\\"exp_id\\\": \\\"exp_015_v2\\\", \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-14T15:35:15.373954+00:00\\\", \\\"tags\\\": [\\\"metrics\\\", \\\"evaluation\\\", \\\"bootstrap\\\", \\\"loo-sj\\\", \\\"multi-dataset\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_adacf4\", \"name\": \"exp015_v2_full_metrics_matrix\", \"type\": \"data\", \"description\": \"Full 5-signal x 10-dataset x 4-metric evaluation matrix with bootstrap 95% CI and LOO-SJ robustness check. 18 dataset-subtask combinations (NER+RE). Signals: SJ, FK, logprob, EM, voting_conf. Metrics: AUROC, Spearman, Kendall, ECE.\", \"path\": null, \"url\": \"autodl-5090:/root/autodl-tmp/struct_self_consist_ie/output/exp_015_v2/exp015_v2_metrics.json\", \"project\": \"struct_self_consist_ie\", \"exp_id\": \"exp_015_v2\", \"skill\": \"\", \"created_at\": \"2026-05-14T15:35:15.373954+00:00\", \"tags\": [\"metrics\", \"evaluation\", \"bootstrap\", \"loo-sj\", \"multi-dataset\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 276_

全部完成。总结如下：

## exp-015 v2 结果

**覆盖范围**: 5 信号 × 10 数据集 × 2 subtask(NER/RE) = 18 组合 × 4 指标 = 360 个指标点，全部附带 bootstrap 95% CI

### AUROC 关键发现

| 数据集组 | SJ | FK | logprob | EM | voting_conf |
|---|---|---|---|---|---|
| CoNLL NER | 0.80 | 0.77 | 0.75 | **0.82** | 0.79 |
| SciERC NER (avg) | 0.73 | 0.62 | 0.59 | **0.79** | 0.74 |
| SciERC RE (avg) | 0.68 | 0.59 | 0.58 | **0.72** | 0.72 |
| LLaMA NER (avg) | 0.70 | 0.65 | 0.56 | **0.75** | 0.72 |
| LLaMA RE (avg) | 0.71 | 0.68 | 0.65 | **0.76** | 0.75 |
| WNUT NER | 0.58 | 0.58 | 0.36 | 0.57 | **0.87** |

### 排名

- **AUROC**: EM 在绝大多数数据集上最强 (12/18)；voting_conf 在 WNUT 上大幅领先 (0.87)
- **Spearman ρ**: voting_conf 在 15/18 组合上最高（rank correlation 与 F1 的关联最强）
- **Kendall τ**: voting_conf 同样领先
- **ECE**: voting_conf 在 RE 上校准最好 (ECE < 0.20)；EM 在 NER 上校准最好

### LOO-SJ Robustness

所有 18 个组合的 |Δρ| < 0.001，LOO-SJ 与 full SJ 相关系数 ≥ 0.9999。**无循环性问题**。

### 产出

- JSON 结果: `autodl-5090:/root/autodl-tmp/struct_self_consist_ie/output/exp_015_v2/exp015_v2_metrics.json` (82KB)
- Registry: `exp_015_v2` → DONE/success
- Artifact: `art_20260514_adacf4` 已注册

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d78d198f-d3c0-4b6a-a32a-e794fcda15c4",
  "uuid": "886a7376-e2ea-48ab-8188-5d0f13921765",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UnXuVZ6q5CZvaDqaGx19sK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 835,
      "cache_read_input_tokens": 143045,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 835
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

_source line 277_

全部完成。总结如下：

## exp-015 v2 结果

**覆盖范围**: 5 信号 × 10 数据集 × 2 subtask(NER/RE) = 18 组合 × 4 指标 = 360 个指标点，全部附带 bootstrap 95% CI

### AUROC 关键发现

| 数据集组 | SJ | FK | logprob | EM | voting_conf |
|---|---|---|---|---|---|
| CoNLL NER | 0.80 | 0.77 | 0.75 | **0.82** | 0.79 |
| SciERC NER (avg) | 0.73 | 0.62 | 0.59 | **0.79** | 0.74 |
| SciERC RE (avg) | 0.68 | 0.59 | 0.58 | **0.72** | 0.72 |
| LLaMA NER (avg) | 0.70 | 0.65 | 0.56 | **0.75** | 0.72 |
| LLaMA RE (avg) | 0.71 | 0.68 | 0.65 | **0.76** | 0.75 |
| WNUT NER | 0.58 | 0.58 | 0.36 | 0.57 | **0.87** |

### 排名

- **AUROC**: EM 在绝大多数数据集上最强 (12/18)；voting_conf 在 WNUT 上大幅领先 (0.87)
- **Spearman ρ**: voting_conf 在 15/18 组合上最高（rank correlation 与 F1 的关联最强）
- **Kendall τ**: voting_conf 同样领先
- **ECE**: voting_conf 在 RE 上校准最好 (ECE < 0.20)；EM 在 NER 上校准最好

### LOO-SJ Robustness

所有 18 个组合的 |Δρ| < 0.001，LOO-SJ 与 full SJ 相关系数 ≥ 0.9999。**无循环性问题**。

### 产出

- JSON 结果: `autodl-5090:/root/autodl-tmp/struct_self_consist_ie/output/exp_015_v2/exp015_v2_metrics.json` (82KB)
- Registry: `exp_015_v2` → DONE/success
- Artifact: `art_20260514_adacf4` 已注册

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 905669,
  "duration_api_ms": 789121,
  "num_turns": 107,
  "stop_reason": "end_turn",
  "session_id": "d78d198f-d3c0-4b6a-a32a-e794fcda15c4",
  "total_cost_usd": 7.203936249999996,
  "usage": {
    "input_tokens": 95,
    "cache_creation_input_tokens": 132039,
    "cache_read_input_tokens": 10569163,
    "output_tokens": 43687,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 132039,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 699,
        "cache_read_input_tokens": 143045,
        "cache_creation_input_tokens": 835,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 835
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1376,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001461,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 95,
      "outputTokens": 43687,
      "cacheReadInputTokens": 10569163,
      "cacheCreationInputTokens": 132039,
      "webSearchRequests": 0,
      "costUSD": 7.202475249999996,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "435315cc-1779-4dce-84a9-82ea89247e21"
}
```

</details>

---
