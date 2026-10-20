# experiment gold 3annotator eval — Part 3 of 3

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Worker execution logs

[← Part 2](part-002.md) · [Transcript overview](../experiment-gold-3annotator-eval.md) · [Structured JSON](../../../sessions/a9/a90f4ef1977b6180395d.json)

## Round 1

### Tool call

_source line 904_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0176g6hngwmhnrRvW32fPpJP`</summary>

```json
{
  "server": "bjb2-23165",
  "command": "tail -10 /tmp/bootstrap_setC.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4ad72269-7830-4ae4-9f6c-62304c9d6f13",
  "uuid": "4f47360a-70de-46dc-9b14-30a54fe306db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HwBZ91QMhx8uQ4ztKkhS3m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 338,
      "cache_read_input_tokens": 119944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 338
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

_source line 905 · 2026-05-15T12:54:47.672Z_

<details><summary>↩ Tool result · `toolu_0176g6hngwmhnrRvW32fPpJP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"  Structural RF macro-F1 (on shared): 0.8099\\n  Structural GB macro-F1 (on shared): 0.8381\\n  Observed delta (Structural RF - Structural GB): -0.0282\\n  95% CI: [-0.0466, -0.0118]\\n  p-value: 0.0003  (significant at alpha=0.05: YES)\\n\\n--- twv_probe_vs_gb ---\\n  Shared windows: 328\\n  TWV Probe macro-F1 (on shared): 0.8569\\n  Structural GB macro-F1 (on shared): 0.8799\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4ad72269-7830-4ae4-9f6c-62304c9d6f13",
  "uuid": "7dfecac7-269f-43d3-abb9-172484f4c8f3",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"  Structural RF macro-F1 (on shared): 0.8099\\\\n  Structural GB macro-F1 (on shared): 0.8381\\\\n  Observed delta (Structural RF - Structural GB): -0.0282\\\\n  95% CI: [-0.0466, -0.0118]\\\\n  p-value: 0.0003  (significant at alpha=0.05: YES)\\\\n\\\\n--- twv_probe_vs_gb ---\\\\n  Shared windows: 328\\\\n  TWV Probe macro-F1 (on shared): 0.8569\\\\n  Structural GB macro-F1 (on shared): 0.8799\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.31}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"  Structural RF macro-F1 (on shared): 0.8099\\n  Structural GB macro-F1 (on shared): 0.8381\\n  Observed delta (Structural RF - Structural GB): -0.0282\\n  95% CI: [-0.0466, -0.0118]\\n  p-value: 0.0003  (significant at alpha=0.05: YES)\\n\\n--- twv_probe_vs_gb ---\\n  Shared windows: 328\\n  TWV Probe macro-F1 (on shared): 0.8569\\n  Structural GB macro-F1 (on shared): 0.8799\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 906_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01MNTykiK9wjwFxpZGgJhGbD`</summary>

```json
{
  "server": "bjb2-23165",
  "command": "tail -10 /tmp/bootstrap_setC.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4ad72269-7830-4ae4-9f6c-62304c9d6f13",
  "uuid": "14918932-42f9-49a6-afde-74013f42f3e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DmqHG6E7Rp28LeQQUiQuAH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 338,
      "cache_read_input_tokens": 120282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 338
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

_source line 907 · 2026-05-15T12:54:51.245Z_

<details><summary>↩ Tool result · `toolu_01MNTykiK9wjwFxpZGgJhGbD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"  TWV Probe macro-F1 (on shared): 0.8569\\n  Structural GB macro-F1 (on shared): 0.8799\\n  Observed delta (TWV Probe - Structural GB): -0.0230\\n  95% CI: [-0.0532, +0.0060]\\n  p-value: 0.0612  (significant at alpha=0.05: NO)\\n\\n--- twv_probe_vs_gru_probe ---\\n  Shared windows: 328\\n  TWV Probe macro-F1 (on shared): 0.8569\\n  GRU Probe macro-F1 (on shared): 0.7936\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4ad72269-7830-4ae4-9f6c-62304c9d6f13",
  "uuid": "39a62f32-5ef7-4aca-a915-695ceb63bafa",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"  TWV Probe macro-F1 (on shared): 0.8569\\\\n  Structural GB macro-F1 (on shared): 0.8799\\\\n  Observed delta (TWV Probe - Structural GB): -0.0230\\\\n  95% CI: [-0.0532, +0.0060]\\\\n  p-value: 0.0612  (significant at alpha=0.05: NO)\\\\n\\\\n--- twv_probe_vs_gru_probe ---\\\\n  Shared windows: 328\\\\n  TWV Probe macro-F1 (on shared): 0.8569\\\\n  GRU Probe macro-F1 (on shared): 0.7936\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.31}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"  TWV Probe macro-F1 (on shared): 0.8569\\n  Structural GB macro-F1 (on shared): 0.8799\\n  Observed delta (TWV Probe - Structural GB): -0.0230\\n  95% CI: [-0.0532, +0.0060]\\n  p-value: 0.0612  (significant at alpha=0.05: NO)\\n\\n--- twv_probe_vs_gru_probe ---\\n  Shared windows: 328\\n  TWV Probe macro-F1 (on shared): 0.8569\\n  GRU Probe macro-F1 (on shared): 0.7936\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 908_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013V4nmmAKJC3tiaBmhso7mY`</summary>

```json
{
  "server": "bjb2-23165",
  "command": "ls -la /root/autodl-tmp/agent_progress_probe/artifacts/gold_set/bootstrap_setC.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4ad72269-7830-4ae4-9f6c-62304c9d6f13",
  "uuid": "5c12f273-efd1-4ad5-a63c-a68fab0a5302",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015UPDELnghrzGzUDn95ba6U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 345,
      "cache_read_input_tokens": 120620,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 345
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

_source line 909 · 2026-05-15T12:54:54.370Z_

<details><summary>↩ Tool result · `toolu_013V4nmmAKJC3tiaBmhso7mY`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/agent_progress_probe/artifacts/gold_set/bootstrap_setC.json': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.32}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4ad72269-7830-4ae4-9f6c-62304c9d6f13",
  "uuid": "7a62e65c-a866-474e-a04e-4b09f8429a1a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"ls: cannot access '/root/autodl-tmp/agent_progress_probe/artifacts/gold_set/bootstrap_setC.json': No such file or directory\\\\n\\\", \\\"return_code\\\": 2}, \\\"error\\\": \\\"exit code 2\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.32}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/agent_progress_probe/artifacts/gold_set/bootstrap_setC.json': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.32}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 910_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01WeXsPDgTVwN4gHZvBVLcFh`</summary>

```json
{
  "server": "bjb2-23165",
  "command": "tail -5 /tmp/bootstrap_setC.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4ad72269-7830-4ae4-9f6c-62304c9d6f13",
  "uuid": "02fd38b7-5b67-497e-b85b-36410aa763d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BvYYDgvz1k6rw5wHkfhzZj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 230,
      "cache_read_input_tokens": 120965,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 230
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

_source line 911 · 2026-05-15T12:54:58.045Z_

<details><summary>↩ Tool result · `toolu_01WeXsPDgTVwN4gHZvBVLcFh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n--- twv_probe_vs_gru_probe ---\\n  Shared windows: 328\\n  TWV Probe macro-F1 (on shared): 0.8569\\n  GRU Probe macro-F1 (on shared): 0.7936\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4ad72269-7830-4ae4-9f6c-62304c9d6f13",
  "uuid": "f36f3fcf-eaed-453a-82a5-f7d42c7069bc",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\n--- twv_probe_vs_gru_probe ---\\\\n  Shared windows: 328\\\\n  TWV Probe macro-F1 (on shared): 0.8569\\\\n  GRU Probe macro-F1 (on shared): 0.7936\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.31}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\n--- twv_probe_vs_gru_probe ---\\n  Shared windows: 328\\n  TWV Probe macro-F1 (on shared): 0.8569\\n  GRU Probe macro-F1 (on shared): 0.7936\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 912_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_011xYtJRHmMRLR5XcVixW6kS`</summary>

```json
{
  "server": "bjb2-23165",
  "command": "tail -5 /tmp/bootstrap_setC.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4ad72269-7830-4ae4-9f6c-62304c9d6f13",
  "uuid": "5521cf43-826a-43ae-9a3b-dd7cb3ebc20c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MFbxFEcY81x6pGMS5Q2YZ8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 240,
      "cache_read_input_tokens": 121195,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 240
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

_source line 913 · 2026-05-15T12:55:01.542Z_

<details><summary>↩ Tool result · `toolu_011xYtJRHmMRLR5XcVixW6kS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n--- twv_probe_vs_gru_probe ---\\n  Shared windows: 328\\n  TWV Probe macro-F1 (on shared): 0.8569\\n  GRU Probe macro-F1 (on shared): 0.7936\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4ad72269-7830-4ae4-9f6c-62304c9d6f13",
  "uuid": "943ab887-ae58-487b-a024-4841f3d40eec",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\n--- twv_probe_vs_gru_probe ---\\\\n  Shared windows: 328\\\\n  TWV Probe macro-F1 (on shared): 0.8569\\\\n  GRU Probe macro-F1 (on shared): 0.7936\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.31}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\n--- twv_probe_vs_gru_probe ---\\n  Shared windows: 328\\n  TWV Probe macro-F1 (on shared): 0.8569\\n  GRU Probe macro-F1 (on shared): 0.7936\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 914_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0127NDuLPiwPeZXrRQyZwbQh`</summary>

```json
{
  "server": "bjb2-23165",
  "command": "tail -5 /tmp/bootstrap_setC.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4ad72269-7830-4ae4-9f6c-62304c9d6f13",
  "uuid": "89997889-12ea-4f6a-ae4d-9ae5a658ac53",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FL5RgwDX5WdLtCechfa7sK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 240,
      "cache_read_input_tokens": 121435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 240
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

_source line 915 · 2026-05-15T12:55:05.858Z_

<details><summary>↩ Tool result · `toolu_0127NDuLPiwPeZXrRQyZwbQh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n--- twv_probe_vs_gru_probe ---\\n  Shared windows: 328\\n  TWV Probe macro-F1 (on shared): 0.8569\\n  GRU Probe macro-F1 (on shared): 0.7936\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4ad72269-7830-4ae4-9f6c-62304c9d6f13",
  "uuid": "3511fd44-b083-4717-979c-0911b51fd47e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\n--- twv_probe_vs_gru_probe ---\\\\n  Shared windows: 328\\\\n  TWV Probe macro-F1 (on shared): 0.8569\\\\n  GRU Probe macro-F1 (on shared): 0.7936\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.31}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\n--- twv_probe_vs_gru_probe ---\\n  Shared windows: 328\\n  TWV Probe macro-F1 (on shared): 0.8569\\n  GRU Probe macro-F1 (on shared): 0.7936\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 916_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01RaSwyNWEVJEEvhSmYRZZ7W`</summary>

```json
{
  "server": "bjb2-23165",
  "command": "tail -5 /tmp/bootstrap_setC.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4ad72269-7830-4ae4-9f6c-62304c9d6f13",
  "uuid": "df586b2f-5c7c-472a-b569-313f4dc2b072",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AqjTvbXKhdNtMpnRFcYbhB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 240,
      "cache_read_input_tokens": 121675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 240
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

_source line 917 · 2026-05-15T12:55:09.172Z_

<details><summary>↩ Tool result · `toolu_01RaSwyNWEVJEEvhSmYRZZ7W`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"  Observed delta (TWV Probe - GRU Probe): +0.0633\\n  95% CI: [+0.0261, +0.1013]\\n  p-value: 0.0002  (significant at alpha=0.05: YES)\\n\\nResults saved: artifacts/gold_set/bootstrap_setC.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4ad72269-7830-4ae4-9f6c-62304c9d6f13",
  "uuid": "71ff94bc-a8eb-44e4-ab77-9c8fbbff5e18",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"  Observed delta (TWV Probe - GRU Probe): +0.0633\\\\n  95% CI: [+0.0261, +0.1013]\\\\n  p-value: 0.0002  (significant at alpha=0.05: YES)\\\\n\\\\nResults saved: artifacts/gold_set/bootstrap_setC.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.31}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"  Observed delta (TWV Probe - GRU Probe): +0.0633\\n  95% CI: [+0.0261, +0.1013]\\n  p-value: 0.0002  (significant at alpha=0.05: YES)\\n\\nResults saved: artifacts/gold_set/bootstrap_setC.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 918_

All 6 jobs complete. Reading the final bootstrap_setC results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4ad72269-7830-4ae4-9f6c-62304c9d6f13",
  "uuid": "340d98c6-4046-49ef-b247-f2b1e1836a86",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013wSBoryQckL267Lm9itchE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 360,
      "cache_read_input_tokens": 121915,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 360
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

_source line 919_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01V7z95oWGs1TaRvSMKSxSsw`</summary>

```json
{
  "server": "bjb2-23165",
  "command": "cat /root/autodl-tmp/agent_progress_probe/artifacts/gold_set/bootstrap_setC.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4ad72269-7830-4ae4-9f6c-62304c9d6f13",
  "uuid": "f4a1b12a-db04-4783-b763-fb9cfd5bb17e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013wSBoryQckL267Lm9itchE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 360,
      "cache_read_input_tokens": 121915,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 360
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

_source line 920 · 2026-05-15T12:55:13.105Z_

<details><summary>↩ Tool result · `toolu_01V7z95oWGs1TaRvSMKSxSsw`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"n_bootstrap\\\": 10000,\\n  \\\"seed\\\": 42,\\n  \\\"tests\\\": {\\n    \\\"gb_vs_mv\\\": {\\n      \\\"model_a\\\": \\\"Structural GB\\\",\\n      \\\"model_b\\\": \\\"MV Labels\\\",\\n      \\\"n_samples\\\": 498,\\n      \\\"n_bootstrap\\\": 10000,\\n      \\\"f1_a_on_shared\\\": 0.838137,\\n      \\\"f1_b_on_shared\\\": 0.799229,\\n      \\\"observed_delta\\\": 0.038908,\\n      \\\"ci_95_lo\\\": 0.017385,\\n      \\\"ci_95_hi\\\": 0.062553,\\n      \\\"p_value\\\": 0.0,\\n      \\\"significant_005\\\": true\\n    },\\n    \\\"gb_vs_gru_probe\\\": {\\n      \\\"model_a\\\": \\\"Structural GB\\\",\\n      \\\"model_b\\\": \\\"GRU Probe\\\",\\n      \\\"n_samples\\\": 328,\\n      \\\"n_bootstrap\\\": 10000,\\n      \\\"f1_a_on_shared\\\": 0.879869,\\n      \\\"f1_b_on_shared\\\": 0.793593,\\n      \\\"observed_delta\\\": 0.086276,\\n      \\\"ci_95_lo\\\": 0.04667,\\n      \\\"ci_95_hi\\\": 0.126498,\\n      \\\"p_value\\\": 0.0,\\n      \\\"significant_005\\\": true\\n    },\\n    \\\"rf_vs_gb\\\": {\\n      \\\"model_a\\\": \\\"Structural RF\\\",\\n      \\\"model_b\\\": \\\"Structural GB\\\",\\n      \\\"n_samples\\\": 498,\\n      \\\"n_bootstrap\\\": 10000,\\n      \\\"f1_a_on_shared\\\": 0.809913,\\n      \\\"f1_b_on_shared\\\": 0.838137,\\n      \\\"observed_delta\\\": -0.028224,\\n      \\\"ci_95_lo\\\": -0.046588,\\n      \\\"ci_95_hi\\\": -0.011751,\\n      \\\"p_value\\\": 0.0003,\\n      \\\"significant_005\\\": true\\n    },\\n    \\\"twv_probe_vs_gb\\\": {\\n      \\\"model_a\\\": \\\"TWV Probe\\\",\\n      \\\"model_b\\\": \\\"Structural GB\\\",\\n      \\\"n_samples\\\": 328,\\n      \\\"n_bootstrap\\\": 10000,\\n      \\\"f1_a_on_shared\\\": 0.856911,\\n      \\\"f1_b_on_shared\\\": 0.879869,\\n      \\\"observed_delta\\\": -0.022958,\\n      \\\"ci_95_lo\\\": -0.053214,\\n      \\\"ci_95_hi\\\": 0.005996,\\n      \\\"p_value\\\": 0.0612,\\n      \\\"significant_005\\\": false\\n    },\\n    \\\"twv_probe_vs_gru_probe\\\": {\\n      \\\"model_a\\\": \\\"TWV Probe\\\",\\n      \\\"model_b\\\": \\\"GRU Probe\\\",\\n      \\\"n_samples\\\": 328,\\n      \\\"n_bootstrap\\\": 10000,\\n      \\\"f1_a_on_shared\\\": 0.856911,\\n      \\\"f1_b_on_shared\\\": 0.793593,\\n      \\\"observed_delta\\\": 0.063318,\\n      \\\"ci_95_lo\\\": 0.02611,\\n      \\\"ci_95_hi\\\": 0.101342,\\n      \\\"p_value\\\": 0.0002,\\n      \\\"significant_005\\\": true\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4ad72269-7830-4ae4-9f6c-62304c9d6f13",
  "uuid": "784a4f61-6c8d-4803-80b2-c7bda358a9a1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"n_bootstrap\\\\\\\": 10000,\\\\n  \\\\\\\"seed\\\\\\\": 42,\\\\n  \\\\\\\"tests\\\\\\\": {\\\\n    \\\\\\\"gb_vs_mv\\\\\\\": {\\\\n      \\\\\\\"model_a\\\\\\\": \\\\\\\"Structural GB\\\\\\\",\\\\n      \\\\\\\"model_b\\\\\\\": \\\\\\\"MV Labels\\\\\\\",\\\\n      \\\\\\\"n_samples\\\\\\\": 498,\\\\n      \\\\\\\"n_bootstrap\\\\\\\": 10000,\\\\n      \\\\\\\"f1_a_on_shared\\\\\\\": 0.838137,\\\\n      \\\\\\\"f1_b_on_shared\\\\\\\": 0.799229,\\\\n      \\\\\\\"observed_delta\\\\\\\": 0.038908,\\\\n      \\\\\\\"ci_95_lo\\\\\\\": 0.017385,\\\\n      \\\\\\\"ci_95_hi\\\\\\\": 0.062553,\\\\n      \\\\\\\"p_value\\\\\\\": 0.0,\\\\n      \\\\\\\"significant_005\\\\\\\": true\\\\n    },\\\\n    \\\\\\\"gb_vs_gru_probe\\\\\\\": {\\\\n      \\\\\\\"model_a\\\\\\\": \\\\\\\"Structural GB\\\\\\\",\\\\n      \\\\\\\"model_b\\\\\\\": \\\\\\\"GRU Probe\\\\\\\",\\\\n      \\\\\\\"n_samples\\\\\\\": 328,\\\\n      \\\\\\\"n_bootstrap\\\\\\\": 10000,\\\\n      \\\\\\\"f1_a_on_shared\\\\\\\": 0.879869,\\\\n      \\\\\\\"f1_b_on_shared\\\\\\\": 0.793593,\\\\n      \\\\\\\"observed_delta\\\\\\\": 0.086276,\\\\n      \\\\\\\"ci_95_lo\\\\\\\": 0.04667,\\\\n      \\\\\\\"ci_95_hi\\\\\\\": 0.126498,\\\\n      \\\\\\\"p_value\\\\\\\": 0.0,\\\\n      \\\\\\\"significant_005\\\\\\\": true\\\\n    },\\\\n    \\\\\\\"rf_vs_gb\\\\\\\": {\\\\n      \\\\\\\"model_a\\\\\\\": \\\\\\\"Structural RF\\\\\\\",\\\\n      \\\\\\\"model_b\\\\\\\": \\\\\\\"Structural GB\\\\\\\",\\\\n      \\\\\\\"n_samples\\\\\\\": 498,\\\\n      \\\\\\\"n_bootstrap\\\\\\\": 10000,\\\\n      \\\\\\\"f1_a_on_shared\\\\\\\": 0.809913,\\\\n      \\\\\\\"f1_b_on_shared\\\\\\\": 0.838137,\\\\n      \\\\\\\"observed_delta\\\\\\\": -0.028224,\\\\n      \\\\\\\"ci_95_lo\\\\\\\": -0.046588,\\\\n      \\\\\\\"ci_95_hi\\\\\\\": -0.011751,\\\\n      \\\\\\\"p_value\\\\\\\": 0.0003,\\\\n      \\\\\\\"significant_005\\\\\\\": true\\\\n    },\\\\n    \\\\\\\"twv_probe_vs_gb\\\\\\\": {\\\\n      \\\\\\\"model_a\\\\\\\": \\\\\\\"TWV Probe\\\\\\\",\\\\n      \\\\\\\"model_b\\\\\\\": \\\\\\\"Structural GB\\\\\\\",\\\\n      \\\\\\\"n_samples\\\\\\\": 328,\\\\n      \\\\\\\"n_bootstrap\\\\\\\": 10000,\\\\n      \\\\\\\"f1_a_on_shared\\\\\\\": 0.856911,\\\\n      \\\\\\\"f1_b_on_shared\\\\\\\": 0.879869,\\\\n      \\\\\\\"observed_delta\\\\\\\": -0.022958,\\\\n      \\\\\\\"ci_95_lo\\\\\\\": -0.053214,\\\\n      \\\\\\\"ci_95_hi\\\\\\\": 0.005996,\\\\n      \\\\\\\"p_value\\\\\\\": 0.0612,\\\\n      \\\\\\\"significant_005\\\\\\\": false\\\\n    },\\\\n    \\\\\\\"twv_probe_vs_gru_probe\\\\\\\": {\\\\n      \\\\\\\"model_a\\\\\\\": \\\\\\\"TWV Probe\\\\\\\",\\\\n      \\\\\\\"model_b\\\\\\\": \\\\\\\"GRU Probe\\\\\\\",\\\\n      \\\\\\\"n_samples\\\\\\\": 328,\\\\n      \\\\\\\"n_bootstrap\\\\\\\": 10000,\\\\n      \\\\\\\"f1_a_on_shared\\\\\\\": 0.856911,\\\\n      \\\\\\\"f1_b_on_shared\\\\\\\": 0.793593,\\\\n      \\\\\\\"observed_delta\\\\\\\": 0.063318,\\\\n      \\\\\\\"ci_95_lo\\\\\\\": 0.02611,\\\\n      \\\\\\\"ci_95_hi\\\\\\\": 0.101342,\\\\n      \\\\\\\"p_value\\\\\\\": 0.0002,\\\\n      \\\\\\\"significant_005\\\\\\\": true\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.32}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"n_bootstrap\\\": 10000,\\n  \\\"seed\\\": 42,\\n  \\\"tests\\\": {\\n    \\\"gb_vs_mv\\\": {\\n      \\\"model_a\\\": \\\"Structural GB\\\",\\n      \\\"model_b\\\": \\\"MV Labels\\\",\\n      \\\"n_samples\\\": 498,\\n      \\\"n_bootstrap\\\": 10000,\\n      \\\"f1_a_on_shared\\\": 0.838137,\\n      \\\"f1_b_on_shared\\\": 0.799229,\\n      \\\"observed_delta\\\": 0.038908,\\n      \\\"ci_95_lo\\\": 0.017385,\\n      \\\"ci_95_hi\\\": 0.062553,\\n      \\\"p_value\\\": 0.0,\\n      \\\"significant_005\\\": true\\n    },\\n    \\\"gb_vs_gru_probe\\\": {\\n      \\\"model_a\\\": \\\"Structural GB\\\",\\n      \\\"model_b\\\": \\\"GRU Probe\\\",\\n      \\\"n_samples\\\": 328,\\n      \\\"n_bootstrap\\\": 10000,\\n      \\\"f1_a_on_shared\\\": 0.879869,\\n      \\\"f1_b_on_shared\\\": 0.793593,\\n      \\\"observed_delta\\\": 0.086276,\\n      \\\"ci_95_lo\\\": 0.04667,\\n      \\\"ci_95_hi\\\": 0.126498,\\n      \\\"p_value\\\": 0.0,\\n      \\\"significant_005\\\": true\\n    },\\n    \\\"rf_vs_gb\\\": {\\n      \\\"model_a\\\": \\\"Structural RF\\\",\\n      \\\"model_b\\\": \\\"Structural GB\\\",\\n      \\\"n_samples\\\": 498,\\n      \\\"n_bootstrap\\\": 10000,\\n      \\\"f1_a_on_shared\\\": 0.809913,\\n      \\\"f1_b_on_shared\\\": 0.838137,\\n      \\\"observed_delta\\\": -0.028224,\\n      \\\"ci_95_lo\\\": -0.046588,\\n      \\\"ci_95_hi\\\": -0.011751,\\n      \\\"p_value\\\": 0.0003,\\n      \\\"significant_005\\\": true\\n    },\\n    \\\"twv_probe_vs_gb\\\": {\\n      \\\"model_a\\\": \\\"TWV Probe\\\",\\n      \\\"model_b\\\": \\\"Structural GB\\\",\\n      \\\"n_samples\\\": 328,\\n      \\\"n_bootstrap\\\": 10000,\\n      \\\"f1_a_on_shared\\\": 0.856911,\\n      \\\"f1_b_on_shared\\\": 0.879869,\\n      \\\"observed_delta\\\": -0.022958,\\n      \\\"ci_95_lo\\\": -0.053214,\\n      \\\"ci_95_hi\\\": 0.005996,\\n      \\\"p_value\\\": 0.0612,\\n      \\\"significant_005\\\": false\\n    },\\n    \\\"twv_probe_vs_gru_probe\\\": {\\n      \\\"model_a\\\": \\\"TWV Probe\\\",\\n      \\\"model_b\\\": \\\"GRU Probe\\\",\\n      \\\"n_samples\\\": 328,\\n      \\\"n_bootstrap\\\": 10000,\\n      \\\"f1_a_on_shared\\\": 0.856911,\\n      \\\"f1_b_on_shared\\\": 0.793593,\\n      \\\"observed_delta\\\": 0.063318,\\n      \\\"ci_95_lo\\\": 0.02611,\\n      \\\"ci_95_hi\\\": 0.101342,\\n      \\\"p_value\\\": 0.0002,\\n      \\\"significant_005\\\": true\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 921_

All 6 results collected. Now producing the comparison tables.

---

## Step 5: Verification & Comparison Tables

### Eval ↔ Bootstrap Consistency Check

Bootstrap F1 values for GB and RF match eval results exactly across all sets:

| Model | Set A eval | Set A boot | Set B eval | Set B boot | Set C eval | Set C boot |
|-------|-----------|-----------|-----------|-----------|-----------|-----------|
| GB | 0.7210 | 0.7210 | 0.8394 | 0.8394 | 0.8381 | 0.8381 |
| RF | 0.7401 | 0.7401 | 0.8107 | 0.8107 | 0.8099 | 0.8099 |

**All within 0pp tolerance — perfect consistency.**

---

### Table 1: Per-Model Macro-F1 Across 4 Gold Sets

| Model | Old N=195 | Set A (N=52, conf≥3) | Set B (N=505, conf≥2) | Set C (N=512, all) |
|-------|----------|---------------------|----------------------|-------------------|
| **GB** | 0.764 | 0.7210 (n=50) | **0.8394** (n=491) | **0.8381** (n=498) |
| RF | 0.752 | 0.7401 (n=50) | 0.8107 (n=491) | 0.8099 (n=498) |
| MV | 0.718 | 0.7210 (n=50) | 0.7975 (n=491) | 0.7992 (n=498) |
| GRU Probe | 0.735 | 0.7619 (n=35) | 0.7895 (n=322) | 0.7936 (n=328) |
| TWV | 0.768 | 0.6766 (n=37) | 0.8478 (n=335) | 0.8508 (n=341) |
| TWV Probe | — | 0.7464 (n=35) | 0.8539 (n=322) | 0.8569 (n=328) |

---

### Table 2: Bootstrap Paired Tests (p-values, 10K iterations, seed=42)

| Comparison | Set A (N=52) | Set B (N=505) | Set C (N=512) |
|-----------|-------------|--------------|--------------|
| **GB vs MV** | p=1.000 (n=50, Δ=0.000) | **p=0.0001** (n=491, Δ=+0.042) | **p<0.0001** (n=498, Δ=+0.039) |
| **GB vs Probe** | p=0.253 (n=35, Δ=-0.053) | **p<0.0001** (n=322, Δ=+0.088) | **p<0.0001** (n=328, Δ=+0.086) |
| **RF vs GB** | p=0.366 (n=50, Δ=+0.019) | **p=0.0003** (n=491, Δ=-0.029) | **p=0.0003** (n=498, Δ=-0.028) |
| TWV Probe vs GB | p=0.289 (n=35, Δ=+0.038) | p=0.056 (n=322, Δ=-0.023) | p=0.061 (n=328, Δ=-0.023) |
| TWV Probe vs Probe | p=0.417 (n=35, Δ=-0.016) | **p=0.0002** (n=322, Δ=+0.064) | **p=0.0002** (n=328, Δ=+0.063) |

---

### Key Findings

1. **Set A (N=52, strict 3-annotator)**: Too small for significance — all p>0.25. GB=MV=0.721, wide CIs.
2. **Set B & C are highly consistent**: B and C differ by only 7 windows, and all F1 values agree within 0.3pp. Significance patterns are identical.
3. **GB dominates on conf≥2**: GB significantly beats MV (+4.2pp, p=0.0001), GRU Probe (+8.8pp, p<0.0001), and RF (+2.9pp, p=0.0003).
4. **TWV Probe vs GB**: Borderline non-significant (p=0.056/0.061) — GB has 2.3pp edge, TWV Probe can't close the gap.
5. **TWV Probe vs GRU Probe**: Strongly significant (+6.3pp, p=0.0002) — trajectory-weighted embeddings dominate standard embeddings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4ad72269-7830-4ae4-9f6c-62304c9d6f13",
  "uuid": "0878e9df-f36a-43af-8fc6-48a9d79ac2a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WvBLajhemuTSN6euPejRQW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1400,
      "cache_read_input_tokens": 122275,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1400
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

_source line 922_

All 6 results collected. Now producing the comparison tables.

---

## Step 5: Verification & Comparison Tables

### Eval ↔ Bootstrap Consistency Check

Bootstrap F1 values for GB and RF match eval results exactly across all sets:

| Model | Set A eval | Set A boot | Set B eval | Set B boot | Set C eval | Set C boot |
|-------|-----------|-----------|-----------|-----------|-----------|-----------|
| GB | 0.7210 | 0.7210 | 0.8394 | 0.8394 | 0.8381 | 0.8381 |
| RF | 0.7401 | 0.7401 | 0.8107 | 0.8107 | 0.8099 | 0.8099 |

**All within 0pp tolerance — perfect consistency.**

---

### Table 1: Per-Model Macro-F1 Across 4 Gold Sets

| Model | Old N=195 | Set A (N=52, conf≥3) | Set B (N=505, conf≥2) | Set C (N=512, all) |
|-------|----------|---------------------|----------------------|-------------------|
| **GB** | 0.764 | 0.7210 (n=50) | **0.8394** (n=491) | **0.8381** (n=498) |
| RF | 0.752 | 0.7401 (n=50) | 0.8107 (n=491) | 0.8099 (n=498) |
| MV | 0.718 | 0.7210 (n=50) | 0.7975 (n=491) | 0.7992 (n=498) |
| GRU Probe | 0.735 | 0.7619 (n=35) | 0.7895 (n=322) | 0.7936 (n=328) |
| TWV | 0.768 | 0.6766 (n=37) | 0.8478 (n=335) | 0.8508 (n=341) |
| TWV Probe | — | 0.7464 (n=35) | 0.8539 (n=322) | 0.8569 (n=328) |

---

### Table 2: Bootstrap Paired Tests (p-values, 10K iterations, seed=42)

| Comparison | Set A (N=52) | Set B (N=505) | Set C (N=512) |
|-----------|-------------|--------------|--------------|
| **GB vs MV** | p=1.000 (n=50, Δ=0.000) | **p=0.0001** (n=491, Δ=+0.042) | **p<0.0001** (n=498, Δ=+0.039) |
| **GB vs Probe** | p=0.253 (n=35, Δ=-0.053) | **p<0.0001** (n=322, Δ=+0.088) | **p<0.0001** (n=328, Δ=+0.086) |
| **RF vs GB** | p=0.366 (n=50, Δ=+0.019) | **p=0.0003** (n=491, Δ=-0.029) | **p=0.0003** (n=498, Δ=-0.028) |
| TWV Probe vs GB | p=0.289 (n=35, Δ=+0.038) | p=0.056 (n=322, Δ=-0.023) | p=0.061 (n=328, Δ=-0.023) |
| TWV Probe vs Probe | p=0.417 (n=35, Δ=-0.016) | **p=0.0002** (n=322, Δ=+0.064) | **p=0.0002** (n=328, Δ=+0.063) |

---

### Key Findings

1. **Set A (N=52, strict 3-annotator)**: Too small for significance — all p>0.25. GB=MV=0.721, wide CIs.
2. **Set B & C are highly consistent**: B and C differ by only 7 windows, and all F1 values agree within 0.3pp. Significance patterns are identical.
3. **GB dominates on conf≥2**: GB significantly beats MV (+4.2pp, p=0.0001), GRU Probe (+8.8pp, p<0.0001), and RF (+2.9pp, p=0.0003).
4. **TWV Probe vs GB**: Borderline non-significant (p=0.056/0.061) — GB has 2.3pp edge, TWV Probe can't close the gap.
5. **TWV Probe vs GRU Probe**: Strongly significant (+6.3pp, p=0.0002) — trajectory-weighted embeddings dominate standard embeddings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 2410598,
  "duration_api_ms": 2049356,
  "num_turns": 386,
  "stop_reason": "end_turn",
  "session_id": "4ad72269-7830-4ae4-9f6c-62304c9d6f13",
  "total_cost_usd": 18.83587124999999,
  "usage": {
    "input_tokens": 324,
    "cache_creation_input_tokens": 266234,
    "cache_read_input_tokens": 30106368,
    "output_tokens": 76143,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 266234,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1257,
        "cache_read_input_tokens": 122275,
        "cache_creation_input_tokens": 1400,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1400
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2513,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002603,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 1995,
      "outputTokens": 80809,
      "cacheReadInputTokens": 30272824,
      "cacheCreationInputTokens": 266665,
      "webSearchRequests": 0,
      "costUSD": 18.83326824999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "36bbfa20-804d-4ef0-a2ff-dcadbd17094d"
}
```

</details>

---
