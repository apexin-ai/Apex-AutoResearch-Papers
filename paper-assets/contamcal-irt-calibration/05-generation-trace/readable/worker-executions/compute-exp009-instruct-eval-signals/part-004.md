# compute exp009 instruct eval signals — Part 4 of 4

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Worker execution logs

[← Part 3](part-003.md) · [Transcript overview](../compute-exp009-instruct-eval-signals.md) · [Structured JSON](../../../sessions/9a/9a466133692df0a03f89.json)

## Round 1

### Tool result

_source line 1463 · 2026-05-17T05:05:07.558Z_

<details><summary>↩ Tool result · `toolu_015nBr8eJCML5Ap87pio684Z`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"Llama-3.2-3B_d000_s42\\nLlama-3.2-3B_d005_s42\\nLlama-3.2-3B_d025_s42\\nLlama-3.2-3B_d100_s42\\nQwen2.5-0.5B-Instruct\\nQwen2.5-0.5B_d000_s123\\nQwen2.5-0.5B_d000_s42\\nQwen2.5-0.5B_d005_s123\\nQwen2.5-0.5B_d005_s42\\nQwen2.5-0.5B_d025_s123\\nQwen2.5-0.5B_d025_s42\\nQwen2.5-0.5B_d100_s123\\nQwen2.5-0.5B_d100_s42\\nQwen2.5-1.5B-Instruct\\nQwen2.5-1.5B_d000_s123\\nQwen2.5-1.5B_d000_s42\\nQwen2.5-1.5B_d005_s123\\nQwen2.5-1.5B_d005_s42\\nQwen2.5-1.5B_d025_s123\\nQwen2.5-1.5B_d025_s42\\nQwen2.5-1.5B_d100_s123\\nQwen2.5-1.5B_d100_s42\\nQwen2.5-3B_d000_a32_s42\\nQwen2.5-3B_d000_s123\\nQwen2.5-3B_d000_s123_a32\\nQwen2.5-3B_d000_s42_a32\\nQwen2.5-3B_d000_v2_s42\\nQwen2.5-3B_d005_a32_s42\\nQwen2.5-3B_d005_s123\\nQwen2.5-3B_d005_s42\\nQwen2.5-3B_d005_s42_a32\\nQwen2.5-3B_d025_s123\\nQwen2.5-3B_d025_s42\\nQwen2.5-3B_d025_s42_DEPRECATED_alpha16\\nQwen2.5-3B_d025_s42_old_alpha16\\nQwen2.5-3B_d025_v3_s42\\nQwen2.5-3B_d100_a32_s123\\nQwen2.5-3B_d100_a32_s42\\nQwen2.5-3B_d100_s42\\nbatch_report_Qwen2.5-0.5B.json\\nbatch_report_Qwen2.5-1.5B.json\\nbatch_report_Qwen2.5-3B.json\\nrrf\\ns1_recompute_cuda0.log\\ns1_recompute_cuda1.log\\nsignals_05B_s123_v2.log\\nsignals_3B_d025_v3_s42.log\\nsignals_3B_v6.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0fe447ab-d377-4ae2-840f-8f8274744c34",
  "uuid": "b8c79df3-29e1-4dae-8c31-47fe36546ee6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"Llama-3.2-3B_d000_s42\\\\nLlama-3.2-3B_d005_s42\\\\nLlama-3.2-3B_d025_s42\\\\nLlama-3.2-3B_d100_s42\\\\nQwen2.5-0.5B-Instruct\\\\nQwen2.5-0.5B_d000_s123\\\\nQwen2.5-0.5B_d000_s42\\\\nQwen2.5-0.5B_d005_s123\\\\nQwen2.5-0.5B_d005_s42\\\\nQwen2.5-0.5B_d025_s123\\\\nQwen2.5-0.5B_d025_s42\\\\nQwen2.5-0.5B_d100_s123\\\\nQwen2.5-0.5B_d100_s42\\\\nQwen2.5-1.5B-Instruct\\\\nQwen2.5-1.5B_d000_s123\\\\nQwen2.5-1.5B_d000_s42\\\\nQwen2.5-1.5B_d005_s123\\\\nQwen2.5-1.5B_d005_s42\\\\nQwen2.5-1.5B_d025_s123\\\\nQwen2.5-1.5B_d025_s42\\\\nQwen2.5-1.5B_d100_s123\\\\nQwen2.5-1.5B_d100_s42\\\\nQwen2.5-3B_d000_a32_s42\\\\nQwen2.5-3B_d000_s123\\\\nQwen2.5-3B_d000_s123_a32\\\\nQwen2.5-3B_d000_s42_a32\\\\nQwen2.5-3B_d000_v2_s42\\\\nQwen2.5-3B_d005_a32_s42\\\\nQwen2.5-3B_d005_s123\\\\nQwen2.5-3B_d005_s42\\\\nQwen2.5-3B_d005_s42_a32\\\\nQwen2.5-3B_d025_s123\\\\nQwen2.5-3B_d025_s42\\\\nQwen2.5-3B_d025_s42_DEPRECATED_alpha16\\\\nQwen2.5-3B_d025_s42_old_alpha16\\\\nQwen2.5-3B_d025_v3_s42\\\\nQwen2.5-3B_d100_a32_s123\\\\nQwen2.5-3B_d100_a32_s42\\\\nQwen2.5-3B_d100_s42\\\\nbatch_report_Qwen2.5-0.5B.json\\\\nbatch_report_Qwen2.5-1.5B.json\\\\nbatch_report_Qwen2.5-3B.json\\\\nrrf\\\\ns1_recompute_cuda0.log\\\\ns1_recompute_cuda1.log\\\\nsignals_05B_s123_v2.log\\\\nsignals_3B_d025_v3_s42.log\\\\nsignals_3B_v6.log\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.37}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"Llama-3.2-3B_d000_s42\\nLlama-3.2-3B_d005_s42\\nLlama-3.2-3B_d025_s42\\nLlama-3.2-3B_d100_s42\\nQwen2.5-0.5B-Instruct\\nQwen2.5-0.5B_d000_s123\\nQwen2.5-0.5B_d000_s42\\nQwen2.5-0.5B_d005_s123\\nQwen2.5-0.5B_d005_s42\\nQwen2.5-0.5B_d025_s123\\nQwen2.5-0.5B_d025_s42\\nQwen2.5-0.5B_d100_s123\\nQwen2.5-0.5B_d100_s42\\nQwen2.5-1.5B-Instruct\\nQwen2.5-1.5B_d000_s123\\nQwen2.5-1.5B_d000_s42\\nQwen2.5-1.5B_d005_s123\\nQwen2.5-1.5B_d005_s42\\nQwen2.5-1.5B_d025_s123\\nQwen2.5-1.5B_d025_s42\\nQwen2.5-1.5B_d100_s123\\nQwen2.5-1.5B_d100_s42\\nQwen2.5-3B_d000_a32_s42\\nQwen2.5-3B_d000_s123\\nQwen2.5-3B_d000_s123_a32\\nQwen2.5-3B_d000_s42_a32\\nQwen2.5-3B_d000_v2_s42\\nQwen2.5-3B_d005_a32_s42\\nQwen2.5-3B_d005_s123\\nQwen2.5-3B_d005_s42\\nQwen2.5-3B_d005_s42_a32\\nQwen2.5-3B_d025_s123\\nQwen2.5-3B_d025_s42\\nQwen2.5-3B_d025_s42_DEPRECATED_alpha16\\nQwen2.5-3B_d025_s42_old_alpha16\\nQwen2.5-3B_d025_v3_s42\\nQwen2.5-3B_d100_a32_s123\\nQwen2.5-3B_d100_a32_s42\\nQwen2.5-3B_d100_s42\\nbatch_report_Qwen2.5-0.5B.json\\nbatch_report_Qwen2.5-1.5B.json\\nbatch_report_Qwen2.5-3B.json\\nrrf\\ns1_recompute_cuda0.log\\ns1_recompute_cuda1.log\\nsignals_05B_s123_v2.log\\nsignals_3B_d025_v3_s42.log\\nsignals_3B_v6.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 1464_

