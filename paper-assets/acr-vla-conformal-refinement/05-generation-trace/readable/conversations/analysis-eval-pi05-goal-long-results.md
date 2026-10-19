# analysis eval pi05 goal long results

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_analysis_eval-pi05-goal-long-results_20260522T155016.jsonl`
- **Structured JSON:** [`a13a0946681de257c6d1.json`](../../sessions/a1/a13a0946681de257c6d1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-22T15:51:07.132921+00:00_

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
  "session": "worker_analysis_eval-pi05-goal-long-results_20260522T155016",
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

_source line 2 · 2026-05-22T15:51:07.135462+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval-pi05-goal-long-results_20260522T155016",
  "tool": "ToolSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T15:51:07.135805+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -100 ~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-goal-seed43-r4.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval-pi05-goal-long-results_20260522T155016",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tail -100 ~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-goal-seed43-r4.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T15:51:07.136115+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'goal', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 10, 'max_steps': 300, 'seed': 43, 'K': 1, 'mode': 'vla_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_goal_vla_only_pi05_seed43.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855, 'n_action_steps': 10}\\n[eval] Mode: vla_only, benchmark: goal\\n[eval] max_steps set to 300 for benchmark goal\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\n✓ Loaded state dict from model.safetensors\\nAll keys loaded successfully!\\n[pi05] Fixed 437 vision tower keys\\n[pi05] Vision tower missing_keys (376): ['model.paligemma_with_expert.paligemma.lm_head.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.bias', 'model.paligemma_with_expert.paligemma.model.language_model.embed_tokens.weight', 'model.paligemma_w
…[truncated 2795 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval-pi05-goal-long-results_20260522T155016",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T15:51:07.136400+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -100 ~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-goal-seed44-r4.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval-pi05-goal-long-results_20260522T155016",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tail -100 ~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-goal-seed44-r4.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T15:51:07.136675+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'goal', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 10, 'max_steps': 300, 'seed': 44, 'K': 1, 'mode': 'vla_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_goal_vla_only_pi05_seed44.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855, 'n_action_steps': 10}\\n[eval] Mode: vla_only, benchmark: goal\\n[eval] max_steps set to 300 for benchmark goal\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\n✓ Loaded state dict from model.safetensors\\nAll keys loaded successfully!\\n[pi05] Fixed 437 vision tower keys\\n[pi05] Vision tower missing_keys (376): ['model.paligemma_with_expert.paligemma.lm_head.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.bias', 'model.paligemma_with_expert.paligemma.model.language_model.embed_tokens.weight', 'model.paligemma_w
…[truncated 2792 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval-pi05-goal-long-results_20260522T155016",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T15:51:07.136911+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "tail -100 ~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-long-seed43-r4.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval-pi05-goal-long-results_20260522T155016",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "tail -100 ~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-long-seed43-r4.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T15:51:07.137180+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[robosuite WARNING] No private macro file found! (__init__.py:7)\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n[evaluate] args: {'benchmark': 'long', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 10, 'max_steps': 520, 'seed': 43, 'K': 1, 'mode': 'vla_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_long_vla_only_pi05_seed43.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855, 'n_action_steps': 10}\\n[eval] Mode: vla_only, benchmark: long\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\n✓ Loaded state dict from model.safetensors\\nAll keys loaded successfully!\\n[pi05] Fixed 437 vision tower keys\\n[pi05] Vision tower missing_keys (376): ['model.paligemma_with_expert.paligemma.lm_head.weight', 'model.paligemma_with_
…[truncated 4433 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval-pi05-goal-long-results_20260522T155016",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T15:51:07.139530+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "tail -100 ~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-long-seed44-r4.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval-pi05-goal-long-results_20260522T155016",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "tail -100 ~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-long-seed44-r4.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T15:51:07.139872+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[robosuite WARNING] No private macro file found! (__init__.py:7)\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n[evaluate] args: {'benchmark': 'long', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 10, 'max_steps': 520, 'seed': 44, 'K': 1, 'mode': 'vla_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_long_vla_only_pi05_seed44.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855, 'n_action_steps': 10}\\n[eval] Mode: vla_only, benchmark: long\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\n✓ Loaded state dict from model.safetensors\\nAll keys loaded successfully!\\n[pi05] Fixed 437 vision tower keys\\n[pi05] Vision tower missing_keys (376): ['model.paligemma_with_expert.paligemma.lm_head.weight', 'model.paligemma_with_
…[truncated 4433 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval-pi05-goal-long-results_20260522T155016",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-22T15:51:07.140292+00:00_

全部 4 个实验已完成，结果如下：

---

### Goal Suite (bjb1-32546)

```
exp_id: eval-pi05-vla-only-goal-seed43-r4
status: completed
success_rate: 97.0% (97/100)
per_task_rates:
  open_the_middle_drawer_of_the_cabinet:        100% (10/10)
  put_the_bowl_on_the_stove:                    100% (10/10)
  put_the_wine_bottle_on_top_of_the_cabinet:    100% (10/10)
  open_the_top_drawer_and_put_the_bowl_inside:   70% (7/10)  ← 最弱
  put_the_bowl_on_top_of_the_cabinet:           100% (10/10)
  push_the_plate_to_the_front_of_the_stove:     100% (10/10)
  put_the_cream_cheese_in_the_bowl:             100% (10/10)
  turn_on_the_stove:                            100% (10/10)
  put_the_bowl_on_the_plate:                    100% (10/10)
  put_the_wine_bottle_on_the_rack:              100% (10/10)
