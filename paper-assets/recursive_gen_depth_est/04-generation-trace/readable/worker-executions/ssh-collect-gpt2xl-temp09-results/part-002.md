# ssh collect gpt2xl temp09 results — Part 2 of 2

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../ssh-collect-gpt2xl-temp09-results.md) · [Structured JSON](../../../sessions/66/66502c251e02e6ec5e4c.json)

## Before a recorded user message

### Tool result

_source line 517 · 2026-05-14T22:43:06.782Z_

<details><summary>↩ Tool result · `toolu_01KuyPiFgdDPijvaWkb6Jwk7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"gpt2xl_temp09_001\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:28:04.139Z\", \"updated_at\": \"2026-05-14T22:43:06.720Z\", \"hypothesis\": \"解码策略鲁棒性: GPT-2 XL 在 temperature-only τ=0.9 下递归生成的深度信号与 nucleus p=0.95 一致，支持跨策略泛化\", \"parent\": \"cross_model_gpt2xl_001\", \"spec\": {\"command\": \"bash scripts/run_pipeline_gpt2xl_temp09.sh (GPT-2 XL, 3x LoRA finetune + 3x generate, temp_only τ=0.9)\", \"server\": \"gpu-6000pro-2\", \"gpu\": \"cuda:1\", \"pid\": 168793, \"log_path\": \"/root/autodl-tmp/recursive_gen_depth_est/logs/pipeline_gpt2xl_temp09.log\", \"submitted_at\": \"2026-05-14T18:28:10Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl_temp09/depth_0.jsonl\", \"data_count\": 5000, \"model_name\": \"openai-community/gpt2-xl\", \"model_path\": \"/root/autodl-tmp/models/gpt2-xl/\", \"seed\": 42, \"hyperparams\": {\"lora_r\": 16, \"lora_alpha\": 32, \"target_modules\": [\"c_attn\", \"c_proj\"], \"epochs\": 3, \"lr\": \"2e-4\", \"batch_size\": 8, \"gradient_accumulation\": 2, \"max_seq_len\": 512, \"max_new_tokens\": 512, \"temperature\": 0.9, \"decoding_strategy\": \"temp_only\"}, \"checkpoint_path\": \"/root/autodl-tmp/recursive_gen_depth_est/checkpoints/gpt2xl_temp09/\", \"checkpoint_source\": \"n/a (full pipeline re-run with different decoding strategy)\", \"eval_data\": \"n/a (training pipeline, not eval)\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T22:19:54.987Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T22:19:56.275209+00:00\"}]}, \"metrics\": {\"data\": {\"samples_per_depth\": 5000, \"total_samples\": 20000, \"depths\": 4}, \"finetune_losses\": {\"depth_1\": 2.5498, \"depth_2\": 1.6972, \"depth_3\": 1.2922}, \"code_contamination\": {\"depth_0\": {\"broad\": 25, \"narrow\": 20, \"broad_pct\": 0.5, \"narrow_pct\": 0.4}, \"depth_1\": {\"broad\": 25, \"narrow\": 40, \"broad_pct\": 0.5, \"narrow_pct\": 0.8}, \"depth_2\": {\"broad\": 34, \"narrow\": 80, \"broad_pct\": 0.7, \"narrow_pct\": 1.6}, \"depth_3\": {\"broad\": 25, \"narrow\": 76, \"broad_pct\": 0.5, \"narrow_pct\": 1.5}}, \"four_class\": {\"rf_accuracy\": 0.8542, \"rf_accuracy_ci\": [0.843, 0.8653], \"lr_accuracy\": 0.8155, \"lr_accuracy_ci\": [0.8025, 0.8273], \"rf_auc\": {\"d0v1\": 0.9963, \"d0v2\": 0.9992, \"d0v3\": 1, \"d1v2\": 0.9367, \"d1v3\": 0.9947, \"d2v3\": 0.8815}, \"lr_auc\": {\"d0v1\": 0.984, \"d0v2\": 0.9998, \"d0v3\": 1, \"d1v2\": 0.8903, \"d1v3\": 0.9824, \"d2v3\": 0.8183}, \"top_features\": [\"p90_ppl\", \"mean_surprisal\", \"p75_ppl\", \"var_surprisal\"]}, \"three_class\": {\"rf_accuracy\": 0.82, \"rf_accuracy_ci\": [0.806, 0.834], \"lr_accuracy\": 0.7773, \"lr_accuracy_ci\": [0.7627, 0.792], \"rf_auc\": {\"d1v2\": 0.9418, \"d1v3\": 0.9967, \"d2v3\": 0.8849}}, \"three_class_filtered\": {\"rf_accuracy\": 0.815, \"rf_accuracy_ci\": [0.7999, 0.8298], \"lr_accuracy\": 0.7869, \"lr_accuracy_ci\": [0.7711, 0.8016], \"rf_auc\": {\"d1v2\": 0.937, \"d1v3\": 0.9944, \"d2v3\": 0.8891}}}, \"conclusion\": \"success\", \"notes\": \"GPT-2 XL temp09 意外优于 nucleus baseline: 4-class RF 85.42% vs 83.3% (+2.1pp), 3-class 82.0% vs 79.3% (+2.7pp)。与 Pythia 方向相反（Pythia temp09 降 1.9pp）。解码策略对深度信号的影响是模型依赖的。d2v3 AUC 基本持平（0.8815 vs 0.883），d1v2 AUC 提升（0.9367 vs 0.913）。filtered 3-class 81.5% 与 unfiltered 82.0% 接近，code contamination 影响小。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1685}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1743bf1f-7501-4415-8a90-6c3403605b32",
  "uuid": "1bcda5e6-f944-43ff-a4bd-5a0d0a617204",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"gpt2xl_temp09_001\\\", \\\"experiment\\\": {\\\"status\\\": \\\"ANALYZING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T18:28:04.139Z\\\", \\\"updated_at\\\": \\\"2026-05-14T22:43:06.720Z\\\", \\\"hypothesis\\\": \\\"解码策略鲁棒性: GPT-2 XL 在 temperature-only τ=0.9 下递归生成的深度信号与 nucleus p=0.95 一致，支持跨策略泛化\\\", \\\"parent\\\": \\\"cross_model_gpt2xl_001\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash scripts/run_pipeline_gpt2xl_temp09.sh (GPT-2 XL, 3x LoRA finetune + 3x generate, temp_only τ=0.9)\\\", \\\"server\\\": \\\"gpu-6000pro-2\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 168793, \\\"log_path\\\": \\\"/root/autodl-tmp/recursive_gen_depth_est/logs/pipeline_gpt2xl_temp09.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T18:28:10Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl_temp09/depth_0.jsonl\\\", \\\"data_count\\\": 5000, \\\"model_name\\\": \\\"openai-community/gpt2-xl\\\", \\\"model_path\\\": \\\"/root/autodl-tmp/models/gpt2-xl/\\\", \\\"seed\\\": 42, \\\"hyperparams\\\": {\\\"lora_r\\\": 16, \\\"lora_alpha\\\": 32, \\\"target_modules\\\": [\\\"c_attn\\\", \\\"c_proj\\\"], \\\"epochs\\\": 3, \\\"lr\\\": \\\"2e-4\\\", \\\"batch_size\\\": 8, \\\"gradient_accumulation\\\": 2, \\\"max_seq_len\\\": 512, \\\"max_new_tokens\\\": 512, \\\"temperature\\\": 0.9, \\\"decoding_strategy\\\": \\\"temp_only\\\"}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/recursive_gen_depth_est/checkpoints/gpt2xl_temp09/\\\", \\\"checkpoint_source\\\": \\\"n/a (full pipeline re-run with different decoding strategy)\\\", \\\"eval_data\\\": \\\"n/a (training pipeline, not eval)\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-14T22:19:54.987Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-14T22:19:56.275209+00:00\\\"}]}, \\\"metrics\\\": {\\\"data\\\": {\\\"samples_per_depth\\\": 5000, \\\"total_samples\\\": 20000, \\\"depths\\\": 4}, \\\"finetune_losses\\\": {\\\"depth_1\\\": 2.5498, \\\"depth_2\\\": 1.6972, \\\"depth_3\\\": 1.2922}, \\\"code_contamination\\\": {\\\"depth_0\\\": {\\\"broad\\\": 25, \\\"narrow\\\": 20, \\\"broad_pct\\\": 0.5, \\\"narrow_pct\\\": 0.4}, \\\"depth_1\\\": {\\\"broad\\\": 25, \\\"narrow\\\": 40, \\\"broad_pct\\\": 0.5, \\\"narrow_pct\\\": 0.8}, \\\"depth_2\\\": {\\\"broad\\\": 34, \\\"narrow\\\": 80, \\\"broad_pct\\\": 0.7, \\\"narrow_pct\\\": 1.6}, \\\"depth_3\\\": {\\\"broad\\\": 25, \\\"narrow\\\": 76, \\\"broad_pct\\\": 0.5, \\\"narrow_pct\\\": 1.5}}, \\\"four_class\\\": {\\\"rf_accuracy\\\": 0.8542, \\\"rf_accuracy_ci\\\": [0.843, 0.8653], \\\"lr_accuracy\\\": 0.8155, \\\"lr_accuracy_ci\\\": [0.8025, 0.8273], \\\"rf_auc\\\": {\\\"d0v1\\\": 0.9963, \\\"d0v2\\\": 0.9992, \\\"d0v3\\\": 1, \\\"d1v2\\\": 0.9367, \\\"d1v3\\\": 0.9947, \\\"d2v3\\\": 0.8815}, \\\"lr_auc\\\": {\\\"d0v1\\\": 0.984, \\\"d0v2\\\": 0.9998, \\\"d0v3\\\": 1, \\\"d1v2\\\": 0.8903, \\\"d1v3\\\": 0.9824, \\\"d2v3\\\": 0.8183}, \\\"top_features\\\": [\\\"p90_ppl\\\", \\\"mean_surprisal\\\", \\\"p75_ppl\\\", \\\"var_surprisal\\\"]}, \\\"three_class\\\": {\\\"rf_accuracy\\\": 0.82, \\\"rf_accuracy_ci\\\": [0.806, 0.834], \\\"lr_accuracy\\\": 0.7773, \\\"lr_accuracy_ci\\\": [0.7627, 0.792], \\\"rf_auc\\\": {\\\"d1v2\\\": 0.9418, \\\"d1v3\\\": 0.9967, \\\"d2v3\\\": 0.8849}}, \\\"three_class_filtered\\\": {\\\"rf_accuracy\\\": 0.815, \\\"rf_accuracy_ci\\\": [0.7999, 0.8298], \\\"lr_accuracy\\\": 0.7869, \\\"lr_accuracy_ci\\\": [0.7711, 0.8016], \\\"rf_auc\\\": {\\\"d1v2\\\": 0.937, \\\"d1v3\\\": 0.9944, \\\"d2v3\\\": 0.8891}}}, \\\"conclusion\\\": \\\"success\\\", \\\"notes\\\": \\\"GPT-2 XL temp09 意外优于 nucleus baseline: 4-class RF 85.42% vs 83.3% (+2.1pp), 3-class 82.0% vs 79.3% (+2.7pp)。与 Pythia 方向相反（Pythia temp09 降 1.9pp）。解码策略对深度信号的影响是模型依赖的。d2v3 AUC 基本持平（0.8815 vs 0.883），d1v2 AUC 提升（0.9367 vs 0.913）。filtered 3-class 81.5% 与 unfiltered 82.0% 接近，code contamination 影响小。\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.1685}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"gpt2xl_temp09_001\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:28:04.139Z\", \"updated_at\": \"2026-05-14T22:43:06.720Z\", \"hypothesis\": \"解码策略鲁棒性: GPT-2 XL 在 temperature-only τ=0.9 下递归生成的深度信号与 nucleus p=0.95 一致，支持跨策略泛化\", \"parent\": \"cross_model_gpt2xl_001\", \"spec\": {\"command\": \"bash scripts/run_pipeline_gpt2xl_temp09.sh (GPT-2 XL, 3x LoRA finetune + 3x generate, temp_only τ=0.9)\", \"server\": \"gpu-6000pro-2\", \"gpu\": \"cuda:1\", \"pid\": 168793, \"log_path\": \"/root/autodl-tmp/recursive_gen_depth_est/logs/pipeline_gpt2xl_temp09.log\", \"submitted_at\": \"2026-05-14T18:28:10Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl_temp09/depth_0.jsonl\", \"data_count\": 5000, \"model_name\": \"openai-community/gpt2-xl\", \"model_path\": \"/root/autodl-tmp/models/gpt2-xl/\", \"seed\": 42, \"hyperparams\": {\"lora_r\": 16, \"lora_alpha\": 32, \"target_modules\": [\"c_attn\", \"c_proj\"], \"epochs\": 3, \"lr\": \"2e-4\", \"batch_size\": 8, \"gradient_accumulation\": 2, \"max_seq_len\": 512, \"max_new_tokens\": 512, \"temperature\": 0.9, \"decoding_strategy\": \"temp_only\"}, \"checkpoint_path\": \"/root/autodl-tmp/recursive_gen_depth_est/checkpoints/gpt2xl_temp09/\", \"checkpoint_source\": \"n/a (full pipeline re-run with different decoding strategy)\", \"eval_data\": \"n/a (training pipeline, not eval)\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T22:19:54.987Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T22:19:56.275209+00:00\"}]}, \"metrics\": {\"data\": {\"samples_per_depth\": 5000, \"total_samples\": 20000, \"depths\": 4}, \"finetune_losses\": {\"depth_1\": 2.5498, \"depth_2\": 1.6972, \"depth_3\": 1.2922}, \"code_contamination\": {\"depth_0\": {\"broad\": 25, \"narrow\": 20, \"broad_pct\": 0.5, \"narrow_pct\": 0.4}, \"depth_1\": {\"broad\": 25, \"narrow\": 40, \"broad_pct\": 0.5, \"narrow_pct\": 0.8}, \"depth_2\": {\"broad\": 34, \"narrow\": 80, \"broad_pct\": 0.7, \"narrow_pct\": 1.6}, \"depth_3\": {\"broad\": 25, \"narrow\": 76, \"broad_pct\": 0.5, \"narrow_pct\": 1.5}}, \"four_class\": {\"rf_accuracy\": 0.8542, \"rf_accuracy_ci\": [0.843, 0.8653], \"lr_accuracy\": 0.8155, \"lr_accuracy_ci\": [0.8025, 0.8273], \"rf_auc\": {\"d0v1\": 0.9963, \"d0v2\": 0.9992, \"d0v3\": 1, \"d1v2\": 0.9367, \"d1v3\": 0.9947, \"d2v3\": 0.8815}, \"lr_auc\": {\"d0v1\": 0.984, \"d0v2\": 0.9998, \"d0v3\": 1, \"d1v2\": 0.8903, \"d1v3\": 0.9824, \"d2v3\": 0.8183}, \"top_features\": [\"p90_ppl\", \"mean_surprisal\", \"p75_ppl\", \"var_surprisal\"]}, \"three_class\": {\"rf_accuracy\": 0.82, \"rf_accuracy_ci\": [0.806, 0.834], \"lr_accuracy\": 0.7773, \"lr_accuracy_ci\": [0.7627, 0.792], \"rf_auc\": {\"d1v2\": 0.9418, \"d1v3\": 0.9967, \"d2v3\": 0.8849}}, \"three_class_filtered\": {\"rf_accuracy\": 0.815, \"rf_accuracy_ci\": [0.7999, 0.8298], \"lr_accuracy\": 0.7869, \"lr_accuracy_ci\": [0.7711, 0.8016], \"rf_auc\": {\"d1v2\": 0.937, \"d1v3\": 0.9944, \"d2v3\": 0.8891}}}, \"conclusion\": \"success\", \"notes\": \"GPT-2 XL temp09 意外优于 nucleus baseline: 4-class RF 85.42% vs 83.3% (+2.1pp), 3-class 82.0% vs 79.3% (+2.7pp)。与 Pythia 方向相反（Pythia temp09 降 1.9pp）。解码策略对深度信号的影响是模型依赖的。d2v3 AUC 基本持平（0.8815 vs 0.883），d1v2 AUC 提升（0.9367 vs 0.913）。filtered 3-class 81.5% 与 unfiltered 82.0% 接近，code contamination 影响小。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1685}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 518_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_013WZDC6ZxNz4VVuJfeKyFmV`</summary>

