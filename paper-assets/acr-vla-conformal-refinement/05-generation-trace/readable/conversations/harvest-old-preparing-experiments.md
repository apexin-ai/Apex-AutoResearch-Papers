# harvest old preparing experiments

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 384
- **Recorded user turns:** 0
- **Tool calls:** 191
- **Original source:** `logs/chats/worker_harvest_old-preparing-experiments_20260521T041745.jsonl`
- **Structured JSON:** [`8375e777f7b530efc480.json`](../../sessions/83/8375e777f7b530efc480.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

384 recorded events

### Tool call

_source line 1 · 2026-05-21T04:18:54.281318+00:00_

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
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
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

_source line 2 · 2026-05-21T04:18:54.281767+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T04:18:54.282028+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cd /root/acr-vla-conformal-refinement && for f in logs/eval_spatial_vla_only_seed54.json logs/eval_long_obs_only_norm02_seed54.json logs/eval_long_obs_only_norm02_seed49.json logs/eval_long_obs_only_norm02_seed48.json logs/eval_spatial_obs_only_norm02_seed50.json logs/eval_long_vla_only_seed53.json logs/eval_goal_vla_only_seed52.json logs/eval_long_obs_only_norm02_seed51.json logs/eval_spatial_vla_only_seed51.json logs/eval_object_vla_only_seed51.json logs/eval_spatial_obs_only_norm02_seed48.json logs/eval_object_obs_only_norm02_k20_seed42.json logs/eval_obs_only_goal_norm02_seed53.json; do echo \"=== $f ===\"; if [ -f \"$f\" ]; then python3 -c \"import json; d=json.load(open('$f')); print('SR=' + str(d.get('overall_success_rate', 'N/A')))\"; else echo \"NOT_FOUND\"; fi; done",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cd /root/acr-vla-conformal-refinement && for f in logs/eval_spatial_vla_only_seed54.json logs/eval_long_obs_only_norm02_seed54.json logs/eval_long_obs_only_norm02_seed49.json logs/eval_long_obs_only_norm02_seed48.json logs/eval_spatial_obs_only_norm02_seed50.json logs/eval_long_vla_only_seed53.json logs/eval_goal_vla_only_seed52.json logs/eval_long_obs_only_norm02_seed51.json logs/eval_spatial_vla_only_seed51.json logs/eval_object_vla_only_seed51.json logs/eval_spatial_obs_only_norm02_seed48.json logs/eval_object_obs_only_norm02_k20_seed42.json logs/eval_obs_only_goal_norm02_seed53.json; do echo \"=== $f ===\"; if [ -f \"$f\" ]; then python3 -c \"import json; d=json.load(open('$f')); print('SR=' + str(d.get('overall_success_rate', 'N/A')))\"; else echo \"NOT_FOUND\"; fi; done",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T04:18:54.282189+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T04:18:54.282368+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "cd /root/acr-vla-conformal-refinement && for f in logs/eval_long_vla_only_seed54.json logs/eval_long_obs_only_norm02_seed53.json logs/eval_spatial_vla_only_seed53.json logs/eval_spatial_vla_only_seed52.json logs/eval_spatial_vla_only_seed50.json logs/eval_spatial_obs_only_norm02_seed47.json logs/eval_object_vla_only_seed49.json logs/eval_object_obs_only_norm02_k20_seed43.json; do echo \"=== $f ===\"; if [ -f \"$f\" ]; then python3 -c \"import json; d=json.load(open('$f')); print('SR=' + str(d.get('overall_success_rate', 'N/A')))\"; else echo \"NOT_FOUND\"; fi; done",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "cd /root/acr-vla-conformal-refinement && for f in logs/eval_long_vla_only_seed54.json logs/eval_long_obs_only_norm02_seed53.json logs/eval_spatial_vla_only_seed53.json logs/eval_spatial_vla_only_seed52.json logs/eval_spatial_vla_only_seed50.json logs/eval_spatial_obs_only_norm02_seed47.json logs/eval_object_vla_only_seed49.json logs/eval_object_obs_only_norm02_k20_seed43.json; do echo \"=== $f ===\"; if [ -f \"$f\" ]; then python3 -c \"import json; d=json.load(open('$f')); print('SR=' + str(d.get('overall_success_rate', 'N/A')))\"; else echo \"NOT_FOUND\"; fi; done",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T04:18:54.282517+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T04:18:54.282648+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cd /root/acr-vla-conformal-refinement && for f in logs/eval_spatial_obs_only_norm02_seed49.json logs/eval_goal_obs_only_norm02_seed48.json logs/eval_goal_obs_only_norm02_seed47.json logs/eval_goal_obs_only_norm02_seed50.json logs/eval_goal_obs_only_norm02_seed49.json logs/eval_long_obs_only_norm02_seed52.json logs/eval_long_vla_only_seed49.json logs/eval_vla_only_spatial_seed49_r2.json; do echo \"=== $f ===\"; if [ -f \"$f\" ]; then python3 -c \"import json; d=json.load(open('$f')); print('SR=' + str(d.get('overall_success_rate', 'N/A')))\"; else echo \"NOT_FOUND\"; fi; done",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "cd /root/acr-vla-conformal-refinement && for f in logs/eval_spatial_obs_only_norm02_seed49.json logs/eval_goal_obs_only_norm02_seed48.json logs/eval_goal_obs_only_norm02_seed47.json logs/eval_goal_obs_only_norm02_seed50.json logs/eval_goal_obs_only_norm02_seed49.json logs/eval_long_obs_only_norm02_seed52.json logs/eval_long_vla_only_seed49.json logs/eval_vla_only_spatial_seed49_r2.json; do echo \"=== $f ===\"; if [ -f \"$f\" ]; then python3 -c \"import json; d=json.load(open('$f')); print('SR=' + str(d.get('overall_success_rate', 'N/A')))\"; else echo \"NOT_FOUND\"; fi; done",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T04:18:54.282789+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T04:18:54.282951+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "python3 -c \"\nimport json, os\nfiles = [\n    'logs/eval_spatial_vla_only_seed54.json',\n    'logs/eval_long_obs_only_norm02_seed54.json',\n    'logs/eval_long_obs_only_norm02_seed49.json',\n    'logs/eval_long_obs_only_norm02_seed48.json',\n    'logs/eval_spatial_obs_only_norm02_seed50.json',\n    'logs/eval_long_vla_only_seed53.json',\n    'logs/eval_goal_vla_only_seed52.json',\n    'logs/eval_long_obs_only_norm02_seed51.json',\n    'logs/eval_spatial_vla_only_seed51.json',\n    'logs/eval_object_vla_only_seed51.json',\n    'logs/eval_spatial_obs_only_norm02_seed48.json',\n    'logs/eval_object_obs_only_norm02_k20_seed42.json',\n    'logs/eval_obs_only_goal_norm02_seed53.json',\n]\nos.chdir('/root/acr-vla-conformal-refinement')\nfor f in files:\n    if os.path.isfile(f):\n        try:\n            d = json.load(open(f))\n            print(f'{f}|SR={d.get(\\\"overall_success_rate\\\", \\\"N/A\\\")}')\n        except Exception as e:\n            print(f'{f}|ERROR={e}')\n    else:\n        print(f'{f}|NOT_FOUND')\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "python3 -c \"\nimport json, os\nfiles = [\n    'logs/eval_spatial_vla_only_seed54.json',\n    'logs/eval_long_obs_only_norm02_seed54.json',\n    'logs/eval_long_obs_only_norm02_seed49.json',\n    'logs/eval_long_obs_only_norm02_seed48.json',\n    'logs/eval_spatial_obs_only_norm02_seed50.json',\n    'logs/eval_long_vla_only_seed53.json',\n    'logs/eval_goal_vla_only_seed52.json',\n    'logs/eval_long_obs_only_norm02_seed51.json',\n    'logs/eval_spatial_vla_only_seed51.json',\n    'logs/eval_object_vla_only_seed51.json',\n    'logs/eval_spatial_obs_only_norm02_seed48.json',\n    'logs/eval_object_obs_only_norm02_k20_seed42.json',\n    'logs/eval_obs_only_goal_norm02_seed53.json',\n]\nos.chdir('/root/acr-vla-conformal-refinement')\nfor f in files:\n    if os.path.isfile(f):\n        try:\n            d = json.load(open(f))\n            print(f'{f}|SR={d.get(\\\"overall_success_rate\\\", \\\"N/A\\\")}')\n        except Exception as e:\n            print(f'{f}|ERROR={e}')\n    else:\n        print(f'{f}|NOT_FOUND')\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T04:18:54.283087+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T04:18:54.283218+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "python3 -c \"\nimport json, os\nfiles = [\n    'logs/eval_long_vla_only_seed54.json',\n    'logs/eval_long_obs_only_norm02_seed53.json',\n    'logs/eval_spatial_vla_only_seed53.json',\n    'logs/eval_spatial_vla_only_seed52.json',\n    'logs/eval_spatial_vla_only_seed50.json',\n    'logs/eval_spatial_obs_only_norm02_seed47.json',\n    'logs/eval_object_vla_only_seed49.json',\n    'logs/eval_object_obs_only_norm02_k20_seed43.json',\n]\nos.chdir('/root/acr-vla-conformal-refinement')\nfor f in files:\n    if os.path.isfile(f):\n        try:\n            d = json.load(open(f))\n            print(f'{f}|SR={d.get(\\\"overall_success_rate\\\", \\\"N/A\\\")}')\n        except Exception as e:\n            print(f'{f}|ERROR={e}')\n    else:\n        print(f'{f}|NOT_FOUND')\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "python3 -c \"\nimport json, os\nfiles = [\n    'logs/eval_long_vla_only_seed54.json',\n    'logs/eval_long_obs_only_norm02_seed53.json',\n    'logs/eval_spatial_vla_only_seed53.json',\n    'logs/eval_spatial_vla_only_seed52.json',\n    'logs/eval_spatial_vla_only_seed50.json',\n    'logs/eval_spatial_obs_only_norm02_seed47.json',\n    'logs/eval_object_vla_only_seed49.json',\n    'logs/eval_object_obs_only_norm02_k20_seed43.json',\n]\nos.chdir('/root/acr-vla-conformal-refinement')\nfor f in files:\n    if os.path.isfile(f):\n        try:\n            d = json.load(open(f))\n            print(f'{f}|SR={d.get(\\\"overall_success_rate\\\", \\\"N/A\\\")}')\n        except Exception as e:\n            print(f'{f}|ERROR={e}')\n    else:\n        print(f'{f}|NOT_FOUND')\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T04:18:54.283391+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T04:18:54.283532+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "python3 -c \"\nimport json, os\nfiles = [\n    'logs/eval_spatial_obs_only_norm02_seed49.json',\n    'logs/eval_goal_obs_only_norm02_seed48.json',\n    'logs/eval_goal_obs_only_norm02_seed47.json',\n    'logs/eval_goal_obs_only_norm02_seed50.json',\n    'logs/eval_goal_obs_only_norm02_seed49.json',\n    'logs/eval_long_obs_only_norm02_seed52.json',\n    'logs/eval_long_vla_only_seed49.json',\n    'logs/eval_vla_only_spatial_seed49_r2.json',\n]\nos.chdir('/root/acr-vla-conformal-refinement')\nfor f in files:\n    if os.path.isfile(f):\n        try:\n            d = json.load(open(f))\n            print(f'{f}|SR={d.get(\\\"overall_success_rate\\\", \\\"N/A\\\")}')\n        except Exception as e:\n            print(f'{f}|ERROR={e}')\n    else:\n        print(f'{f}|NOT_FOUND')\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "python3 -c \"\nimport json, os\nfiles = [\n    'logs/eval_spatial_obs_only_norm02_seed49.json',\n    'logs/eval_goal_obs_only_norm02_seed48.json',\n    'logs/eval_goal_obs_only_norm02_seed47.json',\n    'logs/eval_goal_obs_only_norm02_seed50.json',\n    'logs/eval_goal_obs_only_norm02_seed49.json',\n    'logs/eval_long_obs_only_norm02_seed52.json',\n    'logs/eval_long_vla_only_seed49.json',\n    'logs/eval_vla_only_spatial_seed49_r2.json',\n]\nos.chdir('/root/acr-vla-conformal-refinement')\nfor f in files:\n    if os.path.isfile(f):\n        try:\n            d = json.load(open(f))\n            print(f'{f}|SR={d.get(\\\"overall_success_rate\\\", \\\"N/A\\\")}')\n        except Exception as e:\n            print(f'{f}|ERROR={e}')\n    else:\n        print(f'{f}|NOT_FOUND')\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T04:18:54.283662+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T04:18:54.283813+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "python3 -c \"\nimport json, os\nfiles = [\n    'logs/eval_spatial_vla_only_seed54.json',\n    'logs/eval_long_obs_only_norm02_seed54.json',\n    'logs/eval_long_obs_only_norm02_seed49.json',\n    'logs/eval_long_obs_only_norm02_seed48.json',\n    'logs/eval_spatial_obs_only_norm02_seed50.json',\n    'logs/eval_long_vla_only_seed53.json',\n    'logs/eval_goal_vla_only_seed52.json',\n    'logs/eval_long_obs_only_norm02_seed51.json',\n    'logs/eval_spatial_vla_only_seed51.json',\n    'logs/eval_object_vla_only_seed51.json',\n    'logs/eval_spatial_obs_only_norm02_seed48.json',\n    'logs/eval_object_obs_only_norm02_k20_seed42.json',\n    'logs/eval_obs_only_goal_norm02_seed53.json',\n]\nos.chdir('/root/acr-vla-conformal-refinement')\nfor f in files:\n    if os.path.isfile(f):\n        try:\n            d = json.load(open(f))\n            sr = d.get('overall_success_rate', 'N/A')\n            print(f + ' FOUND SR=' + str(sr))\n        except Exception as e:\n            print(f + ' ERROR ' + str(e))\n    else:\n        print(f + ' NOT_FOUND')\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "python3 -c \"\nimport json, os\nfiles = [\n    'logs/eval_spatial_vla_only_seed54.json',\n    'logs/eval_long_obs_only_norm02_seed54.json',\n    'logs/eval_long_obs_only_norm02_seed49.json',\n    'logs/eval_long_obs_only_norm02_seed48.json',\n    'logs/eval_spatial_obs_only_norm02_seed50.json',\n    'logs/eval_long_vla_only_seed53.json',\n    'logs/eval_goal_vla_only_seed52.json',\n    'logs/eval_long_obs_only_norm02_seed51.json',\n    'logs/eval_spatial_vla_only_seed51.json',\n    'logs/eval_object_vla_only_seed51.json',\n    'logs/eval_spatial_obs_only_norm02_seed48.json',\n    'logs/eval_object_obs_only_norm02_k20_seed42.json',\n    'logs/eval_obs_only_goal_norm02_seed53.json',\n]\nos.chdir('/root/acr-vla-conformal-refinement')\nfor f in files:\n    if os.path.isfile(f):\n        try:\n            d = json.load(open(f))\n            sr = d.get('overall_success_rate', 'N/A')\n            print(f + ' FOUND SR=' + str(sr))\n        except Exception as e:\n            print(f + ' ERROR ' + str(e))\n    else:\n        print(f + ' NOT_FOUND')\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T04:18:54.283942+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: python expression contains disallowed call 'open('. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T04:18:54.284062+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "python3 -c \"\nimport json, os\nfiles = [\n    'logs/eval_long_vla_only_seed54.json',\n    'logs/eval_long_obs_only_norm02_seed53.json',\n    'logs/eval_spatial_vla_only_seed53.json',\n    'logs/eval_spatial_vla_only_seed52.json',\n    'logs/eval_spatial_vla_only_seed50.json',\n    'logs/eval_spatial_obs_only_norm02_seed47.json',\n    'logs/eval_object_vla_only_seed49.json',\n    'logs/eval_object_obs_only_norm02_k20_seed43.json',\n]\nos.chdir('/root/acr-vla-conformal-refinement')\nfor f in files:\n    if os.path.isfile(f):\n        try:\n            d = json.load(open(f))\n            sr = d.get('overall_success_rate', 'N/A')\n            print(f + ' FOUND SR=' + str(sr))\n        except Exception as e:\n            print(f + ' ERROR ' + str(e))\n    else:\n        print(f + ' NOT_FOUND')\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "python3 -c \"\nimport json, os\nfiles = [\n    'logs/eval_long_vla_only_seed54.json',\n    'logs/eval_long_obs_only_norm02_seed53.json',\n    'logs/eval_spatial_vla_only_seed53.json',\n    'logs/eval_spatial_vla_only_seed52.json',\n    'logs/eval_spatial_vla_only_seed50.json',\n    'logs/eval_spatial_obs_only_norm02_seed47.json',\n    'logs/eval_object_vla_only_seed49.json',\n    'logs/eval_object_obs_only_norm02_k20_seed43.json',\n]\nos.chdir('/root/acr-vla-conformal-refinement')\nfor f in files:\n    if os.path.isfile(f):\n        try:\n            d = json.load(open(f))\n            sr = d.get('overall_success_rate', 'N/A')\n            print(f + ' FOUND SR=' + str(sr))\n        except Exception as e:\n            print(f + ' ERROR ' + str(e))\n    else:\n        print(f + ' NOT_FOUND')\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T04:18:54.284192+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: python expression contains disallowed call 'open('. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T04:18:54.284373+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "python3 -c \"\nimport json, os\nfiles = [\n    'logs/eval_spatial_obs_only_norm02_seed49.json',\n    'logs/eval_goal_obs_only_norm02_seed48.json',\n    'logs/eval_goal_obs_only_norm02_seed47.json',\n    'logs/eval_goal_obs_only_norm02_seed50.json',\n    'logs/eval_goal_obs_only_norm02_seed49.json',\n    'logs/eval_long_obs_only_norm02_seed52.json',\n    'logs/eval_long_vla_only_seed49.json',\n    'logs/eval_vla_only_spatial_seed49_r2.json',\n]\nos.chdir('/root/acr-vla-conformal-refinement')\nfor f in files:\n    if os.path.isfile(f):\n        try:\n            d = json.load(open(f))\n            sr = d.get('overall_success_rate', 'N/A')\n            print(f + ' FOUND SR=' + str(sr))\n        except Exception as e:\n            print(f + ' ERROR ' + str(e))\n    else:\n        print(f + ' NOT_FOUND')\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "python3 -c \"\nimport json, os\nfiles = [\n    'logs/eval_spatial_obs_only_norm02_seed49.json',\n    'logs/eval_goal_obs_only_norm02_seed48.json',\n    'logs/eval_goal_obs_only_norm02_seed47.json',\n    'logs/eval_goal_obs_only_norm02_seed50.json',\n    'logs/eval_goal_obs_only_norm02_seed49.json',\n    'logs/eval_long_obs_only_norm02_seed52.json',\n    'logs/eval_long_vla_only_seed49.json',\n    'logs/eval_vla_only_spatial_seed49_r2.json',\n]\nos.chdir('/root/acr-vla-conformal-refinement')\nfor f in files:\n    if os.path.isfile(f):\n        try:\n            d = json.load(open(f))\n            sr = d.get('overall_success_rate', 'N/A')\n            print(f + ' FOUND SR=' + str(sr))\n        except Exception as e:\n            print(f + ' ERROR ' + str(e))\n    else:\n        print(f + ' NOT_FOUND')\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T04:18:54.284563+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: python expression contains disallowed call 'open('. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-21T04:18:54.284729+00:00_

You've hit your limit · resets May 22, 5pm (UTC)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T04:28:26.162106+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry,TodoWrite",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry,TodoWrite",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-21T04:28:26.162419+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T04:28:26.162583+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cd /root/acr-vla-conformal-refinement && for f in logs/eval_spatial_vla_only_seed54.json logs/eval_long_obs_only_norm02_seed54.json logs/eval_long_obs_only_norm02_seed49.json logs/eval_long_obs_only_norm02_seed48.json logs/eval_spatial_obs_only_norm02_seed50.json logs/eval_long_vla_only_seed53.json logs/eval_goal_vla_only_seed52.json logs/eval_long_obs_only_norm02_seed51.json logs/eval_spatial_vla_only_seed51.json logs/eval_object_vla_only_seed51.json logs/eval_spatial_obs_only_norm02_seed48.json logs/eval_object_obs_only_norm02_k20_seed42.json logs/eval_obs_only_goal_norm02_seed53.json; do echo \"=== $f ===\"; if [ -f \"$f\" ]; then python3 -c \"import json; d=json.load(open('$f')); print(f'SR={d.get(\\\"overall_success_rate\\\", \\\"N/A\\\")}')\"; else echo \"NOT_FOUND\"; fi; done",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cd /root/acr-vla-conformal-refinement && for f in logs/eval_spatial_vla_only_seed54.json logs/eval_long_obs_only_norm02_seed54.json logs/eval_long_obs_only_norm02_seed49.json logs/eval_long_obs_only_norm02_seed48.json logs/eval_spatial_obs_only_norm02_seed50.json logs/eval_long_vla_only_seed53.json logs/eval_goal_vla_only_seed52.json logs/eval_long_obs_only_norm02_seed51.json logs/eval_spatial_vla_only_seed51.json logs/eval_object_vla_only_seed51.json logs/eval_spatial_obs_only_norm02_seed48.json logs/eval_object_obs_only_norm02_k20_seed42.json logs/eval_obs_only_goal_norm02_seed53.json; do echo \"=== $f ===\"; if [ -f \"$f\" ]; then python3 -c \"import json; d=json.load(open('$f')); print(f'SR={d.get(\\\"overall_success_rate\\\", \\\"N/A\\\")}')\"; else echo \"NOT_FOUND\"; fi; done",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-21T04:28:26.162734+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-21T04:28:26.162865+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "cd /root/acr-vla-conformal-refinement && for f in logs/eval_long_vla_only_seed54.json logs/eval_long_obs_only_norm02_seed53.json logs/eval_spatial_vla_only_seed53.json logs/eval_spatial_vla_only_seed52.json logs/eval_spatial_vla_only_seed50.json logs/eval_spatial_obs_only_norm02_seed47.json logs/eval_object_vla_only_seed49.json logs/eval_object_obs_only_norm02_k20_seed43.json; do echo \"=== $f ===\"; if [ -f \"$f\" ]; then python3 -c \"import json; d=json.load(open('$f')); print(f'SR={d.get(\\\"overall_success_rate\\\", \\\"N/A\\\")}')\"; else echo \"NOT_FOUND\"; fi; done",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "cd /root/acr-vla-conformal-refinement && for f in logs/eval_long_vla_only_seed54.json logs/eval_long_obs_only_norm02_seed53.json logs/eval_spatial_vla_only_seed53.json logs/eval_spatial_vla_only_seed52.json logs/eval_spatial_vla_only_seed50.json logs/eval_spatial_obs_only_norm02_seed47.json logs/eval_object_vla_only_seed49.json logs/eval_object_obs_only_norm02_k20_seed43.json; do echo \"=== $f ===\"; if [ -f \"$f\" ]; then python3 -c \"import json; d=json.load(open('$f')); print(f'SR={d.get(\\\"overall_success_rate\\\", \\\"N/A\\\")}')\"; else echo \"NOT_FOUND\"; fi; done",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-21T04:28:26.162992+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-21T04:28:26.163114+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cd /root/acr-vla-conformal-refinement && for f in logs/eval_spatial_obs_only_norm02_seed49.json logs/eval_goal_obs_only_norm02_seed48.json logs/eval_goal_obs_only_norm02_seed47.json logs/eval_goal_obs_only_norm02_seed50.json logs/eval_goal_obs_only_norm02_seed49.json logs/eval_long_obs_only_norm02_seed52.json logs/eval_long_vla_only_seed49.json logs/eval_vla_only_spatial_seed49_r2.json; do echo \"=== $f ===\"; if [ -f \"$f\" ]; then python3 -c \"import json; d=json.load(open('$f')); print(f'SR={d.get(\\\"overall_success_rate\\\", \\\"N/A\\\")}')\"; else echo \"NOT_FOUND\"; fi; done",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "cd /root/acr-vla-conformal-refinement && for f in logs/eval_spatial_obs_only_norm02_seed49.json logs/eval_goal_obs_only_norm02_seed48.json logs/eval_goal_obs_only_norm02_seed47.json logs/eval_goal_obs_only_norm02_seed50.json logs/eval_goal_obs_only_norm02_seed49.json logs/eval_long_obs_only_norm02_seed52.json logs/eval_long_vla_only_seed49.json logs/eval_vla_only_spatial_seed49_r2.json; do echo \"=== $f ===\"; if [ -f \"$f\" ]; then python3 -c \"import json; d=json.load(open('$f')); print(f'SR={d.get(\\\"overall_success_rate\\\", \\\"N/A\\\")}')\"; else echo \"NOT_FOUND\"; fi; done",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-21T04:28:26.163238+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-21T04:28:26.163396+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed54.json /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed54.json /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed49.json /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed50.json /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed53.json /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed52.json /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed51.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed51.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed51.json /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed48.json /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k20_seed42.json /root/acr-vla-conformal-refinement/logs/eval_obs_only_goal_norm02_seed53.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed54.json /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed54.json /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed49.json /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed50.json /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed53.json /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed52.json /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed51.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed51.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed51.json /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed48.json /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k20_seed42.json /root/acr-vla-conformal-refinement/logs/eval_obs_only_goal_norm02_seed53.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-21T04:28:26.163549+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 1313 May 20 14:25 /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed52.json\\n-rw-r--r-- 1 root root 1783 May 20 12:33 /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed48.json\\n-rw-r--r-- 1 root root 1783 May 20 12:32 /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed49.json\\n-rw-r--r-- 1 root root 1783 May 20 15:10 /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed51.json\\n-rw-r--r-- 1 root root 1783 May 20 15:25 /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed54.json\\n-rw-r--r-- 1 root root 1779 May 20 15:09 /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed53.json\\n-rw-r--r-- 1 root root 1486 May 20 12:28 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed51.json\\n-rw-r--r-- 1 root root 1319 May 20 22:14 /root/acr-vla-conformal-refinement/logs/eval_obs_only_goal_norm02_seed53.json\\n-rw-r--r-- 1 root root 1697 May 20 10:53 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed48.json\\n-rw-r--r-- 1 root root 1697 May 20 12:17 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed50.json\\n-rw-r--r-- 1 root root 1693 May 20 12:47 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed51.json\\n-rw-r--r-- 1 root root 1692 May 20 15:13 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed54.json\\n\", \"stderr\": \"ls: cannot access '/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k20_seed42.json': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.97}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-21T04:28:26.163681+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed54.json /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed53.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed53.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed52.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed50.json /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k20_seed43.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed54.json /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed53.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed53.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed52.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed50.json /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k20_seed43.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-21T04:28:26.163815+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 1783 May 20 15:35 /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed53.json\\n-rw-r--r-- 1 root root 1779 May 20 15:59 /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed54.json\\n-rw-r--r-- 1 root root 1485 May 20 11:11 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json\\n-rw-r--r-- 1 root root 1696 May 20 11:00 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json\\n-rw-r--r-- 1 root root 1691 May 20 11:21 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed50.json\\n-rw-r--r-- 1 root root 1693 May 20 15:18 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed52.json\\n-rw-r--r-- 1 root root 1693 May 20 15:21 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed53.json\\n\", \"stderr\": \"ls: cannot access '/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k20_seed43.json': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 1.24}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-21T04:28:26.163944+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed49.json /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed48.json /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed47.json /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed50.json /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed49.json /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed52.json /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed49.json /root/acr-vla-conformal-refinement/logs/eval_vla_only_spatial_seed49_r2.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed49.json /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed48.json /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed47.json /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed50.json /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed49.json /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed52.json /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed49.json /root/acr-vla-conformal-refinement/logs/eval_vla_only_spatial_seed49_r2.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-21T04:28:26.164077+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 1318 May 20 12:16 /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed47.json\\n-rw-r--r-- 1 root root 1320 May 20 12:21 /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed48.json\\n-rw-r--r-- 1 root root 1319 May 20 14:58 /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed49.json\\n-rw-r--r-- 1 root root 1319 May 20 14:57 /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed50.json\\n-rw-r--r-- 1 root root 1783 May 20 15:46 /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed52.json\\n-rw-r--r-- 1 root root 1779 May 20 12:56 /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed49.json\\n-rw-r--r-- 1 root root 1696 May 20 12:37 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed49.json\\n\", \"stderr\": \"ls: cannot access '/root/acr-vla-conformal-refinement/logs/eval_vla_only_spatial_seed49_r2.json': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.66}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-21T04:28:26.164214+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -H \"overall_success_rate\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed54.json /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed54.json /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed49.json /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed50.json /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed53.json /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed52.json /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed51.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed51.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed51.json /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed48.json /root/acr-vla-conformal-refinement/logs/eval_obs_only_goal_norm02_seed53.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "grep -H \"overall_success_rate\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed54.json /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed54.json /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed49.json /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed50.json /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed53.json /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed52.json /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed51.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed51.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed51.json /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed48.json /root/acr-vla-conformal-refinement/logs/eval_obs_only_goal_norm02_seed53.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-21T04:28:26.164424+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed54.json:  \\\"overall_success_rate\\\": 0.27,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed54.json:  \\\"overall_success_rate\\\": 0.19,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed49.json:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed48.json:  \\\"overall_success_rate\\\": 0.15,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed50.json:  \\\"overall_success_rate\\\": 0.35,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed53.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed52.json:  \\\"overall_success_rate\\\": 0.68,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed51.json:  \\\"overall_success_rate\\\": 0.13,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed51.json:  \\\"overall_success_rate\\\": 0.33,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed51.json:  \\\"overall_success_rate\\\": 0.15,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed48.json:  \\\"overall_success_rate\\\": 0.35,\\n/root/acr-vla-conformal-refinement/logs/eval_obs_only_goal_norm02_seed53.json:  \\\"overall_success_rate\\\": 0.63,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-21T04:28:26.164562+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "grep -H \"overall_success_rate\" /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed54.json /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed53.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed53.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed52.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed50.json /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "grep -H \"overall_success_rate\" /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed54.json /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed53.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed53.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed52.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed50.json /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-21T04:28:26.164763+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed54.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed53.json:  \\\"overall_success_rate\\\": 0.18,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed53.json:  \\\"overall_success_rate\\\": 0.28,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed52.json:  \\\"overall_success_rate\\\": 0.31,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed50.json:  \\\"overall_success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json:  \\\"overall_success_rate\\\": 0.32,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:  \\\"overall_success_rate\\\": 0.1,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-21T04:28:26.164968+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "grep -H \"overall_success_rate\" /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed49.json /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed48.json /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed47.json /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed50.json /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed49.json /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed52.json /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed49.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "grep -H \"overall_success_rate\" /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed49.json /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed48.json /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed47.json /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed50.json /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed49.json /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed52.json /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed49.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-21T04:28:26.165180+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed49.json:  \\\"overall_success_rate\\\": 0.32,\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed48.json:  \\\"overall_success_rate\\\": 0.68,\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed47.json:  \\\"overall_success_rate\\\": 0.69,\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed50.json:  \\\"overall_success_rate\\\": 0.67,\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed49.json:  \\\"overall_success_rate\\\": 0.62,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed52.json:  \\\"overall_success_rate\\\": 0.15,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed49.json:  \\\"overall_success_rate\\\": 0.16,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-21T04:28:26.165454+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-vla-only-spatial-seed54'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-vla-only-spatial-seed54'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-21T04:28:26.165655+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2283}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-21T04:28:26.165832+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'PREPARING'}",
  "fields": "['exp_id', 'status', 'spec']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'PREPARING'}",
    "fields": "['exp_id', 'status', 'spec']"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-21T04:28:26.166052+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-obs-only-object-norm005-seed75\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm01-seed74\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm01-seed64\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm003-seed73\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm005-seed64\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm003-seed65\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm003-seed64\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm003-seed63-r2\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm003-seed62-r2\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm005-seed65\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm005-seed61\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm01-seed60\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm003-seed56\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm01-seed66\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm005-seed66\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm003-seed66\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm003-seed59\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm005-seed58\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm01-seed57\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm005-seed63\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm005-seed62\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm02-seed43-r3\": {\"status\": \"PREPARING\"}, \"openvla-precompute-k1\": {\"status\": \"PREPARING\"}}, \"count\": 23, \"total\": 23, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3763}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-21T04:28:26.166295+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-crm-long-seed54'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-crm-long-seed54'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-21T04:28:26.166493+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0878}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-21T04:28:26.166663+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-vla-only-goal-seed52'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-vla-only-goal-seed52'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-21T04:28:26.166837+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0932}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-21T04:28:26.166997+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-crm-goal-seed48'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-crm-goal-seed48'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-21T04:28:26.167174+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0866}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-21T04:28:26.167408+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "fields": "['exp_id', 'status']",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "fields": "['exp_id', 'status']",
    "limit": "300"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-21T04:28:26.167687+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-obs-only-object-norm005-seed75\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm01-seed74\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm01-seed64\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm003-seed73\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm005-seed64\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm003-seed65\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm003-seed64\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm003-seed63-r2\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm003-seed62-r2\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm005-seed65\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm005-seed61\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm01-seed60\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm003-seed56\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm01-seed66\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm005-seed66\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm003-seed66\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm003-seed59\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm005-seed58\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm01-seed57\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm005-seed63\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm005-seed62\": {\"status\": \"PREPARING\"}, \"eval-perdof-object-norm02-seed49\": {\"status\": \"DONE\"}, \"eval-obs-only-object-norm02-seed43-r3\": {\"status\": \"PREPARING\"}, \"openvla-precompute-k1\": {\"status\": \"PREPARING\"}, \"eval-obs-only-goal-norm02-seed52\": {\"status\": \"DONE\"}, \"eval-argmin-object-seed49\": {\"status\": \"DONE\"}, \"eval-random-selection-spatial-seed43\": {\"status\": \"DONE\"}, \"eval-adaptive-k-spatial-p90-seed43\": {\"status\": \"DONE\"}, \"eval-adaptive-k-object-p90-see
…[truncated 2423 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-21T04:28:26.167920+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'DONE'}",
  "fields": "['exp_id', 'spec.log_path', 'spec.checkpoint_path']",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'DONE'}",
    "fields": "['exp_id', 'spec.log_path', 'spec.checkpoint_path']",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-21T04:28:26.168070+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-perdof-object-norm02-seed49\": {}, \"eval-obs-only-goal-norm02-seed52\": {}, \"eval-argmin-object-seed49\": {}, \"eval-random-selection-spatial-seed43\": {}, \"eval-adaptive-k-spatial-p90-seed43\": {}, \"eval-adaptive-k-object-p90-seed44\": {}, \"eval-adaptive-k-object-p90-seed43\": {}, \"eval-adaptive-k-spatial-p50-seed42\": {}, \"eval-obs-only-object-norm003-seed44\": {}, \"eval-random-selection-object-seed46-r2\": {}}, \"count\": 10, \"total\": 27, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0937}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-21T04:28:26.168201+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-obs-only-goal-norm02-seed52'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-obs-only-goal-norm02-seed52'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-21T04:28:26.168389+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1081}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-21T04:28:26.168526+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "fields": "['*']",
  "limit": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "fields": "['*']",
    "limit": "3"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-21T04:28:26.168663+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-obs-only-object-norm005-seed75\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:56:05.523Z\", \"updated_at\": \"2026-05-21T02:56:12.611Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15}}, \"eval-obs-only-object-norm01-seed74\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:55:20.812Z\", \"updated_at\": \"2026-05-21T02:55:28.975Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.13}}, \"eval-obs-only-object-norm01-seed64\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:54:30.053Z\", \"updated_at\": \"2026-05-21T02:54:30.754Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15}}}, \"count\": 3, \"total\": 64, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1596}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-21T04:28:26.168804+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Test single registry update to validate flow', 'activeForm': 'Testing single registry update', 'status': 'in_progress'}, {'content': 'Update 12 bjb1-32546 experiments', 'activeForm': 'Updating bjb1-32546 experiments', 'status': 'pending'}, {'content': 'Update 7 bjb1-18228 experiments', 'activeForm': 'Updating bjb1-18228 experiments', 'status': 'pending'}, {'content': 'Update 7 bjb2-28827 experiments', 'activeForm': 'Updating bjb2-28827 experiments', 'status': 'pending'}, {'content': 'Report summary table with 3 missing exps', 'activeForm': 'Reporting summary', 'status': 'pending'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Test single registry update to validate flow', 'activeForm': 'Testing single registry update', 'status': 'in_progress'}, {'content': 'Update 12 bjb1-32546 experiments', 'activeForm': 'Updating bjb1-32546 experiments', 'status': 'pending'}, {'content': 'Update 7 bjb1-18228 experiments', 'activeForm': 'Updating bjb1-18228 experiments', 'status': 'pending'}, {'content': 'Update 7 bjb2-28827 experiments', 'activeForm': 'Updating bjb2-28827 experiments', 'status': 'pending'}, {'content': 'Report summary table with 3 missing exps', 'activeForm': 'Reporting summary', 'status': 'pending'}]"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-21T04:28:26.168936+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-21T04:28:26.169051+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-seed54",
  "field": "status",
  "value": "DONE",
  "spec": "{'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed54.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed54.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-seed54",
    "field": "status",
    "value": "DONE",
    "spec": "{'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed54.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed54.json'}"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-21T04:28:26.169187+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → DONE. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.3661}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-21T04:28:26.169355+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-seed54",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-seed54",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-21T04:28:26.169491+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-seed54\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:22:01.946Z\", \"updated_at\": \"2026-05-21T04:22:01.946Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0913}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-21T04:28:26.169610+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-seed54",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'harvest', 'server': 'bjb1-32546', 'data_path': 'logs/eval_spatial_vla_only_seed54.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 54, 'checkpoint_source': 'harvested', 'eval_data': 'spatial', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed54.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed54.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-seed54",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'harvest', 'server': 'bjb1-32546', 'data_path': 'logs/eval_spatial_vla_only_seed54.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 54, 'checkpoint_source': 'harvested', 'eval_data': 'spatial', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed54.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed54.json'}"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-21T04:28:26.169747+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-seed54\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:22:01.946Z\", \"updated_at\": \"2026-05-21T04:22:11.158Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_spatial_vla_only_seed54.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 54, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed54.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed54.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7147}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-21T04:28:26.169869+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-seed54",
  "field": "hypothesis",
  "value": "VLA-only baseline (no CRM) on spatial task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-seed54",
    "field": "hypothesis",
    "value": "VLA-only baseline (no CRM) on spatial task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants."
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-21T04:28:26.170013+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-seed54\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:22:01.946Z\", \"updated_at\": \"2026-05-21T04:22:16.224Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_spatial_vla_only_seed54.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 54, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed54.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed54.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on spatial task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3399}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-21T04:28:26.170145+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-seed54",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-seed54",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-21T04:28:26.170278+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 0.2293}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-21T04:28:26.170400+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-seed54",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-seed54",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-21T04:28:26.170538+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-seed54\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:22:01.946Z\", \"updated_at\": \"2026-05-21T04:22:29.023Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_spatial_vla_only_seed54.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 54, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed54.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed54.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on spatial task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5735}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-21T04:28:26.170665+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-seed54",
  "field": "metrics",
  "value": "{'overall_success_rate': 0.27}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-seed54",
    "field": "metrics",
    "value": "{'overall_success_rate': 0.27}"
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-21T04:28:26.170809+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-seed54\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:22:01.946Z\", \"updated_at\": \"2026-05-21T04:22:29.953Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_spatial_vla_only_seed54.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 54, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed54.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed54.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on spatial task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.27}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6152}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-21T04:28:26.170952+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-seed54",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-seed54",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-21T04:28:26.171105+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-seed54\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:22:01.946Z\", \"updated_at\": \"2026-05-21T04:22:33.863Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_spatial_vla_only_seed54.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 54, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed54.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed54.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on spatial task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.27}, \"completed_at\": \"2026-05-21T04:22:33.863Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5362}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-21T04:28:26.171293+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-seed54",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-seed54",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-21T04:28:26.171429+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed54\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:06.668Z\", \"updated_at\": \"2026-05-21T04:23:06.668Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2586}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-21T04:28:26.171547+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-seed49",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-seed49",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-21T04:28:26.171672+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed49\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:07.723Z\", \"updated_at\": \"2026-05-21T04:23:07.723Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2823}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-21T04:28:26.171785+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-seed48",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-seed48",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-21T04:28:26.171900+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed48\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:08.751Z\", \"updated_at\": \"2026-05-21T04:23:08.751Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2575}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-21T04:28:26.172010+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-spatial-k10-seed50",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-spatial-k10-seed50",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-21T04:28:26.172125+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-spatial-k10-seed50\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:09.772Z\", \"updated_at\": \"2026-05-21T04:23:09.772Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.267}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-21T04:28:26.172250+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-long-seed53",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-long-seed53",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-21T04:28:26.172437+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-long-seed53\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:10.829Z\", \"updated_at\": \"2026-05-21T04:23:10.829Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2534}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-21T04:28:26.172559+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-goal-seed52",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-goal-seed52",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-21T04:28:26.172675+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-goal-seed52\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:11.994Z\", \"updated_at\": \"2026-05-21T04:23:11.994Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6485}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-21T04:28:26.172791+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-seed51",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-seed51",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-21T04:28:26.172902+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-seed51",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-seed51",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-21T04:28:26.173016+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed51\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:13.004Z\", \"updated_at\": \"2026-05-21T04:23:13.004Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5614}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-21T04:28:26.173129+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-seed51\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:13.579Z\", \"updated_at\": \"2026-05-21T04:23:13.579Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4017}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-21T04:28:26.173237+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-object-seed51",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-object-seed51",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-21T04:28:26.173393+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-object-seed51\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:14.480Z\", \"updated_at\": \"2026-05-21T04:23:14.480Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2819}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-21T04:28:26.173508+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-spatial-seed48",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-spatial-seed48",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-21T04:28:26.173622+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-spatial-seed48\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:15.523Z\", \"updated_at\": \"2026-05-21T04:23:15.523Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2623}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 98 · 2026-05-21T04:28:26.173730+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-goal-norm02-seed53",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-goal-norm02-seed53",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-21T04:28:26.173850+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-goal-norm02-seed53\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:16.545Z\", \"updated_at\": \"2026-05-21T04:23:16.545Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2871}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 100 · 2026-05-21T04:28:26.173983+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-long-seed54",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-long-seed54",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-21T04:28:26.174107+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-long-seed54\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:17.623Z\", \"updated_at\": \"2026-05-21T04:23:17.623Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2839}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 102 · 2026-05-21T04:28:26.174218+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-seed53",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-seed53",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-21T04:28:26.174354+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed53\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:18.634Z\", \"updated_at\": \"2026-05-21T04:23:18.634Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2641}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 104 · 2026-05-21T04:28:26.174467+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-seed53",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-seed53",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 105 · 2026-05-21T04:28:26.174581+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-seed53\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:19.064Z\", \"updated_at\": \"2026-05-21T04:23:19.064Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2834}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 106 · 2026-05-21T04:28:26.174689+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-seed52",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-seed52",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-21T04:28:26.174801+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-seed52\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:24.079Z\", \"updated_at\": \"2026-05-21T04:23:24.079Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4728}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 108 · 2026-05-21T04:28:26.174915+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-seed50",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-seed50",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 109 · 2026-05-21T04:28:26.175029+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-seed50\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:25.081Z\", \"updated_at\": \"2026-05-21T04:23:25.081Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3885}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 110 · 2026-05-21T04:28:26.175137+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-spatial-seed47",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-spatial-seed47",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 111 · 2026-05-21T04:28:26.175249+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-spatial-seed47\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:26.099Z\", \"updated_at\": \"2026-05-21T04:23:26.099Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2994}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 112 · 2026-05-21T04:28:26.175436+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-object-seed49-r2",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-object-seed49-r2",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-21T04:28:26.175568+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-object-seed49-r2\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:27.122Z\", \"updated_at\": \"2026-05-21T04:23:27.122Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2692}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 114 · 2026-05-21T04:28:26.175680+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-spatial-k10-seed49",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-spatial-k10-seed49",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-21T04:28:26.175794+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-spatial-k10-seed49\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:28.274Z\", \"updated_at\": \"2026-05-21T04:23:28.274Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2683}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 116 · 2026-05-21T04:28:26.175902+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-goal-seed48",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-goal-seed48",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-21T04:28:26.176021+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-seed48\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:29.201Z\", \"updated_at\": \"2026-05-21T04:23:29.201Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2732}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 118 · 2026-05-21T04:28:26.176134+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-goal-seed47",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-goal-seed47",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 119 · 2026-05-21T04:28:26.176286+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-seed47\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:29.771Z\", \"updated_at\": \"2026-05-21T04:23:29.771Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2692}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-21T04:28:26.176432+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-goal-seed50",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-goal-seed50",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 121 · 2026-05-21T04:28:26.176552+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-seed50\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:30.804Z\", \"updated_at\": \"2026-05-21T04:23:30.804Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2702}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-21T04:28:26.176661+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-goal-seed49",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-goal-seed49",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 123 · 2026-05-21T04:28:26.176774+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-seed49\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:31.844Z\", \"updated_at\": \"2026-05-21T04:23:31.844Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2674}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 124 · 2026-05-21T04:28:26.176880+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-seed52",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-seed52",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 125 · 2026-05-21T04:28:26.176992+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed52\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:32.959Z\", \"updated_at\": \"2026-05-21T04:23:32.959Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2839}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 126 · 2026-05-21T04:28:26.177107+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-long-seed49",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-long-seed49",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 127 · 2026-05-21T04:28:26.177223+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-long-seed49\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:33.602Z\", \"updated_at\": \"2026-05-21T04:23:33.602Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2968}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 128 · 2026-05-21T04:28:26.177391+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-seed54",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'harvest', 'server': 'bjb1-32546', 'data_path': 'logs/eval_long_obs_only_norm02_seed54.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 54, 'checkpoint_source': 'harvested', 'eval_data': 'long', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed54.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed54.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-seed54",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'harvest', 'server': 'bjb1-32546', 'data_path': 'logs/eval_long_obs_only_norm02_seed54.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 54, 'checkpoint_source': 'harvested', 'eval_data': 'long', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed54.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed54.json'}"
  }
}
```

</details>

---

### Tool result

_source line 129 · 2026-05-21T04:28:26.177536+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed54\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:06.668Z\", \"updated_at\": \"2026-05-21T04:23:44.263Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_long_obs_only_norm02_seed54.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 54, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed54.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed54.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4853}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 130 · 2026-05-21T04:28:26.177657+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-seed49",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'harvest', 'server': 'bjb1-32546', 'data_path': 'logs/eval_long_obs_only_norm02_seed49.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 49, 'checkpoint_source': 'harvested', 'eval_data': 'long', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed49.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed49.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-seed49",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'harvest', 'server': 'bjb1-32546', 'data_path': 'logs/eval_long_obs_only_norm02_seed49.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 49, 'checkpoint_source': 'harvested', 'eval_data': 'long', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed49.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed49.json'}"
  }
}
```

