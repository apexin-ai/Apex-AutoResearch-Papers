# analysis bjb1 crm long s42 r2 diagnosis

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 56
- **Recorded user turns:** 0
- **Tool calls:** 27
- **Original source:** `logs/chats/worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737.jsonl`
- **Structured JSON:** [`6e6adadfeae5a8f219f6.json`](../../sessions/6e/6e6adadfeae5a8f219f6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

56 recorded events

### Assistant

_source line 1 · 2026-05-26T12:17:50.774969+00:00_

Not logged in · Please run /login

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-26T12:22:36.557990+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__detect_image",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__detect_image",
    "max_results": "10"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-26T12:22:36.561560+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "ToolSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-26T12:22:36.561861+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "tail -50 /root/runs/acr-vla-conformal-refinement/pi05-crm-k2-long-s42-r2.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "tail -50 /root/runs/acr-vla-conformal-refinement/pi05-crm-k2-long-s42-r2.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-26T12:22:36.562095+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"tail: cannot open '/root/runs/acr-vla-conformal-refinement/pi05-crm-k2-long-s42-r2.log' for reading: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 1.2}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-26T12:22:36.563345+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "tail -50 /root/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s42-r2.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "tail -50 /root/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s42-r2.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-26T12:22:36.563677+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"tail: cannot open '/root/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s42-r2.log' for reading: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-26T12:22:36.563895+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "ls -la /root/acr-vla-conformal-refinement/logs/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "ls -la /root/acr-vla-conformal-refinement/logs/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-26T12:22:36.564297+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 22184\\ndrwxr-xr-x  3 root root    12288 May 26 20:09 .\\ndrwxr-xr-x 11 root root     4096 May 22 19:02 ..\\n-rw-r--r--  1 root root    11685 May 19 17:40 calibrate_spatial.log\\n-rw-r--r--  1 root root      554 May 19 17:40 calibrate_spatial_K10.json\\n-rw-r--r--  1 root root     3726 May 18 02:49 debug_openvla_gripper_fix.log\\n-rw-r--r--  1 root root     1805 May 18 02:34 debug_openvla_object_fix_verify.log\\n-rw-r--r--  1 root root     5221 May 20 20:35 eval-adaptive-k-spatial-p90-seed43.log\\n-rw-r--r--  1 root root     5220 May 20 22:53 eval-adaptive-k-spatial-p90-seed44.log\\n-rw-r--r--  1 root root     4531 May 21 01:19 eval-k20-obs-only-object-seed42.log\\n-rw-r--r--  1 root root     1920 May 20 19:04 eval-obs-only-goal-norm02-seed51.log\\n-rw-r--r--  1 root root     4541 May 21 03:15 eval-obs-only-object-norm003-seed44.log\\n-rw-r--r--  1 root root     1931 May 17 21:38 eval-obs-only-object-norm005-seed43.log\\n-rw-r--r--  1 root root     4538 May 21 03:16 eval-obs-only-object-norm005-seed44.log\\n-rw-r--r--  1 root root     3023 May 21 03:36 eval-obs-only-object-norm01-seed48.log\\n-rw-r--r--  1 root root     2123 May 18 01:41 eval-obs-only-object-norm02-k20-seed42.log\\n-rw-r--r--  1 root root     5159 May 20 22:40 eval-obs-only-spatial-norm02-seed48.log\\n-rw-r--r--  1 root root     1926 May 17 21:38 eval-perdof-object-norm02-seed45-r2.log\\n-rw-r--r--  1 root root     4404 May 21 01:30 eval-random-selection-object-seed46.log\\n-rw-r--r--  1 root root     4401 May 21 01:21 eval-random-selection-object-seed47.log\\n-rw-r--r--  1 root root     5033 May 20 22:43 eval-random-selection-spatial-seed42-r2.log\\n-rw-r--r--  1 root root     5033 May 21 03:02 eval-random-selection-spatial-seed42-r3.log\\n-rw-r--r--  1 root root     5027 May 20 20:27 eval-random-selection-spatial-seed42.log\\n-rw-r--r--  1 root root     5023 May 21 01:12 eval-random-selection-spatial-seed43.log\\n-rw-r--r--  1 root root
