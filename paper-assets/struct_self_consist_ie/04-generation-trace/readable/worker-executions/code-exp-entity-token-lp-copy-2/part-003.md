# code exp entity token lp — Part 3 of 3

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

[← Part 2](part-002.md) · [Transcript overview](../code-exp-entity-token-lp-copy-2.md) · [Structured JSON](../../../sessions/99/99d19849513d05b4ae6a.json)

## Round 1

### Tool call

_source line 376_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01GsEry5pW4MS2Lm68zuWd8d`</summary>

```json
{
  "name": "exp_entity_token_lp_results",
  "type": "data",
  "description": "Entity-token LP vs full-sequence LP analysis results on SciERC and CoNLL2003. Contains F1 scores for greedy/full-LP/entity-LP/majority-vote/oracle selection, within-instance variance statistics, and entity token statistics.",
  "project": "struct_self_consist_ie",
  "exp_id": "exp_entity_token_lp",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp_entity_token_lp/results.json",
  "tags": [
    "entity-lp",
    "logprobs",
    "sample-selection",
    "scierc",
    "conll"
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
  "session_id": "c8d5c664-11c9-4649-8d2a-1a7b04736b78",
  "uuid": "e65c7072-a2e3-49d9-a672-687f6d955f6c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014cV1PY8r3JKULBh9aUywG3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 905,
      "cache_read_input_tokens": 104335,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 905
      },
      "output_tokens": 67,
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

_source line 377 · 2026-05-16T06:05:52.602Z_

<details><summary>↩ Tool result · `toolu_01GsEry5pW4MS2Lm68zuWd8d`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_6077d0\", \"name\": \"exp_entity_token_lp_results\", \"type\": \"data\", \"description\": \"Entity-token LP vs full-sequence LP analysis results on SciERC and CoNLL2003. Contains F1 scores for greedy/full-LP/entity-LP/majority-vote/oracle selection, within-instance variance statistics, and entity token statistics.\", \"path\": \"projects/struct_self_consist_ie/artifacts/exp_entity_token_lp/data/results.json\", \"url\": null, \"project\": \"struct_self_consist_ie\", \"exp_id\": \"exp_entity_token_lp\", \"skill\": \"\", \"created_at\": \"2026-05-16T06:05:52.321952+00:00\", \"tags\": [\"entity-lp\", \"logprobs\", \"sample-selection\", \"scierc\", \"conll\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d5c664-11c9-4649-8d2a-1a7b04736b78",
  "uuid": "1c5e43dc-7b1a-4992-8126-4b05f3d12644",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260516_6077d0\\\", \\\"name\\\": \\\"exp_entity_token_lp_results\\\", \\\"type\\\": \\\"data\\\", \\\"description\\\": \\\"Entity-token LP vs full-sequence LP analysis results on SciERC and CoNLL2003. Contains F1 scores for greedy/full-LP/entity-LP/majority-vote/oracle selection, within-instance variance statistics, and entity token statistics.\\\", \\\"path\\\": \\\"projects/struct_self_consist_ie/artifacts/exp_entity_token_lp/data/results.json\\\", \\\"url\\\": null, \\\"project\\\": \\\"struct_self_consist_ie\\\", \\\"exp_id\\\": \\\"exp_entity_token_lp\\\", \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-16T06:05:52.321952+00:00\\\", \\\"tags\\\": [\\\"entity-lp\\\", \\\"logprobs\\\", \\\"sample-selection\\\", \\\"scierc\\\", \\\"conll\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_6077d0\", \"name\": \"exp_entity_token_lp_results\", \"type\": \"data\", \"description\": \"Entity-token LP vs full-sequence LP analysis results on SciERC and CoNLL2003. Contains F1 scores for greedy/full-LP/entity-LP/majority-vote/oracle selection, within-instance variance statistics, and entity token statistics.\", \"path\": \"projects/struct_self_consist_ie/artifacts/exp_entity_token_lp/data/results.json\", \"url\": null, \"project\": \"struct_self_consist_ie\", \"exp_id\": \"exp_entity_token_lp\", \"skill\": \"\", \"created_at\": \"2026-05-16T06:05:52.321952+00:00\", \"tags\": [\"entity-lp\", \"logprobs\", \"sample-selection\", \"scierc\", \"conll\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 378_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01VfCNw8LzwNESY8ixSXoN21`</summary>

```json
{
  "name": "exp_entity_token_lp_report",
  "type": "report",
  "description": "Analysis report: entity-token LP does not improve sample selection F1. Entity-LP is worse than full-sequence LP on both SciERC (-2.03pp) and CoNLL (-3.30pp). CoNLL entity tokens are saturated (79% tied). SciERC entity-LP has 4x higher variance but the signal is too noisy (5.3% of tokens).",
  "project": "struct_self_consist_ie",
  "exp_id": "exp_entity_token_lp",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp_entity_token_lp/report.md",
  "tags": [
    "entity-lp",
    "logprobs",
    "sample-selection",
    "negative-result"
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
  "session_id": "c8d5c664-11c9-4649-8d2a-1a7b04736b78",
  "uuid": "37943a99-4c2b-45e5-afd9-54ad06f169be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014cV1PY8r3JKULBh9aUywG3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 905,
      "cache_read_input_tokens": 104335,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 905
      },
      "output_tokens": 67,
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

_source line 379 · 2026-05-16T06:05:55.620Z_

<details><summary>↩ Tool result · `toolu_01VfCNw8LzwNESY8ixSXoN21`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_d4f4aa\", \"name\": \"exp_entity_token_lp_report\", \"type\": \"report\", \"description\": \"Analysis report: entity-token LP does not improve sample selection F1. Entity-LP is worse than full-sequence LP on both SciERC (-2.03pp) and CoNLL (-3.30pp). CoNLL entity tokens are saturated (79% tied). SciERC entity-LP has 4x higher variance but the signal is too noisy (5.3% of tokens).\", \"path\": \"projects/struct_self_consist_ie/artifacts/exp_entity_token_lp/report/report.md\", \"url\": null, \"project\": \"struct_self_consist_ie\", \"exp_id\": \"exp_entity_token_lp\", \"skill\": \"\", \"created_at\": \"2026-05-16T06:05:55.332842+00:00\", \"tags\": [\"entity-lp\", \"logprobs\", \"sample-selection\", \"negative-result\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d5c664-11c9-4649-8d2a-1a7b04736b78",
  "uuid": "73691416-2aaa-4013-9b5c-d26dee5d14dd",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260516_d4f4aa\\\", \\\"name\\\": \\\"exp_entity_token_lp_report\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Analysis report: entity-token LP does not improve sample selection F1. Entity-LP is worse than full-sequence LP on both SciERC (-2.03pp) and CoNLL (-3.30pp). CoNLL entity tokens are saturated (79% tied). SciERC entity-LP has 4x higher variance but the signal is too noisy (5.3% of tokens).\\\", \\\"path\\\": \\\"projects/struct_self_consist_ie/artifacts/exp_entity_token_lp/report/report.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"struct_self_consist_ie\\\", \\\"exp_id\\\": \\\"exp_entity_token_lp\\\", \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-16T06:05:55.332842+00:00\\\", \\\"tags\\\": [\\\"entity-lp\\\", \\\"logprobs\\\", \\\"sample-selection\\\", \\\"negative-result\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_d4f4aa\", \"name\": \"exp_entity_token_lp_report\", \"type\": \"report\", \"description\": \"Analysis report: entity-token LP does not improve sample selection F1. Entity-LP is worse than full-sequence LP on both SciERC (-2.03pp) and CoNLL (-3.30pp). CoNLL entity tokens are saturated (79% tied). SciERC entity-LP has 4x higher variance but the signal is too noisy (5.3% of tokens).\", \"path\": \"projects/struct_self_consist_ie/artifacts/exp_entity_token_lp/report/report.md\", \"url\": null, \"project\": \"struct_self_consist_ie\", \"exp_id\": \"exp_entity_token_lp\", \"skill\": \"\", \"created_at\": \"2026-05-16T06:05:55.332842+00:00\", \"tags\": [\"entity-lp\", \"logprobs\", \"sample-selection\", \"negative-result\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 380_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_017D464maST3ExxbQEBAEWUk`</summary>

```json
{
  "todos": [
    {
      "content": "Verify SciERC inference output",
      "status": "completed",
      "activeForm": "Verifying SciERC inference output"
    },
    {
      "content": "Wait for CoNLL inference to complete",
      "status": "completed",
      "activeForm": "Waiting for CoNLL inference to complete"
    },
    {
      "content": "Run entity_token_analysis.py on both datasets",
      "status": "completed",
      "activeForm": "Running entity token analysis"
    },
    {
      "content": "Save results.json and report.md to local artifacts",
      "status": "completed",
      "activeForm": "Saving artifacts locally"
    },
    {
      "content": "Register artifacts",
      "status": "completed",
      "activeForm": "Registering artifacts"
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
  "session_id": "c8d5c664-11c9-4649-8d2a-1a7b04736b78",
  "uuid": "df7deebc-b9a7-48c5-a1b8-b8c06a9ebd35",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012tJEyjBiXssp9rqoFc44Bj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1389,
      "cache_read_input_tokens": 105240,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1389
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

_source line 381 · 2026-05-16T06:05:59.443Z_

<details><summary>↩ Tool result · `toolu_017D464maST3ExxbQEBAEWUk`</summary>

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
  "session_id": "c8d5c664-11c9-4649-8d2a-1a7b04736b78",
  "uuid": "ee403def-604b-4e70-9575-827bb333508c",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Verify SciERC inference output",
        "status": "completed",
        "activeForm": "Verifying SciERC inference output"
      },
      {
        "content": "Wait for CoNLL inference to complete",
        "status": "completed",
        "activeForm": "Waiting for CoNLL inference to complete"
      },
      {
        "content": "Run entity_token_analysis.py on both datasets",
        "status": "in_progress",
        "activeForm": "Running entity token analysis"
      },
      {
        "content": "Save results.json and report.md to local artifacts",
        "status": "pending",
        "activeForm": "Saving artifacts locally"
      },
      {
        "content": "Register artifacts",
        "status": "pending",
        "activeForm": "Registering artifacts"
      }
    ],
    "newTodos": [
      {
        "content": "Verify SciERC inference output",
        "status": "completed",
        "activeForm": "Verifying SciERC inference output"
      },
      {
        "content": "Wait for CoNLL inference to complete",
        "status": "completed",
        "activeForm": "Waiting for CoNLL inference to complete"
      },
      {
        "content": "Run entity_token_analysis.py on both datasets",
        "status": "completed",
        "activeForm": "Running entity token analysis"
      },
      {
        "content": "Save results.json and report.md to local artifacts",
        "status": "completed",
        "activeForm": "Saving artifacts locally"
      },
      {
        "content": "Register artifacts",
        "status": "completed",
        "activeForm": "Registering artifacts"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---


### Assistant

_source line 382_

All steps complete. Summary of the **exp_entity_token_lp** experiment:

**Entity-token LP does not improve sample selection F1.** It is strictly worse than full-sequence LP on both datasets:

| | SciERC | CoNLL |
|---|---|---|
| Greedy F1 | 0.6430 | 0.9065 |
| Full-LP Selection | 0.6465 (+0.35pp) | 0.8989 (-0.76pp) |
| Entity-LP Selection | 0.6262 (-1.68pp) | 0.8659 (-4.06pp) |
| Entity-LP vs Full-LP | **-2.03pp** | **-3.30pp** |

**Why it fails:**
- **CoNLL**: Entity tokens are saturated (logprobs ~0.0), yielding zero discriminative variance (79.4% of instances tied). The model generates entity tokens with near-certainty.
- **SciERC**: Entity-LP has 4x higher within-instance variance than full-LP, but the signal is too noisy — entity tokens are only 5.3% of total tokens, making the mean logprob unstable.

Artifacts registered: `art_20260516_6077d0` (results.json), `art_20260516_d4f4aa` (report.md).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d5c664-11c9-4649-8d2a-1a7b04736b78",
  "uuid": "f8618e9a-c48c-4119-9ef7-38aa66319af2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016eYV9Hk37iUqXLvhcMZZdQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 254,
      "cache_read_input_tokens": 106629,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 254
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

_source line 383_

All steps complete. Summary of the **exp_entity_token_lp** experiment:

**Entity-token LP does not improve sample selection F1.** It is strictly worse than full-sequence LP on both datasets:

| | SciERC | CoNLL |
|---|---|---|
| Greedy F1 | 0.6430 | 0.9065 |
| Full-LP Selection | 0.6465 (+0.35pp) | 0.8989 (-0.76pp) |
| Entity-LP Selection | 0.6262 (-1.68pp) | 0.8659 (-4.06pp) |
| Entity-LP vs Full-LP | **-2.03pp** | **-3.30pp** |

**Why it fails:**
- **CoNLL**: Entity tokens are saturated (logprobs ~0.0), yielding zero discriminative variance (79.4% of instances tied). The model generates entity tokens with near-certainty.
- **SciERC**: Entity-LP has 4x higher within-instance variance than full-LP, but the signal is too noisy — entity tokens are only 5.3% of total tokens, making the mean logprob unstable.

Artifacts registered: `art_20260516_6077d0` (results.json), `art_20260516_d4f4aa` (report.md).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 949368,
  "duration_api_ms": 845235,
  "num_turns": 135,
  "stop_reason": "end_turn",
  "session_id": "c8d5c664-11c9-4649-8d2a-1a7b04736b78",
  "total_cost_usd": 7.0566645,
  "usage": {
    "input_tokens": 133,
    "cache_creation_input_tokens": 247316,
    "cache_read_input_tokens": 8743818,
    "output_tokens": 35266,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 247316,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 330,
        "cache_read_input_tokens": 106629,
        "cache_creation_input_tokens": 254,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 254
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 6113,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.006203,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10352,
      "outputTokens": 39872,
      "cacheReadInputTokens": 8907653,
      "cacheCreationInputTokens": 247692,
      "webSearchRequests": 0,
      "costUSD": 7.0504615,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "40ac3bf3-dcfa-462e-afa1-76d396e60908"
}
```

</details>

---
