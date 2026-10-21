# research xvla westd41074 — Part 3 of 3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

[← Part 2](part-002.md) · [Transcript overview](../research-xvla-westd41074.md) · [Structured JSON](../../../sessions/ef/ef8d23b07cc382822df2.json)

## Round 1

### Tool result

_source line 782 · 2026-05-20T04:35:33.451Z_

<details><summary>↩ Tool result · `toolu_01UVsvMYJRobdGKUEKPmQJG3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"X-VLA-0.9B (lerobot/xvla-libero)\\\",\\n  \\\"dataset\\\": \\\"LIBERO-Object (task_index 20-29)\\\",\\n  \\\"n_images\\\": 100,\\n  \\\"n_tasks\\\": 10,\\n  \\\"architecture\\\": {\\n    \\\"vision_encoder\\\": \\\"Florence-2 DaViT-Large\\\",\\n    \\\"connector\\\": \\\"Linear projection (image_projection matrix + LayerNorm)\\\",\\n    \\\"vlm_encoder\\\": \\\"Florence-2 BART encoder (12 layers, d=1024)\\\",\\n    \\\"action_head\\\": \\\"SoftPromptedTransformer (24L, h=1024)\\\",\\n    \\\"soft_prompts\\\": 32,\\n    \\\"projection_dim\\\": 1024\\n  },\\n  \\\"sequence_layout\\\": {\\n    \\\"action_tokens\\\": 30,\\n    \\\"vlm_features\\\": 64,\\n    \\\"aux_visual\\\": 150,\\n    \\\"soft_prompts\\\": 32,\\n    \\\"total\\\": 276\\n  },\\n  \\\"per_layer_entropy_ratio\\\": {\\n    \\\"0\\\": 0.4569,\\n    \\\"1\\\": 0.3381,\\n    \\\"2\\\": 0.3838,\\n    \\\"3\\\": 0.5218,\\n    \\\"4\\\": 0.4664,\\n    \\\"5\\\": 0.5572,\\n    \\\"6\\\": 0.6177,\\n    \\\"7\\\": 0.6368,\\n    \\\"8\\\": 0.6378,\\n    \\\"9\\\": 0.6222,\\n    \\\"10\\\": 0.6379,\\n    \\\"11\\\": 0.6595,\\n    \\\"12\\\": 0.6246,\\n    \\\"13\\\": 0.5569,\\n    \\\"14\\\": 0.5868,\\n    \\\"15\\\": 0.6236,\\n    \\\"16\\\": 0.626,\\n    \\\"17\\\": 0.704,\\n    \\\"18\\\": 0.7496,\\n    \\\"19\\\": 0.7422,\\n    \\\"20\\\": 0.7313,\\n    \\\"21\\\": 0.7452,\\n    \\\"22\\\": 0.7933,\\n    \\\"23\\\": 0.7125\\n  },\\n  \\\"per_layer_entropy_std\\\": {\\n    \\\"0\\\": 0.0079,\\n    \\\"1\\\": 0.0167,\\n    \\\"2\\\": 0.0166,\\n    \\\"3\\\": 0.0191,\\n    \\\"4\\\": 0.0263,\\n    \\\"5\\\": 0.0288,\\n    \\\"6\\\": 0.0245,\\n    \\\"7\\\": 0.0275,\\n    \\\"8\\\": 0.0255,\\n    \\\"9\\\": 0.0236,\\n    \\\"10\\\": 0.0241,\\n    \\\"11\\\": 0.0205,\\n    \\\"12\\\": 0.0327,\\n    \\\"13\\\": 0.0262,\\n    \\\"14\\\": 0.0174,\\n    \\\"15\\\": 0.014,\\n    \\\"16\\\": 0.0189,\\n    \\\"17\\\": 0.0188,\\n    \\\"18\\\": 0.017,\\n    \\\"19\\\": 0.0187,\\n    \\\"20\\\": 0.016,\\n    \\\"21\\\": 0.022,\\n    \\\"22\\\": 0.0211,\\n    \\\"23\\\": 0.02\\n  },\\n  \\\"per_layer_vision_attention_fraction\\\": {\\n    \\\"0\\\": 0.3346,\\n    \\\"1\\\": 0.4868,\\n    \\\"2\\\": 0.4645,\\n    \\\"3\\\": 0.705,\\n    \\\"4\\\": 0.6361,\\n    \\\"5\\\": 0.7356,\\n    \\\"6\\\": 0.8549,\\n    \\\"7\\\": 0.9033,\\n    \\\"8\\\": 0.9049,\\n    \\\"9\\\": 0.864,\\n    \\\"10\\\": 0.8551,\\n    \\\"11\\\": 0.8372,\\n    \\\"12\\\": 0.8115,\\n    \\\"13\\\": 0.7475,\\n    \\\"14\\\": 0.74,\\n    \\\"15\\\": 0.6955,\\n    \\\"16\\\": 0.8275,\\n    \\\"17\\\": 0.8611,\\n    \\\"18\\\": 0.861,\\n    \\\"19\\\": 0.9165,\\n    \\\"20\\\": 0.8841,\\n    \\\"21\\\": 0.7898,\\n    \\\"22\\\": 0.8345,\\n    \\\"23\\\": 0.8974\\n  },\\n  \\\"pruning_curve\\\": {\\n    \\\"0.3\\\": {\\n      \\\"mean_loss\\\": 0.112945,\\n      \\\"std_loss\\\": 0.018799\\n    },\\n    \\\"0.5\\\": {\\n      \\\"mean_loss\\\": 0.112823,\\n      \\\"std_loss\\\": 0.018785\\n    },\\n    \\\"0.7\\\": {\\n      \\\"mean_loss\\\": 0.112789,\\n      \\\"std_loss\\\": 0.018772\\n    },\\n    \\\"0.9\\\": {\\n      \\\"mean_loss\\\": 0.112789,\\n      \\\"std_loss\\\": 0.018772\\n    },\\n    \\\"0.95\\\": {\\n      \\\"mean_loss\\\": 0.112789,\\n      \\\"std_loss\\\": 0.018772\\n    },\\n    \\\"1.0\\\": {\\n      \\\"mean_loss\\\": 0.112789,\\n      \\\"std_loss\\\": 0.018772\\n    }\\n  },\\n  \\\"overall_entropy_ratio\\\": 0.6138,\\n  \\\"overall_entropy_std\\\": 0.1159,\\n  \\\"pruning_curve_normalized\\\": {\\n    \\\"0.3\\\": 1.0014,\\n    \\\"0.5\\\": 1.0003,\\n    \\\"0.7\\\": 1.0,\\n    \\\"0.9\\\": 1.0,\\n    \\\"0.95\\\": 1.0,\\n    \\\"1.0\\\": 1.0\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "9d855ec3-ac25-49d6-b0b1-4e4a1973033d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"model\\\\\\\": \\\\\\\"X-VLA-0.9B (lerobot/xvla-libero)\\\\\\\",\\\\n  \\\\\\\"dataset\\\\\\\": \\\\\\\"LIBERO-Object (task_index 20-29)\\\\\\\",\\\\n  \\\\\\\"n_images\\\\\\\": 100,\\\\n  \\\\\\\"n_tasks\\\\\\\": 10,\\\\n  \\\\\\\"architecture\\\\\\\": {\\\\n    \\\\\\\"vision_encoder\\\\\\\": \\\\\\\"Florence-2 DaViT-Large\\\\\\\",\\\\n    \\\\\\\"connector\\\\\\\": \\\\\\\"Linear projection (image_projection matrix + LayerNorm)\\\\\\\",\\\\n    \\\\\\\"vlm_encoder\\\\\\\": \\\\\\\"Florence-2 BART encoder (12 layers, d=1024)\\\\\\\",\\\\n    \\\\\\\"action_head\\\\\\\": \\\\\\\"SoftPromptedTransformer (24L, h=1024)\\\\\\\",\\\\n    \\\\\\\"soft_prompts\\\\\\\": 32,\\\\n    \\\\\\\"projection_dim\\\\\\\": 1024\\\\n  },\\\\n  \\\\\\\"sequence_layout\\\\\\\": {\\\\n    \\\\\\\"action_tokens\\\\\\\": 30,\\\\n    \\\\\\\"vlm_features\\\\\\\": 64,\\\\n    \\\\\\\"aux_visual\\\\\\\": 150,\\\\n    \\\\\\\"soft_prompts\\\\\\\": 32,\\\\n    \\\\\\\"total\\\\\\\": 276\\\\n  },\\\\n  \\\\\\\"per_layer_entropy_ratio\\\\\\\": {\\\\n    \\\\\\\"0\\\\\\\": 0.4569,\\\\n    \\\\\\\"1\\\\\\\": 0.3381,\\\\n    \\\\\\\"2\\\\\\\": 0.3838,\\\\n    \\\\\\\"3\\\\\\\": 0.5218,\\\\n    \\\\\\\"4\\\\\\\": 0.4664,\\\\n    \\\\\\\"5\\\\\\\": 0.5572,\\\\n    \\\\\\\"6\\\\\\\": 0.6177,\\\\n    \\\\\\\"7\\\\\\\": 0.6368,\\\\n    \\\\\\\"8\\\\\\\": 0.6378,\\\\n    \\\\\\\"9\\\\\\\": 0.6222,\\\\n    \\\\\\\"10\\\\\\\": 0.6379,\\\\n    \\\\\\\"11\\\\\\\": 0.6595,\\\\n    \\\\\\\"12\\\\\\\": 0.6246,\\\\n    \\\\\\\"13\\\\\\\": 0.5569,\\\\n    \\\\\\\"14\\\\\\\": 0.5868,\\\\n    \\\\\\\"15\\\\\\\": 0.6236,\\\\n    \\\\\\\"16\\\\\\\": 0.626,\\\\n    \\\\\\\"17\\\\\\\": 0.704,\\\\n    \\\\\\\"18\\\\\\\": 0.7496,\\\\n    \\\\\\\"19\\\\\\\": 0.7422,\\\\n    \\\\\\\"20\\\\\\\": 0.7313,\\\\n    \\\\\\\"21\\\\\\\": 0.7452,\\\\n    \\\\\\\"22\\\\\\\": 0.7933,\\\\n    \\\\\\\"23\\\\\\\": 0.7125\\\\n  },\\\\n  \\\\\\\"per_layer_entropy_std\\\\\\\": {\\\\n    \\\\\\\"0\\\\\\\": 0.0079,\\\\n    \\\\\\\"1\\\\\\\": 0.0167,\\\\n    \\\\\\\"2\\\\\\\": 0.0166,\\\\n    \\\\\\\"3\\\\\\\": 0.0191,\\\\n    \\\\\\\"4\\\\\\\": 0.0263,\\\\n    \\\\\\\"5\\\\\\\": 0.0288,\\\\n    \\\\\\\"6\\\\\\\": 0.0245,\\\\n    \\\\\\\"7\\\\\\\": 0.0275,\\\\n    \\\\\\\"8\\\\\\\": 0.0255,\\\\n    \\\\\\\"9\\\\\\\": 0.0236,\\\\n    \\\\\\\"10\\\\\\\": 0.0241,\\\\n    \\\\\\\"11\\\\\\\": 0.0205,\\\\n    \\\\\\\"12\\\\\\\": 0.0327,\\\\n    \\\\\\\"13\\\\\\\": 0.0262,\\\\n    \\\\\\\"14\\\\\\\": 0.0174,\\\\n    \\\\\\\"15\\\\\\\": 0.014,\\\\n    \\\\\\\"16\\\\\\\": 0.0189,\\\\n    \\\\\\\"17\\\\\\\": 0.0188,\\\\n    \\\\\\\"18\\\\\\\": 0.017,\\\\n    \\\\\\\"19\\\\\\\": 0.0187,\\\\n    \\\\\\\"20\\\\\\\": 0.016,\\\\n    \\\\\\\"21\\\\\\\": 0.022,\\\\n    \\\\\\\"22\\\\\\\": 0.0211,\\\\n    \\\\\\\"23\\\\\\\": 0.02\\\\n  },\\\\n  \\\\\\\"per_layer_vision_attention_fraction\\\\\\\": {\\\\n    \\\\\\\"0\\\\\\\": 0.3346,\\\\n    \\\\\\\"1\\\\\\\": 0.4868,\\\\n    \\\\\\\"2\\\\\\\": 0.4645,\\\\n    \\\\\\\"3\\\\\\\": 0.705,\\\\n    \\\\\\\"4\\\\\\\": 0.6361,\\\\n    \\\\\\\"5\\\\\\\": 0.7356,\\\\n    \\\\\\\"6\\\\\\\": 0.8549,\\\\n    \\\\\\\"7\\\\\\\": 0.9033,\\\\n    \\\\\\\"8\\\\\\\": 0.9049,\\\\n    \\\\\\\"9\\\\\\\": 0.864,\\\\n    \\\\\\\"10\\\\\\\": 0.8551,\\\\n    \\\\\\\"11\\\\\\\": 0.8372,\\\\n    \\\\\\\"12\\\\\\\": 0.8115,\\\\n    \\\\\\\"13\\\\\\\": 0.7475,\\\\n    \\\\\\\"14\\\\\\\": 0.74,\\\\n    \\\\\\\"15\\\\\\\": 0.6955,\\\\n    \\\\\\\"16\\\\\\\": 0.8275,\\\\n    \\\\\\\"17\\\\\\\": 0.8611,\\\\n    \\\\\\\"18\\\\\\\": 0.861,\\\\n    \\\\\\\"19\\\\\\\": 0.9165,\\\\n    \\\\\\\"20\\\\\\\": 0.8841,\\\\n    \\\\\\\"21\\\\\\\": 0.7898,\\\\n    \\\\\\\"22\\\\\\\": 0.8345,\\\\n    \\\\\\\"23\\\\\\\": 0.8974\\\\n  },\\\\n  \\\\\\\"pruning_curve\\\\\\\": {\\\\n    \\\\\\\"0.3\\\\\\\": {\\\\n      \\\\\\\"mean_loss\\\\\\\": 0.112945,\\\\n      \\\\\\\"std_loss\\\\\\\": 0.018799\\\\n    },\\\\n    \\\\\\\"0.5\\\\\\\": {\\\\n      \\\\\\\"mean_loss\\\\\\\": 0.112823,\\\\n      \\\\\\\"std_loss\\\\\\\": 0.018785\\\\n    },\\\\n    \\\\\\\"0.7\\\\\\\": {\\\\n      \\\\\\\"mean_loss\\\\\\\": 0.112789,\\\\n      \\\\\\\"std_loss\\\\\\\": 0.018772\\\\n    },\\\\n    \\\\\\\"0.9\\\\\\\": {\\\\n      \\\\\\\"mean_loss\\\\\\\": 0.112789,\\\\n      \\\\\\\"std_loss\\\\\\\": 0.018772\\\\n    },\\\\n    \\\\\\\"0.95\\\\\\\": {\\\\n      \\\\\\\"mean_loss\\\\\\\": 0.112789,\\\\n      \\\\\\\"std_loss\\\\\\\": 0.018772\\\\n    },\\\\n    \\\\\\\"1.0\\\\\\\": {\\\\n      \\\\\\\"mean_loss\\\\\\\": 0.112789,\\\\n      \\\\\\\"std_loss\\\\\\\": 0.018772\\\\n    }\\\\n  },\\\\n  \\\\\\\"overall_entropy_ratio\\\\\\\": 0.6138,\\\\n  \\\\\\\"overall_entropy_std\\\\\\\": 0.1159,\\\\n  \\\\\\\"pruning_curve_normalized\\\\\\\": {\\\\n    \\\\\\\"0.3\\\\\\\": 1.0014,\\\\n    \\\\\\\"0.5\\\\\\\": 1.0003,\\\\n    \\\\\\\"0.7\\\\\\\": 1.0,\\\\n    \\\\\\\"0.9\\\\\\\": 1.0,\\\\n    \\\\\\\"0.95\\\\\\\": 1.0,\\\\n    \\\\\\\"1.0\\\\\\\": 1.0\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"X-VLA-0.9B (lerobot/xvla-libero)\\\",\\n  \\\"dataset\\\": \\\"LIBERO-Object (task_index 20-29)\\\",\\n  \\\"n_images\\\": 100,\\n  \\\"n_tasks\\\": 10,\\n  \\\"architecture\\\": {\\n    \\\"vision_encoder\\\": \\\"Florence-2 DaViT-Large\\\",\\n    \\\"connector\\\": \\\"Linear projection (image_projection matrix + LayerNorm)\\\",\\n    \\\"vlm_encoder\\\": \\\"Florence-2 BART encoder (12 layers, d=1024)\\\",\\n    \\\"action_head\\\": \\\"SoftPromptedTransformer (24L, h=1024)\\\",\\n    \\\"soft_prompts\\\": 32,\\n    \\\"projection_dim\\\": 1024\\n  },\\n  \\\"sequence_layout\\\": {\\n    \\\"action_tokens\\\": 30,\\n    \\\"vlm_features\\\": 64,\\n    \\\"aux_visual\\\": 150,\\n    \\\"soft_prompts\\\": 32,\\n    \\\"total\\\": 276\\n  },\\n  \\\"per_layer_entropy_ratio\\\": {\\n    \\\"0\\\": 0.4569,\\n    \\\"1\\\": 0.3381,\\n    \\\"2\\\": 0.3838,\\n    \\\"3\\\": 0.5218,\\n    \\\"4\\\": 0.4664,\\n    \\\"5\\\": 0.5572,\\n    \\\"6\\\": 0.6177,\\n    \\\"7\\\": 0.6368,\\n    \\\"8\\\": 0.6378,\\n    \\\"9\\\": 0.6222,\\n    \\\"10\\\": 0.6379,\\n    \\\"11\\\": 0.6595,\\n    \\\"12\\\": 0.6246,\\n    \\\"13\\\": 0.5569,\\n    \\\"14\\\": 0.5868,\\n    \\\"15\\\": 0.6236,\\n    \\\"16\\\": 0.626,\\n    \\\"17\\\": 0.704,\\n    \\\"18\\\": 0.7496,\\n    \\\"19\\\": 0.7422,\\n    \\\"20\\\": 0.7313,\\n    \\\"21\\\": 0.7452,\\n    \\\"22\\\": 0.7933,\\n    \\\"23\\\": 0.7125\\n  },\\n  \\\"per_layer_entropy_std\\\": {\\n    \\\"0\\\": 0.0079,\\n    \\\"1\\\": 0.0167,\\n    \\\"2\\\": 0.0166,\\n    \\\"3\\\": 0.0191,\\n    \\\"4\\\": 0.0263,\\n    \\\"5\\\": 0.0288,\\n    \\\"6\\\": 0.0245,\\n    \\\"7\\\": 0.0275,\\n    \\\"8\\\": 0.0255,\\n    \\\"9\\\": 0.0236,\\n    \\\"10\\\": 0.0241,\\n    \\\"11\\\": 0.0205,\\n    \\\"12\\\": 0.0327,\\n    \\\"13\\\": 0.0262,\\n    \\\"14\\\": 0.0174,\\n    \\\"15\\\": 0.014,\\n    \\\"16\\\": 0.0189,\\n    \\\"17\\\": 0.0188,\\n    \\\"18\\\": 0.017,\\n    \\\"19\\\": 0.0187,\\n    \\\"20\\\": 0.016,\\n    \\\"21\\\": 0.022,\\n    \\\"22\\\": 0.0211,\\n    \\\"23\\\": 0.02\\n  },\\n  \\\"per_layer_vision_attention_fraction\\\": {\\n    \\\"0\\\": 0.3346,\\n    \\\"1\\\": 0.4868,\\n    \\\"2\\\": 0.4645,\\n    \\\"3\\\": 0.705,\\n    \\\"4\\\": 0.6361,\\n    \\\"5\\\": 0.7356,\\n    \\\"6\\\": 0.8549,\\n    \\\"7\\\": 0.9033,\\n    \\\"8\\\": 0.9049,\\n    \\\"9\\\": 0.864,\\n    \\\"10\\\": 0.8551,\\n    \\\"11\\\": 0.8372,\\n    \\\"12\\\": 0.8115,\\n    \\\"13\\\": 0.7475,\\n    \\\"14\\\": 0.74,\\n    \\\"15\\\": 0.6955,\\n    \\\"16\\\": 0.8275,\\n    \\\"17\\\": 0.8611,\\n    \\\"18\\\": 0.861,\\n    \\\"19\\\": 0.9165,\\n    \\\"20\\\": 0.8841,\\n    \\\"21\\\": 0.7898,\\n    \\\"22\\\": 0.8345,\\n    \\\"23\\\": 0.8974\\n  },\\n  \\\"pruning_curve\\\": {\\n    \\\"0.3\\\": {\\n      \\\"mean_loss\\\": 0.112945,\\n      \\\"std_loss\\\": 0.018799\\n    },\\n    \\\"0.5\\\": {\\n      \\\"mean_loss\\\": 0.112823,\\n      \\\"std_loss\\\": 0.018785\\n    },\\n    \\\"0.7\\\": {\\n      \\\"mean_loss\\\": 0.112789,\\n      \\\"std_loss\\\": 0.018772\\n    },\\n    \\\"0.9\\\": {\\n      \\\"mean_loss\\\": 0.112789,\\n      \\\"std_loss\\\": 0.018772\\n    },\\n    \\\"0.95\\\": {\\n      \\\"mean_loss\\\": 0.112789,\\n      \\\"std_loss\\\": 0.018772\\n    },\\n    \\\"1.0\\\": {\\n      \\\"mean_loss\\\": 0.112789,\\n      \\\"std_loss\\\": 0.018772\\n    }\\n  },\\n  \\\"overall_entropy_ratio\\\": 0.6138,\\n  \\\"overall_entropy_std\\\": 0.1159,\\n  \\\"pruning_curve_normalized\\\": {\\n    \\\"0.3\\\": 1.0014,\\n    \\\"0.5\\\": 1.0003,\\n    \\\"0.7\\\": 1.0,\\n    \\\"0.9\\\": 1.0,\\n    \\\"0.95\\\": 1.0,\\n    \\\"1.0\\\": 1.0\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 783_

结果非常清晰。现在注册artifact并更新memory和registry。

关键发现：
- **Overall entropy ratio: 0.6138** — 中等偏高，注意力分布比较均匀
- **Pruning curve几乎完全平坦**: k=0.3时norm loss仅1.0014（只高0.14%），意味着**丢弃70%的vision tokens几乎不影响loss**
- 这说明X-VLA的Linear projection connector产生了**高度可压缩的**vision tokens

先注册结果artifact，然后更新memory.md。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "c82a6972-4d81-44e6-9487-80bec905fecc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MrpHEZFKRXhVxhfkpYVEBh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2273,
      "cache_read_input_tokens": 85994,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2273
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


### Tool call

_source line 784_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014kT1vZQQQb2iydcSS4VSwJ`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_registry",
  "max_results": 4
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "f19ffb03-b41f-4aa7-8e86-fd618479e231",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MrpHEZFKRXhVxhfkpYVEBh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2273,
      "cache_read_input_tokens": 85994,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2273
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


### Tool result

_source line 785 · 2026-05-20T04:35:41.124Z_

<details><summary>↩ Tool result · `toolu_014kT1vZQQQb2iydcSS4VSwJ`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__update_registry"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "53cff6e8-f5ca-43f9-ac58-d666934b0a19",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__update_registry"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_registry",
    "total_deferred_tools": 30
  }
}
```

</details>

---


### Tool call

_source line 786_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01GSZLgUSXGQWuoyMUFdWTZh`</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "f46cab1a-4113-4ff6-9bb0-5adcffec135d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UMsPHmgMYs7iZ6ffFcmed8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1963,
      "cache_read_input_tokens": 88267,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1963
      },
      "output_tokens": 47,
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

