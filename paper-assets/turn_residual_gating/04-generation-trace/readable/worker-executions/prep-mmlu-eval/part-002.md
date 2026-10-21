# prep mmlu eval — Part 2 of 2

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../prep-mmlu-eval.md) · [Structured JSON](../../../sessions/4e/4e7418912efb42ee2f8f.json)

## Before a recorded user message

### Task result

_source line 469_

Dry-run completed successfully. GPU is now nearly free (5.6GB used — SS training appears to have finished). Here's the summary report.

---

## MMLU 5-shot 评估环境准备完成

### 环境
- **lm-evaluation-harness**: v0.4.12 (pip)
- **Python**: 3.12.3 (conda base)
- **GPU**: NVIDIA RTX PRO 6000 Blackwell, 98GB — 当前空闲（5.6GB used）
- **HF mirror**: `HF_ENDPOINT=https://hf-mirror.com`（服务器无法直连 HuggingFace）
- **MMLU 数据集**: 已缓存到 `/root/autodl-tmp/.hf_cache`

### Checkpoint 路径 (全部为 LoRA adapter)

| 条件 | 路径 | gate_params.pt |
|------|------|----------------|
| **base_qwen** | `none`（直接用 base model） | — |
| **lo_s42** | `runs/phase2_lora_only_s42/lora/` | 无 |
| **tg_v7_s42** | `runs/phase2_tg_s42_v7/lora/` | 有 |
| **ug_s42** | `runs/phase2_ug_s42/lora/` | 有 |
| **pcgrad_v9_s42** | `checkpoints/tg_v9_pcgrad_s42/lora/` | 有 |
| **ss_v8b_s42** | `runs/d048_ss_s42/lora/` | 有 |

- Base model: `/root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct`
- 所有 adapter 配置一致: LoRA r=16, alpha=32, target q_proj+v_proj
- Gate weights 存在但对 MMLU（单轮 QA）无影响，直接用 LoRA adapter 即可

### 脚本

| 脚本 | 用法 |
|------|------|
| `scripts/mmlu_eval_single.sh` | `bash scripts/mmlu_eval_single.sh &lt;adapter_path\|none> &lt;name> [--limit N]` |
| `scripts/mmlu_eval_all.sh` | `bash scripts/mmlu_eval_all.sh [--limit N]`，串行跑 6 个条件 |

### Dry-run 验证
- `--limit 2` 在 base model 上成功完成
- Auto batch size: 28
- 456 loglikelihood requests 用时 66s
- 结果已保存到 `results/mmlu/dryrun/`

### 时间估算
- 单个条件全量 MMLU: ~30–60 min（Blackwell GPU + batch_size=28）
- 6 个条件串行: ~3–6h
- 注意：GPU 当前空闲，可以立即启动

### 注意事项
- SS s456 训练似乎已经完成（GPU 占用从 45GB 降到 5.6GB），建议确认
- 启动全量评估: `nohup bash scripts/mmlu_eval_all.sh > /tmp/mmlu_eval_all.log 2>&1 &`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 1044748,
  "duration_api_ms": 817705,
  "num_turns": 198,
  "stop_reason": "end_turn",
  "session_id": "369fbc2e-855c-4dfa-9567-6799bfd5e7ff",
  "total_cost_usd": 8.234686750000002,
  "usage": {
    "input_tokens": 168,
    "cache_creation_input_tokens": 99995,
    "cache_read_input_tokens": 13553748,
    "output_tokens": 33192,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 99995,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 2785,
        "cache_read_input_tokens": 110897,
        "cache_creation_input_tokens": 545,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 545
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2084,
      "outputTokens": 24,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002204,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 168,
      "outputTokens": 33192,
      "cacheReadInputTokens": 13553748,
      "cacheCreationInputTokens": 99995,
      "webSearchRequests": 0,
      "costUSD": 8.23248275,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "20ad8b97-6cb1-439d-8217-bb162798257b"
}
```

</details>

---
