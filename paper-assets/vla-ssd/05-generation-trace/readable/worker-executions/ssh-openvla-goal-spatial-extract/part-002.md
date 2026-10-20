# ssh openvla goal spatial extract — Part 2 of 2

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../ssh-openvla-goal-spatial-extract.md) · [Structured JSON](../../../sessions/51/518f6ab50d7d57d0836f.json)

## Before a recorded user message

### Tool result

_source line 117 · 2026-05-22T00:24:57.657Z_

<details><summary>↩ Tool result · `toolu_01PXtw1UA9mDsjHTWEhCFoSZ`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/openvla_goal_spatial_data.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1a1d35cc-96c1-45e9-a484-057e8b339347",
  "uuid": "f82feada-e178-4e32-9f5b-579575bef008",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/openvla_goal_spatial_data.md",
    "content": "# OpenVLA Goal & Spatial 实验数据汇总\n\n## 数据来源映射\n\n| 目录/文件 | 对应 Suite | 内容 |\n|-----------|-----------|------|\n| `trained/action_prediction/` | LIBERO-Long | R² probing (非 Goal/Spatial) |\n| `functional_validation/action_probe_libero_spatial.json` | LIBERO-Spatial | R² probing (trained+untrained, 33层) |\n| `attention/l1_attention_trained_summary.json` | LIBERO-Goal | L1 attention per-task |\n| `attention/l1_attention_untrained_summary.json` | LIBERO-Goal | L1 attention aggregate |\n| `attention/full_32layer_attention_summary.json` | LIBERO-Goal | 全层 attention (含 n_instruction_dominant) |\n| `cross_instruction/classification_results.json` | LIBERO-Goal | Cross-instruction classification |\n| `cross_instruction_spatial/classification_results.json` | LIBERO-Spatial | Cross-instruction classification |\n| `counterfactual_10tasks/` | LIBERO-Goal | CF (trained model only) |\n| `counterfactual_spatial/` | LIBERO-Spatial | CF (trained model only) |\n\n---\n\n## OpenVLA Spatial\n\n### R² Probing (from `action_probe_libero_spatial.json`)\n\n| Condition | Representation | Peak Layer | Peak R² | Exit (L32) R² |\n|-----------|---------------|------------|---------|---------------|\n| Trained | image_mean | L13 | 0.696 | — |\n| Trained | last_preaction | L21 | 0.675 | — |\n| Untrained | image_mean | L0 | 0.673 | 0.621 |\n| Untrained | last_preaction | L1 | 0.635 | 0.621 |\n\nBootstrap trained vs untrained (image_mean, best-vs-best): Δ=0.023, p=0.0, CI=[0.012, 0.036]\n\n### L1 Attention\n\n**无 Spatial 专用 L1 attention 数据。** `attention/` 目录下的数据是 Goal 任务。\n\n### Cross-Instruction Classification (from `cross_instruction_spatial/`)\n\n| Condition | Representation | L1 | L4 | L8 | L16 | L24 | L31 |\n|-----------|---------------|-----|-----|-----|------|------|------|\n| Trained | last_preaction | 0.989 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |\n| Trained | image_mean | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 0.101 |\n| Untrained | last_preaction | 0.995 | 0.862 | 0.683 | 0.765 | 0.777 | 0.754 |\n| Untrained | image_mean | 0.1 | 0.1 | 0.101 | 0.1 | 0.1 | 0.1 |\n\nChance = 0.1 (10-class)\n\n### Counterfactual (from `counterfactual_spatial/`, trained model only)\n\n| Condition | Cohen's d (token-level) | Paired MSE | Token Divergence Rate |\n|-----------|------------------------|------------|----------------------|\n| empty | 0.942 | 0.0659 | 0.914 |\n| wrong | 0.851 | 0.0580 | 0.865 |\n| shuffled | 0.833 | 0.0570 | 0.877 |\n| paraphrased | 0.806 | 0.0547 | 0.799 |\n\nTop condition: **empty** (d=0.942)\n\n---\n\n## OpenVLA Goal\n\n### R² Probing\n\n**无 Goal 专用 R² probing 数据。** `trained/action_prediction/` 的数据是 LIBERO-Long (复合多步任务)，非 Goal。\n\n附 LIBERO-Long 数据供参考：\n- Trained: peak R²=0.683 (L19, per_task_mean), overall_r2=0.677\n- Untrained: peak R²=0.616 (L32, per_task_mean), overall_r2=0.607\n\n### L1 Attention (from `full_32layer_attention_summary.json` + `l1_attention_*_summary.json`)\n\n| Condition | Instruction-Dominant Heads | Total Heads | Mean Text Attn | Mean Image Attn |\n|-----------|---------------------------|-------------|---------------|----------------|\n| Trained | 24 | 32 | 0.573 | 0.217 |\n| Untrained | 0 | 32 | 0.117 | 0.878 |\n\nTrained 任务：open_the_middle_drawer, push_the_plate_to_the_front, put_the_wine_bottle_on_top 等 LIBERO-Goal 任务。\n\n### Cross-Instruction Classification (from `cross_instruction/`)\n\n| Condition | Representation | L0 | L8 | L16 | L24 | L31 |\n|-----------|---------------|-----|-----|------|------|------|\n| Trained | last_preaction | 0.1 | 1.0 | 1.0 | 1.0 | 1.0 |\n| Trained | image_mean | 0.1 | 0.1 | 0.1 | 0.1 | 0.096 |\n| Untrained | last_preaction | 0.1 | 0.982 | 0.923 | 0.864 | 0.82 |\n| Untrained | image_mean | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 |\n\nChance = 0.1 (10-class)\n\n### Counterfactual (from `counterfactual_10tasks/`, trained model only)\n\n**Token-level:**\n\n| Condition | Cohen's d | Paired MSE | Token Divergence Rate |\n|-----------|----------|------------|----------------------|\n| empty | 0.978 | 0.0691 | 0.913 |\n| wrong | 0.924 | 0.0647 | 0.908 |\n| shuffled | 0.763 | 0.0512 | 0.871 |\n| paraphrased | 0.707 | 0.0462 | 0.830 |\n\n**Trajectory-level (from `trajectory_level_cohens_d.json`):**\n\n| Condition | Cohen's d | 95% CI | Mean MSE |\n|-----------|----------|--------|----------|\n| empty | 3.848 | [3.409, 4.440] | 0.0691 |\n| wrong | 2.992 | [2.634, 3.491] | 0.0647 |\n| paraphrased | 2.353 | [2.092, 2.678] | 0.0462 |\n| shuffled | 2.127 | [1.857, 2.459] | 0.0512 |\n\nTop condition: **empty** (token d=0.978, trajectory d=3.848)\n\n---\n\n## NORA Spatial Untrained CF 状态\n\n**缺失。** `/root/autodl-tmp/vla-ssd/results/nora_spatial/untrained/` 目录下仅有：\n- `action_r2_probing.json` ✓\n- `l1_attention_profile.json` ✓ (14/16 instruction-dominant heads)\n- `cross_instruction_classification.json` ✓ (all layers ≈ 1.0)\n- `counterfactual_combined.json` ✗ **不存在**\n\nNORA Spatial untrained 的 cross-instruction 数据显示所有层 image_mean ≈ 0.999, last_preaction = 1.0，说明 SigLIP 视觉编码器提供了极强的任务可分性，但 CF 需要单独运行。\n\n---\n\n## 可直接填入汇总表的数据行\n\n### OpenVLA Spatial\n\n| Metric | Trained | Untrained |\n|--------|---------|-----------|\n| R² peak (image_mean) | 0.696 (L13) | 0.673 (L0) |\n| R² peak (last_preaction) | 0.675 (L21) | 0.635 (L1) |\n| L1 instr-dominant heads | N/A (no spatial data) | N/A |\n| Cross-inst peak acc | 1.0 (L4+) | 0.995 (L1) |\n| Cross-inst exit acc (L31) | 1.0 | 0.754 |\n| CF top condition | empty | — |\n| CF top Cohen's d | 0.942 | — |\n\n### OpenVLA Goal\n\n| Metric | Trained | Untrained |\n|--------|---------|-----------|\n| R² peak (image_mean) | N/A (no goal data) | N/A |\n| L1 instr-dominant heads | 24/32 | 0/32 |\n| Cross-inst peak acc | 1.0 (L8+) | 0.995 (L1) |\n| Cross-inst exit acc (L31) | 1.0 | 0.82 |\n| CF top condition | empty | — |\n| CF top Cohen's d (token) | 0.978 | — |\n| CF top Cohen's d (traj) | 3.848 | — |\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---