```json
{
  "exp_id": "gpt2xl_temp09_001",
  "field": "status",
  "value": "DONE",
  "project": "recursive_gen_depth_est",
  "spec": {
    "log_path": "/root/autodl-tmp/recursive_gen_depth_est/logs/eval_gpt2xl_temp09.log",
    "checkpoint_path": "/root/autodl-tmp/recursive_gen_depth_est/checkpoints/gpt2xl_temp09/",
    "results_dir": "/root/autodl-tmp/recursive_gen_depth_est/results/gpt2xl_temp09/",
    "eval_finished_at": "2026-05-15T06:42:16+08:00"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1743bf1f-7501-4415-8a90-6c3403605b32",
  "uuid": "d2052dbc-1dd5-4879-ba20-d5729dd25b7c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TatVb7PSgXDyxP4nhXVjzv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3874,
      "cache_read_input_tokens": 108640,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3874
      },
      "output_tokens": 67,
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

_source line 519 · 2026-05-14T22:43:12.215Z_

<details><summary>↩ Tool result · `toolu_013WZDC6ZxNz4VVuJfeKyFmV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"gpt2xl_temp09_001\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:28:04.139Z\", \"updated_at\": \"2026-05-14T22:43:11.919Z\", \"hypothesis\": \"解码策略鲁棒性: GPT-2 XL 在 temperature-only τ=0.9 下递归生成的深度信号与 nucleus p=0.95 一致，支持跨策略泛化\", \"parent\": \"cross_model_gpt2xl_001\", \"spec\": {\"command\": \"bash scripts/run_pipeline_gpt2xl_temp09.sh (GPT-2 XL, 3x LoRA finetune + 3x generate, temp_only τ=0.9)\", \"server\": \"gpu-6000pro-2\", \"gpu\": \"cuda:1\", \"pid\": 168793, \"log_path\": \"/root/autodl-tmp/recursive_gen_depth_est/logs/eval_gpt2xl_temp09.log\", \"submitted_at\": \"2026-05-14T18:28:10Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl_temp09/depth_0.jsonl\", \"data_count\": 5000, \"model_name\": \"openai-community/gpt2-xl\", \"model_path\": \"/root/autodl-tmp/models/gpt2-xl/\", \"seed\": 42, \"hyperparams\": {\"lora_r\": 16, \"lora_alpha\": 32, \"target_modules\": [\"c_attn\", \"c_proj\"], \"epochs\": 3, \"lr\": \"2e-4\", \"batch_size\": 8, \"gradient_accumulation\": 2, \"max_seq_len\": 512, \"max_new_tokens\": 512, \"temperature\": 0.9, \"decoding_strategy\": \"temp_only\"}, \"checkpoint_path\": \"/root/autodl-tmp/recursive_gen_depth_est/checkpoints/gpt2xl_temp09/\", \"checkpoint_source\": \"n/a (full pipeline re-run with different decoding strategy)\", \"eval_data\": \"n/a (training pipeline, not eval)\", \"results_dir\": \"/root/autodl-tmp/recursive_gen_depth_est/results/gpt2xl_temp09/\", \"eval_finished_at\": \"2026-05-15T06:42:16+08:00\", \"wall_clock_seconds\": 15301.9, \"gpu_hours\": 4.25}, \"reproduce\": {\"finished_at\": \"2026-05-14T22:19:54.987Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T22:19:56.275209+00:00\"}]}, \"metrics\": {\"data\": {\"samples_per_depth\": 5000, \"total_samples\": 20000, \"depths\": 4}, \"finetune_losses\": {\"depth_1\": 2.5498, \"depth_2\": 1.6972, \"depth_3\": 1.2922}, \"code_contamination\": {\"depth_0\": {\"broad\": 25, \"narrow\": 20, \"broad_pct\": 0.5, \"narrow_pct\": 0.4}, \"depth_1\": {\"broad\": 25, \"narrow\": 40, \"broad_pct\": 0.5, \"narrow_pct\": 0.8}, \"depth_2\": {\"broad\": 34, \"narrow\": 80, \"broad_pct\": 0.7, \"narrow_pct\": 1.6}, \"depth_3\": {\"broad\": 25, \"narrow\": 76, \"broad_pct\": 0.5, \"narrow_pct\": 1.5}}, \"four_class\": {\"rf_accuracy\": 0.8542, \"rf_accuracy_ci\": [0.843, 0.8653], \"lr_accuracy\": 0.8155, \"lr_accuracy_ci\": [0.8025, 0.8273], \"rf_auc\": {\"d0v1\": 0.9963, \"d0v2\": 0.9992, \"d0v3\": 1, \"d1v2\": 0.9367, \"d1v3\": 0.9947, \"d2v3\": 0.8815}, \"lr_auc\": {\"d0v1\": 0.984, \"d0v2\": 0.9998, \"d0v3\": 1, \"d1v2\": 0.8903, \"d1v3\": 0.9824, \"d2v3\": 0.8183}, \"top_features\": [\"p90_ppl\", \"mean_surprisal\", \"p75_ppl\", \"var_surprisal\"]}, \"three_class\": {\"rf_accuracy\": 0.82, \"rf_accuracy_ci\": [0.806, 0.834], \"lr_accuracy\": 0.7773, \"lr_accuracy_ci\": [0.7627, 0.792], \"rf_auc\": {\"d1v2\": 0.9418, \"d1v3\": 0.9967, \"d2v3\": 0.8849}}, \"three_class_filtered\": {\"rf_accuracy\": 0.815, \"rf_accuracy_ci\": [0.7999, 0.8298], \"lr_accuracy\": 0.7869, \"lr_accuracy_ci\": [0.7711, 0.8016], \"rf_auc\": {\"d1v2\": 0.937, \"d1v3\": 0.9944, \"d2v3\": 0.8891}}}, \"conclusion\": \"success\", \"notes\": \"GPT-2 XL temp09 意外优于 nucleus baseline: 4-class RF 85.42% vs 83.3% (+2.1pp), 3-class 82.0% vs 79.3% (+2.7pp)。与 Pythia 方向相反（Pythia temp09 降 1.9pp）。解码策略对深度信号的影响是模型依赖的。d2v3 AUC 基本持平（0.8815 vs 0.883），d1v2 AUC 提升（0.9367 vs 0.913）。filtered 3-class 81.5% 与 unfiltered 82.0% 接近，code contamination 影响小。\", \"completed_at\": \"2026-05-14T22:43:11.919Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3712}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1743bf1f-7501-4415-8a90-6c3403605b32",
  "uuid": "8cc50f14-4d54-49e6-98a4-bc92bb44f5af",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"gpt2xl_temp09_001\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T18:28:04.139Z\\\", \\\"updated_at\\\": \\\"2026-05-14T22:43:11.919Z\\\", \\\"hypothesis\\\": \\\"解码策略鲁棒性: GPT-2 XL 在 temperature-only τ=0.9 下递归生成的深度信号与 nucleus p=0.95 一致，支持跨策略泛化\\\", \\\"parent\\\": \\\"cross_model_gpt2xl_001\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash scripts/run_pipeline_gpt2xl_temp09.sh (GPT-2 XL, 3x LoRA finetune + 3x generate, temp_only τ=0.9)\\\", \\\"server\\\": \\\"gpu-6000pro-2\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 168793, \\\"log_path\\\": \\\"/root/autodl-tmp/recursive_gen_depth_est/logs/eval_gpt2xl_temp09.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T18:28:10Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl_temp09/depth_0.jsonl\\\", \\\"data_count\\\": 5000, \\\"model_name\\\": \\\"openai-community/gpt2-xl\\\", \\\"model_path\\\": \\\"/root/autodl-tmp/models/gpt2-xl/\\\", \\\"seed\\\": 42, \\\"hyperparams\\\": {\\\"lora_r\\\": 16, \\\"lora_alpha\\\": 32, \\\"target_modules\\\": [\\\"c_attn\\\", \\\"c_proj\\\"], \\\"epochs\\\": 3, \\\"lr\\\": \\\"2e-4\\\", \\\"batch_size\\\": 8, \\\"gradient_accumulation\\\": 2, \\\"max_seq_len\\\": 512, \\\"max_new_tokens\\\": 512, \\\"temperature\\\": 0.9, \\\"decoding_strategy\\\": \\\"temp_only\\\"}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/recursive_gen_depth_est/checkpoints/gpt2xl_temp09/\\\", \\\"checkpoint_source\\\": \\\"n/a (full pipeline re-run with different decoding strategy)\\\", \\\"eval_data\\\": \\\"n/a (training pipeline, not eval)\\\", \\\"results_dir\\\": \\\"/root/autodl-tmp/recursive_gen_depth_est/results/gpt2xl_temp09/\\\", \\\"eval_finished_at\\\": \\\"2026-05-15T06:42:16+08:00\\\", \\\"wall_clock_seconds\\\": 15301.9, \\\"gpu_hours\\\": 4.25}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-14T22:19:54.987Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-14T22:19:56.275209+00:00\\\"}]}, \\\"metrics\\\": {\\\"data\\\": {\\\"samples_per_depth\\\": 5000, \\\"total_samples\\\": 20000, \\\"depths\\\": 4}, \\\"finetune_losses\\\": {\\\"depth_1\\\": 2.5498, \\\"depth_2\\\": 1.6972, \\\"depth_3\\\": 1.2922}, \\\"code_contamination\\\": {\\\"depth_0\\\": {\\\"broad\\\": 25, \\\"narrow\\\": 20, \\\"broad_pct\\\": 0.5, \\\"narrow_pct\\\": 0.4}, \\\"depth_1\\\": {\\\"broad\\\": 25, \\\"narrow\\\": 40, \\\"broad_pct\\\": 0.5, \\\"narrow_pct\\\": 0.8}, \\\"depth_2\\\": {\\\"broad\\\": 34, \\\"narrow\\\": 80, \\\"broad_pct\\\": 0.7, \\\"narrow_pct\\\": 1.6}, \\\"depth_3\\\": {\\\"broad\\\": 25, \\\"narrow\\\": 76, \\\"broad_pct\\\": 0.5, \\\"narrow_pct\\\": 1.5}}, \\\"four_class\\\": {\\\"rf_accuracy\\\": 0.8542, \\\"rf_accuracy_ci\\\": [0.843, 0.8653], \\\"lr_accuracy\\\": 0.8155, \\\"lr_accuracy_ci\\\": [0.8025, 0.8273], \\\"rf_auc\\\": {\\\"d0v1\\\": 0.9963, \\\"d0v2\\\": 0.9992, \\\"d0v3\\\": 1, \\\"d1v2\\\": 0.9367, \\\"d1v3\\\": 0.9947, \\\"d2v3\\\": 0.8815}, \\\"lr_auc\\\": {\\\"d0v1\\\": 0.984, \\\"d0v2\\\": 0.9998, \\\"d0v3\\\": 1, \\\"d1v2\\\": 0.8903, \\\"d1v3\\\": 0.9824, \\\"d2v3\\\": 0.8183}, \\\"top_features\\\": [\\\"p90_ppl\\\", \\\"mean_surprisal\\\", \\\"p75_ppl\\\", \\\"var_surprisal\\\"]}, \\\"three_class\\\": {\\\"rf_accuracy\\\": 0.82, \\\"rf_accuracy_ci\\\": [0.806, 0.834], \\\"lr_accuracy\\\": 0.7773, \\\"lr_accuracy_ci\\\": [0.7627, 0.792], \\\"rf_auc\\\": {\\\"d1v2\\\": 0.9418, \\\"d1v3\\\": 0.9967, \\\"d2v3\\\": 0.8849}}, \\\"three_class_filtered\\\": {\\\"rf_accuracy\\\": 0.815, \\\"rf_accuracy_ci\\\": [0.7999, 0.8298], \\\"lr_accuracy\\\": 0.7869, \\\"lr_accuracy_ci\\\": [0.7711, 0.8016], \\\"rf_auc\\\": {\\\"d1v2\\\": 0.937, \\\"d1v3\\\": 0.9944, \\\"d2v3\\\": 0.8891}}}, \\\"conclusion\\\": \\\"success\\\", \\\"notes\\\": \\\"GPT-2 XL temp09 意外优于 nucleus baseline: 4-class RF 85.42% vs 83.3% (+2.1pp), 3-class 82.0% vs 79.3% (+2.7pp)。与 Pythia 方向相反（Pythia temp09 降 1.9pp）。解码策略对深度信号的影响是模型依赖的。d2v3 AUC 基本持平（0.8815 vs 0.883），d1v2 AUC 提升（0.9367 vs 0.913）。filtered 3-class 81.5% 与 unfiltered 82.0% 接近，code contamination 影响小。\\\", \\\"completed_at\\\": \\\"2026-05-14T22:43:11.919Z\\\"}, \\\"hint\\\": \\\"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\\\"}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.3712}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"gpt2xl_temp09_001\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:28:04.139Z\", \"updated_at\": \"2026-05-14T22:43:11.919Z\", \"hypothesis\": \"解码策略鲁棒性: GPT-2 XL 在 temperature-only τ=0.9 下递归生成的深度信号与 nucleus p=0.95 一致，支持跨策略泛化\", \"parent\": \"cross_model_gpt2xl_001\", \"spec\": {\"command\": \"bash scripts/run_pipeline_gpt2xl_temp09.sh (GPT-2 XL, 3x LoRA finetune + 3x generate, temp_only τ=0.9)\", \"server\": \"gpu-6000pro-2\", \"gpu\": \"cuda:1\", \"pid\": 168793, \"log_path\": \"/root/autodl-tmp/recursive_gen_depth_est/logs/eval_gpt2xl_temp09.log\", \"submitted_at\": \"2026-05-14T18:28:10Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl_temp09/depth_0.jsonl\", \"data_count\": 5000, \"model_name\": \"openai-community/gpt2-xl\", \"model_path\": \"/root/autodl-tmp/models/gpt2-xl/\", \"seed\": 42, \"hyperparams\": {\"lora_r\": 16, \"lora_alpha\": 32, \"target_modules\": [\"c_attn\", \"c_proj\"], \"epochs\": 3, \"lr\": \"2e-4\", \"batch_size\": 8, \"gradient_accumulation\": 2, \"max_seq_len\": 512, \"max_new_tokens\": 512, \"temperature\": 0.9, \"decoding_strategy\": \"temp_only\"}, \"checkpoint_path\": \"/root/autodl-tmp/recursive_gen_depth_est/checkpoints/gpt2xl_temp09/\", \"checkpoint_source\": \"n/a (full pipeline re-run with different decoding strategy)\", \"eval_data\": \"n/a (training pipeline, not eval)\", \"results_dir\": \"/root/autodl-tmp/recursive_gen_depth_est/results/gpt2xl_temp09/\", \"eval_finished_at\": \"2026-05-15T06:42:16+08:00\", \"wall_clock_seconds\": 15301.9, \"gpu_hours\": 4.25}, \"reproduce\": {\"finished_at\": \"2026-05-14T22:19:54.987Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T22:19:56.275209+00:00\"}]}, \"metrics\": {\"data\": {\"samples_per_depth\": 5000, \"total_samples\": 20000, \"depths\": 4}, \"finetune_losses\": {\"depth_1\": 2.5498, \"depth_2\": 1.6972, \"depth_3\": 1.2922}, \"code_contamination\": {\"depth_0\": {\"broad\": 25, \"narrow\": 20, \"broad_pct\": 0.5, \"narrow_pct\": 0.4}, \"depth_1\": {\"broad\": 25, \"narrow\": 40, \"broad_pct\": 0.5, \"narrow_pct\": 0.8}, \"depth_2\": {\"broad\": 34, \"narrow\": 80, \"broad_pct\": 0.7, \"narrow_pct\": 1.6}, \"depth_3\": {\"broad\": 25, \"narrow\": 76, \"broad_pct\": 0.5, \"narrow_pct\": 1.5}}, \"four_class\": {\"rf_accuracy\": 0.8542, \"rf_accuracy_ci\": [0.843, 0.8653], \"lr_accuracy\": 0.8155, \"lr_accuracy_ci\": [0.8025, 0.8273], \"rf_auc\": {\"d0v1\": 0.9963, \"d0v2\": 0.9992, \"d0v3\": 1, \"d1v2\": 0.9367, \"d1v3\": 0.9947, \"d2v3\": 0.8815}, \"lr_auc\": {\"d0v1\": 0.984, \"d0v2\": 0.9998, \"d0v3\": 1, \"d1v2\": 0.8903, \"d1v3\": 0.9824, \"d2v3\": 0.8183}, \"top_features\": [\"p90_ppl\", \"mean_surprisal\", \"p75_ppl\", \"var_surprisal\"]}, \"three_class\": {\"rf_accuracy\": 0.82, \"rf_accuracy_ci\": [0.806, 0.834], \"lr_accuracy\": 0.7773, \"lr_accuracy_ci\": [0.7627, 0.792], \"rf_auc\": {\"d1v2\": 0.9418, \"d1v3\": 0.9967, \"d2v3\": 0.8849}}, \"three_class_filtered\": {\"rf_accuracy\": 0.815, \"rf_accuracy_ci\": [0.7999, 0.8298], \"lr_accuracy\": 0.7869, \"lr_accuracy_ci\": [0.7711, 0.8016], \"rf_auc\": {\"d1v2\": 0.937, \"d1v3\": 0.9944, \"d2v3\": 0.8891}}}, \"conclusion\": \"success\", \"notes\": \"GPT-2 XL temp09 意外优于 nucleus baseline: 4-class RF 85.42% vs 83.3% (+2.1pp), 3-class 82.0% vs 79.3% (+2.7pp)。与 Pythia 方向相反（Pythia temp09 降 1.9pp）。解码策略对深度信号的影响是模型依赖的。d2v3 AUC 基本持平（0.8815 vs 0.883），d1v2 AUC 提升（0.9367 vs 0.913）。filtered 3-class 81.5% 与 unfiltered 82.0% 接近，code contamination 影响小。\", \"completed_at\": \"2026-05-14T22:43:11.919Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3712}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 520_

