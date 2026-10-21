# analysis exp 010a final

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_analysis_exp_010a_final_20260516T120029.jsonl`
- **Structured JSON:** [`9335a4e2f314fa310169.json`](../../sessions/93/9335a4e2f314fa310169.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-16T12:01:18.919025+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_010a_final_20260516T120029",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T12:01:18.919387+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_010a_final_20260516T120029",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T12:01:18.919572+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-45299",
  "command": "tail -100 ~/runs/event-gated-adaptive-horizon/exp_010a_cheetah_baseline_s1.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_010a_final_20260516T120029",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-45299",
    "command": "tail -100 ~/runs/event-gated-adaptive-horizon/exp_010a_cheetah_baseline_s1.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-16T12:01:18.919707+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-45299",
  "command": "ls -la /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010a_cheetah_baseline_s1/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_010a_final_20260516T120029",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-45299",
    "command": "ls -la /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010a_cheetah_baseline_s1/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-16T12:01:18.919988+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[488000] dataset_size 244000.0 / train_return 749.7 / train_length 500.0 / train_episodes 488.0\\n[488000] dataset_size 244000.0 / train_return 796.1 / train_length 500.0 / train_episodes 488.0\\n[488000] dataset_size 244000.0 / train_return 839.5 / train_length 500.0 / train_episodes 488.0\\n[492000] dataset_size 246000.0 / train_return 743.2 / train_length 500.0 / train_episodes 492.0\\n[492000] dataset_size 246000.0 / train_return 817.7 / train_length 500.0 / train_episodes 492.0\\n[492000] dataset_size 246000.0 / train_return 812.3 / train_length 500.0 / train_episodes 492.0\\n[492000] dataset_size 246000.0 / train_return 674.9 / train_length 500.0 / train_episodes 492.0\\n[495000] \\nStart evaluation.\\n  [DBG] iter=100 step=396 ep=0/10 done=[False False False False] t=2.8s\\n  [DBG] iter=200 step=796 ep=0/10 done=[False False False False] t=5.4s\\n  [DBG] iter=300 step=1196 ep=0/10 done=[False False False False] t=8.0s\\n  [DBG] iter=400 step=1596 ep=0/10 done=[False False False False] t=10.6s\\n  [DBG] iter=500 step=1996 ep=0/10 done=[False False False False] t=13.3s\\n  [DBG] iter=600 step=2396 ep=4/10 done=[False False False False] t=16.2s\\n  [DBG] iter=700 step=2796 ep=4/10 done=[False False False False] t=18.9s\\n  [DBG] iter=800 step=3196 ep=4/10 done=[False False False False] t=21.8s\\n  [DBG] iter=900 step=3596 ep=4/10 done=[False False False False] t=24.6s\\n  [DBG] iter=1000 step=3996 ep=4/10 done=[False False False False] t=27.5s\\n  [DBG] iter=1100 step=4396 ep=8/10 done=[False False False False] t=30.4s\\n  [DBG] iter=1200 step=4796 ep=8/10 done=[False False False False] t=33.4s\\n  [DBG] iter=1300 step=5196 ep=8/10 done=[False False False False] t=36.1s\\n  [DBG] iter=1400 step=5596 ep=8/10 done=[False False False False] t=38.8s\\n  [DBG] iter=1500 step=5996 ep=8/10 done=[False False False False] t=41.4s\\n[495000] eval_return 844.3 / eval_length 500.0 / eval_episodes 10.0\\nStart training.
…[truncated 6369 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_010a_final_20260516T120029",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T12:01:18.920200+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 224368\\ndrwxr-xr-x  4 root root       185 May 16 07:08 .\\ndrwxr-xr-x 41 root root      4096 May 16 17:50 ..\\ndrwxr-xr-x  2 root root     49152 May 16 19:44 eval_eps\\n-rw-r--r--  1 root root    268912 May 16 19:57 events.out.tfevents.1778885289.autodl-container-k9z16fn7md-3a522761.536895.0\\n-rw-r--r--  1 root root 229192098 May 16 19:58 latest.pt\\n-rw-r--r--  1 root root    148060 May 16 19:57 metrics.jsonl\\ndrwxr-xr-x  2 root root     40960 May 16 19:57 train_eps\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_010a_final_20260516T120029",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T12:01:18.920371+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-45299",
  "command": "grep \"eval_return\" ~/runs/event-gated-adaptive-horizon/exp_010a_cheetah_baseline_s1.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_010a_final_20260516T120029",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-45299",
    "command": "grep \"eval_return\" ~/runs/event-gated-adaptive-horizon/exp_010a_cheetah_baseline_s1.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T12:01:18.920546+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[5000] eval_return 11.6 / eval_length 500.0 / eval_episodes 10.0\\n[15000] eval_return 18.1 / eval_length 500.0 / eval_episodes 10.0\\n[25000] eval_return 177.8 / eval_length 500.0 / eval_episodes 10.0\\n[35000] eval_return 303.6 / eval_length 500.0 / eval_episodes 10.0\\n[45000] eval_return 358.3 / eval_length 500.0 / eval_episodes 10.0\\n[55000] eval_return 212.2 / eval_length 500.0 / eval_episodes 10.0\\n[65000] eval_return 330.6 / eval_length 500.0 / eval_episodes 10.0\\n[75000] eval_return 377.6 / eval_length 500.0 / eval_episodes 10.0\\n[85000] eval_return 403.5 / eval_length 500.0 / eval_episodes 10.0\\n[95000] eval_return 390.0 / eval_length 500.0 / eval_episodes 10.0\\n[105000] eval_return 420.7 / eval_length 500.0 / eval_episodes 10.0\\n[115000] eval_return 546.7 / eval_length 500.0 / eval_episodes 10.0\\n[125000] eval_return 567.6 / eval_length 500.0 / eval_episodes 10.0\\n[135000] eval_return 416.9 / eval_length 500.0 / eval_episodes 10.0\\n[145000] eval_return 485.8 / eval_length 500.0 / eval_episodes 10.0\\n[155000] eval_return 592.6 / eval_length 500.0 / eval_episodes 10.0\\n[165000] eval_return 583.0 / eval_length 500.0 / eval_episodes 10.0\\n[175000] eval_return 558.8 / eval_length 500.0 / eval_episodes 10.0\\n[185000] eval_return 655.7 / eval_length 500.0 / eval_episodes 10.0\\n[195000] eval_return 640.9 / eval_length 500.0 / eval_episodes 10.0\\n[205000] eval_return 697.0 / eval_length 500.0 / eval_episodes 10.0\\n[215000] eval_return 517.0 / eval_length 500.0 / eval_episodes 10.0\\n[225000] eval_return 610.7 / eval_length 500.0 / eval_episodes 10.0\\n[235000] eval_return 542.5 / eval_length 500.0 / eval_episodes 10.0\\n[245000] eval_return 663.7 / eval_length 500.0 / eval_episodes 10.0\\n[255000] eval_return 624.4 / eval_length 500.0 / eval_episodes 10.0\\n[265000] eval_return 732.9 / eval_length 500.0 / eval_episodes 10.0\\n[275000] eval_return 708.1 / eval_length 500.0 / eval_episodes 10.0
…[truncated 1787 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_010a_final_20260516T120029",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T12:01:18.920694+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-45299",
  "command": "grep \"wandb\" ~/runs/event-gated-adaptive-horizon/exp_010a_cheetah_baseline_s1.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_010a_final_20260516T120029",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-45299",
    "command": "grep \"wandb\" ~/runs/event-gated-adaptive-horizon/exp_010a_cheetah_baseline_s1.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T12:01:18.920842+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_010a_final_20260516T120029",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T12:01:18.921018+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_010a_cheetah_baseline_s1",
  "field": "metrics",
  "value": "{'final_step': 524000, 'eval_return_final': 849.8, 'eval_return_final_step': 515000, 'eval_return_peak': 849.8, 'eval_return_peak_step': 515000, 'train_return_last': 716, 'total_eval_episodes': 52}",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_010a_final_20260516T120029",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_010a_cheetah_baseline_s1",
    "field": "metrics",
    "value": "{'final_step': 524000, 'eval_return_final': 849.8, 'eval_return_final_step': 515000, 'eval_return_peak': 849.8, 'eval_return_peak_step': 515000, 'train_return_last': 716, 'total_eval_episodes': 52}",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T12:01:18.921211+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_010a_cheetah_baseline_s1\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:17:27.101Z\", \"updated_at\": \"2026-05-16T12:01:08.934Z\", \"hypothesis\": \"Cheetah Run baseline seed 1 — 建立第二环境 dt=1 参考基线，为跨环境验证 C1/C2 做准备（plan_020）\", \"notes\": \"Director 排期: cuda:0 上排在 009d 之后。\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010a_cheetah_baseline_s1/checkpoint.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010a_cheetah_baseline_s1\"}, \"server\": \"bjb1-45299\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-45299\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T22:48:05.456Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_010a_cheetah_baseline_s1 --steps 512000 --seed 1 --compile False --device cuda:0\\\"\", \"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"finished_at\": \"2026-05-16T11:59:09.914Z\", \"training_hours\": 13.18}, \"pid\": \"536890\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_010a_cheetah_baseline_s1.log\", \"metrics\": {\"final_step\": 524000, \"eval_return_final\": 849.8, \"eval_return_final_step\": 515000, \"eval_return_peak\": 849.8, \"eval_return_peak_step\": 515000, \"train_return_last\": 716, \"total_eval_episodes\": 52}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T11:59:12.312213+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T12:01:01.080Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4428}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_010a_final_20260516T120029",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T12:01:18.921364+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_010a_cheetah_baseline_s1",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010a_cheetah_baseline_s1/latest.pt",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_010a_final_20260516T120029",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_010a_cheetah_baseline_s1",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010a_cheetah_baseline_s1/latest.pt",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T12:01:18.921531+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_010a_cheetah_baseline_s1\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:17:27.101Z\", \"updated_at\": \"2026-05-16T12:01:10.322Z\", \"hypothesis\": \"Cheetah Run baseline seed 1 — 建立第二环境 dt=1 参考基线，为跨环境验证 C1/C2 做准备（plan_020）\", \"notes\": \"Director 排期: cuda:0 上排在 009d 之后。\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010a_cheetah_baseline_s1/checkpoint.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010a_cheetah_baseline_s1\"}, \"server\": \"bjb1-45299\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-45299\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T22:48:05.456Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_010a_cheetah_baseline_s1 --steps 512000 --seed 1 --compile False --device cuda:0\\\"\", \"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"finished_at\": \"2026-05-16T11:59:09.914Z\", \"training_hours\": 13.18}, \"pid\": \"536890\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_010a_cheetah_baseline_s1.log\", \"metrics\": {\"final_step\": 524000, \"eval_return_final\": 849.8, \"eval_return_final_step\": 515000, \"eval_return_peak\": 849.8, \"eval_return_peak_step\": 515000, \"train_return_last\": 716, \"total_eval_episodes\": 52}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T11:59:12.312213+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T12:01:01.080Z\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010a_cheetah_b
…[truncated 87 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_010a_final_20260516T120029",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T12:01:18.921682+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_010a_cheetah_baseline_s1",
  "field": "log_path",
  "value": "~/runs/event-gated-adaptive-horizon/exp_010a_cheetah_baseline_s1.log",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_010a_final_20260516T120029",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_010a_cheetah_baseline_s1",
    "field": "log_path",
    "value": "~/runs/event-gated-adaptive-horizon/exp_010a_cheetah_baseline_s1.log",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T12:01:18.921868+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_010a_cheetah_baseline_s1\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:17:27.101Z\", \"updated_at\": \"2026-05-16T12:01:11.169Z\", \"hypothesis\": \"Cheetah Run baseline seed 1 — 建立第二环境 dt=1 参考基线，为跨环境验证 C1/C2 做准备（plan_020）\", \"notes\": \"Director 排期: cuda:0 上排在 009d 之后。\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010a_cheetah_baseline_s1/checkpoint.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010a_cheetah_baseline_s1\"}, \"server\": \"bjb1-45299\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-45299\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T22:48:05.456Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_010a_cheetah_baseline_s1 --steps 512000 --seed 1 --compile False --device cuda:0\\\"\", \"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"finished_at\": \"2026-05-16T11:59:09.914Z\", \"training_hours\": 13.18}, \"pid\": \"536890\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_010a_cheetah_baseline_s1.log\", \"metrics\": {\"final_step\": 524000, \"eval_return_final\": 849.8, \"eval_return_final_step\": 515000, \"eval_return_peak\": 849.8, \"eval_return_peak_step\": 515000, \"train_return_last\": 716, \"total_eval_episodes\": 52}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T11:59:12.312213+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T12:01:01.080Z\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010a_cheetah_b
…[truncated 89 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_010a_final_20260516T120029",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-16T12:01:18.922092+00:00_

Registry 已更新。总结：

**exp_010a_cheetah_baseline_s1 — 完成**

| 指标 | 值 |
|------|-----|
| 最终 step | 524,000 |
| 最终 eval_return | **849.8** (step 515K) |
| 峰值 eval_return | **849.8** (step 515K) |
| 训练时长 | 13.18 小时 |
| 退出状态 | 正常 (EXIT_CODE=0) |
| Checkpoint | `latest.pt` (219MB) |
| W&B | 无 |

结果优秀——849.8 完全在 DreamerV3 参考水平（800-900@500K）内，作为 Cheetah Run 的 dt=1 baseline 非常扎实。学习曲线稳定上升，300K 后进入 700+ 区间，500K 附近稳定在 830-850。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_exp_010a_final_20260516T120029"
}
```

</details>

---
