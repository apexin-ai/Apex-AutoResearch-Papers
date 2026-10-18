# diag full status harvest — Part 2 of 2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../diag-full-status-harvest.md) · [Structured JSON](../../../sessions/0c/0c3d6d5e8b95ae695c2b.json)

## Before a recorded user message

### Tool result

_source line 271 · 2026-05-23T18:01:06.536Z_

<details><summary>↩ Tool result · `toolu_015iQEvG111K2TeegDaGQBBg`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_e5_xvla_attn_rollout_goal_k05_v2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T16:50:04.341Z\", \"updated_at\": \"2026-05-23T18:01:04.224Z\", \"spec\": {\"command\": \"eval_xvla_attention_pruning_libero.py --mode attention_rollout --keep_ratio 0.5 --suite libero_goal --seed 42\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:2\"], \"pid\": \"743734\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_e5_xvla_attn_rollout_goal_k05_v2.log\", \"submitted_at\": \"2026-05-23T16:50:03.180Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_goal\", \"data_count\": 500, \"model_name\": \"X-VLA-Libero\", \"seed\": 42, \"wall_clock_seconds\": 4261.0, \"gpu_hours\": 1.18}, \"hypothesis\": \"E5 X-VLA attention_rollout pruning k=0.5 Goal v2 重跑。Rollout综合多层attention信息，在50%极端剪枝下Goal表现。与last/mean/random对比评估attention rollout的有效性。\", \"metrics\": {\"success_rate\": 96.8, \"total_successes\": 484, \"total_episodes\": 500, \"wilson_ci_95\": [94.9, 98], \"elapsed_min\": 31.1}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-23T18:01:04.224Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.4615}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ec827b49-7dff-426d-9a93-6f528ca7a9b6",
  "uuid": "b36a6722-23d3-43be-86d5-cf07cbabf6b5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval_e5_xvla_attn_rollout_goal_k05_v2\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T16:50:04.341Z\\\", \\\"updated_at\\\": \\\"2026-05-23T18:01:04.224Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"eval_xvla_attention_pruning_libero.py --mode attention_rollout --keep_ratio 0.5 --suite libero_goal --seed 42\\\", \\\"server\\\": \\\"westd-38929\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"743734\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_e5_xvla_attn_rollout_goal_k05_v2.log\\\", \\\"submitted_at\\\": \\\"2026-05-23T16:50:03.180Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"libero_goal\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"X-VLA-Libero\\\", \\\"seed\\\": 42, \\\"wall_clock_seconds\\\": 4261.0, \\\"gpu_hours\\\": 1.18}, \\\"hypothesis\\\": \\\"E5 X-VLA attention_rollout pruning k=0.5 Goal v2 重跑。Rollout综合多层attention信息，在50%极端剪枝下Goal表现。与last/mean/random对比评估attention rollout的有效性。\\\", \\\"metrics\\\": {\\\"success_rate\\\": 96.8, \\\"total_successes\\\": 484, \\\"total_episodes\\\": 500, \\\"wilson_ci_95\\\": [94.9, 98], \\\"elapsed_min\\\": 31.1}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"completed_at\\\": \\\"2026-05-23T18:01:04.224Z\\\"}, \\\"hint\\\": \\\"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\\\"}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 3.4615}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval_e5_xvla_attn_rollout_goal_k05_v2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T16:50:04.341Z\", \"updated_at\": \"2026-05-23T18:01:04.224Z\", \"spec\": {\"command\": \"eval_xvla_attention_pruning_libero.py --mode attention_rollout --keep_ratio 0.5 --suite libero_goal --seed 42\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:2\"], \"pid\": \"743734\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_e5_xvla_attn_rollout_goal_k05_v2.log\", \"submitted_at\": \"2026-05-23T16:50:03.180Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_goal\", \"data_count\": 500, \"model_name\": \"X-VLA-Libero\", \"seed\": 42, \"wall_clock_seconds\": 4261.0, \"gpu_hours\": 1.18}, \"hypothesis\": \"E5 X-VLA attention_rollout pruning k=0.5 Goal v2 重跑。Rollout综合多层attention信息，在50%极端剪枝下Goal表现。与last/mean/random对比评估attention rollout的有效性。\", \"metrics\": {\"success_rate\": 96.8, \"total_successes\": 484, \"total_episodes\": 500, \"wilson_ci_95\": [94.9, 98], \"elapsed_min\": 31.1}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-23T18:01:04.224Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.4615}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 272 · 2026-05-23T18:01:10.043Z_