Registry 已全部更新。

---

## gpt2xl_temp09_001 结果汇总

### Finetune Losses
| Depth | Final Loss |
|-------|-----------|
| 1 | 2.5498 |
| 2 | 1.6972 |
| 3 | 1.2922 |

### Code Contamination
| Depth | Broad | Narrow |
|-------|-------|--------|
| 0 | 0.5% | 0.4% |
| 1 | 0.5% | 0.8% |
| 2 | 0.7% | 1.6% |
| 3 | 0.5% | 1.5% |

### 与 Baseline 对比（RF 指标）

| Metric | GPT-2 XL nucleus (baseline) | GPT-2 XL temp09 | Delta |
|--------|---------------------------|-----------------|-------|
| 4-class acc | 83.3% | **85.42%** | **+2.1pp** |
| 3-class acc | 79.3% | **82.00%** | **+2.7pp** |
| 3-class filtered acc | — | **81.50%** | — |
| d1v2 AUC | 0.913 | **0.9367** | +0.024 |
| d2v3 AUC | 0.883 | 0.8815 | -0.002 |

### 跨模型解码策略衰减对比

| Model | Nucleus → Temp09 | Direction |
|-------|-----------------|-----------|
| Pythia-1.4B | 78.15% → 76.25% | **-1.9pp** |
| GPT-2 XL | 83.3% → 85.42% | **+2.1pp** |