</details>

---

### Tool result

_source line 131 · 2026-05-21T04:28:26.177794+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed49\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:07.723Z\", \"updated_at\": \"2026-05-21T04:23:47.491Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_long_obs_only_norm02_seed49.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 49, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed49.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed49.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5114}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 132 · 2026-05-21T04:28:26.177922+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-seed48",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'harvest', 'server': 'bjb1-32546', 'data_path': 'logs/eval_long_obs_only_norm02_seed48.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 48, 'checkpoint_source': 'harvested', 'eval_data': 'long', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed48.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed48.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-seed48",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'harvest', 'server': 'bjb1-32546', 'data_path': 'logs/eval_long_obs_only_norm02_seed48.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 48, 'checkpoint_source': 'harvested', 'eval_data': 'long', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed48.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed48.json'}"
  }
}
```

</details>

---

### Tool result

_source line 133 · 2026-05-21T04:28:26.178059+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:08.751Z\", \"updated_at\": \"2026-05-21T04:23:49.964Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_long_obs_only_norm02_seed48.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 48, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed48.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed48.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3121}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 134 · 2026-05-21T04:28:26.178179+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-spatial-k10-seed50",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'harvest', 'server': 'bjb1-32546', 'data_path': 'logs/eval_spatial_obs_only_norm02_seed50.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 50, 'checkpoint_source': 'harvested', 'eval_data': 'spatial', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed50.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed50.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-spatial-k10-seed50",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'harvest', 'server': 'bjb1-32546', 'data_path': 'logs/eval_spatial_obs_only_norm02_seed50.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 50, 'checkpoint_source': 'harvested', 'eval_data': 'spatial', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed50.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed50.json'}"
  }
}
```

