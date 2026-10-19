# validate dry run phase0 — Part 4 of 4

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Worker execution logs

[← Part 3](part-003.md) · [Transcript overview](../validate-dry-run-phase0.md) · [Structured JSON](../../../sessions/bd/bded38b5375d11fff423.json)

## Round 2

### Task result

_source line 884_

**Phase 0 Dry-run 全部三个阶段通过。** 结果摘要：

### Phase 1: Model Loading ✅
- PI0Pytorch 加载到 cuda:0，耗时 ~46s

### Phase 2: Hook Registration ✅  
- 12 hooks 注册成功（8 PaliGemma + 4 Expert）

### Phase 3: Episode Rollout ✅
- 任务: `pick up the black bowl ... view_11_15_100_0_0_initstate_0`（camera_viewpoints 扰动）
- 220 步完成（达到 max_steps，success=False — 正常，dry-run 验证管线不要求任务成功）
- **12 层 activation shapes 全部正确：**

| Layer | mean | first | last | first_last |
|-------|------|-------|------|------------|
| paligemma_layer_{2,4,6,8,10,12,14,16} | [1, 2048] | [1, 2048] | [1, 2048] | [1, 4096] |
| expert_layer_{2,6,10,14} | [1, 1024] | [1, 1024] | [1, 1024] | [1, 2048] |

维度与 `configs.py` 的 `PALIGEMMA_HIDDEN_DIM=2048` 和 `EXPERT_HIDDEN_DIM=1024` 完全匹配。管线已就绪，可以开始正式数据收集。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 3127404,
  "duration_api_ms": 2016234,
  "num_turns": 332,
  "stop_reason": "end_turn",
  "session_id": "85b6a3e9-2c96-40d0-b14b-c8ddd38892eb",
  "total_cost_usd": 19.886151750000003,
  "usage": {
    "input_tokens": 306,
    "cache_creation_input_tokens": 354616,
    "cache_read_input_tokens": 30530758,
    "output_tokens": 79517,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 354616,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 411,
        "cache_read_input_tokens": 53516,
        "cache_creation_input_tokens": 2909,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2909
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2537,
      "outputTokens": 22,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002647,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 2995,
      "outputTokens": 88731,
      "cacheReadInputTokens": 30864472,
      "cacheCreationInputTokens": 354883,
      "webSearchRequests": 0,
      "costUSD": 19.883504750000007,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "a0396bf5-f1bc-486a-8b2f-1eb7f4b53ee2"
}
```

</details>

---