### 关键发现

GPT-2 XL 在 temperature-only τ=0.9 下**反而优于** nucleus p=0.95 baseline，与 Pythia 方向完全相反。解码策略对深度信号的影响是**模型依赖的**，不能简单假设 nucleus 总是最优。d2v3（最难区分的相邻深度）AUC 基本持平，说明信号增强主要来自 d1v2 边界。

### 3×3 矩阵更新建议

GPT-2 XL temp09 格填入 **85.4%**（原假设预期衰减，实际增强），标注为绿色/正向结果。这强化了"深度信号是递归生成的内在属性"的论点——即使解码策略变了，信号依然可检测，甚至在某些模型上更强。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1743bf1f-7501-4415-8a90-6c3403605b32",
  "uuid": "03afa937-3f1a-4212-a804-9acc86351722",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014HJyaTZmZJc2CKXPHEc8bv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2206,
      "cache_read_input_tokens": 112514,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2206
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

_source line 521_

Registry 已全部更新。

---

## gpt2xl_temp09_001 结果汇总

### Finetune Losses
| Depth | Final Loss |
|-------|-----------|
| 1 | 2.5498 |
| 2 | 1.6972 |
| 3 | 1.2922 |

### Code Contamination
| Depth | Broad | Narrow |
|-------|-------|--------|
| 0 | 0.5% | 0.4% |
| 1 | 0.5% | 0.8% |
| 2 | 0.7% | 1.6% |
| 3 | 0.5% | 1.5% |

