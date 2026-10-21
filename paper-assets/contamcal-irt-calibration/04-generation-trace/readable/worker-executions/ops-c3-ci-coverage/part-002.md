# ops c3 ci coverage — Part 2 of 2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../ops-c3-ci-coverage.md) · [Structured JSON](../../../sessions/f0/f05812752e0c97d3f9a7.json)

## Before a recorded user message

### Tool call

_source line 243_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_019BzsrPmkTfQyLNPrD4tV8T`</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -la /root/autodl-tmp/exp006/ci_coverage_analysis/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "194c08b9-6b0d-438c-bdc6-f8aab2431793",
  "uuid": "653f9489-1c52-4b89-8c75-d46d9102cab3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012XaQZjEp6nPz8JaTeevmLB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1796,
      "cache_read_input_tokens": 128291,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1796
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

_source line 244 · 2026-05-17T15:04:51.524Z_

<details><summary>↩ Tool result · `toolu_019BzsrPmkTfQyLNPrD4tV8T`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 80\\ndrwxr-xr-x  4 root root   140 May 17 23:04 .\\ndrwxr-xr-x 50 root root  4096 May 17 23:00 ..\\n-rw-r--r--  1 root root 40350 May 17 23:01 all_coverage_results.json\\ndrwxr-xr-x  2 root root    38 May 17 23:01 arc_challenge\\n-rw-r--r--  1 root root  1610 May 17 23:04 coverage_summary.json\\ndrwxr-xr-x  2 root root    38 May 17 22:59 mmlu\\n-rw-r--r--  1 root root 30922 May 17 23:01 run.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "194c08b9-6b0d-438c-bdc6-f8aab2431793",
  "uuid": "04e2ffe2-90f8-4ae7-bfda-404e029217db",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"total 80\\\\ndrwxr-xr-x  4 root root   140 May 17 23:04 .\\\\ndrwxr-xr-x 50 root root  4096 May 17 23:00 ..\\\\n-rw-r--r--  1 root root 40350 May 17 23:01 all_coverage_results.json\\\\ndrwxr-xr-x  2 root root    38 May 17 23:01 arc_challenge\\\\n-rw-r--r--  1 root root  1610 May 17 23:04 coverage_summary.json\\\\ndrwxr-xr-x  2 root root    38 May 17 22:59 mmlu\\\\n-rw-r--r--  1 root root 30922 May 17 23:01 run.log\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.38}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"total 80\\ndrwxr-xr-x  4 root root   140 May 17 23:04 .\\ndrwxr-xr-x 50 root root  4096 May 17 23:00 ..\\n-rw-r--r--  1 root root 40350 May 17 23:01 all_coverage_results.json\\ndrwxr-xr-x  2 root root    38 May 17 23:01 arc_challenge\\n-rw-r--r--  1 root root  1610 May 17 23:04 coverage_summary.json\\ndrwxr-xr-x  2 root root    38 May 17 22:59 mmlu\\n-rw-r--r--  1 root root 30922 May 17 23:01 run.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 245_

Results are complete. Here's the summary:

## CI Coverage Results

| Benchmark | Level | Coverage | Nominal | Diff | z-score |
|-----------|-------|----------|---------|------|---------|
| **MMLU** | 50% | **0.833** | 0.50 | +0.33 | +2.83 |
| MMLU | 80% | 0.889 | 0.80 | +0.09 | +0.94 |
| MMLU | 95% | 1.000 | 0.95 | +0.05 | +0.97 |
| **ARC** | 50% | 0.450 | 0.50 | -0.05 | -0.45 |
| ARC | 80% | 0.650 | 0.80 | -0.15 | -1.68 |
| ARC | 95% | 0.900 | 0.95 | -0.05 | -1.03 |

**Key findings:**

1. **MMLU (N=18, 300 items)**: Posterior CIs are **over-conservative** (especially 50% CI covers 83% of models). The 2PL+gamma model's parameter uncertainty provides generous coverage at model level. This means calibrated score uncertainties are trustworthy (if anything, too wide).

2. **ARC (N=20, 300 items)**: CIs are **slightly under-covering** at 80% level (65% vs 80%, z=-1.68). This suggests mild model misfit for some ARC models, though with N=20 the SE~0.09 makes this borderline significant.

3. **Item-bin coverage = 0% everywhere**: This is expected. The posterior CI on predicted means is extremely narrow (parameter uncertainty only). The actual obs-pred discrepancy at the item level reflects IRT model limitations (the 2PL sigmoid attenuates extreme responses), not CI failure.

4. Model-level residual MAE: MMLU=0.009, ARC=0.015.

**Output saved to**: `/root/autodl-tmp/exp006/ci_coverage_analysis/`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "194c08b9-6b0d-438c-bdc6-f8aab2431793",
  "uuid": "9d7450f4-f048-4172-9717-fdeb5f2f7dbb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GiKKYGpsRNBaBu8u4v8487",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 395,
      "cache_read_input_tokens": 130087,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 395
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

_source line 246_

Results are complete. Here's the summary:

## CI Coverage Results

| Benchmark | Level | Coverage | Nominal | Diff | z-score |
|-----------|-------|----------|---------|------|---------|
| **MMLU** | 50% | **0.833** | 0.50 | +0.33 | +2.83 |
| MMLU | 80% | 0.889 | 0.80 | +0.09 | +0.94 |
| MMLU | 95% | 1.000 | 0.95 | +0.05 | +0.97 |
| **ARC** | 50% | 0.450 | 0.50 | -0.05 | -0.45 |
| ARC | 80% | 0.650 | 0.80 | -0.15 | -1.68 |
| ARC | 95% | 0.900 | 0.95 | -0.05 | -1.03 |

**Key findings:**

1. **MMLU (N=18, 300 items)**: Posterior CIs are **over-conservative** (especially 50% CI covers 83% of models). The 2PL+gamma model's parameter uncertainty provides generous coverage at model level. This means calibrated score uncertainties are trustworthy (if anything, too wide).

2. **ARC (N=20, 300 items)**: CIs are **slightly under-covering** at 80% level (65% vs 80%, z=-1.68). This suggests mild model misfit for some ARC models, though with N=20 the SE~0.09 makes this borderline significant.

3. **Item-bin coverage = 0% everywhere**: This is expected. The posterior CI on predicted means is extremely narrow (parameter uncertainty only). The actual obs-pred discrepancy at the item level reflects IRT model limitations (the 2PL sigmoid attenuates extreme responses), not CI failure.

4. Model-level residual MAE: MMLU=0.009, ARC=0.015.

**Output saved to**: `/root/autodl-tmp/exp006/ci_coverage_analysis/`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 786242,
  "duration_api_ms": 696445,
  "num_turns": 99,
  "stop_reason": "end_turn",
  "session_id": "194c08b9-6b0d-438c-bdc6-f8aab2431793",
  "total_cost_usd": 4.639462250000001,
  "usage": {
    "input_tokens": 82,
    "cache_creation_input_tokens": 118641,
    "cache_read_input_tokens": 6416772,
    "output_tokens": 27450,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 118641,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 528,
        "cache_read_input_tokens": 130087,
        "cache_creation_input_tokens": 395,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 395
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2825,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00291,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 82,
      "outputTokens": 27450,
      "cacheReadInputTokens": 6416772,
      "cacheCreationInputTokens": 118641,
      "webSearchRequests": 0,
      "costUSD": 4.636552250000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "2c12bae0-e213-4bd6-b700-26147cb74ac2"
}
```

</details>

---
