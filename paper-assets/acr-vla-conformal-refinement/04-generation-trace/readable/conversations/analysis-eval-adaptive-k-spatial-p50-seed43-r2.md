# analysis eval adaptive k spatial p50 seed43 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/chats/worker_analysis_eval-adaptive-k-spatial-p50-seed43-r2_20260520T091527.jsonl`
- **Structured JSON:** [`9d1e26d75a8379c51de0.json`](../../sessions/9d/9d1e26d75a8379c51de0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

7 recorded events

### Tool call

_source line 1 · 2026-05-20T09:16:03.518120+00:00_

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
  "session": "worker_analysis_eval-adaptive-k-spatial-p50-seed43-r2_20260520T091527",
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

_source line 2 · 2026-05-20T09:16:03.518474+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval-adaptive-k-spatial-p50-seed43-r2_20260520T091527",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T09:16:03.518652+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -100 ~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p50-seed43-r2.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval-adaptive-k-spatial-p50-seed43-r2_20260520T091527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tail -100 ~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p50-seed43-r2.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T09:16:03.518797+00:00_

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
  "session": "worker_analysis_eval-adaptive-k-spatial-p50-seed43-r2_20260520T091527",
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

_source line 5 · 2026-05-20T09:16:03.518992+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'spatial', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'n_rollouts': 10, 'max_steps': 300, 'seed': 43, 'K': 10, 'mode': 'adaptive_k', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'obs_dim': 960, 'hidden_dim': 256, 'render': False, 'output_file': 'logs/eval_adaptive_k_spatial_p50_seed43.json', 'max_correction_norm': 0.2, 'adaptive_k': False, 'adaptive_threshold': 0.074855, 'k_init': 2, 'k_full': 10}\\n[eval] Mode: adaptive_k, benchmark: spatial\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  68%|██████▊   | 333/489 [00:00<00:00, 3265.06it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 3586.15it/s]\\nReducing the number of VLM layers to 16 ...\\nLoading weights from local directory\\n[eval] CRM loaded from /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt (327,198 params)\\n[eval] Override max_correction_norm = 0.2\\n[eval] Loading LIBERO spatial environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 5/10, success so far: 4/5\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 10/10, success so far: 8/10\\n[pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate] success rate: 80.0% (8/10)\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout 5/10, success so far: 5/5\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout 10/10, success so far: 10/10\\
…[truncated 3184 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval-adaptive-k-spatial-p50-seed43-r2_20260520T091527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T09:16:03.519394+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_k\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.33,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 8,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 10,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.4,\\n      \\\"successes\\\": 4,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 9,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_on
…[truncated 8295 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval-adaptive-k-spatial-p50-seed43-r2_20260520T091527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-20T09:16:03.519733+00:00_

实验正常完成（EXIT_CODE=0）。结果如下：

## 总体指标

| 指标 | 值 |
|------|-----|
| **success_rate** | **33.0%** (33/100) |
| n_tasks | 10 |
| n_rollouts | 10 per task |
| total_rollouts | 100 |
| **avg_K** | **6.33** |
| **fast_path_ratio** | **45.8%** |
| adaptive_trigger_rate | 54.2% |
| mean_l2_distance | 0.0903 |
| threshold (τ) | 0.074855 |
| total_steps | 23,414 |
| fast_steps (K=2) | 10,728 |
| full_steps (K=10) | 12,686 |

## Per-task SR

| Task | SR |
|------|-----|
| bowl_next_to_ramekin → plate | **100%** (10/10) |
| bowl_next_to_cookie_box → plate | **90%** (9/10) |
| bowl_between_plate_and_ramekin → plate | **80%** (8/10) |
| bowl_on_cookie_box → plate | 40% (4/10) |
| bowl_in_top_drawer → plate | 10% (1/10) |
| bowl_next_to_plate → plate | 10% (1/10) |
| bowl_from_table_center → plate | 0% (0/10) |
| bowl_on_ramekin → plate | 0% (0/10) |
| bowl_on_stove → plate | 0% (0/10) |
| bowl_on_wooden_cabinet → plate | 0% (0/10) |

## 与 Baseline 对比

| 配置 | SR | avg_K | fast_path |
|------|-----|-------|-----------|
| **Spatial K=10 固定** | **34.4±1.5%** | 10.0 | 0% |
| **Spatial Adaptive P50 (本次)** | **33.0%** | 6.33 | 45.8% |
| Object Adaptive P50 (参考) | 15.3% | ~3.8 | ~77% |

## Checkpoint

- CRM: `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt`
- SmolVLA: `/root/autodl-tmp/models/smolvla_libero/`
- max_correction_norm: 0.2

## 关键发现

1. **SR 33.0% vs K=10 baseline 34.4%** — 仅损失 1.4pp，在 ±1.5% 的 baseline 方差范围内，可认为**无显著差异**
2. **avg_K=6.33，节省 36.7% 推理次数**（vs K=10 固定），但远不如 Object benchmark 的 avg_K=3.8
3. **fast_path=45.8%** 远低于 Object 的 77% — Spatial 任务的 L2 divergence 更频繁超过 P50 阈值，说明 Spatial 场景 CRM 修正需求更大
4. 任务极化严重：3 个 task ≥80% SR，4 个 task = 0%，与 K=10 固定模式的 task 分布应基本一致

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_eval-adaptive-k-spatial-p50-seed43-r2_20260520T091527"
}
```

</details>

---
