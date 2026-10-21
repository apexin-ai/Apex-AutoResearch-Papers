# analyze eval supp obj adapt tau025 s42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/chats/worker_analyze_eval-supp-obj-adapt-tau025-s42_20260523T100543.jsonl`
- **Structured JSON:** [`b7bfd4cc89f37b300ce2.json`](../../sessions/b7/b7bfd4cc89f37b300ce2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

7 recorded events

### Tool call

_source line 1 · 2026-05-23T10:06:16.204106+00:00_

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
  "session": "worker_analyze_eval-supp-obj-adapt-tau025-s42_20260523T100543",
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

_source line 2 · 2026-05-23T10:06:16.204507+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval-supp-obj-adapt-tau025-s42_20260523T100543",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T10:06:16.204665+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tail -100 /root/acr-vla-conformal-refinement/logs/eval-supp-obj-adapt-tau025-s42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval-supp-obj-adapt-tau025-s42_20260523T100543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "tail -100 /root/acr-vla-conformal-refinement/logs/eval-supp-obj-adapt-tau025-s42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T10:06:16.204864+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'n_rollouts': 20, 'max_steps': 300, 'seed': 42, 'K': 2, 'mode': 'adaptive_conformal_crm', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'smolvla', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json', 'max_correction_norm': 0.2, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.25, 'n_action_steps': 10}\\n[eval] Mode: adaptive_conformal_crm, benchmark: object\\n[eval] max_steps set to 280 for benchmark object\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  30%|███       | 149/489 [00:00<00:00, 1450.53it/s]\\rLoading weights:  63%|██████▎   | 309/489 [00:00<00:00, 1536.55it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 1760.59it/s]\\nReducing the number of VLM layers to 16 ...\\nLoading weights from local directory\\n[eval] CRM loaded from /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt (327,198 params)\\n[eval] Override max_correction_norm = 0.2\\n[eval] Loading LIBERO object environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 5/20, success so far: 4/5\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 10/20, success so far: 8/10\\n
…[truncated 4843 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval-supp-obj-adapt-tau025-s42_20260523T100543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T10:06:16.205014+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval-supp-obj-adapt-tau025-s42_20260523T100543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T10:06:16.205185+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.81,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    }\\n  },\\n  \\\"adaptive_stats
…[truncated 319 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval-supp-obj-adapt-tau025-s42_20260523T100543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-23T10:06:16.205405+00:00_

## Object Adaptive CRM (τ=0.25, seed=42) 结果

**Overall: 81.0% (162/200)**

### Per-task

| Task | Rate | Succ/Total |
|------|------|------------|
| alphabet_soup | 80% | 16/20 |
| cream_cheese | 80% | 16/20 |
| salad_dressing | **90%** | 18/20 |
| bbq_sauce | **90%** | 18/20 |
| ketchup | 85% | 17/20 |
| tomato_sauce | 80% | 16/20 |
| butter | **65%** | 13/20 |
| milk | 75% | 15/20 |
| chocolate_pudding | 75% | 15/20 |
| orange_juice | **90%** | 18/20 |

### Adaptive Stats

- **trigger_rate**: 3.55% (1236/34838 steps)
- **mean_uncertainty**: 0.1090
- **τ**: 0.25
- **max_correction_norm**: 0.2

### 对比

| Method | Object SR |
|--------|-----------|
| VLA-only | 79% |
| CRM (always-on) | 77% |
| ReConVLA | 79% |
| **Adaptive CRM τ=0.25** | **81%** |

τ=0.25 比之前错误的 τ=0.074855 (77.5%) 高 3.5pp，超过所有 baseline。trigger rate 从之前的高频触发降到 3.55%，说明只在高不确定性时介入，效果更好。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_eval-supp-obj-adapt-tau025-s42_20260523T100543"
}
```

</details>

---
