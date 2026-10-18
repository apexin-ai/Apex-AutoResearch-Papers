# deploy cqa1 pi05 experiments — Part 2 of 2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../deploy-cqa1-pi05-experiments.md) · [Structured JSON](../../../sessions/8e/8e668a38c128b446e26d.json)

## Before a recorded user message

### Assistant

_source line 420_

两个实验均已成功运行并进入 eval 循环：

| 实验 | GPU | 显存 | Pruning | 状态 |
|------|-----|------|---------|------|
| **A**: `eval_pi05_l2norm_k085_object_seed42` | GPU2 | 10262/24564 MiB | l2norm keep=217/256 | RUNNING |
| **B**: `eval_pi05_random_k03_object_seed43` | GPU3 | 10134/24564 MiB | random keep=76/256 | RUNNING |

部署总结：
- 磁盘 71%（无需清理）
- π0.5 权重从 HuggingFace 下载完成（7.47GB）
- eval 脚本通过 heredoc 传输到 cqa1
- 修复了 `google/paligemma-3b-pt-224` tokenizer 缓存缺失问题
- 两个实验在 tmux session 中运行，日志写入 `logs/` 目录
- 显存 ~10GB/24GB，无 OOM 风险
- Registry 已更新为 RUNNING

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c92ebac-820f-415f-96fa-e8fc44ca3023",
  "uuid": "fac1d551-612f-430a-bacf-ae18edc29b90",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0134K8T5WSYnKz7ZBXzd9sW9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 921,
      "cache_read_input_tokens": 152209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 921
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

_source line 421_

两个实验均已成功运行并进入 eval 循环：

| 实验 | GPU | 显存 | Pruning | 状态 |
|------|-----|------|---------|------|
| **A**: `eval_pi05_l2norm_k085_object_seed42` | GPU2 | 10262/24564 MiB | l2norm keep=217/256 | RUNNING |
| **B**: `eval_pi05_random_k03_object_seed43` | GPU3 | 10134/24564 MiB | random keep=76/256 | RUNNING |

部署总结：
- 磁盘 71%（无需清理）
- π0.5 权重从 HuggingFace 下载完成（7.47GB）
- eval 脚本通过 heredoc 传输到 cqa1
- 修复了 `google/paligemma-3b-pt-224` tokenizer 缓存缺失问题
- 两个实验在 tmux session 中运行，日志写入 `logs/` 目录
- 显存 ~10GB/24GB，无 OOM 风险
- Registry 已更新为 RUNNING

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 1919161,
  "duration_api_ms": 1822790,
  "num_turns": 161,
  "stop_reason": "end_turn",
  "session_id": "9c92ebac-820f-415f-96fa-e8fc44ca3023",
  "total_cost_usd": 7.94261825,
  "usage": {
    "input_tokens": 120,
    "cache_creation_input_tokens": 141289,
    "cache_read_input_tokens": 11422176,
    "output_tokens": 53815,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 141289,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 320,
        "cache_read_input_tokens": 152209,
        "cache_creation_input_tokens": 921,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 921
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2364,
      "outputTokens": 27,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0024990000000000004,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 120,
      "outputTokens": 53815,
      "cacheReadInputTokens": 11422176,
      "cacheCreationInputTokens": 141289,
      "webSearchRequests": 0,
      "costUSD": 7.9401192499999995,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "32028800-d049-46ca-972a-c959797de97f"
}
```

</details>

---