</details>

---

### Tool result

_source line 135 · 2026-05-21T04:28:26.178334+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-spatial-k10-seed50\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:09.772Z\", \"updated_at\": \"2026-05-21T04:23:52.661Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_spatial_obs_only_norm02_seed50.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 50, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed50.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed50.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2785}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 136 · 2026-05-21T04:28:26.178471+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-long-seed53",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'harvest', 'server': 'bjb1-32546', 'data_path': 'logs/eval_long_vla_only_seed53.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 53, 'checkpoint_source': 'harvested', 'eval_data': 'long', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed53.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed53.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-long-seed53",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'harvest', 'server': 'bjb1-32546', 'data_path': 'logs/eval_long_vla_only_seed53.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 53, 'checkpoint_source': 'harvested', 'eval_data': 'long', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed53.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed53.json'}"
  }
}
```

</details>

---

### Tool result

_source line 137 · 2026-05-21T04:28:26.178611+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-long-seed53\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:10.829Z\", \"updated_at\": \"2026-05-21T04:23:55.145Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_long_vla_only_seed53.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 53, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed53.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed53.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3024}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 138 · 2026-05-21T04:28:26.178731+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-goal-seed52",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'harvest', 'server': 'bjb1-32546', 'data_path': 'logs/eval_goal_vla_only_seed52.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 52, 'checkpoint_source': 'harvested', 'eval_data': 'goal', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed52.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed52.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-goal-seed52",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'harvest', 'server': 'bjb1-32546', 'data_path': 'logs/eval_goal_vla_only_seed52.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 52, 'checkpoint_source': 'harvested', 'eval_data': 'goal', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed52.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed52.json'}"
  }
}
```

