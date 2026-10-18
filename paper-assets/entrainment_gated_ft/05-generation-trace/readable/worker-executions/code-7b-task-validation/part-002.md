# code 7b task validation — Part 2 of 2

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../code-7b-task-validation.md) · [Structured JSON](../../../sessions/f2/f2bdcaf6b991169faf1f.json)

## Before a recorded user message

### Assistant

_source line 512_

---

## 诊断结果汇报

### Qwen2.5-7B-Instruct Function Composition 评估

#### 结果汇总

| Depth | Direct | CoT | Random |
|-------|--------|-----|--------|
| 1 | **0.890** | **0.966** | 0.100 |
| 2 | 0.194 | **0.894** | 0.100 |
| 3 | 0.140 | **0.712** | 0.100 |
| 4 | 0.110 | **0.534** | 0.100 |
| 5 | 0.144 | **0.380** | 0.100 |

#### 关键判断

1. **Task 设计有效**：Depth-1 direct accuracy = 89%，远超 random (10%)。强模型可以理解 task format 并正确执行单步函数查表，≤1.3B 模型的失败是能力不足，不是 task 设计问题。

2. **Direct composition 对 7B 也极难**：Depth ≥ 2 时 direct accuracy 骤降到 ~10-19%，接近 random。这说明即使 7B 级别的 transformer 在 single forward pass 中也无法完成多步函数组合，验证了论文的核心理论假说。

3. **CoT 显著提升**：CoT 在所有 depth 上大幅优于 direct：
   - D=2: 89.4% vs 19.4% (+70pp)
   - D=3: 71.2% vs 14.0% (+57pp)
   - D=5: 38.0% vs 14.4% (+24pp)
   
   这证明 composition 需要 chain-of-thought（sequential reasoning），与理论预测一致。

4. **CoT 也有衰减**：随 depth 增加 CoT accuracy 逐渐下降（97% → 38%），说明即使有 CoT，每一步组合仍有约 5-10% 的错误率在累积。

#### 文件路径
- Direct 结果: `/root/entrainment_gated_ft/results_7b/func_comp/summary_direct.json`
- CoT 结果: `/root/entrainment_gated_ft/results_7b/func_comp_cot/summary_cot.json`
- 模型路径: `/root/autodl-tmp/models_7b/Qwen/Qwen2.5-7B-Instruct/`

#### 下载和运行状况
- ModelScope 下载速度约 1-2MB/s/file（4 并行），总耗时约 60 分钟
- 7B 模型在 94GB RTX PRO 6000 上运行正常，batch_size=16 无 OOM
- 每个 depth 评估（500 samples）耗时约 18-93 秒

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f801bf70-ec52-470a-ba2d-0c375f997163",
  "uuid": "139b98e8-f185-4892-8782-018ce9d5547d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TTK3VLJGZqA1jK69kDsDbE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 279,
      "cache_read_input_tokens": 118125,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 279
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


### Tool call

_source line 513_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_018vNBkKapsbJZErSkRzemUq`</summary>

```json
{
  "todos": [
    {
      "content": "Download Qwen2.5-7B-Instruct model",
      "status": "completed",
      "activeForm": "Downloading Qwen2.5-7B-Instruct model"
    },
    {
      "content": "Wait for GPU to be free",
      "status": "completed",
      "activeForm": "Checking GPU availability"
    },
    {
      "content": "Run function composition eval (direct variant)",
      "status": "completed",
      "activeForm": "Running direct variant evaluation"
    },
    {
      "content": "Run function composition eval (CoT variant)",
      "status": "completed",
      "activeForm": "Running CoT variant evaluation"
    },
    {
      "content": "Report results",
      "status": "completed",
      "activeForm": "Reporting results"
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
  "session_id": "f801bf70-ec52-470a-ba2d-0c375f997163",
  "uuid": "0bee61a9-110b-4d4d-a738-027edede733b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TTK3VLJGZqA1jK69kDsDbE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 279,
      "cache_read_input_tokens": 118125,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 279
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


### Tool result

_source line 514 · 2026-05-18T11:09:02.198Z_

<details><summary>↩ Tool result · `toolu_018vNBkKapsbJZErSkRzemUq`</summary>

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
  "session_id": "f801bf70-ec52-470a-ba2d-0c375f997163",
  "uuid": "0768f5c0-61cb-42a0-81ad-d8484e61b62c",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Download Qwen2.5-7B-Instruct model",
        "status": "completed",
        "activeForm": "Downloading Qwen2.5-7B-Instruct model"
      },
      {
        "content": "Wait for GPU to be free",
        "status": "completed",
        "activeForm": "Checking GPU availability"
      },
      {
        "content": "Run function composition eval (direct variant)",
        "status": "completed",
        "activeForm": "Running direct variant evaluation"
      },
      {
        "content": "Run function composition eval (CoT variant)",
        "status": "completed",
        "activeForm": "Running CoT variant evaluation"
      },
      {
        "content": "Report results",
        "status": "in_progress",
        "activeForm": "Reporting results"
      }
    ],
    "newTodos": [
      {
        "content": "Download Qwen2.5-7B-Instruct model",
        "status": "completed",
        "activeForm": "Downloading Qwen2.5-7B-Instruct model"
      },
      {
        "content": "Wait for GPU to be free",
        "status": "completed",
        "activeForm": "Checking GPU availability"
      },
      {
        "content": "Run function composition eval (direct variant)",
        "status": "completed",
        "activeForm": "Running direct variant evaluation"
      },
      {
        "content": "Run function composition eval (CoT variant)",
        "status": "completed",
        "activeForm": "Running CoT variant evaluation"
      },
      {
        "content": "Report results",
        "status": "completed",
        "activeForm": "Reporting results"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---


### Task result

_source line 515_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 4610906,
  "duration_api_ms": 969287,
  "num_turns": 200,
  "stop_reason": "end_turn",
  "session_id": "f801bf70-ec52-470a-ba2d-0c375f997163",
  "total_cost_usd": 8.50100625,
  "usage": {
    "input_tokens": 199,
    "cache_creation_input_tokens": 173847,
    "cache_read_input_tokens": 13047503,
    "output_tokens": 35497,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 173847,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 2,
        "cache_read_input_tokens": 118404,
        "cache_creation_input_tokens": 1048,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1048
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2171,
      "outputTokens": 24,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002291,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 199,
      "outputTokens": 35497,
      "cacheReadInputTokens": 13047503,
      "cacheCreationInputTokens": 173847,
      "webSearchRequests": 0,
      "costUSD": 8.49871525,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "6a645a62-484d-4735-85fe-4426092aa6ca"
}
```

</details>

---
