# analysis bootstrap table2 matched — Part 2 of 2

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../analysis-bootstrap-table2-matched.md) · [Structured JSON](../../../sessions/9d/9dcd867e3440f38da9cb.json)

## Before a recorded user message

### Tool result

_source line 250 · 2026-05-15T05:15:17.680Z_

<details><summary>↩ Tool result · `toolu_01EnnfGByT1o9fmL6K5jTw1z`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loading SWE-Agent trajectories...\\n  5000 trajectories\\nLoading SWE-Agent windows...\\n  59496 total, 54809 non-abstain\\n  Conf>=2: 15401, Train=10634, Val=2943, Test=1824\\nExtracting SWE structural features...\\n  Test: N=1824 (stag=485, prog=1339)\\n\\n=== Comparison 1: RF vs Probe (SWE in-domain) ===\\nTraining RF (n_estimators=100, max_depth=10)...\\n  RF macro-F1: 0.9951\\nLoading SWE embeddings...\\nLoading probe (checkpoints/best_model.pt)...\\n  Probe macro-F1: 0.9055\\nPaired bootstrap (10K)...\\n  RF=0.9951, Probe=0.9055, delta=+8.96pp, CI=[7.44,10.57], p=0.0\\n\\n=== Loading OH data ===\\n  OH conf>=2: 43366 windows\\n  OH test split: N=6122\\nBuilding OH window lookup...\\n  154743 window entries\\nLoading OH trajectories...\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cd54d93-f54a-41e6-85ad-3d6c179602e7",
  "uuid": "320cd4e2-9c7a-4c5d-8959-1412b9a930a6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"Loading SWE-Agent trajectories...\\\\n  5000 trajectories\\\\nLoading SWE-Agent windows...\\\\n  59496 total, 54809 non-abstain\\\\n  Conf>=2: 15401, Train=10634, Val=2943, Test=1824\\\\nExtracting SWE structural features...\\\\n  Test: N=1824 (stag=485, prog=1339)\\\\n\\\\n=== Comparison 1: RF vs Probe (SWE in-domain) ===\\\\nTraining RF (n_estimators=100, max_depth=10)...\\\\n  RF macro-F1: 0.9951\\\\nLoading SWE embeddings...\\\\nLoading probe (checkpoints/best_model.pt)...\\\\n  Probe macro-F1: 0.9055\\\\nPaired bootstrap (10K)...\\\\n  RF=0.9951, Probe=0.9055, delta=+8.96pp, CI=[7.44,10.57], p=0.0\\\\n\\\\n=== Loading OH data ===\\\\n  OH conf>=2: 43366 windows\\\\n  OH test split: N=6122\\\\nBuilding OH window lookup...\\\\n  154743 window entries\\\\nLoading OH trajectories...\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.3}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"Loading SWE-Agent trajectories...\\n  5000 trajectories\\nLoading SWE-Agent windows...\\n  59496 total, 54809 non-abstain\\n  Conf>=2: 15401, Train=10634, Val=2943, Test=1824\\nExtracting SWE structural features...\\n  Test: N=1824 (stag=485, prog=1339)\\n\\n=== Comparison 1: RF vs Probe (SWE in-domain) ===\\nTraining RF (n_estimators=100, max_depth=10)...\\n  RF macro-F1: 0.9951\\nLoading SWE embeddings...\\nLoading probe (checkpoints/best_model.pt)...\\n  Probe macro-F1: 0.9055\\nPaired bootstrap (10K)...\\n  RF=0.9951, Probe=0.9055, delta=+8.96pp, CI=[7.44,10.57], p=0.0\\n\\n=== Loading OH data ===\\n  OH conf>=2: 43366 windows\\n  OH test split: N=6122\\nBuilding OH window lookup...\\n  154743 window entries\\nLoading OH trajectories...\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 251_

<details><summary>Logged reasoning block</summary>

```text
Comparison 1 completed:
- RF=0.9951, Probe=0.9055, delta=+8.96pp, CI=[7.44,10.57], p=0.0

Now loading OH data. Let me wait for more progress.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cd54d93-f54a-41e6-85ad-3d6c179602e7",
  "uuid": "863e4bb6-29d8-4e3c-981f-f1a8c8e18c1d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011PVMTGRB5XcTKkpTHJTPR5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 635,
      "cache_read_input_tokens": 155568,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 635
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


### Assistant

_source line 252_

Comparison 1 done. Waiting for OH comparisons.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cd54d93-f54a-41e6-85ad-3d6c179602e7",
  "uuid": "a65caaae-dfde-46b6-bb48-a4ec1caf6249",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011PVMTGRB5XcTKkpTHJTPR5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 635,
      "cache_read_input_tokens": 155568,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 635
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


### Tool call

_source line 253_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_012t9eawELqRzCrnh4mZnP7M`</summary>

