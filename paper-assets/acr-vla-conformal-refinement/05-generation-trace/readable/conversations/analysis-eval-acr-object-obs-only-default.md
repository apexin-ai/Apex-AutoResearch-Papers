# analysis eval acr object obs only default

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/chats/worker_analysis_eval-acr-object-obs-only-default_20260516T064252.jsonl`
- **Structured JSON:** [`7c397ed56612d0c898bb.json`](../../sessions/7c/7c397ed56612d0c898bb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

7 recorded events

### Tool call

_source line 1 · 2026-05-16T06:43:20.514415+00:00_

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
  "session": "worker_analysis_eval-acr-object-obs-only-default_20260516T064252",
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

_source line 2 · 2026-05-16T06:43:20.514746+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval-acr-object-obs-only-default_20260516T064252",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T06:43:20.514915+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -200 ~/runs/acr-vla-conformal-refinement/eval-acr-object-obs-only-default.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval-acr-object-obs-only-default_20260516T064252",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tail -200 ~/runs/acr-vla-conformal-refinement/eval-acr-object-obs-only-default.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T06:43:20.515113+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'n_rollouts': 10, 'max_steps': 300, 'seed': 42, 'K': 10, 'mode': 'crm_obs_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'obs_dim': 960, 'hidden_dim': 256, 'render': False, 'output_file': 'logs/eval_object_obs_only_default_norm.json', 'max_correction_norm': None}\\n[eval] Mode: crm_obs_only, benchmark: object\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  61%|██████▏   | 300/489 [00:00<00:00, 2994.41it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 3424.46it/s]\\nReducing the number of VLM layers to 16 ...\\nLoading weights from local directory\\n[eval] CRM loaded from /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt (327,198 params)\\n[eval] Loading LIBERO object environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 5/10, success so far: 0/5\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 10/10, success so far: 0/10\\n[pick_up_the_alphabet_soup_and_place_it_in_the_basket] success rate: 0.0% (0/10)\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 5/10, success so far: 0/5\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 10/10, success so far: 0/10\\n[pick_up_the_cream_cheese_and_place_it_in_the_basket] success rate: 0.0% (0/10)\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 5/10, success so far: 1/5\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 10/10, s
…[truncated 2377 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval-acr-object-obs-only-default_20260516T064252",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T06:43:20.515285+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_norm.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval-acr-object-obs-only-default_20260516T064252",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_norm.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T06:43:20.515472+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.17,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.4,\\n      \\\"successes\\\": 4,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.5,\\n      \\\"successes\\\": 5,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \
…[truncated 60 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval-acr-object-obs-only-default_20260516T064252",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-16T06:43:20.515678+00:00_

```
TASKS_DONE: 10
TASKS_TOTAL: 10
OVERALL_SR: 17%
PER_TASK_SR: {alphabet_soup: 0%, cream_cheese: 0%, salad_dressing: 20%, bbq_sauce: 40%, ketchup: 0%, tomato_sauce: 10%, butter: 10%, milk: 10%, chocolate_pudding: 50%, orange_juice: 30%}
CONCLUSION: negative
ANALYSIS: Default max_correction_norm (~1.42) 的 obs_only 得到 17% SR，与 norm=0.1 (19%) 和 norm=0.2 (22%) 相比略低但处于同一量级。这说明 obs_only 模式对 correction norm 的大小确实非常鲁棒——即使 norm 从 0.1 放大到 1.42（14倍），SR 仅从 19-22% 微降到 17%，差异在统计噪声范围内。但整体 SR 仍然很低（17%），远低于 baseline 或 full CRM 的表现，说明 obs_only 本身的 refinement 能力有限，而非 norm 控制的问题。Hypothesis 部分验证：obs_only 对 norm 确实鲁棒，但鲁棒地维持在低性能水平。
LOG_TAIL:
[pick_up_the_chocolate_pudding_and_place_it_in_the_basket] success rate: 50.0% (5/10)
  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 5/10, success so far: 2/5
  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 10/10, success so far: 3/10
[pick_up_the_orange_juice_and_place_it_in_the_basket] success rate: 30.0% (3/10)

============================================================
Overall success rate (crm_obs_only): 17.0% (17/100)
============================================================
[eval] Results saved to logs/eval_object_obs_only_default_norm.json
sys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute
EXIT_CODE=0
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_eval-acr-object-obs-only-default_20260516T064252"
}
```

</details>

---