…[truncated 6401 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-26T12:22:36.564617+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "find /root -maxdepth 4 -name \"*crm-k2-long-s42*\" -o -name \"*crm_k2_long*s42*\" -o -name \"*adaptive-long-s42-r2*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "find /root -maxdepth 4 -name \"*crm-k2-long-s42*\" -o -name \"*crm_k2_long*s42*\" -o -name \"*adaptive-long-s42-r2*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-26T12:22:36.564840+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-26T12:22:36.565041+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "find /root/acr-vla-conformal-refinement/logs -name \"*long*s42*\" -o -name \"*long*seed42*r2*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "find /root/acr-vla-conformal-refinement/logs -name \"*long*s42*\" -o -name \"*long*seed42*r2*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-26T12:22:36.565247+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-26T12:22:36.565517+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "ls -la /root/runs/acr-vla-conformal-refinement/ 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "ls -la /root/runs/acr-vla-conformal-refinement/ 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-26T12:22:36.565723+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-26T12:22:36.565920+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "ls -la /root/runs/acr-vla-conformal-refinement/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "ls -la /root/runs/acr-vla-conformal-refinement/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-26T12:22:36.566337+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 1716\\ndrwxr-xr-x 2 root root   8192 May 26 18:18 .\\ndrwxr-xr-x 3 root root     50 May 13 19:57 ..\\n-rw-r--r-- 1 root root  21221 May 22 14:28 crm-loss-combined.log\\n-rw-r--r-- 1 root root  21031 May 22 14:23 crm-loss-conformal.log\\n-rw-r--r-- 1 root root  21230 May 22 14:25 crm-loss-mse-baseline.log\\n-rw-r--r-- 1 root root  21310 May 22 14:21 crm-loss-perdof.log\\n-rw-r--r-- 1 root root  13513 May 19 12:19 crm-lto-splitA-train-fixed.log\\n-rw-r--r-- 1 root root   7564 May 19 12:03 crm-lto-splitA-train.log\\n-rw-r--r-- 1 root root   2399 May 22 01:57 crm-pipeline-auto.log\\n-rw-r--r-- 1 root root     12 May 14 12:11 crm-train-k5.log\\n-rw-r--r-- 1 root root  84370 May 22 08:58 crm-train-pi05-object-full.log\\n-rw-r--r-- 1 root root  72072 May 22 09:09 crm-train-pi05-spatial-full.log\\n-rw-r--r-- 1 root root  34323 May 14 06:37 crm-train-v1.log\\n-rw-r--r-- 1 root root   5582 May 14 20:06 crm-train-v2-obs-only.log\\n-rw-r--r-- 1 root root   5404 May 14 19:53 crm-train-v2-perdof.log\\n-rw-r--r-- 1 root root   5554 May 14 19:52 crm-train-v2-scalar-unc.log\\n-rw-r--r-- 1 root root   2812 May 15 04:03 eval-acr-object-v3.log\\n-rw-r--r-- 1 root root   4420 May 16 16:57 eval-acr-object-v4-default-r2.log\\n-rw-r--r-- 1 root root   3776 May 14 07:31 eval-acr-spatial-v2.log\\n-rw-r--r-- 1 root root   3186 May 15 04:17 eval-acr-spatial-v3.log\\n-rw-r--r-- 1 root root     54 May 15 06:17 eval-acr-spatial-v4-default-r2.log\\n-rw-r--r-- 1 root root   3590 May 15 12:49 eval-acr-spatial-v4-obs-only-r2.log\\n-rw-r--r-- 1 root root   3269 May 15 18:15 eval-acr-spatial-v4-obs-only-r3.log\\n-rw-r--r-- 1 root root   2089 May 15 15:05 eval-acr-spatial-v4-obs-only-r3.log.bak\\n-rw-r--r-- 1 root root   4237 May 15 21:14 eval-acr-spatial-v4-scalar-r2.log\\n-rw-r--r-- 1 root root   2099 May 15 15:05 eval-acr-spatial-v4-scalar-r2.log.bak\\n-rw-r--r-- 1 root root   2637 May 15 12:57 eval-acr-spatial-v4-scalar.log\\n-rw-r--r-- 1
…[truncated 6425 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-26T12:22:36.566603+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "find /root -maxdepth 5 -name \"*pi05*crm*long*\" -o -name \"*pi05*adaptive*long*r2*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "find /root -maxdepth 5 -name \"*pi05*crm*long*\" -o -name \"*pi05*adaptive*long*r2*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-26T12:22:36.566815+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-26T12:22:36.567010+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "find /root -maxdepth 4 -name \"*long*\" -newer /root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_pi05_seed43_bjb1.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "find /root -maxdepth 4 -name \"*long*\" -newer /root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_pi05_seed43_bjb1.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-26T12:22:36.567220+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed42_pi05_K2.log\\n/root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed43_pi05_K2.log\\n/root/acr-vla-conformal-refinement/logs/eval_long_adaptive_pi05_seed42.log\\n/root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed42_pi05_K2.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_adaptive_pi05_seed42.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-26T12:22:36.567503+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "tail -80 /root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed42_pi05_K2.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "tail -80 /root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed42_pi05_K2.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-26T12:22:36.567839+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[robosuite WARNING] No private macro file found! (__init__.py:7)\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n[evaluate] args: {'benchmark': 'long', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt', 'n_rollouts': 20, 'max_steps': 300, 'seed': 42, 'K': 2, 'mode': 'crm_obs_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'openvla_oft_path': '/root/autodl-tmp/models/openvla-oft/object/', 'obs_dim': 2048, 'unified_obs_dim': 2088, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_long_crm_obs_only_norm0.05_seed42_pi05_K2.json', 'max_correction_norm': 0.05, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855, 'n_action_steps': 10}\\n[eval] Mode: crm_obs_only, benchmark: long\\n[eval] max_steps set to 520 for benchmark long\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\n✓ Loaded state dict from model.safetensors\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embe
…[truncated 6340 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-26T12:22:36.568082+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "tail -80 /root/acr-vla-conformal-refinement/logs/eval_long_adaptive_pi05_seed42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "tail -80 /root/acr-vla-conformal-refinement/logs/eval_long_adaptive_pi05_seed42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-26T12:22:36.568423+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[robosuite WARNING] No private macro file found! (__init__.py:7)\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n[evaluate] args: {'benchmark': 'long', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt', 'n_rollouts': 20, 'max_steps': 300, 'seed': 42, 'K': 2, 'mode': 'adaptive_conformal_crm', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'openvla_oft_path': '/root/autodl-tmp/models/openvla-oft/object/', 'obs_dim': 2048, 'unified_obs_dim': 2088, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_long_adaptive_pi05_seed42.json', 'max_correction_norm': 0.2, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.25, 'n_action_steps': 10}\\n[eval] Mode: adaptive_conformal_crm, benchmark: long\\n[eval] max_steps set to 520 for benchmark long\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\n✓ Loaded state dict from model.safetensors\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embed
…[truncated 6341 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-26T12:22:36.568856+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed42_pi05_K2.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed42_pi05_K2.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-26T12:22:36.569167+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"long\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.82,\\n  \\\"per_task\\\": {\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\": {\\n      \\\"success_rate\\\": 0.6,\\n      \\\"successes\\\": 12,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": {\\n      \\\"success_rate\\\": 0.3,\\n  
…[truncated 366 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-26T12:22:36.569444+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_long_adaptive_pi05_seed42.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_long_adaptive_pi05_seed42.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-26T12:22:36.569674+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'cat /root/acr-vla-conformal-refinement/logs/eval_long_adaptive_pi05_seed42.json'\\n\\nStdout:\\n\\n      \\\"triggered\\\": false,\\n      \\\"correction_norm\\\": 0.0,\\n      \\\"task_name\\\": \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\",\\n      \\\"rollout_idx\\\": 5\\n    },\\n    {\\n      \\\"uncertainty\\\": 0.04596541076898575,\\n      \\\"triggered\\\": false,\\n      \\\"correction_norm\\\": 0.0,\\n      \\\"task_name\\\": \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwa\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 41.79}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-26T12:22:36.569931+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'pi05-crm-k2-long-s42-r2'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'pi05-crm-k2-long-s42-r2'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-26T12:22:36.570138+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'pi05-adaptive-long-s42-r2'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'pi05-adaptive-long-s42-r2'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-26T12:22:36.570365+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.8798}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-26T12:22:36.570567+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.6414}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-26T12:22:36.570758+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'RUNNING'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'RUNNING'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-26T12:22:36.575786+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"westd-pi05-vla-only-long-s43-paired\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T12:00:43.452Z\", \"updated_at\": \"2026-05-26T12:16:24.617Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Long s43. westd same-server paired comparison (Blackwell). Complete Long VLA-only 3-seed coverage.\", \"server\": \"westd-49937\", \"gpu\": \"cuda:4\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-49937\", \"gpu\": \"cuda:4\", \"started_at\": \"2026-05-26T12:15:55.273Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark long --seed 43 --n_rollouts 20 --output_file logs/eval_long_vla_only_pi05_seed43_westd.json\\\"\", \"code_commit\": \"a594db578deeeeddc0ab068549e315c5a3bb4d6a\"}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark long --seed 43 --n_rollouts 20 --output_file logs/eval_long_vla_only_pi05_seed43_westd.json\\\"\", \"server\": \"westd-49937\", \"gpu\": [\"cuda:4\"], \"pid\": \"333252\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-long-s43-paired.log\", \"submitted_at\": \"2026-05-26T12:16:08.461Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"333252\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-long-s43-paired.log\"}, \"westd-pi05-vla-only-long-s42-paired\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T11:59:43.428Z\", \"updated_at\": \"2026-05-26T12:15:35.175Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Long s42. westd same-server paired comparison (Blackwell). Fills Table 2 Long VLA-only gap.\",
…[truncated 34142 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 5
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-26T12:22:36.576188+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-crm-k2-long-s42-r2",
  "field": "log_path",
  "value": "/root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed42_pi05_K2.log",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-crm-k2-long-s42-r2",
    "field": "log_path",
    "value": "/root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed42_pi05_K2.log",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-26T12:22:36.576449+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-crm-k2-long-s42-r2",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-crm-k2-long-s42-r2",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-26T12:22:36.576657+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-adaptive-long-s42-r2",
  "field": "log_path",
  "value": "/root/acr-vla-conformal-refinement/logs/eval_long_adaptive_pi05_seed42.log",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-adaptive-long-s42-r2",
    "field": "log_path",
    "value": "/root/acr-vla-conformal-refinement/logs/eval_long_adaptive_pi05_seed42.log",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-26T12:22:36.576856+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-adaptive-long-s42-r2",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-adaptive-long-s42-r2",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-26T12:22:36.577138+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-crm-k2-long-s42-r2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T03:44:17.432Z\", \"updated_at\": \"2026-05-26T12:20:05.005Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only on LIBERO-Long s42 (re-run after server restart). Tests whether CRM correction affects strong π0.5 baseline on long-horizon tasks.\", \"parent\": \"pi05-crm-k2-long-s42\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model pi05 --mode crm_obs_only --K 2 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark long --seed 42 --n_rollouts 20 --output_file logs/eval_long_crm_obs_only_norm0.05_seed42_pi05_K2.json\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:0\", \"pid\": 2558, \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-crm-k2-long-s42-r2.log\", \"submitted_at\": \"2026-05-26T10:38:03.332Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 42, \"model_name\": \"pi05\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Long 10 tasks x 20 rollouts\", \"wall_clock_seconds\": 6064.7, \"gpu_hours\": 1.68}, \"reproduce\": {\"finished_at\": \"2026-05-26T12:19:00.347Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-26T12:19:08.057Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-26T12:19:46.509550+00:00\"}]}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed42_pi05_K2.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.8194}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-26T12:22:36.577586+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-crm-k2-long-s42-r2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T03:44:17.432Z\", \"updated_at\": \"2026-05-26T12:20:13.619Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only on LIBERO-Long s42 (re-run after server restart). Tests whether CRM correction affects strong π0.5 baseline on long-horizon tasks.\", \"parent\": \"pi05-crm-k2-long-s42\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model pi05 --mode crm_obs_only --K 2 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark long --seed 42 --n_rollouts 20 --output_file logs/eval_long_crm_obs_only_norm0.05_seed42_pi05_K2.json\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:0\", \"pid\": 2558, \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-crm-k2-long-s42-r2.log\", \"submitted_at\": \"2026-05-26T10:38:03.332Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 42, \"model_name\": \"pi05\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Long 10 tasks x 20 rollouts\", \"wall_clock_seconds\": 6064.7, \"gpu_hours\": 1.68}, \"reproduce\": {\"finished_at\": \"2026-05-26T12:19:00.347Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-26T12:19:08.057Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-26T12:19:46.509550+00:00\"}]}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed42_pi05_K2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\"}}, \"error\": null, \"metadata\": {\"el
…[truncated 27 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-26T12:22:36.577895+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-adaptive-long-s42-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T03:44:44.161Z\", \"updated_at\": \"2026-05-26T12:20:25.665Z\", \"hypothesis\": \"π0.5 Adaptive Conformal on Long s42 (re-run after cqa1 crash). Cross-suite validation for π0.5 Table 2.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark long --seed 42 --n_rollouts 20 --output_file logs/eval_long_adaptive_pi05_seed42.json\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"pid\": 3764, \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s42-r2.log\", \"submitted_at\": \"2026-05-26T10:38:19.455Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 42, \"model_name\": \"pi05\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Long 10 tasks x 20 rollouts\"}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_adaptive_pi05_seed42.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 13.6966}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-26T12:22:36.578178+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-adaptive-long-s42-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T03:44:44.161Z\", \"updated_at\": \"2026-05-26T12:20:39.016Z\", \"hypothesis\": \"π0.5 Adaptive Conformal on Long s42 (re-run after cqa1 crash). Cross-suite validation for π0.5 Table 2.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark long --seed 42 --n_rollouts 20 --output_file logs/eval_long_adaptive_pi05_seed42.json\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"pid\": 3764, \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s42-r2.log\", \"submitted_at\": \"2026-05-26T10:38:19.455Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 42, \"model_name\": \"pi05\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Long 10 tasks x 20 rollouts\"}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_adaptive_pi05_seed42.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 15.7836}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-26T12:22:36.578518+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-crm-k2-long-s42-r2",
  "field": "metrics",
  "value": "{'success_rate': 0.82, 'successes': 164, 'total': 200, 'mode': 'crm_obs_only', 'K': 2, 'max_correction_norm': 0.05, 'benchmark': 'long', 'seed': 42}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-crm-k2-long-s42-r2",
    "field": "metrics",
    "value": "{'success_rate': 0.82, 'successes': 164, 'total': 200, 'mode': 'crm_obs_only', 'K': 2, 'max_correction_norm': 0.05, 'benchmark': 'long', 'seed': 42}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-26T12:22:36.578878+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-crm-k2-long-s42-r2",
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
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-crm-k2-long-s42-r2",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-26T12:22:36.579131+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-crm-k2-long-s42-r2",
  "field": "failure_reason",
  "value": "FALSE POSITIVE: cron auto-marked failed but eval actually completed successfully (82.0% on Long s42). Process exited naturally after writing JSON output at 12:14:34. JSON: eval_long_crm_obs_only_norm0.05_seed42_pi05_K2.json. Original cron miss likely due to tmux session ending after eval completion (not a crash).",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-crm-k2-long-s42-r2",
    "field": "failure_reason",
    "value": "FALSE POSITIVE: cron auto-marked failed but eval actually completed successfully (82.0% on Long s42). Process exited naturally after writing JSON output at 12:14:34. JSON: eval_long_crm_obs_only_norm0.05_seed42_pi05_K2.json. Original cron miss likely due to tmux session ending after eval completion (not a crash).",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-26T12:22:36.579434+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-crm-k2-long-s42-r2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T03:44:17.432Z\", \"updated_at\": \"2026-05-26T12:21:04.778Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only on LIBERO-Long s42 (re-run after server restart). Tests whether CRM correction affects strong π0.5 baseline on long-horizon tasks.\", \"parent\": \"pi05-crm-k2-long-s42\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model pi05 --mode crm_obs_only --K 2 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark long --seed 42 --n_rollouts 20 --output_file logs/eval_long_crm_obs_only_norm0.05_seed42_pi05_K2.json\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:0\", \"pid\": 2558, \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-crm-k2-long-s42-r2.log\", \"submitted_at\": \"2026-05-26T10:38:03.332Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 42, \"model_name\": \"pi05\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Long 10 tasks x 20 rollouts\", \"wall_clock_seconds\": 6064.7, \"gpu_hours\": 1.68}, \"reproduce\": {\"finished_at\": \"2026-05-26T12:19:00.347Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-26T12:19:08.057Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-26T12:19:46.509550+00:00\"}]}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed42_pi05_K2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"metrics\": {\"success_rate\": 0.82, 
…[truncated 211 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-26T12:22:36.579763+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-crm-k2-long-s42-r2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T03:44:17.432Z\", \"updated_at\": \"2026-05-26T12:21:15.968Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only on LIBERO-Long s42 (re-run after server restart). Tests whether CRM correction affects strong π0.5 baseline on long-horizon tasks.\", \"parent\": \"pi05-crm-k2-long-s42\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model pi05 --mode crm_obs_only --K 2 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark long --seed 42 --n_rollouts 20 --output_file logs/eval_long_crm_obs_only_norm0.05_seed42_pi05_K2.json\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:0\", \"pid\": 2558, \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-crm-k2-long-s42-r2.log\", \"submitted_at\": \"2026-05-26T10:38:03.332Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 42, \"model_name\": \"pi05\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Long 10 tasks x 20 rollouts\", \"wall_clock_seconds\": 6064.7, \"gpu_hours\": 1.68}, \"reproduce\": {\"finished_at\": \"2026-05-26T12:19:00.347Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-26T12:19:08.057Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-26T12:19:46.509550+00:00\"}]}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed42_pi05_K2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"metrics\": {\"success_rate\": 0.82,
…[truncated 212 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-26T12:22:36.580076+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-crm-k2-long-s42-r2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T03:44:17.432Z\", \"updated_at\": \"2026-05-26T12:21:30.251Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only on LIBERO-Long s42 (re-run after server restart). Tests whether CRM correction affects strong π0.5 baseline on long-horizon tasks.\", \"parent\": \"pi05-crm-k2-long-s42\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model pi05 --mode crm_obs_only --K 2 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark long --seed 42 --n_rollouts 20 --output_file logs/eval_long_crm_obs_only_norm0.05_seed42_pi05_K2.json\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:0\", \"pid\": 2558, \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-crm-k2-long-s42-r2.log\", \"submitted_at\": \"2026-05-26T10:38:03.332Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 42, \"model_name\": \"pi05\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Long 10 tasks x 20 rollouts\", \"wall_clock_seconds\": 6064.7, \"gpu_hours\": 1.68}, \"reproduce\": {\"finished_at\": \"2026-05-26T12:19:00.347Z\"}, \"failure_reason\": \"FALSE POSITIVE: cron auto-marked failed but eval actually completed successfully (82.0% on Long s42). Process exited naturally after writing JSON output at 12:14:34. JSON: eval_long_crm_obs_only_norm0.05_seed42_pi05_K2.json. Original cron miss likely due to tmux session ending after eval completion (not a crash).\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-26T12:19:08.057Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-26T12:19:46.50955
…[truncated 464 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-26T12:22:36.580370+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-adaptive-long-s42-r2",
  "field": "metrics",
  "value": "{'success_rate': 0.805, 'successes': 161, 'total': 200, 'mode': 'adaptive_conformal_crm', 'K': 2, 'max_correction_norm': 0.2, 'conformal_threshold': 0.25, 'trigger_rate': 0.039, 'mean_uncertainty': 0.087, 'benchmark': 'long', 'seed': 42}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-adaptive-long-s42-r2",
    "field": "metrics",
    "value": "{'success_rate': 0.805, 'successes': 161, 'total': 200, 'mode': 'adaptive_conformal_crm', 'K': 2, 'max_correction_norm': 0.2, 'conformal_threshold': 0.25, 'trigger_rate': 0.039, 'mean_uncertainty': 0.087, 'benchmark': 'long', 'seed': 42}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-26T12:22:36.580612+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-adaptive-long-s42-r2",
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
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-adaptive-long-s42-r2",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-26T12:22:36.580814+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-adaptive-long-s42-r2",
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
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-adaptive-long-s42-r2",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-26T12:22:36.581072+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-adaptive-long-s42-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T03:44:44.161Z\", \"updated_at\": \"2026-05-26T12:21:46.529Z\", \"hypothesis\": \"π0.5 Adaptive Conformal on Long s42 (re-run after cqa1 crash). Cross-suite validation for π0.5 Table 2.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark long --seed 42 --n_rollouts 20 --output_file logs/eval_long_adaptive_pi05_seed42.json\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"pid\": 3764, \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s42-r2.log\", \"submitted_at\": \"2026-05-26T10:38:19.455Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 42, \"model_name\": \"pi05\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Long 10 tasks x 20 rollouts\"}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_adaptive_pi05_seed42.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"metrics\": {\"success_rate\": 0.805, \"successes\": 161, \"total\": 200, \"mode\": \"adaptive_conformal_crm\", \"K\": 2, \"max_correction_norm\": 0.2, \"conformal_threshold\": 0.25, \"trigger_rate\": 0.039, \"mean_uncertainty\": 0.087, \"benchmark\": \"long\", \"seed\": 42}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 11.518}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-26T12:22:36.581400+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-adaptive-long-s42-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T03:44:44.161Z\", \"updated_at\": \"2026-05-26T12:21:57.777Z\", \"hypothesis\": \"π0.5 Adaptive Conformal on Long s42 (re-run after cqa1 crash). Cross-suite validation for π0.5 Table 2.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark long --seed 42 --n_rollouts 20 --output_file logs/eval_long_adaptive_pi05_seed42.json\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"pid\": 3764, \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s42-r2.log\", \"submitted_at\": \"2026-05-26T10:38:19.455Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 42, \"model_name\": \"pi05\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Long 10 tasks x 20 rollouts\"}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_adaptive_pi05_seed42.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"metrics\": {\"success_rate\": 0.805, \"successes\": 161, \"total\": 200, \"mode\": \"adaptive_conformal_crm\", \"K\": 2, \"max_correction_norm\": 0.2, \"conformal_threshold\": 0.25, \"trigger_rate\": 0.039, \"mean_uncertainty\": 0.087, \"benchmark\": \"long\", \"seed\": 42}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 11.368}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-26T12:22:36.581740+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-adaptive-long-s42-r2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T03:44:44.161Z\", \"updated_at\": \"2026-05-26T12:22:08.789Z\", \"hypothesis\": \"π0.5 Adaptive Conformal on Long s42 (re-run after cqa1 crash). Cross-suite validation for π0.5 Table 2.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark long --seed 42 --n_rollouts 20 --output_file logs/eval_long_adaptive_pi05_seed42.json\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"pid\": 3764, \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s42-r2.log\", \"submitted_at\": \"2026-05-26T10:38:19.455Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 42, \"model_name\": \"pi05\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Long 10 tasks x 20 rollouts\", \"wall_clock_seconds\": 6229.3, \"gpu_hours\": 1.73}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_adaptive_pi05_seed42.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"metrics\": {\"success_rate\": 0.805, \"successes\": 161, \"total\": 200, \"mode\": \"adaptive_conformal_crm\", \"K\": 2, \"max_correction_norm\": 0.2, \"conformal_threshold\": 0.25, \"trigger_rate\": 0.039, \"mean_uncertainty\": 0.087, \"benchmark\": \"long\", \"seed\": 42}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-26T12:22:08.789Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 20.2583}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 56 · 2026-05-26T12:22:36.582063+00:00_

Both experiments diagnosed and registry updated.

## 诊断结果

**两个实验都已成功完成，cron 误报为 failed（实际是 tmux session 在 eval 自然退出后结束）。**

### pi05-crm-k2-long-s42-r2 ✅ success
- 模式: `crm_obs_only`, K=2, max_correction_norm=0.05
- **Overall success rate: 82.0% (164/200)** on LIBERO-Long s42
- 日志: `/root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed42_pi05_K2.log`
- JSON: `eval_long_crm_obs_only_norm0.05_seed42_pi05_K2.json`（已写盘）
- 之前被 cron 自动标 failed（"process dead 5× with no sentinel/W&B"），已修正 conclusion=success 并记录原因到 failure_reason 字段

### pi05-adaptive-long-s42-r2 ✅ success
- 模式: `adaptive_conformal_crm`, K=2, τ=0.25, max_correction_norm=0.2
- **Overall success rate: 80.5% (161/200)** on LIBERO-Long s42
- 触发率 trigger_rate=3.9%, mean_uncertainty=0.087
- 日志: `/root/acr-vla-conformal-refinement/logs/eval_long_adaptive_pi05_seed42.log`
- JSON: `eval_long_adaptive_pi05_seed42.json`（已写盘）
- 注册表已从 RUNNING → DONE/success

### 关键观察
- CRM K=2 (82.0%) **微优于** Adaptive (80.5%) on Long s42，触发率仅 3.9%（adaptive 几乎从不修正）
- 两个进程都跑了 ~6000+ 秒（wall_clock），正常退出
- **cron 误报根因**：tmux session 在 Python 进程退出后随之消失，cron 检测 pid 时已没了 → 误判 dead。建议未来 eval 任务写 sentinel 文件标识正常完成

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737"
}
```

</details>

---