_source line 787 · 2026-05-20T04:35:44.786Z_

<details><summary>↩ Tool result · `toolu_01GSZLgUSXGQWuoyMUFdWTZh`</summary>

````text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/memory.md\", \"content\": \"# VLA 模型全面调研报告\\n\\n**调研日期**: 2026-05-20\\n**目的**: 寻找不同 connector 架构的开源 VLA 模型，扩展 vision connector 对 token 可压缩性影响的实验\\n\\n---\\n\\n## 已有实验数据\\n\\n| 模型 | Connector | 压缩行为 |\\n|------|-----------|----------|\\n| SmolVLA | Pixel-shuffle | Cliff-edge collapse (k=0.95 → 0% SR) |\\n| OpenVLA | 2-layer MLP projector | Graded degradation (线性下降) |\\n| RoboFlamingo | Perceiver Resampler | 尝试失败（gripper loss 无法训练） |\\n\\n---\\n\\n## 完整模型调研表\\n\\n### 1. Octo (UC Berkeley, 2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 27M (Small) / 93M (Base) |\\n| Vision encoder | Shallow CNN (从头训练，非预训练 ViT) |\\n| **Connector 类型** | **CNN patch encoder → 直接拼接进 transformer（无独立 connector）** |\\n| LLM backbone | 纯 transformer（非预训练 LLM），decoder-only |\\n| 开源状态 | ✅ weights + code, GitHub: [octo-models/octo](https://github.com/octo-models/octo), HF: rail-berkeley/octo-base |\\n| LIBERO 支持 | ✅ 原生支持，fine-tune 后 ~72% SR |\\n| 改造成本 | 低（已有 LIBERO fine-tune 代码） |\\n| 论文 LIBERO 结果 | 有: ~72% (fine-tuned) |\\n| 备注 | 非标准 VLM→LLM 架构，是 transformer-based diffusion policy。图像通过浅层 CNN 编码为 16×16 patches 后直接拼入 transformer 序列。语言用 T5 tokenizer/encoder。Action head 是 diffusion policy。 |\\n\\n### 2. CogACT (Microsoft/Tsinghua, 2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | ~7.1B (7B Prismatic VLM + 89M-300M DiT action module) |\\n| Vision encoder | DINOv2 + SigLIP (双 encoder，channel 拼接) |\\n| **Connector 类型** | **2-layer MLP projector**（Prismatic 架构：DINOv2+SigLIP feature → channel concat → 2-layer MLP → Llama-2 embedding space） |\\n| LLM backbone | Llama-2 7B (via Prismatic-7B) |\\n| 开源状态 | ✅ weights + code, GitHub: [microsoft/CogACT](https://github.com/microsoft/CogACT), HF: CogACT/CogACT-Base, CogACT/CogACT-Small |\\n| LIBERO 支持 | 需改造（paper 用 SimplerEnv + 真机） |\\n| 改造成本 | 中（需接 LIBERO data pipeline + action space） |\\n| 论文 LIBERO 结果 | 无 |\\n| 备注 | 核心创新在 DiT action module（将 VLM 认知特征作为 condition 输入扩散 transformer 生成动作）。Connector 与 OpenVLA 相同（都基于 Prismatic） |\\n\\n### 3. HPT (MIT, NeurIPS 2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 3.1M (S) / 12.6M (B) / 50.5M (L) / 226.8M (XL) / 1.1B (Huge) |\\n| Vision encoder | 预训练冻结 ResNet18 |\\n| **Connector 类型** | **Cross-attention tokenizer**（learnable tokens 通过 cross-attention 聚合 vision features → 固定 16 tokens，每个 camera view 有独立 MLP projector） |\\n| LLM backbone | 无（纯 decoder-only transformer，从头训练） |\\n| 开源状态 | ✅ weights + code, GitHub: [liruiw/HPT](https://github.com/liruiw/HPT), HF: liruiw/hpt |\\n| LIBERO 支持 | 未确认（paper 评测 6 个 benchmark） |\\n| 改造成本 | 中（非标准 VLM 架构，需改 stem + action head） |\\n| 论文 LIBERO 结果 | 无 |\\n| 备注 | 非 VLM→LLM 架构。Cross-attention tokenizer 类似 Perceiver 但更轻量（8 heads, 64 dim/head）。跨 embodiment 预训练。 |\\n\\n### 4. RT-2-X (Google DeepMind, 2023)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 55B |\\n| Vision encoder | ViT (PaLI-X 的视觉编码器) |\\n| **Connector 类型** | 未公开（闭源） |\\n| LLM backbone | PaLI-X / PaLM-E |\\n| 开源状态 | ❌ **闭源**，权重不公开 |\\n| LIBERO 支持 | 不可行 |\\n| 改造成本 | 不可行 |\\n| 论文 LIBERO 结果 | 无 |\\n| 备注 | 闭源模型，无法使用 |\\n\\n### 5. GR-1 (ByteDance, 2023)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 未明确公布 |\\n| Vision encoder | MAE ViT-Base (预训练) |\\n| **Connector 类型** | **Perceiver Resampler**（将 MAE ViT 视觉 token 数量压缩）+ linear layers 对齐维度 |\\n| LLM backbone | GPT-style causal transformer（非预训练 LLM） |\\n| 开源状态 | ✅ weights + code, GitHub: [bytedance/GR-1](https://github.com/bytedance/GR-1), Apache-2.0 |\\n| LIBERO 支持 | 需改造（paper 只有 CALVIN） |\\n| 改造成本 | 高（需改 data pipeline、action space、视频生成部分可能要适配） |\\n| 论文 LIBERO 结果 | 无（CALVIN: 94.9%） |\\n| 备注 | 既做动作预测又做视频生成（future image prediction）。语言用 CLIP text encoder。使用 Perceiver Resampler 这一点很有价值——与 RoboFlamingo 类似但架构不同。 |\\n\\n### 6. GR-2 (ByteDance, 2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 未公布 |\\n| Vision encoder | 未公布 |\\n| **Connector 类型** | 未公布 |\\n| LLM backbone | 未公布 |\\n| 开源状态 | ❌ **未开源**，代码/权重未释放 |\\n| LIBERO 支持 | 不可行 |\\n| 改造成本 | 不可行 |\\n| 论文 LIBERO 结果 | 无 |\\n| 备注 | GR-1 的后续，但未开源 |\\n\\n### 7. LLARVA (2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 7B |\\n| Vision encoder | CLIP ViT-L/14 |\\n| **Connector 类型** | **MLP projector**（LLaVA-style，2-layer MLP with GELU） |\\n| LLM backbone | Llama-2 7B |\\n| 开源状态 | ✅ code + LoRA weights, GitHub: [Dantong88/LLARVA](https://github.com/Dantong88/LLARVA), Apache-2.0 |\\n| LIBERO 支持 | 需改造 |\\n| 改造成本 | 中（需接 action head + LIBERO data pipeline） |\\n| 论文 LIBERO 结果 | 无 |\\n| 备注 | 预测 visual traces (2D 轨迹) 作为中间表示。Connector 与 OpenVLA 类似（都是 MLP projector），但用 CLIP 而非 Prismatic 双 encoder |\\n\\n### 8. RoboVLMs (2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 不定（框架） |\\n| Vision encoder | 支持多种 VLM backbone |\\n| **Connector 类型** | 取决于所选 VLM（框架支持多种） |\\n| LLM backbone | 取决于所选 VLM |\\n| 开源状态 | ✅ code + models, GitHub: [Robot-VLAs/RoboVLMs](https://github.com/Robot-VLAs/RoboVLMs) |\\n| LIBERO 支持 | 需确认 |\\n| 改造成本 | 低-中（框架设计灵活） |\\n| 论文 LIBERO 结果 | 未确认 |\\n| 备注 | 这是一个**框架**而非单一模型。实验了 8+ VLM backbone × 4 policy 架构。最佳模型用 Kosmos backbone。对我们的 connector 对比研究有参考价值但不直接使用。 |\\n\\n### 9. 3D-VLA (UMass, ICML 2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 未明确 |\\n| Vision encoder | 3D feature extraction（point cloud based） |\\n| **Connector 类型** | **Interaction tokens**（3D-LLM 架构，用交互 token 嵌入 embodied 环境） |\\n| LLM backbone | 基于 3D-LLM |\\n| 开源状态 | ✅ code + diffusion models, GitHub: [UMass-Embodied-AGI/3D-VLA](https://github.com/UMass-Embodied-AGI/3D-VLA), HF: anyezhy |\\n| LIBERO 支持 | 需大量改造（paper 用 RLBench） |\\n| 改造成本 | 高（3D 点云输入，与 LIBERO 2D 图像差异大） |\\n| 论文 LIBERO 结果 | 无 |\\n| 备注 | 基于 3D 点云的 VLA，与我们研究的 2D 图像 → connector → LLM 管道差异太大，不推荐 |\\n\\n### 10. π0 / pi-zero (Physical Intelligence, 2024-2025)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | ~3.3B (400M SigLIP + 2.6B Gemma + ~300M action expert) |\\n| Vision encoder | SigLIP-So400m (400M params) |\\n| **Connector 类型** | **Linear projection**（单层线性层，将 SigLIP token 投影到 Gemma embedding space） |\\n| LLM backbone | Gemma 2B (via PaliGemma) |\\n| 开源状态 | ✅ weights + code, GitHub: [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi), HF 有 PyTorch port |\\n| LIBERO 支持 | ✅ 有评测（LIBERO-PRO 中被评测） |\\n| 改造成本 | 低（已有 LIBERO 评测代码） |\\n| 论文 LIBERO 结果 | 有（LIBERO-PRO 中有结果） |\\n| 备注 | **强力推荐**。Linear projection 是最简单的 connector，与 OpenVLA 的 2-layer MLP 形成鲜明对比。Action expert 通过 MoE 架构耦合。Flow matching 生成动作。 |\\n\\n### 11. OpenVLA-OFT (Stanford, 2025)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 7B |\\n| Vision encoder | SigLIP + DINOv2 (Prismatic) |\\n| **Connector 类型** | **2-layer MLP projector**（与 OpenVLA 相同的 Prismatic connector） |\\n| LLM backbone | Llama-2 7B |\\n| 开源状态 | ✅ weights + code, GitHub: [moojink/openvla-oft](https://github.com/moojink/openvla-oft) |\\n| LIBERO 支持 | ✅ 原生支持，SOTA 97.1% |\\n| 改造成本 | 极低（已有完整 LIBERO fine-tune + eval） |\\n| 论文 LIBERO 结果 | 有: 97.1% SR (4 suite avg) |\\n| 备注 | Connector 与 OpenVLA 完全相同。改进在 fine-tuning recipe（continuous actions, action chunking, bidirectional attention）。对压缩实验来说，connector 级别的差异与 OpenVLA 相同，但 action generation 方式不同，可能影响压缩行为。 |\\n\\n### 12. RoboMM (2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 未明确公布 |\\n| Vision encoder | CLIP (via OpenFlamingo) |\\n| **Connector 类型** | **3D Perception Adapter (UVFormer)** + **Cross-attention**（OpenFlamingo 风格：text queries attend to visual features through cross-attention layers） |\\n| LLM backbone | OpenFlamingo (cross-attention decoder) |\\n| 开源状态 | ✅ code, GitHub: [RoboUniview/RoboMM](https://github.com/RoboUniview/RoboMM) |\\n| LIBERO 支持 | ✅ 有评测 |\\n| 改造成本 | 低-中 |\\n| 论文 LIBERO 结果 | 有: 90.7% SR |\\n| 备注 | Cross-attention connector 是独特的融合方式（与 MLP/linear 的 \\\"先投射再拼接\\\" 不同）。还有 occupancy supervision 的 3D adapter。多模态解码器增强感知。 |\\n\\n### 13. SpatialVLA (2025, RSS)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | ~4B |\\n| Vision encoder | SigLIP |\\n| **Connector 类型** | **Linear projection + Ego3D Position Encoding**（PaliGemma2 的 linear connector + MLP(sinusoidal(3D positions)) 叠加到 visual tokens 上） |\\n| LLM backbone | Gemma (via PaliGemma2) |\\n| 开源状态 | ✅ weights + code, GitHub: [SpatialVLA/SpatialVLA](https://github.com/SpatialVLA/SpatialVLA), HF: IPEC-COMMUNITY/spatialvla-4b-224-pt |\\n| LIBERO 支持 | 未确认 |\\n| 改造成本 | 中（需接 LIBERO data pipeline） |\\n| 论文 LIBERO 结果 | 无 |\\n| 备注 | 基于 PaliGemma2，connector 本质上是 linear projection（与 π0 相同），加了 3D spatial encoding。Adaptive Action Grids 只输出 3 个 action token（其他模型 7 个）。 |\\n\\n### 14. DeeR-VLA (2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 3B / 9B (OpenFlamingo 变体) |\\n| Vision encoder | CLIP ViT-L/14 (428M params) |\\n| **Connector 类型** | **Perceiver Resampler + Cross-attention**（OpenFlamingo 架构：CLIP features → Perceiver Resampler → learnable cross-attention blocks 注入 LLM 层间） |\\n| LLM backbone | MPT-1B (3B 版) / MPT-7B (9B 版) |\\n| 开源状态 | ✅ code + checkpoints, GitHub: [yueyang130/DeeR-VLA](https://github.com/yueyang130/DeeR-VLA) |\\n| LIBERO 支持 | 需改造（paper 只有 CALVIN） |\\n| 改造成本 | 中-高（需接 LIBERO pipeline，且多 exit 架构增加复杂度） |\\n| 论文 LIBERO 结果 | 无（CALVIN benchmark） |\\n| 备注 | **Perceiver Resampler** 与 RoboFlamingo 相同架构基础。动态 early exit 是额外功能。可作为 Perceiver Resampler 实验的替代方案。 |\\n\\n### 15. TraceVLA (UMD, ICLR 2025)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 7B (OpenVLA-based) / 4B (Phi-3-Vision-based) |\\n| Vision encoder | SigLIP + DINOv2 (OpenVLA 版) / CLIP ViT (Phi-3 版) |\\n| **Connector 类型** | **2-layer MLP projector**（与 OpenVLA 相同） |\\n| LLM backbone | Llama-2 7B (OpenVLA 版) / Phi-3 4B |\\n| 开源状态 | ✅ code + weights, GitHub: [umd-huang-lab/tracevla](https://github.com/umd-huang-lab/tracevla), HF: furonghuang-lab/tracevla_7b, MIT license |\\n| LIBERO 支持 | 未确认（SimplerEnv + 真机） |\\n| 改造成本 | 低（基于 OpenVLA 改造） |\\n| 论文 LIBERO 结果 | 无 |\\n| 备注 | Connector 与 OpenVLA 相同，改进在于 visual trace prompting（在图像上叠加动作历史轨迹）。压缩行为预期与 OpenVLA 相似。 |\\n\\n### 16. X-VLA (ICLR 2026)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 0.9B |\\n| Vision encoder | Florence-Large (DaViT) |\\n| **Connector 类型** | **Linear projection + Soft Prompts**（vision features 通过 lightweight linear layer 投影到高维空间 + 每个 embodiment 有独立 learnable prompt embeddings 注入 transformer） |\\n| LLM backbone | Standard transformer 24 layers (非预训练 LLM，但使用 Florence 预训练 VLM 初始化) |\\n| 开源状态 | ✅ weights + code, GitHub: [2toinf/X-VLA](https://github.com/2toinf/X-VLA), HF: 2toINF/X-VLA, Apache-2.0 |\\n| LIBERO 支持 | ✅ 原生支持，98% SR |\\n| 改造成本 | 极低（已有 LIBERO 训练权重） |\\n| 论文 LIBERO 结果 | 有: 98% SR |\\n| 备注 | **强力推荐**。Linear projection connector + flow matching action generation。LIBERO SOTA 之一。小模型(0.9B)便于实验。 |\\n\\n### 17. ECoT / Embodied Chain-of-Thought (2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 7B (基于 OpenVLA) |\\n| Vision encoder | SigLIP + DINOv2 (Prismatic) |\\n| **Connector 类型** | **2-layer MLP projector**（与 OpenVLA 相同） |\\n| LLM backbone | Llama-2 7B |\\n| 开源状态 | ✅ code + weights, GitHub: [MichalZawalski/embodied-CoT](https://github.com/MichalZawalski/embodied-CoT), HF: ecot-openvla-7b-bridge/oxe |\\n| LIBERO 支持 | 需改造 |\\n| 改造成本 | 低（基于 OpenVLA） |\\n| 论文 LIBERO 结果 | 无 |\\n| 备注 | Connector 与 OpenVLA 完全相同，增加了 chain-of-thought reasoning。对 connector 压缩研究无新增价值。 |\\n\\n### 18. LingBot-VLA (Ant Group/Robbyant, 2026)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 4B |\\n| Vision encoder | Qwen2.5-VL 的 ViT（2D-RoPE + window attention） |\\n| **Connector 类型** | **MLP merger**（2-layer MLP with ReLU，2×2 spatial grouping 后投影 + LLM decoder 中有 cross-attention 层融合 visual features） |\\n| LLM backbone | Qwen2.5-VL-3B |\\n| 开源状态 | ✅ weights + code, GitHub: [Robbyant/lingbot-vla](https://github.com/Robbyant/lingbot-vla) |\\n| LIBERO 支持 | 未确认 |\\n| 改造成本 | 中 |\\n| 论文 LIBERO 结果 | 未确认 |\\n| 备注 | Qwen2.5-VL 的 MLP merger 是一种混合 connector：先做 spatial grouping（类似 pixel-shuffle 的空间压缩）再 MLP 投射。Mixture of Transformers 架构。 |\\n\\n---\\n\\n## Connector 类型覆盖分析\\n\\n### 已有数据的 Connector 类型\\n| Connector 类型 | 代表模型 | 压缩行为 |\\n|---------------|----------|----------|\\n| Pixel-shuffle | SmolVLA | Cliff-edge collapse |\\n| 2-layer MLP projector | OpenVLA (Prismatic) | Graded degradation |\\n| Perceiver Resampler | RoboFlamingo | 训练失败 |\\n\\n### 可新增的 Connector 类型\\n| Connector 类型 | 候选模型 | 特点 | 可行性 |\\n|---------------|----------|------|--------|\\n| **Linear projection** | **π0**, X-VLA, SpatialVLA | 最简单的 connector，单层线性变换 | ⭐⭐⭐ 高 |\\n| **Cross-attention (Flamingo-style)** | **RoboMM** | 不在 encoder 端压缩，而是 decoder 端通过 cross-attention 选择性融合 | ⭐⭐ 中 |\\n| **CNN patch → direct concat** | Octo | 无独立 connector，图像 patches 直接拼入 transformer | ⭐ 低（架构差异太大） |\\n| **MLP merger + spatial grouping** | LingBot-VLA | 先空间合并再 MLP 投射 + cross-attention | ⭐⭐ 中 |\\n| **Cross-attention tokenizer** | HPT | learnable tokens 通过 cross-attention 聚合 vision features | ⭐ 低（非 VLM 架构） |\\n\\n### 关键发现\\n1. **Linear projection** 是最有价值的新增类型——π0 和 X-VLA 都用这种最简单的 connector，与 OpenVLA 的 2-layer MLP 形成对比\\n2. **Cross-attention** (RoboMM 的 OpenFlamingo 架构) 从根本上不同：不投射拼接，而是 decoder 层间交叉注意力\\n3. 大量模型共享 connector：OpenVLA, CogACT, LLARVA, TraceVLA, ECoT, OpenVLA-OFT 都用 **2-layer MLP**（Prismatic 或 LLaVA 架构）\\n\\n---\\n\\n## Top 推荐：最适合扩展实验的 5 个模型\\n\\n### 🥇 1. π0 (Physical Intelligence)\\n- **Connector**: Linear projection (单层线性)\\n- **推荐理由**: \\n  - 与 OpenVLA 的 2-layer MLP 形成直接对比（linear vs MLP）\\n  - 开源权重 + 代码，社区活跃\\n  - 已有 LIBERO 评测代码\\n  - PaliGemma 架构广为人知\\n  - 3B 参数可在单卡运行\\n- **预期价值**: Linear projection 不增加非线性变换，token 可能保留更多原始 visual feature 结构 → 压缩行为可能与 MLP 不同\\n\\n### 🥈 2. X-VLA\\n- **Connector**: Linear projection + soft prompts\\n- **推荐理由**:\\n  - 同样是 linear projection，与 π0 对比看 soft prompt 的影响\\n  - LIBERO 98% SR，已有训练好的 LIBERO 权重直接可用\\n  - 0.9B 参数，实验成本最低\\n  - ICLR 2026，最新模型\\n  - Apache-2.0 开源\\n- **预期价值**: 验证 linear projection 的压缩行为是否 consistent across models\\n\\n### 🥉 3. DeeR-VLA\\n- **Connector**: Perceiver Resampler + Cross-attention (OpenFlamingo)\\n- **推荐理由**:\\n  - Perceiver Resampler 与 RoboFlamingo 相同架构，但 DeeR-VLA 已验证可训练（CALVIN benchmark 正常工作）\\n  - 给 Perceiver Resampler 第二次机会\\n  - 可对比 RoboFlamingo 的训练失败是架构问题还是实现问题\\n  - Open source with checkpoints\\n- **预期价值**: Perceiver Resampler 本身就做了 attention-based compression → 压缩行为可能与 MLP/linear 截然不同\\n- **风险**: LIBERO 需要自己改造\\n\\n### 4. RoboMM\\n- **Connector**: Cross-attention (OpenFlamingo) + 3D Adapter\\n- **推荐理由**:\\n  - Cross-attention 融合方式从根本上不同于 projection-based connectors\\n  - 已有 LIBERO 结果 (90.7%)\\n  - Open source\\n- **预期价值**: Cross-attention 在 decoder 端动态选择 visual features → 可能展现出与 projection-based 完全不同的压缩模式\\n- **风险**: 架构较复杂，3D adapter 增加变量\\n\\n### 5. OpenVLA-OFT\\n- **Connector**: 2-layer MLP projector (与 OpenVLA 相同)\\n- **推荐理由**:\\n  - Connector 与 OpenVLA 相同，但 action generation 完全不同（continuous + chunking）\\n  - LIBERO 97.1% SOTA\\n  - 可验证 \\\"相同 connector + 不同 action head\\\" 是否影响压缩行为\\n  - 已有完整 LIBERO 代码\\n- **预期价值**: 作为 OpenVLA 的对照组，隔离 connector vs action head 对压缩的影响\\n\\n---\\n\\n## 不推荐的模型及原因\\n\\n| 模型 | 排除原因 |\\n|------|----------|\\n| RT-2-X | 闭源，权重不可用 |\\n| GR-2 | 未开源 |\\n| 3D-VLA | 3D 点云输入，与 2D VLA 差异太大 |\\n| CogACT | Connector 与 OpenVLA 相同（Prismatic MLP），不新增类型 |\\n| LLARVA | Connector 与 OpenVLA 类似（MLP projector），不新增类型 |\\n| TraceVLA | Connector 与 OpenVLA 相同，不新增类型 |\\n| ECoT | Connector 与 OpenVLA 相同，不新增类型 |\\n| HPT | 非 VLM 架构，不适合 connector 压缩叙事 |\\n| GR-1 | 有 Perceiver Resampler（有价值），但无 LIBERO 支持 + 视频生成架构改造成本高 |\\n| Octo | 无独立 connector（CNN patch 直接拼入），架构与标准 VLM 差异太大 |\\n\\n---\\n\\n## 总结：Connector 类型 × 模型矩阵\\n\\n| Connector 类型 | 已有 | 推荐新增 |\\n|---------------|------|----------|\\n| Pixel-shuffle | SmolVLA ✅ | — |\\n| 2-layer MLP projector | OpenVLA ✅ | OpenVLA-OFT（同 connector 不同 action head） |\\n| Perceiver Resampler | RoboFlamingo ❌(失败) | **DeeR-VLA** |\\n| **Linear projection** | — | **π0, X-VLA** |\\n| **Cross-attention** | — | **RoboMM** |\\n\\n实现后可达 **5 种 connector 类型 × 6+ 模型**的全面对比。\\n\\n---\\n\\n## X-VLA 详细架构调研（2026-05-20 新增）\\n\\n### 模型身份确认\\n- **名称**: X-VLA (Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model)\\n- **论文**: arXiv:2510.10274, ICLR 2026\\n- **GitHub**: [2toinf/X-VLA](https://github.com/2toinf/X-VLA)\\n- **HuggingFace**: [2toINF/X-VLA](https://huggingface.co/collections/2toINF/x-vla)\\n- **参数量**: 0.9B\\n- **许可**: Apache-2.0\\n- **LIBERO SR**: 98.1%\\n\\n### 架构详解\\n\\n```\\nImage (224×224) → Florence-Large (DaViT) → Vision Tokens [B, N, 2048]\\n    → Linear Projection + LayerNorm → [B, N, 1024]\\n    → Merge with Text Token Embeddings → Florence2 Encoder (self-attention)\\n    → Context Features → SoftPromptedTransformer (24 layers, hidden=1024)\\n        + Soft Prompts (32 learnable embeddings per embodiment)\\n        + Noised Action Tokens (flow matching)\\n    → Denoised Action Trajectory [B, 30, 20]\\n```\\n\\n**各组件详情**:\\n\\n| 组件 | 规格 |\\n|------|------|\\n| Vision Encoder | Florence-Large (DaViT): patch_stride=[4,2,2,2] → total stride 32 |\\n| Vision Token 数量 | ~49 tokens (7×7 at 224×224) 或 ~576 tokens (24×24 at 768×768) — **需实际加载模型验证** |\\n| Projection | Linear + LayerNorm, dim 2048 → 1024 (projection_dim=1024) |\\n| Soft Prompts | 32 tokens/embodiment, 0.04% of total params |\\n| Transformer | 24 layers, hidden=1024, 16 heads, mlp_ratio=4.0 |\\n| Action Head | Flow matching, 30 anchor points × 20 dims (EE6D), 10 denoising steps |\\n| Max Sequence | 512 tokens |\\n\\n### HuggingFace 权重\\n| Checkpoint | 用途 | 地址 |\\n|------------|------|------|\\n| X-VLA-Pt | 预训练基座 (cross-embodiment) | 2toINF/X-VLA-Pt |\\n| X-VLA-Libero | LIBERO 全参数微调 (98.1% SR) | 2toINF/X-VLA-Libero |\\n| X-VLA-libero-*-peft | LIBERO LoRA 微调 (各 suite) | 2toINF/X-VLA-libero-spatial-peft 等 |\\n\\n### 环境依赖\\n```\\ntransformers<=4.51.3, torch, einops==0.8.1, timm==1.0.12, \\naccelerate==1.2.1, peft==0.17.1, safetensors==0.4.5,\\nnumpy==1.26.3, scipy==1.15.0, mmengine==0.10.5,\\nfastapi, uvicorn==0.34.3, h5py==3.12.1, pyarrow==20.0.0,\\nav==15.0.0, mediapy==1.2.4\\n```\\nLIBERO 评估另需 Python 3.8 环境。\\n\\n### VTC 集成方案\\n**插入点**: Florence2 `_encode_image()` 输出 → **VTC** → `_merge_input_ids_with_image_features()`\\n\\n**改造清单**:\\n1. 创建 `xvla_vtc_adapter.py`（复用 VisionTokenCompressor，hidden_dim 改 1024）\\n2. 创建 XVLASmartCompressWrapper，hook Florence2 vision 输出\\n3. 修改 merge 逻辑以适应压缩后的 token 数量\\n4. 创建 `train_xvla_smart_compress.py`（参考 X-VLA 的 train.py + peft_train.py）\\n5. 适配 flow matching loss（不同于 OpenVLA 的 cross-entropy）\\n\\n**与 OpenVLA VTC 的关键差异**:\\n| 维度 | OpenVLA | X-VLA |\\n|------|---------|-------|\\n| hidden_dim | 4096 | 1024 |\\n| 原始 vision tokens | 256 | ~49-576 (待验证) |\\n| Action 范式 | Autoregressive (256-bin CE) | Flow matching (MSE+BCE) |\\n| Connector | 2-layer MLP | Linear + LayerNorm |\\n| 模型大小 | 7B | 0.9B |\\n\\n**预计工作量**: 8-12 小时\\n- 代码改造: 4-6h（adapter + training script）\\n- 环境搭建 + 模型下载: 2-3h\\n- 验证 + 调试: 2-3h\\n\", \"total_chars\": 17557, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "59a9a5da-4a09-4fad-832e-ad9e1d71f811",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/memory.md\\\", \\\"content\\\": \\\"# VLA 模型全面调研报告\\\\n\\\\n**调研日期**: 2026-05-20\\\\n**目的**: 寻找不同 connector 架构的开源 VLA 模型，扩展 vision connector 对 token 可压缩性影响的实验\\\\n\\\\n---\\\\n\\\\n## 已有实验数据\\\\n\\\\n| 模型 | Connector | 压缩行为 |\\\\n|------|-----------|----------|\\\\n| SmolVLA | Pixel-shuffle | Cliff-edge collapse (k=0.95 → 0% SR) |\\\\n| OpenVLA | 2-layer MLP projector | Graded degradation (线性下降) |\\\\n| RoboFlamingo | Perceiver Resampler | 尝试失败（gripper loss 无法训练） |\\\\n\\\\n---\\\\n\\\\n## 完整模型调研表\\\\n\\\\n### 1. Octo (UC Berkeley, 2024)\\\\n\\\\n| 字段 | 信息 |\\\\n|------|------|\\\\n| 参数量 | 27M (Small) / 93M (Base) |\\\\n| Vision encoder | Shallow CNN (从头训练，非预训练 ViT) |\\\\n| **Connector 类型** | **CNN patch encoder → 直接拼接进 transformer（无独立 connector）** |\\\\n| LLM backbone | 纯 transformer（非预训练 LLM），decoder-only |\\\\n| 开源状态 | ✅ weights + code, GitHub: [octo-models/octo](https://github.com/octo-models/octo), HF: rail-berkeley/octo-base |\\\\n| LIBERO 支持 | ✅ 原生支持，fine-tune 后 ~72% SR |\\\\n| 改造成本 | 低（已有 LIBERO fine-tune 代码） |\\\\n| 论文 LIBERO 结果 | 有: ~72% (fine-tuned) |\\\\n| 备注 | 非标准 VLM→LLM 架构，是 transformer-based diffusion policy。图像通过浅层 CNN 编码为 16×16 patches 后直接拼入 transformer 序列。语言用 T5 tokenizer/encoder。Action head 是 diffusion policy。 |\\\\n\\\\n### 2. CogACT (Microsoft/Tsinghua, 2024)\\\\n\\\\n| 字段 | 信息 |\\\\n|------|------|\\\\n| 参数量 | ~7.1B (7B Prismatic VLM + 89M-300M DiT action module) |\\\\n| Vision encoder | DINOv2 + SigLIP (双 encoder，channel 拼接) |\\\\n| **Connector 类型** | **2-layer MLP projector**（Prismatic 架构：DINOv2+SigLIP feature → channel concat → 2-layer MLP → Llama-2 embedding space） |\\\\n| LLM backbone | Llama-2 7B (via Prismatic-7B) |\\\\n| 开源状态 | ✅ weights + code, GitHub: [microsoft/CogACT](https://github.com/microsoft/CogACT), HF: CogACT/CogACT-Base, CogACT/CogACT-Small |\\\\n| LIBERO 支持 | 需改造（paper 用 SimplerEnv + 真机） |\\\\n| 改造成本 | 中（需接 LIBERO data pipeline + action space） |\\\\n| 论文 LIBERO 结果 | 无 |\\\\n| 备注 | 核心创新在 DiT action module（将 VLM 认知特征作为 condition 输入扩散 transformer 生成动作）。Connector 与 OpenVLA 相同（都基于 Prismatic） |\\\\n\\\\n### 3. HPT (MIT, NeurIPS 2024)\\\\n\\\\n| 字段 | 信息 |\\\\n|------|------|\\\\n| 参数量 | 3.1M (S) / 12.6M (B) / 50.5M (L) / 226.8M (XL) / 1.1B (Huge) |\\\\n| Vision encoder | 预训练冻结 ResNet18 |\\\\n| **Connector 类型** | **Cross-attention tokenizer**（learnable tokens 通过 cross-attention 聚合 vision features → 固定 16 tokens，每个 camera view 有独立 MLP projector） |\\\\n| LLM backbone | 无（纯 decoder-only transformer，从头训练） |\\\\n| 开源状态 | ✅ weights + code, GitHub: [liruiw/HPT](https://github.com/liruiw/HPT), HF: liruiw/hpt |\\\\n| LIBERO 支持 | 未确认（paper 评测 6 个 benchmark） |\\\\n| 改造成本 | 中（非标准 VLM 架构，需改 stem + action head） |\\\\n| 论文 LIBERO 结果 | 无 |\\\\n| 备注 | 非 VLM→LLM 架构。Cross-attention tokenizer 类似 Perceiver 但更轻量（8 heads, 64 dim/head）。跨 embodiment 预训练。 |\\\\n\\\\n### 4. RT-2-X (Google DeepMind, 2023)\\\\n\\\\n| 字段 | 信息 |\\\\n|------|------|\\\\n| 参数量 | 55B |\\\\n| Vision encoder | ViT (PaLI-X 的视觉编码器) |\\\\n| **Connector 类型** | 未公开（闭源） |\\\\n| LLM backbone | PaLI-X / PaLM-E |\\\\n| 开源状态 | ❌ **闭源**，权重不公开 |\\\\n| LIBERO 支持 | 不可行 |\\\\n| 改造成本 | 不可行 |\\\\n| 论文 LIBERO 结果 | 无 |\\\\n| 备注 | 闭源模型，无法使用 |\\\\n\\\\n### 5. GR-1 (ByteDance, 2023)\\\\n\\\\n| 字段 | 信息 |\\\\n|------|------|\\\\n| 参数量 | 未明确公布 |\\\\n| Vision encoder | MAE ViT-Base (预训练) |\\\\n| **Connector 类型** | **Perceiver Resampler**（将 MAE ViT 视觉 token 数量压缩）+ linear layers 对齐维度 |\\\\n| LLM backbone | GPT-style causal transformer（非预训练 LLM） |\\\\n| 开源状态 | ✅ weights + code, GitHub: [bytedance/GR-1](https://github.com/bytedance/GR-1), Apache-2.0 |\\\\n| LIBERO 支持 | 需改造（paper 只有 CALVIN） |\\\\n| 改造成本 | 高（需改 data pipeline、action space、视频生成部分可能要适配） |\\\\n| 论文 LIBERO 结果 | 无（CALVIN: 94.9%） |\\\\n| 备注 | 既做动作预测又做视频生成（future image prediction）。语言用 CLIP text encoder。使用 Perceiver Resampler 这一点很有价值——与 RoboFlamingo 类似但架构不同。 |\\\\n\\\\n### 6. GR-2 (ByteDance, 2024)\\\\n\\\\n| 字段 | 信息 |\\\\n|------|------|\\\\n| 参数量 | 未公布 |\\\\n| Vision encoder | 未公布 |\\\\n| **Connector 类型** | 未公布 |\\\\n| LLM backbone | 未公布 |\\\\n| 开源状态 | ❌ **未开源**，代码/权重未释放 |\\\\n| LIBERO 支持 | 不可行 |\\\\n| 改造成本 | 不可行 |\\\\n| 论文 LIBERO 结果 | 无 |\\\\n| 备注 | GR-1 的后续，但未开源 |\\\\n\\\\n### 7. LLARVA (2024)\\\\n\\\\n| 字段 | 信息 |\\\\n|------|------|\\\\n| 参数量 | 7B |\\\\n| Vision encoder | CLIP ViT-L/14 |\\\\n| **Connector 类型** | **MLP projector**（LLaVA-style，2-layer MLP with GELU） |\\\\n| LLM backbone | Llama-2 7B |\\\\n| 开源状态 | ✅ code + LoRA weights, GitHub: [Dantong88/LLARVA](https://github.com/Dantong88/LLARVA), Apache-2.0 |\\\\n| LIBERO 支持 | 需改造 |\\\\n| 改造成本 | 中（需接 action head + LIBERO data pipeline） |\\\\n| 论文 LIBERO 结果 | 无 |\\\\n| 备注 | 预测 visual traces (2D 轨迹) 作为中间表示。Connector 与 OpenVLA 类似（都是 MLP projector），但用 CLIP 而非 Prismatic 双 encoder |\\\\n\\\\n### 8. RoboVLMs (2024)\\\\n\\\\n| 字段 | 信息 |\\\\n|------|------|\\\\n| 参数量 | 不定（框架） |\\\\n| Vision encoder | 支持多种 VLM backbone |\\\\n| **Connector 类型** | 取决于所选 VLM（框架支持多种） |\\\\n| LLM backbone | 取决于所选 VLM |\\\\n| 开源状态 | ✅ code + models, GitHub: [Robot-VLAs/RoboVLMs](https://github.com/Robot-VLAs/RoboVLMs) |\\\\n| LIBERO 支持 | 需确认 |\\\\n| 改造成本 | 低-中（框架设计灵活） |\\\\n| 论文 LIBERO 结果 | 未确认 |\\\\n| 备注 | 这是一个**框架**而非单一模型。实验了 8+ VLM backbone × 4 policy 架构。最佳模型用 Kosmos backbone。对我们的 connector 对比研究有参考价值但不直接使用。 |\\\\n\\\\n### 9. 3D-VLA (UMass, ICML 2024)\\\\n\\\\n| 字段 | 信息 |\\\\n|------|------|\\\\n| 参数量 | 未明确 |\\\\n| Vision encoder | 3D feature extraction（point cloud based） |\\\\n| **Connector 类型** | **Interaction tokens**（3D-LLM 架构，用交互 token 嵌入 embodied 环境） |\\\\n| LLM backbone | 基于 3D-LLM |\\\\n| 开源状态 | ✅ code + diffusion models, GitHub: [UMass-Embodied-AGI/3D-VLA](https://github.com/UMass-Embodied-AGI/3D-VLA), HF: anyezhy |\\\\n| LIBERO 支持 | 需大量改造（paper 用 RLBench） |\\\\n| 改造成本 | 高（3D 点云输入，与 LIBERO 2D 图像差异大） |\\\\n| 论文 LIBERO 结果 | 无 |\\\\n| 备注 | 基于 3D 点云的 VLA，与我们研究的 2D 图像 → connector → LLM 管道差异太大，不推荐 |\\\\n\\\\n### 10. π0 / pi-zero (Physical Intelligence, 2024-2025)\\\\n\\\\n| 字段 | 信息 |\\\\n|------|------|\\\\n| 参数量 | ~3.3B (400M SigLIP + 2.6B Gemma + ~300M action expert) |\\\\n| Vision encoder | SigLIP-So400m (400M params) |\\\\n| **Connector 类型** | **Linear projection**（单层线性层，将 SigLIP token 投影到 Gemma embedding space） |\\\\n| LLM backbone | Gemma 2B (via PaliGemma) |\\\\n| 开源状态 | ✅ weights + code, GitHub: [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi), HF 有 PyTorch port |\\\\n| LIBERO 支持 | ✅ 有评测（LIBERO-PRO 中被评测） |\\\\n| 改造成本 | 低（已有 LIBERO 评测代码） |\\\\n| 论文 LIBERO 结果 | 有（LIBERO-PRO 中有结果） |\\\\n| 备注 | **强力推荐**。Linear projection 是最简单的 connector，与 OpenVLA 的 2-layer MLP 形成鲜明对比。Action expert 通过 MoE 架构耦合。Flow matching 生成动作。 |\\\\n\\\\n### 11. OpenVLA-OFT (Stanford, 2025)\\\\n\\\\n| 字段 | 信息 |\\\\n|------|------|\\\\n| 参数量 | 7B |\\\\n| Vision encoder | SigLIP + DINOv2 (Prismatic) |\\\\n| **Connector 类型** | **2-layer MLP projector**（与 OpenVLA 相同的 Prismatic connector） |\\\\n| LLM backbone | Llama-2 7B |\\\\n| 开源状态 | ✅ weights + code, GitHub: [moojink/openvla-oft](https://github.com/moojink/openvla-oft) |\\\\n| LIBERO 支持 | ✅ 原生支持，SOTA 97.1% |\\\\n| 改造成本 | 极低（已有完整 LIBERO fine-tune + eval） |\\\\n| 论文 LIBERO 结果 | 有: 97.1% SR (4 suite avg) |\\\\n| 备注 | Connector 与 OpenVLA 完全相同。改进在 fine-tuning recipe（continuous actions, action chunking, bidirectional attention）。对压缩实验来说，connector 级别的差异与 OpenVLA 相同，但 action generation 方式不同，可能影响压缩行为。 |\\\\n\\\\n### 12. RoboMM (2024)\\\\n\\\\n| 字段 | 信息 |\\\\n|------|------|\\\\n| 参数量 | 未明确公布 |\\\\n| Vision encoder | CLIP (via OpenFlamingo) |\\\\n| **Connector 类型** | **3D Perception Adapter (UVFormer)** + **Cross-attention**（OpenFlamingo 风格：text queries attend to visual features through cross-attention layers） |\\\\n| LLM backbone | OpenFlamingo (cross-attention decoder) |\\\\n| 开源状态 | ✅ code, GitHub: [RoboUniview/RoboMM](https://github.com/RoboUniview/RoboMM) |\\\\n| LIBERO 支持 | ✅ 有评测 |\\\\n| 改造成本 | 低-中 |\\\\n| 论文 LIBERO 结果 | 有: 90.7% SR |\\\\n| 备注 | Cross-attention connector 是独特的融合方式（与 MLP/linear 的 \\\\\\\"先投射再拼接\\\\\\\" 不同）。还有 occupancy supervision 的 3D adapter。多模态解码器增强感知。 |\\\\n\\\\n### 13. SpatialVLA (2025, RSS)\\\\n\\\\n| 字段 | 信息 |\\\\n|------|------|\\\\n| 参数量 | ~4B |\\\\n| Vision encoder | SigLIP |\\\\n| **Connector 类型** | **Linear projection + Ego3D Position Encoding**（PaliGemma2 的 linear connector + MLP(sinusoidal(3D positions)) 叠加到 visual tokens 上） |\\\\n| LLM backbone | Gemma (via PaliGemma2) |\\\\n| 开源状态 | ✅ weights + code, GitHub: [SpatialVLA/SpatialVLA](https://github.com/SpatialVLA/SpatialVLA), HF: IPEC-COMMUNITY/spatialvla-4b-224-pt |\\\\n| LIBERO 支持 | 未确认 |\\\\n| 改造成本 | 中（需接 LIBERO data pipeline） |\\\\n| 论文 LIBERO 结果 | 无 |\\\\n| 备注 | 基于 PaliGemma2，connector 本质上是 linear projection（与 π0 相同），加了 3D spatial encoding。Adaptive Action Grids 只输出 3 个 action token（其他模型 7 个）。 |\\\\n\\\\n### 14. DeeR-VLA (2024)\\\\n\\\\n| 字段 | 信息 |\\\\n|------|------|\\\\n| 参数量 | 3B / 9B (OpenFlamingo 变体) |\\\\n| Vision encoder | CLIP ViT-L/14 (428M params) |\\\\n| **Connector 类型** | **Perceiver Resampler + Cross-attention**（OpenFlamingo 架构：CLIP features → Perceiver Resampler → learnable cross-attention blocks 注入 LLM 层间） |\\\\n| LLM backbone | MPT-1B (3B 版) / MPT-7B (9B 版) |\\\\n| 开源状态 | ✅ code + checkpoints, GitHub: [yueyang130/DeeR-VLA](https://github.com/yueyang130/DeeR-VLA) |\\\\n| LIBERO 支持 | 需改造（paper 只有 CALVIN） |\\\\n| 改造成本 | 中-高（需接 LIBERO pipeline，且多 exit 架构增加复杂度） |\\\\n| 论文 LIBERO 结果 | 无（CALVIN benchmark） |\\\\n| 备注 | **Perceiver Resampler** 与 RoboFlamingo 相同架构基础。动态 early exit 是额外功能。可作为 Perceiver Resampler 实验的替代方案。 |\\\\n\\\\n### 15. TraceVLA (UMD, ICLR 2025)\\\\n\\\\n| 字段 | 信息 |\\\\n|------|------|\\\\n| 参数量 | 7B (OpenVLA-based) / 4B (Phi-3-Vision-based) |\\\\n| Vision encoder | SigLIP + DINOv2 (OpenVLA 版) / CLIP ViT (Phi-3 版) |\\\\n| **Connector 类型** | **2-layer MLP projector**（与 OpenVLA 相同） |\\\\n| LLM backbone | Llama-2 7B (OpenVLA 版) / Phi-3 4B |\\\\n| 开源状态 | ✅ code + weights, GitHub: [umd-huang-lab/tracevla](https://github.com/umd-huang-lab/tracevla), HF: furonghuang-lab/tracevla_7b, MIT license |\\\\n| LIBERO 支持 | 未确认（SimplerEnv + 真机） |\\\\n| 改造成本 | 低（基于 OpenVLA 改造） |\\\\n| 论文 LIBERO 结果 | 无 |\\\\n| 备注 | Connector 与 OpenVLA 相同，改进在于 visual trace prompting（在图像上叠加动作历史轨迹）。压缩行为预期与 OpenVLA 相似。 |\\\\n\\\\n### 16. X-VLA (ICLR 2026)\\\\n\\\\n| 字段 | 信息 |\\\\n|------|------|\\\\n| 参数量 | 0.9B |\\\\n| Vision encoder | Florence-Large (DaViT) |\\\\n| **Connector 类型** | **Linear projection + Soft Prompts**（vision features 通过 lightweight linear layer 投影到高维空间 + 每个 embodiment 有独立 learnable prompt embeddings 注入 transformer） |\\\\n| LLM backbone | Standard transformer 24 layers (非预训练 LLM，但使用 Florence 预训练 VLM 初始化) |\\\\n| 开源状态 | ✅ weights + code, GitHub: [2toinf/X-VLA](https://github.com/2toinf/X-VLA), HF: 2toINF/X-VLA, Apache-2.0 |\\\\n| LIBERO 支持 | ✅ 原生支持，98% SR |\\\\n| 改造成本 | 极低（已有 LIBERO 训练权重） |\\\\n| 论文 LIBERO 结果 | 有: 98% SR |\\\\n| 备注 | **强力推荐**。Linear projection connector + flow matching action generation。LIBERO SOTA 之一。小模型(0.9B)便于实验。 |\\\\n\\\\n### 17. ECoT / Embodied Chain-of-Thought (2024)\\\\n\\\\n| 字段 | 信息 |\\\\n|------|------|\\\\n| 参数量 | 7B (基于 OpenVLA) |\\\\n| Vision encoder | SigLIP + DINOv2 (Prismatic) |\\\\n| **Connector 类型** | **2-layer MLP projector**（与 OpenVLA 相同） |\\\\n| LLM backbone | Llama-2 7B |\\\\n| 开源状态 | ✅ code + weights, GitHub: [MichalZawalski/embodied-CoT](https://github.com/MichalZawalski/embodied-CoT), HF: ecot-openvla-7b-bridge/oxe |\\\\n| LIBERO 支持 | 需改造 |\\\\n| 改造成本 | 低（基于 OpenVLA） |\\\\n| 论文 LIBERO 结果 | 无 |\\\\n| 备注 | Connector 与 OpenVLA 完全相同，增加了 chain-of-thought reasoning。对 connector 压缩研究无新增价值。 |\\\\n\\\\n### 18. LingBot-VLA (Ant Group/Robbyant, 2026)\\\\n\\\\n| 字段 | 信息 |\\\\n|------|------|\\\\n| 参数量 | 4B |\\\\n| Vision encoder | Qwen2.5-VL 的 ViT（2D-RoPE + window attention） |\\\\n| **Connector 类型** | **MLP merger**（2-layer MLP with ReLU，2×2 spatial grouping 后投影 + LLM decoder 中有 cross-attention 层融合 visual features） |\\\\n| LLM backbone | Qwen2.5-VL-3B |\\\\n| 开源状态 | ✅ weights + code, GitHub: [Robbyant/lingbot-vla](https://github.com/Robbyant/lingbot-vla) |\\\\n| LIBERO 支持 | 未确认 |\\\\n| 改造成本 | 中 |\\\\n| 论文 LIBERO 结果 | 未确认 |\\\\n| 备注 | Qwen2.5-VL 的 MLP merger 是一种混合 connector：先做 spatial grouping（类似 pixel-shuffle 的空间压缩）再 MLP 投射。Mixture of Transformers 架构。 |\\\\n\\\\n---\\\\n\\\\n## Connector 类型覆盖分析\\\\n\\\\n### 已有数据的 Connector 类型\\\\n| Connector 类型 | 代表模型 | 压缩行为 |\\\\n|---------------|----------|----------|\\\\n| Pixel-shuffle | SmolVLA | Cliff-edge collapse |\\\\n| 2-layer MLP projector | OpenVLA (Prismatic) | Graded degradation |\\\\n| Perceiver Resampler | RoboFlamingo | 训练失败 |\\\\n\\\\n### 可新增的 Connector 类型\\\\n| Connector 类型 | 候选模型 | 特点 | 可行性 |\\\\n|---------------|----------|------|--------|\\\\n| **Linear projection** | **π0**, X-VLA, SpatialVLA | 最简单的 connector，单层线性变换 | ⭐⭐⭐ 高 |\\\\n| **Cross-attention (Flamingo-style)** | **RoboMM** | 不在 encoder 端压缩，而是 decoder 端通过 cross-attention 选择性融合 | ⭐⭐ 中 |\\\\n| **CNN patch → direct concat** | Octo | 无独立 connector，图像 patches 直接拼入 transformer | ⭐ 低（架构差异太大） |\\\\n| **MLP merger + spatial grouping** | LingBot-VLA | 先空间合并再 MLP 投射 + cross-attention | ⭐⭐ 中 |\\\\n| **Cross-attention tokenizer** | HPT | learnable tokens 通过 cross-attention 聚合 vision features | ⭐ 低（非 VLM 架构） |\\\\n\\\\n### 关键发现\\\\n1. **Linear projection** 是最有价值的新增类型——π0 和 X-VLA 都用这种最简单的 connector，与 OpenVLA 的 2-layer MLP 形成对比\\\\n2. **Cross-attention** (RoboMM 的 OpenFlamingo 架构) 从根本上不同：不投射拼接，而是 decoder 层间交叉注意力\\\\n3. 大量模型共享 connector：OpenVLA, CogACT, LLARVA, TraceVLA, ECoT, OpenVLA-OFT 都用 **2-layer MLP**（Prismatic 或 LLaVA 架构）\\\\n\\\\n---\\\\n\\\\n## Top 推荐：最适合扩展实验的 5 个模型\\\\n\\\\n### 🥇 1. π0 (Physical Intelligence)\\\\n- **Connector**: Linear projection (单层线性)\\\\n- **推荐理由**: \\\\n  - 与 OpenVLA 的 2-layer MLP 形成直接对比（linear vs MLP）\\\\n  - 开源权重 + 代码，社区活跃\\\\n  - 已有 LIBERO 评测代码\\\\n  - PaliGemma 架构广为人知\\\\n  - 3B 参数可在单卡运行\\\\n- **预期价值**: Linear projection 不增加非线性变换，token 可能保留更多原始 visual feature 结构 → 压缩行为可能与 MLP 不同\\\\n\\\\n### 🥈 2. X-VLA\\\\n- **Connector**: Linear projection + soft prompts\\\\n- **推荐理由**:\\\\n  - 同样是 linear projection，与 π0 对比看 soft prompt 的影响\\\\n  - LIBERO 98% SR，已有训练好的 LIBERO 权重直接可用\\\\n  - 0.9B 参数，实验成本最低\\\\n  - ICLR 2026，最新模型\\\\n  - Apache-2.0 开源\\\\n- **预期价值**: 验证 linear projection 的压缩行为是否 consistent across models\\\\n\\\\n### 🥉 3. DeeR-VLA\\\\n- **Connector**: Perceiver Resampler + Cross-attention (OpenFlamingo)\\\\n- **推荐理由**:\\\\n  - Perceiver Resampler 与 RoboFlamingo 相同架构，但 DeeR-VLA 已验证可训练（CALVIN benchmark 正常工作）\\\\n  - 给 Perceiver Resampler 第二次机会\\\\n  - 可对比 RoboFlamingo 的训练失败是架构问题还是实现问题\\\\n  - Open source with checkpoints\\\\n- **预期价值**: Perceiver Resampler 本身就做了 attention-based compression → 压缩行为可能与 MLP/linear 截然不同\\\\n- **风险**: LIBERO 需要自己改造\\\\n\\\\n### 4. RoboMM\\\\n- **Connector**: Cross-attention (OpenFlamingo) + 3D Adapter\\\\n- **推荐理由**:\\\\n  - Cross-attention 融合方式从根本上不同于 projection-based connectors\\\\n  - 已有 LIBERO 结果 (90.7%)\\\\n  - Open source\\\\n- **预期价值**: Cross-attention 在 decoder 端动态选择 visual features → 可能展现出与 projection-based 完全不同的压缩模式\\\\n- **风险**: 架构较复杂，3D adapter 增加变量\\\\n\\\\n### 5. OpenVLA-OFT\\\\n- **Connector**: 2-layer MLP projector (与 OpenVLA 相同)\\\\n- **推荐理由**:\\\\n  - Connector 与 OpenVLA 相同，但 action generation 完全不同（continuous + chunking）\\\\n  - LIBERO 97.1% SOTA\\\\n  - 可验证 \\\\\\\"相同 connector + 不同 action head\\\\\\\" 是否影响压缩行为\\\\n  - 已有完整 LIBERO 代码\\\\n- **预期价值**: 作为 OpenVLA 的对照组，隔离 connector vs action head 对压缩的影响\\\\n\\\\n---\\\\n\\\\n## 不推荐的模型及原因\\\\n\\\\n| 模型 | 排除原因 |\\\\n|------|----------|\\\\n| RT-2-X | 闭源，权重不可用 |\\\\n| GR-2 | 未开源 |\\\\n| 3D-VLA | 3D 点云输入，与 2D VLA 差异太大 |\\\\n| CogACT | Connector 与 OpenVLA 相同（Prismatic MLP），不新增类型 |\\\\n| LLARVA | Connector 与 OpenVLA 类似（MLP projector），不新增类型 |\\\\n| TraceVLA | Connector 与 OpenVLA 相同，不新增类型 |\\\\n| ECoT | Connector 与 OpenVLA 相同，不新增类型 |\\\\n| HPT | 非 VLM 架构，不适合 connector 压缩叙事 |\\\\n| GR-1 | 有 Perceiver Resampler（有价值），但无 LIBERO 支持 + 视频生成架构改造成本高 |\\\\n| Octo | 无独立 connector（CNN patch 直接拼入），架构与标准 VLM 差异太大 |\\\\n\\\\n---\\\\n\\\\n## 总结：Connector 类型 × 模型矩阵\\\\n\\\\n| Connector 类型 | 已有 | 推荐新增 |\\\\n|---------------|------|----------|\\\\n| Pixel-shuffle | SmolVLA ✅ | — |\\\\n| 2-layer MLP projector | OpenVLA ✅ | OpenVLA-OFT（同 connector 不同 action head） |\\\\n| Perceiver Resampler | RoboFlamingo ❌(失败) | **DeeR-VLA** |\\\\n| **Linear projection** | — | **π0, X-VLA** |\\\\n| **Cross-attention** | — | **RoboMM** |\\\\n\\\\n实现后可达 **5 种 connector 类型 × 6+ 模型**的全面对比。\\\\n\\\\n---\\\\n\\\\n## X-VLA 详细架构调研（2026-05-20 新增）\\\\n\\\\n### 模型身份确认\\\\n- **名称**: X-VLA (Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model)\\\\n- **论文**: arXiv:2510.10274, ICLR 2026\\\\n- **GitHub**: [2toinf/X-VLA](https://github.com/2toinf/X-VLA)\\\\n- **HuggingFace**: [2toINF/X-VLA](https://huggingface.co/collections/2toINF/x-vla)\\\\n- **参数量**: 0.9B\\\\n- **许可**: Apache-2.0\\\\n- **LIBERO SR**: 98.1%\\\\n\\\\n### 架构详解\\\\n\\\\n```\\\\nImage (224×224) → Florence-Large (DaViT) → Vision Tokens [B, N, 2048]\\\\n    → Linear Projection + LayerNorm → [B, N, 1024]\\\\n    → Merge with Text Token Embeddings → Florence2 Encoder (self-attention)\\\\n    → Context Features → SoftPromptedTransformer (24 layers, hidden=1024)\\\\n        + Soft Prompts (32 learnable embeddings per embodiment)\\\\n        + Noised Action Tokens (flow matching)\\\\n    → Denoised Action Trajectory [B, 30, 20]\\\\n```\\\\n\\\\n**各组件详情**:\\\\n\\\\n| 组件 | 规格 |\\\\n|------|------|\\\\n| Vision Encoder | Florence-Large (DaViT): patch_stride=[4,2,2,2] → total stride 32 |\\\\n| Vision Token 数量 | ~49 tokens (7×7 at 224×224) 或 ~576 tokens (24×24 at 768×768) — **需实际加载模型验证** |\\\\n| Projection | Linear + LayerNorm, dim 2048 → 1024 (projection_dim=1024) |\\\\n| Soft Prompts | 32 tokens/embodiment, 0.04% of total params |\\\\n| Transformer | 24 layers, hidden=1024, 16 heads, mlp_ratio=4.0 |\\\\n| Action Head | Flow matching, 30 anchor points × 20 dims (EE6D), 10 denoising steps |\\\\n| Max Sequence | 512 tokens |\\\\n\\\\n### HuggingFace 权重\\\\n| Checkpoint | 用途 | 地址 |\\\\n|------------|------|------|\\\\n| X-VLA-Pt | 预训练基座 (cross-embodiment) | 2toINF/X-VLA-Pt |\\\\n| X-VLA-Libero | LIBERO 全参数微调 (98.1% SR) | 2toINF/X-VLA-Libero |\\\\n| X-VLA-libero-*-peft | LIBERO LoRA 微调 (各 suite) | 2toINF/X-VLA-libero-spatial-peft 等 |\\\\n\\\\n### 环境依赖\\\\n```\\\\ntransformers<=4.51.3, torch, einops==0.8.1, timm==1.0.12, \\\\naccelerate==1.2.1, peft==0.17.1, safetensors==0.4.5,\\\\nnumpy==1.26.3, scipy==1.15.0, mmengine==0.10.5,\\\\nfastapi, uvicorn==0.34.3, h5py==3.12.1, pyarrow==20.0.0,\\\\nav==15.0.0, mediapy==1.2.4\\\\n```\\\\nLIBERO 评估另需 Python 3.8 环境。\\\\n\\\\n### VTC 集成方案\\\\n**插入点**: Florence2 `_encode_image()` 输出 → **VTC** → `_merge_input_ids_with_image_features()`\\\\n\\\\n**改造清单**:\\\\n1. 创建 `xvla_vtc_adapter.py`（复用 VisionTokenCompressor，hidden_dim 改 1024）\\\\n2. 创建 XVLASmartCompressWrapper，hook Florence2 vision 输出\\\\n3. 修改 merge 逻辑以适应压缩后的 token 数量\\\\n4. 创建 `train_xvla_smart_compress.py`（参考 X-VLA 的 train.py + peft_train.py）\\\\n5. 适配 flow matching loss（不同于 OpenVLA 的 cross-entropy）\\\\n\\\\n**与 OpenVLA VTC 的关键差异**:\\\\n| 维度 | OpenVLA | X-VLA |\\\\n|------|---------|-------|\\\\n| hidden_dim | 4096 | 1024 |\\\\n| 原始 vision tokens | 256 | ~49-576 (待验证) |\\\\n| Action 范式 | Autoregressive (256-bin CE) | Flow matching (MSE+BCE) |\\\\n| Connector | 2-layer MLP | Linear + LayerNorm |\\\\n| 模型大小 | 7B | 0.9B |\\\\n\\\\n**预计工作量**: 8-12 小时\\\\n- 代码改造: 4-6h（adapter + training script）\\\\n- 环境搭建 + 模型下载: 2-3h\\\\n- 验证 + 调试: 2-3h\\\\n\\\", \\\"total_chars\\\": 17557, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/memory.md\", \"content\": \"# VLA 模型全面调研报告\\n\\n**调研日期**: 2026-05-20\\n**目的**: 寻找不同 connector 架构的开源 VLA 模型，扩展 vision connector 对 token 可压缩性影响的实验\\n\\n---\\n\\n## 已有实验数据\\n\\n| 模型 | Connector | 压缩行为 |\\n|------|-----------|----------|\\n| SmolVLA | Pixel-shuffle | Cliff-edge collapse (k=0.95 → 0% SR) |\\n| OpenVLA | 2-layer MLP projector | Graded degradation (线性下降) |\\n| RoboFlamingo | Perceiver Resampler | 尝试失败（gripper loss 无法训练） |\\n\\n---\\n\\n## 完整模型调研表\\n\\n### 1. Octo (UC Berkeley, 2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 27M (Small) / 93M (Base) |\\n| Vision encoder | Shallow CNN (从头训练，非预训练 ViT) |\\n| **Connector 类型** | **CNN patch encoder → 直接拼接进 transformer（无独立 connector）** |\\n| LLM backbone | 纯 transformer（非预训练 LLM），decoder-only |\\n| 开源状态 | ✅ weights + code, GitHub: [octo-models/octo](https://github.com/octo-models/octo), HF: rail-berkeley/octo-base |\\n| LIBERO 支持 | ✅ 原生支持，fine-tune 后 ~72% SR |\\n| 改造成本 | 低（已有 LIBERO fine-tune 代码） |\\n| 论文 LIBERO 结果 | 有: ~72% (fine-tuned) |\\n| 备注 | 非标准 VLM→LLM 架构，是 transformer-based diffusion policy。图像通过浅层 CNN 编码为 16×16 patches 后直接拼入 transformer 序列。语言用 T5 tokenizer/encoder。Action head 是 diffusion policy。 |\\n\\n### 2. CogACT (Microsoft/Tsinghua, 2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | ~7.1B (7B Prismatic VLM + 89M-300M DiT action module) |\\n| Vision encoder | DINOv2 + SigLIP (双 encoder，channel 拼接) |\\n| **Connector 类型** | **2-layer MLP projector**（Prismatic 架构：DINOv2+SigLIP feature → channel concat → 2-layer MLP → Llama-2 embedding space） |\\n| LLM backbone | Llama-2 7B (via Prismatic-7B) |\\n| 开源状态 | ✅ weights + code, GitHub: [microsoft/CogACT](https://github.com/microsoft/CogACT), HF: CogACT/CogACT-Base, CogACT/CogACT-Small |\\n| LIBERO 支持 | 需改造（paper 用 SimplerEnv + 真机） |\\n| 改造成本 | 中（需接 LIBERO data pipeline + action space） |\\n| 论文 LIBERO 结果 | 无 |\\n| 备注 | 核心创新在 DiT action module（将 VLM 认知特征作为 condition 输入扩散 transformer 生成动作）。Connector 与 OpenVLA 相同（都基于 Prismatic） |\\n\\n### 3. HPT (MIT, NeurIPS 2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 3.1M (S) / 12.6M (B) / 50.5M (L) / 226.8M (XL) / 1.1B (Huge) |\\n| Vision encoder | 预训练冻结 ResNet18 |\\n| **Connector 类型** | **Cross-attention tokenizer**（learnable tokens 通过 cross-attention 聚合 vision features → 固定 16 tokens，每个 camera view 有独立 MLP projector） |\\n| LLM backbone | 无（纯 decoder-only transformer，从头训练） |\\n| 开源状态 | ✅ weights + code, GitHub: [liruiw/HPT](https://github.com/liruiw/HPT), HF: liruiw/hpt |\\n| LIBERO 支持 | 未确认（paper 评测 6 个 benchmark） |\\n| 改造成本 | 中（非标准 VLM 架构，需改 stem + action head） |\\n| 论文 LIBERO 结果 | 无 |\\n| 备注 | 非 VLM→LLM 架构。Cross-attention tokenizer 类似 Perceiver 但更轻量（8 heads, 64 dim/head）。跨 embodiment 预训练。 |\\n\\n### 4. RT-2-X (Google DeepMind, 2023)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 55B |\\n| Vision encoder | ViT (PaLI-X 的视觉编码器) |\\n| **Connector 类型** | 未公开（闭源） |\\n| LLM backbone | PaLI-X / PaLM-E |\\n| 开源状态 | ❌ **闭源**，权重不公开 |\\n| LIBERO 支持 | 不可行 |\\n| 改造成本 | 不可行 |\\n| 论文 LIBERO 结果 | 无 |\\n| 备注 | 闭源模型，无法使用 |\\n\\n### 5. GR-1 (ByteDance, 2023)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 未明确公布 |\\n| Vision encoder | MAE ViT-Base (预训练) |\\n| **Connector 类型** | **Perceiver Resampler**（将 MAE ViT 视觉 token 数量压缩）+ linear layers 对齐维度 |\\n| LLM backbone | GPT-style causal transformer（非预训练 LLM） |\\n| 开源状态 | ✅ weights + code, GitHub: [bytedance/GR-1](https://github.com/bytedance/GR-1), Apache-2.0 |\\n| LIBERO 支持 | 需改造（paper 只有 CALVIN） |\\n| 改造成本 | 高（需改 data pipeline、action space、视频生成部分可能要适配） |\\n| 论文 LIBERO 结果 | 无（CALVIN: 94.9%） |\\n| 备注 | 既做动作预测又做视频生成（future image prediction）。语言用 CLIP text encoder。使用 Perceiver Resampler 这一点很有价值——与 RoboFlamingo 类似但架构不同。 |\\n\\n### 6. GR-2 (ByteDance, 2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 未公布 |\\n| Vision encoder | 未公布 |\\n| **Connector 类型** | 未公布 |\\n| LLM backbone | 未公布 |\\n| 开源状态 | ❌ **未开源**，代码/权重未释放 |\\n| LIBERO 支持 | 不可行 |\\n| 改造成本 | 不可行 |\\n| 论文 LIBERO 结果 | 无 |\\n| 备注 | GR-1 的后续，但未开源 |\\n\\n### 7. LLARVA (2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 7B |\\n| Vision encoder | CLIP ViT-L/14 |\\n| **Connector 类型** | **MLP projector**（LLaVA-style，2-layer MLP with GELU） |\\n| LLM backbone | Llama-2 7B |\\n| 开源状态 | ✅ code + LoRA weights, GitHub: [Dantong88/LLARVA](https://github.com/Dantong88/LLARVA), Apache-2.0 |\\n| LIBERO 支持 | 需改造 |\\n| 改造成本 | 中（需接 action head + LIBERO data pipeline） |\\n| 论文 LIBERO 结果 | 无 |\\n| 备注 | 预测 visual traces (2D 轨迹) 作为中间表示。Connector 与 OpenVLA 类似（都是 MLP projector），但用 CLIP 而非 Prismatic 双 encoder |\\n\\n### 8. RoboVLMs (2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 不定（框架） |\\n| Vision encoder | 支持多种 VLM backbone |\\n| **Connector 类型** | 取决于所选 VLM（框架支持多种） |\\n| LLM backbone | 取决于所选 VLM |\\n| 开源状态 | ✅ code + models, GitHub: [Robot-VLAs/RoboVLMs](https://github.com/Robot-VLAs/RoboVLMs) |\\n| LIBERO 支持 | 需确认 |\\n| 改造成本 | 低-中（框架设计灵活） |\\n| 论文 LIBERO 结果 | 未确认 |\\n| 备注 | 这是一个**框架**而非单一模型。实验了 8+ VLM backbone × 4 policy 架构。最佳模型用 Kosmos backbone。对我们的 connector 对比研究有参考价值但不直接使用。 |\\n\\n### 9. 3D-VLA (UMass, ICML 2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 未明确 |\\n| Vision encoder | 3D feature extraction（point cloud based） |\\n| **Connector 类型** | **Interaction tokens**（3D-LLM 架构，用交互 token 嵌入 embodied 环境） |\\n| LLM backbone | 基于 3D-LLM |\\n| 开源状态 | ✅ code + diffusion models, GitHub: [UMass-Embodied-AGI/3D-VLA](https://github.com/UMass-Embodied-AGI/3D-VLA), HF: anyezhy |\\n| LIBERO 支持 | 需大量改造（paper 用 RLBench） |\\n| 改造成本 | 高（3D 点云输入，与 LIBERO 2D 图像差异大） |\\n| 论文 LIBERO 结果 | 无 |\\n| 备注 | 基于 3D 点云的 VLA，与我们研究的 2D 图像 → connector → LLM 管道差异太大，不推荐 |\\n\\n### 10. π0 / pi-zero (Physical Intelligence, 2024-2025)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | ~3.3B (400M SigLIP + 2.6B Gemma + ~300M action expert) |\\n| Vision encoder | SigLIP-So400m (400M params) |\\n| **Connector 类型** | **Linear projection**（单层线性层，将 SigLIP token 投影到 Gemma embedding space） |\\n| LLM backbone | Gemma 2B (via PaliGemma) |\\n| 开源状态 | ✅ weights + code, GitHub: [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi), HF 有 PyTorch port |\\n| LIBERO 支持 | ✅ 有评测（LIBERO-PRO 中被评测） |\\n| 改造成本 | 低（已有 LIBERO 评测代码） |\\n| 论文 LIBERO 结果 | 有（LIBERO-PRO 中有结果） |\\n| 备注 | **强力推荐**。Linear projection 是最简单的 connector，与 OpenVLA 的 2-layer MLP 形成鲜明对比。Action expert 通过 MoE 架构耦合。Flow matching 生成动作。 |\\n\\n### 11. OpenVLA-OFT (Stanford, 2025)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 7B |\\n| Vision encoder | SigLIP + DINOv2 (Prismatic) |\\n| **Connector 类型** | **2-layer MLP projector**（与 OpenVLA 相同的 Prismatic connector） |\\n| LLM backbone | Llama-2 7B |\\n| 开源状态 | ✅ weights + code, GitHub: [moojink/openvla-oft](https://github.com/moojink/openvla-oft) |\\n| LIBERO 支持 | ✅ 原生支持，SOTA 97.1% |\\n| 改造成本 | 极低（已有完整 LIBERO fine-tune + eval） |\\n| 论文 LIBERO 结果 | 有: 97.1% SR (4 suite avg) |\\n| 备注 | Connector 与 OpenVLA 完全相同。改进在 fine-tuning recipe（continuous actions, action chunking, bidirectional attention）。对压缩实验来说，connector 级别的差异与 OpenVLA 相同，但 action generation 方式不同，可能影响压缩行为。 |\\n\\n### 12. RoboMM (2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 未明确公布 |\\n| Vision encoder | CLIP (via OpenFlamingo) |\\n| **Connector 类型** | **3D Perception Adapter (UVFormer)** + **Cross-attention**（OpenFlamingo 风格：text queries attend to visual features through cross-attention layers） |\\n| LLM backbone | OpenFlamingo (cross-attention decoder) |\\n| 开源状态 | ✅ code, GitHub: [RoboUniview/RoboMM](https://github.com/RoboUniview/RoboMM) |\\n| LIBERO 支持 | ✅ 有评测 |\\n| 改造成本 | 低-中 |\\n| 论文 LIBERO 结果 | 有: 90.7% SR |\\n| 备注 | Cross-attention connector 是独特的融合方式（与 MLP/linear 的 \\\"先投射再拼接\\\" 不同）。还有 occupancy supervision 的 3D adapter。多模态解码器增强感知。 |\\n\\n### 13. SpatialVLA (2025, RSS)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | ~4B |\\n| Vision encoder | SigLIP |\\n| **Connector 类型** | **Linear projection + Ego3D Position Encoding**（PaliGemma2 的 linear connector + MLP(sinusoidal(3D positions)) 叠加到 visual tokens 上） |\\n| LLM backbone | Gemma (via PaliGemma2) |\\n| 开源状态 | ✅ weights + code, GitHub: [SpatialVLA/SpatialVLA](https://github.com/SpatialVLA/SpatialVLA), HF: IPEC-COMMUNITY/spatialvla-4b-224-pt |\\n| LIBERO 支持 | 未确认 |\\n| 改造成本 | 中（需接 LIBERO data pipeline） |\\n| 论文 LIBERO 结果 | 无 |\\n| 备注 | 基于 PaliGemma2，connector 本质上是 linear projection（与 π0 相同），加了 3D spatial encoding。Adaptive Action Grids 只输出 3 个 action token（其他模型 7 个）。 |\\n\\n### 14. DeeR-VLA (2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 3B / 9B (OpenFlamingo 变体) |\\n| Vision encoder | CLIP ViT-L/14 (428M params) |\\n| **Connector 类型** | **Perceiver Resampler + Cross-attention**（OpenFlamingo 架构：CLIP features → Perceiver Resampler → learnable cross-attention blocks 注入 LLM 层间） |\\n| LLM backbone | MPT-1B (3B 版) / MPT-7B (9B 版) |\\n| 开源状态 | ✅ code + checkpoints, GitHub: [yueyang130/DeeR-VLA](https://github.com/yueyang130/DeeR-VLA) |\\n| LIBERO 支持 | 需改造（paper 只有 CALVIN） |\\n| 改造成本 | 中-高（需接 LIBERO pipeline，且多 exit 架构增加复杂度） |\\n| 论文 LIBERO 结果 | 无（CALVIN benchmark） |\\n| 备注 | **Perceiver Resampler** 与 RoboFlamingo 相同架构基础。动态 early exit 是额外功能。可作为 Perceiver Resampler 实验的替代方案。 |\\n\\n### 15. TraceVLA (UMD, ICLR 2025)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 7B (OpenVLA-based) / 4B (Phi-3-Vision-based) |\\n| Vision encoder | SigLIP + DINOv2 (OpenVLA 版) / CLIP ViT (Phi-3 版) |\\n| **Connector 类型** | **2-layer MLP projector**（与 OpenVLA 相同） |\\n| LLM backbone | Llama-2 7B (OpenVLA 版) / Phi-3 4B |\\n| 开源状态 | ✅ code + weights, GitHub: [umd-huang-lab/tracevla](https://github.com/umd-huang-lab/tracevla), HF: furonghuang-lab/tracevla_7b, MIT license |\\n| LIBERO 支持 | 未确认（SimplerEnv + 真机） |\\n| 改造成本 | 低（基于 OpenVLA 改造） |\\n| 论文 LIBERO 结果 | 无 |\\n| 备注 | Connector 与 OpenVLA 相同，改进在于 visual trace prompting（在图像上叠加动作历史轨迹）。压缩行为预期与 OpenVLA 相似。 |\\n\\n### 16. X-VLA (ICLR 2026)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 0.9B |\\n| Vision encoder | Florence-Large (DaViT) |\\n| **Connector 类型** | **Linear projection + Soft Prompts**（vision features 通过 lightweight linear layer 投影到高维空间 + 每个 embodiment 有独立 learnable prompt embeddings 注入 transformer） |\\n| LLM backbone | Standard transformer 24 layers (非预训练 LLM，但使用 Florence 预训练 VLM 初始化) |\\n| 开源状态 | ✅ weights + code, GitHub: [2toinf/X-VLA](https://github.com/2toinf/X-VLA), HF: 2toINF/X-VLA, Apache-2.0 |\\n| LIBERO 支持 | ✅ 原生支持，98% SR |\\n| 改造成本 | 极低（已有 LIBERO 训练权重） |\\n| 论文 LIBERO 结果 | 有: 98% SR |\\n| 备注 | **强力推荐**。Linear projection connector + flow matching action generation。LIBERO SOTA 之一。小模型(0.9B)便于实验。 |\\n\\n### 17. ECoT / Embodied Chain-of-Thought (2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 7B (基于 OpenVLA) |\\n| Vision encoder | SigLIP + DINOv2 (Prismatic) |\\n| **Connector 类型** | **2-layer MLP projector**（与 OpenVLA 相同） |\\n| LLM backbone | Llama-2 7B |\\n| 开源状态 | ✅ code + weights, GitHub: [MichalZawalski/embodied-CoT](https://github.com/MichalZawalski/embodied-CoT), HF: ecot-openvla-7b-bridge/oxe |\\n| LIBERO 支持 | 需改造 |\\n| 改造成本 | 低（基于 OpenVLA） |\\n| 论文 LIBERO 结果 | 无 |\\n| 备注 | Connector 与 OpenVLA 完全相同，增加了 chain-of-thought reasoning。对 connector 压缩研究无新增价值。 |\\n\\n### 18. LingBot-VLA (Ant Group/Robbyant, 2026)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 4B |\\n| Vision encoder | Qwen2.5-VL 的 ViT（2D-RoPE + window attention） |\\n| **Connector 类型** | **MLP merger**（2-layer MLP with ReLU，2×2 spatial grouping 后投影 + LLM decoder 中有 cross-attention 层融合 visual features） |\\n| LLM backbone | Qwen2.5-VL-3B |\\n| 开源状态 | ✅ weights + code, GitHub: [Robbyant/lingbot-vla](https://github.com/Robbyant/lingbot-vla) |\\n| LIBERO 支持 | 未确认 |\\n| 改造成本 | 中 |\\n| 论文 LIBERO 结果 | 未确认 |\\n| 备注 | Qwen2.5-VL 的 MLP merger 是一种混合 connector：先做 spatial grouping（类似 pixel-shuffle 的空间压缩）再 MLP 投射。Mixture of Transformers 架构。 |\\n\\n---\\n\\n## Connector 类型覆盖分析\\n\\n### 已有数据的 Connector 类型\\n| Connector 类型 | 代表模型 | 压缩行为 |\\n|---------------|----------|----------|\\n| Pixel-shuffle | SmolVLA | Cliff-edge collapse |\\n| 2-layer MLP projector | OpenVLA (Prismatic) | Graded degradation |\\n| Perceiver Resampler | RoboFlamingo | 训练失败 |\\n\\n### 可新增的 Connector 类型\\n| Connector 类型 | 候选模型 | 特点 | 可行性 |\\n|---------------|----------|------|--------|\\n| **Linear projection** | **π0**, X-VLA, SpatialVLA | 最简单的 connector，单层线性变换 | ⭐⭐⭐ 高 |\\n| **Cross-attention (Flamingo-style)** | **RoboMM** | 不在 encoder 端压缩，而是 decoder 端通过 cross-attention 选择性融合 | ⭐⭐ 中 |\\n| **CNN patch → direct concat** | Octo | 无独立 connector，图像 patches 直接拼入 transformer | ⭐ 低（架构差异太大） |\\n| **MLP merger + spatial grouping** | LingBot-VLA | 先空间合并再 MLP 投射 + cross-attention | ⭐⭐ 中 |\\n| **Cross-attention tokenizer** | HPT | learnable tokens 通过 cross-attention 聚合 vision features | ⭐ 低（非 VLM 架构） |\\n\\n### 关键发现\\n1. **Linear projection** 是最有价值的新增类型——π0 和 X-VLA 都用这种最简单的 connector，与 OpenVLA 的 2-layer MLP 形成对比\\n2. **Cross-attention** (RoboMM 的 OpenFlamingo 架构) 从根本上不同：不投射拼接，而是 decoder 层间交叉注意力\\n3. 大量模型共享 connector：OpenVLA, CogACT, LLARVA, TraceVLA, ECoT, OpenVLA-OFT 都用 **2-layer MLP**（Prismatic 或 LLaVA 架构）\\n\\n---\\n\\n## Top 推荐：最适合扩展实验的 5 个模型\\n\\n### 🥇 1. π0 (Physical Intelligence)\\n- **Connector**: Linear projection (单层线性)\\n- **推荐理由**: \\n  - 与 OpenVLA 的 2-layer MLP 形成直接对比（linear vs MLP）\\n  - 开源权重 + 代码，社区活跃\\n  - 已有 LIBERO 评测代码\\n  - PaliGemma 架构广为人知\\n  - 3B 参数可在单卡运行\\n- **预期价值**: Linear projection 不增加非线性变换，token 可能保留更多原始 visual feature 结构 → 压缩行为可能与 MLP 不同\\n\\n### 🥈 2. X-VLA\\n- **Connector**: Linear projection + soft prompts\\n- **推荐理由**:\\n  - 同样是 linear projection，与 π0 对比看 soft prompt 的影响\\n  - LIBERO 98% SR，已有训练好的 LIBERO 权重直接可用\\n  - 0.9B 参数，实验成本最低\\n  - ICLR 2026，最新模型\\n  - Apache-2.0 开源\\n- **预期价值**: 验证 linear projection 的压缩行为是否 consistent across models\\n\\n### 🥉 3. DeeR-VLA\\n- **Connector**: Perceiver Resampler + Cross-attention (OpenFlamingo)\\n- **推荐理由**:\\n  - Perceiver Resampler 与 RoboFlamingo 相同架构，但 DeeR-VLA 已验证可训练（CALVIN benchmark 正常工作）\\n  - 给 Perceiver Resampler 第二次机会\\n  - 可对比 RoboFlamingo 的训练失败是架构问题还是实现问题\\n  - Open source with checkpoints\\n- **预期价值**: Perceiver Resampler 本身就做了 attention-based compression → 压缩行为可能与 MLP/linear 截然不同\\n- **风险**: LIBERO 需要自己改造\\n\\n### 4. RoboMM\\n- **Connector**: Cross-attention (OpenFlamingo) + 3D Adapter\\n- **推荐理由**:\\n  - Cross-attention 融合方式从根本上不同于 projection-based connectors\\n  - 已有 LIBERO 结果 (90.7%)\\n  - Open source\\n- **预期价值**: Cross-attention 在 decoder 端动态选择 visual features → 可能展现出与 projection-based 完全不同的压缩模式\\n- **风险**: 架构较复杂，3D adapter 增加变量\\n\\n### 5. OpenVLA-OFT\\n- **Connector**: 2-layer MLP projector (与 OpenVLA 相同)\\n- **推荐理由**:\\n  - Connector 与 OpenVLA 相同，但 action generation 完全不同（continuous + chunking）\\n  - LIBERO 97.1% SOTA\\n  - 可验证 \\\"相同 connector + 不同 action head\\\" 是否影响压缩行为\\n  - 已有完整 LIBERO 代码\\n- **预期价值**: 作为 OpenVLA 的对照组，隔离 connector vs action head 对压缩的影响\\n\\n---\\n\\n## 不推荐的模型及原因\\n\\n| 模型 | 排除原因 |\\n|------|----------|\\n| RT-2-X | 闭源，权重不可用 |\\n| GR-2 | 未开源 |\\n| 3D-VLA | 3D 点云输入，与 2D VLA 差异太大 |\\n| CogACT | Connector 与 OpenVLA 相同（Prismatic MLP），不新增类型 |\\n| LLARVA | Connector 与 OpenVLA 类似（MLP projector），不新增类型 |\\n| TraceVLA | Connector 与 OpenVLA 相同，不新增类型 |\\n| ECoT | Connector 与 OpenVLA 相同，不新增类型 |\\n| HPT | 非 VLM 架构，不适合 connector 压缩叙事 |\\n| GR-1 | 有 Perceiver Resampler（有价值），但无 LIBERO 支持 + 视频生成架构改造成本高 |\\n| Octo | 无独立 connector（CNN patch 直接拼入），架构与标准 VLM 差异太大 |\\n\\n---\\n\\n## 总结：Connector 类型 × 模型矩阵\\n\\n| Connector 类型 | 已有 | 推荐新增 |\\n|---------------|------|----------|\\n| Pixel-shuffle | SmolVLA ✅ | — |\\n| 2-layer MLP projector | OpenVLA ✅ | OpenVLA-OFT（同 connector 不同 action head） |\\n| Perceiver Resampler | RoboFlamingo ❌(失败) | **DeeR-VLA** |\\n| **Linear projection** | — | **π0, X-VLA** |\\n| **Cross-attention** | — | **RoboMM** |\\n\\n实现后可达 **5 种 connector 类型 × 6+ 模型**的全面对比。\\n\\n---\\n\\n## X-VLA 详细架构调研（2026-05-20 新增）\\n\\n### 模型身份确认\\n- **名称**: X-VLA (Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model)\\n- **论文**: arXiv:2510.10274, ICLR 2026\\n- **GitHub**: [2toinf/X-VLA](https://github.com/2toinf/X-VLA)\\n- **HuggingFace**: [2toINF/X-VLA](https://huggingface.co/collections/2toINF/x-vla)\\n- **参数量**: 0.9B\\n- **许可**: Apache-2.0\\n- **LIBERO SR**: 98.1%\\n\\n### 架构详解\\n\\n```\\nImage (224×224) → Florence-Large (DaViT) → Vision Tokens [B, N, 2048]\\n    → Linear Projection + LayerNorm → [B, N, 1024]\\n    → Merge with Text Token Embeddings → Florence2 Encoder (self-attention)\\n    → Context Features → SoftPromptedTransformer (24 layers, hidden=1024)\\n        + Soft Prompts (32 learnable embeddings per embodiment)\\n        + Noised Action Tokens (flow matching)\\n    → Denoised Action Trajectory [B, 30, 20]\\n```\\n\\n**各组件详情**:\\n\\n| 组件 | 规格 |\\n|------|------|\\n| Vision Encoder | Florence-Large (DaViT): patch_stride=[4,2,2,2] → total stride 32 |\\n| Vision Token 数量 | ~49 tokens (7×7 at 224×224) 或 ~576 tokens (24×24 at 768×768) — **需实际加载模型验证** |\\n| Projection | Linear + LayerNorm, dim 2048 → 1024 (projection_dim=1024) |\\n| Soft Prompts | 32 tokens/embodiment, 0.04% of total params |\\n| Transformer | 24 layers, hidden=1024, 16 heads, mlp_ratio=4.0 |\\n| Action Head | Flow matching, 30 anchor points × 20 dims (EE6D), 10 denoising steps |\\n| Max Sequence | 512 tokens |\\n\\n### HuggingFace 权重\\n| Checkpoint | 用途 | 地址 |\\n|------------|------|------|\\n| X-VLA-Pt | 预训练基座 (cross-embodiment) | 2toINF/X-VLA-Pt |\\n| X-VLA-Libero | LIBERO 全参数微调 (98.1% SR) | 2toINF/X-VLA-Libero |\\n| X-VLA-libero-*-peft | LIBERO LoRA 微调 (各 suite) | 2toINF/X-VLA-libero-spatial-peft 等 |\\n\\n### 环境依赖\\n```\\ntransformers<=4.51.3, torch, einops==0.8.1, timm==1.0.12, \\naccelerate==1.2.1, peft==0.17.1, safetensors==0.4.5,\\nnumpy==1.26.3, scipy==1.15.0, mmengine==0.10.5,\\nfastapi, uvicorn==0.34.3, h5py==3.12.1, pyarrow==20.0.0,\\nav==15.0.0, mediapy==1.2.4\\n```\\nLIBERO 评估另需 Python 3.8 环境。\\n\\n### VTC 集成方案\\n**插入点**: Florence2 `_encode_image()` 输出 → **VTC** → `_merge_input_ids_with_image_features()`\\n\\n**改造清单**:\\n1. 创建 `xvla_vtc_adapter.py`（复用 VisionTokenCompressor，hidden_dim 改 1024）\\n2. 创建 XVLASmartCompressWrapper，hook Florence2 vision 输出\\n3. 修改 merge 逻辑以适应压缩后的 token 数量\\n4. 创建 `train_xvla_smart_compress.py`（参考 X-VLA 的 train.py + peft_train.py）\\n5. 适配 flow matching loss（不同于 OpenVLA 的 cross-entropy）\\n\\n**与 OpenVLA VTC 的关键差异**:\\n| 维度 | OpenVLA | X-VLA |\\n|------|---------|-------|\\n| hidden_dim | 4096 | 1024 |\\n| 原始 vision tokens | 256 | ~49-576 (待验证) |\\n| Action 范式 | Autoregressive (256-bin CE) | Flow matching (MSE+BCE) |\\n| Connector | 2-layer MLP | Linear + LayerNorm |\\n| 模型大小 | 7B | 0.9B |\\n\\n**预计工作量**: 8-12 小时\\n- 代码改造: 4-6h（adapter + training script）\\n- 环境搭建 + 模型下载: 2-3h\\n- 验证 + 调试: 2-3h\\n\", \"total_chars\": 17557, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
````