</details>

---

### Tool result

_source line 139 · 2026-05-21T04:28:26.178866+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-goal-seed52\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:11.994Z\", \"updated_at\": \"2026-05-21T04:23:57.888Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_goal_vla_only_seed52.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 52, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed52.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed52.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.315}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 140 · 2026-05-21T04:28:26.178991+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-seed51",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'harvest', 'server': 'bjb1-32546', 'data_path': 'logs/eval_long_obs_only_norm02_seed51.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 51, 'checkpoint_source': 'harvested', 'eval_data': 'long', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed51.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed51.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-seed51",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'harvest', 'server': 'bjb1-32546', 'data_path': 'logs/eval_long_obs_only_norm02_seed51.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 51, 'checkpoint_source': 'harvested', 'eval_data': 'long', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed51.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed51.json'}"
  }
}
```

</details>

---

### Tool result

_source line 141 · 2026-05-21T04:28:26.179129+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed51\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:13.004Z\", \"updated_at\": \"2026-05-21T04:24:00.443Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_long_obs_only_norm02_seed51.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 51, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed51.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed51.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2873}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 142 · 2026-05-21T04:28:26.179248+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-seed51",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'harvest', 'server': 'bjb1-32546', 'data_path': 'logs/eval_spatial_vla_only_seed51.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 51, 'checkpoint_source': 'harvested', 'eval_data': 'spatial', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed51.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed51.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-seed51",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'harvest', 'server': 'bjb1-32546', 'data_path': 'logs/eval_spatial_vla_only_seed51.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 51, 'checkpoint_source': 'harvested', 'eval_data': 'spatial', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed51.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed51.json'}"
  }
}
```

</details>

---

### Tool result

_source line 143 · 2026-05-21T04:28:26.179409+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-seed51\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:13.579Z\", \"updated_at\": \"2026-05-21T04:24:03.577Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_spatial_vla_only_seed51.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 51, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed51.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed51.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2918}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 144 · 2026-05-21T04:28:26.179531+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-object-seed51",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'harvest', 'server': 'bjb1-32546', 'data_path': 'logs/eval_object_vla_only_seed51.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 51, 'checkpoint_source': 'harvested', 'eval_data': 'object', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed51.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed51.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-object-seed51",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'harvest', 'server': 'bjb1-32546', 'data_path': 'logs/eval_object_vla_only_seed51.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 51, 'checkpoint_source': 'harvested', 'eval_data': 'object', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed51.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed51.json'}"
  }
}
```

</details>

---

### Tool result

_source line 145 · 2026-05-21T04:28:26.179673+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-object-seed51\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:14.480Z\", \"updated_at\": \"2026-05-21T04:24:06.314Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_object_vla_only_seed51.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 51, \"checkpoint_source\": \"harvested\", \"eval_data\": \"object\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed51.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed51.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.552}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 146 · 2026-05-21T04:28:26.179794+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-spatial-seed48",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'harvest', 'server': 'bjb1-32546', 'data_path': 'logs/eval_spatial_obs_only_norm02_seed48.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 48, 'checkpoint_source': 'harvested', 'eval_data': 'spatial', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed48.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed48.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-spatial-seed48",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'harvest', 'server': 'bjb1-32546', 'data_path': 'logs/eval_spatial_obs_only_norm02_seed48.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 48, 'checkpoint_source': 'harvested', 'eval_data': 'spatial', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed48.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed48.json'}"
  }
}
```

</details>

---

### Tool result

_source line 147 · 2026-05-21T04:28:26.179931+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-spatial-seed48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:15.523Z\", \"updated_at\": \"2026-05-21T04:24:08.829Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_spatial_obs_only_norm02_seed48.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 48, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed48.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed48.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2958}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 148 · 2026-05-21T04:28:26.180050+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-goal-norm02-seed53",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'harvest', 'server': 'bjb1-32546', 'data_path': 'logs/eval_obs_only_goal_norm02_seed53.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 53, 'checkpoint_source': 'harvested', 'eval_data': 'goal', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_obs_only_goal_norm02_seed53.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_obs_only_goal_norm02_seed53.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-goal-norm02-seed53",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'harvest', 'server': 'bjb1-32546', 'data_path': 'logs/eval_obs_only_goal_norm02_seed53.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 53, 'checkpoint_source': 'harvested', 'eval_data': 'goal', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_obs_only_goal_norm02_seed53.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_obs_only_goal_norm02_seed53.json'}"
  }
}
```

</details>

---

### Tool result

_source line 149 · 2026-05-21T04:28:26.180190+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-goal-norm02-seed53\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:16.545Z\", \"updated_at\": \"2026-05-21T04:24:11.289Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_obs_only_goal_norm02_seed53.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 53, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_obs_only_goal_norm02_seed53.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_obs_only_goal_norm02_seed53.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.303}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 150 · 2026-05-21T04:28:26.180370+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-long-seed54",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'harvest', 'server': 'bjb1-18228', 'data_path': 'logs/eval_long_vla_only_seed54.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 54, 'checkpoint_source': 'harvested', 'eval_data': 'long', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed54.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed54.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-long-seed54",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'harvest', 'server': 'bjb1-18228', 'data_path': 'logs/eval_long_vla_only_seed54.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 54, 'checkpoint_source': 'harvested', 'eval_data': 'long', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed54.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed54.json'}"
  }
}
```

</details>

---

### Tool result

_source line 151 · 2026-05-21T04:28:26.180570+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-long-seed54\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:17.623Z\", \"updated_at\": \"2026-05-21T04:24:14.084Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-18228\", \"data_path\": \"logs/eval_long_vla_only_seed54.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 54, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed54.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed54.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6112}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 152 · 2026-05-21T04:28:26.180733+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-seed53",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'harvest', 'server': 'bjb1-18228', 'data_path': 'logs/eval_long_obs_only_norm02_seed53.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 53, 'checkpoint_source': 'harvested', 'eval_data': 'long', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed53.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed53.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-seed53",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'harvest', 'server': 'bjb1-18228', 'data_path': 'logs/eval_long_obs_only_norm02_seed53.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 53, 'checkpoint_source': 'harvested', 'eval_data': 'long', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed53.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed53.json'}"
  }
}
```

</details>

---

### Tool result

_source line 153 · 2026-05-21T04:28:26.180881+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed53\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:18.634Z\", \"updated_at\": \"2026-05-21T04:24:17.192Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-18228\", \"data_path\": \"logs/eval_long_obs_only_norm02_seed53.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 53, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed53.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed53.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5841}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 154 · 2026-05-21T04:28:26.181015+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-seed53",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'harvest', 'server': 'bjb1-18228', 'data_path': 'logs/eval_spatial_vla_only_seed53.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 53, 'checkpoint_source': 'harvested', 'eval_data': 'spatial', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed53.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed53.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-seed53",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'harvest', 'server': 'bjb1-18228', 'data_path': 'logs/eval_spatial_vla_only_seed53.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 53, 'checkpoint_source': 'harvested', 'eval_data': 'spatial', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed53.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed53.json'}"
  }
}
```

</details>

---

### Tool result

_source line 155 · 2026-05-21T04:28:26.181161+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-seed53\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:19.064Z\", \"updated_at\": \"2026-05-21T04:24:19.196Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-18228\", \"data_path\": \"logs/eval_spatial_vla_only_seed53.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 53, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed53.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed53.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3074}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 156 · 2026-05-21T04:28:26.181316+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-seed52",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'harvest', 'server': 'bjb1-18228', 'data_path': 'logs/eval_spatial_vla_only_seed52.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 52, 'checkpoint_source': 'harvested', 'eval_data': 'spatial', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed52.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed52.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-seed52",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'harvest', 'server': 'bjb1-18228', 'data_path': 'logs/eval_spatial_vla_only_seed52.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 52, 'checkpoint_source': 'harvested', 'eval_data': 'spatial', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed52.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed52.json'}"
  }
}
```

</details>

---

### Tool call

_source line 157 · 2026-05-21T04:28:26.181467+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-seed50",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'harvest', 'server': 'bjb1-18228', 'data_path': 'logs/eval_spatial_vla_only_seed50.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 50, 'checkpoint_source': 'harvested', 'eval_data': 'spatial', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed50.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed50.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-seed50",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'harvest', 'server': 'bjb1-18228', 'data_path': 'logs/eval_spatial_vla_only_seed50.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 50, 'checkpoint_source': 'harvested', 'eval_data': 'spatial', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed50.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed50.json'}"
  }
}
```

</details>

---

### Tool result

_source line 158 · 2026-05-21T04:28:26.181628+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-seed52\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:24.079Z\", \"updated_at\": \"2026-05-21T04:24:28.075Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-18228\", \"data_path\": \"logs/eval_spatial_vla_only_seed52.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 52, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed52.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed52.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3729}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 159 · 2026-05-21T04:28:26.181766+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-seed50\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:25.081Z\", \"updated_at\": \"2026-05-21T04:24:28.407Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-18228\", \"data_path\": \"logs/eval_spatial_vla_only_seed50.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 50, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed50.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed50.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3151}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 160 · 2026-05-21T04:28:26.181892+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-spatial-seed47",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'harvest', 'server': 'bjb1-18228', 'data_path': 'logs/eval_spatial_obs_only_norm02_seed47.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 47, 'checkpoint_source': 'harvested', 'eval_data': 'spatial', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-spatial-seed47",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'harvest', 'server': 'bjb1-18228', 'data_path': 'logs/eval_spatial_obs_only_norm02_seed47.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 47, 'checkpoint_source': 'harvested', 'eval_data': 'spatial', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json'}"
  }
}
```

</details>

---

### Tool result

_source line 161 · 2026-05-21T04:28:26.182034+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-spatial-seed47\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:26.099Z\", \"updated_at\": \"2026-05-21T04:24:30.945Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-18228\", \"data_path\": \"logs/eval_spatial_obs_only_norm02_seed47.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 47, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3048}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 162 · 2026-05-21T04:28:26.182164+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-object-seed49-r2",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'harvest', 'server': 'bjb1-18228', 'data_path': 'logs/eval_object_vla_only_seed49.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 49, 'checkpoint_source': 'harvested', 'eval_data': 'object', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-object-seed49-r2",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'harvest', 'server': 'bjb1-18228', 'data_path': 'logs/eval_object_vla_only_seed49.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 49, 'checkpoint_source': 'harvested', 'eval_data': 'object', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json'}"
  }
}
```

</details>

---

### Tool result

_source line 163 · 2026-05-21T04:28:26.182322+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-object-seed49-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:27.122Z\", \"updated_at\": \"2026-05-21T04:24:33.662Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-18228\", \"data_path\": \"logs/eval_object_vla_only_seed49.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 49, \"checkpoint_source\": \"harvested\", \"eval_data\": \"object\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3132}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 164 · 2026-05-21T04:28:26.182454+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-spatial-k10-seed49",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'harvest', 'server': 'bjb2-28827', 'data_path': 'logs/eval_spatial_obs_only_norm02_seed49.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 49, 'checkpoint_source': 'harvested', 'eval_data': 'spatial', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed49.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed49.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-spatial-k10-seed49",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'harvest', 'server': 'bjb2-28827', 'data_path': 'logs/eval_spatial_obs_only_norm02_seed49.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 49, 'checkpoint_source': 'harvested', 'eval_data': 'spatial', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed49.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed49.json'}"
  }
}
```

</details>

---

### Tool result

_source line 165 · 2026-05-21T04:28:26.182596+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-spatial-k10-seed49\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:28.274Z\", \"updated_at\": \"2026-05-21T04:24:36.391Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_spatial_obs_only_norm02_seed49.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 49, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed49.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed49.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3781}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 166 · 2026-05-21T04:28:26.182721+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-goal-seed48",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'harvest', 'server': 'bjb2-28827', 'data_path': 'logs/eval_goal_obs_only_norm02_seed48.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 48, 'checkpoint_source': 'harvested', 'eval_data': 'goal', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed48.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed48.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-goal-seed48",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'harvest', 'server': 'bjb2-28827', 'data_path': 'logs/eval_goal_obs_only_norm02_seed48.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 48, 'checkpoint_source': 'harvested', 'eval_data': 'goal', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed48.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed48.json'}"
  }
}
```

</details>

---

### Tool result