```json
{
  "server": "bjb2-23165",
  "command": "tail -30 /tmp/bootstrap_log.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cd54d93-f54a-41e6-85ad-3d6c179602e7",
  "uuid": "7341dedf-9088-442a-a791-0a2d7af0d9b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011PVMTGRB5XcTKkpTHJTPR5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 635,
      "cache_read_input_tokens": 155568,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 635
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

_source line 254 · 2026-05-15T05:15:22.309Z_

<details><summary>↩ Tool result · `toolu_012t9eawELqRzCrnh4mZnP7M`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\nResults saved to /root/autodl-tmp/agent_progress_probe/bootstrap_table2_matched.json\\n\\n======================================================================\\nSUMMARY\\n======================================================================\\n\\ncomparison_1_rf_vs_probe_indomain:\\n  Scope: SWE-Agent conf>=2 test split, N=1824\\n  Structural RF: F1=0.9951\\n  ProgressProbe (GRU): F1=0.9055\\n  Delta: +8.96pp\\n  95% CI: [7.44, 10.57]\\n  p-value: 0.0\\n\\ncomparison_2_gb_vs_probe_zeroshot_oh:\\n  Scope: OH conf>=2 test split, N=6122\\n  Structural GB: F1=0.9929\\n  ProgressProbe zero-shot: F1=0.5984\\n  Delta: +39.44pp\\n  95% CI: [37.86, 41.04]\\n  p-value: 0.0\\n\\ncomparison_3_gb_vs_probe_finetuned_oh:\\n  Scope: OH conf>=2 test split, N=6122\\n  Structural GB: F1=0.9929\\n  ProgressProbe fine-tuned: F1=0.9763\\n  Delta: +1.65pp\\n  95% CI: [1.11, 2.23]\\n  p-value: 0.0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cd54d93-f54a-41e6-85ad-3d6c179602e7",
  "uuid": "e0e6d0d5-cb78-4725-ada5-5d659107844b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\nResults saved to /root/autodl-tmp/agent_progress_probe/bootstrap_table2_matched.json\\\\n\\\\n======================================================================\\\\nSUMMARY\\\\n======================================================================\\\\n\\\\ncomparison_1_rf_vs_probe_indomain:\\\\n  Scope: SWE-Agent conf>=2 test split, N=1824\\\\n  Structural RF: F1=0.9951\\\\n  ProgressProbe (GRU): F1=0.9055\\\\n  Delta: +8.96pp\\\\n  95% CI: [7.44, 10.57]\\\\n  p-value: 0.0\\\\n\\\\ncomparison_2_gb_vs_probe_zeroshot_oh:\\\\n  Scope: OH conf>=2 test split, N=6122\\\\n  Structural GB: F1=0.9929\\\\n  ProgressProbe zero-shot: F1=0.5984\\\\n  Delta: +39.44pp\\\\n  95% CI: [37.86, 41.04]\\\\n  p-value: 0.0\\\\n\\\\ncomparison_3_gb_vs_probe_finetuned_oh:\\\\n  Scope: OH conf>=2 test split, N=6122\\\\n  Structural GB: F1=0.9929\\\\n  ProgressProbe fine-tuned: F1=0.9763\\\\n  Delta: +1.65pp\\\\n  95% CI: [1.11, 2.23]\\\\n  p-value: 0.0\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.31}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\nResults saved to /root/autodl-tmp/agent_progress_probe/bootstrap_table2_matched.json\\n\\n======================================================================\\nSUMMARY\\n======================================================================\\n\\ncomparison_1_rf_vs_probe_indomain:\\n  Scope: SWE-Agent conf>=2 test split, N=1824\\n  Structural RF: F1=0.9951\\n  ProgressProbe (GRU): F1=0.9055\\n  Delta: +8.96pp\\n  95% CI: [7.44, 10.57]\\n  p-value: 0.0\\n\\ncomparison_2_gb_vs_probe_zeroshot_oh:\\n  Scope: OH conf>=2 test split, N=6122\\n  Structural GB: F1=0.9929\\n  ProgressProbe zero-shot: F1=0.5984\\n  Delta: +39.44pp\\n  95% CI: [37.86, 41.04]\\n  p-value: 0.0\\n\\ncomparison_3_gb_vs_probe_finetuned_oh:\\n  Scope: OH conf>=2 test split, N=6122\\n  Structural GB: F1=0.9929\\n  ProgressProbe fine-tuned: F1=0.9763\\n  Delta: +1.65pp\\n  95% CI: [1.11, 2.23]\\n  p-value: 0.0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 255_

All 3 comparisons completed. Let me read the full JSON output.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cd54d93-f54a-41e6-85ad-3d6c179602e7",
  "uuid": "4180450a-f584-431e-aa75-42827613331d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XnM89thuEhHSQrYBwpGHrA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 637,
      "cache_read_input_tokens": 156203,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 637
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

_source line 256_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01WufMUBf2dRKUroth3CF5wz`</summary>

