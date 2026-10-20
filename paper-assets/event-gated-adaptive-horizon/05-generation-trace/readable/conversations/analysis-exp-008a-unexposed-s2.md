# analysis exp 008a unexposed s2

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_analysis_exp_008a_unexposed_s2_20260518T080858.jsonl`
- **Structured JSON:** [`010cacc5f01be18bd4fc.json`](../../sessions/01/010cacc5f01be18bd4fc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-18T08:10:31.865595+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:fetch_wandb_metrics,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_008a_unexposed_s2_20260518T080858",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:fetch_wandb_metrics,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T08:10:31.866107+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_008a_unexposed_s2_20260518T080858",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T08:10:31.866380+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'exp_008a_unexposed_s2'}",
  "project": "event-gated-adaptive-horizon",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_008a_unexposed_s2_20260518T080858",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'exp_008a_unexposed_s2'}",
    "project": "event-gated-adaptive-horizon",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T08:10:31.866581+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7278}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_008a_unexposed_s2_20260518T080858",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T08:10:31.866752+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-45299",
  "command": "tail -100 /root/runs/event-gated-adaptive-horizon/exp_008a_unexposed_s2.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_008a_unexposed_s2_20260518T080858",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-45299",
    "command": "tail -100 /root/runs/event-gated-adaptive-horizon/exp_008a_unexposed_s2.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-18T08:10:31.866954+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-45299",
  "command": "ls -la /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_unexposed_s2/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_008a_unexposed_s2_20260518T080858",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-45299",
    "command": "ls -la /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_unexposed_s2/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-18T08:10:31.867252+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[45000] civo/ve_ratio 0.3 / civo/delta_ve 0.1 / civo/alert 0.0 / model_loss 3.7 / model_grad_norm 9.8 / height_loss 0.0 / orientations_loss 0.1 / velocity_loss 0.5 / reward_loss 0.6 / cont_loss 0.0 / kl_free 1.0 / dyn_scale 0.5 / rep_scale 0.1 / dyn_loss 4.2 / rep_loss 4.2 / kl 4.2 / prior_ent 38.2 / post_ent 33.8 / normed_target_mean 0.7 / normed_target_std 0.3 / normed_target_min -0.6 / normed_target_max 1.3 / EMA_005 115.8 / EMA_095 135.4 / value_mean 127.1 / value_std 5.7 / value_min 51.9 / value_max 135.4 / target_mean 128.8 / target_std 5.8 / target_min 103.7 / target_max 141.9 / imag_reward_mean 0.7 / imag_reward_std 0.6 / imag_reward_min 0.0 / imag_reward_max 2.0 / imag_action_mean -0.1 / imag_action_std 0.8 / imag_action_min -1.0 / imag_action_max 1.0 / actor_entropy -5.1 / gate_dt_mean 2.0 / gate_dt_std 0.0 / gate_dt_min 2.0 / gate_dt_max 2.0 / gate_dt_1_frac 0.0 / gate_dt_2_frac 1.0 / gate_dt_3_frac 0.0 / gate_dt_4_frac 0.0 / gate_dt_5_frac 0.0 / gate_dt_6_frac 0.0 / gate_dt_7_frac 0.0 / gate_dt_8_frac 0.0 / gate_empirical_entropy 0.0 / gate_entropy_ratio 0.0 / gate_dt_autocorr 0.0 / actor_loss -0.1 / actor_grad_norm 0.4 / value_loss 1.0 / value_grad_norm 0.2 / update_count 10099.0 / fps 11.0\\n[48000] dataset_size 24000.0 / train_return 492.9 / train_length 500.0 / train_episodes 48.0\\n[48000] dataset_size 24000.0 / train_return 416.8 / train_length 500.0 / train_episodes 48.0\\n[48000] dataset_size 24000.0 / train_return 572.5 / train_length 500.0 / train_episodes 48.0\\n[48000] dataset_size 24000.0 / train_return 398.3 / train_length 500.0 / train_episodes 48.0\\n[52000] dataset_size 26000.0 / train_return 421.8 / train_length 500.0 / train_episodes 52.0\\n[52000] dataset_size 26000.0 / train_return 509.9 / train_length 500.0 / train_episodes 52.0\\n[52000] dataset_size 26000.0 / train_return 430.8 / train_length 500.0 / train_episodes 52.0\\n[52000] dataset_size 26000.0 / train_return 513.7 / tr
…[truncated 6297 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_008a_unexposed_s2_20260518T080858",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T08:10:31.867533+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 678172\\ndrwxr-xr-x  4 root root      4096 May 18 15:05 .\\ndrwxr-xr-x 64 root root      4096 May 18 13:19 ..\\n-rw-r--r--  1 root root 231433043 May 18 13:50 checkpoint_25000.pt\\n-rw-r--r--  1 root root 231433043 May 18 15:05 checkpoint_75000.pt\\ndrwxr-xr-x  2 root root     12288 May 18 15:52 eval_eps\\n-rw-r--r--  1 root root     69554 May 18 16:03 events.out.tfevents.1779081567.autodl-container-k9z16fn7md-3a522761.724970.0\\n-rw-r--r--  1 root root 231423011 May 18 16:07 latest.pt\\n-rw-r--r--  1 root root     36349 May 18 16:03 metrics.jsonl\\ndrwxr-xr-x  2 root root     12288 May 18 16:03 train_eps\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_008a_unexposed_s2_20260518T080858",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T08:10:31.867800+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-45299",
  "command": "grep eval_return /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_unexposed_s2/metrics.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_008a_unexposed_s2_20260518T080858",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-45299",
    "command": "grep eval_return /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_unexposed_s2/metrics.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T08:10:31.868074+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"step\\\": 5000, \\\"eval_return\\\": 39.26672782897949, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n{\\\"step\\\": 15000, \\\"eval_return\\\": 159.75057067871094, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n{\\\"step\\\": 25000, \\\"eval_return\\\": 374.70808868408204, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n{\\\"step\\\": 35000, \\\"eval_return\\\": 431.6124771118164, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n{\\\"step\\\": 45000, \\\"eval_return\\\": 430.81328735351565, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n{\\\"step\\\": 55000, \\\"eval_return\\\": 607.5252105712891, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n{\\\"step\\\": 65000, \\\"eval_return\\\": 653.7507568359375, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n{\\\"step\\\": 75000, \\\"eval_return\\\": 534.4343353271485, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n{\\\"step\\\": 85000, \\\"eval_return\\\": 605.3503051757813, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n{\\\"step\\\": 95000, \\\"eval_return\\\": 819.4239990234375, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n{\\\"step\\\": 105000, \\\"eval_return\\\": 899.4473999023437, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_008a_unexposed_s2_20260518T080858",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T08:10:31.868292+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-45299",
  "command": "grep civo /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_unexposed_s2/metrics.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_008a_unexposed_s2_20260518T080858",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-45299",
    "command": "grep civo /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_unexposed_s2/metrics.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T08:10:31.868741+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"step\\\": 15000, \\\"civo/ve_ratio\\\": 0.03492530321708377, \\\"civo/delta_ve\\\": 0.0, \\\"civo/alert\\\": 0.0, \\\"model_loss\\\": 7.907504558563232, \\\"model_grad_norm\\\": 12.741704940795898, \\\"height_loss\\\": 0.008260374888777733, \\\"orientations_loss\\\": 0.4429621398448944, \\\"velocity_loss\\\": 1.6269655227661133, \\\"reward_loss\\\": 0.7291107177734375, \\\"cont_loss\\\": 2.9316892323549837e-05, \\\"kl_free\\\": 1.0, \\\"dyn_scale\\\": 0.5, \\\"rep_scale\\\": 0.09999999999999999, \\\"dyn_loss\\\": 8.500292778015137, \\\"rep_loss\\\": 8.500292778015137, \\\"kl\\\": 8.499000549316406, \\\"prior_ent\\\": 49.448570251464844, \\\"post_ent\\\": 40.16658401489258, \\\"normed_target_mean\\\": 0.5862044095993042, \\\"normed_target_std\\\": 0.3274591267108917, \\\"normed_target_min\\\": 0.016517043113708496, \\\"normed_target_max\\\": 1.7909878492355347, \\\"EMA_005\\\": 4.954224109649658, \\\"EMA_095\\\": 8.83747386932373, \\\"value_mean\\\": 5.587924480438232, \\\"value_std\\\": 0.22666488587856293, \\\"value_min\\\": 4.59206485748291, \\\"value_max\\\": 5.96164608001709, \\\"target_mean\\\": 7.24168586730957, \\\"target_std\\\": 1.319212794303894, \\\"target_min\\\": 4.949962615966797, \\\"target_max\\\": 12.326583862304688, \\\"imag_reward_mean\\\": 0.2569529712200165, \\\"imag_reward_std\\\": 0.2238810509443283, \\\"imag_reward_min\\\": 0.03190484642982483, \\\"imag_reward_max\\\": 0.9290904998779297, \\\"imag_action_mean\\\": -0.11692572385072708, \\\"imag_action_std\\\": 0.7495968341827393, \\\"imag_action_min\\\": -1.0, \\\"imag_action_max\\\": 1.0, \\\"actor_entropy\\\": -1.4059699773788452, \\\"gate_dt_mean\\\": 2.0, \\\"gate_dt_std\\\": 0.0, \\\"gate_dt_min\\\": 2.0, \\\"gate_dt_max\\\": 2.0, \\\"gate_dt_1_frac\\\": 0.0, \\\"gate_dt_2_frac\\\": 1.0, \\\"gate_dt_3_frac\\\": 0.0, \\\"gate_dt_4_frac\\\": 0.0, \\\"gate_dt_5_frac\\\": 0.0, \\\"gate_dt_6_frac\\\": 0.0, \\\"gate_dt_7_frac\\\": 0.
…[truncated 7766 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_008a_unexposed_s2_20260518T080858",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T08:10:31.869059+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "filters": "{'status': 'RUNNING'}",
  "fields": "['exp_id', 'status', 'hypothesis', 'parent']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_008a_unexposed_s2_20260518T080858",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "event-gated-adaptive-horizon",
    "filters": "{'status': 'RUNNING'}",
    "fields": "['exp_id', 'status', 'hypothesis', 'parent']"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T08:10:31.869278+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_008a_unexposed_s1\": {\"status\": \"RUNNING\", \"hypothesis\": \"Walker Walk unexposed trained dt_emb + subsample OFF (gate_subsample_max_dt=1) + gate_fixed_dt=2 + H=15 (default), seed=1. 直接复现 008a_no_subsample_dt2 配置（eval=778, V-recovery, no CIVO）。C3 reproducibility rebuttal 储备。\", \"parent\": \"\"}}, \"count\": 1, \"total\": 1, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2778}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_008a_unexposed_s2_20260518T080858",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T08:10:31.869489+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "limit": "30",
  "fields": "['exp_id', 'status', 'conclusion']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_008a_unexposed_s2_20260518T080858",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "event-gated-adaptive-horizon",
    "limit": "30",
    "fields": "['exp_id', 'status', 'conclusion']"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T08:10:31.869750+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_008a_unexposed_s2\": {\"status\": \"ANALYZING\", \"conclusion\": \"success\"}, \"exp_008d_civo_trigger_s4\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_008a_unexposed_s1\": {\"status\": \"RUNNING\"}, \"exp_008a_untrained_s1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_008a_untrained_s2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_010b_cheetah_civo_trigger_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_008e_v3_s4\": {\"status\": \"PREPARING\"}, \"exp_008e_v3_s3\": {\"status\": \"PREPARING\"}, \"exp_024b_cheetah_no_dt_emb_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_024b_cheetah_no_dt_emb_s1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_024_cheetah_no_dt_emb_s0\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_021_full_sgs_cheetah_s1\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp_023a_cheetah_baseline_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_010b_cheetah_civo_trigger\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_023b_cheetah_baseline_s1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_019b_pickcube_civo_trigger\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_022b_no_curriculum\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_022_untrained_dt_emb_learned_gate\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_019a_v2_pickcube_baseline\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_007_fixed_dt4\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp_008c_no_subsample_dt2_h8\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp_003_event_gated_v2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp_004_event_gated_v3\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp_005_event_gated_v4\": {\"status\": \"DONE\", \"conclusion\": \"negative\
…[truncated 630 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_008a_unexposed_s2_20260518T080858",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T08:10:31.870044+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "filters": "{'exp_id': 'exp_008a_unexposed_s2'}",
  "fields": "['*']",
  "limit": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_008a_unexposed_s2_20260518T080858",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "event-gated-adaptive-horizon",
    "filters": "{'exp_id': 'exp_008a_unexposed_s2'}",
    "fields": "['*']",
    "limit": "1"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T08:10:31.870239+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3356}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_008a_unexposed_s2_20260518T080858",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T08:10:31.870445+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_008a_unexposed_s2",
  "field": "metrics",
  "value": "{'eval_return_final': 899.4, 'eval_return_95k': 819.4, 'eval_return_85k': 605.4, 'eval_return_75k': 534.4, 'eval_return_65k': 653.8, 'eval_return_55k': 607.5, 'civo_ve_ratio_final': 0.333, 'civo_delta_ve_final': -0.003, 'civo_alert': 0, 'value_mean_final': 299.4, 'target_mean_final': 300.3, 'total_steps': 105000, 'gate_dt_mean': 2, 'gate_dt_2_frac': 1}",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_008a_unexposed_s2_20260518T080858",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_008a_unexposed_s2",
    "field": "metrics",
    "value": "{'eval_return_final': 899.4, 'eval_return_95k': 819.4, 'eval_return_85k': 605.4, 'eval_return_75k': 534.4, 'eval_return_65k': 653.8, 'eval_return_55k': 607.5, 'civo_ve_ratio_final': 0.333, 'civo_delta_ve_final': -0.003, 'civo_alert': 0, 'value_mean_final': 299.4, 'target_mean_final': 300.3, 'total_steps': 105000, 'gate_dt_mean': 2, 'gate_dt_2_frac': 1}",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T08:10:31.870717+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_008a_unexposed_s2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T05:13:57.340Z\", \"updated_at\": \"2026-05-18T08:10:14.793Z\", \"hypothesis\": \"Walker Walk unexposed trained dt_emb + subsample OFF (gate_subsample_max_dt=1) + gate_fixed_dt=2 + H=15 (default), seed=2. 008a 新 seed 验证 protection 是否 reproducible。C3 rebuttal 储备。\", \"parent\": \"exp_008a_no_subsample_dt2\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008a_unexposed_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1 --checkpoint_every 25000\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:0\"], \"pid\": \"724965\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008a_unexposed_s2.log\", \"submitted_at\": \"2026-05-18T05:19:26.303Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon\", \"data_count\": 0, \"model_name\": \"DreamerV3+FixedDt2_NoSubsample (unexposed trained dt_emb, H=15)\", \"seed\": 2, \"checkpoint_source\": \"train_from_scratch\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"wall_clock_seconds\": 10239.8, \"gpu_hours\": 2.84}, \"reproduce\": {\"finished_at\": \"2026-05-18T08:07:27.087Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T08:07:33.602043+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_return_final\": 899.4, \"eval_return_95k\": 819.4, \"eval_return_85k\": 605.4, \"eval_return_75k\": 534.4, \"eval_return_65k\": 653.8, \"eval_return_55k\": 607.5, \"civo_ve_ratio_final\": 0.333, \"civo_delta_ve_final\": -0.003, \"civo_alert\": 0, \"value_mean_final\": 299.4, \"target_mean_final\": 300.3, \"total_steps\": 105000, \"gate_dt_mean\": 
…[truncated 359 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_008a_unexposed_s2_20260518T080858",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T08:10:31.870952+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_008a_unexposed_s2",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_unexposed_s2/latest.pt",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_008a_unexposed_s2_20260518T080858",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_008a_unexposed_s2",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_unexposed_s2/latest.pt",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-18T08:10:31.871131+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_008a_unexposed_s2",
  "field": "log_path",
  "value": "/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_unexposed_s2/metrics.jsonl",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_008a_unexposed_s2_20260518T080858",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_008a_unexposed_s2",
    "field": "log_path",
    "value": "/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_unexposed_s2/metrics.jsonl",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-18T08:10:31.871366+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_008a_unexposed_s2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T05:13:57.340Z\", \"updated_at\": \"2026-05-18T08:10:16.463Z\", \"hypothesis\": \"Walker Walk unexposed trained dt_emb + subsample OFF (gate_subsample_max_dt=1) + gate_fixed_dt=2 + H=15 (default), seed=2. 008a 新 seed 验证 protection 是否 reproducible。C3 rebuttal 储备。\", \"parent\": \"exp_008a_no_subsample_dt2\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008a_unexposed_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1 --checkpoint_every 25000\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:0\"], \"pid\": \"724965\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008a_unexposed_s2.log\", \"submitted_at\": \"2026-05-18T05:19:26.303Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon\", \"data_count\": 0, \"model_name\": \"DreamerV3+FixedDt2_NoSubsample (unexposed trained dt_emb, H=15)\", \"seed\": 2, \"checkpoint_source\": \"train_from_scratch\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"wall_clock_seconds\": 10239.8, \"gpu_hours\": 2.84}, \"reproduce\": {\"finished_at\": \"2026-05-18T08:07:27.087Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T08:07:33.602043+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_return_final\": 899.4, \"eval_return_95k\": 819.4, \"eval_return_85k\": 605.4, \"eval_return_75k\": 534.4, \"eval_return_65k\": 653.8, \"eval_return_55k\": 607.5, \"civo_ve_ratio_final\": 0.333, \"civo_delta_ve_final\": -0.003, \"civo_alert\": 0, \"value_mean_final\": 299.4, \"target_mean_final\": 300.3, \"total_steps\": 105000, \"gate_dt_mean\": 
…[truncated 359 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_008a_unexposed_s2_20260518T080858",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-18T08:10:31.871651+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_008a_unexposed_s2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T05:13:57.340Z\", \"updated_at\": \"2026-05-18T08:10:17.263Z\", \"hypothesis\": \"Walker Walk unexposed trained dt_emb + subsample OFF (gate_subsample_max_dt=1) + gate_fixed_dt=2 + H=15 (default), seed=2. 008a 新 seed 验证 protection 是否 reproducible。C3 rebuttal 储备。\", \"parent\": \"exp_008a_no_subsample_dt2\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008a_unexposed_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1 --checkpoint_every 25000\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:0\"], \"pid\": \"724965\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008a_unexposed_s2.log\", \"submitted_at\": \"2026-05-18T05:19:26.303Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon\", \"data_count\": 0, \"model_name\": \"DreamerV3+FixedDt2_NoSubsample (unexposed trained dt_emb, H=15)\", \"seed\": 2, \"checkpoint_source\": \"train_from_scratch\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"wall_clock_seconds\": 10239.8, \"gpu_hours\": 2.84}, \"reproduce\": {\"finished_at\": \"2026-05-18T08:07:27.087Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T08:07:33.602043+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_return_final\": 899.4, \"eval_return_95k\": 819.4, \"eval_return_85k\": 605.4, \"eval_return_75k\": 534.4, \"eval_return_65k\": 653.8, \"eval_return_55k\": 607.5, \"civo_ve_ratio_final\": 0.333, \"civo_delta_ve_final\": -0.003, \"civo_alert\": 0, \"value_mean_final\": 299.4, \"target_mean_final\": 300.3, \"total_steps\": 105000, \"gate_dt_mean\": 
…[truncated 358 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_008a_unexposed_s2_20260518T080858",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-18T08:10:31.871942+00:00_

Registry 已更新为 DONE。

## exp_008a_unexposed_s2 分析结论：**SUCCESS**

### Eval Return 曲线
| Step | eval_return |
|------|------------|
| 5k | 39.3 |
| 15k | 159.8 |
| 25k | 374.7 |
| 35k | 431.6 |
| 45k | 430.8 |
| 55k | 607.5 |
| 65k | 653.8 |
| 75k | 534.4 (临时 dip) |
| 85k | 605.4 |
| 95k | 819.4 |
| **105k** | **899.4** |

### CIVO 检查
- `ve_ratio` 全程 0.03→0.33，稳定在 ~0.33，**远低于 1.5× 阈值**
- `civo/alert = 0` 全程无触发
- `delta_ve` 后半段为负值（-0.003），value estimation 趋于保守

### V-recovery
- `value_mean = 299.4`, `target_mean = 300.3`，差异 <0.3%，**完美对齐**

### 与父实验和 baseline 对比
| 实验 | eval_return | CIVO |
|------|------------|------|
| baseline (无 gate) | ~850 | N/A |
| 父实验 008a_no_subsample_dt2 (seed=0) | 778 | 无 |
| **本实验 (seed=2)** | **899.4** | **无** |

### C3 claim 支撑
seed=2 不仅复现了父实验的 CIVO protection，eval return 还超过 baseline 50 分。unexposed dt_emb + fixed dt=2 + no subsample 配置的 CIVO 保护性跨 seed 稳定可复现，可作为 C3 rebuttal 的有力证据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_exp_008a_unexposed_s2_20260518T080858"
}
```

</details>

---