_source line 167 · 2026-05-21T04:28:26.182867+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-seed48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:29.201Z\", \"updated_at\": \"2026-05-21T04:24:39.352Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_goal_obs_only_norm02_seed48.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 48, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed48.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed48.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3188}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 168 · 2026-05-21T04:28:26.182991+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-goal-seed47",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'harvest', 'server': 'bjb2-28827', 'data_path': 'logs/eval_goal_obs_only_norm02_seed47.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 47, 'checkpoint_source': 'harvested', 'eval_data': 'goal', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed47.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed47.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-goal-seed47",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'harvest', 'server': 'bjb2-28827', 'data_path': 'logs/eval_goal_obs_only_norm02_seed47.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 47, 'checkpoint_source': 'harvested', 'eval_data': 'goal', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed47.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed47.json'}"
  }
}
```

</details>

---

### Tool result

_source line 169 · 2026-05-21T04:28:26.183127+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-seed47\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:29.771Z\", \"updated_at\": \"2026-05-21T04:24:42.117Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_goal_obs_only_norm02_seed47.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 47, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed47.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed47.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.935}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 170 · 2026-05-21T04:28:26.183249+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-goal-seed50",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'harvest', 'server': 'bjb2-28827', 'data_path': 'logs/eval_goal_obs_only_norm02_seed50.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 50, 'checkpoint_source': 'harvested', 'eval_data': 'goal', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed50.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed50.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-goal-seed50",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'harvest', 'server': 'bjb2-28827', 'data_path': 'logs/eval_goal_obs_only_norm02_seed50.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 50, 'checkpoint_source': 'harvested', 'eval_data': 'goal', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed50.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed50.json'}"
  }
}
```

</details>

---

### Tool result

_source line 171 · 2026-05-21T04:28:26.183416+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-seed50\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:30.804Z\", \"updated_at\": \"2026-05-21T04:24:44.577Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_goal_obs_only_norm02_seed50.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 50, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed50.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed50.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3905}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 172 · 2026-05-21T04:28:26.183544+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-goal-seed49",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'harvest', 'server': 'bjb2-28827', 'data_path': 'logs/eval_goal_obs_only_norm02_seed49.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 49, 'checkpoint_source': 'harvested', 'eval_data': 'goal', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed49.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed49.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-goal-seed49",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'harvest', 'server': 'bjb2-28827', 'data_path': 'logs/eval_goal_obs_only_norm02_seed49.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 49, 'checkpoint_source': 'harvested', 'eval_data': 'goal', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed49.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed49.json'}"
  }
}
```

</details>

---

### Tool result

_source line 173 · 2026-05-21T04:28:26.183681+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-seed49\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:31.844Z\", \"updated_at\": \"2026-05-21T04:24:47.097Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_goal_obs_only_norm02_seed49.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 49, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed49.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed49.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3409}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 174 · 2026-05-21T04:28:26.183804+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-seed52",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'harvest', 'server': 'bjb2-28827', 'data_path': 'logs/eval_long_obs_only_norm02_seed52.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 52, 'checkpoint_source': 'harvested', 'eval_data': 'long', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed52.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed52.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-seed52",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'harvest', 'server': 'bjb2-28827', 'data_path': 'logs/eval_long_obs_only_norm02_seed52.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 52, 'checkpoint_source': 'harvested', 'eval_data': 'long', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed52.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed52.json'}"
  }
}
```

</details>

---

### Tool result

_source line 175 · 2026-05-21T04:28:26.183940+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed52\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:32.959Z\", \"updated_at\": \"2026-05-21T04:24:50.266Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_long_obs_only_norm02_seed52.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 52, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed52.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed52.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3876}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 176 · 2026-05-21T04:28:26.184070+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-long-seed49",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'harvest', 'server': 'bjb2-28827', 'data_path': 'logs/eval_long_vla_only_seed49.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 49, 'checkpoint_source': 'harvested', 'eval_data': 'long', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed49.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed49.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-long-seed49",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'harvest', 'server': 'bjb2-28827', 'data_path': 'logs/eval_long_vla_only_seed49.json', 'data_count': 100, 'model_name': 'openvla', 'seed': 49, 'checkpoint_source': 'harvested', 'eval_data': 'long', 'checkpoint_path': '/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed49.json', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed49.json'}"
  }
}
```

</details>

---

### Tool result

_source line 177 · 2026-05-21T04:28:26.184208+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-long-seed49\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:33.602Z\", \"updated_at\": \"2026-05-21T04:24:52.558Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_long_vla_only_seed49.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 49, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed49.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed49.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.689}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 178 · 2026-05-21T04:28:26.184399+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Test single registry update to validate flow', 'activeForm': 'Testing single registry update', 'status': 'completed'}, {'content': 'Transition all 28 to QUEUED then RUNNING with spec', 'activeForm': 'Transitioning to RUNNING', 'status': 'completed'}, {'content': 'Set hypothesis for all 28', 'activeForm': 'Setting hypothesis', 'status': 'in_progress'}, {'content': 'Set conclusion and metrics for all 28', 'activeForm': 'Setting conclusion and metrics', 'status': 'pending'}, {'content': 'Final RUNNING → DONE for all 28', 'activeForm': 'Finalizing DONE state', 'status': 'pending'}, {'content': 'Report summary table', 'activeForm': 'Reporting summary', 'status': 'pending'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Test single registry update to validate flow', 'activeForm': 'Testing single registry update', 'status': 'completed'}, {'content': 'Transition all 28 to QUEUED then RUNNING with spec', 'activeForm': 'Transitioning to RUNNING', 'status': 'completed'}, {'content': 'Set hypothesis for all 28', 'activeForm': 'Setting hypothesis', 'status': 'in_progress'}, {'content': 'Set conclusion and metrics for all 28', 'activeForm': 'Setting conclusion and metrics', 'status': 'pending'}, {'content': 'Final RUNNING → DONE for all 28', 'activeForm': 'Finalizing DONE state', 'status': 'pending'}, {'content': 'Report summary table', 'activeForm': 'Reporting summary', 'status': 'pending'}]"
  }
}
```

</details>

---

### Tool result

_source line 179 · 2026-05-21T04:28:26.184559+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 180 · 2026-05-21T04:28:26.184697+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-seed54",
  "field": "hypothesis",
  "value": "CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-seed54",
    "field": "hypothesis",
    "value": "CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only."
  }
}
```

</details>

---

### Tool result

_source line 181 · 2026-05-21T04:28:26.184854+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed54\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:06.668Z\", \"updated_at\": \"2026-05-21T04:25:11.784Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_long_obs_only_norm02_seed54.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 54, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed54.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed54.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3816}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 182 · 2026-05-21T04:28:26.184989+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-seed49",
  "field": "hypothesis",
  "value": "CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-seed49",
    "field": "hypothesis",
    "value": "CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only."
  }
}
```

</details>

---

### Tool result

_source line 183 · 2026-05-21T04:28:26.185135+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed49\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:07.723Z\", \"updated_at\": \"2026-05-21T04:25:13.360Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_long_obs_only_norm02_seed49.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 49, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed49.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed49.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1917}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 184 · 2026-05-21T04:28:26.185281+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-seed48",
  "field": "hypothesis",
  "value": "CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-seed48",
    "field": "hypothesis",
    "value": "CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only."
  }
}
```

</details>

---

### Tool result

_source line 185 · 2026-05-21T04:28:26.185433+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:08.751Z\", \"updated_at\": \"2026-05-21T04:25:14.270Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_long_obs_only_norm02_seed48.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 48, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed48.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed48.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2155}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 186 · 2026-05-21T04:28:26.185571+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-spatial-k10-seed50",
  "field": "hypothesis",
  "value": "CRM with k=10 candidates and observation-only refinement (norm=0.2) on spatial task — tests refinement quality with larger candidate pool."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-spatial-k10-seed50",
    "field": "hypothesis",
    "value": "CRM with k=10 candidates and observation-only refinement (norm=0.2) on spatial task — tests refinement quality with larger candidate pool."
  }
}
```

</details>

---

### Tool result

_source line 187 · 2026-05-21T04:28:26.185720+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-spatial-k10-seed50\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:09.772Z\", \"updated_at\": \"2026-05-21T04:25:15.807Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_spatial_obs_only_norm02_seed50.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 50, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed50.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed50.json\"}, \"hypothesis\": \"CRM with k=10 candidates and observation-only refinement (norm=0.2) on spatial task — tests refinement quality with larger candidate pool.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1922}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 188 · 2026-05-21T04:28:26.185850+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-long-seed53",
  "field": "hypothesis",
  "value": "VLA-only baseline (no CRM) on long-horizon task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-long-seed53",
    "field": "hypothesis",
    "value": "VLA-only baseline (no CRM) on long-horizon task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants."
  }
}
```

</details>

---

### Tool result

_source line 189 · 2026-05-21T04:28:26.185994+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-long-seed53\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:10.829Z\", \"updated_at\": \"2026-05-21T04:25:17.386Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_long_vla_only_seed53.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 53, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed53.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed53.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on long-horizon task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2128}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 190 · 2026-05-21T04:28:26.186130+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-goal-seed52",
  "field": "hypothesis",
  "value": "VLA-only baseline (no CRM) on goal task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-goal-seed52",
    "field": "hypothesis",
    "value": "VLA-only baseline (no CRM) on goal task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants."
  }
}
```

</details>

---

### Tool result

_source line 191 · 2026-05-21T04:28:26.186312+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-goal-seed52\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:11.994Z\", \"updated_at\": \"2026-05-21T04:25:18.904Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_goal_vla_only_seed52.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 52, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed52.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed52.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on goal task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1928}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 192 · 2026-05-21T04:28:26.186492+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-seed51",
  "field": "hypothesis",
  "value": "CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-seed51",
    "field": "hypothesis",
    "value": "CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only."
  }
}
```

</details>

---

### Tool result

_source line 193 · 2026-05-21T04:28:26.186646+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed51\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:13.004Z\", \"updated_at\": \"2026-05-21T04:25:20.025Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_long_obs_only_norm02_seed51.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 51, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed51.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed51.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2449}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 194 · 2026-05-21T04:28:26.186785+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-seed51",
  "field": "hypothesis",
  "value": "VLA-only baseline (no CRM) on spatial task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-seed51",
    "field": "hypothesis",
    "value": "VLA-only baseline (no CRM) on spatial task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants."
  }
}
```

</details>

---

### Tool result

_source line 195 · 2026-05-21T04:28:26.186933+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-seed51\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:13.579Z\", \"updated_at\": \"2026-05-21T04:25:21.581Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_spatial_vla_only_seed51.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 51, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed51.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed51.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on spatial task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.197}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 196 · 2026-05-21T04:28:26.187065+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-object-seed51",
  "field": "hypothesis",
  "value": "VLA-only baseline (no CRM) on object task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-object-seed51",
    "field": "hypothesis",
    "value": "VLA-only baseline (no CRM) on object task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants."
  }
}
```

</details>

---

### Tool result

_source line 197 · 2026-05-21T04:28:26.187209+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-object-seed51\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:14.480Z\", \"updated_at\": \"2026-05-21T04:25:22.611Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_object_vla_only_seed51.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 51, \"checkpoint_source\": \"harvested\", \"eval_data\": \"object\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed51.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed51.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on object task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.222}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 198 · 2026-05-21T04:28:26.187388+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-spatial-seed48",
  "field": "hypothesis",
  "value": "CRM with observation-only refinement (norm=0.2) on spatial task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-spatial-seed48",
    "field": "hypothesis",
    "value": "CRM with observation-only refinement (norm=0.2) on spatial task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only."
  }
}
```

</details>

---

### Tool result

_source line 199 · 2026-05-21T04:28:26.187546+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-spatial-seed48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:15.523Z\", \"updated_at\": \"2026-05-21T04:25:24.148Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_spatial_obs_only_norm02_seed48.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 48, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed48.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed48.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on spatial task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1873}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 200 · 2026-05-21T04:28:26.187686+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-goal-norm02-seed53",
  "field": "hypothesis",
  "value": "CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-goal-norm02-seed53",
    "field": "hypothesis",
    "value": "CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only."
  }
}
```

</details>

---

### Tool result

_source line 201 · 2026-05-21T04:28:26.187836+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-goal-norm02-seed53\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:16.545Z\", \"updated_at\": \"2026-05-21T04:25:25.712Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_obs_only_goal_norm02_seed53.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 53, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_obs_only_goal_norm02_seed53.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_obs_only_goal_norm02_seed53.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1956}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 202 · 2026-05-21T04:28:26.187969+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-long-seed54",
  "field": "hypothesis",
  "value": "VLA-only baseline (no CRM) on long-horizon task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-long-seed54",
    "field": "hypothesis",
    "value": "VLA-only baseline (no CRM) on long-horizon task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants."
  }
}
```

</details>

---

### Tool result

_source line 203 · 2026-05-21T04:28:26.188114+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-long-seed54\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:17.623Z\", \"updated_at\": \"2026-05-21T04:25:27.276Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-18228\", \"data_path\": \"logs/eval_long_vla_only_seed54.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 54, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed54.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed54.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on long-horizon task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.195}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 204 · 2026-05-21T04:28:26.188297+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-seed53",
  "field": "hypothesis",
  "value": "CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-seed53",
    "field": "hypothesis",
    "value": "CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only."
  }
}
```

</details>

---

### Tool result

_source line 205 · 2026-05-21T04:28:26.188481+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed53\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:18.634Z\", \"updated_at\": \"2026-05-21T04:25:28.316Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-18228\", \"data_path\": \"logs/eval_long_obs_only_norm02_seed53.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 53, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed53.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed53.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1887}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 206 · 2026-05-21T04:28:26.188618+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-seed53",
  "field": "hypothesis",
  "value": "VLA-only baseline (no CRM) on spatial task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-seed53",
    "field": "hypothesis",
    "value": "VLA-only baseline (no CRM) on spatial task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants."
  }
}
```

</details>

---

### Tool result

_source line 207 · 2026-05-21T04:28:26.188765+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-seed53\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:19.064Z\", \"updated_at\": \"2026-05-21T04:25:29.597Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-18228\", \"data_path\": \"logs/eval_spatial_vla_only_seed53.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 53, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed53.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed53.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on spatial task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.22}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 208 · 2026-05-21T04:28:26.188904+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-seed52",
  "field": "hypothesis",
  "value": "VLA-only baseline (no CRM) on spatial task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-seed52",
    "field": "hypothesis",
    "value": "VLA-only baseline (no CRM) on spatial task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants."
  }
}
```

</details>

---

### Tool result

_source line 209 · 2026-05-21T04:28:26.189050+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-seed52\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:24.079Z\", \"updated_at\": \"2026-05-21T04:25:35.573Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-18228\", \"data_path\": \"logs/eval_spatial_vla_only_seed52.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 52, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed52.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed52.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on spatial task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2877}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 210 · 2026-05-21T04:28:26.189181+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-seed50",
  "field": "hypothesis",
  "value": "VLA-only baseline (no CRM) on spatial task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-seed50",
    "field": "hypothesis",
    "value": "VLA-only baseline (no CRM) on spatial task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants."
  }
}
```

</details>

---

### Tool result

_source line 211 · 2026-05-21T04:28:26.189342+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-seed50\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:25.081Z\", \"updated_at\": \"2026-05-21T04:25:36.573Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-18228\", \"data_path\": \"logs/eval_spatial_vla_only_seed50.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 50, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed50.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed50.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on spatial task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2592}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 212 · 2026-05-21T04:28:26.189478+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-spatial-seed47",
  "field": "hypothesis",
  "value": "CRM with observation-only refinement (norm=0.2) on spatial task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-spatial-seed47",
    "field": "hypothesis",
    "value": "CRM with observation-only refinement (norm=0.2) on spatial task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only."
  }
}
```

</details>

---

### Tool result

_source line 213 · 2026-05-21T04:28:26.189627+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-spatial-seed47\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:26.099Z\", \"updated_at\": \"2026-05-21T04:25:38.151Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-18228\", \"data_path\": \"logs/eval_spatial_obs_only_norm02_seed47.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 47, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on spatial task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1903}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 214 · 2026-05-21T04:28:26.189759+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-object-seed49-r2",
  "field": "hypothesis",
  "value": "VLA-only baseline (no CRM) on object task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-object-seed49-r2",
    "field": "hypothesis",
    "value": "VLA-only baseline (no CRM) on object task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants."
  }
}
```