<details><summary>↩ Tool result · `toolu_01MdKhrqYZoqSC4d1v5vaTgK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_e5_xvla_random_goal_k05_v2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T17:58:52.568Z\", \"updated_at\": \"2026-05-23T18:01:07.760Z\", \"hypothesis\": \"E5 X-VLA random pruning k=0.5 Goal v2 重跑。Random baseline在50%剪枝下Goal套件表现，作为importance-based方法(attn_last/mean/rollout)的对照基准。\", \"metrics\": {\"success_rate\": 67.2, \"total_successes\": 336, \"total_episodes\": 500, \"wilson_ci_95\": [63, 71.2], \"elapsed_min\": 58.2}, \"conclusion\": \"negative\", \"checkpoint_path\": \"N/A (eval only)\", \"spec\": {\"command\": \"eval_xvla_attention_pruning_libero.py --mode random --keep_ratio 0.5 --suite libero_goal --seed 42\", \"server\": \"westd-38929\", \"data_path\": \"libero_goal\", \"data_count\": 500, \"model_name\": \"X-VLA-Libero\", \"seed\": 42, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_xvla_random_k05_goal_seed42_v2.log\", \"account\": \"root\"}, \"completed_at\": \"2026-05-23T18:01:07.760Z\"}, \"hint\": \"💡 建议将本次教训写入 memory.md（什么不 work、为什么）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.49}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ec827b49-7dff-426d-9a93-6f528ca7a9b6",
  "uuid": "21f25ea5-92e3-43f5-87ea-87e90c03aae5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval_e5_xvla_random_goal_k05_v2\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T17:58:52.568Z\\\", \\\"updated_at\\\": \\\"2026-05-23T18:01:07.760Z\\\", \\\"hypothesis\\\": \\\"E5 X-VLA random pruning k=0.5 Goal v2 重跑。Random baseline在50%剪枝下Goal套件表现，作为importance-based方法(attn_last/mean/rollout)的对照基准。\\\", \\\"metrics\\\": {\\\"success_rate\\\": 67.2, \\\"total_successes\\\": 336, \\\"total_episodes\\\": 500, \\\"wilson_ci_95\\\": [63, 71.2], \\\"elapsed_min\\\": 58.2}, \\\"conclusion\\\": \\\"negative\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"spec\\\": {\\\"command\\\": \\\"eval_xvla_attention_pruning_libero.py --mode random --keep_ratio 0.5 --suite libero_goal --seed 42\\\", \\\"server\\\": \\\"westd-38929\\\", \\\"data_path\\\": \\\"libero_goal\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"X-VLA-Libero\\\", \\\"seed\\\": 42, \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_xvla_random_k05_goal_seed42_v2.log\\\", \\\"account\\\": \\\"root\\\"}, \\\"completed_at\\\": \\\"2026-05-23T18:01:07.760Z\\\"}, \\\"hint\\\": \\\"💡 建议将本次教训写入 memory.md（什么不 work、为什么）\\\"}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 3.49}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval_e5_xvla_random_goal_k05_v2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T17:58:52.568Z\", \"updated_at\": \"2026-05-23T18:01:07.760Z\", \"hypothesis\": \"E5 X-VLA random pruning k=0.5 Goal v2 重跑。Random baseline在50%剪枝下Goal套件表现，作为importance-based方法(attn_last/mean/rollout)的对照基准。\", \"metrics\": {\"success_rate\": 67.2, \"total_successes\": 336, \"total_episodes\": 500, \"wilson_ci_95\": [63, 71.2], \"elapsed_min\": 58.2}, \"conclusion\": \"negative\", \"checkpoint_path\": \"N/A (eval only)\", \"spec\": {\"command\": \"eval_xvla_attention_pruning_libero.py --mode random --keep_ratio 0.5 --suite libero_goal --seed 42\", \"server\": \"westd-38929\", \"data_path\": \"libero_goal\", \"data_count\": 500, \"model_name\": \"X-VLA-Libero\", \"seed\": 42, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_xvla_random_k05_goal_seed42_v2.log\", \"account\": \"root\"}, \"completed_at\": \"2026-05-23T18:01:07.760Z\"}, \"hint\": \"💡 建议将本次教训写入 memory.md（什么不 work、为什么）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.49}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 273_

全部 8 个实验已标 DONE。完整状态表：

## 服务器状态总览

| Server | GPU | Experiment | Status | SR |
|--------|-----|-----------|--------|-----|
| **westd-38929** | 0-3: 0%, idle | E5 attn_last k=0.5 Goal v2 | **DONE** | **98.2%** |
| | | E5 attn_mean k=0.5 Goal v2 | **DONE** | **97.4%** |
| | | E5 attn_rollout k=0.5 Goal v2 | **DONE** | **96.8%** |
| | | E5 random k=0.5 Goal v2 | **DONE** | **67.2%** |
| **westd-27271** | 0: 68%, 16GB | OpenVLA Goal baseline v3 | Running | Task 10/10 (~soon) |
| | 1: 78%, 16GB | OpenVLA Long baseline | Running | Task 3/10 (ep 40/50) |
| **westd-41074** | 0: 39% | π0.5 l2norm k=0.925 Goal v2 | Running | T8/10, ~94.5% avg |
| | 1: 31% | π0.5 l2norm k=0.85 Spatial v2 | Running | T6-7/10 |
| | 2: 11% | π0.5 random k=0.925 Goal v2 | Running | T5-6/10 |
| | 3: ~0% | π0.5 random k=0.85 Spatial v2 | Running | T4-5/10 |
| **cqa1-33015** | 0-2: idle | π0.5 l2norm k=0.95 Goal v2 | **DONE** | **89.4%** |
| | | π0.5 l2norm k=0.90 Goal v2 | **DONE** | **90.6%** |
| | | π0.5 l2norm k=0.70 Goal v2 | **DONE** | **73.6%** |
| | 3: 11% | π0.5 l2norm k=0.30 Goal v2 | Running | T9/10 (ep 20/50) |

## Registry harvest 完成

| Experiment | conclusion | SR |
|-----------|-----------|-----|
| eval_e5_xvla_attn_last_goal_k05_v2 | success | 98.2% |
| eval_e5_xvla_attn_mean_goal_k05_v2 | success | 97.4% |
| eval_e5_xvla_attn_rollout_goal_k05_v2 | success | 96.8% |
| eval_e5_xvla_random_goal_k05_v2 | negative | 67.2% |
| eval_pi05_random_k095_goal_seed42_v2 | success | 83.8% |
| eval_pi05_random_k09_goal_seed42_v2 | negative | 62.2% |
| eval_pi05_random_k07_goal_seed42_v2 | negative | 78.2% |
| eval_pi05_random_k03_goal_seed42_v2 | negative | 50.6% |

## 关键发现

**E5 Goal k=0.5 v2 — 论文叙事核心数据**：attention-based pruning 在 50% 极端剪枝下 Goal 套件依然保持 96.8-98.2% SR，而 random 只有 67.2%。**Importance margin = +29-31pp**，比 Object/Spatial 套件的 margin 更大，强化了论文叙事。

**westd-38929 已空闲**，可部署新实验。westd-41074 和 cqa1-33015 的实验预计 1-2 小时内全部完成。westd-27271 的 OpenVLA Goal baseline 即将完成（Task 10/10），Long 还需数小时。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ec827b49-7dff-426d-9a93-6f528ca7a9b6",
  "uuid": "808ebadd-638a-44a9-b30c-4c8e5dc556ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UgyxvousJeV8b9VPYvUXcJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3037,
      "cache_read_input_tokens": 100399,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3037
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

_source line 274_

全部 8 个实验已标 DONE。完整状态表：

## 服务器状态总览

| Server | GPU | Experiment | Status | SR |
|--------|-----|-----------|--------|-----|
| **westd-38929** | 0-3: 0%, idle | E5 attn_last k=0.5 Goal v2 | **DONE** | **98.2%** |
| | | E5 attn_mean k=0.5 Goal v2 | **DONE** | **97.4%** |
| | | E5 attn_rollout k=0.5 Goal v2 | **DONE** | **96.8%** |
| | | E5 random k=0.5 Goal v2 | **DONE** | **67.2%** |
| **westd-27271** | 0: 68%, 16GB | OpenVLA Goal baseline v3 | Running | Task 10/10 (~soon) |
| | 1: 78%, 16GB | OpenVLA Long baseline | Running | Task 3/10 (ep 40/50) |
| **westd-41074** | 0: 39% | π0.5 l2norm k=0.925 Goal v2 | Running | T8/10, ~94.5% avg |
| | 1: 31% | π0.5 l2norm k=0.85 Spatial v2 | Running | T6-7/10 |
| | 2: 11% | π0.5 random k=0.925 Goal v2 | Running | T5-6/10 |
| | 3: ~0% | π0.5 random k=0.85 Spatial v2 | Running | T4-5/10 |
| **cqa1-33015** | 0-2: idle | π0.5 l2norm k=0.95 Goal v2 | **DONE** | **89.4%** |
| | | π0.5 l2norm k=0.90 Goal v2 | **DONE** | **90.6%** |
| | | π0.5 l2norm k=0.70 Goal v2 | **DONE** | **73.6%** |
| | 3: 11% | π0.5 l2norm k=0.30 Goal v2 | Running | T9/10 (ep 20/50) |

## Registry harvest 完成

| Experiment | conclusion | SR |
|-----------|-----------|-----|
| eval_e5_xvla_attn_last_goal_k05_v2 | success | 98.2% |
| eval_e5_xvla_attn_mean_goal_k05_v2 | success | 97.4% |
| eval_e5_xvla_attn_rollout_goal_k05_v2 | success | 96.8% |
| eval_e5_xvla_random_goal_k05_v2 | negative | 67.2% |
| eval_pi05_random_k095_goal_seed42_v2 | success | 83.8% |
| eval_pi05_random_k09_goal_seed42_v2 | negative | 62.2% |
| eval_pi05_random_k07_goal_seed42_v2 | negative | 78.2% |
| eval_pi05_random_k03_goal_seed42_v2 | negative | 50.6% |

## 关键发现

**E5 Goal k=0.5 v2 — 论文叙事核心数据**：attention-based pruning 在 50% 极端剪枝下 Goal 套件依然保持 96.8-98.2% SR，而 random 只有 67.2%。**Importance margin = +29-31pp**，比 Object/Spatial 套件的 margin 更大，强化了论文叙事。

**westd-38929 已空闲**，可部署新实验。westd-41074 和 cqa1-33015 的实验预计 1-2 小时内全部完成。westd-27271 的 OpenVLA Goal baseline 即将完成（Task 10/10），Long 还需数小时。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 567937,
  "duration_api_ms": 487709,
  "num_turns": 120,
  "stop_reason": "end_turn",
  "session_id": "ec827b49-7dff-426d-9a93-6f528ca7a9b6",
  "total_cost_usd": 2.31398375,
  "usage": {
    "input_tokens": 35,
    "cache_creation_input_tokens": 114037,
    "cache_read_input_tokens": 1809207,
    "output_tokens": 27785,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 114037,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1091,
        "cache_read_input_tokens": 100399,
        "cache_creation_input_tokens": 3037,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3037
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1779,
      "outputTokens": 14,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001849,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 35,
      "outputTokens": 27785,
      "cacheReadInputTokens": 1809207,
      "cacheCreationInputTokens": 114037,
      "webSearchRequests": 0,
      "costUSD": 2.31213475,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "5bc77803-d7cf-42c2-ab49-0ff90d50612f"
}
```

</details>

---
