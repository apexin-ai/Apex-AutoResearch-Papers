# train exp1 roberta mlm — Part 2 of 2

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../train-exp1-roberta-mlm.md) · [Structured JSON](../../../sessions/42/42db20f76ebae1b2734b.json)

## Before a recorded user message

### Task result

_source line 281_

All done. Results summary:

**RoBERTa MLM-only (continued pretraining + BiGRU):**

| Metric | Mean | Std |
|---|---|---|
| DD OOD K=1 | 0.9428 | 0.0184 |
| DD OOD K=2 | 0.9747 | 0.0232 |
| DD OOD K=3 | 0.9747 | 0.0232 |
| DD OOD K=5 | 0.9841 | 0.0160 |
| DD OOD Full | 0.9874 | 0.0178 |

**RoBERTa Vanilla (no pretraining + BiGRU):**

| Metric | Mean | Std |
|---|---|---|
| DD OOD K=1 | 0.9127 | 0.1028 |
| DD OOD K=2 | 0.9003 | 0.1342 |
| DD OOD K=3 | 0.8976 | 0.1381 |
| DD OOD K=5 | 0.9442 | 0.0789 |
| DD OOD Full | 0.9813 | 0.0264 |

MLM pretraining shows slightly higher mean F1 and substantially lower variance across seeds compared to vanilla. The vanilla baseline has high variance driven by seed=42 underperforming (K=1 F1=0.77 vs 0.98-0.99 for other seeds).

Artifacts saved to:
- `artifacts/exp1_roberta_mlm_results.json`
- `artifacts/exp1_roberta_vanilla_results.json`

Server-side results at:
- `results/exp1_roberta_mlm.json`
- `results/exp1_roberta_vanilla.json`

Script: `src/exp1_roberta_mlm_pipeline.py`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 1085455,
  "duration_api_ms": 991200,
  "num_turns": 117,
  "stop_reason": "end_turn",
  "session_id": "dd524b4b-0666-4735-956d-8549da0c3577",
  "total_cost_usd": 7.1850342499999975,
  "usage": {
    "input_tokens": 96,
    "cache_creation_input_tokens": 135251,
    "cache_read_input_tokens": 9941747,
    "output_tokens": 54647,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 135251,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 490,
        "cache_read_input_tokens": 146803,
        "cache_creation_input_tokens": 289,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 289
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2037,
      "outputTokens": 30,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002187,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 96,
      "outputTokens": 54647,
      "cacheReadInputTokens": 9941747,
      "cacheCreationInputTokens": 135251,
      "webSearchRequests": 0,
      "costUSD": 7.182847249999997,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "f9ec1d64-ae51-4f30-b7f8-c1973900bb07"
}
```

</details>

---