### Assistant

_source line 118_

数据已提取并写入 `artifacts/openvla_goal_spatial_data.md`。

关键发现：

**数据缺失项：**
- OpenVLA Goal **无 R² probing 数据**（`trained/action_prediction/` 实际是 LIBERO-Long，不是 Goal）
- OpenVLA Spatial **无 L1 attention 数据**（`attention/` 目录下的数据是 Goal 任务）
- NORA Spatial untrained **CF 缺失**（目录下无 `counterfactual_combined.json`）

**可用数据摘要：**

| | OpenVLA Goal | OpenVLA Spatial |
|--|--|--|
| R² peak | **缺失** | 0.696 (trained L13) / 0.673 (untrained L0) |
| L1 heads | 24/32 trained, 0/32 untrained | **缺失** |
| Cross-inst | 1.0 trained (L8+), 0.82 untrained (L31) | 1.0 trained (L4+), 0.754 untrained (L31) |
| CF top d | 0.978 empty (token), 3.85 (traj) | 0.942 empty (token) |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1a1d35cc-96c1-45e9-a484-057e8b339347",
  "uuid": "47b2daab-ab3b-4a5d-b851-4431673629bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UVD2SPvvkQNSVvf6hte4EN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2684,
      "cache_read_input_tokens": 144040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2684
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

