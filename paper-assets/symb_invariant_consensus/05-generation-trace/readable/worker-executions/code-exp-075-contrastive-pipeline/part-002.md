# code exp 075 contrastive pipeline — Part 2 of 2

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../code-exp-075-contrastive-pipeline.md) · [Structured JSON](../../../sessions/40/40ed646e724a8a4ae454.json)

## Before a recorded user message

### Tool result

_source line 245 · 2026-05-19T16:59:33.094Z_

<details><summary>↩ Tool result · `toolu_01SX4XDBXtoMMikKKFUgS5MT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "249d31fd-a8ae-4cdf-bf55-60d16e8ec5b7",
  "uuid": "9d9e4f75-e4d1-443f-93a6-6328ee091ae6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 246_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01YGdFohM5Dx1aKMHbE3RwTy`</summary>

```json
{
  "todos": [
    {
      "content": "Read existing codebase and understand architecture",
      "status": "completed",
      "activeForm": "Reading existing codebase"
    },
    {
      "content": "Write run_contrastive.py locally",
      "status": "completed",
      "activeForm": "Writing run_contrastive.py"
    },
    {
      "content": "Deploy run_contrastive.py to server",
      "status": "completed",
      "activeForm": "Deploying to server"
    },
    {
      "content": "Dry-run: C001 pre-flight checks (imports, paths, ports)",
      "status": "completed",
      "activeForm": "Running C001 pre-flight checks"
    },
    {
      "content": "Dry-run 5 problems with mock mode",
      "status": "completed",
      "activeForm": "Running mock dry-run"
    },
    {
      "content": "Dry-run 5 problems with vLLM",
      "status": "completed",
      "activeForm": "Running vLLM dry-run"
    },
    {
      "content": "Clean up dry-run temp files",
      "status": "completed",
      "activeForm": "Cleaning up dry-run temp files"
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
  "session_id": "249d31fd-a8ae-4cdf-bf55-60d16e8ec5b7",
  "uuid": "e941d560-1d19-4c55-a83a-eaa3be8c3a71",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WaFew2X4U5jZBt4R4uAdwC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 256,
      "cache_read_input_tokens": 157788,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 256
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

_source line 247 · 2026-05-19T16:59:37.910Z_

<details><summary>↩ Tool result · `toolu_01YGdFohM5Dx1aKMHbE3RwTy`</summary>

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
  "session_id": "249d31fd-a8ae-4cdf-bf55-60d16e8ec5b7",
  "uuid": "4df8c068-8517-4156-b0c1-a7d362a42b1f",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Read existing codebase and understand architecture",
        "status": "completed",
        "activeForm": "Reading existing codebase"
      },
      {
        "content": "Write run_contrastive.py locally",
        "status": "completed",
        "activeForm": "Writing run_contrastive.py"
      },
      {
        "content": "Deploy run_contrastive.py to server",
        "status": "completed",
        "activeForm": "Deploying to server"
      },
      {
        "content": "Dry-run: C001 pre-flight checks (imports, paths, ports)",
        "status": "completed",
        "activeForm": "Running C001 pre-flight checks"
      },
      {
        "content": "Dry-run 5 problems with mock mode",
        "status": "completed",
        "activeForm": "Running mock dry-run"
      },
      {
        "content": "Dry-run 5 problems with vLLM",
        "status": "completed",
        "activeForm": "Running vLLM dry-run"
      },
      {
        "content": "Clean up dry-run temp files",
        "status": "in_progress",
        "activeForm": "Cleaning up dry-run temp files"
      }
    ],
    "newTodos": [
      {
        "content": "Read existing codebase and understand architecture",
        "status": "completed",
        "activeForm": "Reading existing codebase"
      },
      {
        "content": "Write run_contrastive.py locally",
        "status": "completed",
        "activeForm": "Writing run_contrastive.py"
      },
      {
        "content": "Deploy run_contrastive.py to server",
        "status": "completed",
        "activeForm": "Deploying to server"
      },
      {
        "content": "Dry-run: C001 pre-flight checks (imports, paths, ports)",
        "status": "completed",
        "activeForm": "Running C001 pre-flight checks"
      },
      {
        "content": "Dry-run 5 problems with mock mode",
        "status": "completed",
        "activeForm": "Running mock dry-run"
      },
      {
        "content": "Dry-run 5 problems with vLLM",
        "status": "completed",
        "activeForm": "Running vLLM dry-run"
      },
      {
        "content": "Clean up dry-run temp files",
        "status": "completed",
        "activeForm": "Cleaning up dry-run temp files"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---


### Assistant

_source line 248_

所有任务完成。`run_contrastive.py` 已部署到 `westd-25068:/root/symb_invariant_consensus/run_contrastive.py`，5 题 vLLM dry-run 验证通过。

**实现摘要**：

- **596 行**，三阶段 pipeline：
  - **Phase 1**: 复用 `VLLMGenerator` 生成 K=12 traces + SC 投票确定候选集
  - **Phase 2**: 对每个候选答案，用新设计的 `CONTRASTIVE_PROMPT` 调用 LLM K_contrast=3 次，分别生成 pro/con FOL 约束，每条约束经 `parse_z3_formula` 验证兼容性
  - **Phase 3**: 对每个候选独立运行 MAX-SAT：`score = MAX-SAT(pro) - MAX-SAT(con)`，取最高分答案
- **复用模块**: `VLLMGenerator`, `VLLMBackend`, `ConstraintDeduplicator`, `MaxSATSolver`, `SelfConsistency`, `normalize_logic_answer`
- **特性**: resume 支持、checkpoint、save-intermediates、degenerate case 处理、ETA 估算
- **CLI 接口**与任务要求完全一致
- vLLM 未由本 Worker 启动（复用了已有的 port 8000），无需清理

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "249d31fd-a8ae-4cdf-bf55-60d16e8ec5b7",
  "uuid": "e6d58873-6513-413d-b433-21582169927b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdYNoini8ej23vLLg8wbYg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 343,
      "cache_read_input_tokens": 158044,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 343
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    },
    "context_management": null
  }
}
```

