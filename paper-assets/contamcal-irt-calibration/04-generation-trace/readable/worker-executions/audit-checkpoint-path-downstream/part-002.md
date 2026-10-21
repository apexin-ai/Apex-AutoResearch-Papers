# audit checkpoint path downstream — Part 2 of 2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../audit-checkpoint-path-downstream.md) · [Structured JSON](../../../sessions/49/49738924ea3304f015c9.json)

## Before a recorded user message

### Task result

_source line 163_

所有数据收集和 registry 更新完成。以下是审计报告：

---

## 审计报告

### 1. 下游污染检查

**Eval 实验 — 无污染**
- `exp_001_eval_3B_d025_v2_aligned` / `v2_para_aligned` 引用 `Qwen2.5-3B_d025_s42/lora_adapter`（alpha=16），但这是 v2 eval，对应 v2 SFT，引用正确
- **不存在 v3 eval 实验**（无 `exp_001_eval_3B_d025_v3_*`），所以没有 eval 被旧 checkpoint 污染

**Signals — 存在问题**
- `/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_s42/` 包含 s1/s2/s4 信号（arc_challenge, gsm8k, 部分 mmlu）
- 信号计算时间：May 16 02:31-04:00；v3 checkpoint 创建时间：May 16 04:15
- **信号必然使用了旧 `d025_s42`（alpha=16）checkpoint**
  - s1 (embedding): 使用 sentence-transformers，不依赖 SFT adapter → **无影响**
  - s2 (minkpp) 和 s4 (selfcritique): 加载 SFT adapter → **使用了错误的 alpha=16 模型**
- **如果 IRT 流程需要 alpha=32 的 d025 signals，需用 `d025_v3_s42` checkpoint 重新计算 s2/s4**

### 2. _a32_ checkpoint 审计表

| 实验 ID | Registry Status | Conclusion | checkpoint_path | 磁盘 lora_adapter/ |
|---------|----------------|------------|----------------|-------------------|
| `exp_001_sft_3B_d100_s42_a32` | DONE | killed ✅ (已更新) | 空 | 空（0 files） |
| `exp_001_sft_3B_d100_s42_a32_v2` | DONE | failed ✅ (已更新) | 空 | 空（0 files） |
| `exp_001_sft_3B_d025_s42_a32` | DONE | killed ✅ (已更新) | 空（spec 中指向空目录） | 空（0 files） |

磁盘上还存在无 registry 条目的孤立 _a32_ 目录：
- `Qwen2.5-3B_d000_a32_s42` — lora_adapter 空
- `Qwen2.5-3B_d100_a32_s123` — lora_adapter 完全空
- `Qwen2.5-3B_d100_a32_s42_v3` — lora_adapter 空

所有 _a32_ checkpoint 均为空壳，无可用权重。Registry 已标记 conclusion。

### 3. train_config.json 补写结果

**无需补写。** `Qwen2.5-3B_d025_v3_s42/train_config.json` 已存在，内容正确：
```json
{
  "lora_r": 16,
  "lora_alpha": 32,
  "lr": 5e-05,
  "seed": 42,
  "num_samples": 54133
}
```

所有 _a32_ checkpoint 为空壳，不补写 train_config.json。

### 需要决策

d025 的 s2/s4 signals 是否需要用 v3 (alpha=32) checkpoint 重新计算？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 371563,
  "duration_api_ms": 348044,
  "num_turns": 65,
  "stop_reason": "end_turn",
  "session_id": "f6cb3271-f79e-4ac3-8375-31c24e710823",
  "total_cost_usd": 1.6499290000000002,
  "usage": {
    "input_tokens": 24,
    "cache_creation_input_tokens": 93348,
    "cache_read_input_tokens": 1035620,
    "output_tokens": 21841,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 93348,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1913,
        "cache_read_input_tokens": 77931,
        "cache_creation_input_tokens": 2114,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2114
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2459,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0025489999999999996,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 24,
      "outputTokens": 21841,
      "cacheReadInputTokens": 1035620,
      "cacheCreationInputTokens": 93348,
      "webSearchRequests": 0,
      "costUSD": 1.64738,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "f51dbbc7-a5fd-4341-858b-d67188e4a3fc"
}
```

</details>

---
