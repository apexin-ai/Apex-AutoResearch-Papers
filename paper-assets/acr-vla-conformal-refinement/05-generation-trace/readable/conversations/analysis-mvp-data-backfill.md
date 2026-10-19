# analysis mvp data backfill

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_analysis_mvp-data-backfill_20260513T220508.jsonl`
- **Structured JSON:** [`07ee7dc7d9d08f28daa0.json`](../../sessions/07/07ee7dc7d9d08f28daa0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-13T22:06:18.356908+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_registry",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mvp-data-backfill_20260513T220508",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_registry",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-13T22:06:18.357227+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mvp-data-backfill_20260513T220508",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-13T22:06:18.357415+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*mvp*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mvp-data-backfill_20260513T220508",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*mvp*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-13T22:06:18.357559+00:00_

artifacts/mvp-point-reaching/data/mvp_results.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mvp-data-backfill_20260513T220508",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-13T22:06:18.357682+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*point*reaching*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mvp-data-backfill_20260513T220508",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*point*reaching*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-13T22:06:18.357800+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mvp-data-backfill_20260513T220508",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-13T22:06:18.357915+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*plan_000*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mvp-data-backfill_20260513T220508",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*plan_000*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-13T22:06:18.358028+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mvp-data-backfill_20260513T220508",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-13T22:06:18.358151+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/mvp-point-reaching/data/mvp_results.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mvp-data-backfill_20260513T220508",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/mvp-point-reaching/data/mvp_results.log"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-13T22:06:18.358309+00:00_

1	================================================================================
2	3D Point-Reaching MVP: per-DOF vs scalar vs no uncertainty
3	Design: bias = sigma * 2.5; obs = noisy_action only
4	================================================================================
5	
6	--- Group 1: sigma=(0.5,0.1,0.1), unc=oracle ---
7	  G1 [oracle] A(scalar): x=0.180218 y=0.024970 z=0.024232 total=0.076473
8	  G1 [oracle] B(per-DOF): x=0.172652 y=0.015544 z=0.015610 total=0.067935
9	  G1 [oracle] C(none): x=0.227060 y=0.025542 z=0.024753 total=0.092451
10	
11	  Pass check Group 1:
12	  C1(B vs A): y_imp=0.3775 z_imp=0.3558 x_ok=True -> PASS
13	  C2(B vs C): imps=['0.2396', '0.3914', '0.3694'] -> PASS
14	  Group 1: PASS
15	
16	--- Group 2: sigma=(0.2,0.1,0.1), unc=oracle ---
17	  G2 [oracle] A(scalar): x=0.064642 y=0.023836 z=0.022967 total=0.037148
18	  G2 [oracle] B(per-DOF): x=0.053403 y=0.015695 z=0.015730 total=0.028276
19	  G2 [oracle] C(none): x=0.084178 y=0.025427 z=0.024798 total=0.044801
20	
21	--- Group 3: sigma=(0.15,0.1,0.1), unc=oracle ---
22	  G3 [oracle] A(scalar): x=0.042948 y=0.023218 z=0.022365 total=0.029510
23	  G3 [oracle] B(per-DOF): x=0.033008 y=0.015621 z=0.015647 total=0.021425
24	  G3 [oracle] C(none): x=0.053043 y=0.025523 z=0.024741 total=0.034436
25	
26	--- Group 4: sigma=(0.5,0.1,0.1), unc=K=10 ---
27	  G4 [K=10] A(scalar): x=0.187418 y=0.024701 z=0.024277 total=0.078799
28	  G4 [K=10] B(per-DOF): x=0.182888 y=0.019072 z=0.018475 total=0.073478
29	  G4 [K=10] C(none): x=0.215070 y=0.024960 z=0.024637 total=0.088223
30	
31	  Pass check Group 4:
32	  C1(B vs A): y_imp=0.2279 z_imp=0.2390 x_ok=True -> PASS
33	  C2(B vs C): imps=['0.1496', '0.2359', '0.2501'] -> PASS
34	  Group 4: PASS
35	
36	--- Group 5: sigma=(0.2,0.1,0.1), unc=K=10 ---
37	  G5 [K=10] A(scalar): x=0.064895 y=0.023860 z=0.023596 total=0.037451
38	  G5 [K=10] B(per-DOF): x=0.058510 y=0.018868 z=0.018471 total=0.031950
39	  G5 [K=10] C(none): x=0.077047 y=0.024825 z=0.024640
…[truncated 2132 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mvp-data-backfill_20260513T220508",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-13T22:06:18.358476+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "limit": "0",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mvp-data-backfill_20260513T220508",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "limit": "0",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T22:06:18.359024+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-reconvla-spatial-v2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:29:41.730Z\", \"updated_at\": \"2026-05-13T20:33:38.453Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"87787\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-reconvla-spatial-v1.log\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"smolvla_libero + ReconVLA argmin\", \"seed\": 42, \"hypothesis\": \"ReconVLA (scalar Euclidean nonconformity + argmin) as baseline for ACR-VLA comparison\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"libero_spatial 10 tasks\"}}, \"precompute-k5\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:15:37.603Z\", \"updated_at\": \"2026-05-13T20:33:36.187Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --precompute --benchmark spatial object --K 5 --cache_dir /root/autodl-tmp/crm_cache_k5/\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"79517\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-k5.log\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 26737, \"model_name\": \"smolvla_libero\", \"seed\": 42, \"hypothesis\": \"K=5 precompute for K sensitivity ablation (plan_015)\"}}, \"eval-object-v4-full\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:13:26.341Z\", \"updated_at\": \"2026-05-13T20:33:34.145Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"103768\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-object-v4-full.log\", \"data_path\": \"/root/autodl-tmp/libero_data/ (object)\", \"data
…[truncated 24593 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mvp-data-backfill_20260513T220508",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-13T22:06:18.359207+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/mvp-point-reaching"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mvp-data-backfill_20260513T220508",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/mvp-point-reaching"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-13T22:06:18.359402+00:00_

artifacts/mvp-point-reaching/data/mvp_results.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mvp-data-backfill_20260513T220508",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T22:06:18.359634+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "mvp-point-reaching",
  "field": "metrics",
  "value": "{'group1_oracle': {'A_scalar': {'mse_x': 0.180218, 'mse_y': 0.02497, 'mse_z': 0.024232, 'total': 0.076473}, 'B_perDOF': {'mse_x': 0.172652, 'mse_y': 0.015544, 'mse_z': 0.01561, 'total': 0.067935}, 'C_none': {'mse_x': 0.22706, 'mse_y': 0.025542, 'mse_z': 0.024753, 'total': 0.092451}}, 'group2_oracle': {'A_scalar': {'mse_x': 0.064642, 'mse_y': 0.023836, 'mse_z': 0.022967, 'total': 0.037148}, 'B_perDOF': {'mse_x': 0.053403, 'mse_y': 0.015695, 'mse_z': 0.01573, 'total': 0.028276}, 'C_none': {'mse_x': 0.084178, 'mse_y': 0.025427, 'mse_z': 0.024798, 'total': 0.044801}}, 'group3_oracle': {'A_scalar': {'mse_x': 0.042948, 'mse_y': 0.023218, 'mse_z': 0.022365, 'total': 0.02951}, 'B_perDOF': {'mse_x': 0.033008, 'mse_y': 0.015621, 'mse_z': 0.015647, 'total': 0.021425}, 'C_none': {'mse_x': 0.053043, 'mse_y': 0.025523, 'mse_z': 0.024741, 'total': 0.034436}}, 'group4_K10': {'A_scalar': {'mse_x': 0.187418, 'mse_y': 0.024701, 'mse_z': 0.024277, 'total': 0.078799}, 'B_perDOF': {'mse_x': 0.182888, 'mse_y': 0.019072, 'mse_z': 0.018475, 'total': 0.073478}, 'C_none': {'mse_x': 0.21507, 'mse_y': 0.02496, 'mse_z': 0.024637, 'total': 0.088223}}, 'group5_K10': {'A_scalar': {'mse_x': 0.064895, 'mse_y': 0.02386, 'mse_z': 0.023596, 'total': 0.037451}, 'B_perDOF': {'mse_x': 0.05851, 'mse_y': 0.018868, 'mse_z': 0.018471, 'total': 0.03195}, 'C_none': {'mse_x': 0.077047, 'mse_y': 0.024825, 'mse_z': 0.02464, 'total': 0.042171}}, 'group6_K10': {'A_scalar': {'mse_x': 0.041848, 'mse_y': 0.02344, 'mse_z': 0.023207, 'total': 0.029498}, 'B_perDOF': {'mse_x': 0.036348, 'mse_y': 0.018736, 'mse_z': 0.018453, 'total': 0.024512}, 'C_none': {'mse_x': 0.048365, 'mse_y': 0.024827, 'mse_z': 0.024577, 'total': 0.03259}}, 'pass_criteria': {'group1': 'PASS', 'group4': 'PASS', 'overall': 'SUCCESS'}, 'summary_pct_improvements': {'reference_group': 'group4_K10 (sigma=0.5/0.1/0.1, K=10 estimated uncertainty)', 'perDOF_vs_scalar_total': 6.75, 'perDOF_vs_none_total': 16.71, 'perDOF_vs_scalar_y_axis': 22.79, 'perDOF_vs_scalar_z_axis': 23.9, 'paper_claims': {'6.7_pct_over_scalar': 'group4 total: (0.078799-0.073478)/0.078799 = 6.75%', '16.7_pct_over_none': 'group4 total: (0.088223-0.073478)/0.088223 = 16.71%', '22_24_pct_per_axis': 'group4 y: 22.79%, z: 23.90%'}}}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mvp-data-backfill_20260513T220508",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "mvp-point-reaching",
    "field": "metrics",
    "value": "{'group1_oracle': {'A_scalar': {'mse_x': 0.180218, 'mse_y': 0.02497, 'mse_z': 0.024232, 'total': 0.076473}, 'B_perDOF': {'mse_x': 0.172652, 'mse_y': 0.015544, 'mse_z': 0.01561, 'total': 0.067935}, 'C_none': {'mse_x': 0.22706, 'mse_y': 0.025542, 'mse_z': 0.024753, 'total': 0.092451}}, 'group2_oracle': {'A_scalar': {'mse_x': 0.064642, 'mse_y': 0.023836, 'mse_z': 0.022967, 'total': 0.037148}, 'B_perDOF': {'mse_x': 0.053403, 'mse_y': 0.015695, 'mse_z': 0.01573, 'total': 0.028276}, 'C_none': {'mse_x': 0.084178, 'mse_y': 0.025427, 'mse_z': 0.024798, 'total': 0.044801}}, 'group3_oracle': {'A_scalar': {'mse_x': 0.042948, 'mse_y': 0.023218, 'mse_z': 0.022365, 'total': 0.02951}, 'B_perDOF': {'mse_x': 0.033008, 'mse_y': 0.015621, 'mse_z': 0.015647, 'total': 0.021425}, 'C_none': {'mse_x': 0.053043, 'mse_y': 0.025523, 'mse_z': 0.024741, 'total': 0.034436}}, 'group4_K10': {'A_scalar': {'mse_x': 0.187418, 'mse_y': 0.024701, 'mse_z': 0.024277, 'total': 0.078799}, 'B_perDOF': {'mse_x': 0.182888, 'mse_y': 0.019072, 'mse_z': 0.018475, 'total': 0.073478}, 'C_none': {'mse_x': 0.21507, 'mse_y': 0.02496, 'mse_z': 0.024637, 'total': 0.088223}}, 'group5_K10': {'A_scalar': {'mse_x': 0.064895, 'mse_y': 0.02386, 'mse_z': 0.023596, 'total': 0.037451}, 'B_perDOF': {'mse_x': 0.05851, 'mse_y': 0.018868, 'mse_z': 0.018471, 'total': 0.03195}, 'C_none': {'mse_x': 0.077047, 'mse_y': 0.024825, 'mse_z': 0.02464, 'total': 0.042171}}, 'group6_K10': {'A_scalar': {'mse_x': 0.041848, 'mse_y': 0.02344, 'mse_z': 0.023207, 'total': 0.029498}, 'B_perDOF': {'mse_x': 0.036348, 'mse_y': 0.018736, 'mse_z': 0.018453, 'total': 0.024512}, 'C_none': {'mse_x': 0.048365, 'mse_y': 0.024827, 'mse_z': 0.024577, 'total': 0.03259}}, 'pass_criteria': {'group1': 'PASS', 'group4': 'PASS', 'overall': 'SUCCESS'}, 'summary_pct_improvements': {'reference_group': 'group4_K10 (sigma=0.5/0.1/0.1, K=10 estimated uncertainty)', 'perDOF_vs_scalar_total': 6.75, 'perDOF_vs_none_total': 16.71, 'perDOF_vs_scalar_y_axis': 22.79, 'perDOF_vs_scalar_z_axis': 23.9, 'paper_claims': {'6.7_pct_over_scalar': 'group4 total: (0.078799-0.073478)/0.078799 = 6.75%', '16.7_pct_over_none': 'group4 total: (0.088223-0.073478)/0.088223 = 16.71%', '22_24_pct_per_axis': 'group4 y: 22.79%, z: 23.90%'}}}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-13T22:06:18.359909+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"mvp-point-reaching\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T01:22:10.415Z\", \"updated_at\": \"2026-05-13T22:06:11.073Z\", \"spec\": {\"hypothesis\": \"Per-DOF uncertainty features carry more actionable information than scalar uncertainty summaries, enabling dimension-selective correction\", \"description\": \"3D point-reaching MVP: 3 MLP variants (scalar/per-DOF/no uncertainty) x 6 groups (3 anisotropy ratios x 2 uncertainty sources)\", \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"data_count\": 20000, \"model_name\": \"CorrectionMLP(2-layer, 64-hidden)\", \"seed\": 42, \"command\": \"python -u run_mvp.py\", \"data_path\": \"synthetic (generated in-script)\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/mvp/\", \"log_path\": \"/root/acr-vla-conformal-refinement/mvp/mvp_results.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T01:44:00.055Z\", \"metrics\": {\"group1_oracle\": {\"A_scalar\": {\"mse_x\": 0.180218, \"mse_y\": 0.02497, \"mse_z\": 0.024232, \"total\": 0.076473}, \"B_perDOF\": {\"mse_x\": 0.172652, \"mse_y\": 0.015544, \"mse_z\": 0.01561, \"total\": 0.067935}, \"C_none\": {\"mse_x\": 0.22706, \"mse_y\": 0.025542, \"mse_z\": 0.024753, \"total\": 0.092451}}, \"group2_oracle\": {\"A_scalar\": {\"mse_x\": 0.064642, \"mse_y\": 0.023836, \"mse_z\": 0.022967, \"total\": 0.037148}, \"B_perDOF\": {\"mse_x\": 0.053403, \"mse_y\": 0.015695, \"mse_z\": 0.01573, \"total\": 0.028276}, \"C_none\": {\"mse_x\": 0.084178, \"mse_y\": 0.025427, \"mse_z\": 0.024798, \"total\": 0.044801}}, \"group3_oracle\": {\"A_scalar\": {\"mse_x\": 0.042948, \"mse_y\": 0.023218, \"mse_z\": 0.022365, \"total\": 0.02951}, \"B_perDOF\": {\"mse_x\": 0.033008, \"mse_y\": 0.015621, \"mse_z\": 0.015647, \"total\": 0.021425}, \"C_none\": {\"mse_x\": 0.053043, \"mse_y\": 0.025523, \"mse_z\": 0.024741, \"total\": 0.034436}}, \"group4_K10\": {\"A_scalar\": {\"ms
…[truncated 1555 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mvp-data-backfill_20260513T220508",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-13T22:06:18.360118+00:00_

Registry 更新完成。

**汇总：**

- **数据源文件**: `artifacts/mvp-point-reaching/data/mvp_results.log`
- **Registry 条目**: `mvp-point-reaching` (status: DONE, conclusion: success)
- **论文引用验证** (均来自 Group 4, K=10)：

| 论文引用 | 实际计算 | 来源 |
|---------|---------|------|
| "6.7% over scalar" | (0.078799−0.073478)/0.078799 = **6.75%** | B vs A total MSE |
| "16.7% over no uncertainty" | (0.088223−0.073478)/0.088223 = **16.71%** | B vs C total MSE |
| "22-24% improvements" | y: **22.79%**, z: **23.90%** | B vs A per-axis MSE |

已将 `summary_pct_improvements` 字段（含改进百分比和 paper claims 溯源公式）补录到 registry metrics 中。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_mvp-data-backfill_20260513T220508"
}
```

</details>

---