</details>

---


### Task result

_source line 249_

所有任务完成。`run_contrastive.py` 已部署到 `westd-25068:/root/symb_invariant_consensus/run_contrastive.py`，5 题 vLLM dry-run 验证通过。

**实现摘要**：

- **596 行**，三阶段 pipeline：
  - **Phase 1**: 复用 `VLLMGenerator` 生成 K=12 traces + SC 投票确定候选集
  - **Phase 2**: 对每个候选答案，用新设计的 `CONTRASTIVE_PROMPT` 调用 LLM K_contrast=3 次，分别生成 pro/con FOL 约束，每条约束经 `parse_z3_formula` 验证兼容性
  - **Phase 3**: 对每个候选独立运行 MAX-SAT：`score = MAX-SAT(pro) - MAX-SAT(con)`，取最高分答案
- **复用模块**: `VLLMGenerator`, `VLLMBackend`, `ConstraintDeduplicator`, `MaxSATSolver`, `SelfConsistency`, `normalize_logic_answer`
- **特性**: resume 支持、checkpoint、save-intermediates、degenerate case 处理、ETA 估算
- **CLI 接口**与任务要求完全一致
- vLLM 未由本 Worker 启动（复用了已有的 port 8000），无需清理

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 1089655,
  "duration_api_ms": 1000969,
  "num_turns": 100,
  "stop_reason": "end_turn",
  "session_id": "249d31fd-a8ae-4cdf-bf55-60d16e8ec5b7",
  "total_cost_usd": 7.409361499999998,
  "usage": {
    "input_tokens": 90,
    "cache_creation_input_tokens": 192326,
    "cache_read_input_tokens": 10016656,
    "output_tokens": 47872,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 192326,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 394,
        "cache_read_input_tokens": 158044,
        "cache_creation_input_tokens": 343,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 343
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1666,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001746,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 90,
      "outputTokens": 47872,
      "cacheReadInputTokens": 10016656,
      "cacheCreationInputTokens": 192326,
      "webSearchRequests": 0,
      "costUSD": 7.407615499999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "df0037d1-9e1b-4248-bc2a-1206272a2637"
}
```

</details>

---
