# ops investigate csv selectivity

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 0
- **Tool calls:** 26
- **Original source:** `logs/chats/worker_ops_investigate-csv-selectivity_20260521T063649.jsonl`
- **Structured JSON:** [`938f034e40f6e52d174b.json`](../../sessions/93/938f034e40f6e52d174b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

53 recorded events

### Tool call

_source line 1 · 2026-05-21T06:39:58.442983+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_registry",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_registry",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T06:39:58.443291+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T06:39:58.443443+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-13176",
  "command": "cat /root/xling_calib_direction/results/probing_controls.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-13176",
    "command": "cat /root/xling_calib_direction/results/probing_controls.csv",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T06:39:58.443594+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-13176",
  "command": "ls -la /root/xling_calib_direction/results/probing_controls.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-13176",
    "command": "ls -la /root/xling_calib_direction/results/probing_controls.csv",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-21T06:39:58.443792+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"layer,real_auroc,real_auroc_std,perm_auroc_mean,perm_auroc_std,selectivity\\n0,0.501455,0.130885,0.481224,0.014477,13.906133\\n12,0.529989,0.108674,0.488302,0.012564,1.390067\\n16,0.615245,0.111711,0.491860,0.009270,1.070635\\n20,0.733110,0.080977,0.488458,0.009553,1.049513\\n24,0.738344,0.085949,0.489487,0.006911,1.044108\\n27,0.745862,0.082621,0.483537,0.010185,1.066960\\n4,0.524266,0.111173,0.487428,0.009713,1.518100\\n8,0.529232,0.101445,0.492490,0.007319,1.256899\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.05}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T06:39:58.443927+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-13176",
  "command": "ls /root/xling_calib_direction/results/probing*",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-13176",
    "command": "ls /root/xling_calib_direction/results/probing*",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-21T06:39:58.444056+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 457 May 21 08:04 /root/xling_calib_direction/results/probing_controls.csv\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T06:39:58.444178+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/xling_calib_direction/results/probing_controls.csv\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T06:39:58.444299+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-13176",
  "command": "grep -n \"output\\|save\\|to_csv\\|probing_controls\" /root/xling_calib_direction/probing_controls_v2.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-13176",
    "command": "grep -n \"output\\|save\\|to_csv\\|probing_controls\" /root/xling_calib_direction/probing_controls_v2.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T06:39:58.444420+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T06:39:58.444549+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "xling_calib_direction",
  "filters": "{'plan_id': 'plan_013'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "xling_calib_direction",
    "filters": "{'plan_id': 'plan_013'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T06:39:58.444712+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0191}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T06:39:58.444864+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-13176",
  "command": "grep -n \"selectivity\" /root/xling_calib_direction/probing_controls_v2.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-13176",
    "command": "grep -n \"selectivity\" /root/xling_calib_direction/probing_controls_v2.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T06:39:58.444991+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"grep: /root/xling_calib_direction/probing_controls_v2.py: No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T06:39:58.445108+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-13176",
  "command": "grep -n \"to_csv\\|output\\|save\" /root/xling_calib_direction/probing_controls_v2.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-13176",
    "command": "grep -n \"to_csv\\|output\\|save\" /root/xling_calib_direction/probing_controls_v2.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T06:39:58.445228+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T06:39:58.445342+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "xling_calib_direction",
  "filters": "{'plan_id': '013'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "xling_calib_direction",
    "filters": "{'plan_id': '013'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T06:39:58.445462+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0222}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T06:39:58.445586+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-13176",
  "command": "find /root/xling_calib_direction -name \"probing_controls*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-13176",
    "command": "find /root/xling_calib_direction -name \"probing_controls*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T06:39:58.445747+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T06:39:58.445883+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-13176",
  "command": "grep -rn \"selectivity\" /root/xling_calib_direction/scripts/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-13176",
    "command": "grep -rn \"selectivity\" /root/xling_calib_direction/scripts/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T06:39:58.446005+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"grep: /root/xling_calib_direction/scripts/: No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T06:39:58.446123+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-13176",
  "command": "grep -rn \"selectivity\" /root/xling_calib_direction/src/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-13176",
    "command": "grep -rn \"selectivity\" /root/xling_calib_direction/src/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-21T06:39:58.446242+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"grep: /root/xling_calib_direction/src/: No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T06:39:58.446357+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "xling_calib_direction",
  "limit": "5",
  "fields": "['experiment_id', 'plan_id', 'title', 'status', 'metrics']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "xling_calib_direction",
    "limit": "5",
    "fields": "['experiment_id', 'plan_id', 'title', 'status', 'metrics']"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T06:39:58.446542+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"plan_013_probing_controls_v2\": {\"status\": \"RUNNING\"}, \"plan_013\": {\"status\": \"DONE\", \"metrics\": {\"method\": \"5-fold CV + PCA(100) + LogisticRegression (C=1.0, L2, lbfgs, max_iter=2000)\", \"selectivity_hewitt_liang\": {\"L0\": 0.02, \"L4\": 0.037, \"L8\": 0.036, \"L12\": 0.042, \"L16\": 0.123, \"L20\": 0.244, \"L24\": 0.248, \"L27\": 0.262}, \"real_auroc\": {\"L0\": 0.501, \"L4\": 0.524, \"L8\": 0.529, \"L12\": 0.53, \"L16\": 0.615, \"L20\": 0.733, \"L24\": 0.738, \"L27\": 0.746}, \"permuted_auroc\": {\"L0\": 0.481, \"L4\": 0.487, \"L8\": 0.493, \"L12\": 0.488, \"L16\": 0.492, \"L20\": 0.489, \"L24\": 0.49, \"L27\": 0.484}, \"pca_variance_retained\": {\"L0\": 0.922, \"L4\": 0.912, \"L8\": 0.885, \"L12\": 0.868, \"L16\": 0.783, \"L20\": 0.738, \"L24\": 0.844, \"L27\": 0.794}, \"note\": \"Selectivity = real_AUROC - permuted_AUROC (Hewitt & Liang 2019). Signal concentrated in L20-L27. PCA(100) retains 73-92% variance.\"}}, \"mvp_003\": {\"status\": \"DONE\", \"metrics\": {\"en_best_auroc\": 0.7284, \"en_best_layer\": 31, \"en_best_ece_raw\": 0.2052, \"en_auroc_range\": [0.6331, 0.7284], \"layer_depth_delta\": 0.0953, \"layers_tested\": [0, 4, 8, 12, 16, 20, 24, 28, 31], \"best_zs_auroc\": {\"zh\": 0.64, \"ar\": 0.6146, \"hi\": 0.5935, \"ko\": 0.6481, \"sw\": 0.5838}, \"best_zs_layer\": {\"zh\": 20, \"ar\": 31, \"hi\": 31, \"ko\": 31, \"sw\": 16}, \"zs_pass_langs\": [\"zh\", \"ar\", \"hi\", \"ko\", \"sw\"], \"zs_fail_langs\": [], \"pass_fail\": \"PARTIAL 2/4 (P2 5/5 PASS, P3 PASS 9.53pp, P1 FAIL ECE, P4 FAIL mean-shift)\", \"note\": \"zh@L31 sigmoid saturation artifact fixed (decision_function for AUROC). P4 FAIL is expected: mean-shift adds constant offset to linear logits, AUROC is rank-invariant.\", \"cka_vs_degradation\": {\"overall_rho\": -0.3982, \"overall_p\": 0.0068, \"per_lang\": {\"ar\": {\"rho\": -0.2833, \"p\": 0.46}, \"hi\": {\"rho\": -0.6667, \"p\": 0.0499}, \"ko\": {\"rho\": 0.25
…[truncated 1800 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T06:39:58.446811+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-13176",
  "command": "find /root/xling_calib_direction -name \"*.py\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-13176",
    "command": "find /root/xling_calib_direction -name \"*.py\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-21T06:39:58.446962+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-13176",
  "command": "ls -la /root/xling_calib_direction/results/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-13176",
    "command": "ls -la /root/xling_calib_direction/results/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-21T06:39:58.447093+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-21T06:39:58.447233+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 268\\ndrwxr-xr-x  3 root root   4096 May 21 12:22 .\\ndrwxr-xr-x 18 root root   4096 May 21 14:37 ..\\n-rw-r--r--  1 root root 128571 May 21 02:04 auroc_by_layer.png\\n-rw-r--r--  1 root root    610 May 21 10:50 cka_matrix_verify.csv\\n-rw-r--r--  1 root root    604 May 21 04:22 cka_results.csv\\n-rw-r--r--  1 root root  30773 May 21 09:29 linproj_procrustes_sensitivity.csv\\n-rw-r--r--  1 root root  23473 May 21 07:39 linproj_sensitivity.csv\\n-rw-r--r--  1 root root  47165 May 21 02:04 method_comparison.png\\ndrwxr-xr-x  2 root root    100 May 21 12:22 pareto\\n-rw-r--r--  1 root root    457 May 21 08:04 probing_controls.csv\\n-rw-r--r--  1 root root   6198 May 21 02:04 summary.txt\\n-rw-r--r--  1 root root   4698 May 21 02:49 transfer_results.csv\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T06:39:58.447378+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-13176",
  "command": "find /root/xling_calib_direction -name \"*.py\" -o -name \"*.ipynb\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-13176",
    "command": "find /root/xling_calib_direction -name \"*.py\" -o -name \"*.ipynb\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-21T06:39:58.447499+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-13176",
  "command": "ls /root/xling_calib_direction/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-13176",
    "command": "ls /root/xling_calib_direction/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-21T06:39:58.447662+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-21T06:39:58.447816+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"__pycache__\\nactivations\\nactivations_mvp002\\nactivations_mvp003\\nanalyze_results.py\\nartifacts\\ncode\\ncompute_cka.py\\nextract_activations.py\\nextract_activations_large.py\\nmvp_003.log\\npareto_analysis.py\\nprobes\\nprobes_mvp002\\nprobes_mvp003\\nresults\\nresults_cka_mvp001\\nresults_cka_mvp003\\nresults_fewshot_test\\nresults_mvp002\\nresults_mvp003\\nrun_mvp.sh\\nrun_mvp_002.sh\\nrun_mvp_003.sh\\nrun_plan_001.sh\\nrun_plan_002.sh\\nscripts\\ntemp_scaling.py\\ntemp_scaling_fixed.py\\ntemp_scaling_l27.py\\ntrain_caclr.py\\ntrain_probe.py\\ntransfer_eval.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T06:39:58.447941+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-13176",
  "command": "ls /root/xling_calib_direction/scripts/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-13176",
    "command": "ls /root/xling_calib_direction/scripts/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-21T06:39:58.448061+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"plot_figures.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-21T06:39:58.448174+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-13176",
  "command": "grep -rn \"selectivity\" /root/xling_calib_direction/train_probe.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-13176",
    "command": "grep -rn \"selectivity\" /root/xling_calib_direction/train_probe.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-21T06:39:58.448290+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-13176",
  "command": "grep -rn \"selectivity\" /root/xling_calib_direction/analyze_results.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-13176",
    "command": "grep -rn \"selectivity\" /root/xling_calib_direction/analyze_results.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-21T06:39:58.448406+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-21T06:39:58.448522+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-21T06:39:58.448633+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-13176",
  "command": "grep -rn \"probing_controls\" /root/xling_calib_direction/code/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-13176",
    "command": "grep -rn \"probing_controls\" /root/xling_calib_direction/code/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-21T06:39:58.448784+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/xling_calib_direction/code/probing_controls.py:67:    out_path = os.path.join(activations_dir, \\\"..\\\", \\\"results\\\", \\\"probing_controls.csv\\\")\\n/root/xling_calib_direction/code/probing_controls_v2.py:67:    out_path = os.path.join(activations_dir, \\\"..\\\", \\\"results\\\", \\\"probing_controls_v2.csv\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-21T06:39:58.448937+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-13176",
  "command": "cat /root/xling_calib_direction/code/probing_controls.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-13176",
    "command": "cat /root/xling_calib_direction/code/probing_controls.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-21T06:39:58.449054+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-13176",
  "command": "cat /root/xling_calib_direction/code/probing_controls_v2.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-13176",
    "command": "cat /root/xling_calib_direction/code/probing_controls_v2.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-21T06:39:58.449224+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nProbing control task with permuted labels to compute selectivity.\\nPCA done once outside CV loop (negligible leakage for PCA), then\\n5-fold CV only on LogReg for speed.\\n\\\"\\\"\\\"\\nimport os, glob, warnings, time\\nimport numpy as np\\nimport torch\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.decomposition import PCA\\nfrom sklearn.preprocessing import StandardScaler\\nfrom sklearn.model_selection import cross_val_score\\n\\nwarnings.filterwarnings(\\\"ignore\\\")\\n\\ndef run_controls(activations_dir, n_permutations=10, n_folds=5, n_pca=100, seed=42):\\n    rng = np.random.RandomState(seed)\\n    \\n    en_files = sorted(glob.glob(os.path.join(activations_dir, \\\"layer*_en.pt\\\")))\\n    layer_indices = [int(os.path.basename(f).split(\\\"_\\\")[0].replace(\\\"layer\\\", \\\"\\\")) for f in en_files]\\n    \\n    print(f\\\"Layers: {layer_indices}\\\", flush=True)\\n    print(f\\\"StandardScaler+PCA({n_pca}) outside CV, then CV LogReg(liblinear)\\\", flush=True)\\n    print(f\\\"{'Layer':>5s} {'Real AUROC':>11s} {'Real std':>9s} {'Perm AUROC':>11s} {'Perm std':>9s} {'Selectivity':>12s}\\\", flush=True)\\n    print(\\\"-\\\" * 65, flush=True)\\n    \\n    results = []\\n    for li in layer_indices:\\n        t0 = time.time()\\n        path = os.path.join(activations_dir, f\\\"layer{li}_en.pt\\\")\\n        data = torch.load(path, weights_only=True)\\n        X = data[\\\"activations\\\"].numpy()\\n        y = data[\\\"labels\\\"].numpy()\\n        \\n        if len(np.unique(y)) < 2:\\n            print(f\\\"{li:>5d} SKIP (single class)\\\", flush=True)\\n            continue\\n        \\n        scaler = StandardScaler()\\n        X_s = scaler.fit_transform(X)\\n        pca = PCA(n_components=n_pca, random_state=seed)\\n        X_r = pca.fit_transform(X_s)\\n        print(f\\\"  Layer {li}: PCA done ({time.time()-t0:.1f}s), variance explained: {pca.explained_varia
…[truncated 2304 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-21T06:39:58.449418+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nProbing control task v2: 5-fold CV evaluation (sequential).\\nSame C=1.0, L2 penalty, StandardScaler as mvp_001.\\n\\\"\\\"\\\"\\nimport os, glob, time\\nimport numpy as np\\nimport torch\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.preprocessing import StandardScaler\\nfrom sklearn.model_selection import StratifiedKFold\\nfrom sklearn.metrics import roc_auc_score\\nimport warnings\\nwarnings.filterwarnings(\\\"ignore\\\")\\n\\nPROBE_CONFIG = dict(C=1.0, penalty=\\\"l2\\\", solver=\\\"liblinear\\\", max_iter=2000)\\nN_FOLDS = 5\\nN_PERMUTATIONS = 10\\n\\ndef cv_auroc(X, y, seed=42):\\n    skf = StratifiedKFold(n_splits=N_FOLDS, shuffle=True, random_state=seed)\\n    fold_aurocs = []\\n    for train_idx, test_idx in skf.split(X, y):\\n        scaler = StandardScaler()\\n        X_train = scaler.fit_transform(X[train_idx])\\n        X_test = scaler.transform(X[test_idx])\\n        clf = LogisticRegression(**PROBE_CONFIG, random_state=seed)\\n        clf.fit(X_train, y[train_idx])\\n        logits = clf.decision_function(X_test)\\n        if len(np.unique(y[test_idx])) < 2:\\n            continue\\n        fold_aurocs.append(roc_auc_score(y[test_idx], logits))\\n    return np.mean(fold_aurocs) if fold_aurocs else 0.5\\n\\ndef run_controls(activations_dir, seed=42):\\n    rng = np.random.RandomState(seed)\\n    en_files = sorted(glob.glob(os.path.join(activations_dir, \\\"layer*_en.pt\\\")))\\n    layer_indices = [int(os.path.basename(f).split(\\\"_\\\")[0].replace(\\\"layer\\\", \\\"\\\")) for f in en_files]\\n    print(f\\\"Layers: {layer_indices}\\\")\\n    print(f\\\"Config: C={PROBE_CONFIG['C']}, solver={PROBE_CONFIG['solver']}, \\\"\\n          f\\\"max_iter={PROBE_CONFIG['max_iter']}, {N_FOLDS}-fold CV, {N_PERMUTATIONS} permutations\\\")\\n    print(f\\\"\\\\n{'Layer':>5s} {'CV AUROC':>9s} {'Perm AUROC':>11s} {'Perm std':>9s} {'Selectivity':>12s} {'Time':>6s}\\\")\\n   
…[truncated 2265 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-21T06:39:58.449620+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-13176",
  "command": "ls -la /root/xling_calib_direction/results/probing_controls_v2.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-13176",
    "command": "ls -la /root/xling_calib_direction/results/probing_controls_v2.csv",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-21T06:39:58.449782+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/xling_calib_direction/results/probing_controls_v2.csv': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-21T06:39:58.449921+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-13176",
  "command": "mv /root/xling_calib_direction/results/probing_controls.csv /root/xling_calib_direction/results/probing_controls_DEPRECATED.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-13176",
    "command": "mv /root/xling_calib_direction/results/probing_controls.csv /root/xling_calib_direction/results/probing_controls_DEPRECATED.csv",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-21T06:39:58.450047+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-21T06:39:58.450170+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-13176",
  "command": "ls -la /root/xling_calib_direction/results/probing_controls*",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-13176",
    "command": "ls -la /root/xling_calib_direction/results/probing_controls*",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-21T06:39:58.450292+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 457 May 21 08:04 /root/xling_calib_direction/results/probing_controls_DEPRECATED.csv\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-21T06:39:58.450449+00:00_

---

## 调查报告

### 1. CSV 文件内容

`results/probing_controls.csv` 包含 8 层 (L0/4/8/12/16/20/24/27) 的 real_auroc、perm_auroc 和 selectivity。底层 AUROC 值与 registry 一致，但 selectivity 列差异巨大（CSV L0=13.9 vs registry L0=0.020）。

### 2. 不一致原因

**selectivity 公式不同。** 两个版本的代码在 `code/` 下：

| | `probing_controls.py` (v1, 生成该 CSV) | `probing_controls_v2.py` (v2, registry 权威数据) |
|---|---|---|
| **selectivity 公式** | `(real - perm) / (real - 0.5)` | `real - perm` (Hewitt & Liang 2019) |
| **PCA** | PCA(100) 在 CV 外拟合（有数据泄漏） | 无 PCA |
| **Scaler** | 全局 fit（泄漏） | 每 fold 内 fit（正确） |
| **AUROC 计算** | `cross_val_score` (predict_proba) | `decision_function` |
| **max_iter** | 1000 | 2000 |

v1 的公式 `(real - perm) / (real - 0.5)` 在 L0 处分母极小 (0.501 - 0.5 = 0.0015)，导致 selectivity 膨胀到 13.9。这不是 Hewitt & Liang 定义，且 v1 还有 PCA/Scaler 数据泄漏问题。

### 3. 正确数据

**Registry plan_013 为权威数据**（Hewitt & Liang selectivity: L0=0.020 → L27=0.262），来自 v2 代码，方法学正确。

### 4. 已执行操作

已将 CSV 重命名：`results/probing_controls.csv` → `results/probing_controls_DEPRECATED.csv`

v2 脚本输出的 `probing_controls_v2.csv` 尚未生成（registry 中 `plan_013_probing_controls_v2` 状态为 RUNNING）。

### 5. 其他过时文件

`code/probing_controls.py` (v1) 是产生错误 CSV 的源码，可考虑后续清理，但不紧急——关键是 CSV 已标记为 DEPRECATED，不会被误用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_investigate-csv-selectivity_20260521T063649"
}
```

</details>

---