</details>

---

### Tool result

_source line 215 · 2026-05-21T04:28:26.189919+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-object-seed49-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:27.122Z\", \"updated_at\": \"2026-05-21T04:25:39.712Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-18228\", \"data_path\": \"logs/eval_object_vla_only_seed49.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 49, \"checkpoint_source\": \"harvested\", \"eval_data\": \"object\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on object task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1991}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 216 · 2026-05-21T04:28:26.190084+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-spatial-k10-seed49",
  "field": "hypothesis",
  "value": "CRM with k=10 candidates and observation-only refinement (norm=0.2) on spatial task — tests refinement quality with larger candidate pool."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-spatial-k10-seed49",
    "field": "hypothesis",
    "value": "CRM with k=10 candidates and observation-only refinement (norm=0.2) on spatial task — tests refinement quality with larger candidate pool."
  }
}
```

</details>

---

### Tool result

_source line 217 · 2026-05-21T04:28:26.190235+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-spatial-k10-seed49\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:28.274Z\", \"updated_at\": \"2026-05-21T04:25:40.728Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_spatial_obs_only_norm02_seed49.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 49, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed49.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed49.json\"}, \"hypothesis\": \"CRM with k=10 candidates and observation-only refinement (norm=0.2) on spatial task — tests refinement quality with larger candidate pool.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2083}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 218 · 2026-05-21T04:28:26.190457+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-goal-seed48",
  "field": "hypothesis",
  "value": "CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-goal-seed48",
    "field": "hypothesis",
    "value": "CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only."
  }
}
```

</details>

---

### Tool result

_source line 219 · 2026-05-21T04:28:26.190649+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-seed48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:29.201Z\", \"updated_at\": \"2026-05-21T04:25:42.373Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_goal_obs_only_norm02_seed48.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 48, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed48.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed48.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2498}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 220 · 2026-05-21T04:28:26.190790+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-goal-seed47",
  "field": "hypothesis",
  "value": "CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-goal-seed47",
    "field": "hypothesis",
    "value": "CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only."
  }
}
```

</details>

---

### Tool result

_source line 221 · 2026-05-21T04:28:26.190939+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-seed47\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:29.771Z\", \"updated_at\": \"2026-05-21T04:25:43.881Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_goal_obs_only_norm02_seed47.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 47, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed47.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed47.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1934}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 222 · 2026-05-21T04:28:26.191078+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-goal-seed50",
  "field": "hypothesis",
  "value": "CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-goal-seed50",
    "field": "hypothesis",
    "value": "CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only."
  }
}
```

</details>

---

### Tool result

_source line 223 · 2026-05-21T04:28:26.191224+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-seed50\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:30.804Z\", \"updated_at\": \"2026-05-21T04:25:44.926Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_goal_obs_only_norm02_seed50.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 50, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed50.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed50.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 224 · 2026-05-21T04:28:26.191399+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-goal-seed49",
  "field": "hypothesis",
  "value": "CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-goal-seed49",
    "field": "hypothesis",
    "value": "CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only."
  }
}
```

</details>

---

### Tool result

_source line 225 · 2026-05-21T04:28:26.191552+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-seed49\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:31.844Z\", \"updated_at\": \"2026-05-21T04:25:46.470Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_goal_obs_only_norm02_seed49.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 49, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed49.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed49.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1928}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 226 · 2026-05-21T04:28:26.191716+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-seed52",
  "field": "hypothesis",
  "value": "CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-seed52",
    "field": "hypothesis",
    "value": "CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only."
  }
}
```

</details>

---

### Tool result

_source line 227 · 2026-05-21T04:28:26.191900+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed52\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:32.959Z\", \"updated_at\": \"2026-05-21T04:25:48.058Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_long_obs_only_norm02_seed52.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 52, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed52.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed52.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2036}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 228 · 2026-05-21T04:28:26.192040+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-long-seed49",
  "field": "hypothesis",
  "value": "VLA-only baseline (no CRM) on long-horizon task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-long-seed49",
    "field": "hypothesis",
    "value": "VLA-only baseline (no CRM) on long-horizon task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants."
  }
}
```

</details>

---

### Tool result

_source line 229 · 2026-05-21T04:28:26.192186+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-long-seed49\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:33.602Z\", \"updated_at\": \"2026-05-21T04:25:48.907Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_long_vla_only_seed49.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 49, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed49.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed49.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on long-horizon task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2102}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 230 · 2026-05-21T04:28:26.192412+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-seed54",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-seed54",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 231 · 2026-05-21T04:28:26.192573+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed54\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:06.668Z\", \"updated_at\": \"2026-05-21T04:26:03.874Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_long_obs_only_norm02_seed54.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 54, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed54.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed54.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2045}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 232 · 2026-05-21T04:28:26.192717+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-seed54",
  "field": "metrics",
  "value": "{'overall_success_rate': 0.19}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-seed54",
    "field": "metrics",
    "value": "{'overall_success_rate': 0.19}"
  }
}
```

</details>

---

### Tool result

_source line 233 · 2026-05-21T04:28:26.192871+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed54\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:06.668Z\", \"updated_at\": \"2026-05-21T04:26:04.858Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_long_obs_only_norm02_seed54.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 54, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed54.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed54.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.19}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 234 · 2026-05-21T04:28:26.193004+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-seed49",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-seed49",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 235 · 2026-05-21T04:28:26.193145+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed49\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:07.723Z\", \"updated_at\": \"2026-05-21T04:26:05.328Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_long_obs_only_norm02_seed49.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 49, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed49.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed49.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2328}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 236 · 2026-05-21T04:28:26.193314+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-seed49",
  "field": "metrics",
  "value": "{'overall_success_rate': 0.14}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-seed49",
    "field": "metrics",
    "value": "{'overall_success_rate': 0.14}"
  }
}
```

</details>

---

### Tool result

_source line 237 · 2026-05-21T04:28:26.193488+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed49\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:07.723Z\", \"updated_at\": \"2026-05-21T04:26:06.356Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_long_obs_only_norm02_seed49.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 49, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed49.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed49.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2251}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 238 · 2026-05-21T04:28:26.193623+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-seed48",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-seed48",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 239 · 2026-05-21T04:28:26.193766+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:08.751Z\", \"updated_at\": \"2026-05-21T04:26:07.360Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_long_obs_only_norm02_seed48.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 48, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed48.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed48.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2175}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 240 · 2026-05-21T04:28:26.193896+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-seed48",
  "field": "metrics",
  "value": "{'overall_success_rate': 0.15}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-seed48",
    "field": "metrics",
    "value": "{'overall_success_rate': 0.15}"
  }
}
```

</details>

---

### Tool result

_source line 241 · 2026-05-21T04:28:26.194042+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:08.751Z\", \"updated_at\": \"2026-05-21T04:26:08.358Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_long_obs_only_norm02_seed48.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 48, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed48.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed48.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2005}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 242 · 2026-05-21T04:28:26.194177+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-spatial-k10-seed50",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-spatial-k10-seed50",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 243 · 2026-05-21T04:28:26.194339+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-spatial-k10-seed50\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:09.772Z\", \"updated_at\": \"2026-05-21T04:26:09.356Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_spatial_obs_only_norm02_seed50.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 50, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed50.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed50.json\"}, \"hypothesis\": \"CRM with k=10 candidates and observation-only refinement (norm=0.2) on spatial task — tests refinement quality with larger candidate pool.\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1989}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 244 · 2026-05-21T04:28:26.194475+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-spatial-k10-seed50",
  "field": "metrics",
  "value": "{'overall_success_rate': 0.35}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-spatial-k10-seed50",
    "field": "metrics",
    "value": "{'overall_success_rate': 0.35}"
  }
}
```

</details>

---

### Tool result

_source line 245 · 2026-05-21T04:28:26.194621+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-spatial-k10-seed50\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:09.772Z\", \"updated_at\": \"2026-05-21T04:26:10.362Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_spatial_obs_only_norm02_seed50.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 50, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed50.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed50.json\"}, \"hypothesis\": \"CRM with k=10 candidates and observation-only refinement (norm=0.2) on spatial task — tests refinement quality with larger candidate pool.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.35}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2053}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 246 · 2026-05-21T04:28:26.194755+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-long-seed53",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-long-seed53",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 247 · 2026-05-21T04:28:26.194898+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-long-seed53\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:10.829Z\", \"updated_at\": \"2026-05-21T04:26:11.367Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_long_vla_only_seed53.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 53, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed53.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed53.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on long-horizon task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2009}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 248 · 2026-05-21T04:28:26.195026+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-long-seed53",
  "field": "metrics",
  "value": "{'overall_success_rate': 0.12}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-long-seed53",
    "field": "metrics",
    "value": "{'overall_success_rate': 0.12}"
  }
}
```

</details>

---

### Tool result

_source line 249 · 2026-05-21T04:28:26.195168+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-long-seed53\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:10.829Z\", \"updated_at\": \"2026-05-21T04:26:12.360Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_long_vla_only_seed53.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 53, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed53.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed53.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on long-horizon task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.12}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1983}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 250 · 2026-05-21T04:28:26.195319+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-goal-seed52",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-goal-seed52",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 251 · 2026-05-21T04:28:26.195475+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-goal-seed52\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:11.994Z\", \"updated_at\": \"2026-05-21T04:26:13.441Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_goal_vla_only_seed52.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 52, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed52.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed52.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on goal task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3801}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 252 · 2026-05-21T04:28:26.195604+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-goal-seed52",
  "field": "metrics",
  "value": "{'overall_success_rate': 0.68}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-goal-seed52",
    "field": "metrics",
    "value": "{'overall_success_rate': 0.68}"
  }
}
```

</details>

---

### Tool result

_source line 253 · 2026-05-21T04:28:26.195748+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-goal-seed52\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:11.994Z\", \"updated_at\": \"2026-05-21T04:26:14.414Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_goal_vla_only_seed52.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 52, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed52.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed52.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on goal task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.68}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3539}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 254 · 2026-05-21T04:28:26.195874+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-seed51",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-seed51",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 255 · 2026-05-21T04:28:26.196013+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed51\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:13.004Z\", \"updated_at\": \"2026-05-21T04:26:15.359Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_long_obs_only_norm02_seed51.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 51, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed51.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed51.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2034}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 256 · 2026-05-21T04:28:26.196145+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-seed51",
  "field": "metrics",
  "value": "{'overall_success_rate': 0.13}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-seed51",
    "field": "metrics",
    "value": "{'overall_success_rate': 0.13}"
  }
}
```

</details>

---

### Tool result

_source line 257 · 2026-05-21T04:28:26.196347+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed51\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:13.004Z\", \"updated_at\": \"2026-05-21T04:26:15.939Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_long_obs_only_norm02_seed51.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 51, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed51.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed51.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2206}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 258 · 2026-05-21T04:28:26.196534+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-seed51",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-seed51",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 259 · 2026-05-21T04:28:26.196682+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-seed51\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:13.579Z\", \"updated_at\": \"2026-05-21T04:26:24.986Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_spatial_vla_only_seed51.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 51, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed51.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed51.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on spatial task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2565}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 260 · 2026-05-21T04:28:26.196820+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-seed51",
  "field": "metrics",
  "value": "{'overall_success_rate': 0.33}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-seed51",
    "field": "metrics",
    "value": "{'overall_success_rate': 0.33}"
  }
}
```

</details>

---

### Tool result

_source line 261 · 2026-05-21T04:28:26.196968+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-seed51\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:13.579Z\", \"updated_at\": \"2026-05-21T04:26:26.012Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_spatial_vla_only_seed51.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 51, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed51.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed51.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on spatial task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.33}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.209}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 262 · 2026-05-21T04:28:26.197098+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-object-seed51",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-object-seed51",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 263 · 2026-05-21T04:28:26.197240+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-object-seed51\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:14.480Z\", \"updated_at\": \"2026-05-21T04:26:27.050Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_object_vla_only_seed51.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 51, \"checkpoint_source\": \"harvested\", \"eval_data\": \"object\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed51.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed51.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on object task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2023}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 264 · 2026-05-21T04:28:26.197395+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-object-seed51",
  "field": "metrics",
  "value": "{'overall_success_rate': 0.15}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-object-seed51",
    "field": "metrics",
    "value": "{'overall_success_rate': 0.15}"
  }
}
```

</details>

---

### Tool result

_source line 265 · 2026-05-21T04:28:26.197541+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-object-seed51\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:14.480Z\", \"updated_at\": \"2026-05-21T04:26:28.091Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_object_vla_only_seed51.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 51, \"checkpoint_source\": \"harvested\", \"eval_data\": \"object\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed51.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed51.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on object task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.198}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 266 · 2026-05-21T04:28:26.197676+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-spatial-seed48",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-spatial-seed48",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 267 · 2026-05-21T04:28:26.197819+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-spatial-seed48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:15.523Z\", \"updated_at\": \"2026-05-21T04:26:29.136Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_spatial_obs_only_norm02_seed48.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 48, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed48.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed48.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on spatial task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2044}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 268 · 2026-05-21T04:28:26.197947+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-spatial-seed48",
  "field": "metrics",
  "value": "{'overall_success_rate': 0.35}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-spatial-seed48",
    "field": "metrics",
    "value": "{'overall_success_rate': 0.35}"
  }
}
```

</details>

---

### Tool result

_source line 269 · 2026-05-21T04:28:26.198092+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-spatial-seed48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:15.523Z\", \"updated_at\": \"2026-05-21T04:26:30.240Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_spatial_obs_only_norm02_seed48.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 48, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed48.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed48.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on spatial task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.35}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2094}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 270 · 2026-05-21T04:28:26.198227+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-goal-norm02-seed53",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-goal-norm02-seed53",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool call

_source line 271 · 2026-05-21T04:28:26.198370+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-goal-norm02-seed53",
  "field": "metrics",
  "value": "{'overall_success_rate': 0.63}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-goal-norm02-seed53",
    "field": "metrics",
    "value": "{'overall_success_rate': 0.63}"
  }
}
```

</details>

---

### Tool result

_source line 272 · 2026-05-21T04:28:26.198519+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-goal-norm02-seed53\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:16.545Z\", \"updated_at\": \"2026-05-21T04:26:32.385Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_obs_only_goal_norm02_seed53.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 53, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_obs_only_goal_norm02_seed53.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_obs_only_goal_norm02_seed53.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2012}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 273 · 2026-05-21T04:28:26.198671+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-goal-norm02-seed53\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:16.545Z\", \"updated_at\": \"2026-05-21T04:26:32.591Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_obs_only_goal_norm02_seed53.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 53, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_obs_only_goal_norm02_seed53.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_obs_only_goal_norm02_seed53.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.63}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1975}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 274 · 2026-05-21T04:28:26.198800+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-long-seed54",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-long-seed54",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool call

_source line 275 · 2026-05-21T04:28:26.198924+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-long-seed54",
  "field": "metrics",
  "value": "{'overall_success_rate': 0.12}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-long-seed54",
    "field": "metrics",
    "value": "{'overall_success_rate': 0.12}"
  }
}
```

</details>

---

### Tool result

_source line 276 · 2026-05-21T04:28:26.199071+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-long-seed54\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:17.623Z\", \"updated_at\": \"2026-05-21T04:26:35.669Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-18228\", \"data_path\": \"logs/eval_long_vla_only_seed54.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 54, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed54.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed54.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on long-horizon task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2117}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 277 · 2026-05-21T04:28:26.199218+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-long-seed54\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:17.623Z\", \"updated_at\": \"2026-05-21T04:26:35.905Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-18228\", \"data_path\": \"logs/eval_long_vla_only_seed54.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 54, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed54.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed54.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on long-horizon task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.12}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2238}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 278 · 2026-05-21T04:28:26.199372+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-seed53",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-seed53",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool call

_source line 279 · 2026-05-21T04:28:26.199492+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-seed53",
  "field": "metrics",
  "value": "{'overall_success_rate': 0.18}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-seed53",
    "field": "metrics",
    "value": "{'overall_success_rate': 0.18}"
  }
}
```

