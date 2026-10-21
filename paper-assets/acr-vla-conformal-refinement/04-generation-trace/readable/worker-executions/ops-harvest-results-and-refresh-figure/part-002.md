# ops harvest results and refresh figure — Part 2 of 2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../ops-harvest-results-and-refresh-figure.md) · [Structured JSON](../../../sessions/4d/4de11c0ba48ad9bb84db.json)

## Round 1

### Task result

_source line 142_

Done. Here's the summary:

## New Data Points Added (5)

| Method | Norm | Seed | SR | Source |
|--------|------|------|----|--------|
| perdof | 0.2 | 46 | 0.09 | bjb2-28827 |
| perdof | 0.2 | 47 | 0.11 | bjb2-28827 |
| obs_only | default | 46 | 0.15 | bjb1-32546 |
| obs_only | 0.05 | 43 | 0.14 | bjb1-32546 |
| perdof | default | 46 | 0.00 | bjb1-32546 |

Also noted: obs_only norm=0.2 K=5 seed42 = 0.14 on bjb1-18228 (excluded, different K).

## Updated Magnitude Curve Summary

| Method | Norm | Mean SR | Std | n |
|--------|------|---------|-----|---|
| **obs_only** | 0.03 | 16.0% | - | 1 |
| | 0.05 | **13.5%** | 0.71 | **2** |
| | 0.1 | 15.0% | 1.41 | 2 |
| | 0.2 | 17.5% | 2.81 | 6 |
| | 0.3 | 17.0% | 2.16 | 4 |
| | uncapped | **14.8%** | **2.95** | **5** |
| **perdof** | 0.03 | 14.0% | - | 1 |
| | 0.05 | 14.0% | - | 1 |
| | 0.1 | 10.75% | 2.50 | 4 |
| | 0.2 | **9.83%** | **0.98** | **6** |
| | 0.3 | 4.67% | 1.15 | 3 |
| | uncapped | **7.75%** | **5.44** | **4** |

Bold = changed values.

## Registry Fixes (8)

- `eval-openvla-object-vla-only-seed42`: failed → **negative** (completed, SR=0)
- `eval-acr-object-v3`: failed → **negative** (partial, all SR=0)
- `eval-acr-spatial-v3`: failed → **success** (SR=2.5%)
- 5 experiments: failed → **killed** (SIGTERM from errant kill-restart Worker)

## Figure Changes
- Removed stale "0%" annotation (perdof default now 7.75%, not 0%)
- Fixed argmin legend from hardcoded n=3 to n=1
- Added n=X labels for high-seed-count points

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 460277,
  "duration_api_ms": 452238,
  "num_turns": 45,
  "stop_reason": "end_turn",
  "session_id": "4d8394c6-e634-4645-9660-0c46d3fc3e37",
  "total_cost_usd": 1.9763005000000002,
  "usage": {
    "input_tokens": 24,
    "cache_creation_input_tokens": 67789,
    "cache_read_input_tokens": 1104308,
    "output_tokens": 24126,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 67789,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 732,
        "cache_read_input_tokens": 78333,
        "cache_creation_input_tokens": 1297,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1297
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1295,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00138,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 34,
      "outputTokens": 29704,
      "cacheReadInputTokens": 1246176,
      "cacheCreationInputTokens": 97450,
      "webSearchRequests": 0,
      "costUSD": 1.9749205,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "a20b3538-532d-459f-89d3-02fbc0c292e5"
}
```

</details>

---
