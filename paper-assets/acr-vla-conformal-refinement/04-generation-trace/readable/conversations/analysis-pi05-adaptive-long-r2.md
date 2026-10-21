# analysis pi05 adaptive long r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 68
- **Recorded user turns:** 0
- **Tool calls:** 33
- **Original source:** `logs/chats/worker_analysis_pi05-adaptive-long-r2_20260526T101850.jsonl`
- **Structured JSON:** [`bb84f89aea500b3699e9.json`](../../sessions/bb/bb84f89aea500b3699e9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

68 recorded events

### Assistant

_source line 1 · 2026-05-26T10:19:01.628553+00:00_

Not logged in · Please run /login

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-26T10:21:52.611427+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-26T10:21:52.611882+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "ToolSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-26T10:21:52.612145+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'pi05-adaptive-long-s43-cqa1-r2'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'pi05-adaptive-long-s43-cqa1-r2'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-26T10:21:52.612426+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6262}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-26T10:21:52.612643+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'pi05-adaptive-long-s44-cqa1-r2'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'pi05-adaptive-long-s44-cqa1-r2'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-26T10:21:52.612852+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6239}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-26T10:21:52.613053+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "account": "root",
  "command": "tail -100 /root/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s43-cqa1-r2.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "account": "root",
    "command": "tail -100 /root/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s43-cqa1-r2.log"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-26T10:21:52.613255+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "account": "root",
  "command": "tail -100 /root/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s44-cqa1-r2.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "account": "root",
    "command": "tail -100 /root/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s44-cqa1-r2.log"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-26T10:21:52.615719+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    obs_feat, samples = wrapper.get_obs_features_and_samples(\\n                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/torch/utils/_contextlib.py\\\", line 120, in decorate_context\\n    return func(*args, **kwargs)\\n           ^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/acr-vla-conformal-refinement/src/pi05_wrapper.py\\\", line 330, in get_obs_features_and_samples\\n    imgs, img_masks, lt, lm = self.preprocess_obs(\\n                              ^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/torch/utils/_contextlib.py\\\", line 120, in decorate_context\\n    return func(*args, **kwargs)\\n           ^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/acr-vla-conformal-refinement/src/pi05_wrapper.py\\\", line 204, in preprocess_obs\\n    imgs = [self._preprocess_image(agentview_rgb)]\\n            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/acr-vla-conformal-refinement/src/pi05_wrapper.py\\\", line 163, in _preprocess_image\\n    img = torch.flip(img, dims=[2, 3])\\n          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\ntorch.AcceleratorError: CUDA error: out of memory\\nCUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.\\nFor debugging consider passing CUDA_LAUNCH_BLOCKING=1\\nCompile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.\\n\\n[rollout] Exception at step 0: CUDA error: out of memory\\nCUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.\\nFor debugging consider passing CUDA_LAUNCH_BLOCKING=1\\nCompile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.\\n\\nTraceback (most recent call last):\\n  File \\\"/root/acr-vla-conformal-refinement/src/evaluate.py\\\", line 518, in rollout_single\\n    action_7d = action_fn(obs)\\n                ^^^^^^^^^^^^^^\\n  File \
…[truncated 4587 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-26T10:21:52.616123+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    obs_feat, samples = wrapper.get_obs_features_and_samples(\\n                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/torch/utils/_contextlib.py\\\", line 120, in decorate_context\\n    return func(*args, **kwargs)\\n           ^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/acr-vla-conformal-refinement/src/pi05_wrapper.py\\\", line 330, in get_obs_features_and_samples\\n    imgs, img_masks, lt, lm = self.preprocess_obs(\\n                              ^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/torch/utils/_contextlib.py\\\", line 120, in decorate_context\\n    return func(*args, **kwargs)\\n           ^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/acr-vla-conformal-refinement/src/pi05_wrapper.py\\\", line 204, in preprocess_obs\\n    imgs = [self._preprocess_image(agentview_rgb)]\\n            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/acr-vla-conformal-refinement/src/pi05_wrapper.py\\\", line 163, in _preprocess_image\\n    img = torch.flip(img, dims=[2, 3])\\n          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\ntorch.AcceleratorError: CUDA error: out of memory\\nCUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.\\nFor debugging consider passing CUDA_LAUNCH_BLOCKING=1\\nCompile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.\\n\\n[rollout] Exception at step 0: CUDA error: out of memory\\nCUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.\\nFor debugging consider passing CUDA_LAUNCH_BLOCKING=1\\nCompile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.\\n\\nTraceback (most recent call last):\\n  File \\\"/root/acr-vla-conformal-refinement/src/evaluate.py\\\", line 518, in rollout_single\\n    action_7d = action_fn(obs)\\n                ^^^^^^^^^^^^^^\\n  File \
…[truncated 4587 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-26T10:21:52.616461+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "account": "root",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_long_adaptive_pi05_seed43.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "account": "root",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_long_adaptive_pi05_seed43.json"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-26T10:21:52.616762+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"long\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.0,\\n  \\\"per_task\\\": {\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": {\\n      \\\"success_rate\\\": 0.0,\\n    
…[truncated 362 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-26T10:21:52.617018+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "account": "root",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_long_adaptive_pi05_seed44.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "account": "root",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_long_adaptive_pi05_seed44.json"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-26T10:21:52.618819+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"long\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.0,\\n  \\\"per_task\\\": {\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": {\\n      \\\"success_rate\\\": 0.0,\\n    
…[truncated 362 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-26T10:21:52.619133+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "account": "root",
  "command": "grep -E \"wandb|W&B|run_id|crm_checkpoint|trigger_rate|Overall|Trigger\" /root/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s43-cqa1-r2.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "account": "root",
    "command": "grep -E \"wandb|W&B|run_id|crm_checkpoint|trigger_rate|Overall|Trigger\" /root/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s43-cqa1-r2.log"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-26T10:21:52.619378+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-26T10:21:52.619595+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "account": "root",
  "command": "grep -E \"wandb|W&B|run_id|crm_checkpoint|trigger_rate|Overall|Trigger\" /root/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s44-cqa1-r2.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "account": "root",
    "command": "grep -E \"wandb|W&B|run_id|crm_checkpoint|trigger_rate|Overall|Trigger\" /root/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s44-cqa1-r2.log"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-26T10:21:52.619816+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-26T10:21:52.620017+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "account": "root",
  "command": "grep -E \"wandb|crm_checkpoint|trigger|Overall|seed\" /root/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s43-cqa1-r2.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "account": "root",
    "command": "grep -E \"wandb|crm_checkpoint|trigger|Overall|seed\" /root/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s43-cqa1-r2.log"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-26T10:21:52.620218+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-26T10:21:52.621701+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "account": "root",
  "command": "head -80 /root/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s43-cqa1-r2.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "account": "root",
    "command": "head -80 /root/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s43-cqa1-r2.log"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-26T10:21:52.622049+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[robosuite WARNING] No private macro file found! (__init__.py:7)\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n[evaluate] args: {'benchmark': 'long', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt', 'n_rollouts': 20, 'max_steps': 300, 'seed': 43, 'K': 2, 'mode': 'adaptive_conformal_crm', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'openvla_oft_path': '/root/autodl-tmp/models/openvla-oft/object/', 'obs_dim': 2048, 'unified_obs_dim': 2088, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_long_adaptive_pi05_seed43.json', 'max_correction_norm': 0.2, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.25, 'n_action_steps': 10}\\n[eval] Mode: adaptive_conformal_crm, benchmark: long\\n[eval] max_steps set to 520 for benchmark long\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\n✓ Loaded state dict from model.safetensors\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embed
…[truncated 4722 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-26T10:21:52.622379+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-adaptive-long-s43-cqa1-r2",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python src/evaluate.py --benchmark long --mode adaptive_conformal_crm --model pi05 --seed 43 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ --output_file logs/eval_long_adaptive_pi05_seed43.json', 'server': 'cqa1-32758', 'data_path': 'LIBERO-Long (10 tasks)', 'data_count': 200, 'model_name': 'pi05', 'seed': 43, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt', 'eval_data': 'LIBERO-Long 10 tasks x 20 rollouts'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-adaptive-long-s43-cqa1-r2",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python src/evaluate.py --benchmark long --mode adaptive_conformal_crm --model pi05 --seed 43 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ --output_file logs/eval_long_adaptive_pi05_seed43.json', 'server': 'cqa1-32758', 'data_path': 'LIBERO-Long (10 tasks)', 'data_count': 200, 'model_name': 'pi05', 'seed': 43, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt', 'eval_data': 'LIBERO-Long 10 tasks x 20 rollouts'}"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-26T10:21:52.624395+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.816}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-26T10:21:52.624660+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-adaptive-long-s44-cqa1-r2",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python src/evaluate.py --benchmark long --mode adaptive_conformal_crm --model pi05 --seed 44 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ --output_file logs/eval_long_adaptive_pi05_seed44.json', 'server': 'cqa1-32758', 'data_path': 'LIBERO-Long (10 tasks)', 'data_count': 200, 'model_name': 'pi05', 'seed': 44, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt', 'eval_data': 'LIBERO-Long 10 tasks x 20 rollouts'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-adaptive-long-s44-cqa1-r2",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python src/evaluate.py --benchmark long --mode adaptive_conformal_crm --model pi05 --seed 44 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ --output_file logs/eval_long_adaptive_pi05_seed44.json', 'server': 'cqa1-32758', 'data_path': 'LIBERO-Long (10 tasks)', 'data_count': 200, 'model_name': 'pi05', 'seed': 44, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt', 'eval_data': 'LIBERO-Long 10 tasks x 20 rollouts'}"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-26T10:21:52.624897+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.4377}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-26T10:21:52.625102+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-adaptive-long-s43-cqa1-r2",
  "field": "status",
  "value": "PENDING"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-adaptive-long-s43-cqa1-r2",
    "field": "status",
    "value": "PENDING"
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-26T10:21:52.628361+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-adaptive-long-s44-cqa1-r2",
  "field": "status",
  "value": "PENDING"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-adaptive-long-s44-cqa1-r2",
    "field": "status",
    "value": "PENDING"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-26T10:21:52.628660+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-adaptive-long-s43-cqa1-r2\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T10:20:13.490Z\", \"updated_at\": \"2026-05-26T10:20:13.490Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.309}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-26T10:21:52.628876+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-adaptive-long-s44-cqa1-r2\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T10:20:14.793Z\", \"updated_at\": \"2026-05-26T10:20:14.793Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2505}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-26T10:21:52.629085+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-adaptive-long-s43-cqa1-r2",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python src/evaluate.py --benchmark long --mode adaptive_conformal_crm --model pi05 --seed 43 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ --output_file logs/eval_long_adaptive_pi05_seed43.json', 'server': 'cqa1-32758', 'data_path': 'LIBERO-Long (10 tasks)', 'data_count': 200, 'model_name': 'pi05', 'seed': 43, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt', 'eval_data': 'LIBERO-Long 10 tasks x 20 rollouts'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-adaptive-long-s43-cqa1-r2",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python src/evaluate.py --benchmark long --mode adaptive_conformal_crm --model pi05 --seed 43 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ --output_file logs/eval_long_adaptive_pi05_seed43.json', 'server': 'cqa1-32758', 'data_path': 'LIBERO-Long (10 tasks)', 'data_count': 200, 'model_name': 'pi05', 'seed': 43, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt', 'eval_data': 'LIBERO-Long 10 tasks x 20 rollouts'}"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-26T10:21:52.629351+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.771}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-26T10:21:52.629574+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-adaptive-long-s44-cqa1-r2",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python src/evaluate.py --benchmark long --mode adaptive_conformal_crm --model pi05 --seed 44 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ --output_file logs/eval_long_adaptive_pi05_seed44.json', 'server': 'cqa1-32758', 'data_path': 'LIBERO-Long (10 tasks)', 'data_count': 200, 'model_name': 'pi05', 'seed': 44, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt', 'eval_data': 'LIBERO-Long 10 tasks x 20 rollouts'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-adaptive-long-s44-cqa1-r2",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python src/evaluate.py --benchmark long --mode adaptive_conformal_crm --model pi05 --seed 44 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ --output_file logs/eval_long_adaptive_pi05_seed44.json', 'server': 'cqa1-32758', 'data_path': 'LIBERO-Long (10 tasks)', 'data_count': 200, 'model_name': 'pi05', 'seed': 44, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt', 'eval_data': 'LIBERO-Long 10 tasks x 20 rollouts'}"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-26T10:21:52.629802+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.8139}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-26T10:21:52.630005+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-adaptive-long-s43-cqa1-r2",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-adaptive-long-s43-cqa1-r2",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-26T10:21:52.630203+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-adaptive-long-s44-cqa1-r2",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-adaptive-long-s44-cqa1-r2",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-26T10:21:52.634568+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-adaptive-long-s43-cqa1-r2\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-26T10:20:13.490Z\", \"updated_at\": \"2026-05-26T10:20:38.806Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.247}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-26T10:21:52.634808+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-adaptive-long-s44-cqa1-r2\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-26T10:20:14.793Z\", \"updated_at\": \"2026-05-26T10:20:40.057Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2586}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-26T10:21:52.635018+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-adaptive-long-s43-cqa1-r2",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python src/evaluate.py --benchmark long --mode adaptive_conformal_crm --model pi05 --seed 43 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ --output_file logs/eval_long_adaptive_pi05_seed43.json', 'server': 'cqa1-32758', 'data_path': 'LIBERO-Long (10 tasks)', 'data_count': 200, 'model_name': 'pi05', 'seed': 43, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt', 'eval_data': 'LIBERO-Long 10 tasks x 20 rollouts'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-adaptive-long-s43-cqa1-r2",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python src/evaluate.py --benchmark long --mode adaptive_conformal_crm --model pi05 --seed 43 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ --output_file logs/eval_long_adaptive_pi05_seed43.json', 'server': 'cqa1-32758', 'data_path': 'LIBERO-Long (10 tasks)', 'data_count': 200, 'model_name': 'pi05', 'seed': 43, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt', 'eval_data': 'LIBERO-Long 10 tasks x 20 rollouts'}"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-26T10:21:52.635303+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-adaptive-long-s43-cqa1-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T10:20:13.490Z\", \"updated_at\": \"2026-05-26T10:20:48.882Z\", \"spec\": {\"command\": \"python src/evaluate.py --benchmark long --mode adaptive_conformal_crm --model pi05 --seed 43 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ --output_file logs/eval_long_adaptive_pi05_seed43.json\", \"server\": \"cqa1-32758\", \"data_path\": \"LIBERO-Long (10 tasks)\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Long 10 tasks x 20 rollouts\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.9549}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-26T10:21:52.636772+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-adaptive-long-s44-cqa1-r2",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python src/evaluate.py --benchmark long --mode adaptive_conformal_crm --model pi05 --seed 44 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ --output_file logs/eval_long_adaptive_pi05_seed44.json', 'server': 'cqa1-32758', 'data_path': 'LIBERO-Long (10 tasks)', 'data_count': 200, 'model_name': 'pi05', 'seed': 44, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt', 'eval_data': 'LIBERO-Long 10 tasks x 20 rollouts'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-adaptive-long-s44-cqa1-r2",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python src/evaluate.py --benchmark long --mode adaptive_conformal_crm --model pi05 --seed 44 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ --output_file logs/eval_long_adaptive_pi05_seed44.json', 'server': 'cqa1-32758', 'data_path': 'LIBERO-Long (10 tasks)', 'data_count': 200, 'model_name': 'pi05', 'seed': 44, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt', 'eval_data': 'LIBERO-Long 10 tasks x 20 rollouts'}"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-26T10:21:52.637027+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-adaptive-long-s44-cqa1-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T10:20:14.793Z\", \"updated_at\": \"2026-05-26T10:20:51.954Z\", \"spec\": {\"command\": \"python src/evaluate.py --benchmark long --mode adaptive_conformal_crm --model pi05 --seed 44 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ --output_file logs/eval_long_adaptive_pi05_seed44.json\", \"server\": \"cqa1-32758\", \"data_path\": \"LIBERO-Long (10 tasks)\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Long 10 tasks x 20 rollouts\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.8161}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-26T10:21:52.638930+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-adaptive-long-s43-cqa1-r2",
  "field": "hypothesis",
  "value": "π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIBERO-Long should match or exceed the π0.5 VLA-only baseline (~57.2%) by gating CRM refinement only when conformal uncertainty exceeds threshold, avoiding harmful corrections on easy steps."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-adaptive-long-s43-cqa1-r2",
    "field": "hypothesis",
    "value": "π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIBERO-Long should match or exceed the π0.5 VLA-only baseline (~57.2%) by gating CRM refinement only when conformal uncertainty exceeds threshold, avoiding harmful corrections on easy steps."
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-26T10:21:52.639503+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-adaptive-long-s44-cqa1-r2",
  "field": "hypothesis",
  "value": "π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIBERO-Long should match or exceed the π0.5 VLA-only baseline (~57.2%) by gating CRM refinement only when conformal uncertainty exceeds threshold, avoiding harmful corrections on easy steps."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-adaptive-long-s44-cqa1-r2",
    "field": "hypothesis",
    "value": "π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIBERO-Long should match or exceed the π0.5 VLA-only baseline (~57.2%) by gating CRM refinement only when conformal uncertainty exceeds threshold, avoiding harmful corrections on easy steps."
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-26T10:21:52.639772+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-adaptive-long-s43-cqa1-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T10:20:13.490Z\", \"updated_at\": \"2026-05-26T10:21:00.137Z\", \"spec\": {\"command\": \"python src/evaluate.py --benchmark long --mode adaptive_conformal_crm --model pi05 --seed 43 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ --output_file logs/eval_long_adaptive_pi05_seed43.json\", \"server\": \"cqa1-32758\", \"data_path\": \"LIBERO-Long (10 tasks)\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Long 10 tasks x 20 rollouts\"}, \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIBERO-Long should match or exceed the π0.5 VLA-only baseline (~57.2%) by gating CRM refinement only when conformal uncertainty exceeds threshold, avoiding harmful corrections on easy steps.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.1513}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-26T10:21:52.640036+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-adaptive-long-s44-cqa1-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T10:20:14.793Z\", \"updated_at\": \"2026-05-26T10:21:02.516Z\", \"spec\": {\"command\": \"python src/evaluate.py --benchmark long --mode adaptive_conformal_crm --model pi05 --seed 44 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ --output_file logs/eval_long_adaptive_pi05_seed44.json\", \"server\": \"cqa1-32758\", \"data_path\": \"LIBERO-Long (10 tasks)\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Long 10 tasks x 20 rollouts\"}, \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIBERO-Long should match or exceed the π0.5 VLA-only baseline (~57.2%) by gating CRM refinement only when conformal uncertainty exceeds threshold, avoiding harmful corrections on easy steps.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.3022}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-26T10:21:52.640317+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-adaptive-long-s43-cqa1-r2",
  "field": "metrics",
  "value": "{'overall_success_rate': 0, 'successes': 0, 'total_rollouts': 200, 'n_tasks': 10, 'n_rollouts_per_task': 20, 'per_task_success_rate': {'LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket': 0, 'LIVING_ROOM_SCENE2_cream_cheese_butter_basket': 0, 'KITCHEN_SCENE3_stove_moka_pot': 0, 'KITCHEN_SCENE4_black_bowl_drawer': 0, 'LIVING_ROOM_SCENE5_white_mug_yellow_mug_plates': 0, 'STUDY_SCENE1_book_caddy_back': 0, 'LIVING_ROOM_SCENE6_white_mug_chocolate_pudding': 0, 'LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket': 0, 'KITCHEN_SCENE8_both_moka_pots_stove': 0, 'KITCHEN_SCENE6_yellow_white_mug_microwave': 0}, 'trigger_rate': None, 'failure_mode': 'CUDA_OOM_step_0_every_rollout', 'error_summary': 'Every rollout raised torch.AcceleratorError: CUDA error: out of memory at step 0 in pi05_wrapper.preprocess_obs (line 163, torch.flip). Script completed but produced no valid evaluation signal.', 'vla_only_baseline_long': 0.572, 'delta_vs_baseline': -0.572}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-adaptive-long-s43-cqa1-r2",
    "field": "metrics",
    "value": "{'overall_success_rate': 0, 'successes': 0, 'total_rollouts': 200, 'n_tasks': 10, 'n_rollouts_per_task': 20, 'per_task_success_rate': {'LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket': 0, 'LIVING_ROOM_SCENE2_cream_cheese_butter_basket': 0, 'KITCHEN_SCENE3_stove_moka_pot': 0, 'KITCHEN_SCENE4_black_bowl_drawer': 0, 'LIVING_ROOM_SCENE5_white_mug_yellow_mug_plates': 0, 'STUDY_SCENE1_book_caddy_back': 0, 'LIVING_ROOM_SCENE6_white_mug_chocolate_pudding': 0, 'LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket': 0, 'KITCHEN_SCENE8_both_moka_pots_stove': 0, 'KITCHEN_SCENE6_yellow_white_mug_microwave': 0}, 'trigger_rate': None, 'failure_mode': 'CUDA_OOM_step_0_every_rollout', 'error_summary': 'Every rollout raised torch.AcceleratorError: CUDA error: out of memory at step 0 in pi05_wrapper.preprocess_obs (line 163, torch.flip). Script completed but produced no valid evaluation signal.', 'vla_only_baseline_long': 0.572, 'delta_vs_baseline': -0.572}"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-26T10:21:52.643610+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-adaptive-long-s43-cqa1-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T10:20:13.490Z\", \"updated_at\": \"2026-05-26T10:21:08.418Z\", \"spec\": {\"command\": \"python src/evaluate.py --benchmark long --mode adaptive_conformal_crm --model pi05 --seed 43 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ --output_file logs/eval_long_adaptive_pi05_seed43.json\", \"server\": \"cqa1-32758\", \"data_path\": \"LIBERO-Long (10 tasks)\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Long 10 tasks x 20 rollouts\"}, \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIBERO-Long should match or exceed the π0.5 VLA-only baseline (~57.2%) by gating CRM refinement only when conformal uncertainty exceeds threshold, avoiding harmful corrections on easy steps.\", \"metrics\": {\"overall_success_rate\": 0, \"successes\": 0, \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"per_task_success_rate\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_yellow_mug_plates\": 0, \"STUDY_SCENE1_book_caddy_back\": 0, \"LIVING_ROOM_SCENE6_white_mug_chocolate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0}, \"trigger_rate\": null, \"failure_mode\": \"CUDA_OOM_step_0_every_rollout\", \"error_summary\": \"Every rollout raised torch.AcceleratorError: CUDA error: out of
…[truncated 266 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-26T10:21:52.643901+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-adaptive-long-s44-cqa1-r2",
  "field": "metrics",
  "value": "{'overall_success_rate': 0, 'successes': 0, 'total_rollouts': 200, 'n_tasks': 10, 'n_rollouts_per_task': 20, 'per_task_success_rate': {'LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket': 0, 'LIVING_ROOM_SCENE2_cream_cheese_butter_basket': 0, 'KITCHEN_SCENE3_stove_moka_pot': 0, 'KITCHEN_SCENE4_black_bowl_drawer': 0, 'LIVING_ROOM_SCENE5_white_mug_yellow_mug_plates': 0, 'STUDY_SCENE1_book_caddy_back': 0, 'LIVING_ROOM_SCENE6_white_mug_chocolate_pudding': 0, 'LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket': 0, 'KITCHEN_SCENE8_both_moka_pots_stove': 0, 'KITCHEN_SCENE6_yellow_white_mug_microwave': 0}, 'trigger_rate': None, 'failure_mode': 'CUDA_OOM_step_0_every_rollout', 'error_summary': 'Every rollout raised torch.AcceleratorError: CUDA error: out of memory at step 0 in pi05_wrapper.preprocess_obs (line 163, torch.flip). Script completed but produced no valid evaluation signal.', 'vla_only_baseline_long': 0.572, 'delta_vs_baseline': -0.572}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-adaptive-long-s44-cqa1-r2",
    "field": "metrics",
    "value": "{'overall_success_rate': 0, 'successes': 0, 'total_rollouts': 200, 'n_tasks': 10, 'n_rollouts_per_task': 20, 'per_task_success_rate': {'LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket': 0, 'LIVING_ROOM_SCENE2_cream_cheese_butter_basket': 0, 'KITCHEN_SCENE3_stove_moka_pot': 0, 'KITCHEN_SCENE4_black_bowl_drawer': 0, 'LIVING_ROOM_SCENE5_white_mug_yellow_mug_plates': 0, 'STUDY_SCENE1_book_caddy_back': 0, 'LIVING_ROOM_SCENE6_white_mug_chocolate_pudding': 0, 'LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket': 0, 'KITCHEN_SCENE8_both_moka_pots_stove': 0, 'KITCHEN_SCENE6_yellow_white_mug_microwave': 0}, 'trigger_rate': None, 'failure_mode': 'CUDA_OOM_step_0_every_rollout', 'error_summary': 'Every rollout raised torch.AcceleratorError: CUDA error: out of memory at step 0 in pi05_wrapper.preprocess_obs (line 163, torch.flip). Script completed but produced no valid evaluation signal.', 'vla_only_baseline_long': 0.572, 'delta_vs_baseline': -0.572}"
  }
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-26T10:21:52.644148+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-adaptive-long-s43-cqa1-r2",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-adaptive-long-s43-cqa1-r2",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-26T10:21:52.648571+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-adaptive-long-s44-cqa1-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T10:20:14.793Z\", \"updated_at\": \"2026-05-26T10:21:14.329Z\", \"spec\": {\"command\": \"python src/evaluate.py --benchmark long --mode adaptive_conformal_crm --model pi05 --seed 44 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ --output_file logs/eval_long_adaptive_pi05_seed44.json\", \"server\": \"cqa1-32758\", \"data_path\": \"LIBERO-Long (10 tasks)\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Long 10 tasks x 20 rollouts\"}, \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIBERO-Long should match or exceed the π0.5 VLA-only baseline (~57.2%) by gating CRM refinement only when conformal uncertainty exceeds threshold, avoiding harmful corrections on easy steps.\", \"metrics\": {\"overall_success_rate\": 0, \"successes\": 0, \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"per_task_success_rate\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_yellow_mug_plates\": 0, \"STUDY_SCENE1_book_caddy_back\": 0, \"LIVING_ROOM_SCENE6_white_mug_chocolate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0}, \"trigger_rate\": null, \"failure_mode\": \"CUDA_OOM_step_0_every_rollout\", \"error_summary\": \"Every rollout raised torch.AcceleratorError: CUDA error: out of
…[truncated 266 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-26T10:21:52.648943+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-adaptive-long-s43-cqa1-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T10:20:13.490Z\", \"updated_at\": \"2026-05-26T10:21:15.146Z\", \"spec\": {\"command\": \"python src/evaluate.py --benchmark long --mode adaptive_conformal_crm --model pi05 --seed 43 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ --output_file logs/eval_long_adaptive_pi05_seed43.json\", \"server\": \"cqa1-32758\", \"data_path\": \"LIBERO-Long (10 tasks)\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Long 10 tasks x 20 rollouts\"}, \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIBERO-Long should match or exceed the π0.5 VLA-only baseline (~57.2%) by gating CRM refinement only when conformal uncertainty exceeds threshold, avoiding harmful corrections on easy steps.\", \"metrics\": {\"overall_success_rate\": 0, \"successes\": 0, \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"per_task_success_rate\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_yellow_mug_plates\": 0, \"STUDY_SCENE1_book_caddy_back\": 0, \"LIVING_ROOM_SCENE6_white_mug_chocolate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0}, \"trigger_rate\": null, \"failure_mode\": \"CUDA_OOM_step_0_every_rollout\", \"error_summary\": \"Every rollout raised torch.AcceleratorError: CUDA error: out of
…[truncated 357 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-26T10:21:52.649200+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-adaptive-long-s44-cqa1-r2",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-adaptive-long-s44-cqa1-r2",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-26T10:21:52.649510+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-adaptive-long-s44-cqa1-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T10:20:14.793Z\", \"updated_at\": \"2026-05-26T10:21:16.321Z\", \"spec\": {\"command\": \"python src/evaluate.py --benchmark long --mode adaptive_conformal_crm --model pi05 --seed 44 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ --output_file logs/eval_long_adaptive_pi05_seed44.json\", \"server\": \"cqa1-32758\", \"data_path\": \"LIBERO-Long (10 tasks)\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Long 10 tasks x 20 rollouts\"}, \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIBERO-Long should match or exceed the π0.5 VLA-only baseline (~57.2%) by gating CRM refinement only when conformal uncertainty exceeds threshold, avoiding harmful corrections on easy steps.\", \"metrics\": {\"overall_success_rate\": 0, \"successes\": 0, \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"per_task_success_rate\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_yellow_mug_plates\": 0, \"STUDY_SCENE1_book_caddy_back\": 0, \"LIVING_ROOM_SCENE6_white_mug_chocolate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0}, \"trigger_rate\": null, \"failure_mode\": \"CUDA_OOM_step_0_every_rollout\", \"error_summary\": \"Every rollout raised torch.AcceleratorError: CUDA error: out of
…[truncated 357 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-26T10:21:52.649763+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-adaptive-long-s43-cqa1-r2",
  "field": "log_path",
  "value": "/root/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s43-cqa1-r2.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-adaptive-long-s43-cqa1-r2",
    "field": "log_path",
    "value": "/root/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s43-cqa1-r2.log"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-26T10:21:52.650041+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-adaptive-long-s43-cqa1-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T10:20:13.490Z\", \"updated_at\": \"2026-05-26T10:21:17.804Z\", \"spec\": {\"command\": \"python src/evaluate.py --benchmark long --mode adaptive_conformal_crm --model pi05 --seed 43 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ --output_file logs/eval_long_adaptive_pi05_seed43.json\", \"server\": \"cqa1-32758\", \"data_path\": \"LIBERO-Long (10 tasks)\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Long 10 tasks x 20 rollouts\"}, \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIBERO-Long should match or exceed the π0.5 VLA-only baseline (~57.2%) by gating CRM refinement only when conformal uncertainty exceeds threshold, avoiding harmful corrections on easy steps.\", \"metrics\": {\"overall_success_rate\": 0, \"successes\": 0, \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"per_task_success_rate\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_yellow_mug_plates\": 0, \"STUDY_SCENE1_book_caddy_back\": 0, \"LIVING_ROOM_SCENE6_white_mug_chocolate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0}, \"trigger_rate\": null, \"failure_mode\": \"CUDA_OOM_step_0_every_rollout\", \"error_summary\": \"Every rollout raised torch.AcceleratorError: CUDA error: out of
…[truncated 451 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-26T10:21:52.653327+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-adaptive-long-s44-cqa1-r2",
  "field": "log_path",
  "value": "/root/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s44-cqa1-r2.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-adaptive-long-s44-cqa1-r2",
    "field": "log_path",
    "value": "/root/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s44-cqa1-r2.log"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-26T10:21:52.653692+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-adaptive-long-s44-cqa1-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T10:20:14.793Z\", \"updated_at\": \"2026-05-26T10:21:18.764Z\", \"spec\": {\"command\": \"python src/evaluate.py --benchmark long --mode adaptive_conformal_crm --model pi05 --seed 44 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ --output_file logs/eval_long_adaptive_pi05_seed44.json\", \"server\": \"cqa1-32758\", \"data_path\": \"LIBERO-Long (10 tasks)\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Long 10 tasks x 20 rollouts\"}, \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIBERO-Long should match or exceed the π0.5 VLA-only baseline (~57.2%) by gating CRM refinement only when conformal uncertainty exceeds threshold, avoiding harmful corrections on easy steps.\", \"metrics\": {\"overall_success_rate\": 0, \"successes\": 0, \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"per_task_success_rate\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_yellow_mug_plates\": 0, \"STUDY_SCENE1_book_caddy_back\": 0, \"LIVING_ROOM_SCENE6_white_mug_chocolate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0}, \"trigger_rate\": null, \"failure_mode\": \"CUDA_OOM_step_0_every_rollout\", \"error_summary\": \"Every rollout raised torch.AcceleratorError: CUDA error: out of
…[truncated 451 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-26T10:21:52.653970+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-adaptive-long-s43-cqa1-r2",
  "field": "conclusion",
  "value": "negative"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-adaptive-long-s43-cqa1-r2",
    "field": "conclusion",
    "value": "negative"
  }
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-26T10:21:52.654177+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-adaptive-long-s44-cqa1-r2",
  "field": "conclusion",
  "value": "negative"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-adaptive-long-s44-cqa1-r2",
    "field": "conclusion",
    "value": "negative"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-26T10:21:52.654480+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-adaptive-long-s43-cqa1-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T10:20:13.490Z\", \"updated_at\": \"2026-05-26T10:21:24.737Z\", \"spec\": {\"command\": \"python src/evaluate.py --benchmark long --mode adaptive_conformal_crm --model pi05 --seed 43 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ --output_file logs/eval_long_adaptive_pi05_seed43.json\", \"server\": \"cqa1-32758\", \"data_path\": \"LIBERO-Long (10 tasks)\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Long 10 tasks x 20 rollouts\"}, \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIBERO-Long should match or exceed the π0.5 VLA-only baseline (~57.2%) by gating CRM refinement only when conformal uncertainty exceeds threshold, avoiding harmful corrections on easy steps.\", \"metrics\": {\"overall_success_rate\": 0, \"successes\": 0, \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"per_task_success_rate\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_yellow_mug_plates\": 0, \"STUDY_SCENE1_book_caddy_back\": 0, \"LIVING_ROOM_SCENE6_white_mug_chocolate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0}, \"trigger_rate\": null, \"failure_mode\": \"CUDA_OOM_step_0_every_rollout\", \"error_summary\": \"Every rollout raised torch.AcceleratorError: CUDA error: out of
…[truncated 481 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-26T10:21:52.654803+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-adaptive-long-s44-cqa1-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T10:20:14.793Z\", \"updated_at\": \"2026-05-26T10:21:25.897Z\", \"spec\": {\"command\": \"python src/evaluate.py --benchmark long --mode adaptive_conformal_crm --model pi05 --seed 44 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ --output_file logs/eval_long_adaptive_pi05_seed44.json\", \"server\": \"cqa1-32758\", \"data_path\": \"LIBERO-Long (10 tasks)\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Long 10 tasks x 20 rollouts\"}, \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIBERO-Long should match or exceed the π0.5 VLA-only baseline (~57.2%) by gating CRM refinement only when conformal uncertainty exceeds threshold, avoiding harmful corrections on easy steps.\", \"metrics\": {\"overall_success_rate\": 0, \"successes\": 0, \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"per_task_success_rate\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_yellow_mug_plates\": 0, \"STUDY_SCENE1_book_caddy_back\": 0, \"LIVING_ROOM_SCENE6_white_mug_chocolate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0}, \"trigger_rate\": null, \"failure_mode\": \"CUDA_OOM_step_0_every_rollout\", \"error_summary\": \"Every rollout raised torch.AcceleratorError: CUDA error: out of
…[truncated 481 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-26T10:21:52.655040+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-adaptive-long-s43-cqa1-r2",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-adaptive-long-s43-cqa1-r2",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-26T10:21:52.655246+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-adaptive-long-s44-cqa1-r2",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-adaptive-long-s44-cqa1-r2",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-26T10:21:52.659768+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-adaptive-long-s43-cqa1-r2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T10:20:13.490Z\", \"updated_at\": \"2026-05-26T10:21:32.258Z\", \"spec\": {\"command\": \"python src/evaluate.py --benchmark long --mode adaptive_conformal_crm --model pi05 --seed 43 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ --output_file logs/eval_long_adaptive_pi05_seed43.json\", \"server\": \"cqa1-32758\", \"data_path\": \"LIBERO-Long (10 tasks)\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Long 10 tasks x 20 rollouts\"}, \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIBERO-Long should match or exceed the π0.5 VLA-only baseline (~57.2%) by gating CRM refinement only when conformal uncertainty exceeds threshold, avoiding harmful corrections on easy steps.\", \"metrics\": {\"overall_success_rate\": 0, \"successes\": 0, \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"per_task_success_rate\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_yellow_mug_plates\": 0, \"STUDY_SCENE1_book_caddy_back\": 0, \"LIVING_ROOM_SCENE6_white_mug_chocolate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0}, \"trigger_rate\": null, \"failure_mode\": \"CUDA_OOM_step_0_every_rollout\", \"error_summary\": \"Every rollout raised torch.AcceleratorError: CUDA error: out of me
…[truncated 577 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-26T10:21:52.660145+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-adaptive-long-s44-cqa1-r2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T10:20:14.793Z\", \"updated_at\": \"2026-05-26T10:21:34.999Z\", \"spec\": {\"command\": \"python src/evaluate.py --benchmark long --mode adaptive_conformal_crm --model pi05 --seed 44 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ --output_file logs/eval_long_adaptive_pi05_seed44.json\", \"server\": \"cqa1-32758\", \"data_path\": \"LIBERO-Long (10 tasks)\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Long 10 tasks x 20 rollouts\"}, \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIBERO-Long should match or exceed the π0.5 VLA-only baseline (~57.2%) by gating CRM refinement only when conformal uncertainty exceeds threshold, avoiding harmful corrections on easy steps.\", \"metrics\": {\"overall_success_rate\": 0, \"successes\": 0, \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"per_task_success_rate\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_yellow_mug_plates\": 0, \"STUDY_SCENE1_book_caddy_back\": 0, \"LIVING_ROOM_SCENE6_white_mug_chocolate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0}, \"trigger_rate\": null, \"failure_mode\": \"CUDA_OOM_step_0_every_rollout\", \"error_summary\": \"Every rollout raised torch.AcceleratorError: CUDA error: out of me
…[truncated 577 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 4
}
```

</details>

---

### Assistant

_source line 68 · 2026-05-26T10:21:52.660514+00:00_

两个实验已转 DONE/negative。**结果不是真实算法负面信号，而是 GPU OOM 系统性失败**：

## 关键发现
- **overall_success_rate = 0.0% (0/200)** ，两 seed 完全一致
- **每个 task 的 20 个 rollout 全部在 step 0 抛 `torch.AcceleratorError: CUDA error: out of memory`**
- 失败位置：`pi05_wrapper.py:163` 在 `torch.flip(img, dims=[2, 3])` 处 OOM
- 触发位置：`pi05_wrapper.preprocess_obs → _preprocess_image`（第一次图像预处理）
- 没有 W&B run（脚本未启用）
- `trigger_rate` 无法计算（adaptive gating 还没机会触发就崩了）
- exit_code = 0（脚本"正常"完成，但每个 rollout 都被异常吞掉）

## 失败原因推断
seed 43/44 分别用 cuda:4 / cuda:5 在 cqa1-32758 上**并行运行**。PI05 模型加载阶段成功（说明每张卡至少能容下权重），但首次 forward 时即 OOM——很可能是同卡上有其他进程占用，或 K=2 采样 + PI05 双 expert 推理峰值超出剩余显存。

## 建议下一步
1. 用 `nvidia-smi` 排查 cqa1-32758 cuda:4/5 是否有其他进程占显存
2. 改为顺序运行（不并行）或换到空闲 GPU 重跑
3. 这两个 run 的 conclusion=negative 仅作为状态标记；**真实的 adaptive vs VLA-only 对比尚未获得**，需要 rerun

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_pi05-adaptive-long-r2_20260526T101850"
}
```

</details>

---
