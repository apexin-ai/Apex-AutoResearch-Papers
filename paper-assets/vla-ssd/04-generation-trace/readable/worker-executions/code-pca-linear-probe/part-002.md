# code pca linear probe — Part 2 of 2

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../code-pca-linear-probe.md) · [Structured JSON](../../../sessions/c5/c52d2ddceda70972f7ce.json)

## Before a recorded user message

### Tool result

_source line 227 · 2026-05-15T19:31:55.947Z_

<details><summary>↩ Tool result · `toolu_011FyikBFgpZBYPnevNrR8RC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== PCA + Linear Probe Goal Classification ===\\nModel: trained | Feature key: last_preaction | PCA dim: 1024 | Seed: 42\\nFeatures: 500 demos, 33 layers, dim=4096\\nTasks (10): ['open_the_middle_drawer_of_the_cabinet', 'open_the_top_drawer_and_put_the_bowl_inside', 'push_the_plate_to_the_front_of_the_stove', 'put_the_bowl_on_the_plate', 'put_the_bowl_on_the_stove', 'put_the_bowl_on_top_of_the_cabinet', 'put_the_cream_cheese_in_the_bowl', 'put_the_wine_bottle_on_the_rack', 'put_the_wine_bottle_on_top_of_the_cabinet', 'turn_on_the_stove']\\nSplit: 400 train / 100 val demos\\nLayers to probe: [1]\\n\\n[Layer 1] (1/1)\\n/root/miniconda3/lib/python3.12/site-packages/sklearn/linear_model/_logistic.py:1184: FutureWarning: 'n_jobs' has no effect since 1.8 and will be removed in 1.10. You provided 'n_jobs=-1', please leave it unspecified.\\n  warnings.warn(msg, category=FutureWarning)\\n/root/miniconda3/lib/python3.12/site-packages/sklearn/linear_model/_logistic.py:1184: FutureWarning: 'n_jobs' has no effect since 1.8 and will be removed in 1.10. You provided 'n_jobs=-1', please leave it unspecified.\\n  warnings.warn(msg, category=FutureWarning)\\n/root/miniconda3/lib/python3.12/site-packages/sklearn/linear_model/_logistic.py:1184: FutureWarning: 'n_jobs' has no effect since 1.8 and will be removed in 1.10. You provided 'n_jobs=-1', please leave it unspecified.\\n  warnings.warn(msg, category=FutureWarning)\\n/root/miniconda3/lib/python3.12/site-packages/sklearn/linear_model/_logistic.py:1184: FutureWarning: 'n_jobs' has no effect since 1.8 and will be removed in 1.10. You provided 'n_jobs=-1', please leave it unspecified.\\n  warnings.warn(msg, category=FutureWarning)\\n/root/miniconda3/lib/python3.12/site-packages/sklearn/linear_model/_logistic.py:1184: FutureWarning: 'n_jobs' has no effect since 1.8 and will be removed in 1.10. You provided 'n_jobs=-1', please leave it unspecified.\\n  warnings.warn(msg, category=FutureWarning)\\n/root/miniconda3/lib/python3.12/site-packages/sklearn/linear_model/_logistic.py:1184: FutureWarning: 'n_jobs' has no effect since 1.8 and will be removed in 1.10. You provided 'n_jobs=-1', please leave it unspecified.\\n  warnings.warn(msg, category=FutureWarning)\\n/root/miniconda3/lib/python3.12/site-packages/sklearn/linear_model/_logistic.py:1184: FutureWarning: 'n_jobs' has no effect since 1.8 and will be removed in 1.10. You provided 'n_jobs=-1', please leave it unspecified.\\n  warnings.warn(msg, category=FutureWarning)\\n  acc=0.9999  traj_acc=1.0000  F1=0.9999  selectivity=0.8415\\n\\nResults saved to /tmp/test_pca_probe2/trained_pca1024.json\\n\\n{\\n  \\\"model_type\\\": \\\"trained\\\",\\n  \\\"pca_dim\\\": 1024,\\n  \\\"best_layer\\\": 1,\\n  \\\"best_accuracy\\\": 0.9999221668742216,\\n  \\\"best_traj_accuracy\\\": 1.0,\\n  \\\"best_selectivity\\\": 0.8414539227895392,\\n  \\\"per_layer_accuracies\\\": {\\n    \\\"1\\\": 0.9999221668742216\\n  }\\n}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ba06b4ae-5f87-4dbd-ae90-232d1a7a9d46",
  "uuid": "270be390-9dd9-46cf-a4df-5992963f9e14",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"=== PCA + Linear Probe Goal Classification ===\\\\nModel: trained | Feature key: last_preaction | PCA dim: 1024 | Seed: 42\\\\nFeatures: 500 demos, 33 layers, dim=4096\\\\nTasks (10): ['open_the_middle_drawer_of_the_cabinet', 'open_the_top_drawer_and_put_the_bowl_inside', 'push_the_plate_to_the_front_of_the_stove', 'put_the_bowl_on_the_plate', 'put_the_bowl_on_the_stove', 'put_the_bowl_on_top_of_the_cabinet', 'put_the_cream_cheese_in_the_bowl', 'put_the_wine_bottle_on_the_rack', 'put_the_wine_bottle_on_top_of_the_cabinet', 'turn_on_the_stove']\\\\nSplit: 400 train / 100 val demos\\\\nLayers to probe: [1]\\\\n\\\\n[Layer 1] (1/1)\\\\n/root/miniconda3/lib/python3.12/site-packages/sklearn/linear_model/_logistic.py:1184: FutureWarning: 'n_jobs' has no effect since 1.8 and will be removed in 1.10. You provided 'n_jobs=-1', please leave it unspecified.\\\\n  warnings.warn(msg, category=FutureWarning)\\\\n/root/miniconda3/lib/python3.12/site-packages/sklearn/linear_model/_logistic.py:1184: FutureWarning: 'n_jobs' has no effect since 1.8 and will be removed in 1.10. You provided 'n_jobs=-1', please leave it unspecified.\\\\n  warnings.warn(msg, category=FutureWarning)\\\\n/root/miniconda3/lib/python3.12/site-packages/sklearn/linear_model/_logistic.py:1184: FutureWarning: 'n_jobs' has no effect since 1.8 and will be removed in 1.10. You provided 'n_jobs=-1', please leave it unspecified.\\\\n  warnings.warn(msg, category=FutureWarning)\\\\n/root/miniconda3/lib/python3.12/site-packages/sklearn/linear_model/_logistic.py:1184: FutureWarning: 'n_jobs' has no effect since 1.8 and will be removed in 1.10. You provided 'n_jobs=-1', please leave it unspecified.\\\\n  warnings.warn(msg, category=FutureWarning)\\\\n/root/miniconda3/lib/python3.12/site-packages/sklearn/linear_model/_logistic.py:1184: FutureWarning: 'n_jobs' has no effect since 1.8 and will be removed in 1.10. You provided 'n_jobs=-1', please leave it unspecified.\\\\n  warnings.warn(msg, category=FutureWarning)\\\\n/root/miniconda3/lib/python3.12/site-packages/sklearn/linear_model/_logistic.py:1184: FutureWarning: 'n_jobs' has no effect since 1.8 and will be removed in 1.10. You provided 'n_jobs=-1', please leave it unspecified.\\\\n  warnings.warn(msg, category=FutureWarning)\\\\n/root/miniconda3/lib/python3.12/site-packages/sklearn/linear_model/_logistic.py:1184: FutureWarning: 'n_jobs' has no effect since 1.8 and will be removed in 1.10. You provided 'n_jobs=-1', please leave it unspecified.\\\\n  warnings.warn(msg, category=FutureWarning)\\\\n  acc=0.9999  traj_acc=1.0000  F1=0.9999  selectivity=0.8415\\\\n\\\\nResults saved to /tmp/test_pca_probe2/trained_pca1024.json\\\\n\\\\n{\\\\n  \\\\\\\"model_type\\\\\\\": \\\\\\\"trained\\\\\\\",\\\\n  \\\\\\\"pca_dim\\\\\\\": 1024,\\\\n  \\\\\\\"best_layer\\\\\\\": 1,\\\\n  \\\\\\\"best_accuracy\\\\\\\": 0.9999221668742216,\\\\n  \\\\\\\"best_traj_accuracy\\\\\\\": 1.0,\\\\n  \\\\\\\"best_selectivity\\\\\\\": 0.8414539227895392,\\\\n  \\\\\\\"per_layer_accuracies\\\\\\\": {\\\\n    \\\\\\\"1\\\\\\\": 0.9999221668742216\\\\n  }\\\\n}\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"=== PCA + Linear Probe Goal Classification ===\\nModel: trained | Feature key: last_preaction | PCA dim: 1024 | Seed: 42\\nFeatures: 500 demos, 33 layers, dim=4096\\nTasks (10): ['open_the_middle_drawer_of_the_cabinet', 'open_the_top_drawer_and_put_the_bowl_inside', 'push_the_plate_to_the_front_of_the_stove', 'put_the_bowl_on_the_plate', 'put_the_bowl_on_the_stove', 'put_the_bowl_on_top_of_the_cabinet', 'put_the_cream_cheese_in_the_bowl', 'put_the_wine_bottle_on_the_rack', 'put_the_wine_bottle_on_top_of_the_cabinet', 'turn_on_the_stove']\\nSplit: 400 train / 100 val demos\\nLayers to probe: [1]\\n\\n[Layer 1] (1/1)\\n/root/miniconda3/lib/python3.12/site-packages/sklearn/linear_model/_logistic.py:1184: FutureWarning: 'n_jobs' has no effect since 1.8 and will be removed in 1.10. You provided 'n_jobs=-1', please leave it unspecified.\\n  warnings.warn(msg, category=FutureWarning)\\n/root/miniconda3/lib/python3.12/site-packages/sklearn/linear_model/_logistic.py:1184: FutureWarning: 'n_jobs' has no effect since 1.8 and will be removed in 1.10. You provided 'n_jobs=-1', please leave it unspecified.\\n  warnings.warn(msg, category=FutureWarning)\\n/root/miniconda3/lib/python3.12/site-packages/sklearn/linear_model/_logistic.py:1184: FutureWarning: 'n_jobs' has no effect since 1.8 and will be removed in 1.10. You provided 'n_jobs=-1', please leave it unspecified.\\n  warnings.warn(msg, category=FutureWarning)\\n/root/miniconda3/lib/python3.12/site-packages/sklearn/linear_model/_logistic.py:1184: FutureWarning: 'n_jobs' has no effect since 1.8 and will be removed in 1.10. You provided 'n_jobs=-1', please leave it unspecified.\\n  warnings.warn(msg, category=FutureWarning)\\n/root/miniconda3/lib/python3.12/site-packages/sklearn/linear_model/_logistic.py:1184: FutureWarning: 'n_jobs' has no effect since 1.8 and will be removed in 1.10. You provided 'n_jobs=-1', please leave it unspecified.\\n  warnings.warn(msg, category=FutureWarning)\\n/root/miniconda3/lib/python3.12/site-packages/sklearn/linear_model/_logistic.py:1184: FutureWarning: 'n_jobs' has no effect since 1.8 and will be removed in 1.10. You provided 'n_jobs=-1', please leave it unspecified.\\n  warnings.warn(msg, category=FutureWarning)\\n/root/miniconda3/lib/python3.12/site-packages/sklearn/linear_model/_logistic.py:1184: FutureWarning: 'n_jobs' has no effect since 1.8 and will be removed in 1.10. You provided 'n_jobs=-1', please leave it unspecified.\\n  warnings.warn(msg, category=FutureWarning)\\n  acc=0.9999  traj_acc=1.0000  F1=0.9999  selectivity=0.8415\\n\\nResults saved to /tmp/test_pca_probe2/trained_pca1024.json\\n\\n{\\n  \\\"model_type\\\": \\\"trained\\\",\\n  \\\"pca_dim\\\": 1024,\\n  \\\"best_layer\\\": 1,\\n  \\\"best_accuracy\\\": 0.9999221668742216,\\n  \\\"best_traj_accuracy\\\": 1.0,\\n  \\\"best_selectivity\\\": 0.8414539227895392,\\n  \\\"per_layer_accuracies\\\": {\\n    \\\"1\\\": 0.9999221668742216\\n  }\\n}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 228_

脚本验证通过，无 error。完整 JSON 输出也已保存到 `/tmp/test_pca_probe2/trained_pca1024.json`。

查看详细结果（含 PCA variance 和 per-bin accuracy）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ba06b4ae-5f87-4dbd-ae90-232d1a7a9d46",
  "uuid": "e4ea02c7-5b25-4054-a695-34c07f67a4fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0125nDobw5nqcc6SPedpbhvd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1523,
      "cache_read_input_tokens": 122245,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1523
      },
      "output_tokens": 4,
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


### Tool call

_source line 229_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01JFfUwUiFggh5J77FHAcU8s`</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /tmp/test_pca_probe2/trained_pca1024.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ba06b4ae-5f87-4dbd-ae90-232d1a7a9d46",
  "uuid": "e1bd807d-2e3e-4478-80b3-cbb2b6182dbb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0125nDobw5nqcc6SPedpbhvd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1523,
      "cache_read_input_tokens": 122245,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1523
      },
      "output_tokens": 4,
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

