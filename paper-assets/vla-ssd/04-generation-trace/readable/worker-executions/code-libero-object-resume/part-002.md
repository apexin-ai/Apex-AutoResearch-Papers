# code libero object resume — Part 2 of 2

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../code-libero-object-resume.md) · [Structured JSON](../../../sessions/ba/baeb0e9d9ffc3be75ef2.json)

## Before a recorded user message

### Task result

_source line 301_

实验正式启动，配置正确：10 tasks × 10 demos × 50 timesteps × 15 seeds。

总结：
- **Checkpoint**: openvla-7b-finetuned-libero-object 已下载完成（16GB）
- **Data**: 10 个 LIBERO-Object hdf5 文件齐全
- **Script**: `libero_object_full_pipeline.py` 已修复 4 个问题：
  1. `global N_IMG_TOKENS` 声明位置（SyntaxError）
  2. `PrismaticProcessor` 加载（AutoProcessor 兼容性）
  3. pixel_values dtype 转 bfloat16
  4. 小样本 probing/classification 边界检查
- **新增 RSA 模块**: Phase 5，within-task Spearman(cosine_rep, euclidean_act)
- **Dry-run**: 6 个 phase 全部通过
- **正式实验**: `libero_object_full_pipeline` 已提交到 cuda:0，tmux session 运行中
- **输出**: `/root/autodl-tmp/vla-ssd/results/libero_object/` → 5 个 JSON + pipeline.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 1110600,
  "duration_api_ms": 815275,
  "num_turns": 111,
  "stop_reason": "end_turn",
  "session_id": "547a4424-f53f-4c91-a091-81b7fe9c3764",
  "total_cost_usd": 6.313803999999998,
  "usage": {
    "input_tokens": 97,
    "cache_creation_input_tokens": 125488,
    "cache_read_input_tokens": 9000670,
    "output_tokens": 41049,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 125488,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 332,
        "cache_read_input_tokens": 136839,
        "cache_creation_input_tokens": 490,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 490
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2379,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0024590000000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 97,
      "outputTokens": 41049,
      "cacheReadInputTokens": 9000670,
      "cacheCreationInputTokens": 125488,
      "webSearchRequests": 0,
      "costUSD": 6.311344999999998,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "8cecbba6-4aac-4332-ac1f-4018c837aad0"
}
```

</details>

---
