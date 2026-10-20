# audit appendix tables — Part 2 of 2

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../audit-appendix-tables.md) · [Structured JSON](../../../sessions/dc/dc1fe478bf6c4b0f4aa9.json)

## Round 1

### Tool result

_source line 154 · 2026-05-25T20:32:27.205Z_

<details><summary>↩ Tool result · `toolu_01H6vyQUc8EKJsQ44btpkfLr`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260525_a9e003\", \"name\": \"audit_appendix_tables\", \"type\": \"report\", \"description\": \"附录+表格数据全量审计报告：550+数字验证，10个问题（4中等6低）\", \"path\": \"projects/turn_residual_gating/artifacts/_project/report/audit_appendix_tables.md\", \"url\": null, \"project\": \"turn_residual_gating\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-25T20:32:27.091216+00:00\", \"tags\": [\"audit\", \"paper\", \"data-verification\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b876a478-60f0-4511-a493-7e7c488da19e",
  "uuid": "a0d3b907-ea86-47fe-94ea-4e7ed1378190",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260525_a9e003\\\", \\\"name\\\": \\\"audit_appendix_tables\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"附录+表格数据全量审计报告：550+数字验证，10个问题（4中等6低）\\\", \\\"path\\\": \\\"projects/turn_residual_gating/artifacts/_project/report/audit_appendix_tables.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"turn_residual_gating\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-25T20:32:27.091216+00:00\\\", \\\"tags\\\": [\\\"audit\\\", \\\"paper\\\", \\\"data-verification\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260525_a9e003\", \"name\": \"audit_appendix_tables\", \"type\": \"report\", \"description\": \"附录+表格数据全量审计报告：550+数字验证，10个问题（4中等6低）\", \"path\": \"projects/turn_residual_gating/artifacts/_project/report/audit_appendix_tables.md\", \"url\": null, \"project\": \"turn_residual_gating\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-25T20:32:27.091216+00:00\", \"tags\": [\"audit\", \"paper\", \"data-verification\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 155_

审计完成。550+ 个数字已逐一验证，发现 10 个问题：

**4 个中等问题需修正：**
1. **Table 1 IID 列** — IID PPL（2.78）疑似从 Heldout 列复制，registry 实测为 2.62-2.63；TG/LoRA IID GAR-O 也偏高
2. **MMLU 最大 per-category 降幅** — 正文写 1.2pp，实际 STEM 列为 1.49pp
3. **SS max ratio 矛盾** — appendix-hyper 写 0.5，appendix-ss 写 0.3，实际数据来自 0.3 协议
4. **Llama VRAM** — 表写 46GB，registry 显示 63.4GB

**6 个低优先级问题：** gap ratio 四舍五入不一致（7.8× vs 7.9×，~1.3× vs 1.2×）、"≤1pp" 声明实际为 2pp、PPL std ±0.001 应为 ±0.002、MMLU 表标签 "Base (LoRA-only)" 误导、训练时间四舍五入偏差。

报告已写入 `artifacts/audit_appendix_tables.md`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b876a478-60f0-4511-a493-7e7c488da19e",
  "uuid": "8cbee80b-0913-4347-9bf8-32d5e3d3d3e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Y39WArTNrsbHuskFojjRX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 517,
      "cache_read_input_tokens": 135594,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 517
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

_source line 156_

审计完成。550+ 个数字已逐一验证，发现 10 个问题：

**4 个中等问题需修正：**
1. **Table 1 IID 列** — IID PPL（2.78）疑似从 Heldout 列复制，registry 实测为 2.62-2.63；TG/LoRA IID GAR-O 也偏高
2. **MMLU 最大 per-category 降幅** — 正文写 1.2pp，实际 STEM 列为 1.49pp
3. **SS max ratio 矛盾** — appendix-hyper 写 0.5，appendix-ss 写 0.3，实际数据来自 0.3 协议
4. **Llama VRAM** — 表写 46GB，registry 显示 63.4GB

**6 个低优先级问题：** gap ratio 四舍五入不一致（7.8× vs 7.9×，~1.3× vs 1.2×）、"≤1pp" 声明实际为 2pp、PPL std ±0.001 应为 ±0.002、MMLU 表标签 "Base (LoRA-only)" 误导、训练时间四舍五入偏差。

报告已写入 `artifacts/audit_appendix_tables.md`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 1224043,
  "duration_api_ms": 1223389,
  "num_turns": 48,
  "stop_reason": "end_turn",
  "session_id": "b876a478-60f0-4511-a493-7e7c488da19e",
  "total_cost_usd": 3.6343074999999994,
  "usage": {
    "input_tokens": 20,
    "cache_creation_input_tokens": 124270,
    "cache_read_input_tokens": 1135818,
    "output_tokens": 51943,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 124270,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 370,
        "cache_read_input_tokens": 135594,
        "cache_creation_input_tokens": 517,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 517
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1540,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001625,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 36,
      "outputTokens": 62769,
      "cacheReadInputTokens": 1621205,
      "cacheCreationInputTokens": 200428,
      "webSearchRequests": 0,
      "costUSD": 3.632682499999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "666ca217-d1ae-4148-93d6-8eaf4e25707e"
}
```

</details>

---