_source line 230 · 2026-05-15T19:32:00.551Z_

<details><summary>↩ Tool result · `toolu_01JFfUwUiFggh5J77FHAcU8s`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_type\\\": \\\"trained\\\",\\n  \\\"feature_key\\\": \\\"last_preaction\\\",\\n  \\\"pca_dim\\\": 1024,\\n  \\\"hidden_dim\\\": 4096,\\n  \\\"n_layers\\\": 33,\\n  \\\"n_tasks\\\": 10,\\n  \\\"task_names\\\": [\\n    \\\"open_the_middle_drawer_of_the_cabinet\\\",\\n    \\\"open_the_top_drawer_and_put_the_bowl_inside\\\",\\n    \\\"push_the_plate_to_the_front_of_the_stove\\\",\\n    \\\"put_the_bowl_on_the_plate\\\",\\n    \\\"put_the_bowl_on_the_stove\\\",\\n    \\\"put_the_bowl_on_top_of_the_cabinet\\\",\\n    \\\"put_the_cream_cheese_in_the_bowl\\\",\\n    \\\"put_the_wine_bottle_on_the_rack\\\",\\n    \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\",\\n    \\\"turn_on_the_stove\\\"\\n  ],\\n  \\\"seed\\\": 42,\\n  \\\"best_layer\\\": 1,\\n  \\\"best_accuracy\\\": 0.9999221668742216,\\n  \\\"best_traj_accuracy\\\": 1.0,\\n  \\\"best_macro_f1\\\": 0.9999080516201578,\\n  \\\"per_layer_accuracies\\\": {\\n    \\\"1\\\": 0.9999221668742216\\n  },\\n  \\\"per_layer_traj_accuracies\\\": {\\n    \\\"1\\\": 1.0\\n  },\\n  \\\"per_layer_selectivity\\\": {\\n    \\\"1\\\": 0.8414539227895392\\n  },\\n  \\\"per_layer_control_accuracy\\\": {\\n    \\\"1\\\": 0.15846824408468244\\n  },\\n  \\\"per_layer_per_bin_accuracy\\\": {\\n    \\\"1\\\": {\\n      \\\"0\\\": 0.9992435703479576,\\n      \\\"1\\\": 1.0,\\n      \\\"2\\\": 1.0,\\n      \\\"3\\\": 1.0,\\n      \\\"4\\\": 1.0,\\n      \\\"5\\\": 1.0,\\n      \\\"6\\\": 1.0,\\n      \\\"7\\\": 1.0,\\n      \\\"8\\\": 1.0,\\n      \\\"9\\\": 1.0\\n    }\\n  },\\n  \\\"per_layer_details\\\": {\\n    \\\"1\\\": {\\n      \\\"layer\\\": 1,\\n      \\\"accuracy\\\": 0.9999221668742216,\\n      \\\"traj_accuracy\\\": 1.0,\\n      \\\"macro_f1\\\": 0.9999080516201578,\\n      \\\"selectivity\\\": {\\n        \\\"task_accuracy\\\": 0.9999221668742216,\\n        \\\"control_accuracy\\\": 0.15846824408468244,\\n        \\\"selectivity\\\": 0.8414539227895392,\\n        \\\"control_accs\\\": [\\n          0.15924657534246575,\\n          0.15823474470734744,\\n          0.15823474470734744,\\n          0.15823474470734744,\\n          0.1583904109589041\\n        ]\\n      },\\n      \\\"per_bin_accuracy\\\": {\\n        \\\"0\\\": 0.9992435703479576,\\n        \\\"1\\\": 1.0,\\n        \\\"2\\\": 1.0,\\n        \\\"3\\\": 1.0,\\n        \\\"4\\\": 1.0,\\n        \\\"5\\\": 1.0,\\n        \\\"6\\\": 1.0,\\n        \\\"7\\\": 1.0,\\n        \\\"8\\\": 1.0,\\n        \\\"9\\\": 1.0\\n      },\\n      \\\"n_train_samples\\\": 50880,\\n      \\\"n_val_samples\\\": 12848,\\n      \\\"pca_info\\\": {\\n        \\\"cumulative_variance_ratio\\\": 0.9996331334114075,\\n        \\\"top_10_variance_ratios\\\": [\\n          0.3464735448360443,\\n          0.1712905317544937,\\n          0.0939624160528183,\\n          0.07629749178886414,\\n          0.046393606811761856,\\n          0.037901557981967926,\\n          0.032143186777830124,\\n          0.02830231562256813,\\n          0.022801179438829422,\\n          0.01841193437576294\\n        ]\\n      }\\n    }\\n  },\\n  \\\"explained_variance_ratios\\\": {\\n    \\\"1\\\": 0.9996331334114075\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ba06b4ae-5f87-4dbd-ae90-232d1a7a9d46",
  "uuid": "28578e7e-1128-4e63-9727-93a4d8b352aa",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"model_type\\\\\\\": \\\\\\\"trained\\\\\\\",\\\\n  \\\\\\\"feature_key\\\\\\\": \\\\\\\"last_preaction\\\\\\\",\\\\n  \\\\\\\"pca_dim\\\\\\\": 1024,\\\\n  \\\\\\\"hidden_dim\\\\\\\": 4096,\\\\n  \\\\\\\"n_layers\\\\\\\": 33,\\\\n  \\\\\\\"n_tasks\\\\\\\": 10,\\\\n  \\\\\\\"task_names\\\\\\\": [\\\\n    \\\\\\\"open_the_middle_drawer_of_the_cabinet\\\\\\\",\\\\n    \\\\\\\"open_the_top_drawer_and_put_the_bowl_inside\\\\\\\",\\\\n    \\\\\\\"push_the_plate_to_the_front_of_the_stove\\\\\\\",\\\\n    \\\\\\\"put_the_bowl_on_the_plate\\\\\\\",\\\\n    \\\\\\\"put_the_bowl_on_the_stove\\\\\\\",\\\\n    \\\\\\\"put_the_bowl_on_top_of_the_cabinet\\\\\\\",\\\\n    \\\\\\\"put_the_cream_cheese_in_the_bowl\\\\\\\",\\\\n    \\\\\\\"put_the_wine_bottle_on_the_rack\\\\\\\",\\\\n    \\\\\\\"put_the_wine_bottle_on_top_of_the_cabinet\\\\\\\",\\\\n    \\\\\\\"turn_on_the_stove\\\\\\\"\\\\n  ],\\\\n  \\\\\\\"seed\\\\\\\": 42,\\\\n  \\\\\\\"best_layer\\\\\\\": 1,\\\\n  \\\\\\\"best_accuracy\\\\\\\": 0.9999221668742216,\\\\n  \\\\\\\"best_traj_accuracy\\\\\\\": 1.0,\\\\n  \\\\\\\"best_macro_f1\\\\\\\": 0.9999080516201578,\\\\n  \\\\\\\"per_layer_accuracies\\\\\\\": {\\\\n    \\\\\\\"1\\\\\\\": 0.9999221668742216\\\\n  },\\\\n  \\\\\\\"per_layer_traj_accuracies\\\\\\\": {\\\\n    \\\\\\\"1\\\\\\\": 1.0\\\\n  },\\\\n  \\\\\\\"per_layer_selectivity\\\\\\\": {\\\\n    \\\\\\\"1\\\\\\\": 0.8414539227895392\\\\n  },\\\\n  \\\\\\\"per_layer_control_accuracy\\\\\\\": {\\\\n    \\\\\\\"1\\\\\\\": 0.15846824408468244\\\\n  },\\\\n  \\\\\\\"per_layer_per_bin_accuracy\\\\\\\": {\\\\n    \\\\\\\"1\\\\\\\": {\\\\n      \\\\\\\"0\\\\\\\": 0.9992435703479576,\\\\n      \\\\\\\"1\\\\\\\": 1.0,\\\\n      \\\\\\\"2\\\\\\\": 1.0,\\\\n      \\\\\\\"3\\\\\\\": 1.0,\\\\n      \\\\\\\"4\\\\\\\": 1.0,\\\\n      \\\\\\\"5\\\\\\\": 1.0,\\\\n      \\\\\\\"6\\\\\\\": 1.0,\\\\n      \\\\\\\"7\\\\\\\": 1.0,\\\\n      \\\\\\\"8\\\\\\\": 1.0,\\\\n      \\\\\\\"9\\\\\\\": 1.0\\\\n    }\\\\n  },\\\\n  \\\\\\\"per_layer_details\\\\\\\": {\\\\n    \\\\\\\"1\\\\\\\": {\\\\n      \\\\\\\"layer\\\\\\\": 1,\\\\n      \\\\\\\"accuracy\\\\\\\": 0.9999221668742216,\\\\n      \\\\\\\"traj_accuracy\\\\\\\": 1.0,\\\\n      \\\\\\\"macro_f1\\\\\\\": 0.9999080516201578,\\\\n      \\\\\\\"selectivity\\\\\\\": {\\\\n        \\\\\\\"task_accuracy\\\\\\\": 0.9999221668742216,\\\\n        \\\\\\\"control_accuracy\\\\\\\": 0.15846824408468244,\\\\n        \\\\\\\"selectivity\\\\\\\": 0.8414539227895392,\\\\n        \\\\\\\"control_accs\\\\\\\": [\\\\n          0.15924657534246575,\\\\n          0.15823474470734744,\\\\n          0.15823474470734744,\\\\n          0.15823474470734744,\\\\n          0.1583904109589041\\\\n        ]\\\\n      },\\\\n      \\\\\\\"per_bin_accuracy\\\\\\\": {\\\\n        \\\\\\\"0\\\\\\\": 0.9992435703479576,\\\\n        \\\\\\\"1\\\\\\\": 1.0,\\\\n        \\\\\\\"2\\\\\\\": 1.0,\\\\n        \\\\\\\"3\\\\\\\": 1.0,\\\\n        \\\\\\\"4\\\\\\\": 1.0,\\\\n        \\\\\\\"5\\\\\\\": 1.0,\\\\n        \\\\\\\"6\\\\\\\": 1.0,\\\\n        \\\\\\\"7\\\\\\\": 1.0,\\\\n        \\\\\\\"8\\\\\\\": 1.0,\\\\n        \\\\\\\"9\\\\\\\": 1.0\\\\n      },\\\\n      \\\\\\\"n_train_samples\\\\\\\": 50880,\\\\n      \\\\\\\"n_val_samples\\\\\\\": 12848,\\\\n      \\\\\\\"pca_info\\\\\\\": {\\\\n        \\\\\\\"cumulative_variance_ratio\\\\\\\": 0.9996331334114075,\\\\n        \\\\\\\"top_10_variance_ratios\\\\\\\": [\\\\n          0.3464735448360443,\\\\n          0.1712905317544937,\\\\n          0.0939624160528183,\\\\n          0.07629749178886414,\\\\n          0.046393606811761856,\\\\n          0.037901557981967926,\\\\n          0.032143186777830124,\\\\n          0.02830231562256813,\\\\n          0.022801179438829422,\\\\n          0.01841193437576294\\\\n        ]\\\\n      }\\\\n    }\\\\n  },\\\\n  \\\\\\\"explained_variance_ratios\\\\\\\": {\\\\n    \\\\\\\"1\\\\\\\": 0.9996331334114075\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_type\\\": \\\"trained\\\",\\n  \\\"feature_key\\\": \\\"last_preaction\\\",\\n  \\\"pca_dim\\\": 1024,\\n  \\\"hidden_dim\\\": 4096,\\n  \\\"n_layers\\\": 33,\\n  \\\"n_tasks\\\": 10,\\n  \\\"task_names\\\": [\\n    \\\"open_the_middle_drawer_of_the_cabinet\\\",\\n    \\\"open_the_top_drawer_and_put_the_bowl_inside\\\",\\n    \\\"push_the_plate_to_the_front_of_the_stove\\\",\\n    \\\"put_the_bowl_on_the_plate\\\",\\n    \\\"put_the_bowl_on_the_stove\\\",\\n    \\\"put_the_bowl_on_top_of_the_cabinet\\\",\\n    \\\"put_the_cream_cheese_in_the_bowl\\\",\\n    \\\"put_the_wine_bottle_on_the_rack\\\",\\n    \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\",\\n    \\\"turn_on_the_stove\\\"\\n  ],\\n  \\\"seed\\\": 42,\\n  \\\"best_layer\\\": 1,\\n  \\\"best_accuracy\\\": 0.9999221668742216,\\n  \\\"best_traj_accuracy\\\": 1.0,\\n  \\\"best_macro_f1\\\": 0.9999080516201578,\\n  \\\"per_layer_accuracies\\\": {\\n    \\\"1\\\": 0.9999221668742216\\n  },\\n  \\\"per_layer_traj_accuracies\\\": {\\n    \\\"1\\\": 1.0\\n  },\\n  \\\"per_layer_selectivity\\\": {\\n    \\\"1\\\": 0.8414539227895392\\n  },\\n  \\\"per_layer_control_accuracy\\\": {\\n    \\\"1\\\": 0.15846824408468244\\n  },\\n  \\\"per_layer_per_bin_accuracy\\\": {\\n    \\\"1\\\": {\\n      \\\"0\\\": 0.9992435703479576,\\n      \\\"1\\\": 1.0,\\n      \\\"2\\\": 1.0,\\n      \\\"3\\\": 1.0,\\n      \\\"4\\\": 1.0,\\n      \\\"5\\\": 1.0,\\n      \\\"6\\\": 1.0,\\n      \\\"7\\\": 1.0,\\n      \\\"8\\\": 1.0,\\n      \\\"9\\\": 1.0\\n    }\\n  },\\n  \\\"per_layer_details\\\": {\\n    \\\"1\\\": {\\n      \\\"layer\\\": 1,\\n      \\\"accuracy\\\": 0.9999221668742216,\\n      \\\"traj_accuracy\\\": 1.0,\\n      \\\"macro_f1\\\": 0.9999080516201578,\\n      \\\"selectivity\\\": {\\n        \\\"task_accuracy\\\": 0.9999221668742216,\\n        \\\"control_accuracy\\\": 0.15846824408468244,\\n        \\\"selectivity\\\": 0.8414539227895392,\\n        \\\"control_accs\\\": [\\n          0.15924657534246575,\\n          0.15823474470734744,\\n          0.15823474470734744,\\n          0.15823474470734744,\\n          0.1583904109589041\\n        ]\\n      },\\n      \\\"per_bin_accuracy\\\": {\\n        \\\"0\\\": 0.9992435703479576,\\n        \\\"1\\\": 1.0,\\n        \\\"2\\\": 1.0,\\n        \\\"3\\\": 1.0,\\n        \\\"4\\\": 1.0,\\n        \\\"5\\\": 1.0,\\n        \\\"6\\\": 1.0,\\n        \\\"7\\\": 1.0,\\n        \\\"8\\\": 1.0,\\n        \\\"9\\\": 1.0\\n      },\\n      \\\"n_train_samples\\\": 50880,\\n      \\\"n_val_samples\\\": 12848,\\n      \\\"pca_info\\\": {\\n        \\\"cumulative_variance_ratio\\\": 0.9996331334114075,\\n        \\\"top_10_variance_ratios\\\": [\\n          0.3464735448360443,\\n          0.1712905317544937,\\n          0.0939624160528183,\\n          0.07629749178886414,\\n          0.046393606811761856,\\n          0.037901557981967926,\\n          0.032143186777830124,\\n          0.02830231562256813,\\n          0.022801179438829422,\\n          0.01841193437576294\\n        ]\\n      }\\n    }\\n  },\\n  \\\"explained_variance_ratios\\\": {\\n    \\\"1\\\": 0.9996331334114075\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 231_

