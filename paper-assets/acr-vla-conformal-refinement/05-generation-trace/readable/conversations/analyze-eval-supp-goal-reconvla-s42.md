# analyze eval supp goal reconvla s42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_analyze_eval-supp-goal-reconvla-s42_20260523T100553.jsonl`
- **Structured JSON:** [`41aff6a2585b83c51972.json`](../../sessions/41/41aff6a2585b83c51972.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-23T10:06:23.460142+00:00_

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
  "session": "worker_analyze_eval-supp-goal-reconvla-s42_20260523T100553",
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

_source line 2 · 2026-05-23T10:06:23.460613+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval-supp-goal-reconvla-s42_20260523T100553",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T10:06:23.460807+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tail -100 /root/acr-vla-conformal-refinement/logs/eval-supp-goal-reconvla-s42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval-supp-goal-reconvla-s42_20260523T100553",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "tail -100 /root/acr-vla-conformal-refinement/logs/eval-supp-goal-reconvla-s42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-23T10:06:23.460945+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ls -lt /root/acr-vla-conformal-refinement/logs/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval-supp-goal-reconvla-s42_20260523T100553",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ls -lt /root/acr-vla-conformal-refinement/logs/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-23T10:06:23.461131+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'goal', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'n_rollouts': 20, 'max_steps': 300, 'seed': 42, 'K': 10, 'mode': 'reconvla', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'smolvla', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_goal_reconvla_seed42.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855, 'n_action_steps': 10}\\n[eval] Mode: reconvla, benchmark: goal\\n[eval] max_steps set to 300 for benchmark goal\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  28%|██▊       | 138/489 [00:00<00:00, 1355.46it/s]\\rLoading weights:  59%|█████▉    | 289/489 [00:00<00:00, 1445.02it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 1709.81it/s]\\nReducing the number of VLM layers to 16 ...\\nLoading weights from local directory\\n[eval] Loading LIBERO goal environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  open_the_middle_drawer_of_the_cabinet: rollout 5/20, success so far: 2/5\\n  open_the_middle_drawer_of_the_cabinet: rollout 10/20, success so far: 7/10\\n  open_the_middle_drawer_of_the_cabinet: rollout 15/20, success so far: 10/15\\n  open_the_middle_drawer_of_the_cabinet: rollout 20/20, success so far: 15/20\\n[open_the_middle_drawer_of_the_cabinet] success rate: 75.0% (15/20)\\n  put_the_b
…[truncated 3666 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval-supp-goal-reconvla-s42_20260523T100553",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T10:06:23.461412+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 20896\\n-rw-r--r-- 1 root root    3207 May 23 18:04 eval-supp-obj-reconvla-s43.log\\n-rw-r--r-- 1 root root    6211 May 23 17:59 eval-supp-k2mean-object-s42.log\\n-rw-r--r-- 1 root root    1500 May 23 17:59 eval_object_vla_only_seed42.json\\n-rw-r--r-- 1 root root    6574 May 23 17:57 eval-supp-obj-adapt-tau025-s42.log\\n-rw-r--r-- 1 root root    1699 May 23 17:57 eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\n-rw-r--r-- 1 root root    7242 May 23 17:32 eval-supp-k2mean-spatial-s42.log\\n-rw-r--r-- 1 root root    1705 May 23 17:32 eval_spatial_vla_only_seed42.json\\n-rw-r--r-- 1 root root    5344 May 23 17:31 eval-goal-vla-only-wrapper-s42.log\\n-rw-r--r-- 1 root root    1328 May 23 17:31 eval_goal_vla_only_seed42.json\\n-rw-r--r-- 1 root root    5400 May 23 17:29 eval-supp-goal-reconvla-s42.log\\n-rw-r--r-- 1 root root    1328 May 23 17:29 eval_goal_reconvla_seed42.json\\n-rw-r--r-- 1 root root    5714 May 23 16:52 eval-supp-goal-adapt-tau025-s42.log\\n-rw-r--r-- 1 root root    1527 May 23 16:52 eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\n-rw-r--r-- 1 root root    6139 May 23 14:57 eval-object-vla-only-wrapper-s44-r2.log\\n-rw-r--r-- 1 root root    1502 May 23 14:57 eval_object_vla_only_seed44.json\\n-rw-r--r-- 1 root root    6211 May 23 14:57 eval-object-vla-only-wrapper-s43-r2.log\\n-rw-r--r-- 1 root root    1502 May 23 14:57 eval_object_vla_only_seed43.json\\n-rw-r--r-- 1 root root    6586 May 23 14:57 eval-supp-obj-adapt-s42-r2.log\\n-rw-r--r-- 1 root root    1706 May 23 14:57 eval_object_adaptive_conformal_crm_norm0.2_tau0.074855_seed42.json\\n-rw-r--r-- 1 root root    6210 May 23 14:56 eval-object-vla-only-wrapper-s42-r2.log\\n-rw-r--r-- 1 root root    6274 May 23 14:54 eval-supp-obj-reconvla-s42.log\\n-rw-r--r-- 1 root root    1502 May 23 14:54 eval_object_reconvla_seed42.json\\n-rw-r--r-- 1 root root    5594 May 23 14:23 eval-supp-goal-crm005-s42.log\\n-rw-r--
…[truncated 6408 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval-supp-goal-reconvla-s42_20260523T100553",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T10:06:23.461640+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed42.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval-supp-goal-reconvla-s42_20260523T100553",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed42.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T10:06:23.461821+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"reconvla\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"goal\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.81,\\n  \\\"per_task\\\": {\\n    \\\"open_the_middle_drawer_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_the_stove\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": {\\n      \\\"success_rate\\\": 0.5,\\n      \\\"successes\\\": 10,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"push_the_plate_to_the_front_of_the_stove\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_cream_cheese_in_the_bowl\\\": {\\n      \\\"success_rate\\\": 0.45,\\n      \\\"successes\\\": 9,\\n      \\\"total\\\": 20\\n    },\\n    \\\"turn_on_the_stove\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_wine_bottle_on_the_rack\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval-supp-goal-reconvla-s42_20260523T100553",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-23T10:06:23.462028+00:00_

## Goal Reconvla K=10 argmin, seed=42

**Overall: 81.0% (162/200)**

| Task | Success Rate | Successes/Total |
|------|-------------|-----------------|
| open_the_middle_drawer_of_the_cabinet | 75.0% | 15/20 |
| put_the_bowl_on_the_stove | 95.0% | 19/20 |
| put_the_wine_bottle_on_top_of_the_cabinet | 90.0% | 18/20 |
| open_the_top_drawer_and_put_the_bowl_inside | 50.0% | 10/20 |
| put_the_bowl_on_top_of_the_cabinet | 95.0% | 19/20 |
| push_the_plate_to_the_front_of_the_stove | 85.0% | 17/20 |
| put_the_cream_cheese_in_the_bowl | 45.0% | 9/20 |
| turn_on_the_stove | 100.0% | 20/20 |
| put_the_bowl_on_the_plate | 95.0% | 19/20 |
| put_the_wine_bottle_on_the_rack | 80.0% | 16/20 |

对比：Goal VLA-only=83.5%, Goal CRM=85.5%, **Goal Reconvla=81.0%**。Reconvla 在 Goal suite 上低于 VLA-only 2.5pp，低于 CRM 4.5pp。两个弱任务拖后腿：cream_cheese (45%) 和 top_drawer_bowl (50%)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_eval-supp-goal-reconvla-s42_20260523T100553"
}
```

</details>

---