```json
{
  "server": "bjb2-23165",
  "command": "cat /root/autodl-tmp/agent_progress_probe/bootstrap_table2_matched.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cd54d93-f54a-41e6-85ad-3d6c179602e7",
  "uuid": "61d93d09-44cd-4097-8d82-c158853dc91d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XnM89thuEhHSQrYBwpGHrA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 637,
      "cache_read_input_tokens": 156203,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 637
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

_source line 257 · 2026-05-15T05:15:26.363Z_

<details><summary>↩ Tool result · `toolu_01WufMUBf2dRKUroth3CF5wz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"comparison_1_rf_vs_probe_indomain\\\": {\\n    \\\"scope\\\": \\\"SWE-Agent conf>=2 test split\\\",\\n    \\\"N\\\": 1824,\\n    \\\"class_dist\\\": {\\n      \\\"stagnation\\\": 485,\\n      \\\"progress\\\": 1339\\n    },\\n    \\\"model_a\\\": \\\"Structural RF\\\",\\n    \\\"model_b\\\": \\\"ProgressProbe (GRU)\\\",\\n    \\\"f1_a\\\": 0.9951,\\n    \\\"f1_b\\\": 0.9055,\\n    \\\"delta_pp\\\": 8.96,\\n    \\\"ci_95\\\": [\\n      7.44,\\n      10.57\\n    ],\\n    \\\"p_value\\\": 0.0,\\n    \\\"table2_ref\\\": {\\n      \\\"f1_a\\\": 0.9951,\\n      \\\"f1_b\\\": 0.9055\\n    }\\n  },\\n  \\\"comparison_2_gb_vs_probe_zeroshot_oh\\\": {\\n    \\\"scope\\\": \\\"OH conf>=2 test split\\\",\\n    \\\"scope_note\\\": \\\"Table 2 GB=0.9674 is on all 150,652 OH windows; this bootstrap uses conf>=2 test split only. GB F1 on this subset differs from Table 2.\\\",\\n    \\\"N\\\": 6122,\\n    \\\"class_dist\\\": {\\n      \\\"stagnation\\\": 1179,\\n      \\\"progress\\\": 4943\\n    },\\n    \\\"model_a\\\": \\\"Structural GB\\\",\\n    \\\"model_b\\\": \\\"ProgressProbe zero-shot\\\",\\n    \\\"f1_a\\\": 0.9929,\\n    \\\"f1_b\\\": 0.5984,\\n    \\\"delta_pp\\\": 39.44,\\n    \\\"ci_95\\\": [\\n      37.86,\\n      41.04\\n    ],\\n    \\\"p_value\\\": 0.0,\\n    \\\"table2_ref\\\": {\\n      \\\"f1_a_all_oh\\\": 0.9674,\\n      \\\"f1_b\\\": 0.598\\n    }\\n  },\\n  \\\"comparison_3_gb_vs_probe_finetuned_oh\\\": {\\n    \\\"scope\\\": \\\"OH conf>=2 test split\\\",\\n    \\\"scope_note\\\": \\\"Same scope as comparison 2. GB retrained on same SWE data.\\\",\\n    \\\"N\\\": 6122,\\n    \\\"class_dist\\\": {\\n      \\\"stagnation\\\": 1179,\\n      \\\"progress\\\": 4943\\n    },\\n    \\\"model_a\\\": \\\"Structural GB\\\",\\n    \\\"model_b\\\": \\\"ProgressProbe fine-tuned\\\",\\n    \\\"f1_a\\\": 0.9929,\\n    \\\"f1_b\\\": 0.9763,\\n    \\\"delta_pp\\\": 1.65,\\n    \\\"ci_95\\\": [\\n      1.11,\\n      2.23\\n    ],\\n    \\\"p_value\\\": 0.0,\\n    \\\"table2_ref\\\": {\\n      \\\"f1_a_all_oh\\\": 0.9674,\\n      \\\"f1_b\\\": 0.976\\n    }\\n  },\\n  \\\"metadata\\\": {\\n    \\\"n_bootstrap\\\": 10000,\\n    \\\"seed\\\": 42,\\n    \\\"timestamp\\\": \\\"2026-05-15T13:15:18.797052\\\",\\n    \\\"note\\\": \\\"Paired bootstrap on Table 2 exact scope\\\",\\n    \\\"rf_hp\\\": {\\n      \\\"n_estimators\\\": 100,\\n      \\\"max_depth\\\": 10\\n    },\\n    \\\"gb_hp\\\": {\\n      \\\"n_estimators\\\": 200,\\n      \\\"learning_rate\\\": 0.05,\\n      \\\"max_depth\\\": 5\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cd54d93-f54a-41e6-85ad-3d6c179602e7",
  "uuid": "27cbc5a0-b264-4cc8-8a31-c55640512545",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"comparison_1_rf_vs_probe_indomain\\\\\\\": {\\\\n    \\\\\\\"scope\\\\\\\": \\\\\\\"SWE-Agent conf>=2 test split\\\\\\\",\\\\n    \\\\\\\"N\\\\\\\": 1824,\\\\n    \\\\\\\"class_dist\\\\\\\": {\\\\n      \\\\\\\"stagnation\\\\\\\": 485,\\\\n      \\\\\\\"progress\\\\\\\": 1339\\\\n    },\\\\n    \\\\\\\"model_a\\\\\\\": \\\\\\\"Structural RF\\\\\\\",\\\\n    \\\\\\\"model_b\\\\\\\": \\\\\\\"ProgressProbe (GRU)\\\\\\\",\\\\n    \\\\\\\"f1_a\\\\\\\": 0.9951,\\\\n    \\\\\\\"f1_b\\\\\\\": 0.9055,\\\\n    \\\\\\\"delta_pp\\\\\\\": 8.96,\\\\n    \\\\\\\"ci_95\\\\\\\": [\\\\n      7.44,\\\\n      10.57\\\\n    ],\\\\n    \\\\\\\"p_value\\\\\\\": 0.0,\\\\n    \\\\\\\"table2_ref\\\\\\\": {\\\\n      \\\\\\\"f1_a\\\\\\\": 0.9951,\\\\n      \\\\\\\"f1_b\\\\\\\": 0.9055\\\\n    }\\\\n  },\\\\n  \\\\\\\"comparison_2_gb_vs_probe_zeroshot_oh\\\\\\\": {\\\\n    \\\\\\\"scope\\\\\\\": \\\\\\\"OH conf>=2 test split\\\\\\\",\\\\n    \\\\\\\"scope_note\\\\\\\": \\\\\\\"Table 2 GB=0.9674 is on all 150,652 OH windows; this bootstrap uses conf>=2 test split only. GB F1 on this subset differs from Table 2.\\\\\\\",\\\\n    \\\\\\\"N\\\\\\\": 6122,\\\\n    \\\\\\\"class_dist\\\\\\\": {\\\\n      \\\\\\\"stagnation\\\\\\\": 1179,\\\\n      \\\\\\\"progress\\\\\\\": 4943\\\\n    },\\\\n    \\\\\\\"model_a\\\\\\\": \\\\\\\"Structural GB\\\\\\\",\\\\n    \\\\\\\"model_b\\\\\\\": \\\\\\\"ProgressProbe zero-shot\\\\\\\",\\\\n    \\\\\\\"f1_a\\\\\\\": 0.9929,\\\\n    \\\\\\\"f1_b\\\\\\\": 0.5984,\\\\n    \\\\\\\"delta_pp\\\\\\\": 39.44,\\\\n    \\\\\\\"ci_95\\\\\\\": [\\\\n      37.86,\\\\n      41.04\\\\n    ],\\\\n    \\\\\\\"p_value\\\\\\\": 0.0,\\\\n    \\\\\\\"table2_ref\\\\\\\": {\\\\n      \\\\\\\"f1_a_all_oh\\\\\\\": 0.9674,\\\\n      \\\\\\\"f1_b\\\\\\\": 0.598\\\\n    }\\\\n  },\\\\n  \\\\\\\"comparison_3_gb_vs_probe_finetuned_oh\\\\\\\": {\\\\n    \\\\\\\"scope\\\\\\\": \\\\\\\"OH conf>=2 test split\\\\\\\",\\\\n    \\\\\\\"scope_note\\\\\\\": \\\\\\\"Same scope as comparison 2. GB retrained on same SWE data.\\\\\\\",\\\\n    \\\\\\\"N\\\\\\\": 6122,\\\\n    \\\\\\\"class_dist\\\\\\\": {\\\\n      \\\\\\\"stagnation\\\\\\\": 1179,\\\\n      \\\\\\\"progress\\\\\\\": 4943\\\\n    },\\\\n    \\\\\\\"model_a\\\\\\\": \\\\\\\"Structural GB\\\\\\\",\\\\n    \\\\\\\"model_b\\\\\\\": \\\\\\\"ProgressProbe fine-tuned\\\\\\\",\\\\n    \\\\\\\"f1_a\\\\\\\": 0.9929,\\\\n    \\\\\\\"f1_b\\\\\\\": 0.9763,\\\\n    \\\\\\\"delta_pp\\\\\\\": 1.65,\\\\n    \\\\\\\"ci_95\\\\\\\": [\\\\n      1.11,\\\\n      2.23\\\\n    ],\\\\n    \\\\\\\"p_value\\\\\\\": 0.0,\\\\n    \\\\\\\"table2_ref\\\\\\\": {\\\\n      \\\\\\\"f1_a_all_oh\\\\\\\": 0.9674,\\\\n      \\\\\\\"f1_b\\\\\\\": 0.976\\\\n    }\\\\n  },\\\\n  \\\\\\\"metadata\\\\\\\": {\\\\n    \\\\\\\"n_bootstrap\\\\\\\": 10000,\\\\n    \\\\\\\"seed\\\\\\\": 42,\\\\n    \\\\\\\"timestamp\\\\\\\": \\\\\\\"2026-05-15T13:15:18.797052\\\\\\\",\\\\n    \\\\\\\"note\\\\\\\": \\\\\\\"Paired bootstrap on Table 2 exact scope\\\\\\\",\\\\n    \\\\\\\"rf_hp\\\\\\\": {\\\\n      \\\\\\\"n_estimators\\\\\\\": 100,\\\\n      \\\\\\\"max_depth\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"gb_hp\\\\\\\": {\\\\n      \\\\\\\"n_estimators\\\\\\\": 200,\\\\n      \\\\\\\"learning_rate\\\\\\\": 0.05,\\\\n      \\\\\\\"max_depth\\\\\\\": 5\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.31}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"comparison_1_rf_vs_probe_indomain\\\": {\\n    \\\"scope\\\": \\\"SWE-Agent conf>=2 test split\\\",\\n    \\\"N\\\": 1824,\\n    \\\"class_dist\\\": {\\n      \\\"stagnation\\\": 485,\\n      \\\"progress\\\": 1339\\n    },\\n    \\\"model_a\\\": \\\"Structural RF\\\",\\n    \\\"model_b\\\": \\\"ProgressProbe (GRU)\\\",\\n    \\\"f1_a\\\": 0.9951,\\n    \\\"f1_b\\\": 0.9055,\\n    \\\"delta_pp\\\": 8.96,\\n    \\\"ci_95\\\": [\\n      7.44,\\n      10.57\\n    ],\\n    \\\"p_value\\\": 0.0,\\n    \\\"table2_ref\\\": {\\n      \\\"f1_a\\\": 0.9951,\\n      \\\"f1_b\\\": 0.9055\\n    }\\n  },\\n  \\\"comparison_2_gb_vs_probe_zeroshot_oh\\\": {\\n    \\\"scope\\\": \\\"OH conf>=2 test split\\\",\\n    \\\"scope_note\\\": \\\"Table 2 GB=0.9674 is on all 150,652 OH windows; this bootstrap uses conf>=2 test split only. GB F1 on this subset differs from Table 2.\\\",\\n    \\\"N\\\": 6122,\\n    \\\"class_dist\\\": {\\n      \\\"stagnation\\\": 1179,\\n      \\\"progress\\\": 4943\\n    },\\n    \\\"model_a\\\": \\\"Structural GB\\\",\\n    \\\"model_b\\\": \\\"ProgressProbe zero-shot\\\",\\n    \\\"f1_a\\\": 0.9929,\\n    \\\"f1_b\\\": 0.5984,\\n    \\\"delta_pp\\\": 39.44,\\n    \\\"ci_95\\\": [\\n      37.86,\\n      41.04\\n    ],\\n    \\\"p_value\\\": 0.0,\\n    \\\"table2_ref\\\": {\\n      \\\"f1_a_all_oh\\\": 0.9674,\\n      \\\"f1_b\\\": 0.598\\n    }\\n  },\\n  \\\"comparison_3_gb_vs_probe_finetuned_oh\\\": {\\n    \\\"scope\\\": \\\"OH conf>=2 test split\\\",\\n    \\\"scope_note\\\": \\\"Same scope as comparison 2. GB retrained on same SWE data.\\\",\\n    \\\"N\\\": 6122,\\n    \\\"class_dist\\\": {\\n      \\\"stagnation\\\": 1179,\\n      \\\"progress\\\": 4943\\n    },\\n    \\\"model_a\\\": \\\"Structural GB\\\",\\n    \\\"model_b\\\": \\\"ProgressProbe fine-tuned\\\",\\n    \\\"f1_a\\\": 0.9929,\\n    \\\"f1_b\\\": 0.9763,\\n    \\\"delta_pp\\\": 1.65,\\n    \\\"ci_95\\\": [\\n      1.11,\\n      2.23\\n    ],\\n    \\\"p_value\\\": 0.0,\\n    \\\"table2_ref\\\": {\\n      \\\"f1_a_all_oh\\\": 0.9674,\\n      \\\"f1_b\\\": 0.976\\n    }\\n  },\\n  \\\"metadata\\\": {\\n    \\\"n_bootstrap\\\": 10000,\\n    \\\"seed\\\": 42,\\n    \\\"timestamp\\\": \\\"2026-05-15T13:15:18.797052\\\",\\n    \\\"note\\\": \\\"Paired bootstrap on Table 2 exact scope\\\",\\n    \\\"rf_hp\\\": {\\n      \\\"n_estimators\\\": 100,\\n      \\\"max_depth\\\": 10\\n    },\\n    \\\"gb_hp\\\": {\\n      \\\"n_estimators\\\": 200,\\n      \\\"learning_rate\\\": 0.05,\\n      \\\"max_depth\\\": 5\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 258_