脚本功能完全正确。总结：

**脚本**: `/root/vla-ssd/pca_linear_probe_gc.py` (413 行)

**Layer 1 dry-run 结果**:
| 指标 | 值 |
|------|-----|
| Accuracy | 99.99% |
| Traj accuracy | 100% |
| Macro F1 | 0.9999 |
| Selectivity | 0.841 (task 99.99% - control 15.85%) |
| Bin 0 accuracy | 99.92% |
| PCA explained variance | 99.96% |

**发现**: PCA 从 4096→1024 后，1024 个主成分保留了 99.96% 的方差。即便用 linear probe（非 MLP），trained VLA layer 1 仍然 99.99% accuracy。维度降低并没有打破区分性——10-way goal classification 确实太容易了。

**DINO 实际路径**: `dinov2_libero_goal`（非 `dino_libero_goal`）

**运行完整实验的命令**:
```bash
# Trained VLA (all 33 layers)
python pca_linear_probe_gc.py --model_type trained --feature_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ --pca_dim 1024

# Untrained VLA
python pca_linear_probe_gc.py --model_type untrained --feature_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_goal/ --pca_dim 1024

# DINO (no PCA, already 1024 dim)
python pca_linear_probe_gc.py --model_type dino --feature_dir /root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/
```

注意每层约需 2-3 分钟（PCA + 7 次 LR fit），33 层全跑约 1-1.5 小时。`n_jobs` 参数可以去掉以消除 FutureWarning（sklearn 1.8 不再支持，不影响功能）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ba06b4ae-5f87-4dbd-ae90-232d1a7a9d46",
  "uuid": "98c5971a-73ee-47cc-b2ab-452ad80c6146",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HV8o4qSn54QqGD6KKBzbmc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1738,
      "cache_read_input_tokens": 123768,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1738
      },
      "output_tokens": 4,
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

