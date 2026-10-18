# exp exp 005 priority1 v2

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 55
- **Recorded user turns:** 0
- **Tool calls:** 27
- **Original source:** `logs/chats/worker_exp_exp-005-priority1-v2_20260522T144606.jsonl`
- **Structured JSON:** [`f6d8cb4e96f9754e52a5.json`](../../sessions/f6/f6d8cb4e96f9754e52a5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

55 recorded events

### Tool call

_source line 1 · 2026-05-22T14:49:50.744284+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__register_artifact",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__register_artifact",
    "max_results": "6"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T14:49:50.744613+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T14:49:50.744836+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "ls -la /root/entrainment_gated_ft/models/ | grep -iE 'GLA|DeltaNet|HGRN[^2]'",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "ls -la /root/entrainment_gated_ft/models/ | grep -iE 'GLA|DeltaNet|HGRN[^2]'",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T14:49:50.744983+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T14:49:50.745111+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "du -sh /root/entrainment_gated_ft/models/340M-20B-GLA-hybrid-3-1 /root/entrainment_gated_ft/models/340M-20B-DeltaNet-hybrid-3-1 /root/entrainment_gated_ft/models/340M-20B-HGRN-hybrid-3-1 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "du -sh /root/entrainment_gated_ft/models/340M-20B-GLA-hybrid-3-1 /root/entrainment_gated_ft/models/340M-20B-DeltaNet-hybrid-3-1 /root/entrainment_gated_ft/models/340M-20B-HGRN-hybrid-3-1 2>&1",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T14:49:50.745237+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T14:49:50.745353+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "ls /root/autodl-tmp/.hf_cache/hub/ 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "ls /root/autodl-tmp/.hf_cache/hub/ 2>&1",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T14:49:50.745469+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T14:49:50.745583+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "ps aux | grep -E 'lm_eval|download|huggingface' | grep -v grep",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "ps aux | grep -E 'lm_eval|download|huggingface' | grep -v grep",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T14:49:50.745721+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T14:49:50.745848+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "ls /root/entrainment_gated_ft/results/exp005_zoo_expansion/ 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "ls /root/entrainment_gated_ft/results/exp005_zoo_expansion/ 2>&1",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T14:49:50.745966+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T14:49:50.746109+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "ls -la /root/entrainment_gated_ft/models/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "ls -la /root/entrainment_gated_ft/models/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-22T14:49:50.746222+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "du -sh /root/entrainment_gated_ft/models/340M-20B-GLA-hybrid-3-1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "du -sh /root/entrainment_gated_ft/models/340M-20B-GLA-hybrid-3-1",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T14:49:50.746330+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "ls /root/entrainment_gated_ft/models/340M-20B-GLA-hybrid-3-1/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "ls /root/entrainment_gated_ft/models/340M-20B-GLA-hybrid-3-1/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-22T14:49:50.746437+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "ls /root/entrainment_gated_ft/models/340M-20B-DeltaNet-hybrid-3-1/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "ls /root/entrainment_gated_ft/models/340M-20B-DeltaNet-hybrid-3-1/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T14:49:50.746544+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "ls /root/entrainment_gated_ft/models/340M-20B-HGRN-hybrid-3-1/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "ls /root/entrainment_gated_ft/models/340M-20B-HGRN-hybrid-3-1/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T14:49:50.746690+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 76\\ndrwxr-xr-x 20 root root 4096 May 22 22:22 .\\ndrwxr-xr-x  9 root root 4096 May 22 19:26 ..\\ndrwxr-xr-x  2 root root 4096 May 22 21:51 340M-20B-GLA-hybrid-3-1\\ndrwxr-xr-x  2 root root 4096 May 18 14:09 340M-20B-GatedDeltaNet-New-hybrid-24-1\\ndrwxr-xr-x  2 root root 4096 May 18 14:11 340M-20B-GatedDeltaNet-hybrid-12-1\\ndrwxr-xr-x  2 root root 4096 May 18 14:15 340M-20B-GatedDeltaNet-hybrid-3-1\\ndrwxr-xr-x  2 root root 4096 May 18 14:13 340M-20B-GatedDeltaNet-hybrid-6-1\\ndrwxr-xr-x  2 root root 4096 May 18 14:07 340M-20B-GatedDeltaNet-pure-baseline\\ndrwxr-xr-x  2 root root   10 May 22 20:50 340M-20B-HGRN-hybrid-3-1\\ndrwxr-xr-x  2 root root 4096 May 18 14:19 340M-20B-HGRN2-hybrid-12-1\\ndrwxr-xr-x  2 root root 4096 May 18 14:18 340M-20B-HGRN2-hybrid-24-1\\ndrwxr-xr-x  2 root root 4096 May 18 14:23 340M-20B-HGRN2-hybrid-3-1\\ndrwxr-xr-x  2 root root 4096 May 18 14:21 340M-20B-HGRN2-hybrid-6-1\\ndrwxr-xr-x  2 root root 4096 May 18 14:16 340M-20B-HGRN2-pure-baseline\\ndrwxr-xr-x  2 root root 4096 May 18 14:29 340M-20B-RetNet-hybrid-12-1\\ndrwxr-xr-x  2 root root 4096 May 18 14:27 340M-20B-RetNet-hybrid-24-1\\ndrwxr-xr-x  2 root root 4096 May 18 14:32 340M-20B-RetNet-hybrid-3-1\\ndrwxr-xr-x  2 root root 4096 May 18 14:30 340M-20B-RetNet-hybrid-6-1\\ndrwxr-xr-x  2 root root 4096 May 18 14:25 340M-20B-RetNet-pure\\ndrwxr-xr-x  2 root root 4096 May 18 14:34 transformer_340M_baseline\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.62}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T14:49:50.746834+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "ls /root/entrainment_gated_ft/results/exp005_zoo_expansion/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "ls /root/entrainment_gated_ft/results/exp005_zoo_expansion/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T14:49:50.746954+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"1.3G\\t/root/entrainment_gated_ft/models/340M-20B-GLA-hybrid-3-1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.8}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-22T14:49:50.747070+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"README.md\\nconfig.json\\nconfiguration.json\\ngeneration_config.json\\nmodel.safetensors\\nspecial_tokens_map.json\\ntokenizer.json\\ntokenizer_config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.71}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T14:49:50.747182+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/entrainment_gated_ft/models/340M-20B-DeltaNet-hybrid-3-1/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 1.71}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-22T14:49:50.747293+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.69}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-22T14:49:50.747406+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"analyze_6arch.py\\npriority1.log\\npriority1_v2.log\\npriority1_v3.log\\nrun_all.log\\nrun_priority1.sh\\nrun_priority1_v2.sh\\nrun_priority1_v3.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.19}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-22T14:49:50.747560+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "cat /root/entrainment_gated_ft/results/exp005_zoo_expansion/priority1_v3.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "cat /root/entrainment_gated_ft/results/exp005_zoo_expansion/priority1_v3.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-22T14:49:50.747699+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "ls /root/entrainment_gated_ft/models/340M-20B-GatedDeltaNet-hybrid-3-1/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "ls /root/entrainment_gated_ft/models/340M-20B-GatedDeltaNet-hybrid-3-1/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T14:49:50.747839+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-22T14:49:50.748127+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== Priority 1 v3 START Fri May 22 20:53:27 CST 2026 ===\\nDownloading 340M-20B-GLA-hybrid-3-1 via ModelScope...\\n2026-05-22 20:53:30,534 - modelscope - INFO - Got 8 files, start to download ...\\nDownloading Model from https://www.modelscope.cn to directory: /root/autodl-tmp/.ms_cache/m-a-p/340M-20B-GLA-hybrid-3-1\\n\\rProcessing 8 items:   0%|          | 0.00/8.00 [00:00<?, ?it/s]\\n\\rDownloading [config.json]:   0%|          | 0.00/1.11k [00:00<?, ?B/s]\\u001b[A\\n\\n\\rDownloading [configuration.json]:   0%|          | 0.00/64.0 [00:00<?, ?B/s]\\u001b[A\\u001b[A\\n\\n\\n\\rDownloading [generation_config.json]:   0%|          | 0.00/111 [00:00<?, ?B/s]\\u001b[A\\u001b[A\\u001b[A\\n\\n\\n\\n\\rDownloading [model.safetensors]:   0%|          | 0.00/1.24G [00:00<?, ?B/s]\\u001b[A\\u001b[A\\u001b[A\\u001b[A\\n\\n\\n\\n\\n\\rDownloading [README.md]:   0%|          | 0.00/1.34k [00:00<?, ?B/s]\\u001b[A\\u001b[A\\u001b[A\\u001b[A\\u001b[A\\n\\n\\n\\n\\n\\n\\rDownloading [special_tokens_map.json]:   0%|          | 0.00/414 [00:00<?, ?B/s]\\u001b[A\\u001b[A\\u001b[A\\u001b[A\\u001b[A\\u001b[A\\n\\n\\n\\n\\n\\n\\n\\rDownloading [tokenizer.json]:   0%|          | 0.00/3.34M [00:00<?, ?B/s]\\u001b[A\\u001b[A\\u001b[A\\u001b[A\\u001b[A\\u001b[A\\u001b[A\\n\\n\\n\\n\\n\\n\\n\\n\\rDownloading [tokenizer_config.json]:   0%|          | 0.00/1.00k [00:00<?, ?B/s]\\u001b[A\\u001b[A\\u001b[A\\u001b[A\\u001b[A\\u001b[A\\u001b[A\\u001b[A\\n\\n\\n\\rDownloading [generation_config.json]: 100%|██████████| 111/111 [00:00<00:00, 231B/s]\\u001b[A\\u001b[A\\u001b[A\\rDownloading [generation_config.json]: 100%|██████████| 111/111 [00:00<00:00, 231B/s]\\n\\rProcessing 8 items:  12%|█▎        | 1.00/8.00 [00:00<00:03, 2.05it/s]\\n\\n\\n\\n\\n\\n\\rDownloading [special_tokens_map.json]: 100%|██████████| 414/414 [00:00<00:00, 546B/s]\\u001b[A\\u001b[A\\u001b[A\\u001b[A\\u001b[A\\u001b[A\\rDownloading [special_tokens_map.json]: 100%|███████