Now let me save the JSON locally and register the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cd54d93-f54a-41e6-85ad-3d6c179602e7",
  "uuid": "dc3cb9fd-0272-440f-8439-6b2125aed8d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018he8zk8i9Q4pT2FrWqthbN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1464,
      "cache_read_input_tokens": 156840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1464
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

_source line 259_

<details open><summary>🔧 Tool call — Write · `toolu_014ciTAU7mHQLjZagEEFpWBq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/bootstrap_table2_matched.json",
  "content": "{\n  \"comparison_1_rf_vs_probe_indomain\": {\n    \"scope\": \"SWE-Agent conf>=2 test split\",\n    \"N\": 1824,\n    \"class_dist\": {\n      \"stagnation\": 485,\n      \"progress\": 1339\n    },\n    \"model_a\": \"Structural RF\",\n    \"model_b\": \"ProgressProbe (GRU)\",\n    \"f1_a\": 0.9951,\n    \"f1_b\": 0.9055,\n    \"delta_pp\": 8.96,\n    \"ci_95\": [\n      7.44,\n      10.57\n    ],\n    \"p_value\": 0.0,\n    \"table2_ref\": {\n      \"f1_a\": 0.9951,\n      \"f1_b\": 0.9055\n    }\n  },\n  \"comparison_2_gb_vs_probe_zeroshot_oh\": {\n    \"scope\": \"OH conf>=2 test split\",\n    \"scope_note\": \"Table 2 GB=0.9674 is on all 150,652 OH windows; this bootstrap uses conf>=2 test split only. GB F1 on this subset differs from Table 2.\",\n    \"N\": 6122,\n    \"class_dist\": {\n      \"stagnation\": 1179,\n      \"progress\": 4943\n    },\n    \"model_a\": \"Structural GB\",\n    \"model_b\": \"ProgressProbe zero-shot\",\n    \"f1_a\": 0.9929,\n    \"f1_b\": 0.5984,\n    \"delta_pp\": 39.44,\n    \"ci_95\": [\n      37.86,\n      41.04\n    ],\n    \"p_value\": 0.0,\n    \"table2_ref\": {\n      \"f1_a_all_oh\": 0.9674,\n      \"f1_b\": 0.598\n    }\n  },\n  \"comparison_3_gb_vs_probe_finetuned_oh\": {\n    \"scope\": \"OH conf>=2 test split\",\n    \"scope_note\": \"Same scope as comparison 2. GB retrained on same SWE data.\",\n    \"N\": 6122,\n    \"class_dist\": {\n      \"stagnation\": 1179,\n      \"progress\": 4943\n    },\n    \"model_a\": \"Structural GB\",\n    \"model_b\": \"ProgressProbe fine-tuned\",\n    \"f1_a\": 0.9929,\n    \"f1_b\": 0.9763,\n    \"delta_pp\": 1.65,\n    \"ci_95\": [\n      1.11,\n      2.23\n    ],\n    \"p_value\": 0.0,\n    \"table2_ref\": {\n      \"f1_a_all_oh\": 0.9674,\n      \"f1_b\": 0.976\n    }\n  },\n  \"metadata\": {\n    \"n_bootstrap\": 10000,\n    \"seed\": 42,\n    \"timestamp\": \"2026-05-15T13:15:18.797052\",\n    \"note\": \"Paired bootstrap on Table 2 exact scope\",\n    \"rf_hp\": {\n      \"n_estimators\": 100,\n      \"max_depth\": 10\n    },\n    \"gb_hp\": {\n      \"n_estimators\": 200,\n      \"learning_rate\": 0.05,\n      \"max_depth\": 5\n    }\n  }\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cd54d93-f54a-41e6-85ad-3d6c179602e7",
  "uuid": "e6f02ac9-2d9b-48cf-b5ef-5567fcb462a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018he8zk8i9Q4pT2FrWqthbN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1464,
      "cache_read_input_tokens": 156840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1464
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

_source line 260 · 2026-05-15T05:15:43.063Z_

<details><summary>↩ Tool result · `toolu_014ciTAU7mHQLjZagEEFpWBq`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/bootstrap_table2_matched.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cd54d93-f54a-41e6-85ad-3d6c179602e7",
  "uuid": "ed5a9516-c831-4637-bba4-8bd1f9fc5a95",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/bootstrap_table2_matched.json",
    "content": "{\n  \"comparison_1_rf_vs_probe_indomain\": {\n    \"scope\": \"SWE-Agent conf>=2 test split\",\n    \"N\": 1824,\n    \"class_dist\": {\n      \"stagnation\": 485,\n      \"progress\": 1339\n    },\n    \"model_a\": \"Structural RF\",\n    \"model_b\": \"ProgressProbe (GRU)\",\n    \"f1_a\": 0.9951,\n    \"f1_b\": 0.9055,\n    \"delta_pp\": 8.96,\n    \"ci_95\": [\n      7.44,\n      10.57\n    ],\n    \"p_value\": 0.0,\n    \"table2_ref\": {\n      \"f1_a\": 0.9951,\n      \"f1_b\": 0.9055\n    }\n  },\n  \"comparison_2_gb_vs_probe_zeroshot_oh\": {\n    \"scope\": \"OH conf>=2 test split\",\n    \"scope_note\": \"Table 2 GB=0.9674 is on all 150,652 OH windows; this bootstrap uses conf>=2 test split only. GB F1 on this subset differs from Table 2.\",\n    \"N\": 6122,\n    \"class_dist\": {\n      \"stagnation\": 1179,\n      \"progress\": 4943\n    },\n    \"model_a\": \"Structural GB\",\n    \"model_b\": \"ProgressProbe zero-shot\",\n    \"f1_a\": 0.9929,\n    \"f1_b\": 0.5984,\n    \"delta_pp\": 39.44,\n    \"ci_95\": [\n      37.86,\n      41.04\n    ],\n    \"p_value\": 0.0,\n    \"table2_ref\": {\n      \"f1_a_all_oh\": 0.9674,\n      \"f1_b\": 0.598\n    }\n  },\n  \"comparison_3_gb_vs_probe_finetuned_oh\": {\n    \"scope\": \"OH conf>=2 test split\",\n    \"scope_note\": \"Same scope as comparison 2. GB retrained on same SWE data.\",\n    \"N\": 6122,\n    \"class_dist\": {\n      \"stagnation\": 1179,\n      \"progress\": 4943\n    },\n    \"model_a\": \"Structural GB\",\n    \"model_b\": \"ProgressProbe fine-tuned\",\n    \"f1_a\": 0.9929,\n    \"f1_b\": 0.9763,\n    \"delta_pp\": 1.65,\n    \"ci_95\": [\n      1.11,\n      2.23\n    ],\n    \"p_value\": 0.0,\n    \"table2_ref\": {\n      \"f1_a_all_oh\": 0.9674,\n      \"f1_b\": 0.976\n    }\n  },\n  \"metadata\": {\n    \"n_bootstrap\": 10000,\n    \"seed\": 42,\n    \"timestamp\": \"2026-05-15T13:15:18.797052\",\n    \"note\": \"Paired bootstrap on Table 2 exact scope\",\n    \"rf_hp\": {\n      \"n_estimators\": 100,\n      \"max_depth\": 10\n    },\n    \"gb_hp\": {\n      \"n_estimators\": 200,\n      \"learning_rate\": 0.05,\n      \"max_depth\": 5\n    }\n  }\n}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---


### Tool call

_source line 261_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_017faeFjgAPXexcxRzKK76tP`</summary>

