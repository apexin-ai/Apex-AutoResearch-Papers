# eval oracle folio regen — Part 2 of 2

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../eval-oracle-folio-regen.md) · [Structured JSON](../../../sessions/1b/1b28ad36c69ec52e971c.json)

## Round 1

### Tool call

_source line 178_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_015nfXx4pMVFex94D8Qkh4J9`</summary>

```json
{
  "name": "exp-031 Oracle SICA Summary",
  "type": "report",
  "description": "Oracle SICA results for FOLIO-204 using gold FOL + Z3 entailment on exp-026 traces. Oracle=89.71% vs SC=75.49% (+14.22pp, p=2.0e-07).",
  "project": "symb_invariant_consensus",
  "exp_id": "exp-031-oracle-folio-regen",
  "content": "{\"n\":204,\"k\":12,\"oracle_sica_accuracy\":0.8971,\"sc_accuracy\":0.7549,\"sica_self_accuracy\":0.7451,\"oracle_vs_sc_delta_pp\":14.22,\"oracle_vs_sica_delta_pp\":15.2,\"mcnemar_p_oracle_vs_sc\":2.0024e-07,\"mcnemar_b_c\":{\"b\":29,\"c\":0},\"z3_gold_agreement\":0.951,\"fol_parse_success\":1.0,\"per_answer_type\":{\"True\":{\"n\":72,\"oracle_acc\":0.9722,\"sc_acc\":0.9306},\"False\":{\"n\":63,\"oracle_acc\":0.9365,\"sc_acc\":0.873},\"Unknown\":{\"n\":69,\"oracle_acc\":0.7826,\"sc_acc\":0.4638}},\"comparison_exp021\":{\"exp021_oracle\":0.8824,\"exp021_sc\":0.7941,\"exp031_oracle\":0.8971,\"exp031_sc\":0.7549}}",
  "content_filename": "exp031_oracle_summary.json",
  "tags": [
    "oracle",
    "folio",
    "z3",
    "gold-fol"
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
  "session_id": "313c3feb-1493-4c66-ba8a-5c348c2e5f55",
  "uuid": "7c04eb52-b605-4596-a3c5-f5f8a2ab7a90",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CXytB2qu5sdSNeoVtWgEsj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1272,
      "cache_read_input_tokens": 137820,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1272
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

_source line 179 · 2026-05-18T15:50:00.810Z_

<details><summary>↩ Tool result · reported error · `toolu_015nfXx4pMVFex94D8Qkh4J9`</summary>

```text
Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'n': 204, 'k': 12, 'orac...1, 'exp031_sc': 0.7549}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "313c3feb-1493-4c66-ba8a-5c348c2e5f55",
  "uuid": "4c3a1514-e950-4bae-8303-ca1892579a77",
  "tool_use_result": "Error: Error executing tool register_artifact: 1 validation error for register_artifactArguments\ncontent\n  Input should be a valid string [type=string_type, input_value={'n': 204, 'k': 12, 'orac...1, 'exp031_sc': 0.7549}}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"
}
```

</details>

---


### Tool call

_source line 180_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_016cmPeNRhEjA9RLH2s2SgA9`</summary>

```json
{
  "name": "exp-031 Oracle SICA Summary",
  "type": "report",
  "description": "Oracle SICA results for FOLIO-204 using gold FOL + Z3 entailment on exp-026 traces. Oracle=89.71% vs SC=75.49% (+14.22pp, p=2.0e-07).",
  "project": "symb_invariant_consensus",
  "exp_id": "exp-031-oracle-folio-regen",
  "content": "{\"n\":204,\"k\":12,\"oracle_sica_accuracy\":0.8971,\"sc_accuracy\":0.7549,\"sica_self_accuracy\":0.7451,\"oracle_vs_sc_delta_pp\":14.22,\"oracle_vs_sica_delta_pp\":15.2,\"mcnemar_p_oracle_vs_sc\":\"2.0024e-07\",\"mcnemar_b_c\":{\"b\":29,\"c\":0},\"z3_gold_agreement\":0.951,\"fol_parse_success\":1.0,\"per_answer_type\":{\"True\":{\"n\":72,\"oracle_acc\":0.9722,\"sc_acc\":0.9306},\"False\":{\"n\":63,\"oracle_acc\":0.9365,\"sc_acc\":0.873},\"Unknown\":{\"n\":69,\"oracle_acc\":0.7826,\"sc_acc\":0.4638}},\"comparison_exp021\":{\"exp021_oracle\":0.8824,\"exp021_sc\":0.7941,\"exp031_oracle\":0.8971,\"exp031_sc\":0.7549}}",
  "content_filename": "exp031_oracle_summary.json",
  "tags": [
    "oracle",
    "folio",
    "z3",
    "gold-fol"
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
  "session_id": "313c3feb-1493-4c66-ba8a-5c348c2e5f55",
  "uuid": "a0940dc4-af7d-455a-8a8a-60b5513085fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TzQkiDpak5cGkKfcHVVDPN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 673,
      "cache_read_input_tokens": 139092,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 673
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

_source line 181 · 2026-05-18T15:50:07.543Z_

<details><summary>↩ Tool result · reported error · `toolu_016cmPeNRhEjA9RLH2s2SgA9`</summary>

```text
Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'n': 204, 'k': 12, 'orac...1, 'exp031_sc': 0.7549}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "313c3feb-1493-4c66-ba8a-5c348c2e5f55",
  "uuid": "40a5ff44-882d-44c2-971c-ff9ff471a6ca",
  "tool_use_result": "Error: Error executing tool register_artifact: 1 validation error for register_artifactArguments\ncontent\n  Input should be a valid string [type=string_type, input_value={'n': 204, 'k': 12, 'orac...1, 'exp031_sc': 0.7549}}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"
}
```

</details>

---


### Tool call

_source line 182_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01NK4DSXfArjFHQSNXnBckHz`</summary>

```json
{
  "name": "exp-031 Oracle SICA Summary",
  "type": "report",
  "description": "Oracle SICA results for FOLIO-204 using gold FOL + Z3 entailment on exp-026 traces. Oracle=89.71% vs SC=75.49% (+14.22pp, p=2.0e-07).",
  "project": "symb_invariant_consensus",
  "exp_id": "exp-031-oracle-folio-regen",
  "content": "Oracle SICA (exp-031): 89.71% (183/204), SC: 75.49% (154/204), SICA(self): 74.51% (152/204). Delta +14.22pp, McNemar p=2.0e-07, b=29 c=0. Z3 gold agreement 95.10% (194/204), FOL parse 204/204. Per-type: True 97.2%/93.1%, False 93.6%/87.3%, Unknown 78.3%/46.4%. Results at /root/symb_invariant_consensus/results/oracle_folio_regen/exp031_results.json",
  "content_filename": "exp031_oracle_summary.txt",
  "tags": [
    "oracle",
    "folio",
    "z3",
    "gold-fol"
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
  "session_id": "313c3feb-1493-4c66-ba8a-5c348c2e5f55",
  "uuid": "ff120023-0c47-4d36-8cbc-87557a8c68ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DnkHwRcxeBqfFP7r8t9igZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 673,
      "cache_read_input_tokens": 139765,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 673
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

_source line 183 · 2026-05-18T15:50:14.770Z_

<details><summary>↩ Tool result · `toolu_01NK4DSXfArjFHQSNXnBckHz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260518_5c50be\", \"name\": \"exp-031 Oracle SICA Summary\", \"type\": \"report\", \"description\": \"Oracle SICA results for FOLIO-204 using gold FOL + Z3 entailment on exp-026 traces. Oracle=89.71% vs SC=75.49% (+14.22pp, p=2.0e-07).\", \"path\": \"projects/symb_invariant_consensus/artifacts/exp-031-oracle-folio-regen/report/exp031_oracle_summary.txt\", \"url\": null, \"project\": \"symb_invariant_consensus\", \"exp_id\": \"exp-031-oracle-folio-regen\", \"skill\": \"\", \"created_at\": \"2026-05-18T15:50:14.631232+00:00\", \"tags\": [\"oracle\", \"folio\", \"z3\", \"gold-fol\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "313c3feb-1493-4c66-ba8a-5c348c2e5f55",
  "uuid": "d1f101e3-bbfe-4391-936d-8ea008f8fc3d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260518_5c50be\\\", \\\"name\\\": \\\"exp-031 Oracle SICA Summary\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Oracle SICA results for FOLIO-204 using gold FOL + Z3 entailment on exp-026 traces. Oracle=89.71% vs SC=75.49% (+14.22pp, p=2.0e-07).\\\", \\\"path\\\": \\\"projects/symb_invariant_consensus/artifacts/exp-031-oracle-folio-regen/report/exp031_oracle_summary.txt\\\", \\\"url\\\": null, \\\"project\\\": \\\"symb_invariant_consensus\\\", \\\"exp_id\\\": \\\"exp-031-oracle-folio-regen\\\", \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-18T15:50:14.631232+00:00\\\", \\\"tags\\\": [\\\"oracle\\\", \\\"folio\\\", \\\"z3\\\", \\\"gold-fol\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260518_5c50be\", \"name\": \"exp-031 Oracle SICA Summary\", \"type\": \"report\", \"description\": \"Oracle SICA results for FOLIO-204 using gold FOL + Z3 entailment on exp-026 traces. Oracle=89.71% vs SC=75.49% (+14.22pp, p=2.0e-07).\", \"path\": \"projects/symb_invariant_consensus/artifacts/exp-031-oracle-folio-regen/report/exp031_oracle_summary.txt\", \"url\": null, \"project\": \"symb_invariant_consensus\", \"exp_id\": \"exp-031-oracle-folio-regen\", \"skill\": \"\", \"created_at\": \"2026-05-18T15:50:14.631232+00:00\", \"tags\": [\"oracle\", \"folio\", \"z3\", \"gold-fol\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 184_

Experiment complete. Here's the report:

## exp-031-oracle-folio-regen Results

| Metric | exp-031 (new) | exp-021 (old) |
|---|---|---|
| **Oracle SICA accuracy** | **89.71%** (183/204) | 88.24% (180/204) |
| SC accuracy | 75.49% (154/204) | 79.41% (162/204) |
| SICA(self) accuracy | 74.51% (152/204) | 79.41% (162/204) |
| **Oracle vs SC delta** | **+14.22pp** | +8.82pp |
| McNemar p-value | **2.0e-07** | 6.15e-05 |
| McNemar b/c | b=29, c=0 | - |
| Z3 gold agreement | 95.10% (194/204) | 94.6% (193/204) |
| FOL parse success | 204/204 (100%) | 204/204 (100%) |

**Per answer type (oracle / SC):**
| Type | n | Oracle | SC | Z3 agree |
|---|---|---|---|---|
| True | 72 | 97.2% | 93.1% | 95.8% |
| False | 63 | 93.6% | 87.3% | 92.1% |
| Unknown | 69 | **78.3%** | 46.4% | 97.1% |

**Key findings:**
- Oracle accuracy improved from 88.24% to **89.71%** (+1.47pp) despite different traces
- Delta vs SC dramatically increased from +8.82pp to **+14.22pp** (SC baseline dropped from 79.41% to 75.49% with new traces)
- McNemar b=29, c=0: oracle corrected 29 SC errors while never losing
- Biggest gain on **Unknown** problems: +31.9pp (78.3% vs 46.4%)
- 21 oracle errors: 18 from Z3 correct but no supporting trace, 3 from Z3 wrong + SC also wrong
- Conclusion unchanged from exp-021: **constraint extraction quality is the bottleneck, not the aggregation mechanism**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "313c3feb-1493-4c66-ba8a-5c348c2e5f55",
  "uuid": "56f6d5c4-532a-4324-b792-fdc1b29a3cff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01523aeMwL5DiY2JBttp3Ymr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 786,
      "cache_read_input_tokens": 140438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 786
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


### Task result

_source line 185_

Experiment complete. Here's the report:

## exp-031-oracle-folio-regen Results

| Metric | exp-031 (new) | exp-021 (old) |
|---|---|---|
| **Oracle SICA accuracy** | **89.71%** (183/204) | 88.24% (180/204) |
| SC accuracy | 75.49% (154/204) | 79.41% (162/204) |
| SICA(self) accuracy | 74.51% (152/204) | 79.41% (162/204) |
| **Oracle vs SC delta** | **+14.22pp** | +8.82pp |
| McNemar p-value | **2.0e-07** | 6.15e-05 |
| McNemar b/c | b=29, c=0 | - |
| Z3 gold agreement | 95.10% (194/204) | 94.6% (193/204) |
| FOL parse success | 204/204 (100%) | 204/204 (100%) |

**Per answer type (oracle / SC):**
| Type | n | Oracle | SC | Z3 agree |
|---|---|---|---|---|
| True | 72 | 97.2% | 93.1% | 95.8% |
| False | 63 | 93.6% | 87.3% | 92.1% |
| Unknown | 69 | **78.3%** | 46.4% | 97.1% |

**Key findings:**
- Oracle accuracy improved from 88.24% to **89.71%** (+1.47pp) despite different traces
- Delta vs SC dramatically increased from +8.82pp to **+14.22pp** (SC baseline dropped from 79.41% to 75.49% with new traces)
- McNemar b=29, c=0: oracle corrected 29 SC errors while never losing
- Biggest gain on **Unknown** problems: +31.9pp (78.3% vs 46.4%)
- 21 oracle errors: 18 from Z3 correct but no supporting trace, 3 from Z3 wrong + SC also wrong
- Conclusion unchanged from exp-021: **constraint extraction quality is the bottleneck, not the aggregation mechanism**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 1189318,
  "duration_api_ms": 1117153,
  "num_turns": 65,
  "stop_reason": "end_turn",
  "session_id": "313c3feb-1493-4c66-ba8a-5c348c2e5f55",
  "total_cost_usd": 4.645221749999999,
  "usage": {
    "input_tokens": 41,
    "cache_creation_input_tokens": 129383,
    "cache_read_input_tokens": 3656479,
    "output_tokens": 67904,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 129383,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 564,
        "cache_read_input_tokens": 140438,
        "cache_creation_input_tokens": 786,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 786
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2022,
      "outputTokens": 25,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002147,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 50,
      "outputTokens": 72707,
      "cacheReadInputTokens": 3760437,
      "cacheCreationInputTokens": 151189,
      "webSearchRequests": 0,
      "costUSD": 4.6430747499999985,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b421269b-cba4-45c3-b99d-65f7d41877ab"
}
```

</details>

---