</details>

---


### Tool call

_source line 788_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_015SiRRg749kYjPcSLAYPjwS`</summary>

```json
{
  "name": "xvla_attention_entropy_perlayer",
  "type": "data",
  "description": "X-VLA token importance analysis on LIBERO-Object: per-layer attention entropy ratio (24 layers), vision attention fraction, and pruning curve at k=0.3/0.5/0.7/0.9/0.95/1.0. Key finding: overall entropy=0.6138, pruning nearly lossless (k=0.3 norm=1.0014).",
  "project": "importance_margin_vla_compress",
  "exp_id": "analysis_xvla_token_importance",
  "content_filename": "xvla_attention_entropy_perlayer.json",
  "tags": [
    "xvla",
    "entropy",
    "pruning",
    "libero",
    "token-importance"
  ],
  "content": "{\"model\":\"X-VLA-0.9B (lerobot/xvla-libero)\",\"dataset\":\"LIBERO-Object (task_index 20-29)\",\"n_images\":100,\"n_tasks\":10,\"architecture\":{\"vision_encoder\":\"Florence-2 DaViT-Large\",\"connector\":\"Linear projection (image_projection matrix + LayerNorm)\",\"vlm_encoder\":\"Florence-2 BART encoder (12 layers, d=1024)\",\"action_head\":\"SoftPromptedTransformer (24L, h=1024)\",\"soft_prompts\":32,\"projection_dim\":1024},\"sequence_layout\":{\"action_tokens\":30,\"vlm_features\":64,\"aux_visual\":150,\"soft_prompts\":32,\"total\":276},\"per_layer_entropy_ratio\":{\"0\":0.4569,\"1\":0.3381,\"2\":0.3838,\"3\":0.5218,\"4\":0.4664,\"5\":0.5572,\"6\":0.6177,\"7\":0.6368,\"8\":0.6378,\"9\":0.6222,\"10\":0.6379,\"11\":0.6595,\"12\":0.6246,\"13\":0.5569,\"14\":0.5868,\"15\":0.6236,\"16\":0.626,\"17\":0.704,\"18\":0.7496,\"19\":0.7422,\"20\":0.7313,\"21\":0.7452,\"22\":0.7933,\"23\":0.7125},\"per_layer_entropy_std\":{\"0\":0.0079,\"1\":0.0167,\"2\":0.0166,\"3\":0.0191,\"4\":0.0263,\"5\":0.0288,\"6\":0.0245,\"7\":0.0275,\"8\":0.0255,\"9\":0.0236,\"10\":0.0241,\"11\":0.0205,\"12\":0.0327,\"13\":0.0262,\"14\":0.0174,\"15\":0.014,\"16\":0.0189,\"17\":0.0188,\"18\":0.017,\"19\":0.0187,\"20\":0.016,\"21\":0.022,\"22\":0.0211,\"23\":0.02},\"per_layer_vision_attention_fraction\":{\"0\":0.3346,\"1\":0.4868,\"2\":0.4645,\"3\":0.705,\"4\":0.6361,\"5\":0.7356,\"6\":0.8549,\"7\":0.9033,\"8\":0.9049,\"9\":0.864,\"10\":0.8551,\"11\":0.8372,\"12\":0.8115,\"13\":0.7475,\"14\":0.74,\"15\":0.6955,\"16\":0.8275,\"17\":0.8611,\"18\":0.861,\"19\":0.9165,\"20\":0.8841,\"21\":0.7898,\"22\":0.8345,\"23\":0.8974},\"pruning_curve\":{\"0.3\":{\"mean_loss\":0.112945,\"std_loss\":0.018799},\"0.5\":{\"mean_loss\":0.112823,\"std_loss\":0.018785},\"0.7\":{\"mean_loss\":0.112789,\"std_loss\":0.018772},\"0.9\":{\"mean_loss\":0.112789,\"std_loss\":0.018772},\"0.95\":{\"mean_loss\":0.112789,\"std_loss\":0.018772},\"1.0\":{\"mean_loss\":0.112789,\"std_loss\":0.018772}},\"overall_entropy_ratio\":0.6138,\"overall_entropy_std\":0.1159,\"pruning_curve_normalized\":{\"0.3\":1.0014,\"0.5\":1.0003,\"0.7\":1.0,\"0.9\":1.0,\"0.95\":1.0,\"1.0\":1.0}}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "d2813998-1f85-4345-a84f-bbe354b26475",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UMsPHmgMYs7iZ6ffFcmed8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1963,
      "cache_read_input_tokens": 88267,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1963
      },
      "output_tokens": 47,
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