```json
{
  "name": "bootstrap_table2_matched",
  "type": "data",
  "description": "Paired bootstrap test (10K resamples, seed=42) for 3 Table 2 comparisons: (1) RF vs Probe in-domain SWE conf>=2 test N=1824, (2) GB vs Probe zero-shot OH conf>=2 test N=6122, (3) GB vs Probe fine-tuned OH conf>=2 test N=6122. All p<0.001.",
  "project": "agent_progress_probe",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/bootstrap_table2_matched.json",
  "tags": [
    "bootstrap",
    "table2",
    "significance",
    "paired-test"
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
  "session_id": "2cd54d93-f54a-41e6-85ad-3d6c179602e7",
  "uuid": "d8a54019-658b-47c3-bcd3-853ef43de87d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FL6nUYd9doKquVptnEEoFp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1157,
      "cache_read_input_tokens": 158304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1157
      },
      "output_tokens": 77,
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

_source line 262 · 2026-05-15T05:15:51.513Z_

<details><summary>↩ Tool result · `toolu_017faeFjgAPXexcxRzKK76tP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_4df78b\", \"name\": \"bootstrap_table2_matched\", \"type\": \"data\", \"description\": \"Paired bootstrap test (10K resamples, seed=42) for 3 Table 2 comparisons: (1) RF vs Probe in-domain SWE conf>=2 test N=1824, (2) GB vs Probe zero-shot OH conf>=2 test N=6122, (3) GB vs Probe fine-tuned OH conf>=2 test N=6122. All p<0.001.\", \"path\": \"projects/agent_progress_probe/artifacts/_project/data/bootstrap_table2_matched.json\", \"url\": null, \"project\": \"agent_progress_probe\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T05:15:51.316076+00:00\", \"tags\": [\"bootstrap\", \"table2\", \"significance\", \"paired-test\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cd54d93-f54a-41e6-85ad-3d6c179602e7",
  "uuid": "5c7c4ad9-05c0-4839-a590-0d6e3910edf6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260515_4df78b\\\", \\\"name\\\": \\\"bootstrap_table2_matched\\\", \\\"type\\\": \\\"data\\\", \\\"description\\\": \\\"Paired bootstrap test (10K resamples, seed=42) for 3 Table 2 comparisons: (1) RF vs Probe in-domain SWE conf>=2 test N=1824, (2) GB vs Probe zero-shot OH conf>=2 test N=6122, (3) GB vs Probe fine-tuned OH conf>=2 test N=6122. All p<0.001.\\\", \\\"path\\\": \\\"projects/agent_progress_probe/artifacts/_project/data/bootstrap_table2_matched.json\\\", \\\"url\\\": null, \\\"project\\\": \\\"agent_progress_probe\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-15T05:15:51.316076+00:00\\\", \\\"tags\\\": [\\\"bootstrap\\\", \\\"table2\\\", \\\"significance\\\", \\\"paired-test\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_4df78b\", \"name\": \"bootstrap_table2_matched\", \"type\": \"data\", \"description\": \"Paired bootstrap test (10K resamples, seed=42) for 3 Table 2 comparisons: (1) RF vs Probe in-domain SWE conf>=2 test N=1824, (2) GB vs Probe zero-shot OH conf>=2 test N=6122, (3) GB vs Probe fine-tuned OH conf>=2 test N=6122. All p<0.001.\", \"path\": \"projects/agent_progress_probe/artifacts/_project/data/bootstrap_table2_matched.json\", \"url\": null, \"project\": \"agent_progress_probe\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T05:15:51.316076+00:00\", \"tags\": [\"bootstrap\", \"table2\", \"significance\", \"paired-test\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 263_

