# analysis obsonly norm02 seed42 vs seed43 partial

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 0
- **Tool calls:** 26
- **Original source:** `logs/chats/worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813.jsonl`
- **Structured JSON:** [`7152e5ab484ef4034c0b.json`](../../sessions/71/7152e5ab484ef4034c0b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

53 recorded events

### Tool call

_source line 1 · 2026-05-16T06:10:31.636242+00:00_

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
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
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

_source line 2 · 2026-05-16T06:10:31.636614+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T06:10:31.636863+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*obs_only*norm02*\" -o -name \"*obs-only*norm02*\" -o -name \"*obs_only*0.2*\" -o -name \"*obs_only*02*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*obs_only*norm02*\" -o -name \"*obs-only*norm02*\" -o -name \"*obs_only*0.2*\" -o -name \"*obs_only*02*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T06:10:31.637034+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.94}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T06:10:31.637178+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/runs/acr-vla-conformal-refinement/ -name \"*obs*only*seed43*\" -o -name \"*obs*only*norm02*seed43*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "find /root/runs/acr-vla-conformal-refinement/ -name \"*obs*only*seed43*\" -o -name \"*obs*only*norm02*seed43*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T06:10:31.637381+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T06:10:31.637515+00:00_

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
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
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

_source line 8 · 2026-05-16T06:10:31.637647+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"crm_spatial_train.log\\neval-object-v5-full.log\\neval_mag_obsonly_norm003.json\\neval_object_obs_only.json\\neval_object_vla_only_seed44.json\\nprecompute.log\\nreconvla_object.log\\nreconvla_spatial.log\\ntrain_crm.log\\ntrain_crm_v2.log\\nvla_only_spatial_K1.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.33}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T06:10:31.637792+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T06:10:31.637960+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.19,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.4,\\n      \\\"successes\\\": 4,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.5,\\n      \\\"successes\\\": 5,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    }\\n  }\\n}\\n\", \"stderr\": \"\", \"return_code\": 0}
…[truncated 63 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T06:10:31.638119+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/runs/acr-vla-conformal-refinement/ -name \"*obs*only*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "find /root/runs/acr-vla-conformal-refinement/ -name \"*obs*only*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T06:10:31.638254+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/runs/acr-vla-conformal-refinement/crm-train-v3-obs-only.log\\n/root/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm003-b2.log\\n/root/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm003.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T06:10:31.638406+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement/ -name \"*.json\" -path \"*/results/*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "find /root/acr-vla-conformal-refinement/ -name \"*.json\" -path \"*/results/*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T06:10:31.638533+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T06:10:31.638704+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/ -maxdepth 4 -name \"*norm02*\" -o -name \"*norm0.2*\" -o -name \"*eps02*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "find /root/ -maxdepth 4 -name \"*norm02*\" -o -name \"*norm0.2*\" -o -name \"*eps02*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T06:10:31.638835+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T06:10:31.638955+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/ -maxdepth 4 -name \"*seed43*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "find /root/ -maxdepth 4 -name \"*seed43*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T06:10:31.639074+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.33}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T06:10:31.639189+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/ -maxdepth 4 -name \"*seed42*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "find /root/ -maxdepth 4 -name \"*seed42*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T06:10:31.639325+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T06:10:31.639475+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/artifacts/**/*obs*only*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/artifacts/**/*obs*only*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T06:10:31.639592+00:00_

artifacts/eval-acr-object-v4-obs-only/report/eval_object_v4_obs_only_final.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T06:10:31.639705+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/MEMORY.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/MEMORY.md"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T06:10:31.639818+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T06:10:31.639929+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/eval-acr-object-v4-obs-only/report/eval_object_v4_obs_only_final.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/eval-acr-object-v4-obs-only/report/eval_object_v4_obs_only_final.md"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T06:10:31.640082+00:00_

1	# eval-acr-object-v4-obs-only — Final Results
2	
3	## Config
4	- Mode: crm_obs_only (CRM v3-norm)
5	- Benchmark: LIBERO object (10 tasks)
6	- max_correction_norm: 0.1
7	- Seed: 42, K=10 rollouts/task
8	- Checkpoint: crm_v3_norm/obs_only/crm_best.pt
9	
10	## Per-Task Success Rate
11	
12	| # | Task | obs_only | VLA-only | Δ |
13	|---|------|----------|----------|---|
14	| 1 | alphabet_soup | 0% | 0% | 0 |
15	| 2 | cream_cheese | 10% | 10% | 0 |
16	| 3 | salad_dressing | 20% | 20% | 0 |
17	| 4 | bbq_sauce | **40%** | 20% | **+20** |
18	| 5 | ketchup | 10% | 0% | +10 |
19	| 6 | tomato_sauce | 0% | 10% | -10 |
20	| 7 | butter | 10% | 0% | +10 |
21	| 8 | milk | 20% | 10% | +10 |
22	| 9 | chocolate_pudding | **50%** | 20% | **+30** |
23	| 10 | orange_juice | 30% | 30% | 0 |
24	| **Avg** | | **19.0%** | **12.0%** | **+7.0pp** |
25	
26	## Baseline Comparison
27	
28	| Method | Object 10-task SR | vs obs_only |
29	|--------|------------------|-------------|
30	| **obs_only (CRM v3-norm)** | **19.0%** | — |
31	| VLA-only (no correction) | 12.0% | -7.0pp |
32	| perdof (CRM v3-norm) | 11.0% | -8.0pp |
33	| argmin (partial 6/10) | ~6.7% | ~-12.3pp |
34	
35	## Conclusion: SUCCESS — Project Lives
36	
37	obs_only achieves **19.0% SR on object benchmark**, the strongest result among all CRM variants:
38	- **+7pp over VLA-only** (19% vs 12%) — correction improves the base policy
39	- **+8pp over perdof** (19% vs 11%) — obs_only >> perdof on object
40	- **+12.3pp over argmin partial** (19% vs ~6.7%) — massively outperforms argmin baseline
41	
42	Key observations:
43	- chocolate_pudding (50%) and bbq_sauce (40%) are the big winners, +30pp and +20pp over VLA-only
44	- The last 4 tasks (butter/milk/chocolate_pudding/orange_juice) boosted avg from 13.3% → 19.0%
45	- obs_only is the only CRM variant that shows clear, consistent improvement over VLA-only on object
46	
47	Cross-benchmark summary (obs_only CRM v3-norm, norm=0.1):
48	- Spatial: 35% (vs argmin 34%, +1pp — marginal)
49	- **Objec
…[truncated 50 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T06:10:31.640231+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/artifacts/**/*norm02*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/artifacts/**/*norm02*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T06:10:31.640373+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T06:10:31.640487+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/artifacts/**/*seed4*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/artifacts/**/*seed4*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T06:10:31.640597+00:00_

artifacts/seed43_env_check.md
artifacts/analysis/seed43_fisher_analysis.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T06:10:31.640760+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/artifacts/**/*eval*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/artifacts/**/*eval*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T06:10:31.640915+00:00_

artifacts/eval-reconvla-spatial-v1-diag.md
artifacts/diag-eval-v6-batch-failure.md
artifacts/_project/report/object_eval_commands.md
artifacts/object_eval_commands.md
artifacts/report_eval_progress.md
artifacts/ablation_eval_commands.md
artifacts/eval-acr-object-v4-obs-only/report/eval_object_v4_obs_only_final.md
artifacts/eval-acr-object-v4-scalar/report/eval-acr-object-v4-scalar-report.md
artifacts/_project/intermediate/merge_eval_results_info.txt

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T06:10:31.641044+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/seed43_env_check.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/seed43_env_check.md"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T06:10:31.641179+00:00_

1	# bjb1-18228 Object Benchmark Eval 环境检查 (seed=43)
2	
3	**日期**: 2026-05-15
4	
5	## 检查结果
6	
7	### 1. Object Benchmark 数据 — OK
8	
9	- 路径: `/root/autodl-tmp/libero_data/libero_object/`
10	- 大小: 7.0 GB
11	- 任务数: 10 个 hdf5 文件（alphabet_soup, bbq_sauce, butter, chocolate_pudding, cream_cheese, ketchup, milk, orange_juice, salad_dressing, tomato_sauce）
12	
13	### 2. Checkpoints — OK
14	
15	| Checkpoint | 路径 | 大小 | 时间 |
16	|---|---|---|---|
17	| obs_only | `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt` | 1.3 MB | May 15 06:00 |
18	| perdof | `/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt` | 1.4 MB | May 15 03:57 |
19	
20	### 3. evaluate.py — OK
21	
22	- `--benchmark` 参数: 支持 `object`（默认值即为 object）
23	- `--seed` 参数: 支持，默认 42，可设为 43
24	- 支持模式: vla_only, crm_scalar, crm_perdof, acr_vla, reconvla
25	
26	### 4. GPU 状态 — OK
27	
28	| GPU | 型号 | 显存使用 | 利用率 | 状态 |
29	|---|---|---|---|---|
30	| cuda:0 | RTX 4090 | 3594 / 24564 MiB | 23% | 占用 |
31	| cuda:1 | RTX 4090 | 2005 / 24564 MiB | 24% | 占用 |
32	| cuda:2 | RTX 4090 | 1 / 24564 MiB | 0% | **空闲** |
33	| cuda:3 | RTX 4090 | 1 / 24564 MiB | 0% | **空闲** |
34	
35	### 5. SmolVLA 模型 — OK
36	
37	- 路径: `/root/autodl-tmp/models/smolvla_libero/`
38	- model.safetensors: 906 MB
39	- config.json + preprocessor/postprocessor 文件齐全
40	
41	## 结论
42	
43	**可以直接部署。** 所有资源就绪，无需额外下载或准备：
44	- Object benchmark 数据 10 个任务完整
45	- obs_only 和 perdof 两个 checkpoint 均存在
46	- evaluate.py 支持 `--benchmark object --seed 43`
47	- cuda:2 和 cuda:3 完全空闲（各 24GB）
48	- SmolVLA 模型已下载
49	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T06:10:31.641359+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/artifacts/**/*norm*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/artifacts/**/*norm*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T06:10:31.641480+00:00_

artifacts/_project/data/norm_stats_v3_summary.txt

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T06:10:31.641596+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/artifacts/**/*ablation*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/artifacts/**/*ablation*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-16T06:10:31.641708+00:00_

artifacts/ablation_eval_commands.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T06:10:31.641832+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/artifacts/**/*report*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/artifacts/**/*report*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-16T06:10:31.641951+00:00_

artifacts/dream_reports/dream_20260513T015051/best/review_report.md
artifacts/dream_reports/dream_20260513T015051/median/review_report.md
artifacts/libero-smolvla-env-report.md
artifacts/dream_reports/dream_20260513T023849/best/review_report.md
artifacts/dream_reports/dream_20260513T023849/median/review_report.md
artifacts/dream_reports/dream_20260513T023849/worst/review_report.md
artifacts/_project/report/v4_deployment_report.md
artifacts/reconvla-comparison-report.md
artifacts/report_eval_progress.md
artifacts/report_running_status.md
artifacts/_project/report/progress-report-20260515-0526.md
artifacts/literature_gap_report.md
artifacts/eval-acr-object-v4-scalar/report/eval-acr-object-v4-scalar-report.md
artifacts/citation_audit_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-16T06:10:31.642070+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/report_eval_progress.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/report_eval_progress.md"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-16T06:10:31.642240+00:00_

1	# Eval 进度检查 — 2026-05-14 02:17 UTC
2	
3	## 各实验状态
4	
5	| exp_id | server | GPU | PID alive? | tasks done/total | 当前成功率 | 最新 log 摘要 | 预计剩余时间 |
6	|--------|--------|-----|-----------|-----------------|-----------|--------------|-------------|
7	| eval-vla-mean-spatial | bjb2 | cuda:0 (4090D) | ✅ 143106, 15.1h | 7.5/10 | 28/70 = 40.0% | task 8 rollout 5/10, 0/5 | ~5h |
8	| eval-acr-spatial-v3 | bjb1 | cuda:0 (4090) | ✅ 197062, 6h | 4/10 | 1/40 = 2.5% | 完成 task 4, 正跑 task 5 | ~9h |
9	| eval-acr-object-v3 | bjb1 | cuda:3 (4090) | ✅ 197803, 6h | 4/10 | 0/40 = 0.0% | 完成 task 4, 正跑 task 5 | ~9h |
10	| eval-argmin-only-spatial | bjb1 | cuda:1 (4090) | ✅ 231426, 29min | 0/10 | — | task 1 运行中, 无 rollout 输出 | ~14h |
11	| eval-tiny-correction-spatial | bjb1 | cuda:2 (4090) | ✅ 232820, 28min | 0.5/10 | task1: 4/5 | task 1 rollout 5/10 | ~9h |
12	
13	### 各 task 成功率明细
14	
15	**eval-vla-mean-spatial** (vla_only, baseline_mode=mean, spatial):
16	| task | success |
17	|------|---------|
18	| bowl_between_plate_ramekin → plate | 7/10 (70%) |
19	| bowl_next_to_ramekin → plate | 10/10 (100%) |
20	| bowl_from_table_center → plate | 0/10 (0%) |
21	| bowl_on_cookie_box → plate | 3/10 (30%) |
22	| bowl_in_top_drawer → plate | 0/10 (0%) |
23	| bowl_on_ramekin → plate | 0/10 (0%) |
24	| bowl_next_to_cookie_box → plate | 8/10 (80%) |
25	| bowl_on_stove → plate | running (0/5 so far) |
26	
27	**eval-acr-spatial-v3** (acr_vla, crm_v2/perdof, spatial):
28	| task | success |
29	|------|---------|
30	| bowl_between_plate_ramekin → plate | 1/10 (10%) |
31	| bowl_next_to_ramekin → plate | 0/10 (0%) |
32	| bowl_from_table_center → plate | 0/10 (0%) |
33	| bowl_on_cookie_box → plate | 0/10 (0%) |
34	
35	**eval-acr-object-v3** (acr_vla, crm_v2/perdof, object):
36	| task | success |
37	|------|---------|
38	| alphabet_soup → basket | 0/10 (0%) |
39	| cream_cheese → basket | 0/10 (0%) |
40	| salad_dressing → basket | 0/10 (0%) |
41	| bbq_sauce → basket | 0/10 (0%) |
42	
43	**eval-tiny-correction-spatial**
…[truncated 1960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-16T06:10:31.642420+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/ablation_eval_commands.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/ablation_eval_commands.md"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-16T06:10:31.642578+00:00_

1	# Ablation Eval Commands
2	
3	## 代码审查结果
4	
5	### evaluate.py 中 ablation modes 状态：✅ 全部就绪
6	
7	`--mode` 接受 6 个值：`vla_only`, `crm_scalar`, `crm_perdof`, `acr_vla`, `crm_obs_only`, `reconvla`
8	
9	两个 ablation mode 的 CRM 加载逻辑：
10	
11	| mode | uncertainty_dim | uf_input 传入 CRM | 与 train_crm.py 一致性 |
12	|------|----------------|-------------------|----------------------|
13	| `crm_obs_only` | 0 | `None` | ✅ `input_mode=obs_only` → `unc_dim=0`, `crm(ba, None, obs_feat)` |
14	| `crm_scalar` | 3 | `_to_scalar_uf(uf)` 压缩为 3D | ✅ `input_mode=scalar_unc` → `unc_dim=3`, `_to_scalar_uf()` 同函数 |
15	
16	`_to_scalar_uf()` 实现：将 40D uncertainty 压缩为 3D — `[per_dof_std.norm(), interval_width.mean(), coverage.mean()]`，evaluate.py 和 train_crm.py 中完全一致。
17	
18	CRM forward 中 `uncertainty_features=None` 时跳过拼接，只用 `base_action + obs_features`，与训练 obs_only 模式匹配。
19	
20	**无 bug 风险。** 训练与评估的 uncertainty_dim 映射、uf 处理、CRM 输入构造完全对齐。
21	
22	### max_correction_norm
23	
24	命令行 `--max_correction_norm` 可覆盖 checkpoint 中保存的值。不指定则用 checkpoint 默认值（训练时设为 1.42）。
25	
26	---
27	
28	## Eval 命令
29	
30	### 1. obs_only ablation
31	
32	```bash
33	source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
34	cd /root/acr-vla-conformal-refinement && \
35	HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
36	python -u src/evaluate.py \
37	  --mode crm_obs_only \
38	  --benchmark spatial \
39	  --n_rollouts 10 \
40	  --seed 42 \
41	  --K 10 \
42	  --checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt \
43	  --output_file /root/autodl-tmp/eval_results/ablation_obs_only_spatial.json
44	```
45	
46	### 2. scalar_unc ablation
47	
48	```bash
49	source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
50	cd /root/acr-vla-conformal-refinement && \
51	HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
52	python -u src/evaluate.py \
53	  --mode crm_scalar \
54	  --benchmark spatial \
55	  --n_rollouts 10 \
56	  --seed 42 \
57	  --K 10 \
58	  --checkpoint /root/autodl-tmp/checkpoints/crm_v3_nor
…[truncated 914 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-16T06:10:31.642743+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/progress-report-20260515-0526.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/progress-report-20260515-0526.md"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-16T06:10:31.642905+00:00_

1	## 进度总结 (2026-05-15 05:26 UTC)
2	
3	| 实验 | 服务器 | 进度 | 关键指标 | 预计完成 |
4	|------|--------|------|---------|---------|
5	| eval-vla-mean-spatial | bjb2 GPU0 | 9/10 tasks | avg 34.4% (31/90) | ~2h |
6	| eval-argmin-only-spatial | bjb1 GPU1 | 3/10 tasks (T4 rollout 5/10) | avg 53.3% (16/30) | ~8h |
7	| eval-tiny-correction-spatial | bjb1 GPU2 | 3/10 tasks (T4 rollout 5/10) | avg 53.3% (16/30) | ~8h |
8	| **eval-acr-spatial-v4-default** | **bjb1 GPU0** | **0/10 — 未运行!** | **无进程，需重启** | **N/A** |
9	| eval-acr-spatial-v4-small | bjb1 GPU3 | 1/10 tasks | T1: 60% (6/10) | ~9h |
10	| crm-train-v3-norm-obs-only | bjb1 GPU0 | epoch 26/50 | best val_loss=0.01669 (ep23) | ~35m |
11	| crm-train-v3-norm-scalar-unc | bjb1 GPU3 | epoch 26/50 | best val_loss=0.03998 (ep26, 仍在下降) | ~35m |
12	
13	### Eval 详细结果（已完成 tasks）
14	
15	**eval-vla-mean-spatial (K=10 mean baseline):**
16	| Task | Success Rate |
17	|------|-------------|
18	| T1 between_plate_ramekin | 70% (7/10) |
19	| T2 next_to_ramekin | 100% (10/10) |
20	| T3 from_table_center | 0% (0/10) |
21	| T4 on_cookie_box | 30% (3/10) |
22	| T5 in_top_drawer | 0% (0/10) |
23	| T6 on_ramekin | 0% (0/10) |
24	| T7 next_to_cookie_box | 80% (8/10) |
25	| T8 on_stove | 0% (0/10) |
26	| T9 next_to_plate | 30% (3/10) |
27	
28	**eval-argmin-only-spatial (reconvla K=10 argmin):**
29	T1: 60%, T2: 100%, T3: 0% → avg 53.3%
30	
31	**eval-tiny-correction-spatial (acr_vla max_norm=0.05):**
32	T1: 70%, T2: 90%, T3: 0% → avg 53.3%
33	
34	**eval-acr-spatial-v4-small (v3-norm, max_norm=0.1):**
35	T1: 60%
36	
37	## GPU 利用率
38	
39	**bjb1-18228 (4× RTX 4090):**
40	| GPU | 利用率 | 显存 | 负载 |
41	|-----|--------|------|------|
42	| 0 | 71% | 17441/24564 MiB | crm-train-obs-only + stale v3 eval tmux |
43	| 1 | 20% | 1423/24564 MiB | eval-argmin-only |
44	| 2 | 23% | 1459/24564 MiB | eval-tiny-correction |
45	| 3 | 70% | 2022/24564 MiB | eval-v4-small + crm-train-scalar-unc |
46	
47	**bjb2-40593 (1× RTX 4090 D):**
48	| GPU | 利用率 | 显存 |
49	|-----|--------|------|
50	
…[truncated 494 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-16T06:10:31.643060+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/artifacts/**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/artifacts/**/*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-16T06:10:31.643204+00:00_

artifacts/dream_reports/dream_20260513T015051/best/review_report.md
artifacts/dream_reports/dream_20260513T015051/median/review_report.md
artifacts/dream_reports/dream_20260513T023849/best/paper_framing.md
artifacts/libero-smolvla-env-report.md
artifacts/dream_reports/dream_20260513T023849/median/paper_framing.md
artifacts/dream_reports/dream_20260513T023849/worst/paper_framing.md
artifacts/dream_reports/dream_20260513T023849/best/review_report.md
artifacts/dream_reports/dream_20260513T023849/median/review_report.md
artifacts/dream_reports/dream_20260513T023849/worst/review_report.md
artifacts/pipeline-dimension-verification.md
artifacts/smolvla-libero-finetune-survey.md
artifacts/lerobot-pipeline-alignment.md
artifacts/_project/report/v4_deployment_report.md
artifacts/eval-reconvla-spatial-v1-diag.md
artifacts/_project/report/claim-strength-analysis.md
artifacts/precompute-k5-analysis.md
artifacts/precompute-k5/report/precompute-k5-analysis.md
artifacts/reconvla-comparison-report.md
artifacts/_project/report/next_batch_plan.md
artifacts/diag-eval-v6-batch-failure.md
artifacts/_project/report/object_eval_commands.md
artifacts/object_eval_commands.md
artifacts/_project/report/competitor_analysis.md
artifacts/competitor_analysis.md
artifacts/_project/report/spatial_comparison_template.md
artifacts/spatial_comparison_template.md
artifacts/_project/report/correction_degradation_literature.md
artifacts/correction_degradation_literature.md
artifacts/crm_bug_audit.md
artifacts/_project/report/crm_bug_audit.md
artifacts/_project/report/fix_plan_code_sketch.md
artifacts/fix_plan_code_sketch.md
artifacts/crm-train-v2-k5/intermediate/crm-train-v2-k5-blocked.md
artifacts/report_eval_progress.md
artifacts/ablation_eval_commands.md
artifacts/report_running_status.md
artifacts/_project/report/progress-report-20260515-0526.md
artifacts/_project/report/competitive_analysis_20260515.md
artifacts/competitive_analysis_20260515.md
artifacts/spatial_analysis_prep.md
artifacts/_project/re
…[truncated 1103 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-16T06:10:31.643380+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/magnitude_sweep_summary.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/magnitude_sweep_summary.md"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-16T06:10:31.643562+00:00_

1	# Magnitude Sweep Summary (2026-05-16)
2	
3	## Spatial Benchmark (DONE points only)
4	
5	| norm | obs_only | perdof | gap | obs_only status | perdof status |
6	|------|----------|--------|-----|-----------------|---------------|
7	| 0.03 | — | 30.0% | — | 7/10 RUNNING | 10/10 DONE |
8	| 0.05 | 35.0% | 31.0% | +4.0pp | 10/10 DONE | 10/10 DONE |
9	| 0.10 | 35.0% | 35.0% | 0pp | 10/10 DONE | 10/10 DONE |
10	| 0.20 | 35.0% | — | — | 10/10 DONE | killed (6/10 partial 28.3%) |
11	| 0.30 | 36.0% | 26.0% | +10pp | 10/10 DONE | 10/10 DONE |
12	
13	**Key finding**: obs_only stable 35-36% across [0.05, 0.30]. perdof peaks at 0.10 (35%) and collapses to 26% at 0.30 (-9pp).
14	
15	Baselines: argmin 34%, VLA-only 30%, VLA-mean 32%.
16	
17	## Object Benchmark (in progress)
18	
19	| norm | obs_only | perdof | status |
20	|------|----------|--------|--------|
21	| 0.03 | RUNNING (2/10) | RUNNING (1/10) | bjb1-32546, bjb2-28827 |
22	| 0.05 | RUNNING (2/10) | RUNNING (1/10) | bjb2-28827 |
23	| 0.10 | **19.0% FINAL** | **11.0% FINAL** | from main eval experiments |
24	| 0.20 | **22.0% FINAL** | RUNNING (2/10) | obs_only done, perdof on bjb1-32546 |
25	| 0.30 | RUNNING (2/10) | RUNNING (0/10) | bjb2-28827 |
26	
27	Baselines: argmin 12%, VLA-only 12%, VLA-mean 12%.
28	
29	**obs_only 0.2 > obs_only 0.1** (22% vs 19%, +3pp): suggests moderate correction magnitude may be optimal for object.
30	
31	## Narrative for Paper
32	
33	1. **obs_only is robust to norm scaling**: spatial 35-36% across 6× range [0.05, 0.30]; object 19-22% at [0.1, 0.2]
34	2. **perdof is fragile**: spatial peaks at 0.10 (35%), drops to 26% at 0.30; object 11% at 0.10
35	3. **Unbounded correction (norm≈1.42) is catastrophic**: 0% SR for both variants (eval-acr-object-v4-default, eval-acr-spatial-v4-default)
36	4. **Safe operating range**: ε ∈ [0.05, 0.2] for obs_only; ε = 0.1 only for perdof
37	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-16T06:10:31.643711+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/results_tables.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/results_tables.md"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-16T06:10:31.643891+00:00_

1	# ACR-VLA Experiment Results Tables
2	
3	> Generated: 2026-05-15 | All numbers from registry. Percentages = success rate (%).
4	
5	---
6	
7	## Table 1: Object Benchmark 6-way Comparison (seed=42, all FINAL 10/10 tasks)
8	
9	| Method | Exp ID | **Overall SR** | alphabet_soup | cream_cheese | salad_dressing | bbq_sauce | ketchup | tomato_sauce | butter | milk | chocolate_pudding | orange_juice |
10	|--------|--------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
11	| **obs_only (norm=0.1)** | `eval-acr-object-v4-obs-only` | **19%** | 0 | 10 | 20 | 40 | 10 | 0 | 10 | 20 | 50 | 30 |
12	| argmin (K=10) | `eval-reconvla-object` | **12%** | 0 | 0 | 10 | 30 | 0 | 0 | 10 | 10 | 30 | 30 |
13	| VLA-only (K=1) | `eval-vla-only-object` | **12%** | 0 | 10 | 20 | 20 | 0 | 10 | 0 | 10 | 20 | 30 |
14	| VLA-mean (K=10) | `eval-vla-mean-object` | **12%** | 0 | 0 | 10 | 30 | 10 | 10 | 0 | 20 | 30 | 10 |
15	| perdof (norm=0.1) | `eval-acr-object-v4-perdof` | **11%** | 0 | 0 | 20 | 30 | 0 | 0 | 10 | 0 | 20 | 30 |
16	| scalar (norm=0.1) | `eval-acr-object-v4-scalar` | **9%** | 0 | 0 | 10 | 10 | 0 | 0 | 10 | 10 | 30 | 20 |
17	
18	**Key findings:**
19	- obs_only leads by +7pp over all baselines
20	- All methods cluster on chocolate_pudding and bbq_sauce (easiest tasks)
21	- alphabet_soup is universally 0% across all methods
22	
23	---
24	
25	## Table 2: Spatial Benchmark 6-way Comparison (seed=42, all FINAL 10/10 tasks)
26	
27	Task abbreviations: T0=between_plate_and_ramekin, T1=next_to_ramekin, T2=from_table_center, T3=on_cookie_box, T4=in_top_drawer, T5=on_ramekin, T6=next_to_cookie_box, T7=on_stove, T8=next_to_plate, T9=on_wooden_cabinet
28	
29	| Method | Exp ID | **Overall SR** | T0 | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 |
30	|--------|--------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
31	| **obs_only (norm=0.1)** | `eval-acr-spatial-v4-obs-only-r3` | **35%** | 90 | 100 | 0 | 40 | 10 | 0 | 90 | 0 | 20 | 0 |
32	| **perdof (norm=0.1)** | `eval-acr-spatial-v4-small-r2` | **35%** 
…[truncated 6621 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-16T06:10:31.644117+00:00_

找到所有数据了。以下是分析。

## Seed42 obs_only norm=0.2 逐 task 累计

| # | Task | SR | 累计 SR |
|---|------|----|---------|
| 1 | alphabet_soup | 0% | 0.0% |
| 2 | cream_cheese | 0% | 0.0% |
| 3 | salad_dressing | 30% | 10.0% |
| 4 | bbq_sauce | 40% | 17.5% |
| 5 | ketchup | 20% | 18.0% |
| 6 | tomato_sauce | 10% | 16.7% |
| 7 | **butter** | **10%** | **15.7%** |
| 8 | milk | 20% | 16.25% |
| 9 | chocolate_pudding | **60%** | **21.1%** |
| 10 | orange_juice | 30% | **22.0%** |

## 对比 seed43 前 7 task

| | seed42 | seed43 | Δ |
|---|--------|--------|---|
| 7-task partial | **15.7%** | **12.9%** | -2.9pp |
| 7-task sum (成功数) | 11/70 | 9/70 | -2 |

差距来自：
- ketchup: seed42=20%, seed43=0% (-2 successes)
- cream_cheese: seed42=0%, seed43=10% (+1)
- salad_dressing: seed42=30%, seed43=20% (-1)

## Seed43 翻盘分析

Seed42 的最后 3 个 task (milk/choc_pudding/OJ) 拿了 **20+60+30 = 110**，平均 **36.7%**，把 partial 从 15.7% 拉到 22.0%（+6.3pp）。

Seed43 当前 7-task sum = 9 (90/1000). 各目标需要的剩余 3 task 均值：

| 目标 | 需 3 task 总和 | 需均值 | 可能性 |
|------|--------------|--------|--------|
| 追平 22% | 130 | 43.3% | **困难** — seed42 同样 3 task 只拿了 36.7% |
| 追平 19% (norm=0.1) | 100 | 33.3% | **有希望** — 如果 choc_pudding≥50% + OJ≥30% |
| 达到 17% | 80 | 26.7% | **大概率** — choc_pudding 是全局最易 task |

## 结论

1. **Seed42 前 7 task 也只有 15.7%**，后 3 task 拉了 +6.3pp。所以后段翻盘是真实现象，主要靠 chocolate_pudding (60%)。

2. **Seed43 翻盘空间有限但存在。** 最可能落在 **17-20%** 区间。追平 22% 需要 3 task 均值 43.3%，比 seed42 同 3 task 的 36.7% 还高，不太现实。

3. **chocolate_pudding 是关键变量。** 如果 seed43 也能拿到 50-60%，最终大概率 18-20%；如果掉到 30% 以下，可能只有 15-16%。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813"
}
```

</details>

---
