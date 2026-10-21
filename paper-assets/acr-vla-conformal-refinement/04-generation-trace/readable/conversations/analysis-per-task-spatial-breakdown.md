# analysis per task spatial breakdown

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 215
- **Recorded user turns:** 0
- **Tool calls:** 106
- **Original source:** `logs/chats/worker_analysis_per-task-spatial-breakdown_20260524T222035.jsonl`
- **Structured JSON:** [`7be06d48b90ad4a9529a.json`](../../sessions/7b/7be06d48b90ad4a9529a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

215 recorded events

### Assistant

_source line 1 · 2026-05-24T22:20:45.650049+00:00_

Not logged in · Please run /login

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-24T22:27:00.466036+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,TodoWrite",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,TodoWrite",
    "max_results": "10"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-24T22:27:00.466414+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-24T22:27:00.466615+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Locate Spatial experiment result files on bjb2-40593', 'activeForm': 'Locating Spatial experiment result files on bjb2-40593', 'status': 'in_progress'}, {'content': 'Extract per-task SR for VLA-only and Adaptive', 'activeForm': 'Extracting per-task SR for VLA-only and Adaptive', 'status': 'pending'}, {'content': 'Identify always-0% tasks and compute Δ + p-value', 'activeForm': 'Identifying always-0% tasks and computing Δ + p-value', 'status': 'pending'}, {'content': 'Mechanism analysis: trigger_rate vs Δ correlation', 'activeForm': 'Analyzing mechanism: trigger_rate vs Δ correlation', 'status': 'pending'}, {'content': 'Output formatted breakdown table', 'activeForm': 'Outputting formatted breakdown table', 'status': 'pending'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Locate Spatial experiment result files on bjb2-40593', 'activeForm': 'Locating Spatial experiment result files on bjb2-40593', 'status': 'in_progress'}, {'content': 'Extract per-task SR for VLA-only and Adaptive', 'activeForm': 'Extracting per-task SR for VLA-only and Adaptive', 'status': 'pending'}, {'content': 'Identify always-0% tasks and compute Δ + p-value', 'activeForm': 'Identifying always-0% tasks and computing Δ + p-value', 'status': 'pending'}, {'content': 'Mechanism analysis: trigger_rate vs Δ correlation', 'activeForm': 'Analyzing mechanism: trigger_rate vs Δ correlation', 'status': 'pending'}, {'content': 'Output formatted breakdown table', 'activeForm': 'Outputting formatted breakdown table', 'status': 'pending'}]"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-24T22:27:00.466785+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-24T22:27:00.466916+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement/results/ -name \"*spatial*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "find /root/acr-vla-conformal-refinement/results/ -name \"*spatial*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-24T22:27:00.467041+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "ls /root/acr-vla-conformal-refinement/results/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "ls /root/acr-vla-conformal-refinement/results/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-24T22:27:00.467167+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"find: '/root/acr-vla-conformal-refinement/results/': No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 1.02}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-24T22:27:00.467328+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/acr-vla-conformal-refinement/results/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-24T22:27:00.467488+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "ls /root/acr-vla-conformal-refinement/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "ls /root/acr-vla-conformal-refinement/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-24T22:27:00.467635+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"artifacts\\nbenchmark_batched.py\\nbenchmark_output.log\\ndiag_padding.py\\ndiag_pi05.py\\ndiversity_analysis.py\\nlogs\\nmvp\\noutputs\\nscripts\\nsmoke_test.py\\nsrc\\ntests\\nverify2_output.log\\nverify_batched.py\\nverify_output.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-24T22:27:00.467758+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "ls /root/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "ls /root/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-24T22:27:00.467879+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"acr-vla-conformal-refinement\\nautodl-pub\\nautodl-tmp\\nminiconda3\\noft_stubs\\nopenvla-oft-code\\nprecompute_pi05_shard0.log\\nprecompute_pi05_shard0_resume.log\\nruns\\ntf-logs\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-24T22:27:00.468040+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement/outputs -name \"*spatial*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "find /root/acr-vla-conformal-refinement/outputs -name \"*spatial*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-24T22:27:00.468163+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-24T22:27:00.468343+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "ls /root/acr-vla-conformal-refinement/outputs/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "ls /root/acr-vla-conformal-refinement/outputs/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-24T22:27:00.468499+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"eval\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-24T22:27:00.468617+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "ls /root/acr-vla-conformal-refinement/artifacts/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "ls /root/acr-vla-conformal-refinement/artifacts/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-24T22:27:00.468735+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"fig2_norm_sweep_v3.pdf\\nfig2_norm_sweep_v3.png\\nfig2_norm_sweep_v3.py\\nfig2_norm_sweep_v4.pdf\\nfig2_norm_sweep_v4.png\\nfig2_norm_sweep_v4.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-24T22:27:00.468861+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "ls /root/acr-vla-conformal-refinement/outputs/eval/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "ls /root/acr-vla-conformal-refinement/outputs/eval/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-24T22:27:00.468978+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-21\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-24T22:27:00.469089+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "ls /root/acr-vla-conformal-refinement/logs/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "ls /root/acr-vla-conformal-refinement/logs/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-24T22:27:00.469229+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"calibrate_crm_signal.log\\ncrm_spatial_train.log\\ndiversity_openvla_oft_K2.json\\neval-adaptive-k5-spatial-s42.log\\neval-k2-tau010-spatial-s42.log\\neval-k2-tau015-spatial-s42.log\\neval-object-v5-full.log\\neval-random-selection-object-seed43.log\\neval-random-selection-object-seed48.log\\neval-supp-k2mean-goal-s42.log\\neval_adaptive_k_p25_seed44.json\\neval_adaptive_k_spatial_p50_seed42.json\\neval_adaptive_k_spatial_p50_seed42.log\\neval_goal_vla_only_seed42.json\\neval_long_vla_only_seed42_r4.json\\neval_mag_obsonly_norm003.json\\neval_object_crm_obs_only_norm0.05_seed45.json\\neval_object_obs_only.json\\neval_object_perdof_norm01_seed47.log\\neval_object_random_selection_seed42.json\\neval_object_random_selection_seed42.log\\neval_object_random_selection_seed46.log\\neval_object_scalar_seed45_r2.json\\neval_object_scalar_seed45_r2.log\\neval_object_vla_only_openvla_oft_seed42.json\\neval_object_vla_only_pi05_seed42.json\\neval_object_vla_only_seed44.json\\neval_object_vla_only_seed48.json\\neval_object_vla_only_seed48.log\\neval_obs_only_object_norm02_seed55.json\\neval_pi05_baseline_object_seed42_r2.json\\neval_random_selection_object_seed43.json\\neval_random_selection_object_seed48.json\\neval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\neval_spatial_crm_obs_only_norm0.05_seed47.json\\neval_spatial_k2mean_seed45.json\\neval_spatial_obs_only_norm02_seed43.log\\neval_spatial_obs_only_norm02_seed44.json\\neval_spatial_obs_only_norm02_seed44.log\\neval_spatial_obs_only_norm02_seed45.log\\neval_spatial_reconvla_seed47.json\\neval_spatial_vla_only_seed44.json\\nlatency_profiling_formal.log\\nobs_only_object_norm02_seed55.log\\npi05_action_queue_quicktest.json\\npi05_vision_fix_quicktest.json\\nprecompute.log\\nreconvla_object.log\\nreconvla_spatial.log\\nsentinels\\ntrain_crm.log\\ntrain_crm_v2.log\\nvla_only_spatial_K1.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"met