…[truncated 8527 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-22T14:49:50.748295+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"README.md\\nconfig.json\\nconfiguration.json\\ngeneration_config.json\\nmodel.safetensors\\nspecial_tokens_map.json\\ntokenizer.json\\ntokenizer_config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.71}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-22T14:49:50.748416+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-22T14:49:50.748570+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "tail -80 /root/entrainment_gated_ft/results/exp005_zoo_expansion/priority1_v3.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "tail -80 /root/entrainment_gated_ft/results/exp005_zoo_expansion/priority1_v3.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-22T14:49:50.748715+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:huggingface.co m-a-p 340M-20B DeltaNet hybrid",
  "allowed_domains": "['huggingface.co']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:huggingface.co m-a-p 340M-20B DeltaNet hybrid",
    "allowed_domains": "['huggingface.co']"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-22T14:49:50.748903+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n\\n\\n\\rDownloading [model.safetensors]:  96%|█████████▌| 1.19G/1.24G [55:09<02:23, 385kB/s]\\u001b[A\\u001b[A\\u001b[A\\u001b[A\\n\\n\\n\\n\\rDownloading [model.safetensors]:  96%|█████████▌| 1.19G/1.24G [55:12<02:23, 375kB/s]\\u001b[A\\u001b[A\\u001b[A\\u001b[A\\n\\n\\n\\n\\rDownloading [model.safetensors]:  96%|█████████▌| 1.19G/1.24G [55:15<02:23, 370kB/s]\\u001b[A\\u001b[A\\u001b[A\\u001b[A\\n\\n\\n\\n\\rDownloading [model.safetensors]:  96%|█████████▌| 1.19G/1.24G [55:18<02:18, 375kB/s]\\u001b[A\\u001b[A\\u001b[A\\u001b[A\\n\\n\\n\\n\\rDownloading [model.safetensors]:  96%|█████████▌| 1.19G/1.24G [55:21<02:14, 378kB/s]\\u001b[A\\u001b[A\\u001b[A\\u001b[A\\n\\n\\n\\n\\rDownloading [model.safetensors]:  96%|█████████▋| 1.19G/1.24G [55:23<02:09, 385kB/s]\\u001b[A\\u001b[A\\u001b[A\\u001b[A\\n\\n\\n\\n\\rDownloading [model.safetensors]:  96%|█████████▋| 1.20G/1.24G [55:26<02:03, 394kB/s]\\u001b[A\\u001b[A\\u001b[A\\u001b[A\\n\\n\\n\\n\\rDownloading [model.safetensors]:  96%|█████████▋| 1.20G/1.24G [55:28<02:03, 386kB/s]\\u001b[A\\u001b[A\\u001b[A\\u001b[A\\n\\n\\n\\n\\rDownloading [model.safetensors]:  96%|█████████▋| 1.20G/1.24G [55:31<01:57, 398kB/s]\\u001b[A\\u001b[A\\u001b[A\\u001b[A\\n\\n\\n\\n\\rDownloading [model.safetensors]:  97%|█████████▋| 1.20G/1.24G [55:33<01:49, 418kB/s]\\u001b[A\\u001b[A\\u001b[A\\u001b[A\\n\\n\\n\\n\\rDownloading [model.safetensors]:  97%|█████████▋| 1.20G/1.24G [55:36<01:45, 421kB/s]\\u001b[A\\u001b[A\\u001b[A\\u001b[A\\n\\n\\n\\n\\rDownloading [model.safetensors]:  97%|█████████▋| 1.20G/1.24G [55:38<01:42, 425kB/s]\\u001b[A\\u001b[A\\u001b[A\\u001b[A\\n\\n\\n\\n\\rDownloading [model.safetensors]:  97%|█████████▋| 1.20G/1.24G [55:41<01:42, 413kB/s]\\u001b[A\\u001b[A\\u001b[A\\u001b[A\\n\\n\\n\\n\\rDownloading [model.safetensors]:  97%|█████████▋| 1.20G/1.24G [55:44<01:45, 394kB/s]\\u001b[A\\u001b[A\\u001b[A\\u001b[A\\n\\n\\n\\n\\rDownloading [model.safetensors]:  97%|████
…[truncated 859 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-22T14:49:50.749051+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:huggingface.co m-a-p 340M-20B HGRN hybrid",
  "allowed_domains": "['huggingface.co']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:huggingface.co m-a-p 340M-20B HGRN hybrid",
    "allowed_domains": "['huggingface.co']"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-22T14:49:50.749203+00:00_

Web search results for query: "site:huggingface.co m-a-p 340M-20B DeltaNet hybrid"

Links: [{"title":"m-a-p/340M-20B-DeltaNet-hybrid-24-1 · Hugging Face","url":"https://huggingface.co/m-a-p/340M-20B-DeltaNet-hybrid-24-1"},{"title":"m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1 · Hugging Face","url":"https://huggingface.co/m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1"},{"title":"diff --git \"a/tokenizer.json\" \"b/tokenizer.json\"","url":"https://huggingface.co/m-a-p/340M-20B-DeltaNet-hybrid-6-1/commit/5696ff2a5ba98c31a95505684bb96737cbb05260.diff?file=tokenizer.json"},{"title":"See raw diff","url":"https://huggingface.co/m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1/commit/df87c03b9e0ed686df4adef8e3eff9e7f4f6b925.diff?file=tokenizer.json"},{"title":"m-a-p/1.3B-100B-DeltaNet-hybrid-6-1 · Hugging Face","url":"https://huggingface.co/m-a-p/1.3B-100B-DeltaNet-hybrid-6-1"},{"title":"The Secret Engine of Next-Gen AI: Why Hybrid Attention is a Game Changer","url":"https://huggingface.co/blog/jlopez-dl/hybrid-attention-game-changer"},{"title":"https://huggingface.co/m-a-p/340M-20B-GLA-hybrid-2...","url":"https://huggingface.co/m-a-p/340M-20B-GLA-hybrid-24-1/commit/f8831c8a23e2016653685c3b01502dd47157fa78.diff?file=tokenizer.json"},{"title":"linear-moe-hub/Gated-Deltanet-340M · Hugging Face","url":"https://huggingface.co/linear-moe-hub/Gated-Deltanet-340M"},{"title":"m-a-p/transformer_340M_baseline · Hugging Face","url":"https://huggingface.co/m-a-p/transformer_340M_baseline"},{"title":"DuoNeural/Qwen3.6-35B-A3B-Code-imatrix-GGUF · Hugging Face","url":"https://huggingface.co/DuoNeural/Qwen3.6-35B-A3B-Code-imatrix-GGUF"}]

I found several results related to your search. The web search revealed:

1. The m-a-p/340M-20B-DeltaNet-hybrid model is part of "All 1.3B & 340M hybrid linear-attention experiments".

2. There are multiple variants in this model family hosted on Hugging Face, including the 340M-20B-DeltaNet-hybrid-24-1 and 340M-20B-GatedDeltaNet-New-hybrid-24-1.

3. The hybri
…[truncated 518 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-22T14:49:50.749376+00:00_

Web search results for query: "site:huggingface.co m-a-p 340M-20B HGRN hybrid"

Links: [{"title":"A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/pdf/2507.06457"},{"title":"https://huggingface.co/m-a-p/340M-20B-GLA-hybrid-2...","url":"https://huggingface.co/m-a-p/340M-20B-GLA-hybrid-24-1/commit/f8831c8a23e2016653685c3b01502dd47157fa78.diff?file=tokenizer.json"},{"title":"m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1 · Hugging Face","url":"https://huggingface.co/m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1"},{"title":"m-a-p/340M-20B-DeltaNet-hybrid-24-1 · Hugging Face","url":"https://huggingface.co/m-a-p/340M-20B-DeltaNet-hybrid-24-1"},{"title":"m-a-p/transformer_340M_baseline · Hugging Face","url":"https://huggingface.co/m-a-p/transformer_340M_baseline"},{"title":"HGRN2: Gated Linear RNNs with State Expansion","url":"https://arxiv.org/pdf/2404.07904"},{"title":"BabyHGRN: Exploring RNNs for Sample-Efficient Training of Language Models","url":"https://arxiv.org/pdf/2412.15978"},{"title":"apierro-hf/hgrn-340M-instruct-capybara · Hugging Face","url":"https://huggingface.co/apierro-hf/hgrn-340M-instruct-capybara"}]

Based on the search results, I found information about the models you're looking for. The m-a-p organization trained and open-sourced 72 models: 36 at 340M parameters (20B tokens) and 36 at 1.3B parameters (100B tokens), covering six linear attention variants across five hybridization ratios.

The search results show several related models on Hugging Face from the m-a-p organization, including models like "340M-20B-GatedDeltaNet-New-hybrid-24-1" and "340M-20B-DeltaNet-hybrid-24-1". These models are part of a comprehensive study on hybrid linear attention architectures.

The researchers recommend architectures such as HGRN-2 or GatedDeltaNet with a linear-to-full ratio between 3:1 and 6:1 to achieve Transformer-level recall efficiently. This suggests that the HGRN hybrid models you're asking about are part of this broader research eff
…[truncated 158 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-22T14:49:50.749555+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:huggingface.co \"m-a-p/340M-20B-DeltaNet-hybrid-3-1\"",
  "allowed_domains": "['huggingface.co']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:huggingface.co \"m-a-p/340M-20B-DeltaNet-hybrid-3-1\"",
    "allowed_domains": "['huggingface.co']"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-22T14:49:50.749702+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:huggingface.co \"m-a-p/340M-20B-HGRN-hybrid\"",
  "allowed_domains": "['huggingface.co']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:huggingface.co \"m-a-p/340M-20B-HGRN-hybrid\"",
    "allowed_domains": "['huggingface.co']"
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-22T14:49:50.749830+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "huggingface.co/collections/m-a-p hybrid-linear-attention-research 340M models list",
  "allowed_domains": "['huggingface.co']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "WebSearch",
  "tool_args": {
    "query": "huggingface.co/collections/m-a-p hybrid-linear-attention-research 340M models list",
    "allowed_domains": "['huggingface.co']"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-22T14:49:50.749973+00:00_

Web search results for query: "site:huggingface.co "m-a-p/340M-20B-DeltaNet-hybrid-3-1""

Links: [{"title":"m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1 · Hugging Face","url":"https://huggingface.co/m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1"},{"title":"m-a-p/340M-20B-DeltaNet-hybrid-24-1 · Hugging Face","url":"https://huggingface.co/m-a-p/340M-20B-DeltaNet-hybrid-24-1"},{"title":"m-a-p/1.3B-100B-DeltaNet-hybrid-6-1 · Hugging Face","url":"https://huggingface.co/m-a-p/1.3B-100B-DeltaNet-hybrid-6-1"},{"title":"linear-moe-hub/Gated-Deltanet-340M · Hugging Face","url":"https://huggingface.co/linear-moe-hub/Gated-Deltanet-340M"},{"title":"m-a-p/transformer_340M_baseline · Hugging Face","url":"https://huggingface.co/m-a-p/transformer_340M_baseline"},{"title":"A Unified View of Delta Parameter Editing in Post-Trained Large-Scale   Models","url":"https://arxiv.org/pdf/2410.13841"},{"title":"https://huggingface.co/m-a-p/340M-20B-GLA-hybrid-2...","url":"https://huggingface.co/m-a-p/340M-20B-GLA-hybrid-24-1/commit/f8831c8a23e2016653685c3b01502dd47157fa78.diff?file=tokenizer.json"},{"title":"Gated Delta Networks: Improving Mamba2 with Delta Rule","url":"https://arxiv.org/pdf/2412.06464"},{"title":"Parallelizing Linear Transformers with the Delta Rule over Sequence   Length","url":"https://arxiv.org/pdf/2406.06484"}]

The search results show similar models from the m-a-p organization on Hugging Face, but not the exact model "m-a-p/340M-20B-DeltaNet-hybrid-3-1" that you requested. The closest results include:

- **m-a-p/340M-20B-DeltaNet-hybrid-24-1** - A hybrid linear-attention model (updated September 11, 2025)
- **m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1** - Another hybrid linear-attention variant (updated September 11, 2025)

These appear to be part of 1.3B & 340M hybrid linear-attention experiments from the m-a-p organization.

The specific model with the "-3-1" suffix you're looking for doesn't appear in these search results. It's possible the model may not be publicl
…[truncated 276 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-22T14:49:50.750144+00:00_

Web search results for query: "site:huggingface.co "m-a-p/340M-20B-HGRN-hybrid""

Links: [{"title":"m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1 · Hugging Face","url":"https://huggingface.co/m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1"},{"title":"m-a-p/340M-20B-DeltaNet-hybrid-24-1 · Hugging Face","url":"https://huggingface.co/m-a-p/340M-20B-DeltaNet-hybrid-24-1"},{"title":"Hybrid Linear Attention Research - a m-a-p Collection","url":"https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research"},{"title":"https://huggingface.co/m-a-p/340M-20B-GLA-hybrid-2...","url":"https://huggingface.co/m-a-p/340M-20B-GLA-hybrid-24-1/commit/f8831c8a23e2016653685c3b01502dd47157fa78.diff?file=tokenizer.json"},{"title":"m-a-p/transformer_340M_baseline · Hugging Face","url":"https://huggingface.co/m-a-p/transformer_340M_baseline"},{"title":"m-a-p (Multimodal Art Projection)","url":"https://huggingface.co/m-a-p"},{"title":"diff --git \"a/tokenizer.json\" \"b/tokenizer.json\"","url":"https://huggingface.co/m-a-p/340M-20B-DeltaNet-hybrid-6-1/commit/5696ff2a5ba98c31a95505684bb96737cbb05260.diff?file=tokenizer.json"},{"title":"apierro-hf/hgrn-340M-instruct-capybara · Hugging Face","url":"https://huggingface.co/apierro-hf/hgrn-340M-instruct-capybara"},{"title":"HGRN - a fla-hub Collection","url":"https://huggingface.co/collections/fla-hub/hgrn"},{"title":"m-a-p/1.3B-100B-DeltaNet-hybrid-6-1 · Hugging Face","url":"https://huggingface.co/m-a-p/1.3B-100B-DeltaNet-hybrid-6-1"}]

The search didn't return results for the exact model "m-a-p/340M-20B-HGRN-hybrid". However, the results show related models from the m-a-p organization on Hugging Face that appear to be part of hybrid linear-attention research experiments. The search returned several similar model variants including:

- 340M-20B-GatedDeltaNet-New-hybrid-24-1
- 340M-20B-DeltaNet-hybrid-24-1
- 340M-20B-GLA-hybrid-24-1

These models are part of "All 1.3B & 340M hybrid linear-attention experiments" from the m-a-p (Multimodal 
…[truncated 473 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-22T14:49:50.750317+00:00_

Web search results for query: "huggingface.co/collections/m-a-p hybrid-linear-attention-research 340M models list"

Links: [{"title":"Paper page - A Systematic Analysis of Hybrid Linear Attention","url":"https://huggingface.co/papers/2507.06457"},{"title":"Hybrid Linear Attention Research - a m-a-p Collection","url":"https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research"},{"title":"A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/pdf/2507.06457"},{"title":"m-a-p/transformer_340M_baseline · Hugging Face","url":"https://huggingface.co/m-a-p/transformer_340M_baseline"},{"title":"m-a-p/340M-20B-DeltaNet-hybrid-24-1 · Hugging Face","url":"https://huggingface.co/m-a-p/340M-20B-DeltaNet-hybrid-24-1"},{"title":"m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1 · Hugging Face","url":"https://huggingface.co/m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1"},{"title":"Paper page - Gated Linear Attention Transformers with Hardware-Efficient Training","url":"https://huggingface.co/papers/2312.06635"},{"title":"RADLADS: Rapid Attention Distillation to Linear Attention Decoders at Scale","url":"https://arxiv.org/pdf/2505.03005"},{"title":"TerminalTraj - a m-a-p Collection","url":"https://huggingface.co/collections/m-a-p/terminaltraj"}]

Based on the search results, I found information about the Hugging Face collection for hybrid linear attention research:

The models are open-sourced at https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research.

The collection includes 72 trained models: 36 at 340M parameters (20B tokens) and 36 at 1.3B parameters (100B tokens), covering six linear attention variants across five hybridization ratios. All models in the collection are 1.3B & 340M hybrid linear-attention experiments.

The study recommends architectures such as HGRN-2 or GatedDeltaNet with a linear-to-full ratio between 3:1 and 6:1 to achieve Transformer-level recall efficiently.

The collection contains various models trained on th
…[truncated 299 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-22T14:49:50.750500+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-48145",
  "command": "bash -c \"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && python3 -c \\\"\nfrom huggingface_hub import repo_info\nrepos = [\n    'm-a-p/340M-20B-DeltaNet-hybrid-3-1',\n    'm-a-p/340M-20B-HGRN-hybrid-3-1',\n    'm-a-p/340M-20B-GLA-hybrid-3-1',\n]\nfor r in repos:\n    try:\n        info = repo_info(r)\n        print(f'OK: {r} (siblings={len(info.siblings)})')\n    except Exception as e:\n        print(f'FAIL: {r} -> {e}')\n\\\"\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-48145",
    "command": "bash -c \"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && python3 -c \\\"\nfrom huggingface_hub import repo_info\nrepos = [\n    'm-a-p/340M-20B-DeltaNet-hybrid-3-1',\n    'm-a-p/340M-20B-HGRN-hybrid-3-1',\n    'm-a-p/340M-20B-GLA-hybrid-3-1',\n]\nfor r in repos:\n    try:\n        info = repo_info(r)\n        print(f'OK: {r} (siblings={len(info.siblings)})')\n    except Exception as e:\n        print(f'FAIL: {r} -> {e}')\n\\\"\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-22T14:49:50.750670+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"设置成功\\n注意：仅限于学术用途和加速访问github/huggingface，不承诺稳定性保证\\nOK: m-a-p/340M-20B-DeltaNet-hybrid-3-1 (siblings=7)\\nOK: m-a-p/340M-20B-HGRN-hybrid-3-1 (siblings=7)\\nOK: m-a-p/340M-20B-GLA-hybrid-3-1 (siblings=7)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.92}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-22T14:49:50.750842+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "find /root/entrainment_gated_ft/results/exp005_zoo_expansion/ -name \"*.jsonl\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "find /root/entrainment_gated_ft/results/exp005_zoo_expansion/ -name \"*.jsonl\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-22T14:49:50.750968+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-48145",
  "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \\\"import fla; print('fla version:', fla.__version__)\\\"\"",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-48145",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \\\"import fla; print('fla version:', fla.__version__)\\\"\"",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-22T14:49:50.751091+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-22T14:49:50.751207+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"fla version: 0.5.0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.94}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-22T14:49:50.751381+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-48145",
  "command": "cat > /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_p1_v4.sh << 'SCRIPT_EOF'\n#!/bin/bash\nset -eo pipefail\n\n# Environment\nsource /etc/network_turbo\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\nexport HF_HOME=/root/autodl-tmp/.hf_cache\nexport HF_HUB_DISABLE_XET=1\nexport REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt\nexport SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt\nexport CUDA_VISIBLE_DEVICES=0\n\nMODELS=\"/root/entrainment_gated_ft/models\"\nRESULTS=\"/root/entrainment_gated_ft/results/exp005_zoo_expansion\"\nLOG=\"$RESULTS/priority1_v4.log\"\n\necho \"=== P1 v4 START $(date) ===\" | tee \"$LOG\"\n\n# Verify fla\npython3 -c \"import fla; print('fla OK:', fla.__version__)\" 2>&1 | tee -a \"$LOG\"\n\n# Download DeltaNet if needed\nif [ ! -f \"$MODELS/340M-20B-DeltaNet-hybrid-3-1/model.safetensors\" ]; then\n  echo \"=== Downloading DeltaNet h3-1 $(date) ===\" | tee -a \"$LOG\"\n  python3 -c \"\nimport os\nos.environ['HF_HUB_DISABLE_XET'] = '1'\nfrom huggingface_hub import snapshot_download\nsnapshot_download(\n    'm-a-p/340M-20B-DeltaNet-hybrid-3-1',\n    local_dir='$MODELS/340M-20B-DeltaNet-hybrid-3-1'\n)\nprint('DeltaNet download complete')\n\" 2>&1 | tee -a \"$LOG\"\nelse\n  echo \"DeltaNet already present\" | tee -a \"$LOG\"\nfi\n\n# Download HGRN if needed\nif [ ! -f \"$MODELS/340M-20B-HGRN-hybrid-3-1/model.safetensors\" ]; then\n  echo \"=== Downloading HGRN h3-1 $(date) ===\" | tee -a \"$LOG\"\n  python3 -c \"\nimport os\nos.environ['HF_HUB_DISABLE_XET'] = '1'\nfrom huggingface_hub import snapshot_download\nsnapshot_download(\n    'm-a-p/340M-20B-HGRN-hybrid-3-1',\n    local_dir='$MODELS/340M-20B-HGRN-hybrid-3-1'\n)\nprint('HGRN download complete')\n\" 2>&1 | tee -a \"$LOG\"\nelse\n  echo \"HGRN already present\" | tee -a \"$LOG\"\nfi\n\n# Verify all 3 models exist\necho \"=== Verifying models ===\" | tee -a \"$LOG\"\nfor ARCH in GLA DeltaNet HGRN; do\n  if [ -f \"$MODELS/340M-20B-${ARCH}-hybrid-3-1/model.safetensors\" ]; then\n    echo \"  $ARCH: OK ($(du -sh $MODELS/340M-20B-${ARCH}-hybrid-3-1/model.safetensors | cut -f1))\" | tee -a \"$LOG\"\n  else\n    echo \"  $ARCH: MISSING!\" | tee -a \"$LOG\"\n    exit 1\n  fi\ndone\n\n# Evaluate each model\nfor ARCH in GLA DeltaNet HGRN; do\n  LOCAL=\"$MODELS/340M-20B-${ARCH}-hybrid-3-1\"\n  OUTDIR=\"$RESULTS/${ARCH}_hybrid-3-1\"\n\n  # Skip if already evaluated (check for jsonl output)\n  if find \"$OUTDIR\" -name \"*.jsonl\" 2>/dev/null | head -1 | grep -q .; then\n    echo \"=== $ARCH already evaluated, skipping ===\" | tee -a \"$LOG\"\n    continue\n  fi\n\n  echo \"=== EVAL $ARCH START $(date) ===\" | tee -a \"$LOG\"\n  python3 -m lm_eval \\\n    --model hf \\\n    --model_args pretrained=$LOCAL,trust_remote_code=True \\\n    --tasks lambada_openai,arc_easy \\\n    --device cuda:0 \\\n    --batch_size auto \\\n    --log_samples \\\n    --output_path \"$OUTDIR/\" 2>&1 | tee -a \"$LOG\"\n  echo \"=== EVAL $ARCH DONE $(date) ===\" | tee -a \"$LOG\"\ndone\n\necho \"=== P1 v4 ALL DONE $(date) ===\" | tee \"$LOG.done\"\necho \"=== P1 v4 ALL DONE $(date) ===\" | tee -a \"$LOG\"\n\n# Summary\necho \"\" | tee -a \"$LOG\"\necho \"=== RESULTS SUMMARY ===\" | tee -a \"$LOG\"\nfind \"$RESULTS\" -name \"*.jsonl\" -type f 2>/dev/null | tee -a \"$LOG\"\nSCRIPT_EOF\nchmod +x /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_p1_v4.sh\necho \"Script written OK\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-48145",
    "command": "cat > /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_p1_v4.sh << 'SCRIPT_EOF'\n#!/bin/bash\nset -eo pipefail\n\n# Environment\nsource /etc/network_turbo\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\nexport HF_HOME=/root/autodl-tmp/.hf_cache\nexport HF_HUB_DISABLE_XET=1\nexport REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt\nexport SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt\nexport CUDA_VISIBLE_DEVICES=0\n\nMODELS=\"/root/entrainment_gated_ft/models\"\nRESULTS=\"/root/entrainment_gated_ft/results/exp005_zoo_expansion\"\nLOG=\"$RESULTS/priority1_v4.log\"\n\necho \"=== P1 v4 START $(date) ===\" | tee \"$LOG\"\n\n# Verify fla\npython3 -c \"import fla; print('fla OK:', fla.__version__)\" 2>&1 | tee -a \"$LOG\"\n\n# Download DeltaNet if needed\nif [ ! -f \"$MODELS/340M-20B-DeltaNet-hybrid-3-1/model.safetensors\" ]; then\n  echo \"=== Downloading DeltaNet h3-1 $(date) ===\" | tee -a \"$LOG\"\n  python3 -c \"\nimport os\nos.environ['HF_HUB_DISABLE_XET'] = '1'\nfrom huggingface_hub import snapshot_download\nsnapshot_download(\n    'm-a-p/340M-20B-DeltaNet-hybrid-3-1',\n    local_dir='$MODELS/340M-20B-DeltaNet-hybrid-3-1'\n)\nprint('DeltaNet download complete')\n\" 2>&1 | tee -a \"$LOG\"\nelse\n  echo \"DeltaNet already present\" | tee -a \"$LOG\"\nfi\n\n# Download HGRN if needed\nif [ ! -f \"$MODELS/340M-20B-HGRN-hybrid-3-1/model.safetensors\" ]; then\n  echo \"=== Downloading HGRN h3-1 $(date) ===\" | tee -a \"$LOG\"\n  python3 -c \"\nimport os\nos.environ['HF_HUB_DISABLE_XET'] = '1'\nfrom huggingface_hub import snapshot_download\nsnapshot_download(\n    'm-a-p/340M-20B-HGRN-hybrid-3-1',\n    local_dir='$MODELS/340M-20B-HGRN-hybrid-3-1'\n)\nprint('HGRN download complete')\n\" 2>&1 | tee -a \"$LOG\"\nelse\n  echo \"HGRN already present\" | tee -a \"$LOG\"\nfi\n\n# Verify all 3 models exist\necho \"=== Verifying models ===\" | tee -a \"$LOG\"\nfor ARCH in GLA DeltaNet HGRN; do\n  if [ -f \"$MODELS/340M-20B-${ARCH}-hybrid-3-1/model.safetensors\" ]; then\n    echo \"  $ARCH: OK ($(du -sh $MODELS/340M-20B-${ARCH}-hybrid-3-1/model.safetensors | cut -f1))\" | tee -a \"$LOG\"\n  else\n    echo \"  $ARCH: MISSING!\" | tee -a \"$LOG\"\n    exit 1\n  fi\ndone\n\n# Evaluate each model\nfor ARCH in GLA DeltaNet HGRN; do\n  LOCAL=\"$MODELS/340M-20B-${ARCH}-hybrid-3-1\"\n  OUTDIR=\"$RESULTS/${ARCH}_hybrid-3-1\"\n\n  # Skip if already evaluated (check for jsonl output)\n  if find \"$OUTDIR\" -name \"*.jsonl\" 2>/dev/null | head -1 | grep -q .; then\n    echo \"=== $ARCH already evaluated, skipping ===\" | tee -a \"$LOG\"\n    continue\n  fi\n\n  echo \"=== EVAL $ARCH START $(date) ===\" | tee -a \"$LOG\"\n  python3 -m lm_eval \\\n    --model hf \\\n    --model_args pretrained=$LOCAL,trust_remote_code=True \\\n    --tasks lambada_openai,arc_easy \\\n    --device cuda:0 \\\n    --batch_size auto \\\n    --log_samples \\\n    --output_path \"$OUTDIR/\" 2>&1 | tee -a \"$LOG\"\n  echo \"=== EVAL $ARCH DONE $(date) ===\" | tee -a \"$LOG\"\ndone\n\necho \"=== P1 v4 ALL DONE $(date) ===\" | tee \"$LOG.done\"\necho \"=== P1 v4 ALL DONE $(date) ===\" | tee -a \"$LOG\"\n\n# Summary\necho \"\" | tee -a \"$LOG\"\necho \"=== RESULTS SUMMARY ===\" | tee -a \"$LOG\"\nfind \"$RESULTS\" -name \"*.jsonl\" -type f 2>/dev/null | tee -a \"$LOG\"\nSCRIPT_EOF\nchmod +x /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_p1_v4.sh\necho \"Script written OK\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-22T14:49:50.751542+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.77}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-22T14:49:50.751699+00:00_

called mcp__agent-ml-research__submit_training_job

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_training_job</summary>

```json
{
  "server": "westb-48145",
  "gpu_ids": "['cuda:0']",
  "exp_id": "exp-005-p1-v4",
  "command": "bash -c \"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_p1_v4.sh\"",
  "timeout_hours": "8",
  "project": "entrainment_gated_ft",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "tool_args": {
    "server": "westb-48145",
    "gpu_ids": "['cuda:0']",
    "exp_id": "exp-005-p1-v4",
    "command": "bash -c \"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_p1_v4.sh\"",
    "timeout_hours": "8",
    "project": "entrainment_gated_ft",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-22T14:49:50.751854+00:00_

{"result":"{\"success\": true, \"data\": {\"pid\": \"870648\", \"log_file\": \"~/runs/entrainment_gated_ft/exp-005-p1-v4.log\", \"gpu_ids\": [\"cuda:0\"], \"server\": \"westb-48145\", \"account\": \"root\", \"cuda_visible_devices\": \"0\", \"backend\": \"tmux\", \"tmux_session\": \"exp-005-p1-v4\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.89}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-22T14:49:50.752005+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "tail -20 /root/runs/entrainment_gated_ft/exp-005-p1-v4.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "tail -20 /root/runs/entrainment_gated_ft/exp-005-p1-v4.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-22T14:49:50.752144+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"设置成功\\n注意：仅限于学术用途和加速访问github/huggingface，不承诺稳定性保证\\n=== P1 v4 START Fri May 22 22:49:35 CST 2026 ===\\nfla OK: 0.5.0\\n=== Downloading DeltaNet h3-1 Fri May 22 22:49:35 CST 2026 ===\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-22T14:49:50.752305+00:00_

Job 正常启动，正在下载 DeltaNet h3-1。

**当前状态：**
- **GLA h3-1**: 已下载 ✅，待评估
- **DeltaNet h3-1**: 正在下载（~50min @ 400KB/s）
- **HGRN h3-1**: 待下载（DeltaNet 完成后开始）

**预估时间线：**
- 下载 2 个模型：~100 min
- 评估 3 个模型：~15-20 min/model = ~60 min
- 总计：~2.5-3 小时

脚本流程：下载 DeltaNet → 下载 HGRN → 验证全部 3 个模型文件 → 逐个评估（LAMBADA + ARC-Easy, `--log_samples`）。全程在 tmux 中运行，不怕 SSH 断连。

可以过 30-60 分钟后 `tail` 日志文件检查进度：
```
tail -30 /root/runs/entrainment_gated_ft/exp-005-p1-v4.log
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_exp_exp-005-priority1-v2_20260522T144606"
}
```

</details>

---
