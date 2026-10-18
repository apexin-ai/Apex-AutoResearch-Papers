# analysis plan006 cross benchmark v2 reverse — Part 2 of 2

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../analysis-plan006-cross-benchmark-v2-reverse.md) · [Structured JSON](../../../sessions/fe/fea3cfd565dcbe3b64e5.json)

## Before a recorded user message

### Task result

_source line 361_

结果已保存到 `cross_benchmark_v2_bidirectional.json`。

## 完整结果

### β(K_eff) Sign Consistency: 17/18（对称，两个方向相同）

| K | 一致/总数 | 不一致条件 |
|---|----------|-----------|
| K=3 | 5/6 | **K3×position_bias** (MMLU β=+0.084, ARC β=−0.050) |
| K=5 | 6/6 | — |
| K=7 | 6/6 | — |

### Cross-Predict R² 双向对比

| Condition | MMLU→ARC R² | ARC→MMLU R² |
|-----------|-------------|-------------|
| K3×prompt_injection | 0.238 | **0.362** |
| K3×sycophancy | 0.130 | **0.156** |
| K3×score_manipulation | 0.178 | **0.360** |
| K3×verbosity_bias | 0.242 | **0.324** |
| K3×position_bias | −0.842 | 0.091 |
| K3×authority_bias | 0.096 | 0.070 |
| K5×prompt_injection | 0.220 | **0.299** |
| K5×sycophancy | −0.145 | −0.648 |
| K5×score_manipulation | **0.249** | 0.194 |
| K5×verbosity_bias | 0.120 | **0.293** |
| K5×position_bias | −2.528 | 0.086 |
| K5×authority_bias | −0.185 | −0.441 |
| K7×prompt_injection | 0.147 | **0.188** |
| K7×sycophancy | −0.469 | −1.772 |
| K7×score_manipulation | **0.188** | 0.148 |
| K7×verbosity_bias | −0.206 | **0.186** |
| K7×position_bias | −3.490 | 0.097 |
| K7×authority_bias | −0.489 | −1.014 |

### 关键发现

1. **Sign consistency 是对称的**：`sign(β_keff_MMLU) == sign(β_keff_ARC)` 不分方向，17/18 适用于两个方向。V1 的 14/18 和 10/18 差异应来自不同的定义或数据版本。

2. **Cross-predict R² 不对称**：ARC→MMLU方向在多数条件下R²更高（尤其K3），说明用ARC系数预测MMLU比反过来更准。这可能因为ARC拟合的系数更保守，泛化性更好。

3. **唯一不一致条件**：K3×position_bias（MMLU β_keff=+0.084 接近0，ARC β_keff=−0.050 不显著 p=0.43）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 902480,
  "duration_api_ms": 820917,
  "num_turns": 151,
  "stop_reason": "end_turn",
  "session_id": "a8221767-4e2b-4df2-94e7-4e7e7736960a",
  "total_cost_usd": 7.6688490000000025,
  "usage": {
    "input_tokens": 149,
    "cache_creation_input_tokens": 112038,
    "cache_read_input_tokens": 12432823,
    "output_tokens": 29996,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 112038,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 824,
        "cache_read_input_tokens": 123511,
        "cache_creation_input_tokens": 368,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 368
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1445,
      "outputTokens": 22,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0015550000000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 149,
      "outputTokens": 29996,
      "cacheReadInputTokens": 12432823,
      "cacheCreationInputTokens": 112038,
      "webSearchRequests": 0,
      "costUSD": 7.667294000000003,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "c55174e0-4865-4ca9-88af-23432da65e1f"
}
```

</details>

---