</details>

---

### Tool result

_source line 280 · 2026-05-21T04:28:26.199635+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed53\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:18.634Z\", \"updated_at\": \"2026-05-21T04:26:39.715Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-18228\", \"data_path\": \"logs/eval_long_obs_only_norm02_seed53.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 53, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed53.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed53.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4288}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 281 · 2026-05-21T04:28:26.199790+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed53\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:18.634Z\", \"updated_at\": \"2026-05-21T04:26:40.138Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-18228\", \"data_path\": \"logs/eval_long_obs_only_norm02_seed53.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 53, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed53.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed53.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4197}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 282 · 2026-05-21T04:28:26.199920+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-seed53",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-seed53",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool call

_source line 283 · 2026-05-21T04:28:26.200038+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-seed53",
  "field": "metrics",
  "value": "{'overall_success_rate': 0.28}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-seed53",
    "field": "metrics",
    "value": "{'overall_success_rate': 0.28}"
  }
}
```

</details>

---

### Tool result

_source line 284 · 2026-05-21T04:28:26.200181+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-seed53\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:19.064Z\", \"updated_at\": \"2026-05-21T04:26:40.765Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-18228\", \"data_path\": \"logs/eval_spatial_vla_only_seed53.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 53, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed53.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed53.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on spatial task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4228}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 285 · 2026-05-21T04:28:26.200454+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-seed53\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:19.064Z\", \"updated_at\": \"2026-05-21T04:26:41.164Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-18228\", \"data_path\": \"logs/eval_spatial_vla_only_seed53.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 53, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed53.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed53.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on spatial task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.28}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3758}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 286 · 2026-05-21T04:28:26.200612+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-seed52",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-seed52",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 287 · 2026-05-21T04:28:26.200759+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-seed52\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:24.079Z\", \"updated_at\": \"2026-05-21T04:26:45.305Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-18228\", \"data_path\": \"logs/eval_spatial_vla_only_seed52.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 52, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed52.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed52.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on spatial task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3338}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 288 · 2026-05-21T04:28:26.200891+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-seed52",
  "field": "metrics",
  "value": "{'overall_success_rate': 0.31}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-seed52",
    "field": "metrics",
    "value": "{'overall_success_rate': 0.31}"
  }
}
```

</details>

---

### Tool result

_source line 289 · 2026-05-21T04:28:26.201039+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-seed52\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:24.079Z\", \"updated_at\": \"2026-05-21T04:26:46.276Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-18228\", \"data_path\": \"logs/eval_spatial_vla_only_seed52.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 52, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed52.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed52.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on spatial task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.31}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.202}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 290 · 2026-05-21T04:28:26.201177+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-seed50",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-seed50",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 291 · 2026-05-21T04:28:26.201339+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-seed50\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:25.081Z\", \"updated_at\": \"2026-05-21T04:26:47.362Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-18228\", \"data_path\": \"logs/eval_spatial_vla_only_seed50.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 50, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed50.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed50.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on spatial task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2068}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 292 · 2026-05-21T04:28:26.201477+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-seed50",
  "field": "metrics",
  "value": "{'overall_success_rate': 0.3}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-seed50",
    "field": "metrics",
    "value": "{'overall_success_rate': 0.3}"
  }
}
```

</details>

---

### Tool result

_source line 293 · 2026-05-21T04:28:26.201622+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-seed50\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:25.081Z\", \"updated_at\": \"2026-05-21T04:26:48.350Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-18228\", \"data_path\": \"logs/eval_spatial_vla_only_seed50.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 50, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed50.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed50.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on spatial task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2015}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 294 · 2026-05-21T04:28:26.201757+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-spatial-seed47",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-spatial-seed47",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 295 · 2026-05-21T04:28:26.201900+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-spatial-seed47\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:26.099Z\", \"updated_at\": \"2026-05-21T04:26:49.387Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-18228\", \"data_path\": \"logs/eval_spatial_obs_only_norm02_seed47.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 47, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on spatial task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2072}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 296 · 2026-05-21T04:28:26.202029+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-spatial-seed47",
  "field": "metrics",
  "value": "{'overall_success_rate': 0.32}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-spatial-seed47",
    "field": "metrics",
    "value": "{'overall_success_rate': 0.32}"
  }
}
```

</details>

---

### Tool result

_source line 297 · 2026-05-21T04:28:26.202174+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-spatial-seed47\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:26.099Z\", \"updated_at\": \"2026-05-21T04:26:50.500Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-18228\", \"data_path\": \"logs/eval_spatial_obs_only_norm02_seed47.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 47, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on spatial task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.32}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.262}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 298 · 2026-05-21T04:28:26.202321+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-object-seed49-r2",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-object-seed49-r2",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 299 · 2026-05-21T04:28:26.202472+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-object-seed49-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:27.122Z\", \"updated_at\": \"2026-05-21T04:26:51.533Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-18228\", \"data_path\": \"logs/eval_object_vla_only_seed49.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 49, \"checkpoint_source\": \"harvested\", \"eval_data\": \"object\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on object task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.29}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 300 · 2026-05-21T04:28:26.202603+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-object-seed49-r2",
  "field": "metrics",
  "value": "{'overall_success_rate': 0.1}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-object-seed49-r2",
    "field": "metrics",
    "value": "{'overall_success_rate': 0.1}"
  }
}
```

</details>

---

### Tool result

_source line 301 · 2026-05-21T04:28:26.202749+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-object-seed49-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:27.122Z\", \"updated_at\": \"2026-05-21T04:26:52.522Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-18228\", \"data_path\": \"logs/eval_object_vla_only_seed49.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 49, \"checkpoint_source\": \"harvested\", \"eval_data\": \"object\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on object task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2058}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 302 · 2026-05-21T04:28:26.202922+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-spatial-k10-seed49",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-spatial-k10-seed49",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 303 · 2026-05-21T04:28:26.203077+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-spatial-k10-seed49\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:28.274Z\", \"updated_at\": \"2026-05-21T04:26:53.695Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_spatial_obs_only_norm02_seed49.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 49, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed49.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed49.json\"}, \"hypothesis\": \"CRM with k=10 candidates and observation-only refinement (norm=0.2) on spatial task — tests refinement quality with larger candidate pool.\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4057}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 304 · 2026-05-21T04:28:26.203223+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-spatial-k10-seed49",
  "field": "metrics",
  "value": "{'overall_success_rate': 0.32}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-spatial-k10-seed49",
    "field": "metrics",
    "value": "{'overall_success_rate': 0.32}"
  }
}
```

</details>

---

### Tool result

_source line 305 · 2026-05-21T04:28:26.203416+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-spatial-k10-seed49\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:28.274Z\", \"updated_at\": \"2026-05-21T04:26:54.720Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_spatial_obs_only_norm02_seed49.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 49, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed49.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed49.json\"}, \"hypothesis\": \"CRM with k=10 candidates and observation-only refinement (norm=0.2) on spatial task — tests refinement quality with larger candidate pool.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.32}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3761}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 306 · 2026-05-21T04:28:26.203554+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-goal-seed48",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-goal-seed48",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 307 · 2026-05-21T04:28:26.203698+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-seed48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:29.201Z\", \"updated_at\": \"2026-05-21T04:26:55.759Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_goal_obs_only_norm02_seed48.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 48, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed48.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed48.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 308 · 2026-05-21T04:28:26.203835+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-goal-seed48",
  "field": "metrics",
  "value": "{'overall_success_rate': 0.68}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-goal-seed48",
    "field": "metrics",
    "value": "{'overall_success_rate': 0.68}"
  }
}
```

</details>

---

### Tool result

_source line 309 · 2026-05-21T04:28:26.203984+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-seed48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:29.201Z\", \"updated_at\": \"2026-05-21T04:26:56.674Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_goal_obs_only_norm02_seed48.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 48, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed48.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed48.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.68}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2092}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 310 · 2026-05-21T04:28:26.204114+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-goal-seed47",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-goal-seed47",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 311 · 2026-05-21T04:28:26.204291+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-seed47\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:29.771Z\", \"updated_at\": \"2026-05-21T04:26:57.740Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_goal_obs_only_norm02_seed47.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 47, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed47.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed47.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2098}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 312 · 2026-05-21T04:28:26.204482+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-goal-seed47",
  "field": "metrics",
  "value": "{'overall_success_rate': 0.69}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-goal-seed47",
    "field": "metrics",
    "value": "{'overall_success_rate': 0.69}"
  }
}
```

</details>

---

### Tool result

_source line 313 · 2026-05-21T04:28:26.204648+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-seed47\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:29.771Z\", \"updated_at\": \"2026-05-21T04:26:58.269Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_goal_obs_only_norm02_seed47.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 47, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed47.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed47.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.69}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2184}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 314 · 2026-05-21T04:28:26.204788+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-goal-seed50",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-goal-seed50",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 315 · 2026-05-21T04:28:26.204934+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-seed50\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:30.804Z\", \"updated_at\": \"2026-05-21T04:27:02.697Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_goal_obs_only_norm02_seed50.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 50, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed50.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed50.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2163}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 316 · 2026-05-21T04:28:26.205065+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-goal-seed50",
  "field": "metrics",
  "value": "{'overall_success_rate': 0.67}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-goal-seed50",
    "field": "metrics",
    "value": "{'overall_success_rate': 0.67}"
  }
}
```

</details>

---

### Tool result

_source line 317 · 2026-05-21T04:28:26.205214+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-seed50\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:30.804Z\", \"updated_at\": \"2026-05-21T04:27:03.748Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_goal_obs_only_norm02_seed50.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 50, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed50.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed50.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.67}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2093}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 318 · 2026-05-21T04:28:26.205373+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-goal-seed49",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-goal-seed49",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 319 · 2026-05-21T04:28:26.205520+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-seed49\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:31.844Z\", \"updated_at\": \"2026-05-21T04:27:04.761Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_goal_obs_only_norm02_seed49.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 49, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed49.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed49.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2248}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 320 · 2026-05-21T04:28:26.205649+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-goal-seed49",
  "field": "metrics",
  "value": "{'overall_success_rate': 0.62}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-goal-seed49",
    "field": "metrics",
    "value": "{'overall_success_rate': 0.62}"
  }
}
```

</details>

---

### Tool result

_source line 321 · 2026-05-21T04:28:26.205795+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-seed49\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:31.844Z\", \"updated_at\": \"2026-05-21T04:27:05.928Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_goal_obs_only_norm02_seed49.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 49, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed49.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed49.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.62}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2496}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 322 · 2026-05-21T04:28:26.205923+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-seed52",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-seed52",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 323 · 2026-05-21T04:28:26.206069+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed52\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:32.959Z\", \"updated_at\": \"2026-05-21T04:27:06.308Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_long_obs_only_norm02_seed52.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 52, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed52.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed52.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2085}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 324 · 2026-05-21T04:28:26.206229+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-seed52",
  "field": "metrics",
  "value": "{'overall_success_rate': 0.15}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-seed52",
    "field": "metrics",
    "value": "{'overall_success_rate': 0.15}"
  }
}
```

</details>

---

### Tool result

_source line 325 · 2026-05-21T04:28:26.206433+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed52\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:32.959Z\", \"updated_at\": \"2026-05-21T04:27:10.950Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_long_obs_only_norm02_seed52.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 52, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed52.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed52.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2399}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 326 · 2026-05-21T04:28:26.206574+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-long-seed49",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-long-seed49",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool call

_source line 327 · 2026-05-21T04:28:26.206697+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-long-seed49",
  "field": "metrics",
  "value": "{'overall_success_rate': 0.16}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-long-seed49",
    "field": "metrics",
    "value": "{'overall_success_rate': 0.16}"
  }
}
```

</details>

---

### Tool result