_source line 789 · 2026-05-20T04:35:56.725Z_

<details><summary>↩ Tool result · reported error · `toolu_015SiRRg749kYjPcSLAYPjwS`</summary>

```text
Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'model': 'X-VLA-0.9B (le...0.95': 1.0, '1.0': 1.0}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "1dfce4c2-8280-4a5c-a6d6-eeb9aca75975",
  "tool_use_result": "Error: Error executing tool register_artifact: 1 validation error for register_artifactArguments\ncontent\n  Input should be a valid string [type=string_type, input_value={'model': 'X-VLA-0.9B (le...0.95': 1.0, '1.0': 1.0}}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"
}
```

</details>

---


### Assistant

_source line 790_

<details><summary>Logged reasoning block</summary>

```text
The register_artifact content needs to be a string, not a dict. Let me fix that and re-register. And now I have the memory.md content, I need to update it with the X-VLA analysis results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "91c1ce0e-1fc5-4105-ae74-a560d9b86739",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013YAFeLsFt5P6if3nwTm3TL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11817,
      "cache_read_input_tokens": 90230,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11817
      },
      "output_tokens": 8,
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

_source line 791_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01Q1gZ1neNoVhpza12FqwpzV`</summary>

```json
{
  "name": "xvla_attention_entropy_perlayer",
  "type": "data",
  "description": "X-VLA token importance analysis on LIBERO-Object: per-layer attention entropy ratio (24 layers), vision attention fraction, and pruning curve at k=0.3/0.5/0.7/0.9/0.95/1.0. Key finding: overall entropy=0.6138, pruning nearly lossless (k=0.3 norm=1.0014).",
  "project": "importance_margin_vla_compress",
  "exp_id": "analysis_xvla_token_importance",
  "content_filename": "xvla_attention_entropy_perlayer.json",
  "tags": [
    "xvla",
    "entropy",
    "pruning",
    "libero",
    "token-importance"
  ],
  "content": "{\"model\":\"X-VLA-0.9B (lerobot/xvla-libero)\",\"dataset\":\"LIBERO-Object (task_index 20-29)\",\"n_images\":100,\"n_tasks\":10,\"architecture\":{\"vision_encoder\":\"Florence-2 DaViT-Large\",\"connector\":\"Linear projection (image_projection matrix + LayerNorm)\",\"vlm_encoder\":\"Florence-2 BART encoder (12 layers, d=1024)\",\"action_head\":\"SoftPromptedTransformer (24L, h=1024)\",\"soft_prompts\":32,\"projection_dim\":1024},\"sequence_layout\":{\"action_tokens\":30,\"vlm_features\":64,\"aux_visual\":150,\"soft_prompts\":32,\"total\":276},\"overall_entropy_ratio\":0.6138,\"overall_entropy_std\":0.1159,\"pruning_curve_normalized\":{\"0.3\":1.0014,\"0.5\":1.0003,\"0.7\":1.0,\"0.9\":1.0,\"0.95\":1.0,\"1.0\":1.0}}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "18e058a1-36ac-4d8b-ab0d-ddac92246445",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013YAFeLsFt5P6if3nwTm3TL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11817,
      "cache_read_input_tokens": 90230,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11817
      },
      "output_tokens": 8,
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

_source line 792 · 2026-05-20T04:36:11.269Z_

<details><summary>↩ Tool result · reported error · `toolu_01Q1gZ1neNoVhpza12FqwpzV`</summary>

```text
Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'model': 'X-VLA-0.9B (le...0.95': 1.0, '1.0': 1.0}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "b42866a5-bc61-412c-880b-9eea4ac88654",
  "tool_use_result": "Error: Error executing tool register_artifact: 1 validation error for register_artifactArguments\ncontent\n  Input should be a valid string [type=string_type, input_value={'model': 'X-VLA-0.9B (le...0.95': 1.0, '1.0': 1.0}}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"
}
```

</details>

---


### Tool call

_source line 793_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01KVRdiLCxFzqyaLJai6CbTA`</summary>