完成。3 组 paired bootstrap 结果：

| Comparison | Model A | Model B | F1_A | F1_B | Δ (pp) | 95% CI | p |
|---|---|---|---|---|---|---|---|
| 1. In-domain SWE (N=1,824) | RF | Probe | 0.9951 | 0.9055 | +8.96 | [7.44, 10.57] | <0.001 |
| 2. Cross-agent OH zero-shot (N=6,122) | GB | Probe-ZS | 0.9929 | 0.5984 | +39.44 | [37.86, 41.04] | <0.001 |
| 3. Cross-agent OH fine-tuned (N=6,122) | GB | Probe-FT | 0.9929 | 0.9763 | +1.65 | [1.11, 2.23] | <0.001 |

验证：
- Comparison 1 的 F1_A=0.9951、F1_B=0.9055 与 Table 2 完全一致
- Comparison 2 的 Probe-ZS=0.5984 与 Table 2 的 0.598 一致；GB 在 conf≥2 test split 上为 0.9929（Table 2 报告的 0.9674 是在 all 150,652 OH windows 上的值，scope 不同已注明）
- Comparison 3 的 Probe-FT=0.9763 与 Table 2 的 0.976 一致
- 所有 3 组差异均显著（p<0.001）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cd54d93-f54a-41e6-85ad-3d6c179602e7",
  "uuid": "f77314dd-1f00-4ad6-9177-06332a31507e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D7cb2Sr4N8RFWLqDQxqPMQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 644,
      "cache_read_input_tokens": 159461,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 644
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