<details><summary>Logged reasoning block</summary>

```text
Confirmed: existing Instruct signals are at:
- `/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B-Instruct/`
- `/root/autodl-tmp/exp002/signals/Qwen2.5-1.5B-Instruct/`

Now let me provide the final comprehensive status report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0fe447ab-d377-4ae2-840f-8f8274744c34",
  "uuid": "1b48465a-4959-4429-85ff-ca48c56e068f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JAYivxTGnC3sTgZWsmAoXE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1046,
      "cache_read_input_tokens": 135238,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1046
      },
      "output_tokens": 29,
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


### Assistant

_source line 1465_

All tasks complete. Here's the final status:

## exp-009 Status Report

### Signals Computation (COMPLETE)

| Model | GPU | Status | Duration | Output |
|-------|-----|--------|----------|--------|
| Qwen2.5-3B-Instruct | cuda:5 | DONE | ~31 min (12:18→12:48) | `/root/autodl-tmp/exp009/signals/Qwen2.5-3B-Instruct/` |
| DeepSeek-R1-Distill-Qwen-1.5B | cuda:3 | DONE | ~29 min (12:18→12:46) | `/root/autodl-tmp/exp009/signals/DeepSeek-R1-Distill-Qwen-1.5B/` |

**Output files** (18 total, 9 per model):
- `{mmlu,arc_challenge,gsm8k}/signal_minkpp_*.json`
- `{mmlu,arc_challenge,gsm8k}/signal_selfcritique_*.json`
- `{mmlu,arc_challenge,gsm8k}/signals_merged_*.json`

### DeepSeek Eval (IN PROGRESS)

| Benchmark | Status | Accuracy |
|-----------|--------|----------|
| mmlu | DONE | 22.95% (3222/14042) |
| arc_challenge | DONE | 22.61% (265/1172) |
| gsm8k | RUNNING (~5s/it, ETA ~1.5h) | pending |

GSM8K eval is slow because DeepSeek-R1-Distill generates long chain-of-thought reasoning per item. Running in tmux session `exp009_deepseek` on cuda:3.

### Existing Instruct Signals (confirmed)
- `/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B-Instruct/`
- `/root/autodl-tmp/exp002/signals/Qwen2.5-1.5B-Instruct/`

The gsm8k eval will complete autonomously in the tmux session. Final results will be saved to `/root/autodl-tmp/exp009/eval_results/DeepSeek-R1-Distill-Qwen-1.5B/gsm8k_results.json`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0fe447ab-d377-4ae2-840f-8f8274744c34",
  "uuid": "c4250fb4-74d2-4db1-8c72-95bb716138e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JAYivxTGnC3sTgZWsmAoXE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1046,
      "cache_read_input_tokens": 135238,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1046
      },
      "output_tokens": 29,
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

_source line 1466_

All tasks complete. Here's the final status:

## exp-009 Status Report

### Signals Computation (COMPLETE)

| Model | GPU | Status | Duration | Output |
|-------|-----|--------|----------|--------|
| Qwen2.5-3B-Instruct | cuda:5 | DONE | ~31 min (12:18→12:48) | `/root/autodl-tmp/exp009/signals/Qwen2.5-3B-Instruct/` |
| DeepSeek-R1-Distill-Qwen-1.5B | cuda:3 | DONE | ~29 min (12:18→12:46) | `/root/autodl-tmp/exp009/signals/DeepSeek-R1-Distill-Qwen-1.5B/` |

**Output files** (18 total, 9 per model):
- `{mmlu,arc_challenge,gsm8k}/signal_minkpp_*.json`
- `{mmlu,arc_challenge,gsm8k}/signal_selfcritique_*.json`
- `{mmlu,arc_challenge,gsm8k}/signals_merged_*.json`

### DeepSeek Eval (IN PROGRESS)

| Benchmark | Status | Accuracy |
|-----------|--------|----------|
| mmlu | DONE | 22.95% (3222/14042) |
| arc_challenge | DONE | 22.61% (265/1172) |
| gsm8k | RUNNING (~5s/it, ETA ~1.5h) | pending |

GSM8K eval is slow because DeepSeek-R1-Distill generates long chain-of-thought reasoning per item. Running in tmux session `exp009_deepseek` on cuda:3.

### Existing Instruct Signals (confirmed)
- `/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B-Instruct/`
- `/root/autodl-tmp/exp002/signals/Qwen2.5-1.5B-Instruct/`

The gsm8k eval will complete autonomously in the tmux session. Final results will be saved to `/root/autodl-tmp/exp009/eval_results/DeepSeek-R1-Distill-Qwen-1.5B/gsm8k_results.json`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 2926467,
  "duration_api_ms": 2569877,
  "num_turns": 591,
  "stop_reason": "end_turn",
  "session_id": "0fe447ab-d377-4ae2-840f-8f8274744c34",
  "total_cost_usd": 24.120079249999996,
  "usage": {
    "input_tokens": 416,
    "cache_creation_input_tokens": 279416,
    "cache_read_input_tokens": 39743686,
    "output_tokens": 92839,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 279416,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 686,
        "cache_read_input_tokens": 135238,
        "cache_creation_input_tokens": 1046,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1046
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 3553,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.003648,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 2105,
      "outputTokens": 96106,
      "cacheReadInputTokens": 39910500,
      "cacheCreationInputTokens": 279681,
      "webSearchRequests": 0,
      "costUSD": 24.116431249999994,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "0dbd4f74-1fff-4f22-9798-e13a415c2152"
}
```

</details>

---