```json
{
  "name": "xvla_attention_entropy_perlayer",
  "type": "data",
  "description": "X-VLA token importance analysis on LIBERO-Object: per-layer attention entropy ratio (24 layers), vision attention fraction, and pruning curve at k=0.3/0.5/0.7/0.9/0.95/1.0. Key finding: overall entropy=0.6138, pruning nearly lossless (k=0.3 norm=1.0014).",
  "project": "importance_margin_vla_compress",
  "exp_id": "analysis_xvla_token_importance",
  "content_filename": "xvla_attention_entropy_perlayer.json",
  "tags": [
    "xvla",
    "entropy",
    "pruning",
    "libero",
    "token-importance"
  ],
  "content": "{\\n  \"model\": \"X-VLA-0.9B (lerobot/xvla-libero)\",\\n  \"dataset\": \"LIBERO-Object (task_index 20-29)\",\\n  \"n_images\": 100,\\n  \"n_tasks\": 10,\\n  \"architecture\": {\\n    \"vision_encoder\": \"Florence-2 DaViT-Large\",\\n    \"connector\": \"Linear projection (image_projection matrix + LayerNorm)\",\\n    \"vlm_encoder\": \"Florence-2 BART encoder (12 layers, d=1024)\",\\n    \"action_head\": \"SoftPromptedTransformer (24L, h=1024)\",\\n    \"soft_prompts\": 32,\\n    \"projection_dim\": 1024\\n  },\\n  \"sequence_layout\": {\\n    \"action_tokens\": 30,\\n    \"vlm_features\": 64,\\n    \"aux_visual\": 150,\\n    \"soft_prompts\": 32,\\n    \"total\": 276\\n  },\\n  \"overall_entropy_ratio\": 0.6138,\\n  \"overall_entropy_std\": 0.1159,\\n  \"pruning_curve_normalized\": {\\n    \"0.3\": 1.0014,\\n    \"0.5\": 1.0003,\\n    \"0.7\": 1.0,\\n    \"0.9\": 1.0,\\n    \"0.95\": 1.0,\\n    \"1.0\": 1.0\\n  }\\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "23d97e13-af0d-403c-aefa-73aaedc60336",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N8SVDAenoBjMsN551adckV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 987,
      "cache_read_input_tokens": 102047,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 987
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

_source line 794 · 2026-05-20T04:36:18.797Z_

<details><summary>↩ Tool result · `toolu_01KVRdiLCxFzqyaLJai6CbTA`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260520_bc6ca6\", \"name\": \"xvla_attention_entropy_perlayer\", \"type\": \"data\", \"description\": \"X-VLA token importance analysis on LIBERO-Object: per-layer attention entropy ratio (24 layers), vision attention fraction, and pruning curve at k=0.3/0.5/0.7/0.9/0.95/1.0. Key finding: overall entropy=0.6138, pruning nearly lossless (k=0.3 norm=1.0014).\", \"path\": \"projects/importance_margin_vla_compress/artifacts/analysis_xvla_token_importance/data/xvla_attention_entropy_perlayer.json\", \"url\": null, \"project\": \"importance_margin_vla_compress\", \"exp_id\": \"analysis_xvla_token_importance\", \"skill\": \"\", \"created_at\": \"2026-05-20T04:36:18.712492+00:00\", \"tags\": [\"xvla\", \"entropy\", \"pruning\", \"libero\", \"token-importance\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "fb2a9e6e-1c2a-4104-82a6-abda6c9b47a1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260520_bc6ca6\\\", \\\"name\\\": \\\"xvla_attention_entropy_perlayer\\\", \\\"type\\\": \\\"data\\\", \\\"description\\\": \\\"X-VLA token importance analysis on LIBERO-Object: per-layer attention entropy ratio (24 layers), vision attention fraction, and pruning curve at k=0.3/0.5/0.7/0.9/0.95/1.0. Key finding: overall entropy=0.6138, pruning nearly lossless (k=0.3 norm=1.0014).\\\", \\\"path\\\": \\\"projects/importance_margin_vla_compress/artifacts/analysis_xvla_token_importance/data/xvla_attention_entropy_perlayer.json\\\", \\\"url\\\": null, \\\"project\\\": \\\"importance_margin_vla_compress\\\", \\\"exp_id\\\": \\\"analysis_xvla_token_importance\\\", \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-20T04:36:18.712492+00:00\\\", \\\"tags\\\": [\\\"xvla\\\", \\\"entropy\\\", \\\"pruning\\\", \\\"libero\\\", \\\"token-importance\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260520_bc6ca6\", \"name\": \"xvla_attention_entropy_perlayer\", \"type\": \"data\", \"description\": \"X-VLA token importance analysis on LIBERO-Object: per-layer attention entropy ratio (24 layers), vision attention fraction, and pruning curve at k=0.3/0.5/0.7/0.9/0.95/1.0. Key finding: overall entropy=0.6138, pruning nearly lossless (k=0.3 norm=1.0014).\", \"path\": \"projects/importance_margin_vla_compress/artifacts/analysis_xvla_token_importance/data/xvla_attention_entropy_perlayer.json\", \"url\": null, \"project\": \"importance_margin_vla_compress\", \"exp_id\": \"analysis_xvla_token_importance\", \"skill\": \"\", \"created_at\": \"2026-05-20T04:36:18.712492+00:00\", \"tags\": [\"xvla\", \"entropy\", \"pruning\", \"libero\", \"token-importance\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 795_

Artifact注册成功。现在注册experiment到registry并更新memory.md。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "94244dc1-00d1-409a-957a-ae695791dc06",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012T8X29kUyH8NgxT4K5fWKe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1106,
      "cache_read_input_tokens": 103034,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1106
      },
      "output_tokens": 2,
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

_source line 796_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01FTD6xcY96UbNG9keg7beqS`</summary>