_source line 264_

完成。3 组 paired bootstrap 结果：

| Comparison | Model A | Model B | F1_A | F1_B | Δ (pp) | 95% CI | p |
|---|---|---|---|---|---|---|---|
| 1. In-domain SWE (N=1,824) | RF | Probe | 0.9951 | 0.9055 | +8.96 | [7.44, 10.57] | <0.001 |
| 2. Cross-agent OH zero-shot (N=6,122) | GB | Probe-ZS | 0.9929 | 0.5984 | +39.44 | [37.86, 41.04] | <0.001 |
| 3. Cross-agent OH fine-tuned (N=6,122) | GB | Probe-FT | 0.9929 | 0.9763 | +1.65 | [1.11, 2.23] | <0.001 |

验证：
- Comparison 1 的 F1_A=0.9951、F1_B=0.9055 与 Table 2 完全一致
- Comparison 2 的 Probe-ZS=0.5984 与 Table 2 的 0.598 一致；GB 在 conf≥2 test split 上为 0.9929（Table 2 报告的 0.9674 是在 all 150,652 OH windows 上的值，scope 不同已注明）
- Comparison 3 的 Probe-FT=0.9763 与 Table 2 的 0.976 一致
- 所有 3 组差异均显著（p<0.001）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 1497425,
  "duration_api_ms": 1328900,
  "num_turns": 94,
  "stop_reason": "end_turn",
  "session_id": "2cd54d93-f54a-41e6-85ad-3d6c179602e7",
  "total_cost_usd": 6.064789499999998,
  "usage": {
    "input_tokens": 66,
    "cache_creation_input_tokens": 148264,
    "cache_read_input_tokens": 6631875,
    "output_tokens": 72766,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 148264,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 443,
        "cache_read_input_tokens": 159461,
        "cache_creation_input_tokens": 644,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 644
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2627,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002722,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 66,
      "outputTokens": 72766,
      "cacheReadInputTokens": 6631875,
      "cacheCreationInputTokens": 148264,
      "webSearchRequests": 0,
      "costUSD": 6.062067499999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "4c840de7-c50c-4599-916b-86db5dc42b38"
}
```

</details>

---
