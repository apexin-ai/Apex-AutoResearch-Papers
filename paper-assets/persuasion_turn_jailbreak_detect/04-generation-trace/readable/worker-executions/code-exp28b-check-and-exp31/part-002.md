# code exp28b check and exp31 — Part 2 of 2

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../code-exp28b-check-and-exp31.md) · [Structured JSON](../../../sessions/d1/d163fa7476193022eafe.json)

## Before a recorded user message

### Tool result

_source line 372 · 2026-05-20T19:28:46.899Z_

<details><summary>↩ Tool result · `toolu_01WwL81JE9W5AHzFyeMHCwEt`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp31_lambda_ablation_aa\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:29:23.924Z\", \"updated_at\": \"2026-05-20T19:28:46.306Z\", \"hypothesis\": \"Multi-task persuasion loss weight (lambda) affects OOD generalization in E2E fine-tuning: lambda=0 (intent-only) will underperform on hard OOD (ActorAttack) compared to lambda>0, because the persuasion auxiliary signal provides a regularization effect that preserves OOD-relevant features in the encoder. There exists an optimal lambda that maximizes AA OOD without sacrificing IID performance.\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/persuasion_turn_jailbreak_detect && python scripts/exp31_lambda_ablation.py\", \"server\": \"westd-33183\", \"data_path\": \"data/plan_002_splits/\", \"data_count\": 350, \"model_name\": \"microsoft/deberta-v3-base\", \"seed\": 42, \"checkpoint_source\": \"plan_002 DAPT seed42\", \"eval_data\": \"IID test + DD OOD + AA OOD + FITD OOD\", \"checkpoint_path\": \"checkpoints/exp31_lambda*_seed42/best.pt\", \"log_path\": \"/tmp/exp31.log\", \"lambdas\": [0, 0.1, 0.5, 1, 2], \"pid\": 84095}, \"metrics\": {\"lambda_0_aa\": 1, \"lambda_0.1_aa\": 0.9904, \"lambda_0.5_aa\": 0.9809, \"lambda_1.0_aa\": 0.9809, \"lambda_2.0_aa\": 0.9439, \"iid_all\": 1, \"dd_all\": 1, \"fitd_all\": 1, \"note\": \"Higher lambda monotonically hurts AA OOD. lambda=0 (intent-only E2E) achieves perfect AA. Persuasion aux loss acts as a distractor during E2E.\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-20T19:28:46.306Z\"}, \"hint\": \"💡 建议将本次教训写入 memory.md（什么不 work、为什么）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8427}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "15e5a860-373b-49ea-8377-25e0412b8f17",
  "uuid": "ee8a7084-2f9a-43e2-933a-dfdadbb7bb79",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"exp31_lambda_ablation_aa\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T15:29:23.924Z\\\", \\\"updated_at\\\": \\\"2026-05-20T19:28:46.306Z\\\", \\\"hypothesis\\\": \\\"Multi-task persuasion loss weight (lambda) affects OOD generalization in E2E fine-tuning: lambda=0 (intent-only) will underperform on hard OOD (ActorAttack) compared to lambda>0, because the persuasion auxiliary signal provides a regularization effect that preserves OOD-relevant features in the encoder. There exists an optimal lambda that maximizes AA OOD without sacrificing IID performance.\\\", \\\"spec\\\": {\\\"command\\\": \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/persuasion_turn_jailbreak_detect && python scripts/exp31_lambda_ablation.py\\\", \\\"server\\\": \\\"westd-33183\\\", \\\"data_path\\\": \\\"data/plan_002_splits/\\\", \\\"data_count\\\": 350, \\\"model_name\\\": \\\"microsoft/deberta-v3-base\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"plan_002 DAPT seed42\\\", \\\"eval_data\\\": \\\"IID test + DD OOD + AA OOD + FITD OOD\\\", \\\"checkpoint_path\\\": \\\"checkpoints/exp31_lambda*_seed42/best.pt\\\", \\\"log_path\\\": \\\"/tmp/exp31.log\\\", \\\"lambdas\\\": [0, 0.1, 0.5, 1, 2], \\\"pid\\\": 84095}, \\\"metrics\\\": {\\\"lambda_0_aa\\\": 1, \\\"lambda_0.1_aa\\\": 0.9904, \\\"lambda_0.5_aa\\\": 0.9809, \\\"lambda_1.0_aa\\\": 0.9809, \\\"lambda_2.0_aa\\\": 0.9439, \\\"iid_all\\\": 1, \\\"dd_all\\\": 1, \\\"fitd_all\\\": 1, \\\"note\\\": \\\"Higher lambda monotonically hurts AA OOD. lambda=0 (intent-only E2E) achieves perfect AA. Persuasion aux loss acts as a distractor during E2E.\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"completed_at\\\": \\\"2026-05-20T19:28:46.306Z\\\"}, \\\"hint\\\": \\\"💡 建议将本次教训写入 memory.md（什么不 work、为什么）\\\"}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.8427}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"exp31_lambda_ablation_aa\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:29:23.924Z\", \"updated_at\": \"2026-05-20T19:28:46.306Z\", \"hypothesis\": \"Multi-task persuasion loss weight (lambda) affects OOD generalization in E2E fine-tuning: lambda=0 (intent-only) will underperform on hard OOD (ActorAttack) compared to lambda>0, because the persuasion auxiliary signal provides a regularization effect that preserves OOD-relevant features in the encoder. There exists an optimal lambda that maximizes AA OOD without sacrificing IID performance.\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/persuasion_turn_jailbreak_detect && python scripts/exp31_lambda_ablation.py\", \"server\": \"westd-33183\", \"data_path\": \"data/plan_002_splits/\", \"data_count\": 350, \"model_name\": \"microsoft/deberta-v3-base\", \"seed\": 42, \"checkpoint_source\": \"plan_002 DAPT seed42\", \"eval_data\": \"IID test + DD OOD + AA OOD + FITD OOD\", \"checkpoint_path\": \"checkpoints/exp31_lambda*_seed42/best.pt\", \"log_path\": \"/tmp/exp31.log\", \"lambdas\": [0, 0.1, 0.5, 1, 2], \"pid\": 84095}, \"metrics\": {\"lambda_0_aa\": 1, \"lambda_0.1_aa\": 0.9904, \"lambda_0.5_aa\": 0.9809, \"lambda_1.0_aa\": 0.9809, \"lambda_2.0_aa\": 0.9439, \"iid_all\": 1, \"dd_all\": 1, \"fitd_all\": 1, \"note\": \"Higher lambda monotonically hurts AA OOD. lambda=0 (intent-only E2E) achieves perfect AA. Persuasion aux loss acts as a distractor during E2E.\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-20T19:28:46.306Z\"}, \"hint\": \"💡 建议将本次教训写入 memory.md（什么不 work、为什么）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8427}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 373_