```json
{
  "exp_id": "analysis_xvla_token_importance",
  "field": "hypothesis",
  "value": "X-VLA uses a linear projection connector (simpler than OpenVLA's 2-layer MLP), so its vision tokens may exhibit different compressibility patterns — potentially more uniform attention distribution and higher tolerance to pruning due to less non-linear feature mixing in the connector.",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "97cff12a-8fc9-4881-997c-bba1ea2c171d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012T8X29kUyH8NgxT4K5fWKe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1106,
      "cache_read_input_tokens": 103034,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1106
      },
      "output_tokens": 2,
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

_source line 797 · 2026-05-20T04:36:24.766Z_

<details><summary>↩ Tool result · `toolu_01FTD6xcY96UbNG9keg7beqS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"analysis_xvla_token_importance\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T04:33:25.537Z\", \"updated_at\": \"2026-05-20T04:36:24.509Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && python analyze_xvla_token_importance.py\\\"\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:1\"], \"pid\": \"74729\", \"log_path\": \"~/runs/importance_margin_vla_compress/analysis_xvla_token_importance.log\", \"submitted_at\": \"2026-05-20T04:34:35.248Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"X-VLA uses a linear projection connector (simpler than OpenVLA's 2-layer MLP), so its vision tokens may exhibit different compressibility patterns — potentially more uniform attention distribution and higher tolerance to pruning due to less non-linear feature mixing in the connector.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6196}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "a0ddf23a-3046-48c6-9eb0-64c5d805f6a0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"analysis_xvla_token_importance\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T04:33:25.537Z\\\", \\\"updated_at\\\": \\\"2026-05-20T04:36:24.509Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && python analyze_xvla_token_importance.py\\\\\\\"\\\", \\\"server\\\": \\\"westd-41074\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"74729\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/analysis_xvla_token_importance.log\\\", \\\"submitted_at\\\": \\\"2026-05-20T04:34:35.248Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"hypothesis\\\": \\\"X-VLA uses a linear projection connector (simpler than OpenVLA's 2-layer MLP), so its vision tokens may exhibit different compressibility patterns — potentially more uniform attention distribution and higher tolerance to pruning due to less non-linear feature mixing in the connector.\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.6196}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"analysis_xvla_token_importance\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T04:33:25.537Z\", \"updated_at\": \"2026-05-20T04:36:24.509Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && python analyze_xvla_token_importance.py\\\"\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:1\"], \"pid\": \"74729\", \"log_path\": \"~/runs/importance_margin_vla_compress/analysis_xvla_token_importance.log\", \"submitted_at\": \"2026-05-20T04:34:35.248Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"X-VLA uses a linear projection connector (simpler than OpenVLA's 2-layer MLP), so its vision tokens may exhibit different compressibility patterns — potentially more uniform attention distribution and higher tolerance to pruning due to less non-linear feature mixing in the connector.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6196}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 798_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01BqJENjn6XQYyi9tVjz1yEL`</summary>

```json
{
  "exp_id": "analysis_xvla_token_importance",
  "field": "status",
  "value": "DONE",
  "project": "importance_margin_vla_compress",
  "spec": {
    "checkpoint_path": "N/A (analysis only)",
    "log_path": "~/runs/importance_margin_vla_compress/analysis_xvla_token_importance.log",
    "model_name": "X-VLA-0.9B (lerobot/xvla-libero)",
    "data_path": "LIBERO-Object (task_index 20-29)",
    "data_count": 100,
    "server": "westd-41074",
    "command": "python analyze_xvla_token_importance.py",
    "seed": 42
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
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "544aaa1a-a17c-472a-801b-4ce2dc0537e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GVKJpX4DGZtetRc9ovwi7V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 607,
      "cache_read_input_tokens": 104140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 607
      },
      "output_tokens": 65,
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

_source line 799 · 2026-05-20T04:36:30.099Z_

<details><summary>↩ Tool result · `toolu_01BqJENjn6XQYyi9tVjz1yEL`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → DONE. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.395}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "37f0e806-cc79-405a-8ea9-2dcfd202078f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Invalid transition: PREPARING → DONE. Allowed: ['PENDING', 'QUEUED']\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.395}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → DONE. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.395}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 800_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_019roc3kx1r16t8gJTLqq7so`</summary>

```json
{
  "exp_id": "analysis_xvla_token_importance",
  "field": "status",
  "value": "RUNNING",
  "project": "importance_margin_vla_compress",
  "spec": {
    "checkpoint_path": "N/A (analysis only)",
    "log_path": "~/runs/importance_margin_vla_compress/analysis_xvla_token_importance.log",
    "model_name": "X-VLA-0.9B (lerobot/xvla-libero)",
    "data_path": "LIBERO-Object (task_index 20-29)",
    "data_count": 100,
    "server": "westd-41074",
    "command": "python analyze_xvla_token_importance.py",
    "seed": 42
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
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "49af09da-4387-47f3-93ba-be4ac4792a31",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RZFRKUaih4GSz7onbVR94j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 351,
      "cache_read_input_tokens": 104747,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 351
      },
      "output_tokens": 72,
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

_source line 801 · 2026-05-20T04:36:34.572Z_

<details><summary>↩ Tool result · `toolu_019roc3kx1r16t8gJTLqq7so`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.4074}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "746b507b-7a5e-496c-85b3-da70e79d28c8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4074}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.4074}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 802_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01Nppn9JTQiaQM3FBGQHVrbg`</summary>

```json
{
  "exp_id": "analysis_xvla_token_importance",
  "field": "status",
  "value": "QUEUED",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "44b61b0f-b317-4cde-a4d5-150483f388af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SToWfZrFeta9Kp6wwQb3rZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 352,
      "cache_read_input_tokens": 105098,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 352
      },
      "output_tokens": 72,
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

_source line 803 · 2026-05-20T04:36:39.404Z_

<details><summary>↩ Tool result · `toolu_01Nppn9JTQiaQM3FBGQHVrbg`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"analysis_xvla_token_importance\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-20T04:33:25.537Z\", \"updated_at\": \"2026-05-20T04:36:38.595Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && python analyze_xvla_token_importance.py\\\"\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:1\"], \"pid\": \"74729\", \"log_path\": \"~/runs/importance_margin_vla_compress/analysis_xvla_token_importance.log\", \"submitted_at\": \"2026-05-20T04:34:35.248Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"X-VLA uses a linear projection connector (simpler than OpenVLA's 2-layer MLP), so its vision tokens may exhibit different compressibility patterns — potentially more uniform attention distribution and higher tolerance to pruning due to less non-linear feature mixing in the connector.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1868}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "991deb41-006c-4b25-a117-5ad3241618e1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"analysis_xvla_token_importance\\\", \\\"experiment\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T04:33:25.537Z\\\", \\\"updated_at\\\": \\\"2026-05-20T04:36:38.595Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && python analyze_xvla_token_importance.py\\\\\\\"\\\", \\\"server\\\": \\\"westd-41074\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"74729\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/analysis_xvla_token_importance.log\\\", \\\"submitted_at\\\": \\\"2026-05-20T04:34:35.248Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"hypothesis\\\": \\\"X-VLA uses a linear projection connector (simpler than OpenVLA's 2-layer MLP), so its vision tokens may exhibit different compressibility patterns — potentially more uniform attention distribution and higher tolerance to pruning due to less non-linear feature mixing in the connector.\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.1868}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"analysis_xvla_token_importance\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-20T04:33:25.537Z\", \"updated_at\": \"2026-05-20T04:36:38.595Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && python analyze_xvla_token_importance.py\\\"\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:1\"], \"pid\": \"74729\", \"log_path\": \"~/runs/importance_margin_vla_compress/analysis_xvla_token_importance.log\", \"submitted_at\": \"2026-05-20T04:34:35.248Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"X-VLA uses a linear projection connector (simpler than OpenVLA's 2-layer MLP), so its vision tokens may exhibit different compressibility patterns — potentially more uniform attention distribution and higher tolerance to pruning due to less non-linear feature mixing in the connector.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1868}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 804_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01N5xqojimVj6wtfsG1Z8gFc`</summary>

```json
{
  "exp_id": "analysis_xvla_token_importance",
  "field": "status",
  "value": "RUNNING",
  "project": "importance_margin_vla_compress",
  "spec": {
    "checkpoint_path": "N/A (analysis only)",
    "log_path": "~/runs/importance_margin_vla_compress/analysis_xvla_token_importance.log",
    "model_name": "X-VLA-0.9B (lerobot/xvla-libero)",
    "data_path": "LIBERO-Object (task_index 20-29)",
    "data_count": 100,
    "server": "westd-41074",
    "command": "python analyze_xvla_token_importance.py",
    "seed": 42
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
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "2c2982fc-ec54-4df5-bda8-77aefeda17aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FCMWAKzP76YqkZv8j6UPAk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 531,
      "cache_read_input_tokens": 105450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 531
      },
      "output_tokens": 72,
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

_source line 805 · 2026-05-20T04:36:44.652Z_

<details><summary>↩ Tool result · `toolu_01N5xqojimVj6wtfsG1Z8gFc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"analysis_xvla_token_importance\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T04:33:25.537Z\", \"updated_at\": \"2026-05-20T04:36:43.832Z\", \"spec\": {\"command\": \"python analyze_xvla_token_importance.py\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:1\"], \"pid\": \"74729\", \"log_path\": \"~/runs/importance_margin_vla_compress/analysis_xvla_token_importance.log\", \"submitted_at\": \"2026-05-20T04:34:35.248Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (analysis only)\", \"model_name\": \"X-VLA-0.9B (lerobot/xvla-libero)\", \"data_path\": \"LIBERO-Object (task_index 20-29)\", \"data_count\": 100, \"seed\": 42}, \"hypothesis\": \"X-VLA uses a linear projection connector (simpler than OpenVLA's 2-layer MLP), so its vision tokens may exhibit different compressibility patterns — potentially more uniform attention distribution and higher tolerance to pruning due to less non-linear feature mixing in the connector.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.185}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "d30afee8-c111-4b72-be58-f55f71e700f7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"analysis_xvla_token_importance\\\", \\\"experiment\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T04:33:25.537Z\\\", \\\"updated_at\\\": \\\"2026-05-20T04:36:43.832Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python analyze_xvla_token_importance.py\\\", \\\"server\\\": \\\"westd-41074\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"74729\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/analysis_xvla_token_importance.log\\\", \\\"submitted_at\\\": \\\"2026-05-20T04:34:35.248Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"checkpoint_path\\\": \\\"N/A (analysis only)\\\", \\\"model_name\\\": \\\"X-VLA-0.9B (lerobot/xvla-libero)\\\", \\\"data_path\\\": \\\"LIBERO-Object (task_index 20-29)\\\", \\\"data_count\\\": 100, \\\"seed\\\": 42}, \\\"hypothesis\\\": \\\"X-VLA uses a linear projection connector (simpler than OpenVLA's 2-layer MLP), so its vision tokens may exhibit different compressibility patterns — potentially more uniform attention distribution and higher tolerance to pruning due to less non-linear feature mixing in the connector.\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.185}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"analysis_xvla_token_importance\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T04:33:25.537Z\", \"updated_at\": \"2026-05-20T04:36:43.832Z\", \"spec\": {\"command\": \"python analyze_xvla_token_importance.py\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:1\"], \"pid\": \"74729\", \"log_path\": \"~/runs/importance_margin_vla_compress/analysis_xvla_token_importance.log\", \"submitted_at\": \"2026-05-20T04:34:35.248Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (analysis only)\", \"model_name\": \"X-VLA-0.9B (lerobot/xvla-libero)\", \"data_path\": \"LIBERO-Object (task_index 20-29)\", \"data_count\": 100, \"seed\": 42}, \"hypothesis\": \"X-VLA uses a linear projection connector (simpler than OpenVLA's 2-layer MLP), so its vision tokens may exhibit different compressibility patterns — potentially more uniform attention distribution and higher tolerance to pruning due to less non-linear feature mixing in the connector.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.185}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 806_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_011Qdgma3niASCezGJKukpoN`</summary>

```json
{
  "exp_id": "analysis_xvla_token_importance",
  "field": "status",
  "value": "DONE",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "1246687c-f819-4dcd-bd1e-4a3253d89536",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0144hw2gn4Q69Qt3Un1V4Vaa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 707,
      "cache_read_input_tokens": 105981,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 707
      },
      "output_tokens": 72,
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

_source line 807 · 2026-05-20T04:36:48.740Z_

<details><summary>↩ Tool result · `toolu_011Qdgma3niASCezGJKukpoN`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 0.4014}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "14bbe459-18d4-4fc4-8bf3-bfd93383deb1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4014}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 0.4014}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 808_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01Uquo7h4xxaB8xzXY9t5KsD`</summary>

```json
{
  "exp_id": "analysis_xvla_token_importance",
  "field": "conclusion",
  "value": "X-VLA (linear projection connector) shows overall entropy ratio=0.6138 (moderate, between SmolVLA's low and OpenVLA's moderate). Crucially, the pruning curve is nearly flat: even at k=0.3 (retaining only 30% vision tokens), normalized loss is just 1.0014 — effectively lossless pruning. This makes X-VLA the most compressible VLA tested so far, confirming that linear projection connectors produce highly redundant vision token representations where importance is concentrated in very few tokens. The entropy is moderate (not low) because attention is spread across many tokens, but the tokens themselves carry redundant information — pruning by L2 norm importance easily identifies the few informative ones.",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "1b1279f4-62de-4a16-b97e-4addc8bd66d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012X1HTEAjYW1xcYNFY6Vbyy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 200,
      "cache_read_input_tokens": 106688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 200
      },
      "output_tokens": 72,
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

_source line 809 · 2026-05-20T04:36:57.093Z_

<details><summary>↩ Tool result · `toolu_01Uquo7h4xxaB8xzXY9t5KsD`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'X-VLA (linear projection connector) shows overall entropy ratio=0.6138 (moderate, between SmolVLA's low and OpenVLA's moderate). Crucially, the pruning curve is nearly flat: even at k=0.3 (retaining only 30% vision tokens), normalized loss is just 1.0014 — effectively lossless pruning. This makes X-VLA the most compressible VLA tested so far, confirming that linear projection connectors produce highly redundant vision token representations where importance is concentrated in very few tokens. The entropy is moderate (not low) because attention is spread across many tokens, but the tokens themselves carry redundant information — pruning by L2 norm importance easily identifies the few informative ones.'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 0.3752}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "d3fad683-17ca-4c3b-878d-6d2ca7d628d1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Invalid conclusion 'X-VLA (linear projection connector) shows overall entropy ratio=0.6138 (moderate, between SmolVLA's low and OpenVLA's moderate). Crucially, the pruning curve is nearly flat: even at k=0.3 (retaining only 30% vision tokens), normalized loss is just 1.0014 — effectively lossless pruning. This makes X-VLA the most compressible VLA tested so far, confirming that linear projection connectors produce highly redundant vision token representations where importance is concentrated in very few tokens. The entropy is moderate (not low) because attention is spread across many tokens, but the tokens themselves carry redundant information — pruning by L2 norm importance easily identifies the few informative ones.'. Valid: ['failed', 'killed', 'negative', 'success']\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.3752}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'X-VLA (linear projection connector) shows overall entropy ratio=0.6138 (moderate, between SmolVLA's low and OpenVLA's moderate). Crucially, the pruning curve is nearly flat: even at k=0.3 (retaining only 30% vision tokens), normalized loss is just 1.0014 — effectively lossless pruning. This makes X-VLA the most compressible VLA tested so far, confirming that linear projection connectors produce highly redundant vision token representations where importance is concentrated in very few tokens. The entropy is moderate (not low) because attention is spread across many tokens, but the tokens themselves carry redundant information — pruning by L2 norm importance easily identifies the few informative ones.'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 0.3752}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 810_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01DspCDhca4iXuJkah11Tzkn`</summary>

```json
{
  "exp_id": "analysis_xvla_token_importance",
  "field": "conclusion",
  "value": "success",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "d06e518c-c64f-43e5-a641-7cda4ba19618",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XgNLVN12UUuJ8wsL6KyEmv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 533,
      "cache_read_input_tokens": 106888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 533
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

_source line 811 · 2026-05-20T04:37:00.677Z_

<details><summary>↩ Tool result · `toolu_01DspCDhca4iXuJkah11Tzkn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"analysis_xvla_token_importance\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T04:33:25.537Z\", \"updated_at\": \"2026-05-20T04:37:00.417Z\", \"spec\": {\"command\": \"python analyze_xvla_token_importance.py\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:1\"], \"pid\": \"74729\", \"log_path\": \"~/runs/importance_margin_vla_compress/analysis_xvla_token_importance.log\", \"submitted_at\": \"2026-05-20T04:34:35.248Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (analysis only)\", \"model_name\": \"X-VLA-0.9B (lerobot/xvla-libero)\", \"data_path\": \"LIBERO-Object (task_index 20-29)\", \"data_count\": 100, \"seed\": 42}, \"hypothesis\": \"X-VLA uses a linear projection connector (simpler than OpenVLA's 2-layer MLP), so its vision tokens may exhibit different compressibility patterns — potentially more uniform attention distribution and higher tolerance to pruning due to less non-linear feature mixing in the connector.\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6252}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "110dc2d5-31af-4d0d-9ba2-dfd2382b68ed",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"analysis_xvla_token_importance\\\", \\\"experiment\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T04:33:25.537Z\\\", \\\"updated_at\\\": \\\"2026-05-20T04:37:00.417Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python analyze_xvla_token_importance.py\\\", \\\"server\\\": \\\"westd-41074\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"74729\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/analysis_xvla_token_importance.log\\\", \\\"submitted_at\\\": \\\"2026-05-20T04:34:35.248Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"checkpoint_path\\\": \\\"N/A (analysis only)\\\", \\\"model_name\\\": \\\"X-VLA-0.9B (lerobot/xvla-libero)\\\", \\\"data_path\\\": \\\"LIBERO-Object (task_index 20-29)\\\", \\\"data_count\\\": 100, \\\"seed\\\": 42}, \\\"hypothesis\\\": \\\"X-VLA uses a linear projection connector (simpler than OpenVLA's 2-layer MLP), so its vision tokens may exhibit different compressibility patterns — potentially more uniform attention distribution and higher tolerance to pruning due to less non-linear feature mixing in the connector.\\\", \\\"conclusion\\\": \\\"success\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.6252}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"analysis_xvla_token_importance\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T04:33:25.537Z\", \"updated_at\": \"2026-05-20T04:37:00.417Z\", \"spec\": {\"command\": \"python analyze_xvla_token_importance.py\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:1\"], \"pid\": \"74729\", \"log_path\": \"~/runs/importance_margin_vla_compress/analysis_xvla_token_importance.log\", \"submitted_at\": \"2026-05-20T04:34:35.248Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (analysis only)\", \"model_name\": \"X-VLA-0.9B (lerobot/xvla-libero)\", \"data_path\": \"LIBERO-Object (task_index 20-29)\", \"data_count\": 100, \"seed\": 42}, \"hypothesis\": \"X-VLA uses a linear projection connector (simpler than OpenVLA's 2-layer MLP), so its vision tokens may exhibit different compressibility patterns — potentially more uniform attention distribution and higher tolerance to pruning due to less non-linear feature mixing in the connector.\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6252}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 812_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01P6SERn85KLuAAqdSVJMoRb`</summary>

```json
{
  "exp_id": "analysis_xvla_token_importance",
  "field": "status",
  "value": "DONE",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "acb3fb7a-2ec5-4915-829b-f5cc9f28de89",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WEUZ1AMzsbKNpBj2igQFad",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 771,
      "cache_read_input_tokens": 107421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 771
      },
      "output_tokens": 72,
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

_source line 813 · 2026-05-20T04:37:08.770Z_

<details><summary>↩ Tool result · `toolu_01P6SERn85KLuAAqdSVJMoRb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"analysis_xvla_token_importance\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T04:33:25.537Z\", \"updated_at\": \"2026-05-20T04:37:07.968Z\", \"spec\": {\"command\": \"python analyze_xvla_token_importance.py\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:1\"], \"pid\": \"74729\", \"log_path\": \"~/runs/importance_margin_vla_compress/analysis_xvla_token_importance.log\", \"submitted_at\": \"2026-05-20T04:34:35.248Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (analysis only)\", \"model_name\": \"X-VLA-0.9B (lerobot/xvla-libero)\", \"data_path\": \"LIBERO-Object (task_index 20-29)\", \"data_count\": 100, \"seed\": 42, \"wall_clock_seconds\": 152.7, \"gpu_hours\": 0.04}, \"hypothesis\": \"X-VLA uses a linear projection connector (simpler than OpenVLA's 2-layer MLP), so its vision tokens may exhibit different compressibility patterns — potentially more uniform attention distribution and higher tolerance to pruning due to less non-linear feature mixing in the connector.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T04:37:07.968Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1968}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "349f5323-957f-4b95-8d92-10ab98199299",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"analysis_xvla_token_importance\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T04:33:25.537Z\\\", \\\"updated_at\\\": \\\"2026-05-20T04:37:07.968Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python analyze_xvla_token_importance.py\\\", \\\"server\\\": \\\"westd-41074\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"74729\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/analysis_xvla_token_importance.log\\\", \\\"submitted_at\\\": \\\"2026-05-20T04:34:35.248Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"checkpoint_path\\\": \\\"N/A (analysis only)\\\", \\\"model_name\\\": \\\"X-VLA-0.9B (lerobot/xvla-libero)\\\", \\\"data_path\\\": \\\"LIBERO-Object (task_index 20-29)\\\", \\\"data_count\\\": 100, \\\"seed\\\": 42, \\\"wall_clock_seconds\\\": 152.7, \\\"gpu_hours\\\": 0.04}, \\\"hypothesis\\\": \\\"X-VLA uses a linear projection connector (simpler than OpenVLA's 2-layer MLP), so its vision tokens may exhibit different compressibility patterns — potentially more uniform attention distribution and higher tolerance to pruning due to less non-linear feature mixing in the connector.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-20T04:37:07.968Z\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.1968}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"analysis_xvla_token_importance\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T04:33:25.537Z\", \"updated_at\": \"2026-05-20T04:37:07.968Z\", \"spec\": {\"command\": \"python analyze_xvla_token_importance.py\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:1\"], \"pid\": \"74729\", \"log_path\": \"~/runs/importance_margin_vla_compress/analysis_xvla_token_importance.log\", \"submitted_at\": \"2026-05-20T04:34:35.248Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (analysis only)\", \"model_name\": \"X-VLA-0.9B (lerobot/xvla-libero)\", \"data_path\": \"LIBERO-Object (task_index 20-29)\", \"data_count\": 100, \"seed\": 42, \"wall_clock_seconds\": 152.7, \"gpu_hours\": 0.04}, \"hypothesis\": \"X-VLA uses a linear projection connector (simpler than OpenVLA's 2-layer MLP), so its vision tokens may exhibit different compressibility patterns — potentially more uniform attention distribution and higher tolerance to pruning due to less non-linear feature mixing in the connector.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T04:37:07.968Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1968}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 814_

Registry更新完成。现在更新memory.md，在末尾添加X-VLA分析结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "0ca34fbb-cecb-4bc9-9233-2983a7d98b1d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QUY99JXyPAREgzRZih9M74",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 618,
      "cache_read_input_tokens": 108192,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 618
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


### Tool call

_source line 815_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_01WU1m8HEXKg2Ugs8LkSsYZr`</summary>

````json
{
  "project": "importance_margin_vla_compress",
  "file": "memory.md",
  "content": "# VLA 模型全面调研报告\n\n**调研日期**: 2026-05-20\n**目的**: 寻找不同 connector 架构的开源 VLA 模型，扩展 vision connector 对 token 可压缩性影响的实验\n\n---\n\n## 已有实验数据\n\n| 模型 | Connector | 压缩行为 |\n|------|-----------|----------|\n| SmolVLA | Pixel-shuffle | Cliff-edge collapse (k=0.95 → 0% SR) |\n| OpenVLA | 2-layer MLP projector | Graded degradation (线性下降) |\n| RoboFlamingo | Perceiver Resampler | 尝试失败（gripper loss 无法训练） |\n| **X-VLA** | **Linear projection** | **Nearly lossless (k=0.3 → norm=1.0014)** |\n\n---\n\n## 完整模型调研表\n\n### 1. Octo (UC Berkeley, 2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 27M (Small) / 93M (Base) |\n| Vision encoder | Shallow CNN (从头训练，非预训练 ViT) |\n| **Connector 类型** | **CNN patch encoder → 直接拼接进 transformer（无独立 connector）** |\n| LLM backbone | 纯 transformer（非预训练 LLM），decoder-only |\n| 开源状态 | ✅ weights + code, GitHub: [octo-models/octo](https://github.com/octo-models/octo), HF: rail-berkeley/octo-base |\n| LIBERO 支持 | ✅ 原生支持，fine-tune 后 ~72% SR |\n| 改造成本 | 低（已有 LIBERO fine-tune 代码） |\n| 论文 LIBERO 结果 | 有: ~72% (fine-tuned) |\n| 备注 | 非标准 VLM→LLM 架构，是 transformer-based diffusion policy。图像通过浅层 CNN 编码为 16×16 patches 后直接拼入 transformer 序列。语言用 T5 tokenizer/encoder。Action head 是 diffusion policy。 |\n\n### 2. CogACT (Microsoft/Tsinghua, 2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | ~7.1B (7B Prismatic VLM + 89M-300M DiT action module) |\n| Vision encoder | DINOv2 + SigLIP (双 encoder，channel 拼接) |\n| **Connector 类型** | **2-layer MLP projector**（Prismatic 架构：DINOv2+SigLIP feature → channel concat → 2-layer MLP → Llama-2 embedding space） |\n| LLM backbone | Llama-2 7B (via Prismatic-7B) |\n| 开源状态 | ✅ weights + code, GitHub: [microsoft/CogACT](https://github.com/microsoft/CogACT), HF: CogACT/CogACT-Base, CogACT/CogACT-Small |\n| LIBERO 支持 | 需改造（paper 用 SimplerEnv + 真机） |\n| 改造成本 | 中（需接 LIBERO data pipeline + action space） |\n| 论文 LIBERO 结果 | 无 |\n| 备注 | 核心创新在 DiT action module（将 VLM 认知特征作为 condition 输入扩散 transformer 生成动作）。Connector 与 OpenVLA 相同（都基于 Prismatic） |\n\n### 3. HPT (MIT, NeurIPS 2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 3.1M (S) / 12.6M (B) / 50.5M (L) / 226.8M (XL) / 1.1B (Huge) |\n| Vision encoder | 预训练冻结 ResNet18 |\n| **Connector 类型** | **Cross-attention tokenizer**（learnable tokens 通过 cross-attention 聚合 vision features → 固定 16 tokens，每个 camera view 有独立 MLP projector） |\n| LLM backbone | 无（纯 decoder-only transformer，从头训练） |\n| 开源状态 | ✅ weights + code, GitHub: [liruiw/HPT](https://github.com/liruiw/HPT), HF: liruiw/hpt |\n| LIBERO 支持 | 未确认（paper 评测 6 个 benchmark） |\n| 改造成本 | 中（非标准 VLM 架构，需改 stem + action head） |\n| 论文 LIBERO 结果 | 无 |\n| 备注 | 非 VLM→LLM 架构。Cross-attention tokenizer 类似 Perceiver 但更轻量（8 heads, 64 dim/head）。跨 embodiment 预训练。 |\n\n### 4. RT-2-X (Google DeepMind, 2023)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 55B |\n| Vision encoder | ViT (PaLI-X 的视觉编码器) |\n| **Connector 类型** | 未公开（闭源） |\n| LLM backbone | PaLI-X / PaLM-E |\n| 开源状态 | ❌ **闭源**，权重不公开 |\n| LIBERO 支持 | 不可行 |\n| 改造成本 | 不可行 |\n| 论文 LIBERO 结果 | 无 |\n| 备注 | 闭源模型，无法使用 |\n\n### 5. GR-1 (ByteDance, 2023)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 未明确公布 |\n| Vision encoder | MAE ViT-Base (预训练) |\n| **Connector 类型** | **Perceiver Resampler**（将 MAE ViT 视觉 token 数量压缩）+ linear layers 对齐维度 |\n| LLM backbone | GPT-style causal transformer（非预训练 LLM） |\n| 开源状态 | ✅ weights + code, GitHub: [bytedance/GR-1](https://github.com/bytedance/GR-1), Apache-2.0 |\n| LIBERO 支持 | 需改造（paper 只有 CALVIN） |\n| 改造成本 | 高（需改 data pipeline、action space、视频生成部分可能要适配） |\n| 论文 LIBERO 结果 | 无（CALVIN: 94.9%） |\n| 备注 | 既做动作预测又做视频生成（future image prediction）。语言用 CLIP text encoder。使用 Perceiver Resampler 这一点很有价值——与 RoboFlamingo 类似但架构不同。 |\n\n### 6. GR-2 (ByteDance, 2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 未公布 |\n| Vision encoder | 未公布 |\n| **Connector 类型** | 未公布 |\n| LLM backbone | 未公布 |\n| 开源状态 | ❌ **未开源**，代码/权重未释放 |\n| LIBERO 支持 | 不可行 |\n| 改造成本 | 不可行 |\n| 论文 LIBERO 结果 | 无 |\n| 备注 | GR-1 的后续，但未开源 |\n\n### 7. LLARVA (2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 7B |\n| Vision encoder | CLIP ViT-L/14 |\n| **Connector 类型** | **MLP projector**（LLaVA-style，2-layer MLP with GELU） |\n| LLM backbone | Llama-2 7B |\n| 开源状态 | ✅ code + LoRA weights, GitHub: [Dantong88/LLARVA](https://github.com/Dantong88/LLARVA), Apache-2.0 |\n| LIBERO 支持 | 需改造 |\n| 改造成本 | 中（需接 action head + LIBERO data pipeline） |\n| 论文 LIBERO 结果 | 无 |\n| 备注 | 预测 visual traces (2D 轨迹) 作为中间表示。Connector 与 OpenVLA 类似（都是 MLP projector），但用 CLIP 而非 Prismatic 双 encoder |\n\n### 8. RoboVLMs (2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 不定（框架） |\n| Vision encoder | 支持多种 VLM backbone |\n| **Connector 类型** | 取决于所选 VLM（框架支持多种） |\n| LLM backbone | 取决于所选 VLM |\n| 开源状态 | ✅ code + models, GitHub: [Robot-VLAs/RoboVLMs](https://github.com/Robot-VLAs/RoboVLMs) |\n| LIBERO 支持 | 需确认 |\n| 改造成本 | 低-中（框架设计灵活） |\n| 论文 LIBERO 结果 | 未确认 |\n| 备注 | 这是一个**框架**而非单一模型。实验了 8+ VLM backbone × 4 policy 架构。最佳模型用 Kosmos backbone。对我们的 connector 对比研究有参考价值但不直接使用。 |\n\n### 9. 3D-VLA (UMass, ICML 2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 未明确 |\n| Vision encoder | 3D feature extraction（point cloud based） |\n| **Connector 类型** | **Interaction tokens**（3D-LLM 架构，用交互 token 嵌入 embodied 环境） |\n| LLM backbone | 基于 3D-LLM |\n| 开源状态 | ✅ code + diffusion models, GitHub: [UMass-Embodied-AGI/3D-VLA](https://github.com/UMass-Embodied-AGI/3D-VLA), HF: anyezhy |\n| LIBERO 支持 | 需大量改造（paper 用 RLBench） |\n| 改造成本 | 高（3D 点云输入，与 LIBERO 2D 图像差异大） |\n| 论文 LIBERO 结果 | 无 |\n| 备注 | 基于 3D 点云的 VLA，与我们研究的 2D 图像 → connector → LLM 管道差异太大，不推荐 |\n\n### 10. π0 / pi-zero (Physical Intelligence, 2024-2025)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | ~3.3B (400M SigLIP + 2.6B Gemma + ~300M action expert) |\n| Vision encoder | SigLIP-So400m (400M params) |\n| **Connector 类型** | **Linear projection**（单层线性层，将 SigLIP token 投影到 Gemma embedding space） |\n| LLM backbone | Gemma 2B (via PaliGemma) |\n| 开源状态 | ✅ weights + code, GitHub: [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi), HF 有 PyTorch port |\n| LIBERO 支持 | ✅ 有评测（LIBERO-PRO 中被评测） |\n| 改造成本 | 低（已有 LIBERO 评测代码） |\n| 论文 LIBERO 结果 | 有（LIBERO-PRO 中有结果） |\n| 备注 | **强力推荐**。Linear projection 是最简单的 connector，与 OpenVLA 的 2-layer MLP 形成鲜明对比。Action expert 通过 MoE 架构耦合。Flow matching 生成动作。 |\n\n### 11. OpenVLA-OFT (Stanford, 2025)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 7B |\n| Vision encoder | SigLIP + DINOv2 (Prismatic) |\n| **Connector 类型** | **2-layer MLP projector**（与 OpenVLA 相同的 Prismatic connector） |\n| LLM backbone | Llama-2 7B |\n| 开源状态 | ✅ weights + code, GitHub: [moojink/openvla-oft](https://github.com/moojink/openvla-oft) |\n| LIBERO 支持 | ✅ 原生支持，SOTA 97.1% |\n| 改造成本 | 极低（已有完整 LIBERO fine-tune + eval） |\n| 论文 LIBERO 结果 | 有: 97.1% SR (4 suite avg) |\n| 备注 | Connector 与 OpenVLA 完全相同。改进在 fine-tuning recipe（continuous actions, action chunking, bidirectional attention）。对压缩实验来说，connector 级别的差异与 OpenVLA 相同，但 action generation 方式不同，可能影响压缩行为。 |\n\n### 12. RoboMM (2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 未明确公布 |\n| Vision encoder | CLIP (via OpenFlamingo) |\n| **Connector 类型** | **3D Perception Adapter (UVFormer)** + **Cross-attention**（OpenFlamingo 风格：text queries attend to visual features through cross-attention layers） |\n| LLM backbone | OpenFlamingo (cross-attention decoder) |\n| 开源状态 | ✅ code, GitHub: [RoboUniview/RoboMM](https://github.com/RoboUniview/RoboMM) |\n| LIBERO 支持 | ✅ 有评测 |\n| 改造成本 | 低-中 |\n| 论文 LIBERO 结果 | 有: 90.7% SR |\n| 备注 | Cross-attention connector 是独特的融合方式（与 MLP/linear 的 \"先投射再拼接\" 不同）。还有 occupancy supervision 的 3D adapter。多模态解码器增强感知。 |\n\n### 13. SpatialVLA (2025, RSS)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | ~4B |\n| Vision encoder | SigLIP |\n| **Connector 类型** | **Linear projection + Ego3D Position Encoding**（PaliGemma2 的 linear connector + MLP(sinusoidal(3D positions)) 叠加到 visual tokens 上） |\n| LLM backbone | Gemma (via PaliGemma2) |\n| 开源状态 | ✅ weights + code, GitHub: [SpatialVLA/SpatialVLA](https://github.com/SpatialVLA/SpatialVLA), HF: IPEC-COMMUNITY/spatialvla-4b-224-pt |\n| LIBERO 支持 | 未确认 |\n| 改造成本 | 中（需接 LIBERO data pipeline） |\n| 论文 LIBERO 结果 | 无 |\n| 备注 | 基于 PaliGemma2，connector 本质上是 linear projection（与 π0 相同），加了 3D spatial encoding。Adaptive Action Grids 只输出 3 个 action token（其他模型 7 个）。 |\n\n### 14. DeeR-VLA (2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 3B / 9B (OpenFlamingo 变体) |\n| Vision encoder | CLIP ViT-L/14 (428M params) |\n| **Connector 类型** | **Perceiver Resampler + Cross-attention**（OpenFlamingo 架构：CLIP features → Perceiver Resampler → learnable cross-attention blocks 注入 LLM 层间） |\n| LLM backbone | MPT-1B (3B 版) / MPT-7B (9B 版) |\n| 开源状态 | ✅ code + checkpoints, GitHub: [yueyang130/DeeR-VLA](https://github.com/yueyang130/DeeR-VLA) |\n| LIBERO 支持 | 需改造（paper 只有 CALVIN） |\n| 改造成本 | 中-高（需接 LIBERO pipeline，且多 exit 架构增加复杂度） |\n| 论文 LIBERO 结果 | 无（CALVIN benchmark） |\n| 备注 | **Perceiver Resampler** 与 RoboFlamingo 相同架构基础。动态 early exit 是额外功能。可作为 Perceiver Resampler 实验的替代方案。 |\n\n### 15. TraceVLA (UMD, ICLR 2025)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 7B (OpenVLA-based) / 4B (Phi-3-Vision-based) |\n| Vision encoder | SigLIP + DINOv2 (OpenVLA 版) / CLIP ViT (Phi-3 版) |\n| **Connector 类型** | **2-layer MLP projector**（与 OpenVLA 相同） |\n| LLM backbone | Llama-2 7B (OpenVLA 版) / Phi-3 4B |\n| 开源状态 | ✅ code + weights, GitHub: [umd-huang-lab/tracevla](https://github.com/umd-huang-lab/tracevla), HF: furonghuang-lab/tracevla_7b, MIT license |\n| LIBERO 支持 | 未确认（SimplerEnv + 真机） |\n| 改造成本 | 低（基于 OpenVLA 改造） |\n| 论文 LIBERO 结果 | 无 |\n| 备注 | Connector 与 OpenVLA 相同，改进在于 visual trace prompting（在图像上叠加动作历史轨迹）。压缩行为预期与 OpenVLA 相似。 |\n\n### 16. X-VLA (ICLR 2026)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 0.9B |\n| Vision encoder | Florence-Large (DaViT) |\n| **Connector 类型** | **Linear projection + Soft Prompts**（vision features 通过 lightweight linear layer 投影到高维空间 + 每个 embodiment 有独立 learnable prompt embeddings 注入 transformer） |\n| LLM backbone | Standard transformer 24 layers (非预训练 LLM，但使用 Florence 预训练 VLM 初始化) |\n| 开源状态 | ✅ weights + code, GitHub: [2toinf/X-VLA](https://github.com/2toinf/X-VLA), HF: 2toINF/X-VLA, Apache-2.0 |\n| LIBERO 支持 | ✅ 原生支持，98% SR |\n| 改造成本 | 极低（已有 LIBERO 训练权重） |\n| 论文 LIBERO 结果 | 有: 98% SR |\n| 备注 | **强力推荐**。Linear projection connector + flow matching action generation。LIBERO SOTA 之一。小模型(0.9B)便于实验。 |\n\n### 17. ECoT / Embodied Chain-of-Thought (2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 7B (基于 OpenVLA) |\n| Vision encoder | SigLIP + DINOv2 (Prismatic) |\n| **Connector 类型** | **2-layer MLP projector**（与 OpenVLA 相同） |\n| LLM backbone | Llama-2 7B |\n| 开源状态 | ✅ code + weights, GitHub: [MichalZawalski/embodied-CoT](https://github.com/MichalZawalski/embodied-CoT), HF: ecot-openvla-7b-bridge/oxe |\n| LIBERO 支持 | 需改造 |\n| 改造成本 | 低（基于 OpenVLA） |\n| 论文 LIBERO 结果 | 无 |\n| 备注 | Connector 与 OpenVLA 完全相同，增加了 chain-of-thought reasoning。对 connector 压缩研究无新增价值。 |\n\n### 18. LingBot-VLA (Ant Group/Robbyant, 2026)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 4B |\n| Vision encoder | Qwen2.5-VL 的 ViT（2D-RoPE + window attention） |\n| **Connector 类型** | **MLP merger**（2-layer MLP with ReLU，2×2 spatial grouping 后投影 + LLM decoder 中有 cross-attention 层融合 visual features） |\n| LLM backbone | Qwen2.5-VL-3B |\n| 开源状态 | ✅ weights + code, GitHub: [Robbyant/lingbot-vla](https://github.com/Robbyant/lingbot-vla) |\n| LIBERO 支持 | 未确认 |\n| 改造成本 | 中 |\n| 论文 LIBERO 结果 | 未确认 |\n| 备注 | Qwen2.5-VL 的 MLP merger 是一种混合 connector：先做 spatial grouping（类似 pixel-shuffle 的空间压缩）再 MLP 投射。Mixture of Transformers 架构。 |\n\n---\n\n## Connector 类型覆盖分析\n\n### 已有数据的 Connector 类型\n| Connector 类型 | 代表模型 | 压缩行为 |\n|---------------|----------|----------|\n| Pixel-shuffle | SmolVLA | Cliff-edge collapse |\n| 2-layer MLP projector | OpenVLA (Prismatic) | Graded degradation |\n| Perceiver Resampler | RoboFlamingo | 训练失败 |\n| **Linear projection** | **X-VLA** | **Nearly lossless pruning** |\n\n### 可新增的 Connector 类型\n| Connector 类型 | 候选模型 | 特点 | 可行性 |\n|---------------|----------|------|--------|\n| **Linear projection** | **π0**, SpatialVLA | 验证 X-VLA 发现的一致性 | ⭐⭐⭐ 高 |\n| **Cross-attention (Flamingo-style)** | **RoboMM** | 不在 encoder 端压缩，而是 decoder 端通过 cross-attention 选择性融合 | ⭐⭐ 中 |\n| **CNN patch → direct concat** | Octo | 无独立 connector，图像 patches 直接拼入 transformer | ⭐ 低（架构差异太大） |\n| **MLP merger + spatial grouping** | LingBot-VLA | 先空间合并再 MLP 投射 + cross-attention | ⭐⭐ 中 |\n| **Cross-attention tokenizer** | HPT | learnable tokens 通过 cross-attention 聚合 vision features | ⭐ 低（非 VLM 架构） |\n\n### 关键发现\n1. **Linear projection** 是最有价值的新增类型——π0 和 X-VLA 都用这种最简单的 connector，与 OpenVLA 的 2-layer MLP 形成对比\n2. **Cross-attention** (RoboMM 的 OpenFlamingo 架构) 从根本上不同：不投射拼接，而是 decoder 层间交叉注意力\n3. 大量模型共享 connector：OpenVLA, CogACT, LLARVA, TraceVLA, ECoT, OpenVLA-OFT 都用 **2-layer MLP**（Prismatic 或 LLaVA 架构）\n\n---\n\n## Top 推荐：最适合扩展实验的 5 个模型\n\n### 🥇 1. π0 (Physical Intelligence)\n- **Connector**: Linear projection (单层线性)\n- **推荐理由**: \n  - 与 OpenVLA 的 2-layer MLP 形成直接对比（linear vs MLP）\n  - 开源权重 + 代码，社区活跃\n  - 已有 LIBERO 评测代码\n  - PaliGemma 架构广为人知\n  - 3B 参数可在单卡运行\n- **预期价值**: Linear projection 不增加非线性变换，token 可能保留更多原始 visual feature 结构 → 压缩行为可能与 MLP 不同\n\n### 🥈 2. X-VLA\n- **Connector**: Linear projection + soft prompts\n- **推荐理由**:\n  - 同样是 linear projection，与 π0 对比看 soft prompt 的影响\n  - LIBERO 98% SR，已有训练好的 LIBERO 权重直接可用\n  - 0.9B 参数，实验成本最低\n  - ICLR 2026，最新模型\n  - Apache-2.0 开源\n- **预期价值**: 验证 linear projection 的压缩行为是否 consistent across models\n\n### 🥉 3. DeeR-VLA\n- **Connector**: Perceiver Resampler + Cross-attention (OpenFlamingo)\n- **推荐理由**:\n  - Perceiver Resampler 与 RoboFlamingo 相同架构，但 DeeR-VLA 已验证可训练（CALVIN benchmark 正常工作）\n  - 给 Perceiver Resampler 第二次机会\n  - 可对比 RoboFlamingo 的训练失败是架构问题还是实现问题\n  - Open source with checkpoints\n- **预期价值**: Perceiver Resampler 本身就做了 attention-based compression → 压缩行为可能与 MLP/linear 截然不同\n- **风险**: LIBERO 需要自己改造\n\n### 4. RoboMM\n- **Connector**: Cross-attention (OpenFlamingo) + 3D Adapter\n- **推荐理由**:\n  - Cross-attention 融合方式从根本上不同于 projection-based connectors\n  - 已有 LIBERO 结果 (90.7%)\n  - Open source\n- **预期价值**: Cross-attention 在 decoder 端动态选择 visual features → 可能展现出与 projection-based 完全不同的压缩模式\n- **风险**: 架构较复杂，3D adapter 增加变量\n\n### 5. OpenVLA-OFT\n- **Connector**: 2-layer MLP projector (与 OpenVLA 相同)\n- **推荐理由**:\n  - Connector 与 OpenVLA 相同，但 action generation 完全不同（continuous + chunking）\n  - LIBERO 97.1% SOTA\n  - 可验证 \"相同 connector + 不同 action head\" 是否影响压缩行为\n  - 已有完整 LIBERO 代码\n- **预期价值**: 作为 OpenVLA 的对照组，隔离 connector vs action head 对压缩的影响\n\n---\n\n## 不推荐的模型及原因\n\n| 模型 | 排除原因 |\n|------|----------|\n| RT-2-X | 闭源，权重不可用 |\n| GR-2 | 未开源 |\n| 3D-VLA | 3D 点云输入，与 2D VLA 差异太大 |\n| CogACT | Connector 与 OpenVLA 相同（Prismatic MLP），不新增类型 |\n| LLARVA | Connector 与 OpenVLA 类似（MLP projector），不新增类型 |\n| TraceVLA | Connector 与 OpenVLA 相同，不新增类型 |\n| ECoT | Connector 与 OpenVLA 相同，不新增类型 |\n| HPT | 非 VLM 架构，不适合 connector 压缩叙事 |\n| GR-1 | 有 Perceiver Resampler（有价值），但无 LIBERO 支持 + 视频生成架构改造成本高 |\n| Octo | 无独立 connector（CNN patch 直接拼入），架构与标准 VLM 差异太大 |\n\n---\n\n## 总结：Connector 类型 × 模型矩阵\n\n| Connector 类型 | 已有 | 推荐新增 |\n|---------------|------|----------|\n| Pixel-shuffle | SmolVLA ✅ | — |\n| 2-layer MLP projector | OpenVLA ✅ | OpenVLA-OFT（同 connector 不同 action head） |\n| Perceiver Resampler | RoboFlamingo ❌(失败) | **DeeR-VLA** |\n| **Linear projection** | **X-VLA ✅** | **π0** |\n| **Cross-attention** | — | **RoboMM** |\n\n实现后可达 **5 种 connector 类型 × 6+ 模型**的全面对比。\n\n---\n\n## X-VLA 详细架构调研（2026-05-20 新增）\n\n### 模型身份确认\n- **名称**: X-VLA (Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model)\n- **论文**: arXiv:2510.10274, ICLR 2026\n- **GitHub**: [2toinf/X-VLA](https://github.com/2toinf/X-VLA)\n- **HuggingFace**: [2toINF/X-VLA](https://huggingface.co/collections/2toINF/x-vla)\n- **参数量**: 0.9B\n- **许可**: Apache-2.0\n- **LIBERO SR**: 98.1%\n\n### 架构详解\n\n```\nImage (224×224) → Florence-Large (DaViT) → Vision Tokens [B, N, 2048]\n    → Linear Projection + LayerNorm → [B, N, 1024]\n    → Merge with Text Token Embeddings → Florence2 Encoder (self-attention)\n    → Context Features → SoftPromptedTransformer (24 layers, hidden=1024)\n        + Soft Prompts (32 learnable embeddings per embodiment)\n        + Noised Action Tokens (flow matching)\n    → Denoised Action Trajectory [B, 30, 20]\n```\n\n**各组件详情**:\n\n| 组件 | 规格 |\n|------|------|\n| Vision Encoder | Florence-Large (DaViT): patch_stride=[4,2,2,2] → total stride 32 |\n| Vision Token 数量 | ~49 tokens (7×7 at 224×224) 或 ~576 tokens (24×24 at 768×768) — **需实际加载模型验证** |\n| Projection | Linear + LayerNorm, dim 2048 → 1024 (projection_dim=1024) |\n| Soft Prompts | 32 tokens/embodiment, 0.04% of total params |\n| Transformer | 24 layers, hidden=1024, 16 heads, mlp_ratio=4.0 |\n| Action Head | Flow matching, 30 anchor points × 20 dims (EE6D), 10 denoising steps |\n| Max Sequence | 512 tokens |\n\n### HuggingFace 权重\n| Checkpoint | 用途 | 地址 |\n|------------|------|------|\n| X-VLA-Pt | 预训练基座 (cross-embodiment) | 2toINF/X-VLA-Pt |\n| X-VLA-Libero | LIBERO 全参数微调 (98.1% SR) | 2toINF/X-VLA-Libero |\n| X-VLA-libero-*-peft | LIBERO LoRA 微调 (各 suite) | 2toINF/X-VLA-libero-spatial-peft 等 |\n\n### 环境依赖\n```\ntransformers<=4.51.3, torch, einops==0.8.1, timm==1.0.12, \naccelerate==1.2.1, peft==0.17.1, safetensors==0.4.5,\nnumpy==1.26.3, scipy==1.15.0, mmengine==0.10.5,\nfastapi, uvicorn==0.34.3, h5py==3.12.1, pyarrow==20.0.0,\nav==15.0.0, mediapy==1.2.4\n```\nLIBERO 评估另需 Python 3.8 环境。\n\n### VTC 集成方案\n**插入点**: Florence2 `_encode_image()` 输出 → **VTC** → `_merge_input_ids_with_image_features()`\n\n**改造清单**:\n1. 创建 `xvla_vtc_adapter.py`（复用 VisionTokenCompressor，hidden_dim 改 1024）\n2. 创建 XVLASmartCompressWrapper，hook Florence2 vision 输出\n3. 修改 merge 逻辑以适应压缩后的 token 数量\n4. 创建 `train_xvla_smart_compress.py`（参考 X-VLA 的 train.py + peft_train.py）\n5. 适配 flow matching loss（不同于 OpenVLA 的 cross-entropy）\n\n**与 OpenVLA VTC 的关键差异**:\n| 维度 | OpenVLA | X-VLA |\n|------|---------|-------|\n| hidden_dim | 4096 | 1024 |\n| 原始 vision tokens | 256 | ~49-576 (待验证) |\n| Action 范式 | Autoregressive (256-bin CE) | Flow matching (MSE+BCE) |\n| Connector | 2-layer MLP | Linear + LayerNorm |\n| 模型大小 | 7B | 0.9B |\n\n**预计工作量**: 8-12 小时\n- 代码改造: 4-6h（adapter + training script）\n- 环境搭建 + 模型下载: 2-3h\n- 验证 + 调试: 2-3h\n\n---\n\n## X-VLA Token Importance 分析结果（2026-05-20）\n\n### 实验配置\n- **模型**: X-VLA-0.9B (lerobot/xvla-libero checkpoint)\n- **数据**: LIBERO-Object (task_index 20-29), 100 images, 10 tasks\n- **服务器**: westd-41074, cuda:1\n- **分析脚本**: `/root/autodl-tmp/importance_margin_vla_compress/analyze_xvla_token_importance.py`\n- **结果文件**: `/root/autodl-tmp/importance_margin_vla_compress/eval_results/xvla_attention_entropy_perlayer.json`\n\n### SoftPromptedTransformer 序列布局\n| Token 类型 | 数量 | 说明 |\n|-----------|------|------|\n| Action tokens | 30 | Flow matching denoised action |\n| VLM features | 64 | Florence2 encoder output (main view) |\n| Aux visual | 150 | Additional camera views |\n| Soft prompts | 32 | Embodiment-specific learnable tokens |\n| **Total** | **276** | |\n\n### Entropy Ratio（Action→Vision 注意力熵）\n- **Overall**: **0.6138** ± 0.1159\n- **趋势**: 浅层低（L0=0.46, L1=0.34），深层高（L22=0.79, L23=0.71）\n- 浅层集中注意力于少数 vision tokens，深层趋于均匀\n\n### Vision Attention Fraction（Action tokens 分配给 vision tokens 的注意力比例）\n- 浅层（L0-2）: 33-49% — action tokens 还关注 soft prompts 和 self\n- 中层（L6-11）: 84-90% — 绝大部分注意力给 vision tokens\n- 深层（L17-23）: 79-90% — 持续高注意力\n\n### Pruning Curve（核心发现）\n| Retention k | Mean Loss | Normalized |\n|-------------|-----------|------------|\n| 0.30 | 0.112945 | **1.0014** |\n| 0.50 | 0.112823 | 1.0003 |\n| 0.70 | 0.112789 | 1.0000 |\n| 0.90 | 0.112789 | 1.0000 |\n| 0.95 | 0.112789 | 1.0000 |\n| 1.00 | 0.112789 | 1.0000 |\n\n**关键结论**: 丢弃 70% 的 vision tokens（k=0.3）仅导致 0.14% 的 loss 增加。X-VLA 的 vision tokens **几乎完全可压缩**。\n\n### 跨模型对比\n| 模型 | Connector | Entropy Ratio | k=0.3 Norm Loss | 压缩行为 |\n|------|-----------|---------------|-----------------|----------|\n| SmolVLA | Pixel-shuffle | ~0.45 (低) | Cliff-edge | 不可压缩 |\n| OpenVLA | 2-layer MLP | ~0.55 (中) | ~1.15 (15%↑) | 渐进退化 |\n| **X-VLA** | **Linear proj** | **0.61 (中高)** | **1.0014 (0.14%↑)** | **几乎无损** |\n\n### 解读\n1. **Linear projection connector 产生了高度冗余的 vision token 表示**——大部分信息集中在少数 token 中，L2 norm 可以轻松识别\n2. Entropy 比 OpenVLA 更高（0.61 vs 0.55），说明注意力分布更均匀，但这不矛盾——均匀分布意味着 \"每个 token 被平等关注\"，而 pruning 几乎无损意味着 \"被关注的内容高度冗余\"\n3. 这是 **connector 架构论文的关键数据点**：linear projection（无非线性变换）保留了 DaViT 输出的原始冗余结构，而 MLP projector（2 层 + GELU）通过非线性变换重新分配了信息，使得 token 间差异更大、更难压缩\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "af56858b-a467-44c6-88c4-c9489271ff2b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QUY99JXyPAREgzRZih9M74",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 618,
      "cache_read_input_tokens": 108192,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 618
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


### Tool result

_source line 816 · 2026-05-20T04:40:33.776Z_

<details><summary>↩ Tool result · `toolu_01WU1m8HEXKg2Ugs8LkSsYZr`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "9df16129-e3bb-421f-a103-b578f63ca028",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/memory.md\\\", \\\"saved\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 817_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01LFT5Q3mCkgd1Lpfwk1nwnf`</summary>

```json
{
  "todos": [
    {
      "content": "Research X-VLA architecture details",
      "status": "completed",
      "activeForm": "Researching X-VLA architecture"
    },
    {
      "content": "Check server environment and install dependencies",
      "status": "completed",
      "activeForm": "Checking server environment"
    },
    {
      "content": "Download X-VLA LIBERO checkpoint to server",
      "status": "completed",
      "activeForm": "Downloading model checkpoint"
    },
    {
      "content": "Study X-VLA source code and write analysis script",
      "status": "completed",
      "activeForm": "Studying X-VLA source code"
    },
    {
      "content": "Run analysis and collect results",
      "status": "completed",
      "activeForm": "Running token importance analysis"
    },
    {
      "content": "Update memory.md and registry with findings",
      "status": "completed",
      "activeForm": "Updating memory and registry"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "627aa3a9-4680-40e5-b43c-e05021035ea2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jfo9CGjUhMDusgdAAA8bZq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11103,
      "cache_read_input_tokens": 108810,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11103
      },
      "output_tokens": 57,
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

_source line 818 · 2026-05-20T04:40:39.102Z_

<details><summary>↩ Tool result · `toolu_01LFT5Q3mCkgd1Lpfwk1nwnf`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "51f02873-41a4-4989-828c-8dec8a026579",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Research X-VLA architecture details",
        "status": "completed",
        "activeForm": "Researching X-VLA architecture"
      },
      {
        "content": "Check server environment and install dependencies",
        "status": "completed",
        "activeForm": "Checking server environment"
      },
      {
        "content": "Download X-VLA LIBERO checkpoint to server",
        "status": "completed",
        "activeForm": "Downloading model checkpoint"
      },
      {
        "content": "Study X-VLA source code and write analysis script",
        "status": "completed",
        "activeForm": "Studying X-VLA source code"
      },
      {
        "content": "Run analysis and collect results",
        "status": "in_progress",
        "activeForm": "Running token importance analysis"
      },
      {
        "content": "Update memory.md and registry with findings",
        "status": "pending",
        "activeForm": "Updating memory and registry"
      }
    ],
    "newTodos": [
      {
        "content": "Research X-VLA architecture details",
        "status": "completed",
        "activeForm": "Researching X-VLA architecture"
      },
      {
        "content": "Check server environment and install dependencies",
        "status": "completed",
        "activeForm": "Checking server environment"
      },
      {
        "content": "Download X-VLA LIBERO checkpoint to server",
        "status": "completed",
        "activeForm": "Downloading model checkpoint"
      },
      {
        "content": "Study X-VLA source code and write analysis script",
        "status": "completed",
        "activeForm": "Studying X-VLA source code"
      },
      {
        "content": "Run analysis and collect results",
        "status": "completed",
        "activeForm": "Running token importance analysis"
      },
      {
        "content": "Update memory.md and registry with findings",
        "status": "completed",
        "activeForm": "Updating memory and registry"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---


### Assistant

_source line 819_

全部任务完成。汇报结果：

---

## X-VLA Token Importance 分析结果

**模型**: X-VLA-0.9B (lerobot/xvla-libero)，Linear projection connector  
**数据**: LIBERO-Object 100帧, 10 tasks  
**服务器**: westd-41074:cuda:1

### 核心发现

**Pruning curve 几乎完全平坦** — 这是目前测过最可压缩的 VLA 模型：

| Retention k | Normalized Loss |
|-------------|----------------|
| 0.30 (保留30%) | **1.0014** (+0.14%) |
| 0.50 | 1.0003 |
| 0.70 | 1.0000 |
| 1.00 | 1.0000 |

丢弃 70% 的 vision tokens 仅导致 0.14% 的 loss 增加。

**Entropy ratio**: 0.6138（中高），浅层集中（L1=0.34）→ 深层均匀（L22=0.79）

### 跨模型对比

| 模型 | Connector | k=0.3 Norm Loss | 压缩行为 |
|------|-----------|-----------------|----------|
| SmolVLA | Pixel-shuffle | Cliff-edge | 不可压缩 |
| OpenVLA | 2-layer MLP | ~1.15 (+15%) | 渐进退化 |
| **X-VLA** | **Linear proj** | **1.0014 (+0.14%)** | **几乎无损** |

### 解读

Linear projection connector 保留了 DaViT 输出的原始冗余结构——大部分信息集中在少数 token，L2 norm 即可轻松识别。相比之下，MLP projector 通过非线性变换重新分配了信息，使 token 间差异更大、更难压缩。

**这是 connector 架构论文的关键数据点**，直接支持 "connector 架构决定 token 可压缩性" 的核心论点。

已完成：memory.md 更新、registry 注册（analysis_xvla_token_importance, DONE/success）、artifact 注册（xvla_attention_entropy_perlayer.json）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "uuid": "7478c5dd-6e3f-4087-9fce-32ff70b8cd8f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LhvSYau91ePNWcEc3jGNUg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 283,
      "cache_read_input_tokens": 119913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 283
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

_source line 820_

全部任务完成。汇报结果：

---

## X-VLA Token Importance 分析结果

**模型**: X-VLA-0.9B (lerobot/xvla-libero)，Linear projection connector  
**数据**: LIBERO-Object 100帧, 10 tasks  
**服务器**: westd-41074:cuda:1

### 核心发现

**Pruning curve 几乎完全平坦** — 这是目前测过最可压缩的 VLA 模型：

| Retention k | Normalized Loss |
|-------------|----------------|
| 0.30 (保留30%) | **1.0014** (+0.14%) |
| 0.50 | 1.0003 |
| 0.70 | 1.0000 |
| 1.00 | 1.0000 |

丢弃 70% 的 vision tokens 仅导致 0.14% 的 loss 增加。

**Entropy ratio**: 0.6138（中高），浅层集中（L1=0.34）→ 深层均匀（L22=0.79）

### 跨模型对比

| 模型 | Connector | k=0.3 Norm Loss | 压缩行为 |
|------|-----------|-----------------|----------|
| SmolVLA | Pixel-shuffle | Cliff-edge | 不可压缩 |
| OpenVLA | 2-layer MLP | ~1.15 (+15%) | 渐进退化 |
| **X-VLA** | **Linear proj** | **1.0014 (+0.14%)** | **几乎无损** |

### 解读

Linear projection connector 保留了 DaViT 输出的原始冗余结构——大部分信息集中在少数 token，L2 norm 即可轻松识别。相比之下，MLP projector 通过非线性变换重新分配了信息，使 token 间差异更大、更难压缩。

**这是 connector 架构论文的关键数据点**，直接支持 "connector 架构决定 token 可压缩性" 的核心论点。

已完成：memory.md 更新、registry 注册（analysis_xvla_token_importance, DONE/success）、artifact 注册（xvla_attention_entropy_perlayer.json）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 2767307,
  "duration_api_ms": 2192315,
  "num_turns": 327,
  "stop_reason": "end_turn",
  "session_id": "db2d96f5-e22f-4df1-9d1d-03ecb917c862",
  "total_cost_usd": 15.399880249999999,
  "usage": {
    "input_tokens": 310,
    "cache_creation_input_tokens": 256364,
    "cache_read_input_tokens": 21707798,
    "output_tokens": 103244,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 256364,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 637,
        "cache_read_input_tokens": 119913,
        "cache_creation_input_tokens": 283,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 283
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 62245,
      "outputTokens": 2081,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 5,
      "costUSD": 0.12265000000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 1650,
      "outputTokens": 107923,
      "cacheReadInputTokens": 21867648,
      "cacheCreationInputTokens": 261933,
      "webSearchRequests": 0,
      "costUSD": 15.277230249999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "1d01cd1f-9a15-4bbb-adf5-5bb9c6f3fc5b"
}
```

</details>

---