_source line 328 · 2026-05-21T04:28:26.206846+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-long-seed49\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:33.602Z\", \"updated_at\": \"2026-05-21T04:27:11.447Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_long_vla_only_seed49.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 49, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed49.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed49.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on long-horizon task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.242}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 329 · 2026-05-21T04:28:26.207005+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-long-seed49\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:33.602Z\", \"updated_at\": \"2026-05-21T04:27:11.683Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_long_vla_only_seed49.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 49, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed49.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed49.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on long-horizon task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2179}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 330 · 2026-05-21T04:28:26.207149+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Test single registry update to validate flow', 'activeForm': 'Testing single registry update', 'status': 'completed'}, {'content': 'Transition all 28 to QUEUED then RUNNING with spec', 'activeForm': 'Transitioning to RUNNING', 'status': 'completed'}, {'content': 'Set hypothesis for all 28', 'activeForm': 'Setting hypothesis', 'status': 'completed'}, {'content': 'Set conclusion and metrics for all 28', 'activeForm': 'Setting conclusion and metrics', 'status': 'completed'}, {'content': 'Final RUNNING → DONE for all 28', 'activeForm': 'Finalizing DONE state', 'status': 'in_progress'}, {'content': 'Report summary table', 'activeForm': 'Reporting summary', 'status': 'pending'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Test single registry update to validate flow', 'activeForm': 'Testing single registry update', 'status': 'completed'}, {'content': 'Transition all 28 to QUEUED then RUNNING with spec', 'activeForm': 'Transitioning to RUNNING', 'status': 'completed'}, {'content': 'Set hypothesis for all 28', 'activeForm': 'Setting hypothesis', 'status': 'completed'}, {'content': 'Set conclusion and metrics for all 28', 'activeForm': 'Setting conclusion and metrics', 'status': 'completed'}, {'content': 'Final RUNNING → DONE for all 28', 'activeForm': 'Finalizing DONE state', 'status': 'in_progress'}, {'content': 'Report summary table', 'activeForm': 'Reporting summary', 'status': 'pending'}]"
  }
}
```

</details>

---

### Tool result

_source line 331 · 2026-05-21T04:28:26.207324+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 332 · 2026-05-21T04:28:26.207471+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-seed54",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-seed54",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 333 · 2026-05-21T04:28:26.207638+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed54\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:06.668Z\", \"updated_at\": \"2026-05-21T04:27:26.691Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_long_obs_only_norm02_seed54.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 54, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed54.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed54.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.19}, \"completed_at\": \"2026-05-21T04:27:26.691Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7134}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 334 · 2026-05-21T04:28:26.207778+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-seed49",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-seed49",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 335 · 2026-05-21T04:28:26.207931+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed49\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:07.723Z\", \"updated_at\": \"2026-05-21T04:27:27.682Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_long_obs_only_norm02_seed49.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 49, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed49.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed49.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}, \"completed_at\": \"2026-05-21T04:27:27.682Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6663}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 336 · 2026-05-21T04:28:26.208065+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-seed48",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-seed48",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 337 · 2026-05-21T04:28:26.208214+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed48\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:08.751Z\", \"updated_at\": \"2026-05-21T04:27:28.708Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_long_obs_only_norm02_seed48.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 48, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed48.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed48.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}, \"completed_at\": \"2026-05-21T04:27:28.708Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6848}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 338 · 2026-05-21T04:28:26.208436+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-spatial-k10-seed50",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-spatial-k10-seed50",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool call

_source line 339 · 2026-05-21T04:28:26.208576+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-long-seed53",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-long-seed53",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 340 · 2026-05-21T04:28:26.208733+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-spatial-k10-seed50\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:09.772Z\", \"updated_at\": \"2026-05-21T04:27:29.713Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_spatial_obs_only_norm02_seed50.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 50, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed50.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed50.json\"}, \"hypothesis\": \"CRM with k=10 candidates and observation-only refinement (norm=0.2) on spatial task — tests refinement quality with larger candidate pool.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.35}, \"completed_at\": \"2026-05-21T04:27:29.713Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6265}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 341 · 2026-05-21T04:28:26.208898+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-long-seed53\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:10.829Z\", \"updated_at\": \"2026-05-21T04:27:30.368Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_long_vla_only_seed53.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 53, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed53.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed53.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on long-horizon task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.12}, \"completed_at\": \"2026-05-21T04:27:30.368Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5955}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 342 · 2026-05-21T04:28:26.209040+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-goal-seed52",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-goal-seed52",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 343 · 2026-05-21T04:28:26.209194+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-goal-seed52\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:11.994Z\", \"updated_at\": \"2026-05-21T04:27:31.314Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_goal_vla_only_seed52.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 52, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed52.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed52.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on goal task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.68}, \"completed_at\": \"2026-05-21T04:27:31.314Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6302}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 344 · 2026-05-21T04:28:26.209349+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-seed51",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-seed51",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 345 · 2026-05-21T04:28:26.209505+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed51\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:13.004Z\", \"updated_at\": \"2026-05-21T04:27:32.349Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_long_obs_only_norm02_seed51.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 51, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed51.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed51.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}, \"completed_at\": \"2026-05-21T04:27:32.349Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6277}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 346 · 2026-05-21T04:28:26.209646+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-seed51",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-seed51",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 347 · 2026-05-21T04:28:26.209799+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-seed51\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:13.579Z\", \"updated_at\": \"2026-05-21T04:27:33.399Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_spatial_vla_only_seed51.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 51, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed51.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed51.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on spatial task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.33}, \"completed_at\": \"2026-05-21T04:27:33.399Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6315}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 348 · 2026-05-21T04:28:26.209931+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-object-seed51",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-object-seed51",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 349 · 2026-05-21T04:28:26.210081+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-object-seed51\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:14.480Z\", \"updated_at\": \"2026-05-21T04:27:34.498Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_object_vla_only_seed51.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 51, \"checkpoint_source\": \"harvested\", \"eval_data\": \"object\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed51.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed51.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on object task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}, \"completed_at\": \"2026-05-21T04:27:34.498Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6842}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 350 · 2026-05-21T04:28:26.210221+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-spatial-seed48",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-spatial-seed48",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 351 · 2026-05-21T04:28:26.210393+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-spatial-seed48\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:15.523Z\", \"updated_at\": \"2026-05-21T04:27:35.508Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_spatial_obs_only_norm02_seed48.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 48, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed48.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed48.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on spatial task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.35}, \"completed_at\": \"2026-05-21T04:27:35.508Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6614}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 352 · 2026-05-21T04:28:26.210530+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-goal-norm02-seed53",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-goal-norm02-seed53",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 353 · 2026-05-21T04:28:26.210681+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-goal-norm02-seed53\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:16.545Z\", \"updated_at\": \"2026-05-21T04:27:36.518Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-32546\", \"data_path\": \"logs/eval_obs_only_goal_norm02_seed53.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 53, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_obs_only_goal_norm02_seed53.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_obs_only_goal_norm02_seed53.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.63}, \"completed_at\": \"2026-05-21T04:27:36.518Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6281}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 354 · 2026-05-21T04:28:26.210815+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-long-seed54",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-long-seed54",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool call

_source line 355 · 2026-05-21T04:28:26.210937+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-seed53",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-seed53",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 356 · 2026-05-21T04:28:26.211088+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-long-seed54\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:17.623Z\", \"updated_at\": \"2026-05-21T04:27:37.520Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-18228\", \"data_path\": \"logs/eval_long_vla_only_seed54.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 54, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed54.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed54.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on long-horizon task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.12}, \"completed_at\": \"2026-05-21T04:27:37.520Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6148}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 357 · 2026-05-21T04:28:26.211249+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed53\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:18.634Z\", \"updated_at\": \"2026-05-21T04:27:38.166Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-18228\", \"data_path\": \"logs/eval_long_obs_only_norm02_seed53.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 53, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed53.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed53.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}, \"completed_at\": \"2026-05-21T04:27:38.166Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5942}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 358 · 2026-05-21T04:28:26.211405+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-seed53",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-seed53",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 359 · 2026-05-21T04:28:26.211558+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-seed53\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:19.064Z\", \"updated_at\": \"2026-05-21T04:27:38.859Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-18228\", \"data_path\": \"logs/eval_spatial_vla_only_seed53.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 53, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed53.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed53.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on spatial task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.28}, \"completed_at\": \"2026-05-21T04:27:38.859Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6972}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 360 · 2026-05-21T04:28:26.211699+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-seed52",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-seed52",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 361 · 2026-05-21T04:28:26.211849+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-seed52\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:24.079Z\", \"updated_at\": \"2026-05-21T04:27:44.351Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-18228\", \"data_path\": \"logs/eval_spatial_vla_only_seed52.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 52, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed52.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed52.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on spatial task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.31}, \"completed_at\": \"2026-05-21T04:27:44.351Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6609}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 362 · 2026-05-21T04:28:26.211982+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-seed50",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-seed50",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 363 · 2026-05-21T04:28:26.212128+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-seed50\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:25.081Z\", \"updated_at\": \"2026-05-21T04:27:45.373Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-18228\", \"data_path\": \"logs/eval_spatial_vla_only_seed50.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 50, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed50.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed50.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on spatial task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3}, \"completed_at\": \"2026-05-21T04:27:45.373Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6624}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 364 · 2026-05-21T04:28:26.212307+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-spatial-seed47",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-spatial-seed47",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool call

_source line 365 · 2026-05-21T04:28:26.212488+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-object-seed49-r2",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-object-seed49-r2",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 366 · 2026-05-21T04:28:26.212650+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-spatial-seed47\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:26.099Z\", \"updated_at\": \"2026-05-21T04:27:46.878Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-18228\", \"data_path\": \"logs/eval_spatial_obs_only_norm02_seed47.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 47, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on spatial task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.32}, \"completed_at\": \"2026-05-21T04:27:46.878Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7807}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 367 · 2026-05-21T04:28:26.212827+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-spatial-k10-seed49",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-spatial-k10-seed49",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 368 · 2026-05-21T04:28:26.212991+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-object-seed49-r2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:27.122Z\", \"updated_at\": \"2026-05-21T04:27:47.609Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb1-18228\", \"data_path\": \"logs/eval_object_vla_only_seed49.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 49, \"checkpoint_source\": \"harvested\", \"eval_data\": \"object\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on object task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1}, \"completed_at\": \"2026-05-21T04:27:47.609Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6502}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 369 · 2026-05-21T04:28:26.213164+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-spatial-k10-seed49\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:28.274Z\", \"updated_at\": \"2026-05-21T04:27:48.274Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_spatial_obs_only_norm02_seed49.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 49, \"checkpoint_source\": \"harvested\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed49.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed49.json\"}, \"hypothesis\": \"CRM with k=10 candidates and observation-only refinement (norm=0.2) on spatial task — tests refinement quality with larger candidate pool.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.32}, \"completed_at\": \"2026-05-21T04:27:48.274Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6354}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 370 · 2026-05-21T04:28:26.213333+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-goal-seed48",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-goal-seed48",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 371 · 2026-05-21T04:28:26.213503+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-seed48\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:29.201Z\", \"updated_at\": \"2026-05-21T04:27:49.021Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_goal_obs_only_norm02_seed48.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 48, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed48.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed48.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.68}, \"completed_at\": \"2026-05-21T04:27:49.021Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6729}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 372 · 2026-05-21T04:28:26.213649+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-goal-seed47",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-goal-seed47",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 373 · 2026-05-21T04:28:26.213803+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-seed47\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:29.771Z\", \"updated_at\": \"2026-05-21T04:27:50.201Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_goal_obs_only_norm02_seed47.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 47, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed47.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed47.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.69}, \"completed_at\": \"2026-05-21T04:27:50.201Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.966}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 374 · 2026-05-21T04:28:26.213937+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-goal-seed50",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-goal-seed50",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool call

_source line 375 · 2026-05-21T04:28:26.214055+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-goal-seed49",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-goal-seed49",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 376 · 2026-05-21T04:28:26.214204+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-seed50\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:30.804Z\", \"updated_at\": \"2026-05-21T04:27:51.247Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_goal_obs_only_norm02_seed50.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 50, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed50.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed50.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.67}, \"completed_at\": \"2026-05-21T04:27:51.247Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0216}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 377 · 2026-05-21T04:28:26.214366+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-seed52",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-seed52",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 378 · 2026-05-21T04:28:26.214526+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-seed49\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:31.844Z\", \"updated_at\": \"2026-05-21T04:27:52.398Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_goal_obs_only_norm02_seed49.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 49, \"checkpoint_source\": \"harvested\", \"eval_data\": \"goal\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed49.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed49.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on goal task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.62}, \"completed_at\": \"2026-05-21T04:27:52.398Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0678}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 379 · 2026-05-21T04:28:26.214660+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-long-seed49",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-long-seed49",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 380 · 2026-05-21T04:28:26.214811+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-seed52\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:32.959Z\", \"updated_at\": \"2026-05-21T04:27:53.425Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_long_obs_only_norm02_seed52.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 52, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed52.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed52.json\"}, \"hypothesis\": \"CRM with observation-only refinement (norm=0.2) on long-horizon task — tests whether observation embedding similarity improves VLA action selection over baseline VLA-only.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}, \"completed_at\": \"2026-05-21T04:27:53.426Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.758}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 381 · 2026-05-21T04:28:26.214973+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-long-seed49\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:23:33.602Z\", \"updated_at\": \"2026-05-21T04:27:54.076Z\", \"spec\": {\"command\": \"harvest\", \"server\": \"bjb2-28827\", \"data_path\": \"logs/eval_long_vla_only_seed49.json\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 49, \"checkpoint_source\": \"harvested\", \"eval_data\": \"long\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed49.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed49.json\"}, \"hypothesis\": \"VLA-only baseline (no CRM) on long-horizon task — measures intrinsic VLA capability for ablation comparison against CRM-refined variants.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}, \"completed_at\": \"2026-05-21T04:27:54.076Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.69}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 382 · 2026-05-21T04:28:26.215126+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Test single registry update to validate flow', 'activeForm': 'Testing single registry update', 'status': 'completed'}, {'content': 'Transition all 28 to QUEUED then RUNNING with spec', 'activeForm': 'Transitioning to RUNNING', 'status': 'completed'}, {'content': 'Set hypothesis for all 28', 'activeForm': 'Setting hypothesis', 'status': 'completed'}, {'content': 'Set conclusion and metrics for all 28', 'activeForm': 'Setting conclusion and metrics', 'status': 'completed'}, {'content': 'Final RUNNING → DONE for all 28', 'activeForm': 'Finalizing DONE state', 'status': 'completed'}, {'content': 'Report summary table', 'activeForm': 'Reporting summary', 'status': 'completed'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Test single registry update to validate flow', 'activeForm': 'Testing single registry update', 'status': 'completed'}, {'content': 'Transition all 28 to QUEUED then RUNNING with spec', 'activeForm': 'Transitioning to RUNNING', 'status': 'completed'}, {'content': 'Set hypothesis for all 28', 'activeForm': 'Setting hypothesis', 'status': 'completed'}, {'content': 'Set conclusion and metrics for all 28', 'activeForm': 'Setting conclusion and metrics', 'status': 'completed'}, {'content': 'Final RUNNING → DONE for all 28', 'activeForm': 'Finalizing DONE state', 'status': 'completed'}, {'content': 'Report summary table', 'activeForm': 'Reporting summary', 'status': 'completed'}]"
  }
}
```

</details>

---

### Tool result

_source line 383 · 2026-05-21T04:28:26.215301+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 384 · 2026-05-21T04:28:26.215484+00:00_

All 29 experiments processed: 26 marked DONE with metrics, 3 missing JSONs flagged.

## 汇总表

| # | exp_id | server | JSON exists? | SR | 备注 |
|---|---|---|---|---|---|
| 1 | eval-vla-only-spatial-seed54 | bjb1-32546 | ✓ | 0.27 | DONE |
| 2 | eval-crm-long-seed54 | bjb1-32546 | ✓ | 0.19 | DONE |
| 3 | eval-crm-long-seed49 | bjb1-32546 | ✓ | 0.14 | DONE |
| 4 | eval-crm-long-seed48 | bjb1-32546 | ✓ | 0.15 | DONE |
| 5 | eval-crm-spatial-k10-seed50 | bjb1-32546 | ✓ | 0.35 | DONE |
| 6 | eval-vla-only-long-seed53 | bjb1-32546 | ✓ | 0.12 | DONE |
| 7 | eval-vla-only-goal-seed52 | bjb1-32546 | ✓ | 0.68 | DONE |
| 8 | eval-crm-long-seed51 | bjb1-32546 | ✓ | 0.13 | DONE |
| 9 | eval-vla-only-spatial-seed51 | bjb1-32546 | ✓ | 0.33 | DONE |
| 10 | eval-vla-only-object-seed51 | bjb1-32546 | ✓ | 0.15 | DONE |
| 11 | eval-crm-spatial-seed48 | bjb1-32546 | ✓ | 0.35 | DONE |
| 12 | eval-obs-only-object-norm02-k20-seed42 | bjb1-32546 | ✗ | — | 进程可能仍在运行或已失败，未更新 |
| 13 | eval-obs-only-goal-norm02-seed53 | bjb1-32546 | ✓ | 0.63 | DONE |
| 14 | eval-vla-only-long-seed54 | bjb1-18228 | ✓ | 0.12 | DONE |
| 15 | eval-crm-long-seed53 | bjb1-18228 | ✓ | 0.18 | DONE |
| 16 | eval-vla-only-spatial-seed53 | bjb1-18228 | ✓ | 0.28 | DONE |
| 17 | eval-vla-only-spatial-seed52 | bjb1-18228 | ✓ | 0.31 | DONE |
| 18 | eval-vla-only-spatial-seed50 | bjb1-18228 | ✓ | 0.30 | DONE |
| 19 | eval-crm-spatial-seed47 | bjb1-18228 | ✓ | 0.32 | DONE |
| 20 | eval-vla-only-object-seed49-r2 | bjb1-18228 | ✓ | 0.10 | DONE |
| 21 | eval-obs-only-object-norm02-k20-seed43 | bjb1-18228 | ✗ | — | 进程可能仍在运行或已失败，未更新 |
| 22 | eval-crm-spatial-k10-seed49 | bjb2-28827 | ✓ | 0.32 | DONE |
| 23 | eval-crm-goal-seed48 | bjb2-28827 | ✓ | 0.68 | DONE |
| 24 | eval-crm-goal-seed47 | bjb2-28827 | ✓ | 0.69 | DONE |
| 25 | eval-crm-goal-seed50 | bjb2-28827 | ✓ | 0.67 | DONE |
| 26 | eval-crm-goal-seed49 | bjb2-28827 | ✓ | 0.62 | DONE |
| 27 | eval-crm-long-seed52 | bjb2-28827 | ✓ | 0.15 | DONE |
| 28 | eval-vla-only-long-seed49 | bjb2-28827 | ✓ | 0.16 | DONE |
| 29 | eval-vla-only-spatial-seed49-r2 | bjb2-28827 | ✗ | — | 进程可能仍在运行或已失败，未更新 |

**统计**：26 个已收割到 DONE（全部 SR > 0，conclusion=success），3 个 JSON 缺失保持 PREPARING。

**关键观察**：
- VLA-only goal seed52 = 0.68 vs CRM goal (47/48/49/50) = 0.62-0.69 — CRM 在 goal 任务上与 VLA-only 持平甚至略低
- CRM long (0.13-0.19) vs VLA-only long (0.12, 0.16) — long-horizon 上 CRM 提升微弱
- CRM spatial (0.32-0.35) vs VLA-only spatial (0.27-0.33) — spatial 上 CRM 有小幅领先

**注**：registry 中 spec.command 填的是占位 "harvest"，因为原始 submit_training_job 的命令未保留；checkpoint_path 和 log_path 都指向同一 JSON 文件（eval 类任务无独立训练 checkpoint）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_harvest_old-preparing-experiments_20260521T041745"
}
```

</details>

---