Both tasks complete. Summary:

---

## Part A: exp28b Results

exp28b crashed during evaluation (float16 dtype in GRU), but all **9-class seed123 + seed456 runs completed**. Combined with exp28 seed42:

| N | IID | DD_OOD | AA_OOD |
|--:|:---:|:------:|:------:|
| 50 | 1.000±0.000 | 1.000±0.000 | 0.969±0.037 |
| 125 | 1.000±0.000 | 1.000±0.000 | 0.975±0.019 |
| 250 | 1.000±0.000 | 1.000±0.000 | 0.975±0.035 |
| 350 | 1.000±0.000 | 0.978±0.030 | 0.972±0.033 |

Vanilla (seed42 only): N=125 aa=0.244, N=350 aa=0.489. Vanilla N=50/250 missing (crash).

Registry: exp28b → **DONE (success)**.

## Part B: exp31 Lambda Ablation

| Lambda | IID | DD_OOD | **AA_OOD** | FITD_OOD |
|-------:|:---:|:------:|:----------:|:--------:|
| 0 | 1.0 | 1.0 | **1.0** | 1.0 |
| 0.1 | 1.0 | 1.0 | **0.990** | 1.0 |
| 0.5 | 1.0 | 1.0 | **0.981** | 1.0 |
| 1.0 | 1.0 | 1.0 | **0.981** | 1.0 |
| 2.0 | 1.0 | 1.0 | **0.944** | 1.0 |

