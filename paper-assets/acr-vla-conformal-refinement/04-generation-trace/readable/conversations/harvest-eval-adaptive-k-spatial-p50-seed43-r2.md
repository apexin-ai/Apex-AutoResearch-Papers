# harvest eval adaptive k spatial p50 seed43 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/chats/worker_harvest_eval-adaptive-k-spatial-p50-seed43-r2_20260520T092516.jsonl`
- **Structured JSON:** [`8e713850e9eaa6f972d9.json`](../../sessions/8e/8e713850e9eaa6f972d9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

13 recorded events

### Tool call

_source line 1 · 2026-05-20T09:26:22.144024+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_eval-adaptive-k-spatial-p50-seed43-r2_20260520T092516",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T09:26:22.144377+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_eval-adaptive-k-spatial-p50-seed43-r2_20260520T092516",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T09:26:22.144553+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p50_seed43.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_eval-adaptive-k-spatial-p50-seed43-r2_20260520T092516",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p50_seed43.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T09:26:22.144948+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_k\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.33,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 8,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 10,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.4,\\n      \\\"successes\\\": 4,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 9,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_on
…[truncated 8295 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_eval-adaptive-k-spatial-p50-seed43-r2_20260520T092516",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T09:26:22.145195+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-adaptive-k-spatial-p50-seed43-r2",
  "field": "metrics",
  "value": "{'overall_success_rate': 0.33, 'per_task_sr': {'between_plate_and_ramekin': 0.8, 'next_to_ramekin': 1, 'from_table_center': 0, 'on_cookie_box': 0.4, 'in_top_drawer': 0.1, 'on_ramekin': 0, 'next_to_cookie_box': 0.9, 'on_stove': 0, 'next_to_plate': 0.1, 'on_wooden_cabinet': 0}, 'avg_k': 6.33, 'fast_path_ratio': 0.458, 'adaptive_trigger_rate': 0.542, 'mean_l2_distance': 0.0903, 'total_steps': 23414, 'fast_steps': 10728, 'full_steps': 12686, 'threshold': 0.074855, 'total_rollouts': 100}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_eval-adaptive-k-spatial-p50-seed43-r2_20260520T092516",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-adaptive-k-spatial-p50-seed43-r2",
    "field": "metrics",
    "value": "{'overall_success_rate': 0.33, 'per_task_sr': {'between_plate_and_ramekin': 0.8, 'next_to_ramekin': 1, 'from_table_center': 0, 'on_cookie_box': 0.4, 'in_top_drawer': 0.1, 'on_ramekin': 0, 'next_to_cookie_box': 0.9, 'on_stove': 0, 'next_to_plate': 0.1, 'on_wooden_cabinet': 0}, 'avg_k': 6.33, 'fast_path_ratio': 0.458, 'adaptive_trigger_rate': 0.542, 'mean_l2_distance': 0.0903, 'total_steps': 23414, 'fast_steps': 10728, 'full_steps': 12686, 'threshold': 0.074855, 'total_rollouts': 100}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T09:26:22.145451+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-adaptive-k-spatial-p50-seed43-r2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T06:42:06.832Z\", \"updated_at\": \"2026-05-20T09:25:58.413Z\", \"hypothesis\": \"K=2 L2 divergence-based adaptive K allocation (P50 threshold τ=0.074855) transfers from Object to Spatial benchmark, achieving comparable SR to fixed K=10 with ~62% compute savings. Cross-benchmark validation of adaptive K as core method.\", \"parent\": \"eval-adaptive-k-spatial-p50-seed43\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode adaptive_k --adaptive_threshold 0.074855 --k_full 10 --benchmark spatial --seed 43 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_adaptive_k_spatial_p50_seed43.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"303834\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p50-seed43-r2.log\", \"submitted_at\": \"2026-05-20T07:07:51.122Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-20T07:07:47.040Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode adaptive_k --adaptive_threshold 0.074855 --k_full 10 --benchmark spatial --seed 43 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/chec
…[truncated 1065 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_eval-adaptive-k-spatial-p50-seed43-r2_20260520T092516",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T09:26:22.145615+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-adaptive-k-spatial-p50-seed43-r2",
  "field": "conclusion",
  "value": "success",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_eval-adaptive-k-spatial-p50-seed43-r2_20260520T092516",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-adaptive-k-spatial-p50-seed43-r2",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-20T09:26:22.145748+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-adaptive-k-spatial-p50-seed43-r2",
  "field": "spec",
  "value": "{'checkpoint_path': 'N/A (eval only)', 'log_path': '~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p50-seed43-r2.log'}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_eval-adaptive-k-spatial-p50-seed43-r2_20260520T092516",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-adaptive-k-spatial-p50-seed43-r2",
    "field": "spec",
    "value": "{'checkpoint_path': 'N/A (eval only)', 'log_path': '~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p50-seed43-r2.log'}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-20T09:26:22.145933+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-adaptive-k-spatial-p50-seed43-r2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T06:42:06.832Z\", \"updated_at\": \"2026-05-20T09:26:03.401Z\", \"hypothesis\": \"K=2 L2 divergence-based adaptive K allocation (P50 threshold τ=0.074855) transfers from Object to Spatial benchmark, achieving comparable SR to fixed K=10 with ~62% compute savings. Cross-benchmark validation of adaptive K as core method.\", \"parent\": \"eval-adaptive-k-spatial-p50-seed43\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode adaptive_k --adaptive_threshold 0.074855 --k_full 10 --benchmark spatial --seed 43 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_adaptive_k_spatial_p50_seed43.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"303834\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p50-seed43-r2.log\", \"submitted_at\": \"2026-05-20T07:07:51.122Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-20T07:07:47.040Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode adaptive_k --adaptive_threshold 0.074855 --k_full 10 --benchmark spatial --seed 43 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/chec
…[truncated 1094 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_eval-adaptive-k-spatial-p50-seed43-r2_20260520T092516",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T09:26:22.146162+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-adaptive-k-spatial-p50-seed43-r2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T06:42:06.832Z\", \"updated_at\": \"2026-05-20T09:26:05.141Z\", \"hypothesis\": \"K=2 L2 divergence-based adaptive K allocation (P50 threshold τ=0.074855) transfers from Object to Spatial benchmark, achieving comparable SR to fixed K=10 with ~62% compute savings. Cross-benchmark validation of adaptive K as core method.\", \"parent\": \"eval-adaptive-k-spatial-p50-seed43\", \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p50-seed43-r2.log\"}, \"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-20T07:07:47.040Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode adaptive_k --adaptive_threshold 0.074855 --k_full 10 --benchmark spatial --seed 43 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_adaptive_k_spatial_p50_seed43.json\\\"\", \"finished_at\": \"2026-05-20T09:14:06.027Z\", \"training_hours\": 2.11}, \"pid\": \"303834\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p50-seed43-r2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T09:14:15.835758+00:00\"}]}, \"metrics\": {\"overall_success_rate\": 0.33, \"per_task_sr\": {\"between_plate_and_ramekin\": 0.8, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.4, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9,
…[truncated 393 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_eval-adaptive-k-spatial-p50-seed43-r2_20260520T092516",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T09:26:22.146388+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-adaptive-k-spatial-p50-seed43-r2",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_eval-adaptive-k-spatial-p50-seed43-r2_20260520T092516",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-adaptive-k-spatial-p50-seed43-r2",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T09:26:22.146603+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-adaptive-k-spatial-p50-seed43-r2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T06:42:06.832Z\", \"updated_at\": \"2026-05-20T09:26:09.877Z\", \"hypothesis\": \"K=2 L2 divergence-based adaptive K allocation (P50 threshold τ=0.074855) transfers from Object to Spatial benchmark, achieving comparable SR to fixed K=10 with ~62% compute savings. Cross-benchmark validation of adaptive K as core method.\", \"parent\": \"eval-adaptive-k-spatial-p50-seed43\", \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p50-seed43-r2.log\"}, \"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-20T07:07:47.040Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode adaptive_k --adaptive_threshold 0.074855 --k_full 10 --benchmark spatial --seed 43 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_adaptive_k_spatial_p50_seed43.json\\\"\", \"finished_at\": \"2026-05-20T09:14:06.027Z\", \"training_hours\": 2.11}, \"pid\": \"303834\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p50-seed43-r2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T09:14:15.835758+00:00\"}]}, \"metrics\": {\"overall_success_rate\": 0.33, \"per_task_sr\": {\"between_plate_and_ramekin\": 0.8, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.4, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on
…[truncated 486 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_eval-adaptive-k-spatial-p50-seed43-r2_20260520T092516",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-20T09:26:22.146795+00:00_

Registry 已更新为 DONE/success。

## 摘要

| 指标 | Adaptive-K Spatial P50 | Spatial K=10 baseline | Object P50 |
|------|----------------------|----------------------|------------|
| **SR** | **33.0%** | 34.3% (±1.5%) | 15.3% |
| **avg_K** | **6.33** | 10 | 3.8 |
| **fast_path** | **45.8%** | N/A | 77% |
| **compute saving** | **~37%** | — | ~62% |

P50 阈值（τ=0.074855）从 Object 迁移到 Spatial：SR 仅降 1.3pp（在 baseline CI 内），avg_K=6.33 节省 37% 计算。Spatial 任务 L2 divergence 均值更高（0.090 vs Object），导致 fast_path 从 77% 降至 46%——Spatial 任务不确定性更大，需要更多 full refinement steps，但自适应分配仍能在不损失 SR 的前提下显著节省计算。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_harvest_eval-adaptive-k-spatial-p50-seed43-r2_20260520T092516"
}
```

</details>

---