_source line 232_

脚本功能完全正确。总结：

**脚本**: `/root/vla-ssd/pca_linear_probe_gc.py` (413 行)

**Layer 1 dry-run 结果**:
| 指标 | 值 |
|------|-----|
| Accuracy | 99.99% |
| Traj accuracy | 100% |
| Macro F1 | 0.9999 |
| Selectivity | 0.841 (task 99.99% - control 15.85%) |
| Bin 0 accuracy | 99.92% |
| PCA explained variance | 99.96% |

**发现**: PCA 从 4096→1024 后，1024 个主成分保留了 99.96% 的方差。即便用 linear probe（非 MLP），trained VLA layer 1 仍然 99.99% accuracy。维度降低并没有打破区分性——10-way goal classification 确实太容易了。

**DINO 实际路径**: `dinov2_libero_goal`（非 `dino_libero_goal`）

**运行完整实验的命令**:
```bash
# Trained VLA (all 33 layers)
python pca_linear_probe_gc.py --model_type trained --feature_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ --pca_dim 1024

# Untrained VLA
python pca_linear_probe_gc.py --model_type untrained --feature_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_goal/ --pca_dim 1024

# DINO (no PCA, already 1024 dim)
python pca_linear_probe_gc.py --model_type dino --feature_dir /root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/
```

注意每层约需 2-3 分钟（PCA + 7 次 LR fit），33 层全跑约 1-1.5 小时。`n_jobs` 参数可以去掉以消除 FutureWarning（sklearn 1.8 不再支持，不影响功能）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 679431,
  "duration_api_ms": 555810,
  "num_turns": 89,
  "stop_reason": "end_turn",
  "session_id": "ba06b4ae-5f87-4dbd-ae90-232d1a7a9d46",
  "total_cost_usd": 4.96630725,
  "usage": {
    "input_tokens": 84,
    "cache_creation_input_tokens": 113665,
    "cache_read_input_tokens": 6947322,
    "output_tokens": 31171,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 113665,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 590,
        "cache_read_input_tokens": 123768,
        "cache_creation_input_tokens": 1738,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1738
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2465,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0025450000000000004,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 84,
      "outputTokens": 31171,
      "cacheReadInputTokens": 6947322,
      "cacheCreationInputTokens": 113665,
      "webSearchRequests": 0,
      "costUSD": 4.96376225,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "81a88bdf-45be-46af-9e42-cc2a872e1933"
}
```

</details>

---