**Hypothesis falsified (negative result)**: Higher lambda **monotonically hurts** AA OOD. lambda=0 (intent-only E2E, no persuasion aux loss) achieves perfect scores everywhere. The persuasion auxiliary loss acts as a distractor during E2E fine-tuning rather than a regularizer.

Registry: exp31 → **DONE (negative)**.

Output files:
- `results/exp28_combined_data_efficiency.json`
- `results/exp31_lambda_ablation.json`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "15e5a860-373b-49ea-8377-25e0412b8f17",
  "uuid": "04cee5c9-33e5-4ae2-95f6-304d74d7c294",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ACNutkKXiErjY99Fjrh8rc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 862,
      "cache_read_input_tokens": 132576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 862
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

_source line 374_

Both tasks complete. Summary:

---

## Part A: exp28b Results

exp28b crashed during evaluation (float16 dtype in GRU), but all **9-class seed123 + seed456 runs completed**. Combined with exp28 seed42:

| N | IID | DD_OOD | AA_OOD |
|--:|:---:|:------:|:------:|
| 50 | 1.000±0.000 | 1.000±0.000 | 0.969±0.037 |
| 125 | 1.000±0.000 | 1.000±0.000 | 0.975±0.019 |
| 250 | 1.000±0.000 | 1.000±0.000 | 0.975±0.035 |
| 350 | 1.000±0.000 | 0.978±0.030 | 0.972±0.033 |

Vanilla (seed42 only): N=125 aa=0.244, N=350 aa=0.489. Vanilla N=50/250 missing (crash).

Registry: exp28b → **DONE (success)**.

## Part B: exp31 Lambda Ablation

| Lambda | IID | DD_OOD | **AA_OOD** | FITD_OOD |
|-------:|:---:|:------:|:----------:|:--------:|
| 0 | 1.0 | 1.0 | **1.0** | 1.0 |
| 0.1 | 1.0 | 1.0 | **0.990** | 1.0 |
| 0.5 | 1.0 | 1.0 | **0.981** | 1.0 |
| 1.0 | 1.0 | 1.0 | **0.981** | 1.0 |
| 2.0 | 1.0 | 1.0 | **0.944** | 1.0 |

**Hypothesis falsified (negative result)**: Higher lambda **monotonically hurts** AA OOD. lambda=0 (intent-only E2E, no persuasion aux loss) achieves perfect scores everywhere. The persuasion auxiliary loss acts as a distractor during E2E fine-tuning rather than a regularizer.

Registry: exp31 → **DONE (negative)**.

Output files:
- `results/exp28_combined_data_efficiency.json`
- `results/exp31_lambda_ablation.json`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 1091244,
  "duration_api_ms": 889982,
  "num_turns": 141,
  "stop_reason": "end_turn",
  "session_id": "15e5a860-373b-49ea-8377-25e0412b8f17",
  "total_cost_usd": 7.362596750000003,
  "usage": {
    "input_tokens": 114,
    "cache_creation_input_tokens": 121991,
    "cache_read_input_tokens": 10730234,
    "output_tokens": 49274,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 121991,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 632,
        "cache_read_input_tokens": 132576,
        "cache_creation_input_tokens": 862,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 862
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2511,
      "outputTokens": 21,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0026160000000000003,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 114,
      "outputTokens": 49274,
      "cacheReadInputTokens": 10730234,
      "cacheCreationInputTokens": 121991,
      "webSearchRequests": 0,
      "costUSD": 7.359980750000003,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "549393f3-afcb-431f-9fec-b9c00701bb35"
}
```

</details>

---