_source line 119_

数据已提取并写入 `artifacts/openvla_goal_spatial_data.md`。

关键发现：

**数据缺失项：**
- OpenVLA Goal **无 R² probing 数据**（`trained/action_prediction/` 实际是 LIBERO-Long，不是 Goal）
- OpenVLA Spatial **无 L1 attention 数据**（`attention/` 目录下的数据是 Goal 任务）
- NORA Spatial untrained **CF 缺失**（目录下无 `counterfactual_combined.json`）

**可用数据摘要：**

| | OpenVLA Goal | OpenVLA Spatial |
|--|--|--|
| R² peak | **缺失** | 0.696 (trained L13) / 0.673 (untrained L0) |
| L1 heads | 24/32 trained, 0/32 untrained | **缺失** |
| Cross-inst | 1.0 trained (L8+), 0.82 untrained (L31) | 1.0 trained (L4+), 0.754 untrained (L31) |
| CF top d | 0.978 empty (token), 3.85 (traj) | 0.942 empty (token) |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 514705,
  "duration_api_ms": 512897,
  "num_turns": 50,
  "stop_reason": "end_turn",
  "session_id": "1a1d35cc-96c1-45e9-a484-057e8b339347",
  "total_cost_usd": 1.8954732500000004,
  "usage": {
    "input_tokens": 15,
    "cache_creation_input_tokens": 134883,
    "cache_read_input_tokens": 761283,
    "output_tokens": 26791,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 134883,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 336,
        "cache_read_input_tokens": 144040,
        "cache_creation_input_tokens": 2684,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2684
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1873,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001963,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 15,
      "outputTokens": 26791,
      "cacheReadInputTokens": 761283,
      "cacheCreationInputTokens": 134883,
      "webSearchRequests": 0,
      "costUSD": 1.89351025,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "62aff3ac-5400-4b5b-94d8-e90790a9e478"
}
```

</details>

---
