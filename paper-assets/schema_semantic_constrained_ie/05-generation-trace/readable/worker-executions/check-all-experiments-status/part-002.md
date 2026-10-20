# check all experiments status — Part 2 of 2

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../check-all-experiments-status.md) · [Structured JSON](../../../sessions/7a/7ab0e78dba0049ba4f68.json)

## Before a recorded user message

### Task result

_source line 208_

Cron 已设置。汇总当前状态：

---

## 已完成实验评估结果

| 实验 | DR% | RV% | ET% | CF | R-F1 | E-F1 | Parse% | 状态 |
|------|-----|-----|-----|-----|------|------|--------|------|
| **70B LoRA SciERC unconstrained** | 1.5 | 0 | 0 | 0 | 44.73 | 64.86 | 100 | DONE |
| **70B LoRA SciERC beam4_s1 (full)** | 0 | 0 | 0 | 0 | 44.81 | 64.89 | 100 | DONE |
| **70B LoRA SciERC grammar_only** | 1.5 | 0 | 0 | 0 | 44.63 | 64.82 | 100 | DONE (negative) |
| **70B LoRA SciERC semantic_only** | **0.6** | 0 | 0 | 9 | **44.73** | 64.86 | 100 | DONE (new) |
| **70B LoRA SciERC full_s2** | **0** | 0 | 0 | 18 | **36.28** | 62.35 | 100 | DONE (negative) |
| **70B ZS SciERC unconstrained** | 6.4 | 0.6 | 0 | 0 | 11.23 | 35.22 | 100 | DONE (new) |

### 关键发现

- **semantic_only**: DR 从 1.5%→0.6%，R-F1 不变（44.73）。语义层单独贡献 DR 下降，无 F1 损失。
- **grammar_only**: DR 仍 1.5%，与 unconstrained 一致 → grammar 层对 DR 零贡献。conclusion 已修正为 negative。
- **full_s2**: DR=0% 但 R-F1 暴跌至 36.28（-8.5pp），E-F1 也降到 62.35。S2 模式过度约束导致 recall 大幅下降。

## GPU 使用状态

| 服务器 | GPU 0 | GPU 1 |
|--------|-------|-------|
| **westd-16980** | eval_70b_lora_docred_200_semantic_only (新启动) | eval_70b_lora_docred_200_grammar_only (新启动) |
| **westd-21461** | eval_70b_zs_docred_200_semantic_only (新启动) | eval_70b_lora_docred_200_beam4_s1 (160/200) |

## Registry 修复

- `eval_70b_lora_scierc_grammar_only` conclusion: success → **negative** (已修复)

## 新启动实验 (3个)

1. **eval_70b_lora_docred_200_semantic_only** — westd-16980 GPU 0, PID 983803
2. **eval_70b_lora_docred_200_grammar_only** — westd-16980 GPU 1, PID 984253
3. **eval_70b_zs_docred_200_semantic_only** — westd-21461 GPU 0, PID 78742

Cron 每 12 分钟轮询进度，完成后自动评估并更新 registry。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 616336,
  "duration_api_ms": 483730,
  "num_turns": 86,
  "stop_reason": "end_turn",
  "session_id": "32621180-93b2-45d3-863b-e3eab636106c",
  "total_cost_usd": 2.2867667499999995,
  "usage": {
    "input_tokens": 35,
    "cache_creation_input_tokens": 106971,
    "cache_read_input_tokens": 1894572,
    "output_tokens": 26754,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 106971,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 949,
        "cache_read_input_tokens": 100514,
        "cache_creation_input_tokens": 684,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 684
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1817,
      "outputTokens": 14,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001887,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 35,
      "outputTokens": 26754,
      "cacheReadInputTokens": 1894572,
      "cacheCreationInputTokens": 106971,
      "webSearchRequests": 0,
      "costUSD": 2.2848797499999995,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "83df9436-ee03-414e-bb85-056cc076747d"
}
```

</details>

---
