# analysis openvla long cf trained

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_analysis_openvla_long_cf_trained_20260521T224214.jsonl`
- **Structured JSON:** [`350acd90b1f9e4fa4273.json`](../../sessions/35/350acd90b1f9e4fa4273.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-21T22:43:19.632556+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_openvla_long_cf_trained_20260521T224214",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T22:43:19.632881+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_openvla_long_cf_trained_20260521T224214",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T22:43:19.633130+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "tail -200 ~/runs/vla-ssd/openvla_long_cf_trained.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_openvla_long_cf_trained_20260521T224214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "tail -200 ~/runs/vla-ssd/openvla_long_cf_trained.log"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T22:43:19.633285+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/results/ -name \"*long*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_openvla_long_cf_trained_20260521T224214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/results/ -name \"*long*\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-21T22:43:19.633496+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[05:09:38] Pipeline conditions: ['trained']\\n[05:09:38] === TRAINED ===\\n[05:09:38] Config: tasks=10 demos=10 timesteps=50 seeds=15 dry_run=False\\n[05:09:38] Checkpoint: /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-oft-finetuned-libero-10\\n[05:09:38] Output: /root/autodl-tmp/vla-ssd/results/libero_long\\n[05:09:38] Loading model ...\\nExpected `transformers==4.40.1` and `tokenizers==0.19.1` but got `transformers==4.48.3` and `tokenizers==0.21.4`; there might be inference-time regressions due to dependency changes. If in doubt, pleaseuse the above versions.\\n\\rLoading checkpoint shards:   0%|          | 0/4 [00:00<?, ?it/s]\\rLoading checkpoint shards:  25%|██▌       | 1/4 [00:00<00:00,  4.91it/s]\\rLoading checkpoint shards:  75%|███████▌  | 3/4 [00:00<00:00,  8.26it/s]\\rLoading checkpoint shards: 100%|██████████| 4/4 [00:00<00:00,  8.39it/s]\\nUsing a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.48, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.\\n[05:09:48] Model loaded in 10.8s\\n[05:09:48]   Merged norm_stats key: libero_10_no_noops\\n[05:09:48] Validating token layout ...\\n[05:09:49]   input_ids shape: torch.Size([1, 27])\\n[05:09:49]   pixel_values shape: torch.Size([1, 6, 224, 224])\\n`torch.nn.functional.scaled_dot_product_attention` does not support `output_attentions=True`. Falling back to eager attention. This warning can be removed using the argument `attn_implementation=\\\"eager\\\"` when loading the model.\\n[05:09:49]   hidden_states[0] shape: torch.Size([1, 283, 4096])\\n[05:09:49]   Token layout: BOS(1) + img(256) + text(26)\\n[05:09:49] Phase 6: counterfactual analysis\\n[05:09:49]   Condition: wrong\\n[05:10:39]     200/5000\\n[05:11:29]     400/5000\\n[05:12:22]  
…[truncated 3308 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_openvla_long_cf_trained_20260521T224214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T22:43:19.633657+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_openvla_long_cf_trained_20260521T224214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T22:43:19.633818+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls -la /root/autodl-tmp/vla-ssd/results/libero_long/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_openvla_long_cf_trained_20260521T224214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls -la /root/autodl-tmp/vla-ssd/results/libero_long/"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T22:43:19.633998+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 76\\ndrwxr-xr-x  2 root root  4096 May 22 06:39 .\\ndrwxr-xr-x 57 root root  8192 May 22 00:39 ..\\n-rw-r--r--  1 root root  6372 May 21 23:55 action_r2_probing.json\\n-rw-r--r--  1 root root 31694 May 22 06:39 counterfactual_combined.json\\n-rw-r--r--  1 root root  1727 May 21 23:59 cross_instruction_classification.json\\n-rw-r--r--  1 root root  4665 May 21 23:55 l1_attention_profile.json\\n-rw-r--r--  1 root root  7360 May 21 23:59 rsa_analysis.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_openvla_long_cf_trained_20260521T224214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T22:43:19.634143+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/libero_long/counterfactual_combined.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_openvla_long_cf_trained_20260521T224214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/libero_long/counterfactual_combined.json"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T22:43:19.634445+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"experiment\\\": \\\"counterfactual_libero_long\\\",\\n    \\\"conditions\\\": [\\n      \\\"wrong\\\",\\n      \\\"empty\\\",\\n      \\\"shuffled\\\",\\n      \\\"paraphrased\\\"\\n    ],\\n    \\\"n_tasks\\\": 10,\\n    \\\"n_demos_per_task\\\": 10,\\n    \\\"n_timesteps_per_demo\\\": 50,\\n    \\\"model\\\": \\\"openvla-7b-finetuned-libero-object\\\",\\n    \\\"unnorm_key\\\": \\\"libero_10_no_noops\\\",\\n    \\\"seed\\\": 42,\\n    \\\"task_names\\\": [\\n      \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\",\\n      \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\",\\n      \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\",\\n      \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\",\\n      \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\",\\n      \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\",\\n      \\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\",\\n      \\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\",\\n      \\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\",\\n      \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\"\\n    ]\\n  },\\n  \\\"wrong\\\": {\\n    \\\"global_metrics\\\": {\\n      \\\"paired_mse\\\": {\\n        \\\"mean\\\": 0.030466,\\n        \\\"std\\\": 0.055863,\\n        \\\"cohens_d\\\": 0.5453\\n      },\\n      \\\"per_dim_shift\\\": {\\n        \\\"means\\\": [\\n          0.03791,\\n          0.057858,\\n          0.097442,\\n          0.009456,\\n          0.01182,\\n          0.020614,\\n          0.17278\\n        ],\\n        \\\"stds\\\": [\\n          0.062
…[truncated 7624 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_openvla_long_cf_trained_20260521T224214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-21T22:43:19.634674+00:00_

## 实验结果: `openvla_long_cf_trained`

**状态**: 成功完成 (EXIT_CODE=0, 90.0 min)

### Counterfactual Sensitivity (Cohen's d, global)

| Rank | Condition | Cohen's d | Cross-task mean d | MSE mean | Token div |
|------|-----------|-----------|-------------------|----------|-----------|
| 1 | **shuffled** | 0.5646 | 0.5664 | 0.032518 | 0.999 |
| 2 | **wrong** | 0.5453 | 0.5452 | 0.030466 | 0.999 |
| 3 | **empty** | 0.5048 | 0.5063 | 0.026031 | 1.000 |
| 4 | **paraphrased** | 0.4486 | 0.4454 | 0.022493 | 0.957 |

### Ranking 对比

- **Hypothesized**: empty > wrong > shuffled > para
- **Observed**: shuffled > wrong > empty > para

Paraphrased 最低这一点与其他 suite 一致，但 shuffled 升至第一、empty 降至第三，与 Goal/Spatial/Object suite 的 ordering 不同。Top-3 条件间差距较小（d=0.50–0.56），paraphrased 明显低于其余三者。

### 注意事项
- Paraphrased 的 token_divergence=0.957 明显低于其他条件（~1.0），符合语义保留预期
- Per-task variance: paraphrased 的 CV=0.2516 最高，部分 task d 低至 0.28（LIVING_ROOM_SCENE5/6）
- 无 untrained 对照数据（遵守 C001: 不下 trained vs untrained 对比结论）

### 文件路径
- **log_path**: `~/runs/vla-ssd/openvla_long_cf_trained.log`
- **result_path**: `/root/autodl-tmp/vla-ssd/results/libero_long/counterfactual_combined.json`
- **checkpoint**: `/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-oft-finetuned-libero-10`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_openvla_long_cf_trained_20260521T224214"
}
```

</details>

---
