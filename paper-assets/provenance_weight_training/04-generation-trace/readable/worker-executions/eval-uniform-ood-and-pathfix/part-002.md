# eval uniform ood and pathfix — Part 2 of 2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../eval-uniform-ood-and-pathfix.md) · [Structured JSON](../../../sessions/cf/cf390b63a9c2ad13efbb.json)

## Before a recorded user message

### Assistant

_source line 494_

All eval complete. Both directories now have all 3 required files matching `n5_statistical_analysis.py --auto` expectations.

## 结果汇总

### Uniform seed789

| Dataset | PPL |
|---------|-----|
| Holdout | 17.695 |
| OWT | 18.387 |
| Wiki | 15.349 |

### Uniform seed234

| Dataset | PPL |
|---------|-----|
| Holdout | 17.708 |
| OWT | 18.355 |
| Wiki | 15.352 |

### 与 3-seed 参考对比 (seed42)

| Dataset | seed42 | seed789 | seed234 |
|---------|--------|---------|---------|
| Holdout | 17.694 | 17.695 | 17.708 |
| OWT | 18.364 | 18.387 | 18.355 |
| Wiki | 15.337 | 15.349 | 15.352 |

### 目录结构

```
eval_results/
├── bs16_uniform_seed42/     (已有)
│   ├── eval_holdout.json
│   ├── eval_owt.json
│   └── eval_wiki.json
├── bs16_uniform_seed123/    (已有)
├── bs16_uniform_seed456/    (已有)
├── bs16_uniform_seed789/    ← 新建
│   ├── eval_holdout.json
│   ├── eval_owt.json
│   └── eval_wiki.json
└── bs16_uniform_seed234/    ← 新建
    ├── eval_holdout.json
    ├── eval_owt.json
    └── eval_wiki.json
```

与 `n5_statistical_analysis.py --auto` 完全兼容 — 目录名匹配 `bs16_uniform_seed(\d+)` 模式，文件名为 `eval_holdout.json`、`eval_owt.json`、`eval_wiki.json`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9ee1b75-467c-4277-92da-8778e2cd7236",
  "uuid": "beb2ec89-b073-4e37-9056-b76e084c43b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013KBP6XcdVGcVqai6hmP4AK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1496,
      "cache_read_input_tokens": 110819,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1496
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

_source line 495_

All eval complete. Both directories now have all 3 required files matching `n5_statistical_analysis.py --auto` expectations.

## 结果汇总

### Uniform seed789

| Dataset | PPL |
|---------|-----|
| Holdout | 17.695 |
| OWT | 18.387 |
| Wiki | 15.349 |

### Uniform seed234

| Dataset | PPL |
|---------|-----|
| Holdout | 17.708 |
| OWT | 18.355 |
| Wiki | 15.352 |

### 与 3-seed 参考对比 (seed42)

| Dataset | seed42 | seed789 | seed234 |
|---------|--------|---------|---------|
| Holdout | 17.694 | 17.695 | 17.708 |
| OWT | 18.364 | 18.387 | 18.355 |
| Wiki | 15.337 | 15.349 | 15.352 |

### 目录结构

```
eval_results/
├── bs16_uniform_seed42/     (已有)
│   ├── eval_holdout.json
│   ├── eval_owt.json
│   └── eval_wiki.json
├── bs16_uniform_seed123/    (已有)
├── bs16_uniform_seed456/    (已有)
├── bs16_uniform_seed789/    ← 新建
│   ├── eval_holdout.json
│   ├── eval_owt.json
│   └── eval_wiki.json
└── bs16_uniform_seed234/    ← 新建
    ├── eval_holdout.json
    ├── eval_owt.json
    └── eval_wiki.json
```

与 `n5_statistical_analysis.py --auto` 完全兼容 — 目录名匹配 `bs16_uniform_seed(\d+)` 模式，文件名为 `eval_holdout.json`、`eval_owt.json`、`eval_wiki.json`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 809384,
  "duration_api_ms": 702592,
  "num_turns": 215,
  "stop_reason": "end_turn",
  "session_id": "b9ee1b75-467c-4277-92da-8778e2cd7236",
  "total_cost_usd": 5.486875499999998,
  "usage": {
    "input_tokens": 113,
    "cache_creation_input_tokens": 100474,
    "cache_read_input_tokens": 8152016,
    "output_tokens": 31202,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 100474,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 532,
        "cache_read_input_tokens": 110819,
        "cache_creation_input_tokens": 1496,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1496
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2185,
      "outputTokens": 21,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00229,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 113,
      "outputTokens": 31202,
      "cacheReadInputTokens": 8152016,
      "cacheCreationInputTokens": 100474,
      "webSearchRequests": 0,
      "costUSD": 5.484585499999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "0ad3f8b9-6006-44c7-8969-3ebaf327f4a1"
}
```

</details>

---
