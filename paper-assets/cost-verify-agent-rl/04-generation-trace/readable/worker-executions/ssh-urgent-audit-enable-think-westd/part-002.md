# ssh urgent audit enable think westd — Part 2 of 2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../ssh-urgent-audit-enable-think-westd.md) · [Structured JSON](../../../sessions/6b/6b776e843bbcdd6d6d88.json)

## Before a recorded user message

### Task result

_source line 223_

审计完成。以下是完整结果。

---

## enable_think 审计结果

### Config 层

| 来源 | enable_think | 备注 |
|------|------------|------|
| `base.yaml:142` | **True** | 默认值 |
| `eval.yaml:58` | **True** | |
| `_alfworld_8b_v9d_ood_eval.yaml` | **False** | 8B Cell C 的 OOD eval config |
| Cell A/C configs | **False** | 8B 实验 |

### v2 RAGEN Eval（即 Table 1 数据来源，25-31%）

| Seed | enable_think | 来源 | OOD Success | Episodes |
|------|-------------|------|-------------|----------|
| seed4 step15 | **True** | v2 config dump `agent_proxy.enable_think: True` | **30.6%** | 134 |
| seed5 step10 | **True** | v2 config dump `agent_proxy.enable_think: True` | **25.4%** | 134 |
| seed6 step15 | **True** | v2 config dump `agent_proxy.enable_think: True` | **29.1%** | 134 |

**结论：三个 seed 的 v2 RAGEN eval 全部 `enable_think=True`，与训练一致。Table 1 在 enable_think 维度是安全的。**

### table1_ood Standalone Eval（交叉验证，数值显著更低）

| Seed | enable_think | OOD Success | 状态 |
|------|-------------|-------------|------|
| seed4 step15 | **N/A（脚本无此参数）** | **6.7%** (9/134) | 完成 |
| seed5 step10 | **N/A** | **14.2%** (19/134) | 完成 |
| seed6 step15 | **N/A** | **incomplete** (93/134) | 中断 |

### ⚠️ 新发现的问题

standalone eval (`eval_checkpoint.py`) 与 RAGEN eval 的 **3 个关键差异**导致结果巨大落差（6.7-14.2% vs 25-31%）：

1. **Context window**: standalone 用 `HISTORY_LENGTH=5` 滑动窗口，RAGEN 用 `context_window_mode=full`（全部历史）
2. **Response prefix**: RAGEN 在生成后给 response 加 `&lt;think>` 前缀存入对话历史（`ctx_manager.py:1614`），standalone 不做此处理
3. **Prompt format**: standalone 的 action 不加 `&lt;answer>` tags（`&lt;/think>` 后直接输出 action），RAGEN 用 `&lt;think>...&lt;answer>...` 格式
4. **Chat template**: tokenizer_config.json 无自定义 chat_template，`apply_chat_template` 未传 `enable_thinking` 参数（两边行为一致，都用 Qwen3 默认）

这些差异意味着 standalone eval 数值不能直接替换 v2 RAGEN eval 的 Table 1 数据。如果 Table 1 使用 v2 数据则无问题；如果想用 standalone eval 验证，需要用 `eval_checkpoint_full_context.py`（全上下文版）重跑。

---

## seed200 v3 状态

- **PID 129823**: alive, 运行时间 ~56 分钟
- **Config**: `_alfworld_exp029_seed200_episode`, CUDA_VISIBLE_DEVICES=2,3
- **GPU 占用**: PID 132938 (45072 MiB) + PID 132939 (45774 MiB), 两张卡活跃
- **状态**: 正常运行中

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 599882,
  "duration_api_ms": 591429,
  "num_turns": 91,
  "stop_reason": "end_turn",
  "session_id": "c1669270-3c44-4d96-bdfb-d08861ee0a65",
  "total_cost_usd": 2.25897125,
  "usage": {
    "input_tokens": 29,
    "cache_creation_input_tokens": 114635,
    "cache_read_input_tokens": 1769059,
    "output_tokens": 26195,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 114635,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 2884,
        "cache_read_input_tokens": 120597,
        "cache_creation_input_tokens": 5879,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 5879
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2853,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002953,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 29,
      "outputTokens": 26195,
      "cacheReadInputTokens": 1769059,
      "cacheCreationInputTokens": 114635,
      "webSearchRequests": 0,
      "costUSD": 2.25601825,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "45a177ae-42f8-4aa5-a14a-43b00d4d967f"
}
```

</details>

---