…[truncated 39 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-24T22:27:00.469555+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement/outputs/eval/2026-05-21 -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "find /root/acr-vla-conformal-refinement/outputs/eval/2026-05-21 -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-24T22:27:00.469771+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/outputs/eval/2026-05-21/14-32-14_libero_pi05/videos/libero_object_0/eval_episode_0.mp4\\n/root/acr-vla-conformal-refinement/outputs/eval/2026-05-21/14-32-14_libero_pi05/videos/libero_object_0/eval_episode_1.mp4\\n/root/acr-vla-conformal-refinement/outputs/eval/2026-05-21/14-32-14_libero_pi05/videos/libero_object_0/eval_episode_2.mp4\\n/root/acr-vla-conformal-refinement/outputs/eval/2026-05-21/14-32-14_libero_pi05/eval_info.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-24T22:27:00.469971+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "head -c 2000 /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "head -c 2000 /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-24T22:27:00.470221+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.79,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pi
…[truncated 524 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-24T22:27:00.470492+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Locate Spatial experiment result files on bjb2-40593', 'activeForm': 'Locating Spatial experiment result files on bjb2-40593', 'status': 'completed'}, {'content': 'Extract per-task SR for VLA-only and Adaptive (multi-seed)', 'activeForm': 'Extracting per-task SR for VLA-only and Adaptive', 'status': 'in_progress'}, {'content': 'Identify always-0% tasks and compute Δ + p-value', 'activeForm': 'Identifying always-0% tasks and computing Δ + p-value', 'status': 'pending'}, {'content': 'Mechanism analysis: trigger_rate vs Δ correlation', 'activeForm': 'Analyzing mechanism: trigger_rate vs Δ correlation', 'status': 'pending'}, {'content': 'Output formatted breakdown table', 'activeForm': 'Outputting formatted breakdown table', 'status': 'pending'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Locate Spatial experiment result files on bjb2-40593', 'activeForm': 'Locating Spatial experiment result files on bjb2-40593', 'status': 'completed'}, {'content': 'Extract per-task SR for VLA-only and Adaptive (multi-seed)', 'activeForm': 'Extracting per-task SR for VLA-only and Adaptive', 'status': 'in_progress'}, {'content': 'Identify always-0% tasks and compute Δ + p-value', 'activeForm': 'Identifying always-0% tasks and computing Δ + p-value', 'status': 'pending'}, {'content': 'Mechanism analysis: trigger_rate vs Δ correlation', 'activeForm': 'Analyzing mechanism: trigger_rate vs Δ correlation', 'status': 'pending'}, {'content': 'Output formatted breakdown table', 'activeForm': 'Outputting formatted breakdown table', 'status': 'pending'}]"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-24T22:27:00.470725+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-24T22:27:00.470898+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-24T22:27:00.471144+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.785,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_blac
…[truncated 275 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-24T22:27:00.471395+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*spatial*vla*\" -o -name \"*spatial*adaptive*\" -o -name \"*spatial*conformal*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*spatial*vla*\" -o -name \"*spatial*adaptive*\" -o -name \"*spatial*conformal*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-24T22:27:00.471556+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-24T22:27:00.471697+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/ -path '*/logs/*spatial*' -type f 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/ -path '*/logs/*spatial*' -type f 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-24T22:27:00.471823+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-24T22:27:00.471943+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/acr-vla-conformal-refinement/ -path '*/logs/*spatial*' -type f 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "find /root/acr-vla-conformal-refinement/ -path '*/logs/*spatial*' -type f 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-24T22:27:00.472063+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-24T22:27:00.472179+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "find /root/acr-vla-conformal-refinement/ -path '*/logs/*spatial*' -type f 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "find /root/acr-vla-conformal-refinement/ -path '*/logs/*spatial*' -type f 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-24T22:27:00.472363+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-24T22:27:00.472495+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/ -path '*spatial*' -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/ -path '*spatial*' -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-24T22:27:00.472671+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_norm02_seed45.log\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed43_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.log\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed50.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed51.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed54.json\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p50_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p75_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval-random-selection-spatial-seed42.log\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p25_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval-random-selection-spatial-seed44.log\\n/root/acr-vla-conformal-refinement/logs/eval_random_selection_spatial_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval-obs-only-spatial-norm02-seed50.log\\n/root/acr-vla-conformal-refinement/logs/eval_obs_only_spatial_norm02_seed50.json\\n/root/acr-vla-conformal
…[truncated 4976 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-24T22:27:00.472809+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/acr-vla-conformal-refinement/ -path '*spatial*' -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "find /root/acr-vla-conformal-refinement/ -path '*spatial*' -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-24T22:27:00.472928+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "find /root/acr-vla-conformal-refinement/ -path '*spatial*' -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "find /root/acr-vla-conformal-refinement/ -path '*spatial*' -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-24T22:27:00.473082+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_perdof_norm003.log\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_perdof_norm005.log\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_perdof_norm02.log\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_perdof_norm03.log\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obsonly_norm005.log\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obsonly_norm02.log\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_norm02_seed44.log\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed44.log\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed45.log\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed46_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed49.json\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p50_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval-adaptive-k-spatial-p75-seed44.log\\n/root/acr-vla-conformal-refinement/logs/eval-adaptive-k-spatial-p25-seed44.log\\n/root/acr-vla-conformal-refinement/logs/eval-adaptive-k-spatial-p90-seed42.log\\n/root/acr-vla-conformal-refinement/logs/eval-obs-only-spatial-norm02-seed42.log\\n/root/acr-vla-conformal-refinement/logs/eval-vla-only-spatial-seed48.log\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p90_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p75_seed44.json\\n/root/acr-vla-conformal-re
…[truncated 2706 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-24T22:27:00.473249+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/reconvla_spatial.log\\n/root/acr-vla-conformal-refinement/logs/crm_spatial_train.log\\n/root/acr-vla-conformal-refinement/logs/vla_only_spatial_K1.log\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed43.log\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.log\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed45.log\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p50_seed42.log\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p50_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_k2mean_spatial_seed43.log\\n/root/acr-vla-conformal-refinement/logs/eval_k2mean_spatial_seed44.log\\n/root/acr-vla-conformal-refinement/logs/eval-supp-reconvla-spatial-s43.log\\n/root/acr-vla-conformal-refinement/logs/eval-supp-reconvla-spatial-s44.log\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_k2mean_spatial_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed46.json\\n/root/acr-vla-conformal-refinement/logs
…[truncated 1266 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-24T22:27:00.473525+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "python3 -c \"\nimport json, os, glob\nlogs = '/root/acr-vla-conformal-refinement/logs/'\nfiles = sorted(glob.glob(logs + 'eval_spatial_vla_only_seed*.json') + glob.glob(logs + 'eval_vla_only_spatial_seed*.json'))\nfor f in files:\n    try:\n        d = json.load(open(f))\n        print(os.path.basename(f), d.get('mode'), d.get('benchmark'), d.get('n_rollouts'), d.get('overall_success_rate'))\n    except Exception as e:\n        print(os.path.basename(f), 'ERR', e)\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "python3 -c \"\nimport json, os, glob\nlogs = '/root/acr-vla-conformal-refinement/logs/'\nfiles = sorted(glob.glob(logs + 'eval_spatial_vla_only_seed*.json') + glob.glob(logs + 'eval_vla_only_spatial_seed*.json'))\nfor f in files:\n    try:\n        d = json.load(open(f))\n        print(os.path.basename(f), d.get('mode'), d.get('benchmark'), d.get('n_rollouts'), d.get('overall_success_rate'))\n    except Exception as e:\n        print(os.path.basename(f), 'ERR', e)\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-24T22:27:00.473797+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: python expression contains disallowed call 'open('. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-24T22:27:00.473985+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "python3 -c \"\nimport json, os, glob\nlogs = '/root/acr-vla-conformal-refinement/logs/'\nfiles = sorted(glob.glob(logs + 'eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed*.json'))\nfor f in files:\n    try:\n        d = json.load(open(f))\n        print(os.path.basename(f), d.get('mode'), d.get('benchmark'), d.get('n_rollouts'), d.get('overall_success_rate'), d.get('adaptive_stats',{}).get('trigger_rate'))\n    except Exception as e:\n        print(os.path.basename(f), 'ERR', e)\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "python3 -c \"\nimport json, os, glob\nlogs = '/root/acr-vla-conformal-refinement/logs/'\nfiles = sorted(glob.glob(logs + 'eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed*.json'))\nfor f in files:\n    try:\n        d = json.load(open(f))\n        print(os.path.basename(f), d.get('mode'), d.get('benchmark'), d.get('n_rollouts'), d.get('overall_success_rate'), d.get('adaptive_stats',{}).get('trigger_rate'))\n    except Exception as e:\n        print(os.path.basename(f), 'ERR', e)\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-24T22:27:00.474130+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: python expression contains disallowed call 'open('. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-24T22:27:00.474296+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "python3 << 'PYEOF'\nimport json, os, glob\nlogs = '/root/acr-vla-conformal-refinement/logs/'\n\nprint(\"=== VLA-only spatial ===\")\nfiles = sorted(glob.glob(logs + 'eval_spatial_vla_only_seed*.json') + glob.glob(logs + 'eval_vla_only_spatial_seed*.json'))\nfor f in files:\n    try:\n        with open(f) as fp:\n            d = json.load(fp)\n        print(os.path.basename(f), d.get('mode'), d.get('benchmark'), d.get('n_rollouts'), d.get('overall_success_rate'))\n    except Exception as e:\n        print(os.path.basename(f), 'ERR', e)\n\nprint()\nprint(\"=== Adaptive Conformal CRM norm0.2 tau0.25 spatial ===\")\nfiles = sorted(glob.glob(logs + 'eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed*.json'))\nfor f in files:\n    try:\n        with open(f) as fp:\n            d = json.load(fp)\n        print(os.path.basename(f), d.get('mode'), d.get('benchmark'), d.get('n_rollouts'), d.get('overall_success_rate'), d.get('adaptive_stats',{}).get('trigger_rate'))\n    except Exception as e:\n        print(os.path.basename(f), 'ERR', e)\nPYEOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "python3 << 'PYEOF'\nimport json, os, glob\nlogs = '/root/acr-vla-conformal-refinement/logs/'\n\nprint(\"=== VLA-only spatial ===\")\nfiles = sorted(glob.glob(logs + 'eval_spatial_vla_only_seed*.json') + glob.glob(logs + 'eval_vla_only_spatial_seed*.json'))\nfor f in files:\n    try:\n        with open(f) as fp:\n            d = json.load(fp)\n        print(os.path.basename(f), d.get('mode'), d.get('benchmark'), d.get('n_rollouts'), d.get('overall_success_rate'))\n    except Exception as e:\n        print(os.path.basename(f), 'ERR', e)\n\nprint()\nprint(\"=== Adaptive Conformal CRM norm0.2 tau0.25 spatial ===\")\nfiles = sorted(glob.glob(logs + 'eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed*.json'))\nfor f in files:\n    try:\n        with open(f) as fp:\n            d = json.load(fp)\n        print(os.path.basename(f), d.get('mode'), d.get('benchmark'), d.get('n_rollouts'), d.get('overall_success_rate'), d.get('adaptive_stats',{}).get('trigger_rate'))\n    except Exception as e:\n        print(os.path.basename(f), 'ERR', e)\nPYEOF",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-24T22:27:00.474468+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== VLA-only spatial ===\\neval_spatial_vla_only_seed42.json vla_only spatial 10 0.3\\neval_spatial_vla_only_seed45.json vla_only spatial 10 0.27\\neval_spatial_vla_only_seed46.json vla_only spatial 10 0.3\\neval_spatial_vla_only_seed47.json vla_only spatial 10 0.3\\neval_spatial_vla_only_seed48.json vla_only spatial 10 0.3\\neval_spatial_vla_only_seed49.json vla_only spatial 10 0.29\\neval_spatial_vla_only_seed51.json vla_only spatial 10 0.33\\neval_spatial_vla_only_seed54.json vla_only spatial 10 0.27\\neval_vla_only_spatial_seed50.json vla_only spatial 10 0.3\\n\\n=== Adaptive Conformal CRM norm0.2 tau0.25 spatial ===\\neval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json adaptive_conformal_crm spatial 20 0.795 0.19649737302977233\\neval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json adaptive_conformal_crm spatial 20 0.8 0.1944700134532323\\neval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json adaptive_conformal_crm spatial 20 0.805 0.19977406714442053\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-24T22:27:00.474611+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "python3 << 'PYEOF'\nimport json, os, glob\nlogs = '/root/acr-vla-conformal-refinement/logs/'\nprint(\"=== VLA-only spatial ===\")\nfiles = sorted(glob.glob(logs + 'eval_spatial_vla_only_seed*.json') + glob.glob(logs + 'eval_vla_only_spatial_seed*.json'))\nfor f in files:\n    try:\n        with open(f) as fp:\n            d = json.load(fp)\n        print(os.path.basename(f), d.get('mode'), d.get('benchmark'), d.get('n_rollouts'), d.get('overall_success_rate'))\n    except Exception as e:\n        print(os.path.basename(f), 'ERR', e)\nprint()\nprint(\"=== Adaptive Conformal CRM norm0.2 tau0.25 spatial ===\")\nfiles = sorted(glob.glob(logs + 'eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed*.json'))\nfor f in files:\n    try:\n        with open(f) as fp:\n            d = json.load(fp)\n        print(os.path.basename(f), d.get('mode'), d.get('benchmark'), d.get('n_rollouts'), d.get('overall_success_rate'), d.get('adaptive_stats',{}).get('trigger_rate'))\n    except Exception as e:\n        print(os.path.basename(f), 'ERR', e)\nPYEOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "python3 << 'PYEOF'\nimport json, os, glob\nlogs = '/root/acr-vla-conformal-refinement/logs/'\nprint(\"=== VLA-only spatial ===\")\nfiles = sorted(glob.glob(logs + 'eval_spatial_vla_only_seed*.json') + glob.glob(logs + 'eval_vla_only_spatial_seed*.json'))\nfor f in files:\n    try:\n        with open(f) as fp:\n            d = json.load(fp)\n        print(os.path.basename(f), d.get('mode'), d.get('benchmark'), d.get('n_rollouts'), d.get('overall_success_rate'))\n    except Exception as e:\n        print(os.path.basename(f), 'ERR', e)\nprint()\nprint(\"=== Adaptive Conformal CRM norm0.2 tau0.25 spatial ===\")\nfiles = sorted(glob.glob(logs + 'eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed*.json'))\nfor f in files:\n    try:\n        with open(f) as fp:\n            d = json.load(fp)\n        print(os.path.basename(f), d.get('mode'), d.get('benchmark'), d.get('n_rollouts'), d.get('overall_success_rate'), d.get('adaptive_stats',{}).get('trigger_rate'))\n    except Exception as e:\n        print(os.path.basename(f), 'ERR', e)\nPYEOF",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-24T22:27:00.474752+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== VLA-only spatial ===\\neval_spatial_vla_only_seed42.json vla_only spatial 20 0.815\\neval_spatial_vla_only_seed43.json vla_only spatial 20 0.805\\neval_spatial_vla_only_seed44.json vla_only spatial 20 0.805\\neval_spatial_vla_only_seed45.json vla_only spatial 20 0.8\\neval_spatial_vla_only_seed46.json vla_only spatial 20 0.805\\n\\n=== Adaptive Conformal CRM norm0.2 tau0.25 spatial ===\\neval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json adaptive_conformal_crm spatial 20 0.8 0.2013357110388475\\neval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed48.json adaptive_conformal_crm spatial 20 0.81 0.19767112621221775\\neval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed49.json adaptive_conformal_crm spatial 20 0.82 0.19522981006234594\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-24T22:27:00.474879+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-32758",
  "command": "python3 << 'PYEOF'\nimport json, os, glob\nlogs = '/root/acr-vla-conformal-refinement/logs/'\nprint(\"=== VLA-only spatial ===\")\nfiles = sorted(glob.glob(logs + 'eval_spatial_vla_only_seed*.json') + glob.glob(logs + 'eval_vla_only_spatial_seed*.json'))\nfor f in files:\n    try:\n        with open(f) as fp:\n            d = json.load(fp)\n        print(os.path.basename(f), d.get('mode'), d.get('benchmark'), d.get('n_rollouts'), d.get('overall_success_rate'))\n    except Exception as e:\n        print(os.path.basename(f), 'ERR', e)\nprint()\nprint(\"=== Adaptive Conformal CRM norm0.2 tau0.25 spatial ===\")\nfiles = sorted(glob.glob(logs + 'eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed*.json'))\nfor f in files:\n    try:\n        with open(f) as fp:\n            d = json.load(fp)\n        print(os.path.basename(f), d.get('mode'), d.get('benchmark'), d.get('n_rollouts'), d.get('overall_success_rate'), d.get('adaptive_stats',{}).get('trigger_rate'))\n    except Exception as e:\n        print(os.path.basename(f), 'ERR', e)\nPYEOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "python3 << 'PYEOF'\nimport json, os, glob\nlogs = '/root/acr-vla-conformal-refinement/logs/'\nprint(\"=== VLA-only spatial ===\")\nfiles = sorted(glob.glob(logs + 'eval_spatial_vla_only_seed*.json') + glob.glob(logs + 'eval_vla_only_spatial_seed*.json'))\nfor f in files:\n    try:\n        with open(f) as fp:\n            d = json.load(fp)\n        print(os.path.basename(f), d.get('mode'), d.get('benchmark'), d.get('n_rollouts'), d.get('overall_success_rate'))\n    except Exception as e:\n        print(os.path.basename(f), 'ERR', e)\nprint()\nprint(\"=== Adaptive Conformal CRM norm0.2 tau0.25 spatial ===\")\nfiles = sorted(glob.glob(logs + 'eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed*.json'))\nfor f in files:\n    try:\n        with open(f) as fp:\n            d = json.load(fp)\n        print(os.path.basename(f), d.get('mode'), d.get('benchmark'), d.get('n_rollouts'), d.get('overall_success_rate'), d.get('adaptive_stats',{}).get('trigger_rate'))\n    except Exception as e:\n        print(os.path.basename(f), 'ERR', e)\nPYEOF",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-24T22:27:00.475034+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'python3 << \\\\'PYEOF\\\\'\\\\nimport json, os, glob\\\\nlogs = \\\\'/root/acr-vla-conformal-refinement/logs/\\\\'\\\\nprint(\\\"=== VLA-only spatial ===\\\")\\\\nfiles = sorted(glob.glob(logs + \\\\'eval_spatial_vla_only_seed*.json\\\\') + glob.glob(logs + \\\\'eval_vla_only_spatial_seed*.json\\\\'))\\\\nfor f in files:\\\\n    try:\\\\n        with open(f) as fp:\\\\n            d = json.load(fp)\\\\n        print(os.path.basename(f), d.get(\\\\'mode\\\\'), d.get(\\\\'benchmark\\\\'), d.get(\\\\'n_rollouts\\\\'), d.get(\\\\'overall_success_rate\\\\'))\\\\n    except Exception as e:\\\\n        print(os.path.basename(f), \\\\'ERR\\\\', e)\\\\nprint()\\\\nprint(\\\"=== Adaptive Conformal CRM norm0.2 tau0.25 spatial ===\\\")\\\\nfiles = sorted(glob.glob(logs + \\\\'eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed*.json\\\\'))\\\\nfor f in files:\\\\n    try:\\\\n        with open(f) as fp:\\\\n            d = json.load(fp)\\\\n        print(os.path.basename(f), d.get(\\\\'mode\\\\'), d.get(\\\\'benchmark\\\\'), d.get(\\\\'n_rollouts\\\\'), d.get(\\\\'overall_success_rate\\\\'), d.get(\\\\'adaptive_stats\\\\',{}).get(\\\\'trigger_rate\\\\'))\\\\n    except Exception as e:\\\\n        print(os.path.basename(f), \\\\'ERR\\\\', e)\\\\nPYEOF'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-24T22:27:00.475185+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-32758",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 << 'PYEOF'\nimport json, os, glob\nlogs = '/root/acr-vla-conformal-refinement/logs/'\nprint(\"=== VLA-only spatial ===\")\nfiles = sorted(glob.glob(logs + 'eval_spatial_vla_only_seed*.json') + glob.glob(logs + 'eval_vla_only_spatial_seed*.json'))\nfor f in files:\n    try:\n        with open(f) as fp:\n            d = json.load(fp)\n        print(os.path.basename(f), d.get('mode'), d.get('benchmark'), d.get('n_rollouts'), d.get('overall_success_rate'))\n    except Exception as e:\n        print(os.path.basename(f), 'ERR', e)\nprint()\nprint(\"=== Adaptive Conformal CRM norm0.2 tau0.25 spatial ===\")\nfiles = sorted(glob.glob(logs + 'eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed*.json'))\nfor f in files:\n    try:\n        with open(f) as fp:\n            d = json.load(fp)\n        print(os.path.basename(f), d.get('mode'), d.get('benchmark'), d.get('n_rollouts'), d.get('overall_success_rate'), d.get('adaptive_stats',{}).get('trigger_rate'))\n    except Exception as e:\n        print(os.path.basename(f), 'ERR', e)\nPYEOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 << 'PYEOF'\nimport json, os, glob\nlogs = '/root/acr-vla-conformal-refinement/logs/'\nprint(\"=== VLA-only spatial ===\")\nfiles = sorted(glob.glob(logs + 'eval_spatial_vla_only_seed*.json') + glob.glob(logs + 'eval_vla_only_spatial_seed*.json'))\nfor f in files:\n    try:\n        with open(f) as fp:\n            d = json.load(fp)\n        print(os.path.basename(f), d.get('mode'), d.get('benchmark'), d.get('n_rollouts'), d.get('overall_success_rate'))\n    except Exception as e:\n        print(os.path.basename(f), 'ERR', e)\nprint()\nprint(\"=== Adaptive Conformal CRM norm0.2 tau0.25 spatial ===\")\nfiles = sorted(glob.glob(logs + 'eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed*.json'))\nfor f in files:\n    try:\n        with open(f) as fp:\n            d = json.load(fp)\n        print(os.path.basename(f), d.get('mode'), d.get('benchmark'), d.get('n_rollouts'), d.get('overall_success_rate'), d.get('adaptive_stats',{}).get('trigger_rate'))\n    except Exception as e:\n        print(os.path.basename(f), 'ERR', e)\nPYEOF",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-24T22:27:00.475387+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== VLA-only spatial ===\\neval_spatial_vla_only_seed43.json vla_only spatial 20 0.79\\neval_spatial_vla_only_seed44.json vla_only spatial 20 0.81\\neval_spatial_vla_only_seed45.json vla_only spatial 20 0.77\\neval_spatial_vla_only_seed46.json vla_only spatial 20 0.805\\neval_spatial_vla_only_seed47.json vla_only spatial 20 0.81\\neval_spatial_vla_only_seed48.json vla_only spatial 20 0.795\\neval_spatial_vla_only_seed49.json vla_only spatial 20 0.785\\n\\n=== Adaptive Conformal CRM norm0.2 tau0.25 spatial ===\\neval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json adaptive_conformal_crm spatial 20 0.8 0.19954975553132365\\neval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json adaptive_conformal_crm spatial 20 0.8 0.19917476746625637\\neval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json adaptive_conformal_crm spatial 20 0.815 0.204562439944482\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.01}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-24T22:27:00.475561+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "python3 << 'PYEOF'\nimport json, glob, os\nfrom collections import defaultdict\n\nlogs = '/root/acr-vla-conformal-refinement/logs/'\nprint(\"# bjb2-28827 VLA-only (n=20)\")\nfor f in sorted(glob.glob(logs + 'eval_spatial_vla_only_seed*.json')):\n    with open(f) as fp: d = json.load(fp)\n    if d.get('n_rollouts')!=20: continue\n    print(f)\n    for t,v in d['per_task'].items():\n        print(' ', t[:60], v['success_rate'], v['successes'], v['total'])\n\nprint()\nprint(\"# bjb2-28827 Adaptive Conformal CRM norm0.2 tau0.25 (n=20)\")\nfor f in sorted(glob.glob(logs + 'eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed*.json')):\n    with open(f) as fp: d = json.load(fp)\n    if d.get('n_rollouts')!=20: continue\n    print(f)\n    for t,v in d['per_task'].items():\n        print(' ', t[:60], v['success_rate'], v['successes'], v['total'])\nPYEOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "python3 << 'PYEOF'\nimport json, glob, os\nfrom collections import defaultdict\n\nlogs = '/root/acr-vla-conformal-refinement/logs/'\nprint(\"# bjb2-28827 VLA-only (n=20)\")\nfor f in sorted(glob.glob(logs + 'eval_spatial_vla_only_seed*.json')):\n    with open(f) as fp: d = json.load(fp)\n    if d.get('n_rollouts')!=20: continue\n    print(f)\n    for t,v in d['per_task'].items():\n        print(' ', t[:60], v['success_rate'], v['successes'], v['total'])\n\nprint()\nprint(\"# bjb2-28827 Adaptive Conformal CRM norm0.2 tau0.25 (n=20)\")\nfor f in sorted(glob.glob(logs + 'eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed*.json')):\n    with open(f) as fp: d = json.load(fp)\n    if d.get('n_rollouts')!=20: continue\n    print(f)\n    for t,v in d['per_task'].items():\n        print(' ', t[:60], v['success_rate'], v['successes'], v['total'])\nPYEOF",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-24T22:27:00.475741+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# bjb2-28827 VLA-only (n=20)\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and 0.95 19 20\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_t 0.95 19 20\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the 1.0 20 20\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the 1.0 20 20\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabin 0.7 14 20\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_pl 0.0 0 20\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_o 0.95 19 20\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plat 0.8 16 20\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the 0.85 17 20\\n  pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on 0.95 19 20\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and 1.0 20 20\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_t 0.95 19 20\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the 0.95 19 20\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the 0.9 18 20\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabin 0.75 15 20\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_pl 0.0 0 20\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_o 0.95 19 20\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plat 0.8 16 20\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the 0.85 17 20\\n  pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on 0.9 18 20\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and 0.9 18 20\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_t 0.95 19 20\\n  pick_up_the_black_bowl_f
…[truncated 4977 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-24T22:27:00.475896+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-32758",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 << 'PYEOF'\nimport json, glob, os\nlogs = '/root/acr-vla-conformal-refinement/logs/'\nprint(\"# cqa1-32758 VLA-only (n=20)\")\nfor f in sorted(glob.glob(logs + 'eval_spatial_vla_only_seed*.json')):\n    with open(f) as fp: d = json.load(fp)\n    if d.get('n_rollouts')!=20: continue\n    print(f)\n    for t,v in d['per_task'].items():\n        print(' ', t[:60], v['success_rate'], v['successes'], v['total'])\nprint()\nprint(\"# cqa1-32758 Adaptive Conformal CRM norm0.2 tau0.25 (n=20)\")\nfor f in sorted(glob.glob(logs + 'eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed*.json')):\n    with open(f) as fp: d = json.load(fp)\n    if d.get('n_rollouts')!=20: continue\n    print(f)\n    for t,v in d['per_task'].items():\n        print(' ', t[:60], v['success_rate'], v['successes'], v['total'])\nPYEOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 << 'PYEOF'\nimport json, glob, os\nlogs = '/root/acr-vla-conformal-refinement/logs/'\nprint(\"# cqa1-32758 VLA-only (n=20)\")\nfor f in sorted(glob.glob(logs + 'eval_spatial_vla_only_seed*.json')):\n    with open(f) as fp: d = json.load(fp)\n    if d.get('n_rollouts')!=20: continue\n    print(f)\n    for t,v in d['per_task'].items():\n        print(' ', t[:60], v['success_rate'], v['successes'], v['total'])\nprint()\nprint(\"# cqa1-32758 Adaptive Conformal CRM norm0.2 tau0.25 (n=20)\")\nfor f in sorted(glob.glob(logs + 'eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed*.json')):\n    with open(f) as fp: d = json.load(fp)\n    if d.get('n_rollouts')!=20: continue\n    print(f)\n    for t,v in d['per_task'].items():\n        print(' ', t[:60], v['success_rate'], v['successes'], v['total'])\nPYEOF",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-24T22:27:00.476110+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# cqa1-32758 VLA-only (n=20)\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and 0.85 17 20\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_t 1.0 20 20\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the 0.95 19 20\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the 0.9 18 20\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabin 0.65 13 20\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_pl 0.0 0 20\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_o 0.95 19 20\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plat 0.9 18 20\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the 0.85 17 20\\n  pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on 0.85 17 20\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and 1.0 20 20\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_t 0.95 19 20\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the 0.95 19 20\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the 1.0 20 20\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabin 0.75 15 20\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_pl 0.0 0 20\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_o 1.0 20 20\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plat 0.75 15 20\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the 0.8 16 20\\n  pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on 0.9 18 20\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and 0.9 18 20\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_t 0.9 18 20\\n  pick_up_the_black_bowl_fr
…[truncated 6420 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-24T22:27:00.476329+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "python3 << 'PYEOF'\nimport json, glob, os\nlogs = '/root/acr-vla-conformal-refinement/logs/'\nprint(\"# bjb1-32546 Adaptive Conformal CRM norm0.2 tau0.25 (n=20)\")\nfor f in sorted(glob.glob(logs + 'eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed*.json')):\n    with open(f) as fp: d = json.load(fp)\n    if d.get('n_rollouts')!=20: continue\n    print(f)\n    for t,v in d['per_task'].items():\n        print(' ', t[:60], v['success_rate'], v['successes'], v['total'])\nPYEOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "python3 << 'PYEOF'\nimport json, glob, os\nlogs = '/root/acr-vla-conformal-refinement/logs/'\nprint(\"# bjb1-32546 Adaptive Conformal CRM norm0.2 tau0.25 (n=20)\")\nfor f in sorted(glob.glob(logs + 'eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed*.json')):\n    with open(f) as fp: d = json.load(fp)\n    if d.get('n_rollouts')!=20: continue\n    print(f)\n    for t,v in d['per_task'].items():\n        print(' ', t[:60], v['success_rate'], v['successes'], v['total'])\nPYEOF",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-24T22:27:00.476524+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# bjb1-32546 Adaptive Conformal CRM norm0.2 tau0.25 (n=20)\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and 0.95 19 20\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_t 0.95 19 20\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the 1.0 20 20\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the 1.0 20 20\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabin 0.65 13 20\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_pl 0.0 0 20\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_o 1.0 20 20\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plat 0.8 16 20\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the 0.8 16 20\\n  pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on 0.8 16 20\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and 0.95 19 20\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_t 0.95 19 20\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the 0.95 19 20\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the 1.0 20 20\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabin 0.7 14 20\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_pl 0.0 0 20\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_o 1.0 20 20\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plat 0.8 16 20\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the 0.85 17 20\\n  pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on 0.8 16 20\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_a
…[truncated 795 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-24T22:27:00.476694+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-32758",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 << 'PYEOF'\nimport json, glob, os\nlogs = '/root/acr-vla-conformal-refinement/logs/'\nfor f in ['eval_spatial_vla_only_seed47.json', 'eval_spatial_vla_only_seed48.json']:\n    with open(logs+f) as fp: d = json.load(fp)\n    print(f, 'n=', d.get('n_rollouts'), 'overall=', d.get('overall_success_rate'))\n    for t,v in d['per_task'].items():\n        print(' ', t[:65], v['success_rate'], v['successes'], v['total'])\n    print()\nPYEOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 << 'PYEOF'\nimport json, glob, os\nlogs = '/root/acr-vla-conformal-refinement/logs/'\nfor f in ['eval_spatial_vla_only_seed47.json', 'eval_spatial_vla_only_seed48.json']:\n    with open(logs+f) as fp: d = json.load(fp)\n    print(f, 'n=', d.get('n_rollouts'), 'overall=', d.get('overall_success_rate'))\n    for t,v in d['per_task'].items():\n        print(' ', t[:65], v['success_rate'], v['successes'], v['total'])\n    print()\nPYEOF",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-24T22:27:00.476848+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"eval_spatial_vla_only_seed47.json n= 20 overall= 0.81\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_plac 0.95 19 20\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_pl 0.95 19 20\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plat 1.0 20 20\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plat 1.0 20 20\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_an 0.7 14 20\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate 0.0 0 20\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the 1.0 20 20\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate 0.9 18 20\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plat 0.7 14 20\\n  pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_ 0.9 18 20\\n\\neval_spatial_vla_only_seed48.json n= 20 overall= 0.795\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_plac 1.0 20 20\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_pl 0.9 18 20\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plat 0.95 19 20\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plat 0.95 19 20\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_an 0.8 16 20\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate 0.0 0 20\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the 0.95 19 20\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate 0.75 15 20\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plat 0.85 17 20\\n  pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_ 0.8 16 20\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.59}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-24T22:27:00.476997+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "python3 << 'PYEOF'\nimport json\nwith open('/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json') as fp:\n    d = json.load(fp)\nprint('Top-level keys:', list(d.keys()))\nprint('per_task entry keys:', list(next(iter(d['per_task'].values())).keys()))\nprint('adaptive_stats:', d.get('adaptive_stats'))\nPYEOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "python3 << 'PYEOF'\nimport json\nwith open('/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json') as fp:\n    d = json.load(fp)\nprint('Top-level keys:', list(d.keys()))\nprint('per_task entry keys:', list(next(iter(d['per_task'].values())).keys()))\nprint('adaptive_stats:', d.get('adaptive_stats'))\nPYEOF",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-24T22:27:00.477125+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Top-level keys: ['mode', 'baseline_mode', 'benchmark', 'n_rollouts', 'overall_success_rate', 'per_task', 'adaptive_stats']\\nper_task entry keys: ['success_rate', 'successes', 'total']\\nadaptive_stats: {'mean_uncertainty': 0.1857245399690708, 'trigger_rate': 0.19649737302977233, 'tau': 0.25, 'total_steps': 28550, 'crm_applied_steps': 5610}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-24T22:27:00.477246+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/outputs -name \"*.json\" -path \"*adaptive*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/outputs -name \"*.json\" -path \"*adaptive*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-24T22:27:00.477431+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"find: '/root/acr-vla-conformal-refinement/outputs': No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-24T22:27:00.477586+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Locate Spatial experiment result files on bjb2-40593', 'activeForm': 'Locating Spatial experiment result files on bjb2-40593', 'status': 'completed'}, {'content': 'Extract per-task SR for VLA-only and Adaptive (multi-seed)', 'activeForm': 'Extracting per-task SR for VLA-only and Adaptive', 'status': 'completed'}, {'content': 'Check per-task trigger_rate availability in eval_info or logs', 'activeForm': 'Checking per-task trigger_rate availability', 'status': 'in_progress'}, {'content': 'Identify always-0% tasks and compute Δ + p-value', 'activeForm': 'Identifying always-0% tasks and computing Δ + p-value', 'status': 'pending'}, {'content': 'Mechanism analysis: trigger_rate vs Δ correlation', 'activeForm': 'Analyzing mechanism: trigger_rate vs Δ correlation', 'status': 'pending'}, {'content': 'Output formatted breakdown table', 'activeForm': 'Outputting formatted breakdown table', 'status': 'pending'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Locate Spatial experiment result files on bjb2-40593', 'activeForm': 'Locating Spatial experiment result files on bjb2-40593', 'status': 'completed'}, {'content': 'Extract per-task SR for VLA-only and Adaptive (multi-seed)', 'activeForm': 'Extracting per-task SR for VLA-only and Adaptive', 'status': 'completed'}, {'content': 'Check per-task trigger_rate availability in eval_info or logs', 'activeForm': 'Checking per-task trigger_rate availability', 'status': 'in_progress'}, {'content': 'Identify always-0% tasks and compute Δ + p-value', 'activeForm': 'Identifying always-0% tasks and computing Δ + p-value', 'status': 'pending'}, {'content': 'Mechanism analysis: trigger_rate vs Δ correlation', 'activeForm': 'Analyzing mechanism: trigger_rate vs Δ correlation', 'status': 'pending'}, {'content': 'Output formatted breakdown table', 'activeForm': 'Outputting formatted breakdown table', 'status': 'pending'}]"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-24T22:27:00.477751+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-24T22:27:00.477874+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root -name \"eval_info.json\" -path \"*spatial*\" -not -path \"*/.*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root -name \"eval_info.json\" -path \"*spatial*\" -not -path \"*/.*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-24T22:27:00.477997+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/outputs/eval/smolvla_spatial_seed44/eval_info.json\\n/root/outputs/eval/smolvla_spatial_seed43_v3/eval_info.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.67}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-24T22:27:00.478113+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -200 /root/acr-vla-conformal-refinement/logs/adapt_tau025_spatial_s42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tail -200 /root/acr-vla-conformal-refinement/logs/adapt_tau025_spatial_s42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-24T22:27:00.478296+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'spatial', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'n_rollouts': 20, 'max_steps': 300, 'seed': 42, 'K': 10, 'mode': 'adaptive_conformal_crm', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'smolvla', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_spatial_adaptive_conformal_crm_tau0.25_seed42.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.25, 'n_action_steps': 10}\\n[eval] Mode: adaptive_conformal_crm, benchmark: spatial\\n[eval] max_steps set to 280 for benchmark spatial\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  56%|█████▌    | 273/489 [00:00<00:00, 2582.75it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 3158.93it/s]\\nReducing the number of VLM layers to 16 ...\\nLoading weights from local directory\\n[eval] CRM loaded from /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt (327,198 params)\\n[eval] Override max_correction_norm = 0.2\\n[eval] Loading LIBERO spatial environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 5/20, success so far: 5/5\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 10/20, success so far: 10/10\\n  pick_up_t
…[truncated 2454 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-24T22:27:00.478473+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -E \"trigger|task_name|^\\[pick_up|adaptive|crm_applied|per-task\" /root/acr-vla-conformal-refinement/logs/adapt_tau025_spatial_s42.log | head -100",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "grep -E \"trigger|task_name|^\\[pick_up|adaptive|crm_applied|per-task\" /root/acr-vla-conformal-refinement/logs/adapt_tau025_spatial_s42.log | head -100",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-24T22:27:00.478614+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'spatial', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'n_rollouts': 20, 'max_steps': 300, 'seed': 42, 'K': 10, 'mode': 'adaptive_conformal_crm', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'smolvla', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_spatial_adaptive_conformal_crm_tau0.25_seed42.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.25, 'n_action_steps': 10}\\n[eval] Mode: adaptive_conformal_crm, benchmark: spatial\\n[pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\n[pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\n[pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n[pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-24T22:27:00.478768+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Locate Spatial experiment result files on bjb2-40593', 'activeForm': 'Locating Spatial experiment result files on bjb2-40593', 'status': 'completed'}, {'content': 'Extract per-task SR for VLA-only and Adaptive (multi-seed)', 'activeForm': 'Extracting per-task SR for VLA-only and Adaptive', 'status': 'completed'}, {'content': 'Check per-task trigger_rate availability in eval_info or logs', 'activeForm': 'Checking per-task trigger_rate availability', 'status': 'completed'}, {'content': 'Identify always-0% tasks and compute Δ + p-value', 'activeForm': 'Identifying always-0% tasks and computing Δ + p-value', 'status': 'in_progress'}, {'content': 'Mechanism analysis: trigger_rate vs Δ correlation', 'activeForm': 'Analyzing mechanism: trigger_rate vs Δ correlation', 'status': 'pending'}, {'content': 'Output formatted breakdown table', 'activeForm': 'Outputting formatted breakdown table', 'status': 'pending'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Locate Spatial experiment result files on bjb2-40593', 'activeForm': 'Locating Spatial experiment result files on bjb2-40593', 'status': 'completed'}, {'content': 'Extract per-task SR for VLA-only and Adaptive (multi-seed)', 'activeForm': 'Extracting per-task SR for VLA-only and Adaptive', 'status': 'completed'}, {'content': 'Check per-task trigger_rate availability in eval_info or logs', 'activeForm': 'Checking per-task trigger_rate availability', 'status': 'completed'}, {'content': 'Identify always-0% tasks and compute Δ + p-value', 'activeForm': 'Identifying always-0% tasks and computing Δ + p-value', 'status': 'in_progress'}, {'content': 'Mechanism analysis: trigger_rate vs Δ correlation', 'activeForm': 'Analyzing mechanism: trigger_rate vs Δ correlation', 'status': 'pending'}, {'content': 'Output formatted breakdown table', 'activeForm': 'Outputting formatted breakdown table', 'status': 'pending'}]"
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-24T22:27:00.478933+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-24T22:27:00.479064+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "python3 << 'PYEOF'\n# Aggregate per-task SR across seeds (n=20) for VLA-only and Adaptive Conformal CRM\n# VLA-only available on bjb2-28827 (seeds 42-46). Adaptive available on bjb2-28827 (45,48,49).\n# Plus we need data from cqa1 (seeds 47-49 vla, 46-47 adaptive) and bjb1 (42-44 adaptive).\n# This script aggregates only what is on this server; we'll merge with manual data from others.\n\nimport json, glob, os, numpy as np\nlogs = '/root/acr-vla-conformal-refinement/logs/'\n\nTASKS = [\n    'pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate',\n]\n\ndef load_files(pat):\n    out = {}\n    for f in sorted(glob.glob(logs + pat)):\n        with open(f) as fp:\n            d = json.load(fp)\n        if d.get('n_rollouts') != 20: continue\n        seed = int(f.split('seed')[-1].split('.')[0])\n        out[seed] = {t: d['per_task'][t]['success_rate'] for t in TASKS}\n    return out\n\nvla = load_files('eval_spatial_vla_only_seed*.json')\nadp = load_files('eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed*.json')\nprint('bjb2-28827 VLA-only seeds:', sorted(vla.keys()))\nprint('bjb2-28827 Adaptive seeds:', sorted(adp.keys()))\nimport json as J\nprint('VLA_DATA=' + J.dumps(vla))\nprint('ADP_DATA=' + J.dumps(adp))\nPYEOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "python3 << 'PYEOF'\n# Aggregate per-task SR across seeds (n=20) for VLA-only and Adaptive Conformal CRM\n# VLA-only available on bjb2-28827 (seeds 42-46). Adaptive available on bjb2-28827 (45,48,49).\n# Plus we need data from cqa1 (seeds 47-49 vla, 46-47 adaptive) and bjb1 (42-44 adaptive).\n# This script aggregates only what is on this server; we'll merge with manual data from others.\n\nimport json, glob, os, numpy as np\nlogs = '/root/acr-vla-conformal-refinement/logs/'\n\nTASKS = [\n    'pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate',\n]\n\ndef load_files(pat):\n    out = {}\n    for f in sorted(glob.glob(logs + pat)):\n        with open(f) as fp:\n            d = json.load(fp)\n        if d.get('n_rollouts') != 20: continue\n        seed = int(f.split('seed')[-1].split('.')[0])\n        out[seed] = {t: d['per_task'][t]['success_rate'] for t in TASKS}\n    return out\n\nvla = load_files('eval_spatial_vla_only_seed*.json')\nadp = load_files('eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed*.json')\nprint('bjb2-28827 VLA-only seeds:', sorted(vla.keys()))\nprint('bjb2-28827 Adaptive seeds:', sorted(adp.keys()))\nimport json as J\nprint('VLA_DATA=' + J.dumps(vla))\nprint('ADP_DATA=' + J.dumps(adp))\nPYEOF",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-24T22:27:00.479286+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"bjb2-28827 VLA-only seeds: [42, 43, 44, 45, 46]\\nbjb2-28827 Adaptive seeds: [45, 48, 49]\\nVLA_DATA={\\\"42\\\": {\\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": 0.95, \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": 0.95, \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": 1.0, \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": 1.0, \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": 0.7, \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": 0.0, \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": 0.95, \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": 0.8, \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": 0.85, \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\": 0.95}, \\\"43\\\": {\\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": 1.0, \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": 0.95, \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": 0.95, \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": 0.9, \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": 0.75, \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": 0.0, \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": 0.95, \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": 0.8, \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": 0.85, \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\": 0.9}, \\\"44\\\": {\\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\
…[truncated 5228 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-24T22:27:00.479509+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "python3 << 'PYEOF'\nimport json, glob\nlogs = '/root/acr-vla-conformal-refinement/logs/'\nTASKS = [\n    'pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate',\n]\ndef load(pat):\n    out={}\n    for f in sorted(glob.glob(logs+pat)):\n        with open(f) as fp: d=json.load(fp)\n        if d.get('n_rollouts')!=20: continue\n        seed=int(f.split('seed')[-1].split('.')[0])\n        out[seed]={t:d['per_task'][t]['success_rate'] for t in TASKS}\n    return out\nadp = load('eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed*.json')\nprint('bjb1-32546 Adaptive seeds:', sorted(adp.keys()))\nprint('ADP_DATA=' + json.dumps(adp))\nPYEOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "python3 << 'PYEOF'\nimport json, glob\nlogs = '/root/acr-vla-conformal-refinement/logs/'\nTASKS = [\n    'pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate',\n]\ndef load(pat):\n    out={}\n    for f in sorted(glob.glob(logs+pat)):\n        with open(f) as fp: d=json.load(fp)\n        if d.get('n_rollouts')!=20: continue\n        seed=int(f.split('seed')[-1].split('.')[0])\n        out[seed]={t:d['per_task'][t]['success_rate'] for t in TASKS}\n    return out\nadp = load('eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed*.json')\nprint('bjb1-32546 Adaptive seeds:', sorted(adp.keys()))\nprint('ADP_DATA=' + json.dumps(adp))\nPYEOF",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-24T22:27:00.479779+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"bjb1-32546 Adaptive seeds: [42, 43, 44]\\nADP_DATA={\\\"42\\\": {\\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": 0.95, \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": 0.95, \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": 1.0, \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": 1.0, \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": 0.65, \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": 0.0, \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": 1.0, \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": 0.8, \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": 0.8, \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\": 0.8}, \\\"43\\\": {\\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": 0.95, \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": 0.95, \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": 0.95, \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": 1.0, \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": 0.7, \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": 0.0, \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": 1.0, \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": 0.8, \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": 0.85, \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\": 0.8}, \\\"44\\\": {\\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": 0.9, \\\"pick_up_the_black_bowl_next_to_the_rameki
…[truncated 818 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-24T22:27:00.480002+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-32758",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 << 'PYEOF'\nimport json, glob\nlogs = '/root/acr-vla-conformal-refinement/logs/'\nTASKS = [\n    'pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate',\n]\ndef load(pat):\n    out={}\n    for f in sorted(glob.glob(logs+pat)):\n        with open(f) as fp: d=json.load(fp)\n        if d.get('n_rollouts')!=20: continue\n        seed=int(f.split('seed')[-1].split('.')[0])\n        out[seed]={t:d['per_task'][t]['success_rate'] for t in TASKS}\n    return out\nvla = load('eval_spatial_vla_only_seed*.json')\nadp = load('eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed*.json')\nprint('cqa1-32758 VLA-only seeds:', sorted(vla.keys()))\nprint('cqa1-32758 Adaptive seeds:', sorted(adp.keys()))\nprint('VLA_DATA=' + json.dumps(vla))\nprint('ADP_DATA=' + json.dumps(adp))\nPYEOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 << 'PYEOF'\nimport json, glob\nlogs = '/root/acr-vla-conformal-refinement/logs/'\nTASKS = [\n    'pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate',\n    'pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate',\n]\ndef load(pat):\n    out={}\n    for f in sorted(glob.glob(logs+pat)):\n        with open(f) as fp: d=json.load(fp)\n        if d.get('n_rollouts')!=20: continue\n        seed=int(f.split('seed')[-1].split('.')[0])\n        out[seed]={t:d['per_task'][t]['success_rate'] for t in TASKS}\n    return out\nvla = load('eval_spatial_vla_only_seed*.json')\nadp = load('eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed*.json')\nprint('cqa1-32758 VLA-only seeds:', sorted(vla.keys()))\nprint('cqa1-32758 Adaptive seeds:', sorted(adp.keys()))\nprint('VLA_DATA=' + json.dumps(vla))\nprint('ADP_DATA=' + json.dumps(adp))\nPYEOF",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-24T22:27:00.480386+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"cqa1-32758 VLA-only seeds: [43, 44, 45, 46, 47, 48, 49]\\ncqa1-32758 Adaptive seeds: [45, 46, 47]\\nVLA_DATA={\\\"43\\\": {\\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": 0.85, \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": 1.0, \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": 0.95, \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": 0.9, \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": 0.65, \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": 0.0, \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": 0.95, \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": 0.9, \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": 0.85, \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\": 0.85}, \\\"44\\\": {\\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": 1.0, \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": 0.95, \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": 0.95, \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": 1.0, \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": 0.75, \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": 0.0, \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": 1.0, \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": 0.75, \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": 0.8, \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\": 0.9}, \\\"45\\\": {\\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_
…[truncated 6850 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-24T22:27:00.480700+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "python3 << 'PYEOF'\nimport json, numpy as np\nfrom scipy import stats\n\nTASKS = [\n 'between_plate_and_ramekin',\n 'next_to_ramekin',\n 'from_table_center',\n 'on_cookie_box',\n 'in_top_drawer',\n 'on_ramekin',\n 'next_to_cookie_box',\n 'on_stove',\n 'next_to_plate',\n 'on_wooden_cabinet',\n]\n\n# VLA-only runs (each row = 10 task SRs, in TASKS order). n=20 rollouts each.\nVLA = {\n ('bjb2-28827','42'): [0.95, 0.95, 1.0, 1.0, 0.7, 0.0, 0.95, 0.8, 0.85, 0.95],\n ('bjb2-28827','43'): [1.0, 0.95, 0.95, 0.9, 0.75, 0.0, 0.95, 0.8, 0.85, 0.9],\n ('bjb2-28827','44'): [0.9, 0.95, 1.0, 0.95, 0.8, 0.0, 1.0, 0.85, 0.7, 0.9],\n ('bjb2-28827','45'): [0.95, 0.95, 1.0, 1.0, 0.7, 0.0, 1.0, 0.75, 0.8, 0.85],\n ('bjb2-28827','46'): [0.95, 0.95, 1.0, 1.0, 0.75, 0.0, 0.95, 0.8, 0.8, 0.85],\n ('cqa1','43'):       [0.85, 1.0, 0.95, 0.9, 0.65, 0.0, 0.95, 0.9, 0.85, 0.85],\n ('cqa1','44'):       [1.0, 0.95, 0.95, 1.0, 0.75, 0.0, 1.0, 0.75, 0.8, 0.9],\n ('cqa1','45'):       [0.9, 0.9, 0.9, 1.0, 0.75, 0.0, 0.95, 0.75, 0.8, 0.75],\n ('cqa1','46'):       [0.95, 1.0, 1.0, 1.0, 0.7, 0.0, 1.0, 0.75, 0.8, 0.85],\n ('cqa1','47'):       [0.95, 0.95, 1.0, 1.0, 0.7, 0.0, 1.0, 0.9, 0.7, 0.9],\n ('cqa1','48'):       [1.0, 0.9, 0.95, 0.95, 0.8, 0.0, 0.95, 0.75, 0.85, 0.8],\n ('cqa1','49'):       [0.9, 0.95, 0.95, 0.95, 0.7, 0.0, 0.9, 0.8, 0.75, 0.95],\n}\n\n# Adaptive Conformal CRM (norm0.2, tau0.25, n=20).\nADP = {\n ('bjb1','42'):       [0.95, 0.95, 1.0, 1.0, 0.65, 0.0, 1.0, 0.8, 0.8, 0.8],\n ('bjb1','43'):       [0.95, 0.95, 0.95, 1.0, 0.7, 0.0, 1.0, 0.8, 0.85, 0.8],\n ('bjb1','44'):       [0.9, 0.95, 1.0, 1.0, 0.65, 0.0, 1.0, 0.8, 0.8, 0.95],\n ('bjb2-28827','45'): [0.95, 0.95, 1.0, 1.0, 0.75, 0.0, 1.0, 0.75, 0.8, 0.8],\n ('bjb2-28827','48'): [1.0, 1.0, 1.0, 0.95, 0.65, 0.0, 0.95, 0.85, 0.8, 0.9],\n ('bjb2-28827','49'): [0.95, 1.0, 1.0, 1.0, 0.7, 0.0, 1.0, 0.8, 0.9, 0.85],\n ('cqa1','45'):       [0.95, 0.95, 1.0, 1.0, 0.75, 0.0, 0.95, 0.8, 0.8, 0.8],\n ('cqa1','46'):       [1.0, 0.9, 0.95, 1.0, 0.65, 0.0, 1.0, 0.9, 0.75, 0.85],\n ('cqa1','47'):       [1.0, 1.0, 1.0, 0.95, 0.8, 0.0, 0.9, 0.85, 0.8, 0.85],\n}\n\nV = np.array(list(VLA.values()))  # (n_runs_v, 10)\nA = np.array(list(ADP.values()))  # (n_runs_a, 10)\nprint(f\"VLA-only runs: {V.shape[0]}, Adaptive runs: {A.shape[0]}\")\n\n# Per-task mean & SE across runs (independent runs, not seed-paired)\nvm = V.mean(0); vs = V.std(0, ddof=1)/np.sqrt(V.shape[0])\nam = A.mean(0); as_ = A.std(0, ddof=1)/np.sqrt(A.shape[0])\ndelta = am - vm\n\nprint()\nprint(f\"{'task':<28} {'VLA-only':>14} {'Adaptive':>14} {'Δ(pp)':>8}\")\nfor i,t in enumerate(TASKS):\n    flag = '  always-0%' if vm[i]==0 and am[i]==0 else ''\n    print(f\"{t:<28} {vm[i]*100:>7.2f}±{vs[i]*100:<5.2f} {am[i]*100:>7.2f}±{as_[i]*100:<5.2f} {delta[i]*100:>+7.2f}{flag}\")\n\n# Overall\nv_overall = V.mean(1)  # mean SR per run\na_overall = A.mean(1)\nprint()\nprint(f\"All 10 tasks:\")\nprint(f\"  VLA-only mean: {v_overall.mean()*100:.2f}% (sd={v_overall.std(ddof=1)*100:.2f}, n={len(v_overall)})\")\nprint(f\"  Adaptive mean: {a_overall.mean()*100:.2f}% (sd={a_overall.std(ddof=1)*100:.2f}, n={len(a_overall)})\")\nprint(f\"  Δ = {(a_overall.mean()-v_overall.mean())*100:+.2f}pp\")\n\n# Paired t-test on per-task means\nt,p = stats.ttest_rel(am, vm)\nprint(f\"  Paired t-test (per-task, 10 paired): t={t:.3f}, p={p:.4f}\")\n\n# Welch's t-test on overall (run-level, unpaired)\nt2,p2 = stats.ttest_ind(a_overall, v_overall, equal_var=False)\nprint(f\"  Welch t-test (run-level overall): t={t2:.3f}, p={p2:.4f}\")\n\n# Excluding always-0% tasks (on_ramekin)\nmask = ~((vm==0) & (am==0))\nprint()\nprint(f\"Excluding always-0% task(s) ({sum(~mask)} dropped): {[TASKS[i] for i in range(10) if not mask[i]]}\")\nV9 = V[:, mask]\nA9 = A[:, mask]\nvm9 = V9.mean(0); am9 = A9.mean(0)\nv_o9 = V9.mean(1); a_o9 = A9.mean(1)\nprint(f\"  VLA-only mean: {v_o9.mean()*100:.2f}% (sd={v_o9.std(ddof=1)*100:.2f})\")\nprint(f\"  Adaptive mean: {a_o9.mean()*100:.2f}% (sd={a_o9.std(ddof=1)*100:.2f})\")\nprint(f\"  Δ = {(a_o9.mean()-v_o9.mean())*100:+.2f}pp\")\nt,p = stats.ttest_rel(am9, vm9)\nprint(f\"  Paired t-test (per-task, 9 paired): t={t:.3f}, p={p:.4f}\")\nt2,p2 = stats.ttest_ind(a_o9, v_o9, equal_var=False)\nprint(f\"  Welch t-test (run-level overall, 9-task): t={t2:.3f}, p={p2:.4f}\")\n\n# Mechanism: trigger_rate is global ~19.6% across all seeds. No per-task trigger_rate available.\nprint()\nprint(\"Note: per-task trigger_rate NOT logged in eval JSONs; global trigger_rate ≈ 19.6% across all seeds.\")\nPYEOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "python3 << 'PYEOF'\nimport json, numpy as np\nfrom scipy import stats\n\nTASKS = [\n 'between_plate_and_ramekin',\n 'next_to_ramekin',\n 'from_table_center',\n 'on_cookie_box',\n 'in_top_drawer',\n 'on_ramekin',\n 'next_to_cookie_box',\n 'on_stove',\n 'next_to_plate',\n 'on_wooden_cabinet',\n]\n\n# VLA-only runs (each row = 10 task SRs, in TASKS order). n=20 rollouts each.\nVLA = {\n ('bjb2-28827','42'): [0.95, 0.95, 1.0, 1.0, 0.7, 0.0, 0.95, 0.8, 0.85, 0.95],\n ('bjb2-28827','43'): [1.0, 0.95, 0.95, 0.9, 0.75, 0.0, 0.95, 0.8, 0.85, 0.9],\n ('bjb2-28827','44'): [0.9, 0.95, 1.0, 0.95, 0.8, 0.0, 1.0, 0.85, 0.7, 0.9],\n ('bjb2-28827','45'): [0.95, 0.95, 1.0, 1.0, 0.7, 0.0, 1.0, 0.75, 0.8, 0.85],\n ('bjb2-28827','46'): [0.95, 0.95, 1.0, 1.0, 0.75, 0.0, 0.95, 0.8, 0.8, 0.85],\n ('cqa1','43'):       [0.85, 1.0, 0.95, 0.9, 0.65, 0.0, 0.95, 0.9, 0.85, 0.85],\n ('cqa1','44'):       [1.0, 0.95, 0.95, 1.0, 0.75, 0.0, 1.0, 0.75, 0.8, 0.9],\n ('cqa1','45'):       [0.9, 0.9, 0.9, 1.0, 0.75, 0.0, 0.95, 0.75, 0.8, 0.75],\n ('cqa1','46'):       [0.95, 1.0, 1.0, 1.0, 0.7, 0.0, 1.0, 0.75, 0.8, 0.85],\n ('cqa1','47'):       [0.95, 0.95, 1.0, 1.0, 0.7, 0.0, 1.0, 0.9, 0.7, 0.9],\n ('cqa1','48'):       [1.0, 0.9, 0.95, 0.95, 0.8, 0.0, 0.95, 0.75, 0.85, 0.8],\n ('cqa1','49'):       [0.9, 0.95, 0.95, 0.95, 0.7, 0.0, 0.9, 0.8, 0.75, 0.95],\n}\n\n# Adaptive Conformal CRM (norm0.2, tau0.25, n=20).\nADP = {\n ('bjb1','42'):       [0.95, 0.95, 1.0, 1.0, 0.65, 0.0, 1.0, 0.8, 0.8, 0.8],\n ('bjb1','43'):       [0.95, 0.95, 0.95, 1.0, 0.7, 0.0, 1.0, 0.8, 0.85, 0.8],\n ('bjb1','44'):       [0.9, 0.95, 1.0, 1.0, 0.65, 0.0, 1.0, 0.8, 0.8, 0.95],\n ('bjb2-28827','45'): [0.95, 0.95, 1.0, 1.0, 0.75, 0.0, 1.0, 0.75, 0.8, 0.8],\n ('bjb2-28827','48'): [1.0, 1.0, 1.0, 0.95, 0.65, 0.0, 0.95, 0.85, 0.8, 0.9],\n ('bjb2-28827','49'): [0.95, 1.0, 1.0, 1.0, 0.7, 0.0, 1.0, 0.8, 0.9, 0.85],\n ('cqa1','45'):       [0.95, 0.95, 1.0, 1.0, 0.75, 0.0, 0.95, 0.8, 0.8, 0.8],\n ('cqa1','46'):       [1.0, 0.9, 0.95, 1.0, 0.65, 0.0, 1.0, 0.9, 0.75, 0.85],\n ('cqa1','47'):       [1.0, 1.0, 1.0, 0.95, 0.8, 0.0, 0.9, 0.85, 0.8, 0.85],\n}\n\nV = np.array(list(VLA.values()))  # (n_runs_v, 10)\nA = np.array(list(ADP.values()))  # (n_runs_a, 10)\nprint(f\"VLA-only runs: {V.shape[0]}, Adaptive runs: {A.shape[0]}\")\n\n# Per-task mean & SE across runs (independent runs, not seed-paired)\nvm = V.mean(0); vs = V.std(0, ddof=1)/np.sqrt(V.shape[0])\nam = A.mean(0); as_ = A.std(0, ddof=1)/np.sqrt(A.shape[0])\ndelta = am - vm\n\nprint()\nprint(f\"{'task':<28} {'VLA-only':>14} {'Adaptive':>14} {'Δ(pp)':>8}\")\nfor i,t in enumerate(TASKS):\n    flag = '  always-0%' if vm[i]==0 and am[i]==0 else ''\n    print(f\"{t:<28} {vm[i]*100:>7.2f}±{vs[i]*100:<5.2f} {am[i]*100:>7.2f}±{as_[i]*100:<5.2f} {delta[i]*100:>+7.2f}{flag}\")\n\n# Overall\nv_overall = V.mean(1)  # mean SR per run\na_overall = A.mean(1)\nprint()\nprint(f\"All 10 tasks:\")\nprint(f\"  VLA-only mean: {v_overall.mean()*100:.2f}% (sd={v_overall.std(ddof=1)*100:.2f}, n={len(v_overall)})\")\nprint(f\"  Adaptive mean: {a_overall.mean()*100:.2f}% (sd={a_overall.std(ddof=1)*100:.2f}, n={len(a_overall)})\")\nprint(f\"  Δ = {(a_overall.mean()-v_overall.mean())*100:+.2f}pp\")\n\n# Paired t-test on per-task means\nt,p = stats.ttest_rel(am, vm)\nprint(f\"  Paired t-test (per-task, 10 paired): t={t:.3f}, p={p:.4f}\")\n\n# Welch's t-test on overall (run-level, unpaired)\nt2,p2 = stats.ttest_ind(a_overall, v_overall, equal_var=False)\nprint(f\"  Welch t-test (run-level overall): t={t2:.3f}, p={p2:.4f}\")\n\n# Excluding always-0% tasks (on_ramekin)\nmask = ~((vm==0) & (am==0))\nprint()\nprint(f\"Excluding always-0% task(s) ({sum(~mask)} dropped): {[TASKS[i] for i in range(10) if not mask[i]]}\")\nV9 = V[:, mask]\nA9 = A[:, mask]\nvm9 = V9.mean(0); am9 = A9.mean(0)\nv_o9 = V9.mean(1); a_o9 = A9.mean(1)\nprint(f\"  VLA-only mean: {v_o9.mean()*100:.2f}% (sd={v_o9.std(ddof=1)*100:.2f})\")\nprint(f\"  Adaptive mean: {a_o9.mean()*100:.2f}% (sd={a_o9.std(ddof=1)*100:.2f})\")\nprint(f\"  Δ = {(a_o9.mean()-v_o9.mean())*100:+.2f}pp\")\nt,p = stats.ttest_rel(am9, vm9)\nprint(f\"  Paired t-test (per-task, 9 paired): t={t:.3f}, p={p:.4f}\")\nt2,p2 = stats.ttest_ind(a_o9, v_o9, equal_var=False)\nprint(f\"  Welch t-test (run-level overall, 9-task): t={t2:.3f}, p={p2:.4f}\")\n\n# Mechanism: trigger_rate is global ~19.6% across all seeds. No per-task trigger_rate available.\nprint()\nprint(\"Note: per-task trigger_rate NOT logged in eval JSONs; global trigger_rate ≈ 19.6% across all seeds.\")\nPYEOF",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-24T22:27:00.481037+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"VLA-only runs: 12, Adaptive runs: 9\\n\\ntask                               VLA-only       Adaptive    Δ(pp)\\nbetween_plate_and_ramekin      94.17±1.35    96.11±1.11    +1.94\\nnext_to_ramekin                95.00±0.87    96.11±1.11    +1.11\\nfrom_table_center              97.08±0.96    98.89±0.73    +1.81\\non_cookie_box                  97.08±1.14    98.89±0.73    +1.81\\nin_top_drawer                  72.92±1.30    70.00±1.86    -2.92\\non_ramekin                      0.00±0.00     0.00±0.00    +0.00  always-0%\\nnext_to_cookie_box             96.67±0.94    97.78±1.21    +1.11\\non_stove                       80.00±1.63    81.67±1.44    +1.67\\nnext_to_plate                  79.58±1.56    81.11±1.39    +1.53\\non_wooden_cabinet              87.08±1.68    84.44±1.76    -2.64\\n\\nAll 10 tasks:\\n  VLA-only mean: 79.96% (sd=1.27, n=12)\\n  Adaptive mean: 80.50% (sd=0.83, n=9)\\n  Δ = +0.54pp\\n  Paired t-test (per-task, 10 paired): t=0.932, p=0.3758\\n  Welch t-test (run-level overall): t=1.180, p=0.2527\\n\\nExcluding always-0% task(s) (1 dropped): ['on_ramekin']\\n  VLA-only mean: 88.84% (sd=1.41)\\n  Adaptive mean: 89.44% (sd=0.92)\\n  Δ = +0.60pp\\n  Paired t-test (per-task, 9 paired): t=0.931, p=0.3791\\n  Welch t-test (run-level overall, 9-task): t=1.180, p=0.2527\\n\\nNote: per-task trigger_rate NOT logged in eval JSONs; global trigger_rate ≈ 19.6% across all seeds.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.14}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-24T22:27:00.481382+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "python3 << 'PYEOF'\nimport numpy as np\nfrom scipy import stats\n\nTASKS = [\n 'between_plate_and_ramekin','next_to_ramekin','from_table_center','on_cookie_box',\n 'in_top_drawer','on_ramekin','next_to_cookie_box','on_stove','next_to_plate','on_wooden_cabinet',\n]\nvm = np.array([0.9417,0.95,0.9708,0.9708,0.7292,0.0,0.9667,0.80,0.7958,0.8708])\nam = np.array([0.9611,0.9611,0.9889,0.9889,0.70,0.0,0.9778,0.8167,0.8111,0.8444])\ndelta = am - vm\n\n# Correlation between Δ and (1 - VLA SR) [headroom]: do gains concentrate on tasks with headroom?\nmask9 = vm > 0   # exclude on_ramekin\nheadroom = 1.0 - vm\nr_head, p_head = stats.pearsonr(delta[mask9], headroom[mask9])\nprint(f\"Pearson r(Δ, headroom=1-VLA_SR), n=9: r={r_head:.3f}, p={p_head:.4f}\")\n\n# Spearman as well\nrs, ps = stats.spearmanr(delta[mask9], headroom[mask9])\nprint(f\"Spearman r(Δ, headroom), n=9: r={rs:.3f}, p={ps:.4f}\")\n\n# Correlation: Δ vs VLA SR (negative = gain on hard tasks)\nr2, p2 = stats.pearsonr(delta[mask9], vm[mask9])\nprint(f\"Pearson r(Δ, VLA_SR), n=9: r={r2:.3f}, p={p2:.4f}\")\n\n# Trigger rates across seeds (global; per-seed values from earlier print)\ntrigger_rates = [0.1965, 0.1945, 0.1998, 0.2013, 0.1977, 0.1952, 0.1995, 0.1992, 0.2046]\nprint(f\"\\nGlobal trigger_rate across {len(trigger_rates)} adaptive seeds: \"\n      f\"mean={np.mean(trigger_rates)*100:.2f}%, sd={np.std(trigger_rates,ddof=1)*100:.2f}%, \"\n      f\"min={min(trigger_rates)*100:.2f}%, max={max(trigger_rates)*100:.2f}%\")\nPYEOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "python3 << 'PYEOF'\nimport numpy as np\nfrom scipy import stats\n\nTASKS = [\n 'between_plate_and_ramekin','next_to_ramekin','from_table_center','on_cookie_box',\n 'in_top_drawer','on_ramekin','next_to_cookie_box','on_stove','next_to_plate','on_wooden_cabinet',\n]\nvm = np.array([0.9417,0.95,0.9708,0.9708,0.7292,0.0,0.9667,0.80,0.7958,0.8708])\nam = np.array([0.9611,0.9611,0.9889,0.9889,0.70,0.0,0.9778,0.8167,0.8111,0.8444])\ndelta = am - vm\n\n# Correlation between Δ and (1 - VLA SR) [headroom]: do gains concentrate on tasks with headroom?\nmask9 = vm > 0   # exclude on_ramekin\nheadroom = 1.0 - vm\nr_head, p_head = stats.pearsonr(delta[mask9], headroom[mask9])\nprint(f\"Pearson r(Δ, headroom=1-VLA_SR), n=9: r={r_head:.3f}, p={p_head:.4f}\")\n\n# Spearman as well\nrs, ps = stats.spearmanr(delta[mask9], headroom[mask9])\nprint(f\"Spearman r(Δ, headroom), n=9: r={rs:.3f}, p={ps:.4f}\")\n\n# Correlation: Δ vs VLA SR (negative = gain on hard tasks)\nr2, p2 = stats.pearsonr(delta[mask9], vm[mask9])\nprint(f\"Pearson r(Δ, VLA_SR), n=9: r={r2:.3f}, p={p2:.4f}\")\n\n# Trigger rates across seeds (global; per-seed values from earlier print)\ntrigger_rates = [0.1965, 0.1945, 0.1998, 0.2013, 0.1977, 0.1952, 0.1995, 0.1992, 0.2046]\nprint(f\"\\nGlobal trigger_rate across {len(trigger_rates)} adaptive seeds: \"\n      f\"mean={np.mean(trigger_rates)*100:.2f}%, sd={np.std(trigger_rates,ddof=1)*100:.2f}%, \"\n      f\"min={min(trigger_rates)*100:.2f}%, max={max(trigger_rates)*100:.2f}%\")\nPYEOF",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-24T22:27:00.481648+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Pearson r(Δ, headroom=1-VLA_SR), n=9: r=-0.542, p=0.1313\\nSpearman r(Δ, headroom), n=9: r=-0.506, p=0.1643\\nPearson r(Δ, VLA_SR), n=9: r=0.542, p=0.1313\\n\\nGlobal trigger_rate across 9 adaptive seeds: mean=19.87%, sd=0.32%, min=19.45%, max=20.46%\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-24T22:27:00.481884+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Locate Spatial experiment result files on bjb2-40593', 'activeForm': 'Locating Spatial experiment result files on bjb2-40593', 'status': 'completed'}, {'content': 'Extract per-task SR for VLA-only and Adaptive (multi-seed)', 'activeForm': 'Extracting per-task SR for VLA-only and Adaptive', 'status': 'completed'}, {'content': 'Check per-task trigger_rate availability in eval_info or logs', 'activeForm': 'Checking per-task trigger_rate availability', 'status': 'completed'}, {'content': 'Identify always-0% tasks and compute Δ + p-value', 'activeForm': 'Identifying always-0% tasks and computing Δ + p-value', 'status': 'completed'}, {'content': 'Mechanism analysis: trigger_rate vs Δ correlation', 'activeForm': 'Analyzing mechanism: trigger_rate vs Δ correlation', 'status': 'completed'}, {'content': 'Output formatted breakdown table', 'activeForm': 'Outputting formatted breakdown table', 'status': 'in_progress'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Locate Spatial experiment result files on bjb2-40593', 'activeForm': 'Locating Spatial experiment result files on bjb2-40593', 'status': 'completed'}, {'content': 'Extract per-task SR for VLA-only and Adaptive (multi-seed)', 'activeForm': 'Extracting per-task SR for VLA-only and Adaptive', 'status': 'completed'}, {'content': 'Check per-task trigger_rate availability in eval_info or logs', 'activeForm': 'Checking per-task trigger_rate availability', 'status': 'completed'}, {'content': 'Identify always-0% tasks and compute Δ + p-value', 'activeForm': 'Identifying always-0% tasks and computing Δ + p-value', 'status': 'completed'}, {'content': 'Mechanism analysis: trigger_rate vs Δ correlation', 'activeForm': 'Analyzing mechanism: trigger_rate vs Δ correlation', 'status': 'completed'}, {'content': 'Output formatted breakdown table', 'activeForm': 'Outputting formatted breakdown table', 'status': 'in_progress'}]"
  }
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-24T22:27:00.482140+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 92 · 2026-05-24T22:27:00.482423+00:00_

## Spatial 10-task SR Breakdown（VLA-only vs Adaptive Conformal CRM, norm=0.2, τ=0.25）

**数据源**：bjb1-32546 / bjb2-28827 / cqa1-32758 上的 `logs/eval_spatial_*_seed*.json`，全部 n_rollouts=20。
- VLA-only: 12 个 run（seeds 42-49，多服务器，每个 run 独立测量）
- Adaptive: 9 个 run（seeds 42-49，bjb1 seeds 42-44 + bjb2-28827 seeds 45/48/49 + cqa1 seeds 45-47）
- bjb2-40593 上仅一份 spatial JSON（seed42 adaptive），已并入 bjb1 seed42 同源数据

### Per-task SR（mean±SE over runs）

```
task                      | VLA-only      | Adaptive       |   Δ(pp)  | 备注
between_plate_and_ramekin | 94.17 ± 1.35  | 96.11 ± 1.11   |   +1.94  |
next_to_ramekin           | 95.00 ± 0.87  | 96.11 ± 1.11   |   +1.11  |
from_table_center         | 97.08 ± 0.96  | 98.89 ± 0.73   |   +1.81  |
on_cookie_box             | 97.08 ± 1.14  | 98.89 ± 0.73   |   +1.81  |
in_top_drawer             | 72.92 ± 1.30  | 70.00 ± 1.86   |   -2.92  | ← adaptive 反退化
on_ramekin                |  0.00 ± 0.00  |  0.00 ± 0.00   |    0.00  | always-0%
next_to_cookie_box        | 96.67 ± 0.94  | 97.78 ± 1.21   |   +1.11  |
on_stove                  | 80.00 ± 1.63  | 81.67 ± 1.44   |   +1.67  |
next_to_plate             | 79.58 ± 1.56  | 81.11 ± 1.39   |   +1.53  |
on_wooden_cabinet         | 87.08 ± 1.68  | 84.44 ± 1.76   |   -2.64  | ← adaptive 反退化
```

### 聚合统计

```
全部 10 task:
  VLA-only mean: 79.96% (sd=1.27, n=12 runs)
  Adaptive mean: 80.50% (sd=0.83, n=9 runs)
  Δ = +0.54pp
  Paired t-test (per-task, 10 paired): t=0.932, p=0.3758
  Welch t-test (run-level overall):    t=1.180, p=0.2527

剔除 always-0% task (on_ramekin, 1 个):
  VLA-only mean: 88.84% (sd=1.41)
  Adaptive mean: 89.44% (sd=0.92)
  Δ = +0.60pp
  Paired t-test (per-task, 9 paired): t=0.931, p=0.3791
  Welch t-test (run-level overall):   t=1.180, p=0.2527
```

剔除 always-0% task **几乎不改变结论**——Δ 从 +0.54pp 升至 +0.60pp，p 值仍 ≈0.38，均不显著。

### Mechanism 分析

**per-task trigger_rate 在 eval JSON 中未记录**（只有全局 trigger_rate）。全局 trigger_rate 跨 9 个 adaptive seed 极其稳定：mean=19.87%, sd=0.32%, range [19.45%, 20.46%]。

替代 mechanism 指标：**Δ 与 task 难度（headroom = 1−VLA_SR）的相关性**（剔除 always-0%, n=9）：

```
Pearson  r(Δ, headroom) = -0.542  (p=0.1313)
Spearman r(Δ, headroom) = -0.506  (p=0.1643)
```

**反向相关**：Adaptive 的增益**集中在已经很容易的 task**（4 个 95%+ 的 task 各得 +1.1~+1.9pp），而**最难的两个非零 task（in_top_drawer 72.9%、on_wooden_cabinet 87.1%）反而退化 −2.6~−2.9pp**。不能支持 "conformal 在需要时激活" 的叙述——相反，增益分布与"修在容易处、改坏在难处"一致。p=0.13 不显著（n=9 power 低），但符号明确。

### Rebuttal 建议要点

1. Δ=+0.54pp（10-task）/ +0.60pp（剔除 always-0%），均**不显著**（p≈0.38）。剔除 always-0% 不能救回显著性。
2. on_ramekin 是任务本身极难（VLA-only 跨 12 seed 全部 0/20），与方法无关；adaptive 对它也无能为力。
3. 两个 task 的 SR 因 adaptive 而下降（in_top_drawer −2.92pp、on_wooden_cabinet −2.64pp），任何 "trigger_rate 与改进高度对齐" 的叙述需谨慎——目前数据反向。
4. 全局 trigger_rate≈19.87%（极稳定）说明 calibration 一致，但**触发并不等于改进**。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035"
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-24T22:37:42.142504+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,TodoWrite",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,TodoWrite",
    "max_results": "10"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-24T22:37:42.142797+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-24T22:37:42.142956+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Find Spatial result JSON files on servers', 'activeForm': 'Finding Spatial result JSON files', 'status': 'in_progress'}, {'content': 'Extract per-task SR for VLA-only and Adaptive', 'activeForm': 'Extracting per-task SR', 'status': 'pending'}, {'content': 'Identify always-0% tasks and compute filtered stats', 'activeForm': 'Computing filtered stats', 'status': 'pending'}, {'content': 'Mechanism analysis: trigger_rate vs Delta correlation', 'activeForm': 'Analyzing mechanism', 'status': 'pending'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Find Spatial result JSON files on servers', 'activeForm': 'Finding Spatial result JSON files', 'status': 'in_progress'}, {'content': 'Extract per-task SR for VLA-only and Adaptive', 'activeForm': 'Extracting per-task SR', 'status': 'pending'}, {'content': 'Identify always-0% tasks and compute filtered stats', 'activeForm': 'Computing filtered stats', 'status': 'pending'}, {'content': 'Mechanism analysis: trigger_rate vs Delta correlation', 'activeForm': 'Analyzing mechanism', 'status': 'pending'}]"
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-24T22:37:42.143098+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-24T22:37:42.143221+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement/results -name \"*spatial*\" -type f 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "find /root/acr-vla-conformal-refinement/results -name \"*spatial*\" -type f 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-24T22:37:42.143399+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-24T22:37:42.143553+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement/results -iname \"*spatial*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "find /root/acr-vla-conformal-refinement/results -iname \"*spatial*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-24T22:37:42.143738+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"find: '/root/acr-vla-conformal-refinement/results': No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.94}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-24T22:37:42.143902+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "ls /root/acr-vla-conformal-refinement/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "ls /root/acr-vla-conformal-refinement/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-24T22:37:42.144084+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"artifacts\\nbenchmark_batched.py\\nbenchmark_output.log\\ndiag_padding.py\\ndiag_pi05.py\\ndiversity_analysis.py\\nlogs\\nmvp\\noutputs\\nscripts\\nsmoke_test.py\\nsrc\\ntests\\nverify2_output.log\\nverify_batched.py\\nverify_output.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-24T22:37:42.144303+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement -iname \"*spatial*\" -type f -not -path \"*/node_modules/*\" -not -path \"*/.git/*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "find /root/acr-vla-conformal-refinement -iname \"*spatial*\" -type f -not -path \"*/node_modules/*\" -not -path \"*/.git/*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-24T22:37:42.144564+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/reconvla_spatial.log\\n/root/acr-vla-conformal-refinement/logs/crm_spatial_train.log\\n/root/acr-vla-conformal-refinement/logs/vla_only_spatial_K1.log\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed43.log\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.log\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed45.log\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p50_seed42.log\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p50_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_k2mean_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval-adaptive-k5-spatial-s42.log\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval-k2-tau010-spatial-s42.log\\n/root/acr-vla-conformal-refinement/logs/eval-k2-tau015-spatial-s42.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-24T22:37:42.144793+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "ls /root/acr-vla-conformal-refinement/logs/ | grep -iE \"spatial\" | sort",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "ls /root/acr-vla-conformal-refinement/logs/ | grep -iE \"spatial\" | sort",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-24T22:37:42.144982+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-24T22:37:42.145154+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement/logs -maxdepth 1 -iname \"*spatial*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "find /root/acr-vla-conformal-refinement/logs -maxdepth 1 -iname \"*spatial*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-24T22:37:42.145394+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/reconvla_spatial.log\\n/root/acr-vla-conformal-refinement/logs/crm_spatial_train.log\\n/root/acr-vla-conformal-refinement/logs/vla_only_spatial_K1.log\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed43.log\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.log\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed45.log\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p50_seed42.log\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p50_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_k2mean_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval-adaptive-k5-spatial-s42.log\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval-k2-tau010-spatial-s42.log\\n/root/acr-vla-conformal-refinement/logs/eval-k2-tau015-spatial-s42.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-24T22:37:42.145603+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement/logs -maxdepth 1 -iname \"eval*spatial*\" -type f -name \"*.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "find /root/acr-vla-conformal-refinement/logs -maxdepth 1 -iname \"eval*spatial*\" -type f -name \"*.json\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-24T22:37:42.145804+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p50_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_k2mean_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-24T22:37:42.146012+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "python3 -c \"import json; d=json.load(open('/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json')); print('keys=', list(d.keys())[:20])\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "python3 -c \"import json; d=json.load(open('/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json')); print('keys=', list(d.keys())[:20])\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-24T22:37:42.146192+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-24T22:37:42.146412+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "head -c 2000 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "head -c 2000 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-24T22:37:42.146653+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.785,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_blac
…[truncated 275 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 115 · 2026-05-24T22:37:42.146902+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "head -c 1500 /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "head -c 1500 /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-24T22:37:42.147139+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.79,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_r\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\
…[truncated 11 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 117 · 2026-05-24T22:37:42.147399+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement -maxdepth 3 -iname \"*spatial*\" -type f -name \"*.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement -maxdepth 3 -iname \"*spatial*\" -type f -name \"*.json\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-24T22:37:42.147639+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed43_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed50.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed51.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed54.json\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p50_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p75_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p25_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_random_selection_spatial_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_obs_only_spatial_norm02_seed50.json\\n/root/acr-vla-conformal-refinement/logs/eval_obs_only_spatial_norm02_seed52.json\\n/root/acr-vla-conformal-refinement/logs/eval_plan_a_spatial_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_plan_a_spatial_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_plan_a_spatial_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_vla_only_spatial_seed50.json\\n/root/acr-vla-conformal-refinement/log
…[truncated 1920 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-24T22:37:42.147839+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/acr-vla-conformal-refinement -maxdepth 3 -iname \"*spatial*\" -type f -name \"*.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "find /root/acr-vla-conformal-refinement -maxdepth 3 -iname \"*spatial*\" -type f -name \"*.json\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 120 · 2026-05-24T22:37:42.147995+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed46_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed49.json\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p50_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p90_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p75_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p25_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_obs_only_spatial_norm02_seed49.json\\n/root/acr-vla-conformal-refinement/logs/eval_obs_only_spatial_norm02_seed42_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p90_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed49.json\\n/root/acr
…[truncated 201 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 121 · 2026-05-24T22:37:42.148134+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "find /root/acr-vla-conformal-refinement -maxdepth 3 -iname \"*spatial*\" -type f -name \"*.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "find /root/acr-vla-conformal-refinement -maxdepth 3 -iname \"*spatial*\" -type f -name \"*.json\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 122 · 2026-05-24T22:37:42.148327+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p50_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_k2mean_spatial_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_tau0.25_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 123 · 2026-05-24T22:37:42.148532+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/",
  "description": "List project directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/",
    "description": "List project directory"
  }
}
```

</details>

---

### Tool result

_source line 124 · 2026-05-24T22:37:42.148681+00:00_

AGENTS.md
ROADMAP.lock
ROADMAP.md
_last_visual_review.json
artifacts
checkpoints
decisions.lock
decisions.yaml
docs
dream_registry.lock
dream_registry.yaml
dream_registry.yaml.bak
experiment_plan.lock
experiment_plan.yaml
figures
literature_map.yaml
logs
memory.md
mistakes.lock
mistakes.yaml
openvla_oft_wrapper.py
paper
paper_framing.md
paper_provenance.lock
paper_provenance.yaml
patch_modeling.py
registry.lock
registry.yaml
report.md
scripts
src
study_status.lock
task_context
worker_output.md
writing_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 125 · 2026-05-24T22:37:42.148841+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -inE \"spatial|adaptive|tau|seed\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md 2>/dev/null | head -50",
  "description": "Search memory.md for spatial/adaptive context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -inE \"spatial|adaptive|tau|seed\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md 2>/dev/null | head -50",
    "description": "Search memory.md for spatial/adaptive context"
  }
}
```

</details>

---

### Tool result

_source line 126 · 2026-05-24T22:37:42.148986+00:00_

26:| eval-supp-long-adapt-tau025-s45 | cuda:2 | — | 103397 | ALIVE | 23% util, 4917 MiB |
29:| eval-supp-goal-adapt-tau025-s45 | cuda:5 | — | 104216 | ALIVE | 22% util, 2786 MiB |
42:| eval-supp-k2mean-obj-s46 | cuda:3 | — | — | COMPLETED | 76.5% (153/200), saved eval_object_vla_only_seed46.json |
43:| eval-supp-k2mean-obj-s45 | cuda:0 | — | — | COMPLETED | 77.5% (155/200), saved eval_object_vla_only_seed45.json |
44:| eval-supp-long-crm-norm005-s44 | cuda:5 | 291523 | — | COMPLETED | 56.5% (113/200), saved eval_long_crm_obs_only_norm0.05_seed44.json |
45:| eval-supp-long-adapt-tau025-s44 | cuda:1 | 291315 | — | COMPLETED | 56.0% (112/200), trigger_rate=4.9%, saved eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json |
50:Tmux sessions: eval-reconvla-obj-s45, eval-reconvla-obj-s46 (+ stale: k2mean_spatial_s43)
82:| eval-supp-long-adapt-tau025-s44 | 56.0% (112/200) |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 127 · 2026-05-24T22:37:42.149124+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -B2 -A8 -inE \"spatial\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md 2>/dev/null | head -100",
  "description": "Search report.md for spatial info"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -B2 -A8 -inE \"spatial\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md 2>/dev/null | head -100",
    "description": "Search report.md for spatial info"
  }
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-24T22:37:42.149254+00:00_

3-> 由 Agent 生成。硬限 150 行。
4-
5:## τ-sweep 结果（Spatial, seed=42）— 全部完成
6-| τ | SR | trigger_rate |
7-|---|-----|-------------|
8-| 0.10 | 79.0% | 75.2% |
9-| 0.15 | 80.5% | 40.7% |
10-| **0.20** | **81.0%** | **26.6%** |
11-| 0.25 | 79.5% | 19.6% |
12-| 0.30 | 80.5% | 16.7% |
13-| 0.35 | 80.0% | 12.2% |
--
19-
20-## Table 1 8-seed（art_20260524_7faa0d）
21:清洗后 Spatial Δ(A-V) p=0.0049。数据缺口正在填补中。
22-
23-## 运行中实验
24-| 服务器 | GPU | 实验 |
25-|--------|-----|------|
26-| bjb1-32546:0 | 0 | vla_only object s42 |
27-| bjb1-32546:2 | 2 | vla_only object s43 |
28-| bjb1-32546:3 | 3 | vla_only object s44 |
29-| bjb1-32546:4 | 4 | vla_only goal s42 |
30-| bjb1-32546:5 | 5 | vla_only long s43 |
31:| bjb2-28827:0 | 0 | CRM spatial s48 |
32:| bjb2-28827:4 | 4 | CRM spatial s49 |
33-| bjb2-28827:5 | 5 | CRM goal s48 |
34-| bjb2-28827:2 | 2 | π0.5 reconvla goal s42 |
35-| bjb2-28827:3 | 3 | π0.5 reconvla object s42 |
36-| bjb1-18228:1 | 1 | CRM object s48 |
37-| bjb1-18228:2 | 2 | CRM goal s49 |
38-| bjb1-18228:3 | 3 | precompute-pi05-long-2048-r2 (疑似僵尸) |
39-| bjb2-40593:0 | 0 | K=5 sweep (~50min) |
40-| cqa1-32758 | ? | 部署 Worker 运行中 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 129 · 2026-05-24T22:37:42.149431+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -B2 -A20 -inE \"art_20260524_7faa0d|table.?1|8.?seed\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/*.md 2>/dev/null | head -200",
  "description": "Search artifacts md for table 1 context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -B2 -A20 -inE \"art_20260524_7faa0d|table.?1|8.?seed\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/*.md 2>/dev/null | head -200",
    "description": "Search artifacts md for table 1 context"
  }
}
```

</details>

---

### Tool result

_source line 130 · 2026-05-24T22:37:42.149633+00:00_

&lt;persisted-output>
Output too large (38.2KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/5496f3ef-d9d0-4fa3-b43b-00c635802928/tool-results/b5ag74hs2.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/benchmark_data_audit.md-48-| eval-crm-spatial-k10-seed51 | 51 | 0.36 |
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/benchmark_data_audit.md-49-
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/benchmark_data_audit.md:50:**Diff**: MATCH — all 8 seeds present with correct values.
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/benchmark_data_audit.md-51-- Note: eval-mag-obsonly-norm02 has `conclusion=negative` (not `success`), but SR=0.35 is valid data. Script correctly uses it.
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/benchmark_data_audit.md-52-
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/benchmark_data_audit.md-53-#### VLA-only
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/benchmark_data_audit.md-54-**Script**: n=9, seeds=[42, 43, 44, 45, 46, 47, 48, 49, 50]
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/benchmark_data_audit.md-55-- values: {42: 0.30, 43: 0.29, 44: 0.31, 45: 0.27, 46: 0.30, 47: 0.30, 48: 0.30, 49: 0.29, 50: 0.30}
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/benchmark_data_audit.md-56-
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/benchmark_data_audit.md-57-**Registry** (DONE+success):
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/proj
…[truncated 241 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 131 · 2026-05-24T22:37:42.149786+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -B2 -A30 -E \"Spatial\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/benchmark_data_audit.md 2>/dev/null | head -150",
  "description": "Look at the spatial section of benchmark audit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -B2 -A30 -E \"Spatial\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/benchmark_data_audit.md 2>/dev/null | head -150",
    "description": "Look at the spatial section of benchmark audit"
  }
}
```

</details>

---

### Tool result

_source line 132 · 2026-05-24T22:37:42.149950+00:00_

| Category | Count | Details |
|----------|-------|---------|
| **Perfect matches** | 9/15 | Spatial-CRM, Long-CRM, Long-VLA (10/11), Goal-VLA, Obj-norm02-K10 (6/6), Obj-K5, Obj-VLA, Argmin-K10, Argmin-K5 |
| **Seeds in script but not in DONE+success registry** | 8 | See details below |
| **Seeds in registry but excluded from script** | 1 | Obj-CRM-norm02-K10 seed42 |
| **Value mismatches** | 0 | All common seeds have matching SR values |
| **Registry status anomalies** | 6 | Experiments with data but status ≠ DONE or conclusion ≠ success |

### Seeds in Script Not in DONE+success Registry

| Benchmark | Method | Seed | Script SR | Registry Status | Notes |
|-----------|--------|------|-----------|-----------------|-------|
| Spatial | VLA-only | 48 | 0.30 | DONE/failed | Director directive; data exists outside registry |
| Spatial | VLA-only | 49 | 0.29 | DONE/failed | Director directive; data exists outside registry |
| Spatial | VLA-only | 50 | 0.30 | PREPARING/success | SR=0.30 in registry but status not DONE |
| Long | VLA-only | 49 | 0.16 | PREPARING/None | No SR in registry; Director directive |
| Goal | CRM obs_only | 47 | 0.69 | PREPARING/None | SR=0.69 in registry metrics but status PREPARING |
| Object | CRM norm01 | 42 | 0.19 | DEPLOYED/success | SR=0.19 in registry but status DEPLOYED, not DONE |
| Object | Adaptive-K p50 | 42,43 | 0.16,0.16 | ALLOCATED/success | SR matches; status should be DONE |
| Object | Adaptive-K p75 | 42,43 | 0.12,0.13 | ALLOCATED/success | SR matches; status should be DONE |

---

## Per-Benchmark Details

### LIBERO-Spatial

#### CRM obs_only norm02 K=10
**Script**: n=8, seeds=[42, 43, 44, 45, 46, 47, 48, 51]
- values: {42: 0.35, 43: 0.34, 44: 0.36, 45: 0.34, 46: 0.33, 47: 0.32, 48: 0.35, 51: 0.36}

**Registry** (all DONE+success):

| exp_id | seed | SR |
|--------|------|----|
| eval-mag-obsonly-norm02 | 42 | 0.35 |
| eval-obs-only-spatial-norm02-seed43-r2 | 43 | 0.34 |
| eval-obs-only-spatial-norm02-seed44 | 44 | 0.36 |
| ev
…[truncated 3464 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 133 · 2026-05-24T22:37:42.150112+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "head -c 700 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "head -c 700 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 134 · 2026-05-24T22:37:42.150280+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.3,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.6,\\n      \\\"successes\\\": 6,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 10,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"su\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 135 · 2026-05-24T22:37:42.150442+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md 2>/dev/null | head -150",
  "description": "Read project report"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md 2>/dev/null | head -150",
    "description": "Read project report"
  }
}
```

</details>

---

### Tool result

_source line 136 · 2026-05-24T22:37:42.150575+00:00_

# Handover — 2026-05-24 21:00 UTC

> 由 Agent 生成。硬限 150 行。

## τ-sweep 结果（Spatial, seed=42）— 全部完成
| τ | SR | trigger_rate |
|---|-----|-------------|
| 0.10 | 79.0% | 75.2% |
| 0.15 | 80.5% | 40.7% |
| **0.20** | **81.0%** | **26.6%** |
| 0.25 | 79.5% | 19.6% |
| 0.30 | 80.5% | 16.7% |
| 0.35 | 80.0% | 12.2% |

SR 平坦（2pp 波动），trigger_rate 随 τ 单调下降。τ=0.10 过度修正降 SR → 支持 D140 方案 C。

## K-sweep（部分）
- K=1: SR=79.5% | K=5: 运行中 bjb2-40593 (7/10 tasks) | K=10: 默认值（见 τ-sweep）

## Table 1 8-seed（art_20260524_7faa0d）
清洗后 Spatial Δ(A-V) p=0.0049。数据缺口正在填补中。

## 运行中实验
| 服务器 | GPU | 实验 |
|--------|-----|------|
| bjb1-32546:0 | 0 | vla_only object s42 |
| bjb1-32546:2 | 2 | vla_only object s43 |
| bjb1-32546:3 | 3 | vla_only object s44 |
| bjb1-32546:4 | 4 | vla_only goal s42 |
| bjb1-32546:5 | 5 | vla_only long s43 |
| bjb2-28827:0 | 0 | CRM spatial s48 |
| bjb2-28827:4 | 4 | CRM spatial s49 |
| bjb2-28827:5 | 5 | CRM goal s48 |
| bjb2-28827:2 | 2 | π0.5 reconvla goal s42 |
| bjb2-28827:3 | 3 | π0.5 reconvla object s42 |
| bjb1-18228:1 | 1 | CRM object s48 |
| bjb1-18228:2 | 2 | CRM goal s49 |
| bjb1-18228:3 | 3 | precompute-pi05-long-2048-r2 (疑似僵尸) |
| bjb2-40593:0 | 0 | K=5 sweep (~50min) |
| cqa1-32758 | ? | 部署 Worker 运行中 |

## ⚠️ 告警
- **π0.5 CRM 训练中断**：epoch 26 被平台 SIGKILL，best val_loss=0.004790 @ epoch 25。Worker 已派恢复。
- **precompute-pi05-long-2048-r2**：PID 114507，47h+，疑似僵尸。
- **GPU 空闲**：bjb1-32546:1, bjb2-28827:1 各 1 张空闲。

## π0.5 Object s43
r4=98.5% 有效（chunked），v2=86.5% OOM 废结果。closed-loop 用 r3=81.5%。

## 趋势
成功 496+ / 负向 75 / 失败 80+

## 下一步
1. K=5 结果 → 完成 K-sweep
2. 收割 bjb1-32546 VLA-only → 补 Table 1 缺口
3. CRM 训练恢复 → π0.5 评估前置
4. cqa1-32758 部署确认

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 137 · 2026-05-24T22:37:42.150732+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts -iname \"*table*\" -o -iname \"*7faa0d*\" 2>/dev/null | head -20",
  "description": "Find Table 1 artifact files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts -iname \"*table*\" -o -iname \"*7faa0d*\" 2>/dev/null | head -20",
    "description": "Find Table 1 artifact files"
  }
}
```

</details>

---

### Tool result

_source line 138 · 2026-05-24T22:37:42.150856+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/comparison_table.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/table1_8seed_final.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/results_tables.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/table1_8seed_v2.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/figures/object_benchmark_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/figures/spatial_final_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/results_tables.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/analysis/comparison_table.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 139 · 2026-05-24T22:37:42.150975+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/table1_8seed_final.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/table1_8seed_final.md"
  }
}
```

</details>

---

### Tool result

_source line 140 · 2026-05-24T22:37:42.151125+00:00_

1	# Table 1 — Multi-seed Results (Clean supp-era data)
2	
3	Generated: 2026-05-24 20:10 UTC
4	
5	## Main Table
6	
7	| Suite | VLA-only | CRM (ε=0.05) | Adaptive (τ=0.25) | Δ(A-V) | Δ(A-C) |
8	|-------|---------|-------------|-------------------|--------|--------|
9	| Spatial | 79.1±1.1 (8s) | 79.8±1.4 (5s) | 80.9±0.9 (8s) | **+1.8pp** | +1.1pp |
10	| Goal | 82.9±1.1 (7s) | 82.7±1.6 (6s) | 83.4±1.8 (8s) | +0.5pp | +0.8pp |
11	| Object | 77.0±1.8 (5s) | 78.0±2.9 (6s) | 77.0±2.1 (8s) | +0.0pp | -1.0pp |
12	| Long | 58.4±1.6 (5s) | 56.4±2.3 (6s) | 57.8±1.9 (6s) | -0.6pp | +1.3pp |
13	
14	## Paired t-test: Δ(A-V) = Adaptive - VLA-only
15	
16	| Suite | Δ(mean) | t-stat | p-value | n matched | Seeds |
17	|-------|---------|--------|---------|-----------|-------|
18	| **Spatial** | **+1.75pp** | **4.041** | **0.0049** | **8** | s42-s49 |
19	| Goal | +0.43pp | 0.505 | 0.6314 | 7 | s43-s49 |
20	| Object | -0.50pp | -0.520 | 0.6306 | 5 | s45-s49 |
21	| Long | -0.70pp | -0.578 | 0.5940 | 5 | s42,s44-s47 |
22	
23	## Paired t-test: Δ(A-C) = Adaptive - CRM always-on
24	
25	| Suite | Δ(mean) | t-stat | p-value | n matched | Seeds |
26	|-------|---------|--------|---------|-----------|-------|
27	| Spatial | +0.60pp | 0.885 | 0.4263 | 5 | s43-s47 |
28	| Goal | +0.92pp | 1.309 | 0.2474 | 6 | s42-s47 |
29	| Object | -0.33pp | -0.249 | 0.8134 | 6 | s42-s47 |
30	| Long | +1.33pp | 1.315 | 0.2455 | 6 | s42-s47 |
31	
32	## Trigger Rate ↔ Effect Size (D140 key evidence)
33	
34	| Suite | Mean Trigger Rate | Δ(A-V) | Correlation |
35	|-------|------------------|--------|-------------|
36	| Spatial | 19.8% | +1.75pp | Highest trigger → Strongest positive Δ |
37	| Goal | 8.6% | +0.43pp | Medium trigger → Small positive Δ |
38	| Object | 3.8% | -0.50pp | Low trigger → Near zero Δ |
39	| Long | 4.2% | -0.70pp | Low trigger → Near zero Δ |
40	
41	## Per-seed Raw Data
42	
43	### Spatial (8 matched seeds)
44	| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |
45	|------|---------|----------|-----|-------
…[truncated 2279 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 141 · 2026-05-24T22:37:42.151327+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -rE \"supp-spatial|supp.*spatial.*vla\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml 2>/dev/null | head -30",
  "description": "Find supp-spatial entries in registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -rE \"supp-spatial|supp.*spatial.*vla\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml 2>/dev/null | head -30",
    "description": "Find supp-spatial entries in registry"
  }
}
```

</details>

---

### Tool result

_source line 142 · 2026-05-24T22:37:42.151472+00:00_

  eval-supp-spatial-vla-only-s43:
      log_path: ~/runs/acr-vla-conformal-refinement/eval-supp-spatial-vla-only-s43.log
    log_path: ~/runs/acr-vla-conformal-refinement/eval-supp-spatial-vla-only-s43.log
  eval-supp-spatial-vla-only-s44:
      log_path: ~/runs/acr-vla-conformal-refinement/eval-supp-spatial-vla-only-s44.log
  eval-supp-spatial-vla-only-s45:
  eval-supp-spatial-crm-norm005-s45:
  eval-supp-spatial-reconvla-s45:
  eval-supp-spatial-adapt-tau025-s45:
      log_path: /root/runs/acr-vla-conformal-refinement/eval-supp-spatial-adapt-tau025-s45.log
      tmux_session: eval-supp-spatial-adapt-tau025-s45
  eval-supp-spatial-k2mean-s45:
  eval-supp-spatial-k2mean-s46:
  eval-supp-spatial-adapt-tau025-s45-r3:
    parent: eval-supp-spatial-adapt-tau025-s45
      log_path: /root/runs/acr-vla-conformal-refinement/eval-supp-spatial-adapt-tau025-s45.log
      tmux_session: eval-supp-spatial-adapt-tau025-s45
  eval-supp-spatial-adapt-tau025-s46:
  eval-supp-spatial-crm-norm005-s46:
  eval-supp-spatial-vla-only-s46:
  eval-supp-spatial-reconvla-s46:
  eval-supp-spatial-crm-norm005-s47:
    parent: eval-supp-spatial-crm-norm005-s46
    notes: 'DUPLICATE of eval-supp-spatial-k2mean-s47 (different naming). JSON overwritten
  eval-supp-spatial-vla-only-s47:
  eval-supp-spatial-adapt-tau025-s47:
  eval-supp-spatial-k2mean-s47:
    notes: 'WARNING: per-task JSON was overwritten by eval-supp-spatial-vla-only-s47
  eval-supp-spatial-reconvla-s47:
  eval-supp-spatial-vla-only-s42:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 143 · 2026-05-24T22:37:42.151599+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -B1 -A8 \"eval-supp-spatial-vla-only-s44:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml 2>/dev/null | head -40",
  "description": "Inspect eval-supp-spatial-vla-only-s44 spec"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -B1 -A8 \"eval-supp-spatial-vla-only-s44:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml 2>/dev/null | head -40",
    "description": "Inspect eval-supp-spatial-vla-only-s44 spec"
  }
}
```

</details>

---

### Tool result

_source line 144 · 2026-05-24T22:37:42.151717+00:00_

    completed_at: '2026-05-23T14:21:57.954Z'
  eval-supp-spatial-vla-only-s44:
    status: DONE
    retry_count: 0
    created_at: '2026-05-23T11:51:10.407Z'
    updated_at: '2026-05-23T17:22:10.552Z'
    spec:
      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
        base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py
        --mode vla_only --benchmark spatial --seed 44 --n_rollouts 20"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 145 · 2026-05-24T22:37:42.151846+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -B1 -A20 \"eval-supp-spatial-vla-only-s42:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml 2>/dev/null | head -30",
  "description": "Inspect supp-spatial-vla-only-s42"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -B1 -A20 \"eval-supp-spatial-vla-only-s42:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml 2>/dev/null | head -30",
    "description": "Inspect supp-spatial-vla-only-s42"
  }
}
```

</details>

---

### Tool result

_source line 146 · 2026-05-24T22:37:42.151966+00:00_

        oj: 0.9
  eval-supp-spatial-vla-only-s42:
    status: DONE
    retry_count: 0
    created_at: '2026-05-24T15:56:22.838Z'
    updated_at: '2026-05-24T19:35:25.978Z'
    hypothesis: SmolVLA VLA-only baseline on LIBERO-Spatial seed 42. Missing seed
      in 7-seed baseline sweep (s43-s49 done); s42 completes the seed=42 baseline
      used for paired CRM/Adaptive comparisons. Re-deploy after PREPARING-stuck entry
      on bjb1-18228.
    spec:
      command: bash -c "set -o pipefail; cd /root/acr-vla-conformal-refinement &&
        python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 42 --n_rollouts
        20 2>&1 | tee logs/eval-supp-spatial-vla-only-s42.log"
      server: bjb1-18228
      gpu:
      - cuda:1
      pid: '356458'
      log_path: ~/runs/acr-vla-conformal-refinement/eval-supp-spatial-vla-only-s42.log
      submitted_at: '2026-05-24T16:18:52.189Z'
      submitted_via: submit_training_job
      backend: tmux

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 147 · 2026-05-24T22:37:42.152091+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -B1 -A40 \"eval-supp-spatial-vla-only-s42:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml 2>/dev/null | head -60",
  "description": "More detail on supp-spatial-s42 results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -B1 -A40 \"eval-supp-spatial-vla-only-s42:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml 2>/dev/null | head -60",
    "description": "More detail on supp-spatial-s42 results"
  }
}
```

</details>

---

### Tool result

_source line 148 · 2026-05-24T22:37:42.152222+00:00_

        oj: 0.9
  eval-supp-spatial-vla-only-s42:
    status: DONE
    retry_count: 0
    created_at: '2026-05-24T15:56:22.838Z'
    updated_at: '2026-05-24T19:35:25.978Z'
    hypothesis: SmolVLA VLA-only baseline on LIBERO-Spatial seed 42. Missing seed
      in 7-seed baseline sweep (s43-s49 done); s42 completes the seed=42 baseline
      used for paired CRM/Adaptive comparisons. Re-deploy after PREPARING-stuck entry
      on bjb1-18228.
    spec:
      command: bash -c "set -o pipefail; cd /root/acr-vla-conformal-refinement &&
        python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 42 --n_rollouts
        20 2>&1 | tee logs/eval-supp-spatial-vla-only-s42.log"
      server: bjb1-18228
      gpu:
      - cuda:1
      pid: '356458'
      log_path: ~/runs/acr-vla-conformal-refinement/eval-supp-spatial-vla-only-s42.log
      submitted_at: '2026-05-24T16:18:52.189Z'
      submitted_via: submit_training_job
      backend: tmux
      account: root
      data_path: LIBERO-Spatial (10 tasks × 20 rollouts)
      data_count: 200
      model_name: pi05
      seed: 42
      checkpoint_source: /root/autodl-tmp/models/pi05_libero_finetuned/
      eval_data: LIBERO-Spatial
      checkpoint_path: /root/autodl-tmp/models/pi05_libero_finetuned/
      wall_clock_seconds: 11293.8
      gpu_hours: 3.14
    metrics:
      overall_success_rate: 0.8
      successes: 160
      total: 200
      n_rollouts: 20
      benchmark: spatial
      seed: 42
      mode: vla_only
      model: pi05
    conclusion: success

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 149 · 2026-05-24T22:37:42.152478+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement -name \"*.json\" -iname \"*spatial*\" 2>/dev/null | head -30",
  "description": "Find spatial JSONs locally in project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement -name \"*.json\" -iname \"*spatial*\" 2>/dev/null | head -30",
    "description": "Find spatial JSONs locally in project"
  }
}
```

</details>

---

### Tool result

_source line 150 · 2026-05-24T22:37:42.152633+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_diagnosis_spatial-norm02-seed44_20260519T142056_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_check_spatial-training-pid_20260521T213417_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_diagnose_spatial-r4-baseline-missing_20260522T135352_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_deploy_cqa1-4gpu-spatial-goal-s45_20260523T212934_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_debug_spatial-eval-0pct_20260513T151936_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_investigate_vla-mean-spatial-finalize_20260514T221220_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_fix_crm-train-pi05-spatial-cache_20260521T212924_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analyze_eval-adaptive-k-spatial-p75-seed42_20260520T103231_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_diag_spatial-cache-fix_20260521T212824_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analyze_eval-supp-reconvla-spatial-s43_20260523T111954_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analyze_eval-adaptive-k-spatial-p25-seed42_20260520T103941_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_diagnose_eval-adaptive-k-spatial-p50-seed42_202
…[truncated 3101 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 151 · 2026-05-24T22:37:42.152790+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers -name \"*supp*spatial*\" 2>/dev/null | head -20",
  "description": "List supp spatial worker logs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers -name \"*supp*spatial*\" 2>/dev/null | head -20",
    "description": "List supp spatial worker logs"
  }
}
```

</details>

---

### Tool result

_source line 152 · 2026-05-24T22:37:42.152927+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analyze_eval-supp-adapt-tau025-spatial-s44_20260523T084318.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analyze_eval-supp-reconvla-spatial-s43_20260523T111954_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analyze_eval-supp-adapt-tau025-spatial-s44_20260523T084318_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analyze_eval-supp-adapt-tau015-spatial-s42-r2_20260523T061528_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analyze_eval-supp-reconvla-spatial-s44_20260523T112334_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analyze_eval-supp-adapt-tau015-spatial-s42-r2_20260523T061528.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analyze_eval-supp-adapt-tau035-spatial-s42-r2_20260523T061940_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analyze_eval-supp-k2mean-spatial-s43_20260523T112439_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analysis_eval-supp-k2mean-spatial-s42_20260523T093827_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analyze_eval-supp-k2mean-spatial-s43_20260523T112439.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analyze_eval-supp-adapt-tau025-spatial-s43_20260523T083433.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/wo
…[truncated 1442 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 153 · 2026-05-24T22:37:42.153065+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -B1 -A30 \"eval-supp-spatial-vla-only-s43:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml 2>/dev/null | head -50",
  "description": "supp-spatial-vla-only-s43 spec"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -B1 -A30 \"eval-supp-spatial-vla-only-s43:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml 2>/dev/null | head -50",
    "description": "supp-spatial-vla-only-s43 spec"
  }
}
```

</details>

---

### Tool result

_source line 154 · 2026-05-24T22:37:42.153195+00:00_

    completed_at: '2026-05-23T17:24:48.531Z'
  eval-supp-spatial-vla-only-s43:
    status: DONE
    retry_count: 0
    created_at: '2026-05-23T11:31:48.527Z'
    updated_at: '2026-05-23T14:41:43.043Z'
    spec:
      command: python -u src/evaluate.py --mode vla_only --benchmark spatial --seed
        43 --n_rollouts 20
      server: cqa1-32758
      gpu:
      - cuda:5
      pid: '181173'
      log_path: ~/runs/acr-vla-conformal-refinement/eval-supp-spatial-vla-only-s43.log
      submitted_at: '2026-05-23T11:31:46.804Z'
      submitted_via: submit_training_job
      backend: tmux
      account: root
      seed: 43
      data_path: LIBERO-Spatial
      data_count: 200
      model_name: SmolVLA
      wall_clock_seconds: 11396.2
      gpu_hours: 3.17
    hypothesis: VLA-only baseline on Spatial seed43. s42=78.5%. Second seed for 3-seed
      baseline mean±std.
    metrics:
      overall_success_rate: 0.79
      successes: 158
      total: 200
    conclusion: success
    checkpoint_path: N/A (eval only)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 155 · 2026-05-24T22:37:42.153364+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -l \"n_rollouts.*20\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed51.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed54.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "grep -l \"n_rollouts.*20\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed51.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed54.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 156 · 2026-05-24T22:37:42.153495+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 157 · 2026-05-24T22:37:42.153610+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -H \"n_rollouts\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "grep -H \"n_rollouts\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 158 · 2026-05-24T22:37:42.153749+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json:  \\\"n_rollouts\\\": 10,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 159 · 2026-05-24T22:37:42.153880+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "grep -H \"n_rollouts\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "grep -H \"n_rollouts\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 160 · 2026-05-24T22:37:42.154007+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json:  \\\"n_rollouts\\\": 20,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json:  \\\"n_rollouts\\\": 20,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json:  \\\"n_rollouts\\\": 20,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json:  \\\"n_rollouts\\\": 20,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json:  \\\"n_rollouts\\\": 20,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 161 · 2026-05-24T22:37:42.154125+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "grep -H \"n_rollouts\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "grep -H \"n_rollouts\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 162 · 2026-05-24T22:37:42.154254+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json:  \\\"n_rollouts\\\": 20,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json:  \\\"n_rollouts\\\": 20,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json:  \\\"n_rollouts\\\": 20,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json:  \\\"n_rollouts\\\": 20,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json:  \\\"n_rollouts\\\": 20,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json:  \\\"n_rollouts\\\": 20,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json:  \\\"n_rollouts\\\": 20,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json:  \\\"n_rollouts\\\": 20,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 163 · 2026-05-24T22:37:42.154468+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "find /root/acr-vla-conformal-refinement/logs -maxdepth 1 -name \"eval_spatial_adaptive*tau0.25*.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "find /root/acr-vla-conformal-refinement/logs -maxdepth 1 -name \"eval_spatial_adaptive*tau0.25*.json\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 164 · 2026-05-24T22:37:42.155209+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_tau0.25_seed47.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 165 · 2026-05-24T22:37:42.155394+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/acr-vla-conformal-refinement/logs -maxdepth 1 -name \"eval_spatial_adaptive*tau0.25*.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "find /root/acr-vla-conformal-refinement/logs -maxdepth 1 -name \"eval_spatial_adaptive*tau0.25*.json\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 166 · 2026-05-24T22:37:42.155544+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed49.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed48.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 167 · 2026-05-24T22:37:42.155668+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs -maxdepth 1 -name \"eval_spatial_adaptive*tau0.25*.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/logs -maxdepth 1 -name \"eval_spatial_adaptive*tau0.25*.json\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 168 · 2026-05-24T22:37:42.155790+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 169 · 2026-05-24T22:37:42.156103+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "head -c 3000 /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "head -c 3000 /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 170 · 2026-05-24T22:37:42.156391+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.795,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pi
…[truncated 524 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 171 · 2026-05-24T22:37:42.156592+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "grep -H \"overall_success_rate\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "grep -H \"overall_success_rate\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 172 · 2026-05-24T22:37:42.156748+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json:  \\\"overall_success_rate\\\": 0.785,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json:  \\\"overall_success_rate\\\": 0.79,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json:  \\\"overall_success_rate\\\": 0.81,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json:  \\\"overall_success_rate\\\": 0.77,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json:  \\\"overall_success_rate\\\": 0.805,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json:  \\\"overall_success_rate\\\": 0.81,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json:  \\\"overall_success_rate\\\": 0.795,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json:  \\\"overall_success_rate\\\": 0.785,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 173 · 2026-05-24T22:37:42.156894+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "grep -H \"overall_success_rate\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "grep -H \"overall_success_rate\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 174 · 2026-05-24T22:37:42.157020+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json:  \\\"overall_success_rate\\\": 0.8,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.88}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 175 · 2026-05-24T22:37:42.157153+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -200 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/comparison_table.py",
  "description": "Read comparison_table.py for Table 1 source mapping"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "Bash",
  "tool_args": {
    "command": "head -200 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/comparison_table.py",
    "description": "Read comparison_table.py for Table 1 source mapping"
  }
}
```

</details>

---

### Tool result

_source line 176 · 2026-05-24T22:37:42.157371+00:00_

#!/usr/bin/env python3
"""Six-way comparison table: seed42 + seed43 + pooled, LaTeX tabular output.

Dependencies: numpy
Usage: python comparison_table.py [--json INPUT.json] [--out TABLE.tex] [--dry-run]
"""

import argparse
import json
import sys
from pathlib import Path

import numpy as np

OUT_DIR = Path(__file__).parent.parent / "figures"
OUT_DIR.mkdir(parents=True, exist_ok=True)

SPATIAL_TASKS = [
    "between_plate_and_ramekin",
    "next_to_ramekin",
    "from_table_center",
    "on_cookie_box",
    "in_top_drawer",
    "on_ramekin",
    "next_to_cookie_box",
    "on_stove",
    "next_to_plate",
    "on_wooden_cabinet",
]

TASK_DISPLAY = {
    "between_plate_and_ramekin": "Betw. Plate \\& Ramekin",
    "next_to_ramekin": "Next to Ramekin",
    "from_table_center": "Table Center",
    "on_cookie_box": "On Cookie Box",
    "in_top_drawer": "In Top Drawer",
    "on_ramekin": "On Ramekin",
    "next_to_cookie_box": "Next to Cookie Box",
    "on_stove": "On Stove",
    "next_to_plate": "Next to Plate",
    "on_wooden_cabinet": "On Wooden Cabinet",
}

TRIALS_PER_TASK = 10

# Six methods for comparison
METHODS = [
    "vla_only",
    "vla_mean",
    "argmin",
    "acr_scalar",
    "acr_perdof",
    "acr_obs_only",
]

METHOD_DISPLAY = {
    "vla_only":     "VLA-only (K=1)",
    "vla_mean":     "VLA-mean (K=10)",
    "argmin":       "Argmin (K=10)",
    "acr_scalar":   "ACR scalar",
    "acr_perdof":   "ACR per-DOF",
    "acr_obs_only": "ACR obs-only",
}

# ── placeholder data ──────────────────────────────────────────────────
# Format: {method: {task: SR_0_to_1}}
# Fill these or pass --json
SEED42_DATA = {m: {t: None for t in SPATIAL_TASKS} for m in METHODS}
SEED43_DATA = {m: {t: None for t in SPATIAL_TASKS} for m in METHODS}


def load_data(json_path=None):
    if json_path:
        with open(json_path) as f:
            raw = json.load(f)
        return raw["seed42"], raw["seed43"]
    return SEED42_DATA, SEED43_DATA


def compute_overall_sr(data, method):
    ""
…[truncated 4286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 177 · 2026-05-24T22:37:42.157545+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Find Spatial result JSON files on servers', 'activeForm': 'Finding Spatial result JSON files', 'status': 'completed'}, {'content': 'Extract per-task SR for VLA-only and Adaptive across all seeds', 'activeForm': 'Extracting per-task SR', 'status': 'in_progress'}, {'content': 'Identify always-0% tasks and compute filtered stats', 'activeForm': 'Computing filtered stats', 'status': 'pending'}, {'content': 'Mechanism analysis: trigger_rate vs Delta correlation', 'activeForm': 'Analyzing mechanism', 'status': 'pending'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Find Spatial result JSON files on servers', 'activeForm': 'Finding Spatial result JSON files', 'status': 'completed'}, {'content': 'Extract per-task SR for VLA-only and Adaptive across all seeds', 'activeForm': 'Extracting per-task SR', 'status': 'in_progress'}, {'content': 'Identify always-0% tasks and compute filtered stats', 'activeForm': 'Computing filtered stats', 'status': 'pending'}, {'content': 'Mechanism analysis: trigger_rate vs Delta correlation', 'activeForm': 'Analyzing mechanism', 'status': 'pending'}]"
  }
}
```

</details>

---

### Tool result

_source line 178 · 2026-05-24T22:37:42.157690+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 179 · 2026-05-24T22:37:42.157820+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 180 · 2026-05-24T22:37:42.157978+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.785,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bl
…[truncated 277 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 181 · 2026-05-24T22:37:42.158139+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 182 · 2026-05-24T22:37:42.158406+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.79,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bla
…[truncated 6620 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 183 · 2026-05-24T22:37:42.158583+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "grep -H \"baseline_mode\\|overall_success_rate\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "grep -H \"baseline_mode\\|overall_success_rate\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 184 · 2026-05-24T22:37:42.158714+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 185 · 2026-05-24T22:37:42.158833+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "grep -HE \"baseline_mode|overall_success_rate\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "grep -HE \"baseline_mode|overall_success_rate\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 186 · 2026-05-24T22:37:42.158953+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 187 · 2026-05-24T22:37:42.159066+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "grep -H baseline_mode /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "grep -H baseline_mode /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 188 · 2026-05-24T22:37:42.159202+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json:  \\\"baseline_mode\\\": \\\"mean\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json:  \\\"baseline_mode\\\": \\\"single\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json:  \\\"baseline_mode\\\": \\\"single\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json:  \\\"baseline_mode\\\": \\\"single\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json:  \\\"baseline_mode\\\": \\\"single\\\",\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 189 · 2026-05-24T22:37:42.159360+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "grep -H baseline_mode /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "grep -H baseline_mode /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 190 · 2026-05-24T22:37:42.159497+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json:  \\\"baseline_mode\\\": \\\"single\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json:  \\\"baseline_mode\\\": \\\"single\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json:  \\\"baseline_mode\\\": \\\"mean\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json:  \\\"baseline_mode\\\": \\\"single\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json:  \\\"baseline_mode\\\": \\\"single\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json:  \\\"baseline_mode\\\": \\\"single\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json:  \\\"baseline_mode\\\": \\\"single\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json:  \\\"baseline_mode\\\": \\\"single\\\",\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 191 · 2026-05-24T22:37:42.159617+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 192 · 2026-05-24T22:37:42.159770+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.805,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_blac
…[truncated 275 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 193 · 2026-05-24T22:37:42.159932+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -H baseline_mode /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "grep -H baseline_mode /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 194 · 2026-05-24T22:37:42.160063+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json:  \\\"baseline_mode\\\": \\\"single\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json:  \\\"baseline_mode\\\": \\\"single\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json:  \\\"baseline_mode\\\": \\\"single\\\",\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 195 · 2026-05-24T22:37:42.160188+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "grep -H baseline_mode /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "grep -H baseline_mode /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 196 · 2026-05-24T22:37:42.160384+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json:  \\\"baseline_mode\\\": \\\"single\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json:  \\\"baseline_mode\\\": \\\"single\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json:  \\\"baseline_mode\\\": \\\"single\\\",\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 197 · 2026-05-24T22:37:42.160518+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "grep -H baseline_mode /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed49.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "grep -H baseline_mode /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed49.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 198 · 2026-05-24T22:37:42.160642+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed48.json:  \\\"baseline_mode\\\": \\\"single\\\",\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed49.json:  \\\"baseline_mode\\\": \\\"single\\\",\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 199 · 2026-05-24T22:37:42.160770+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 200 · 2026-05-24T22:37:42.160983+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.81,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_
…[truncated 4507 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 201 · 2026-05-24T22:37:42.161154+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 202 · 2026-05-24T22:37:42.161399+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.795,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pi
…[truncated 5251 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 203 · 2026-05-24T22:37:42.161561+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 204 · 2026-05-24T22:37:42.161788+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.8,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pic
…[truncated 5250 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 205 · 2026-05-24T22:37:42.161940+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed49.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed49.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 206 · 2026-05-24T22:37:42.162138+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.81,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pi
…[truncated 2888 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 207 · 2026-05-24T22:37:42.162341+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Find Spatial result JSON files on servers', 'activeForm': 'Finding Spatial result JSON files', 'status': 'completed'}, {'content': 'Extract per-task SR for VLA-only and Adaptive across all seeds', 'activeForm': 'Extracting per-task SR', 'status': 'completed'}, {'content': 'Identify always-0% tasks and compute filtered stats', 'activeForm': 'Computing filtered stats', 'status': 'in_progress'}, {'content': 'Mechanism analysis: trigger_rate vs Delta correlation', 'activeForm': 'Analyzing mechanism', 'status': 'pending'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Find Spatial result JSON files on servers', 'activeForm': 'Finding Spatial result JSON files', 'status': 'completed'}, {'content': 'Extract per-task SR for VLA-only and Adaptive across all seeds', 'activeForm': 'Extracting per-task SR', 'status': 'completed'}, {'content': 'Identify always-0% tasks and compute filtered stats', 'activeForm': 'Computing filtered stats', 'status': 'in_progress'}, {'content': 'Mechanism analysis: trigger_rate vs Delta correlation', 'activeForm': 'Analyzing mechanism', 'status': 'pending'}]"
  }
}
```

</details>

---

### Tool result

_source line 208 · 2026-05-24T22:37:42.162505+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 209 · 2026-05-24T22:37:42.162678+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport math\nfrom statistics import mean, stdev\n\nTASKS = [\n    \"between_plate_and_ramekin\",\n    \"next_to_ramekin\",\n    \"from_table_center\",\n    \"on_cookie_box\",\n    \"in_top_drawer\",\n    \"on_ramekin\",\n    \"next_to_cookie_box\",\n    \"on_stove\",\n    \"next_to_plate\",\n    \"on_wooden_cabinet\",\n]\n\n# Successes out of 20 per (task, seed)\n# Seeds: 42, 43, 44, 45, 46, 47, 48, 49\n\n# VLA-only (baseline_mode=single, n=20)\n# s42: cqa1, s43: cqa1, s44: bjb2-40593 (canonical), s45-49: cqa1\nVLA = {\n    \"between_plate_and_ramekin\":      [19, 17, 18, 18, 19, 19, 20, 18],\n    \"next_to_ramekin\":                [18, 20, 19, 18, 20, 19, 18, 19],\n    \"from_table_center\":              [19, 19, 19, 18, 20, 20, 19, 19],\n    \"on_cookie_box\":                  [17, 18, 20, 20, 20, 20, 19, 19],\n    \"in_top_drawer\":                  [14, 13, 15, 15, 14, 14, 16, 14],\n    \"on_ramekin\":                     [0,  0,  0,  0,  0,  0,  0,  0],\n    \"next_to_cookie_box\":             [20, 19, 20, 19, 20, 20, 19, 18],\n    \"on_stove\":                       [17, 18, 16, 15, 15, 18, 15, 16],\n    \"next_to_plate\":                  [15, 17, 16, 16, 16, 14, 17, 15],\n    \"on_wooden_cabinet\":              [18, 17, 14, 15, 17, 18, 16, 19],\n}\n\n# Adaptive Conformal CRM, tau=0.25, norm=0.2\nADP = {\n    \"between_plate_and_ramekin\":      [19, 19, 18, 19, 20, 20, 20, 19],\n    \"next_to_ramekin\":                [19, 19, 19, 19, 18, 20, 20, 20],\n    \"from_table_center\":              [20, 19, 20, 20, 19, 20, 20, 20],\n    \"on_cookie_box\":                  [20, 20, 20, 20, 20, 19, 19, 20],\n    \"in_top_drawer\":                  [13, 14, 13, 15, 13, 16, 13, 14],\n    \"on_ramekin\":                     [0,  0,  0,  0,  0,  0,  0,  0],\n    \"next_to_cookie_box\":             [20, 20, 20, 19, 20, 18, 19, 20],\n    \"on_stove\":                       [16, 16, 16, 16, 18, 17, 17, 16],\n    \"next_to_plate\":                  [16, 17, 16, 16, 15, 16, 16, 18],\n    \"on_wooden_cabinet\":              [16, 16, 19, 16, 17, 17, 18, 17],\n}\n\n# Overall trigger rates per seed (from adaptive_stats.trigger_rate)\nTRIGGER = [0.19650, 0.19447, 0.19977, 0.19955, 0.19917, 0.20456, 0.19767, 0.19523]\nSEEDS = [42, 43, 44, 45, 46, 47, 48, 49]\nN_ROLL = 20\nN_SEEDS = 8\n\n# Per-task aggregate SR (across 8 seeds, total successes / 160)\nprint(\"=\" * 95)\nprint(f\"{'Task':<26} | {'VLA-only SR':>11} | {'Adaptive SR':>11} | {'Δ':>7} | {'备注'}\")\nprint(\"-\" * 95)\ntotal_v, total_a = 0, 0\nfor t in TASKS:\n    sv = sum(VLA[t]); sa = sum(ADP[t])\n    total_v += sv; total_a += sa\n    sr_v = sv / (N_SEEDS * N_ROLL) * 100\n    sr_a = sa / (N_SEEDS * N_ROLL) * 100\n    d = sr_a - sr_v\n    note = \"\"\n    if sr_v == 0 and sr_a == 0:\n        note = \"always-0%\"\n    elif d < 0:\n        note = \"Adaptive 反降\"\n    print(f\"{t:<26} | {sr_v:>10.2f}% | {sr_a:>10.2f}% | {d:+6.2f}pp | {note}\")\nprint(\"-\" * 95)\nsr_v_all = total_v / (10 * N_SEEDS * N_ROLL) * 100\nsr_a_all = total_a / (10 * N_SEEDS * N_ROLL) * 100\nprint(f\"{'10-task overall':<26} | {sr_v_all:>10.2f}% | {sr_a_all:>10.2f}% | {sr_a_all-sr_v_all:+6.2f}pp |\")\n\n# Per-seed overall SR (all 10 tasks)\nprint(\"\\nPer-seed overall (all 10 tasks):\")\nprint(f\"{'Seed':<5} | {'VLA-only':>9} | {'Adaptive':>9} | {'Δ':>7} | {'trig_rate':>9}\")\nv_pct, a_pct = [], []\nfor i, s in enumerate(SEEDS):\n    v = sum(VLA[t][i] for t in TASKS) / (10 * N_ROLL) * 100\n    a = sum(ADP[t][i] for t in TASKS) / (10 * N_ROLL) * 100\n    v_pct.append(v); a_pct.append(a)\n    print(f\"{s:<5} | {v:>8.2f}% | {a:>8.2f}% | {a-v:+6.2f}pp | {TRIGGER[i]*100:>8.2f}%\")\n\n# Paired t-test (10 tasks)\ndiffs = [a - v for a, v in zip(a_pct, v_pct)]\nmean_d = mean(diffs)\nsd_d = stdev(diffs)\nse_d = sd_d / math.sqrt(len(diffs))\nt = mean_d / se_d\ndf = len(diffs) - 1\n\n# t-distribution p-value via approximation\n# For 2-sided p with t and df, use Student's t survival\ndef t_pvalue_2sided(t, df):\n    x = df / (df + t*t)\n    # Use scipy if avail; else fallback to approx using regularized incomplete beta\n    try:\n        from scipy.stats import t as tdist\n        return 2 * (1 - tdist.cdf(abs(t), df))\n    except ImportError:\n        # Incomplete beta approximation via simpson's rule (rough)\n        # Use formula: p = I(x; df/2, 1/2)\n        # Falling back to crude estimate\n        return None\n\np_full = t_pvalue_2sided(t, df)\nprint(f\"\\n全部 10 task paired t-test (n={N_SEEDS}):\")\nprint(f\"  VLA-only mean: {mean(v_pct):.2f}% | Adaptive mean: {mean(a_pct):.2f}%\")\nprint(f\"  Δ={mean_d:+.3f}pp, sd={sd_d:.3f}, t={t:.3f}, df={df}, p={p_full:.4f}\")\n\n# Identify always-0% tasks\nzero_tasks = [t for t in TASKS if sum(VLA[t]) == 0 and sum(ADP[t]) == 0]\nprint(f\"\\nAlways-0% task: {zero_tasks}\")\n\n# Filtered: exclude always-0% tasks\nkeep_tasks = [t for t in TASKS if t not in zero_tasks]\nv_pct_f, a_pct_f = [], []\nfor i, s in enumerate(SEEDS):\n    v = sum(VLA[t][i] for t in keep_tasks) / (len(keep_tasks) * N_ROLL) * 100\n    a = sum(ADP[t][i] for t in keep_tasks) / (len(keep_tasks) * N_ROLL) * 100\n    v_pct_f.append(v); a_pct_f.append(a)\n\ndiffs_f = [a - v for a, v in zip(a_pct_f, v_pct_f)]\nmean_df = mean(diffs_f); sd_df = stdev(diffs_f); se_df = sd_df / math.sqrt(len(diffs_f))\ntf = mean_df / se_df\np_filt = t_pvalue_2sided(tf, len(diffs_f) - 1)\nprint(f\"\\n剔除 always-0% task ({len(zero_tasks)} 个) 后 ({len(keep_tasks)} tasks, paired t-test):\")\nprint(f\"  VLA-only mean: {mean(v_pct_f):.2f}% | Adaptive mean: {mean(a_pct_f):.2f}%\")\nprint(f\"  Δ={mean_df:+.3f}pp, sd={sd_df:.3f}, t={tf:.3f}, df={len(diffs_f)-1}, p={p_filt:.4f}\")\n\n# Mechanism: per-task Δ vs VLA-only difficulty\nprint(\"\\nPer-task Δ ordered by VLA-only SR (mechanism):\")\nrows = []\nfor t in TASKS:\n    sv = sum(VLA[t]) / (N_SEEDS * N_ROLL) * 100\n    sa = sum(ADP[t]) / (N_SEEDS * N_ROLL) * 100\n    rows.append((t, sv, sa, sa - sv))\nrows.sort(key=lambda r: r[1])\nfor t, v, a, d in rows:\n    print(f\"  {t:<26} VLA={v:>5.1f}%  Δ={d:+5.2f}pp\")\n\n# Per-seed corr trigger vs Δ\nn = len(SEEDS)\nmt = mean(TRIGGER); md = mean(diffs)\nnum = sum((TRIGGER[i]-mt)*(diffs[i]-md) for i in range(n))\nden = math.sqrt(sum((TRIGGER[i]-mt)**2 for i in range(n)) * sum((diffs[i]-md)**2 for i in range(n)))\nr = num / den if den else float('nan')\nprint(f\"\\nPer-seed corr(trigger_rate, Δ): r={r:.3f}  (n=8, trigger 跨 seed 几乎不变, 此相关性 noisy)\")\nprint(f\"Trigger rate 范围: [{min(TRIGGER)*100:.2f}%, {max(TRIGGER)*100:.2f}%] mean={mean(TRIGGER)*100:.2f}%\")\nPYEOF",
  "description": "Run per-task statistical analysis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport math\nfrom statistics import mean, stdev\n\nTASKS = [\n    \"between_plate_and_ramekin\",\n    \"next_to_ramekin\",\n    \"from_table_center\",\n    \"on_cookie_box\",\n    \"in_top_drawer\",\n    \"on_ramekin\",\n    \"next_to_cookie_box\",\n    \"on_stove\",\n    \"next_to_plate\",\n    \"on_wooden_cabinet\",\n]\n\n# Successes out of 20 per (task, seed)\n# Seeds: 42, 43, 44, 45, 46, 47, 48, 49\n\n# VLA-only (baseline_mode=single, n=20)\n# s42: cqa1, s43: cqa1, s44: bjb2-40593 (canonical), s45-49: cqa1\nVLA = {\n    \"between_plate_and_ramekin\":      [19, 17, 18, 18, 19, 19, 20, 18],\n    \"next_to_ramekin\":                [18, 20, 19, 18, 20, 19, 18, 19],\n    \"from_table_center\":              [19, 19, 19, 18, 20, 20, 19, 19],\n    \"on_cookie_box\":                  [17, 18, 20, 20, 20, 20, 19, 19],\n    \"in_top_drawer\":                  [14, 13, 15, 15, 14, 14, 16, 14],\n    \"on_ramekin\":                     [0,  0,  0,  0,  0,  0,  0,  0],\n    \"next_to_cookie_box\":             [20, 19, 20, 19, 20, 20, 19, 18],\n    \"on_stove\":                       [17, 18, 16, 15, 15, 18, 15, 16],\n    \"next_to_plate\":                  [15, 17, 16, 16, 16, 14, 17, 15],\n    \"on_wooden_cabinet\":              [18, 17, 14, 15, 17, 18, 16, 19],\n}\n\n# Adaptive Conformal CRM, tau=0.25, norm=0.2\nADP = {\n    \"between_plate_and_ramekin\":      [19, 19, 18, 19, 20, 20, 20, 19],\n    \"next_to_ramekin\":                [19, 19, 19, 19, 18, 20, 20, 20],\n    \"from_table_center\":              [20, 19, 20, 20, 19, 20, 20, 20],\n    \"on_cookie_box\":                  [20, 20, 20, 20, 20, 19, 19, 20],\n    \"in_top_drawer\":                  [13, 14, 13, 15, 13, 16, 13, 14],\n    \"on_ramekin\":                     [0,  0,  0,  0,  0,  0,  0,  0],\n    \"next_to_cookie_box\":             [20, 20, 20, 19, 20, 18, 19, 20],\n    \"on_stove\":                       [16, 16, 16, 16, 18, 17, 17, 16],\n    \"next_to_plate\":                  [16, 17, 16, 16, 15, 16, 16, 18],\n    \"on_wooden_cabinet\":              [16, 16, 19, 16, 17, 17, 18, 17],\n}\n\n# Overall trigger rates per seed (from adaptive_stats.trigger_rate)\nTRIGGER = [0.19650, 0.19447, 0.19977, 0.19955, 0.19917, 0.20456, 0.19767, 0.19523]\nSEEDS = [42, 43, 44, 45, 46, 47, 48, 49]\nN_ROLL = 20\nN_SEEDS = 8\n\n# Per-task aggregate SR (across 8 seeds, total successes / 160)\nprint(\"=\" * 95)\nprint(f\"{'Task':<26} | {'VLA-only SR':>11} | {'Adaptive SR':>11} | {'Δ':>7} | {'备注'}\")\nprint(\"-\" * 95)\ntotal_v, total_a = 0, 0\nfor t in TASKS:\n    sv = sum(VLA[t]); sa = sum(ADP[t])\n    total_v += sv; total_a += sa\n    sr_v = sv / (N_SEEDS * N_ROLL) * 100\n    sr_a = sa / (N_SEEDS * N_ROLL) * 100\n    d = sr_a - sr_v\n    note = \"\"\n    if sr_v == 0 and sr_a == 0:\n        note = \"always-0%\"\n    elif d < 0:\n        note = \"Adaptive 反降\"\n    print(f\"{t:<26} | {sr_v:>10.2f}% | {sr_a:>10.2f}% | {d:+6.2f}pp | {note}\")\nprint(\"-\" * 95)\nsr_v_all = total_v / (10 * N_SEEDS * N_ROLL) * 100\nsr_a_all = total_a / (10 * N_SEEDS * N_ROLL) * 100\nprint(f\"{'10-task overall':<26} | {sr_v_all:>10.2f}% | {sr_a_all:>10.2f}% | {sr_a_all-sr_v_all:+6.2f}pp |\")\n\n# Per-seed overall SR (all 10 tasks)\nprint(\"\\nPer-seed overall (all 10 tasks):\")\nprint(f\"{'Seed':<5} | {'VLA-only':>9} | {'Adaptive':>9} | {'Δ':>7} | {'trig_rate':>9}\")\nv_pct, a_pct = [], []\nfor i, s in enumerate(SEEDS):\n    v = sum(VLA[t][i] for t in TASKS) / (10 * N_ROLL) * 100\n    a = sum(ADP[t][i] for t in TASKS) / (10 * N_ROLL) * 100\n    v_pct.append(v); a_pct.append(a)\n    print(f\"{s:<5} | {v:>8.2f}% | {a:>8.2f}% | {a-v:+6.2f}pp | {TRIGGER[i]*100:>8.2f}%\")\n\n# Paired t-test (10 tasks)\ndiffs = [a - v for a, v in zip(a_pct, v_pct)]\nmean_d = mean(diffs)\nsd_d = stdev(diffs)\nse_d = sd_d / math.sqrt(len(diffs))\nt = mean_d / se_d\ndf = len(diffs) - 1\n\n# t-distribution p-value via approximation\n# For 2-sided p with t and df, use Student's t survival\ndef t_pvalue_2sided(t, df):\n    x = df / (df + t*t)\n    # Use scipy if avail; else fallback to approx using regularized incomplete beta\n    try:\n        from scipy.stats import t as tdist\n        return 2 * (1 - tdist.cdf(abs(t), df))\n    except ImportError:\n        # Incomplete beta approximation via simpson's rule (rough)\n        # Use formula: p = I(x; df/2, 1/2)\n        # Falling back to crude estimate\n        return None\n\np_full = t_pvalue_2sided(t, df)\nprint(f\"\\n全部 10 task paired t-test (n={N_SEEDS}):\")\nprint(f\"  VLA-only mean: {mean(v_pct):.2f}% | Adaptive mean: {mean(a_pct):.2f}%\")\nprint(f\"  Δ={mean_d:+.3f}pp, sd={sd_d:.3f}, t={t:.3f}, df={df}, p={p_full:.4f}\")\n\n# Identify always-0% tasks\nzero_tasks = [t for t in TASKS if sum(VLA[t]) == 0 and sum(ADP[t]) == 0]\nprint(f\"\\nAlways-0% task: {zero_tasks}\")\n\n# Filtered: exclude always-0% tasks\nkeep_tasks = [t for t in TASKS if t not in zero_tasks]\nv_pct_f, a_pct_f = [], []\nfor i, s in enumerate(SEEDS):\n    v = sum(VLA[t][i] for t in keep_tasks) / (len(keep_tasks) * N_ROLL) * 100\n    a = sum(ADP[t][i] for t in keep_tasks) / (len(keep_tasks) * N_ROLL) * 100\n    v_pct_f.append(v); a_pct_f.append(a)\n\ndiffs_f = [a - v for a, v in zip(a_pct_f, v_pct_f)]\nmean_df = mean(diffs_f); sd_df = stdev(diffs_f); se_df = sd_df / math.sqrt(len(diffs_f))\ntf = mean_df / se_df\np_filt = t_pvalue_2sided(tf, len(diffs_f) - 1)\nprint(f\"\\n剔除 always-0% task ({len(zero_tasks)} 个) 后 ({len(keep_tasks)} tasks, paired t-test):\")\nprint(f\"  VLA-only mean: {mean(v_pct_f):.2f}% | Adaptive mean: {mean(a_pct_f):.2f}%\")\nprint(f\"  Δ={mean_df:+.3f}pp, sd={sd_df:.3f}, t={tf:.3f}, df={len(diffs_f)-1}, p={p_filt:.4f}\")\n\n# Mechanism: per-task Δ vs VLA-only difficulty\nprint(\"\\nPer-task Δ ordered by VLA-only SR (mechanism):\")\nrows = []\nfor t in TASKS:\n    sv = sum(VLA[t]) / (N_SEEDS * N_ROLL) * 100\n    sa = sum(ADP[t]) / (N_SEEDS * N_ROLL) * 100\n    rows.append((t, sv, sa, sa - sv))\nrows.sort(key=lambda r: r[1])\nfor t, v, a, d in rows:\n    print(f\"  {t:<26} VLA={v:>5.1f}%  Δ={d:+5.2f}pp\")\n\n# Per-seed corr trigger vs Δ\nn = len(SEEDS)\nmt = mean(TRIGGER); md = mean(diffs)\nnum = sum((TRIGGER[i]-mt)*(diffs[i]-md) for i in range(n))\nden = math.sqrt(sum((TRIGGER[i]-mt)**2 for i in range(n)) * sum((diffs[i]-md)**2 for i in range(n)))\nr = num / den if den else float('nan')\nprint(f\"\\nPer-seed corr(trigger_rate, Δ): r={r:.3f}  (n=8, trigger 跨 seed 几乎不变, 此相关性 noisy)\")\nprint(f\"Trigger rate 范围: [{min(TRIGGER)*100:.2f}%, {max(TRIGGER)*100:.2f}%] mean={mean(TRIGGER)*100:.2f}%\")\nPYEOF",
    "description": "Run per-task statistical analysis"
  }
}
```

</details>

---

### Tool result

_source line 210 · 2026-05-24T22:37:42.162893+00:00_

===============================================================================================
Task                       | VLA-only SR | Adaptive SR |       Δ | 备注
-----------------------------------------------------------------------------------------------
between_plate_and_ramekin  |      92.50% |      96.25% |  +3.75pp | 
next_to_ramekin            |      94.38% |      96.25% |  +1.88pp | 
from_table_center          |      95.62% |      98.75% |  +3.12pp | 
on_cookie_box              |      95.62% |      98.75% |  +3.12pp | 
in_top_drawer              |      71.88% |      69.38% |  -2.50pp | Adaptive 反降
on_ramekin                 |       0.00% |       0.00% |  +0.00pp | always-0%
next_to_cookie_box         |      96.88% |      97.50% |  +0.62pp | 
on_stove                   |      81.25% |      82.50% |  +1.25pp | 
next_to_plate              |      78.75% |      81.25% |  +2.50pp | 
on_wooden_cabinet          |      83.75% |      85.00% |  +1.25pp | 
-----------------------------------------------------------------------------------------------
10-task overall            |      79.06% |      80.56% |  +1.50pp |

Per-seed overall (all 10 tasks):
Seed  |  VLA-only |  Adaptive |       Δ | trig_rate
42    |    78.50% |    79.50% |  +1.00pp |    19.65%
43    |    79.00% |    80.00% |  +1.00pp |    19.45%
44    |    78.50% |    80.50% |  +2.00pp |    19.98%
45    |    77.00% |    80.00% |  +3.00pp |    19.96%
46    |    80.50% |    80.00% |  -0.50pp |    19.92%
47    |    81.00% |    81.50% |  +0.50pp |    20.46%
48    |    79.50% |    81.00% |  +1.50pp |    19.77%
49    |    78.50% |    82.00% |  +3.50pp |    19.52%

全部 10 task paired t-test (n=8):
  VLA-only mean: 79.06% | Adaptive mean: 80.56%
  Δ=+1.500pp, sd=1.309, t=3.240, df=7, p=0.0142

Always-0% task: ['on_ramekin']

剔除 always-0% task (1 个) 后 (9 tasks, paired t-test):
  VLA-only mean: 87.85% | Adaptive mean: 89.51%
  Δ=+1.667pp, sd=1.455, t=3.240, df=7, p=0.0142

Per-task Δ ordered by VLA-only SR (mechanis
…[truncated 641 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 211 · 2026-05-24T22:37:42.163052+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Find Spatial result JSON files on servers', 'activeForm': 'Finding Spatial result JSON files', 'status': 'completed'}, {'content': 'Extract per-task SR for VLA-only and Adaptive across all seeds', 'activeForm': 'Extracting per-task SR', 'status': 'completed'}, {'content': 'Identify always-0% tasks and compute filtered stats', 'activeForm': 'Computing filtered stats', 'status': 'completed'}, {'content': 'Mechanism analysis: trigger_rate vs Delta correlation', 'activeForm': 'Analyzing mechanism', 'status': 'completed'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Find Spatial result JSON files on servers', 'activeForm': 'Finding Spatial result JSON files', 'status': 'completed'}, {'content': 'Extract per-task SR for VLA-only and Adaptive across all seeds', 'activeForm': 'Extracting per-task SR', 'status': 'completed'}, {'content': 'Identify always-0% tasks and compute filtered stats', 'activeForm': 'Computing filtered stats', 'status': 'completed'}, {'content': 'Mechanism analysis: trigger_rate vs Delta correlation', 'activeForm': 'Analyzing mechanism', 'status': 'completed'}]"
  }
}
```

</details>

---

### Tool result

_source line 212 · 2026-05-24T22:37:42.163193+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 213 · 2026-05-24T22:37:42.163367+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/spatial_per_task_breakdown.md",
  "content": "# Spatial Per-Task SR Breakdown (P0: Reviewer Response)\n\nGenerated: 2026-05-24\nEval regime: LIBERO-Spatial, n_rollouts=20 per task, 10 tasks, 8 seeds (42-49)\nMethods: VLA-only (baseline_mode=single) vs Adaptive Conformal CRM (τ=0.25, norm=0.2)\n\n## Data Sources (canonical files used)\n\n| Seed | VLA-only source | Adaptive source |\n|------|-----------------|-----------------|\n| 42 | cqa1-32758 | bjb1-32546 |\n| 43 | cqa1-32758 | bjb1-32546 |\n| 44 | bjb2-40593 | bjb1-32546 |\n| 45 | cqa1-32758 | cqa1-32758 |\n| 46 | cqa1-32758 | cqa1-32758 |\n| 47 | cqa1-32758 | cqa1-32758 |\n| 48 | cqa1-32758 | bjb2-28827 |\n| 49 | cqa1-32758 | bjb2-28827 |\n\nAll files: `logs/eval_spatial_vla_only_seedXX.json`,\n`logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seedXX.json`.\n\n## Per-Task SR (mean over 8 seeds × 20 rollouts = 160 trials per cell)\n\n| Task | VLA-only SR | Adaptive SR | Δ | 备注 |\n|------|-------------|-------------|-----|------|\n| between_plate_and_ramekin | 92.5% | 96.3% | **+3.75pp** | |\n| next_to_ramekin | 94.4% | 96.3% | +1.88pp | |\n| from_table_center | 95.6% | 98.8% | **+3.12pp** | |\n| on_cookie_box | 95.6% | 98.8% | **+3.12pp** | |\n| in_top_drawer | 71.9% | 69.4% | **-2.50pp** | Adaptive 反降；唯一负 Δ task |\n| on_ramekin | 0.0% | 0.0% | 0.00pp | **always-0%** (任务自身极难) |\n| next_to_cookie_box | 96.9% | 97.5% | +0.62pp | 接近天花板 |\n| on_stove | 81.3% | 82.5% | +1.25pp | |\n| next_to_plate | 78.8% | 81.3% | +2.50pp | |\n| on_wooden_cabinet | 83.8% | 85.0% | +1.25pp | |\n| **10-task overall** | **79.06%** | **80.56%** | **+1.50pp** | |\n\n## Per-Seed Overall SR and Trigger Rate (all 10 tasks)\n\n| Seed | VLA-only | Adaptive | Δ | trigger_rate |\n|------|----------|----------|-----|--------------|\n| 42 | 78.50% | 79.50% | +1.00pp | 19.65% |\n| 43 | 79.00% | 80.00% | +1.00pp | 19.45% |\n| 44 | 78.50% | 80.50% | +2.00pp | 19.98% |\n| 45 | 77.00% | 80.00% | +3.00pp | 19.96% |\n| 46 | 80.50% | 80.00% | -0.50pp | 19.92% |\n| 47 | 81.00% | 81.50% | +0.50pp | 20.46% |\n| 48 | 79.50% | 81.00% | +1.50pp | 19.77% |\n| 49 | 78.50% | 82.00% | +3.50pp | 19.52% |\n\n## Paired t-test\n\n| Analysis | n_seeds | VLA-only | Adaptive | Δ | t | df | p |\n|----------|---------|----------|----------|-----|------|------|-------|\n| 全部 10 task | 8 | 79.06% | 80.56% | +1.50pp | 3.240 | 7 | **0.0142** |\n| 剔除 always-0% (9 task) | 8 | 87.85% | 89.51% | +1.67pp | 3.240 | 7 | **0.0142** |\n\n注：剔除 on_ramekin 不改变 p-value（恒零任务在 paired t-test 中两 arm 都减去相同值，\n方差结构不变；只把 SR base 从 200 缩到 180，Δ 在 pp 单位上等比放大 1.111 倍）。\n\n## Mechanism Analysis\n\n### Per-task Δ vs VLA-only baseline difficulty (sorted)\n\n| Task | VLA-only SR | Δ | bucket |\n|------|-------------|-----|--------|\n| on_ramekin | 0.0% | +0.00 | impossible |\n| in_top_drawer | 71.9% | **-2.50** | hardest non-zero — Adaptive hurts |\n| next_to_plate | 78.8% | +2.50 | mid |\n| on_stove | 81.3% | +1.25 | mid |\n| on_wooden_cabinet | 83.8% | +1.25 | mid |\n| between_plate_and_ramekin | 92.5% | +3.75 | high |\n| next_to_ramekin | 94.4% | +1.88 | high |\n| from_table_center | 95.6% | +3.12 | high |\n| on_cookie_box | 95.6% | +3.12 | high |\n| next_to_cookie_box | 96.9% | +0.62 | ceiling |\n\n### Trigger-rate observations\n\n- 8 seeds 的 overall trigger_rate 集中在 **19.45%–20.46%**（mean 19.84%, σ=0.31pp），\n  几乎不随 seed 变化 → conformal threshold 在 calibration 后表现稳定。\n- Per-task trigger_rate 未在 JSON 中输出，无法直接做 task-level trigger ↔ Δ correlation。\n- Per-seed corr(trigger_rate, Δ) = **-0.298** (n=8)，weak negative 但 trigger 跨 seed\n  几乎不变（range 1pp），相关性极不稳定，不作为证据。\n\n### 结论性观察\n\n1. **9/10 task 上 Adaptive ≥ VLA-only**（含一个 ties，on_ramekin 都是 0%）；\n   唯一例外是 **in_top_drawer（−2.50pp）**——也是 VLA-only 最弱的 non-zero task。\n   假设：该 task 视觉/几何挑战大（深抽屉里取物），CRM 可能放大了不可靠的 observation refinement。\n2. **on_ramekin always-0%** 的根因是任务本身（黑碗放在 ramekin 顶部），与方法无关；\n   该 task 完全不被任何方法救起，剔除后 Adaptive 的相对优势绝对值更大（87.85% → 89.51%）。\n3. Adaptive 改进 **不集中在最难 task** 上（top_drawer 反而变差），而是 **均匀分布于\n   mid-到-high SR task**，最大单 task gain 出现在 between_plate_and_ramekin (+3.75pp)\n   和 from_table_center/on_cookie_box (+3.12pp)。\n4. 8 个 seed 中 **7/8 Δ ≥ 0**（s46 = -0.5pp 为唯一例外），符号方向稳定，paired\n   t-test p=0.0142 显著。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/spatial_per_task_breakdown.md",
    "content": "# Spatial Per-Task SR Breakdown (P0: Reviewer Response)\n\nGenerated: 2026-05-24\nEval regime: LIBERO-Spatial, n_rollouts=20 per task, 10 tasks, 8 seeds (42-49)\nMethods: VLA-only (baseline_mode=single) vs Adaptive Conformal CRM (τ=0.25, norm=0.2)\n\n## Data Sources (canonical files used)\n\n| Seed | VLA-only source | Adaptive source |\n|------|-----------------|-----------------|\n| 42 | cqa1-32758 | bjb1-32546 |\n| 43 | cqa1-32758 | bjb1-32546 |\n| 44 | bjb2-40593 | bjb1-32546 |\n| 45 | cqa1-32758 | cqa1-32758 |\n| 46 | cqa1-32758 | cqa1-32758 |\n| 47 | cqa1-32758 | cqa1-32758 |\n| 48 | cqa1-32758 | bjb2-28827 |\n| 49 | cqa1-32758 | bjb2-28827 |\n\nAll files: `logs/eval_spatial_vla_only_seedXX.json`,\n`logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seedXX.json`.\n\n## Per-Task SR (mean over 8 seeds × 20 rollouts = 160 trials per cell)\n\n| Task | VLA-only SR | Adaptive SR | Δ | 备注 |\n|------|-------------|-------------|-----|------|\n| between_plate_and_ramekin | 92.5% | 96.3% | **+3.75pp** | |\n| next_to_ramekin | 94.4% | 96.3% | +1.88pp | |\n| from_table_center | 95.6% | 98.8% | **+3.12pp** | |\n| on_cookie_box | 95.6% | 98.8% | **+3.12pp** | |\n| in_top_drawer | 71.9% | 69.4% | **-2.50pp** | Adaptive 反降；唯一负 Δ task |\n| on_ramekin | 0.0% | 0.0% | 0.00pp | **always-0%** (任务自身极难) |\n| next_to_cookie_box | 96.9% | 97.5% | +0.62pp | 接近天花板 |\n| on_stove | 81.3% | 82.5% | +1.25pp | |\n| next_to_plate | 78.8% | 81.3% | +2.50pp | |\n| on_wooden_cabinet | 83.8% | 85.0% | +1.25pp | |\n| **10-task overall** | **79.06%** | **80.56%** | **+1.50pp** | |\n\n## Per-Seed Overall SR and Trigger Rate (all 10 tasks)\n\n| Seed | VLA-only | Adaptive | Δ | trigger_rate |\n|------|----------|----------|-----|--------------|\n| 42 | 78.50% | 79.50% | +1.00pp | 19.65% |\n| 43 | 79.00% | 80.00% | +1.00pp | 19.45% |\n| 44 | 78.50% | 80.50% | +2.00pp | 19.98% |\n| 45 | 77.00% | 80.00% | +3.00pp | 19.96% |\n| 46 | 80.50% | 80.00% | -0.50pp | 19.92% |\n| 47 | 81.00% | 81.50% | +0.50pp | 20.46% |\n| 48 | 79.50% | 81.00% | +1.50pp | 19.77% |\n| 49 | 78.50% | 82.00% | +3.50pp | 19.52% |\n\n## Paired t-test\n\n| Analysis | n_seeds | VLA-only | Adaptive | Δ | t | df | p |\n|----------|---------|----------|----------|-----|------|------|-------|\n| 全部 10 task | 8 | 79.06% | 80.56% | +1.50pp | 3.240 | 7 | **0.0142** |\n| 剔除 always-0% (9 task) | 8 | 87.85% | 89.51% | +1.67pp | 3.240 | 7 | **0.0142** |\n\n注：剔除 on_ramekin 不改变 p-value（恒零任务在 paired t-test 中两 arm 都减去相同值，\n方差结构不变；只把 SR base 从 200 缩到 180，Δ 在 pp 单位上等比放大 1.111 倍）。\n\n## Mechanism Analysis\n\n### Per-task Δ vs VLA-only baseline difficulty (sorted)\n\n| Task | VLA-only SR | Δ | bucket |\n|------|-------------|-----|--------|\n| on_ramekin | 0.0% | +0.00 | impossible |\n| in_top_drawer | 71.9% | **-2.50** | hardest non-zero — Adaptive hurts |\n| next_to_plate | 78.8% | +2.50 | mid |\n| on_stove | 81.3% | +1.25 | mid |\n| on_wooden_cabinet | 83.8% | +1.25 | mid |\n| between_plate_and_ramekin | 92.5% | +3.75 | high |\n| next_to_ramekin | 94.4% | +1.88 | high |\n| from_table_center | 95.6% | +3.12 | high |\n| on_cookie_box | 95.6% | +3.12 | high |\n| next_to_cookie_box | 96.9% | +0.62 | ceiling |\n\n### Trigger-rate observations\n\n- 8 seeds 的 overall trigger_rate 集中在 **19.45%–20.46%**（mean 19.84%, σ=0.31pp），\n  几乎不随 seed 变化 → conformal threshold 在 calibration 后表现稳定。\n- Per-task trigger_rate 未在 JSON 中输出，无法直接做 task-level trigger ↔ Δ correlation。\n- Per-seed corr(trigger_rate, Δ) = **-0.298** (n=8)，weak negative 但 trigger 跨 seed\n  几乎不变（range 1pp），相关性极不稳定，不作为证据。\n\n### 结论性观察\n\n1. **9/10 task 上 Adaptive ≥ VLA-only**（含一个 ties，on_ramekin 都是 0%）；\n   唯一例外是 **in_top_drawer（−2.50pp）**——也是 VLA-only 最弱的 non-zero task。\n   假设：该 task 视觉/几何挑战大（深抽屉里取物），CRM 可能放大了不可靠的 observation refinement。\n2. **on_ramekin always-0%** 的根因是任务本身（黑碗放在 ramekin 顶部），与方法无关；\n   该 task 完全不被任何方法救起，剔除后 Adaptive 的相对优势绝对值更大（87.85% → 89.51%）。\n3. Adaptive 改进 **不集中在最难 task** 上（top_drawer 反而变差），而是 **均匀分布于\n   mid-到-high SR task**，最大单 task gain 出现在 between_plate_and_ramekin (+3.75pp)\n   和 from_table_center/on_cookie_box (+3.12pp)。\n4. 8 个 seed 中 **7/8 Δ ≥ 0**（s46 = -0.5pp 为唯一例外），符号方向稳定，paired\n   t-test p=0.0142 显著。\n"
  }
}
```

</details>

---

### Tool result

_source line 214 · 2026-05-24T22:37:42.163634+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/spatial_per_task_breakdown.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 215 · 2026-05-24T22:37:42.163828+00:00_

## Spatial 10-Task SR Breakdown (VLA-only vs Adaptive τ=0.25, 8 seeds × 20 rollouts)

| Task | VLA-only | Adaptive | Δ | 备注 |
|------|----------|----------|-----|------|
| between_plate_and_ramekin | 92.5% | 96.3% | **+3.75pp** | |
| next_to_ramekin | 94.4% | 96.3% | +1.88pp | |
| from_table_center | 95.6% | 98.8% | +3.12pp | |
| on_cookie_box | 95.6% | 98.8% | +3.12pp | |
| in_top_drawer | 71.9% | 69.4% | **-2.50pp** | 唯一负 Δ |
| **on_ramekin** | **0.0%** | **0.0%** | **0.00pp** | **always-0%** |
| next_to_cookie_box | 96.9% | 97.5% | +0.62pp | |
| on_stove | 81.3% | 82.5% | +1.25pp | |
| next_to_plate | 78.8% | 81.3% | +2.50pp | |
| on_wooden_cabinet | 83.8% | 85.0% | +1.25pp | |
| **10-task overall** | **79.06%** | **80.56%** | **+1.50pp** | |

### Paired t-test (n=8 seeds)

| 范围 | VLA-only | Adaptive | Δ | t | df | p |
|------|----------|----------|-----|----|------|-------|
| 全部 10 task | 79.06% | 80.56% | +1.50pp | 3.240 | 7 | **0.0142** |
| 剔除 always-0% (9 task) | 87.85% | 89.51% | +1.67pp | 3.240 | 7 | **0.0142** |

注：剔除 on_ramekin 不改 p-value——恒零 task 在 paired diff 上贡献为 0，仅把 SR base 从 200 缩到 180，Δ 在 pp 单位上等比放大 ~1.11 倍。

### Mechanism

- **9/10 task Adaptive ≥ VLA-only**（含一个 ties）；唯一例外 in_top_drawer（−2.50pp）是 VLA-only 最弱的非零 task，推测深抽屉视觉挑战大、CRM 在此放大了不可靠 refinement。
- **on_ramekin always-0%** 是任务本身（黑碗放在 ramekin 顶部不可达），与方法无关。
- **trigger_rate 跨 8 seed 极稳定**：19.45%–20.46%（mean 19.84%，σ=0.31pp），conformal threshold 在 calibration 后稳定。
- Per-task trigger_rate 在 JSON 中**未输出**——无法直接做 task-level trigger↔Δ correlation；per-seed corr(trigger_rate, Δ)=-0.30（n=8）不显著且 trigger 几乎不变，不作证据。
- Adaptive gain **不集中在最难 task**（top_drawer 反降），而是均匀分布在 mid→high SR task，最大 gain 在 between_plate_and_ramekin (+3.75pp) 和 from_table_center / on_cookie_box (+3.12pp)。
- 8/8 seed 中 **7/8 Δ ≥ 0**（s46 = −0.5pp 是唯一例外），符号方向稳定。

数据源已记录到 `artifacts/spatial_per_task_breakdown.md`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_per-task-spatial-breakdown_20260524T222035"
}
```

</details>

---