### 与 Baseline 对比（RF 指标）

| Metric | GPT-2 XL nucleus (baseline) | GPT-2 XL temp09 | Delta |
|--------|---------------------------|-----------------|-------|
| 4-class acc | 83.3% | **85.42%** | **+2.1pp** |
| 3-class acc | 79.3% | **82.00%** | **+2.7pp** |
| 3-class filtered acc | — | **81.50%** | — |
| d1v2 AUC | 0.913 | **0.9367** | +0.024 |
| d2v3 AUC | 0.883 | 0.8815 | -0.002 |

### 跨模型解码策略衰减对比

| Model | Nucleus → Temp09 | Direction |
|-------|-----------------|-----------|
| Pythia-1.4B | 78.15% → 76.25% | **-1.9pp** |
| GPT-2 XL | 83.3% → 85.42% | **+2.1pp** |

### 关键发现

GPT-2 XL 在 temperature-only τ=0.9 下**反而优于** nucleus p=0.95 baseline，与 Pythia 方向完全相反。解码策略对深度信号的影响是**模型依赖的**，不能简单假设 nucleus 总是最优。d2v3（最难区分的相邻深度）AUC 基本持平，说明信号增强主要来自 d1v2 边界。

### 3×3 矩阵更新建议

GPT-2 XL temp09 格填入 **85.4%**（原假设预期衰减，实际增强），标注为绿色/正向结果。这强化了"深度信号是递归生成的内在属性"的论点——即使解码策略变了，信号依然可检测，甚至在某些模型上更强。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 1081435,
  "duration_api_ms": 861719,
  "num_turns": 231,
  "stop_reason": "end_turn",
  "session_id": "1743bf1f-7501-4415-8a90-6c3403605b32",
  "total_cost_usd": 9.193970750000002,
  "usage": {
    "input_tokens": 207,
    "cache_creation_input_tokens": 102879,
    "cache_read_input_tokens": 15289150,
    "output_tokens": 36141,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 102879,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 734,
        "cache_read_input_tokens": 112514,
        "cache_creation_input_tokens": 2206,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2206
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1732,
      "outputTokens": 22,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001842,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 207,
      "outputTokens": 36141,
      "cacheReadInputTokens": 15289150,
      "cacheCreationInputTokens": 102879,
      "webSearchRequests": 0,
      "costUSD": 9.192128750000002,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "c42c1c2b-1a81-4f8b-a958-6aca507b362b"
}
```

</details>

---