wandb_run_id: N/A
errors: none
```

```
exp_id: eval-pi05-vla-only-goal-seed44-r4
status: completed
success_rate: 97.0% (97/100)
per_task_rates:
  open_the_middle_drawer_of_the_cabinet:         80% (8/10)
  put_the_bowl_on_the_stove:                    100% (10/10)
  put_the_wine_bottle_on_top_of_the_cabinet:    100% (10/10)
  open_the_top_drawer_and_put_the_bowl_inside:   90% (9/10)
  put_the_bowl_on_top_of_the_cabinet:           100% (10/10)
  push_the_plate_to_the_front_of_the_stove:     100% (10/10)
  put_the_cream_cheese_in_the_bowl:             100% (10/10)
  turn_on_the_stove:                            100% (10/10)
  put_the_bowl_on_the_plate:                    100% (10/10)
  put_the_wine_bottle_on_the_rack:              100% (10/10)
wandb_run_id: N/A
errors: none
```

### Long Suite (bjb1-18228)

```
exp_id: eval-pi05-vla-only-long-seed43-r4
status: completed
success_rate: 96.0% (96/100)
per_task_rates:
  LIVING_ROOM_SCENE2_alphabet_soup_and_tomato_sauce_in_basket:  100% (10/10)
  LIVING_ROOM_SCENE2_cream_cheese_and_butter_in_basket:         100% (10/10)
  KITCHEN_SCENE3_turn_on_stove_and_moka_pot:                    100% (10/10)
  KITCHEN_SCENE4_black_bowl_in_bottom_drawer:                   100% (10/10)
  LIVING_ROOM_SCENE5_white_mug_left_plate_yellow_mug_right:      90% (9/10)
  STUDY_SCENE1_book_in_back_compartment:                        100% (10/10)
  LIVING_ROOM_SCENE6_white_mug_on_plate_chocolate_pudding:      100% (10/10)
  LIVING_ROOM_SCENE1_alphabet_soup_and_cream_cheese_in_basket:  100% (10/10)
  KITCHEN_SCENE8_both_moka_pots_on_stove:                        70% (7/10)  ← 最弱
  KITCHEN_SCENE6_yellow_mug_in_microwave:                       100% (10/10)
wandb_run_id: N/A
errors: none
```

```
exp_id: eval-pi05-vla-only-long-seed44-r4
status: completed
success_rate: 95.0% (95/100)
per_task_rates:
  LIVING_ROOM_SCENE2_alphabet_soup_and_tomato_sauce_in_basket:  100% (10/10)
  LIVING_ROOM_SCENE2_cream_cheese_and_butter_in_basket:         100% (10/10)
  KITCHEN_SCENE3_turn_on_stove_and_moka_pot:                    100% (10/10)
  KITCHEN_SCENE4_black_bowl_in_bottom_drawer:                   100% (10/10)
  LIVING_ROOM_SCENE5_white_mug_left_plate_yellow_mug_right:     100% (10/10)
  STUDY_SCENE1_book_in_back_compartment:                        100% (10/10)
  LIVING_ROOM_SCENE6_white_mug_on_plate_chocolate_pudding:      100% (10/10)
  LIVING_ROOM_SCENE1_alphabet_soup_and_cream_cheese_in_basket:   90% (9/10)
  KITCHEN_SCENE8_both_moka_pots_on_stove:                        60% (6/10)  ← 最弱
  KITCHEN_SCENE6_yellow_mug_in_microwave:                       100% (10/10)
wandb_run_id: N/A
errors: none
```

---

### 汇总（含已有 seed42）

| Benchmark | seed42 | seed43 | seed44 | Mean ± Std |
|-----------|--------|--------|--------|------------|
| **Goal**  | 98.0%  | 97.0%  | 97.0%  | **97.3% ± 0.6%** |
| **Long**  | 94.0%  | 96.0%  | 95.0%  | **95.0% ± 1.0%** |

难点 task 一致：Goal 的 `open_the_top_drawer_and_put_the_bowl_inside`（70-90%），Long 的 `KITCHEN_SCENE8_both_moka_pots_on_stove`（60-70%）。日志均无 W&B run ID。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_eval-pi05-goal-long-results_20260522T155016"
}
```

</details>

---
