# check exp 029 results

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/chats/worker_check_exp-029-results_20260518T153603.jsonl`
- **Structured JSON:** [`71e87056ac0b4cc8c505.json`](../../sessions/71/71e87056ac0b4cc8c505.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

41 recorded events

### Tool call

_source line 1 · 2026-05-18T15:39:07.769920+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__register_artifact",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__register_artifact",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T15:39:07.770456+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T15:39:07.770737+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ps -p 42353 -o pid,cmd --no-headers 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ps -p 42353 -o pid,cmd --no-headers 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T15:39:07.770922+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T15:39:07.771110+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'exp-029-contrastive-folio204'}",
  "project": "symb_invariant_consensus",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'exp-029-contrastive-folio204'}",
    "project": "symb_invariant_consensus",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T15:39:07.771262+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4194}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T15:39:07.771390+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "find /root -path \"*exp-029*\" -name \"*.json\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "find /root -path \"*exp-029*\" -name \"*.json\" 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T15:39:07.771516+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T15:39:07.771639+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "find /root -path \"*contrastive*folio*\" -name \"*.json\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "find /root -path \"*contrastive*folio*\" -name \"*.json\" 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T15:39:07.771762+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T15:39:07.771946+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "ps -p 42353 -o pid,cmd --no-headers 2>/dev/null && echo \"ALIVE\" || echo \"DEAD\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "ps -p 42353 -o pid,cmd --no-headers 2>/dev/null && echo \"ALIVE\" || echo \"DEAD\""
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-18T15:39:07.772103+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "find /root -path \"*exp-029*\" -name \"*.json\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "find /root -path \"*exp-029*\" -name \"*.json\" 2>/dev/null | head -20"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T15:39:07.772229+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "find /root -path \"*contrastive*folio*\" -name \"*.json\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "find /root -path \"*contrastive*folio*\" -name \"*.json\" 2>/dev/null | head -20"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-18T15:39:07.772350+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "ls -la /root/symb_invariant_consensus/results/exp-029-contrastive-folio204/ 2>/dev/null; ls -la /root/autodl-tmp/sica_project/results/exp-029-contrastive-folio204/ 2>/dev/null; echo \"---\"; find /root -path \"*exp-029*\" -type d 2>/dev/null | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls -la /root/symb_invariant_consensus/results/exp-029-contrastive-folio204/ 2>/dev/null; ls -la /root/autodl-tmp/sica_project/results/exp-029-contrastive-folio204/ 2>/dev/null; echo \"---\"; find /root -path \"*exp-029*\" -type d 2>/dev/null | head -10"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T15:39:07.772471+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'RUNNING'}",
  "project": "symb_invariant_consensus",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'RUNNING'}",
    "project": "symb_invariant_consensus",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T15:39:07.772601+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"DEAD\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.26}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-18T15:39:07.772742+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_0.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_1.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_2.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_3.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_4.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_5.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_6.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_7.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_8.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_9.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_10.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_11.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_12.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_13.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_14.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_15.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_16.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_17.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_18.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_19.j
…[truncated 109 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T15:39:07.772932+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_0.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_1.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_2.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_3.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_4.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_5.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_6.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_7.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_8.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_9.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_10.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_11.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_12.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_13.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_14.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_15.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_16.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_17.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_18.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/folio_19.j
…[truncated 110 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-18T15:39:07.773087+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 560\\ndrwxr-xr-x 3 root root     90 May 18 22:25 .\\ndrwxr-xr-x 7 root root   4096 May 18 22:50 ..\\n-rw-r--r-- 1 root root 247792 May 18 23:12 contrastive_results.json\\ndrwxr-xr-x 2 root root   8192 May 18 23:12 intermediates\\n-rw-r--r-- 1 root root 304015 May 18 23:12 run.log\\n---\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.33}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T15:39:07.774017+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp-029-contrastive-folio204\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T14:22:03.513Z\", \"updated_at\": \"2026-05-18T15:36:36.585Z\", \"hypothesis\": \"Contrastive constraint extraction (answer-conditioned supporting/opposing constraints with structured JSON output and MaxSAT integration) will achieve discriminative_rate >20% (vs baseline 8.2%) and positive recovery_rate on FOLIO 204, because per-candidate opposing constraints provide stronger signal than simple majority voting for disambiguating closely-scored answers.\", \"parent\": \"exp-026-folio204-trace-regen\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && bash /root/symb_invariant_consensus/scripts/run_exp029_contrastive.sh'\", \"server\": \"westd-25068\", \"gpu\": [\"cuda:3\"], \"pid\": \"42353\", \"log_path\": \"~/runs/symb_invariant_consensus/exp-029-contrastive-folio204.log\", \"submitted_at\": \"2026-05-18T14:24:26.683Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/symb_invariant_consensus/results/folio_204_14b/intermediates/\", \"data_count\": 181, \"model_name\": \"Qwen2.5-14B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"exp-026-folio204-trace-regen\", \"eval_data\": \"FOLIO-204\"}, \"conclusion\": \"success\"}}, \"count\": 1, \"total\": 1, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5596}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T15:39:07.774291+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "tail -80 /root/symb_invariant_consensus/results/exp-029-contrastive-folio204/run.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "tail -80 /root/symb_invariant_consensus/results/exp-029-contrastive-folio204/run.log"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-18T15:39:07.774454+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/ | wc -l"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates/ | wc -l"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-18T15:39:07.774656+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  Constraints: {'total_extracted': 24, 'unique_after_dedup': 7, 'stance_distribution': {'supporting': 12, 'opposing': 12}}\\n  Time: 13.6s\\n  ETA: 0.8 min (3 remaining)\\n\\n============================================================\\n[180/182] folio_179\\n  GT: False\\n  Traces: 12\\n2026-05-18 23:11:31,406 INFO HTTP Request: POST http://localhost:8003/v1/chat/completions \\\"HTTP/1.1 200 OK\\\"\\n2026-05-18 23:11:31,533 INFO HTTP Request: POST http://localhost:8003/v1/chat/completions \\\"HTTP/1.1 200 OK\\\"\\n2026-05-18 23:11:31,637 INFO HTTP Request: POST http://localhost:8003/v1/chat/completions \\\"HTTP/1.1 200 OK\\\"\\n2026-05-18 23:11:32,244 INFO HTTP Request: POST http://localhost:8003/v1/chat/completions \\\"HTTP/1.1 200 OK\\\"\\n2026-05-18 23:11:35,808 INFO HTTP Request: POST http://localhost:8003/v1/chat/completions \\\"HTTP/1.1 200 OK\\\"\\n2026-05-18 23:11:35,935 INFO HTTP Request: POST http://localhost:8003/v1/chat/completions \\\"HTTP/1.1 200 OK\\\"\\n2026-05-18 23:11:36,460 INFO HTTP Request: POST http://localhost:8003/v1/chat/completions \\\"HTTP/1.1 200 OK\\\"\\n2026-05-18 23:11:36,678 INFO HTTP Request: POST http://localhost:8003/v1/chat/completions \\\"HTTP/1.1 200 OK\\\"\\n2026-05-18 23:11:38,568 INFO HTTP Request: POST http://localhost:8003/v1/chat/completions \\\"HTTP/1.1 200 OK\\\"\\n2026-05-18 23:11:40,451 INFO HTTP Request: POST http://localhost:8003/v1/chat/completions \\\"HTTP/1.1 200 OK\\\"\\n2026-05-18 23:11:40,677 INFO HTTP Request: POST http://localhost:8003/v1/chat/completions \\\"HTTP/1.1 200 OK\\\"\\n2026-05-18 23:11:40,947 INFO HTTP Request: POST http://localhost:8003/v1/chat/completions \\\"HTTP/1.1 200 OK\\\"\\n  Contrastive: False (V)\\n  SC baseline: False (V)\\n  Scores: {'False': 9.0, 'True': -9.0}\\n  Constraints: {'total_extracted': 23, 'unique_after_dedup': 15, 'stance_distribution': {'supporting': 11, 'opposing': 12}}\\n  Time: 13.9s\\n  ETA: 0.5 min (2 remainin
…[truncated 3993 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-18T15:39:07.774977+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"182\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.58}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T15:39:07.775366+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "python3 -c \"\nimport json\nwith open('/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/contrastive_results.json') as f:\n    d = json.load(f)\nprint('Type:', type(d).__name__)\nif isinstance(d, dict):\n    print('Top keys:', list(d.keys())[:30])\n    for k in ['accuracy','sc_accuracy','contrastive_accuracy','discriminative_rate','n_problems','summary']:\n        if k in d: print(f'{k}: {d[k]}')\n    if 'results' in d:\n        print('N results:', len(d['results']))\n        if d['results']:\n            first = d['results'][0] if isinstance(d['results'], list) else list(d['results'].values())[0]\n            print('First result keys:', list(first.keys())[:20] if isinstance(first, dict) else type(first))\nelif isinstance(d, list):\n    print('N items:', len(d))\n    if d:\n        print('First item keys:', list(d[0].keys())[:20] if isinstance(d[0], dict) else type(d[0]))\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "python3 -c \"\nimport json\nwith open('/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/contrastive_results.json') as f:\n    d = json.load(f)\nprint('Type:', type(d).__name__)\nif isinstance(d, dict):\n    print('Top keys:', list(d.keys())[:30])\n    for k in ['accuracy','sc_accuracy','contrastive_accuracy','discriminative_rate','n_problems','summary']:\n        if k in d: print(f'{k}: {d[k]}')\n    if 'results' in d:\n        print('N results:', len(d['results']))\n        if d['results']:\n            first = d['results'][0] if isinstance(d['results'], list) else list(d['results'].values())[0]\n            print('First result keys:', list(first.keys())[:20] if isinstance(first, dict) else type(first))\nelif isinstance(d, list):\n    print('N items:', len(d))\n    if d:\n        print('First item keys:', list(d[0].keys())[:20] if isinstance(d[0], dict) else type(d[0]))\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-18T15:39:07.775622+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'python3 -c \\\"\\\\nimport json\\\\nwith open(\\\\'/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/contrastive_results.json\\\\') as f:\\\\n    d = json.load(f)\\\\nprint(\\\\'Type:\\\\', type(d).__name__)\\\\nif isinstance(d, dict):\\\\n    print(\\\\'Top keys:\\\\', list(d.keys())[:30])\\\\n    for k in [\\\\'accuracy\\\\',\\\\'sc_accuracy\\\\',\\\\'contrastive_accuracy\\\\',\\\\'discriminative_rate\\\\',\\\\'n_problems\\\\',\\\\'summary\\\\']:\\\\n        if k in d: print(f\\\\'{k}: {d[k]}\\\\')\\\\n    if \\\\'results\\\\' in d:\\\\n        print(\\\\'N results:\\\\', len(d[\\\\'results\\\\']))\\\\n        if d[\\\\'results\\\\']:\\\\n            first = d[\\\\'results\\\\'][0] if isinstance(d[\\\\'results\\\\'], list) else list(d[\\\\'results\\\\'].values())[0]\\\\n            print(\\\\'First result keys:\\\\', list(first.keys())[:20] if isinstance(first, dict) else type(first))\\\\nelif isinstance(d, list):\\\\n    print(\\\\'N items:\\\\', len(d))\\\\n    if d:\\\\n        print(\\\\'First item keys:\\\\', list(d[0].keys())[:20] if isinstance(d[0], dict) else type(d[0]))\\\\n\\\"\\\\n'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 12.7}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-18T15:39:07.776134+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "source /root/miniconda3/bin/activate && python3 -c \"\nimport json\n\nwith open('/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/contrastive_results.json') as f:\n    d = json.load(f)\n\nprint('Type:', type(d).__name__)\nif isinstance(d, dict):\n    print('Top keys:', list(d.keys())[:30])\n    for k in ['accuracy','sc_accuracy','contrastive_accuracy','discriminative_rate','n_problems','summary','config']:\n        if k in d: print(f'{k}: {d[k]}')\n    if 'results' in d:\n        results = d['results']\n        print('N results:', len(results))\n        if results:\n            first = results[0] if isinstance(results, list) else list(results.values())[0]\n            print('First result keys:', list(first.keys())[:25] if isinstance(first, dict) else type(first))\nelif isinstance(d, list):\n    print('N items:', len(d))\n    if d:\n        print('First item keys:', list(d[0].keys())[:25] if isinstance(d[0], dict) else type(d[0]))\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "source /root/miniconda3/bin/activate && python3 -c \"\nimport json\n\nwith open('/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/contrastive_results.json') as f:\n    d = json.load(f)\n\nprint('Type:', type(d).__name__)\nif isinstance(d, dict):\n    print('Top keys:', list(d.keys())[:30])\n    for k in ['accuracy','sc_accuracy','contrastive_accuracy','discriminative_rate','n_problems','summary','config']:\n        if k in d: print(f'{k}: {d[k]}')\n    if 'results' in d:\n        results = d['results']\n        print('N results:', len(results))\n        if results:\n            first = results[0] if isinstance(results, list) else list(results.values())[0]\n            print('First result keys:', list(first.keys())[:25] if isinstance(first, dict) else type(first))\nelif isinstance(d, list):\n    print('N items:', len(d))\n    if d:\n        print('First item keys:', list(d[0].keys())[:25] if isinstance(d[0], dict) else type(d[0]))\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-18T15:39:07.776424+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Type: dict\\nTop keys: ['summary', 'results']\\nsummary: {'n': 182, 'contrastive_accuracy': 0.7253, 'sc_accuracy': 0.7363, 'delta': -0.011, 'scorer_alpha': 1.0, 'mode': 'vllm', 'total_wall_time_s': 2833.5, 'extractor_stats': {'success': 2184, 'fail_json_parse': 0, 'fail_empty': 0, 'fail_invalid_expr': 0}}\\nN results: 182\\nFirst result keys: ['problem_idx', 'problem_id', 'problem', 'dataset', 'ground_truth', 'contrastive_answer', 'contrastive_correct', 'contrastive_scores', 'sc_answer', 'sc_correct', 'constraints_stats', 'maxsat_stats', 'timing']\\n\", \"stderr\": \"Error while loading conda entry point: conda-libmamba-solver (module 'libmambapy' has no attribute 'QueryFormat')\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-18T15:39:07.776684+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "source /root/miniconda3/bin/activate && python3 << 'PYEOF'\nimport json\n\nwith open('/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/contrastive_results.json') as f:\n    d = json.load(f)\n\nresults = d['results']\nsummary = d['summary']\nn = summary['n']\n\n# Core metrics\ncont_correct = sum(1 for r in results if r['contrastive_correct'])\nsc_correct = sum(1 for r in results if r['sc_correct'])\ncont_acc = cont_correct / n\nsc_acc = sc_correct / n\ndelta = cont_acc - sc_acc\n\nprint(f\"=== CORE METRICS (n={n}) ===\")\nprint(f\"Contrastive accuracy: {cont_acc:.4f} ({cont_correct}/{n})\")\nprint(f\"SC accuracy:          {sc_acc:.4f} ({sc_correct}/{n})\")\nprint(f\"Delta:                {delta:+.4f} ({delta*100:+.2f}pp)\")\n\n# Discriminative rate\ndiscriminative = sum(1 for r in results if r['contrastive_answer'] != r['sc_answer'])\ndisc_rate = discriminative / n\nprint(f\"\\nDiscriminative rate:  {disc_rate:.4f} ({discriminative}/{n})\")\n\n# When contrastive disagrees with SC, who is right?\ncont_wins = 0\nsc_wins = 0\nboth_wrong = 0\nfor r in results:\n    if r['contrastive_answer'] != r['sc_answer']:\n        if r['contrastive_correct'] and not r['sc_correct']:\n            cont_wins += 1\n        elif r['sc_correct'] and not r['contrastive_correct']:\n            sc_wins += 1\n        else:\n            both_wrong += 1\n\nprint(f\"\\nWhen disagree ({discriminative} cases):\")\nprint(f\"  Contrastive wins: {cont_wins}\")\nprint(f\"  SC wins:          {sc_wins}\")\nprint(f\"  Both wrong:       {both_wrong}\")\n\n# McNemar test (2x2 contingency)\n# a = both correct, b = cont correct & sc wrong, c = cont wrong & sc correct, d = both wrong\na = sum(1 for r in results if r['contrastive_correct'] and r['sc_correct'])\nb = sum(1 for r in results if r['contrastive_correct'] and not r['sc_correct'])\nc = sum(1 for r in results if not r['contrastive_correct'] and r['sc_correct'])\ndd = sum(1 for r in results if not r['contrastive_correct'] and not r['sc_correct'])\n\nprint(f\"\\n=== McNemar 2x2 ===\")\nprint(f\"  Both correct:    {a}\")\nprint(f\"  Cont only:       {b}\")\nprint(f\"  SC only:         {c}\")\nprint(f\"  Both wrong:      {dd}\")\n\n# McNemar chi-squared (with continuity correction)\nif b + c > 0:\n    chi2 = (abs(b - c) - 1)**2 / (b + c)\n    # p-value from chi-squared with 1 df\n    import math\n    # Approximate p-value\n    z = math.sqrt(chi2)\n    # Using normal approximation for p-value\n    p_approx = 2 * (1 - 0.5 * (1 + math.erf(z / math.sqrt(2))))\n    print(f\"  McNemar chi2:    {chi2:.4f}\")\n    print(f\"  p-value (approx): {p_approx:.4f}\")\n    print(f\"  Significant (p<0.05): {'YES' if p_approx < 0.05 else 'NO'}\")\n\n# Recovery rate: oracle delta on FOLIO regen was 88.24% - 75.00% = 13.24pp\noracle_delta_pp = 13.24\nrecovery = (delta * 100) / oracle_delta_pp * 100\nprint(f\"\\n=== RECOVERY RATE ===\")\nprint(f\"  Oracle delta:    {oracle_delta_pp}pp (88.24% - 75.00%)\")\nprint(f\"  Actual delta:    {delta*100:+.2f}pp\")\nprint(f\"  Recovery rate:   {recovery:+.2f}%\")\n\n# Constraint stats\ntotal_supporting = 0\ntotal_opposing = 0\ntotal_extracted = 0\ntotal_unique = 0\nfor r in results:\n    cs = r.get('constraints_stats', {})\n    total_supporting += cs.get('supporting', 0)\n    total_opposing += cs.get('opposing', 0)\n    total_extracted += cs.get('total_extracted', 0)\n    total_unique += cs.get('unique_after_dedup', 0)\n\nprint(f\"\\n=== CONSTRAINT STATS ===\")\nprint(f\"  Total extracted: {total_extracted}\")\nprint(f\"  Unique (dedup):  {total_unique}\")\nprint(f\"  Supporting:      {total_supporting} ({total_supporting/(total_supporting+total_opposing)*100:.1f}%)\")\nprint(f\"  Opposing:        {total_opposing} ({total_opposing/(total_supporting+total_opposing)*100:.1f}%)\")\nprint(f\"  Avg per problem: {total_extracted/n:.1f} extracted, {total_unique/n:.1f} unique\")\nprint(f\"  Support ratio:   {total_supporting/total_opposing:.2f}\")\n\nPYEOF\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "source /root/miniconda3/bin/activate && python3 << 'PYEOF'\nimport json\n\nwith open('/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/contrastive_results.json') as f:\n    d = json.load(f)\n\nresults = d['results']\nsummary = d['summary']\nn = summary['n']\n\n# Core metrics\ncont_correct = sum(1 for r in results if r['contrastive_correct'])\nsc_correct = sum(1 for r in results if r['sc_correct'])\ncont_acc = cont_correct / n\nsc_acc = sc_correct / n\ndelta = cont_acc - sc_acc\n\nprint(f\"=== CORE METRICS (n={n}) ===\")\nprint(f\"Contrastive accuracy: {cont_acc:.4f} ({cont_correct}/{n})\")\nprint(f\"SC accuracy:          {sc_acc:.4f} ({sc_correct}/{n})\")\nprint(f\"Delta:                {delta:+.4f} ({delta*100:+.2f}pp)\")\n\n# Discriminative rate\ndiscriminative = sum(1 for r in results if r['contrastive_answer'] != r['sc_answer'])\ndisc_rate = discriminative / n\nprint(f\"\\nDiscriminative rate:  {disc_rate:.4f} ({discriminative}/{n})\")\n\n# When contrastive disagrees with SC, who is right?\ncont_wins = 0\nsc_wins = 0\nboth_wrong = 0\nfor r in results:\n    if r['contrastive_answer'] != r['sc_answer']:\n        if r['contrastive_correct'] and not r['sc_correct']:\n            cont_wins += 1\n        elif r['sc_correct'] and not r['contrastive_correct']:\n            sc_wins += 1\n        else:\n            both_wrong += 1\n\nprint(f\"\\nWhen disagree ({discriminative} cases):\")\nprint(f\"  Contrastive wins: {cont_wins}\")\nprint(f\"  SC wins:          {sc_wins}\")\nprint(f\"  Both wrong:       {both_wrong}\")\n\n# McNemar test (2x2 contingency)\n# a = both correct, b = cont correct & sc wrong, c = cont wrong & sc correct, d = both wrong\na = sum(1 for r in results if r['contrastive_correct'] and r['sc_correct'])\nb = sum(1 for r in results if r['contrastive_correct'] and not r['sc_correct'])\nc = sum(1 for r in results if not r['contrastive_correct'] and r['sc_correct'])\ndd = sum(1 for r in results if not r['contrastive_correct'] and not r['sc_correct'])\n\nprint(f\"\\n=== McNemar 2x2 ===\")\nprint(f\"  Both correct:    {a}\")\nprint(f\"  Cont only:       {b}\")\nprint(f\"  SC only:         {c}\")\nprint(f\"  Both wrong:      {dd}\")\n\n# McNemar chi-squared (with continuity correction)\nif b + c > 0:\n    chi2 = (abs(b - c) - 1)**2 / (b + c)\n    # p-value from chi-squared with 1 df\n    import math\n    # Approximate p-value\n    z = math.sqrt(chi2)\n    # Using normal approximation for p-value\n    p_approx = 2 * (1 - 0.5 * (1 + math.erf(z / math.sqrt(2))))\n    print(f\"  McNemar chi2:    {chi2:.4f}\")\n    print(f\"  p-value (approx): {p_approx:.4f}\")\n    print(f\"  Significant (p<0.05): {'YES' if p_approx < 0.05 else 'NO'}\")\n\n# Recovery rate: oracle delta on FOLIO regen was 88.24% - 75.00% = 13.24pp\noracle_delta_pp = 13.24\nrecovery = (delta * 100) / oracle_delta_pp * 100\nprint(f\"\\n=== RECOVERY RATE ===\")\nprint(f\"  Oracle delta:    {oracle_delta_pp}pp (88.24% - 75.00%)\")\nprint(f\"  Actual delta:    {delta*100:+.2f}pp\")\nprint(f\"  Recovery rate:   {recovery:+.2f}%\")\n\n# Constraint stats\ntotal_supporting = 0\ntotal_opposing = 0\ntotal_extracted = 0\ntotal_unique = 0\nfor r in results:\n    cs = r.get('constraints_stats', {})\n    total_supporting += cs.get('supporting', 0)\n    total_opposing += cs.get('opposing', 0)\n    total_extracted += cs.get('total_extracted', 0)\n    total_unique += cs.get('unique_after_dedup', 0)\n\nprint(f\"\\n=== CONSTRAINT STATS ===\")\nprint(f\"  Total extracted: {total_extracted}\")\nprint(f\"  Unique (dedup):  {total_unique}\")\nprint(f\"  Supporting:      {total_supporting} ({total_supporting/(total_supporting+total_opposing)*100:.1f}%)\")\nprint(f\"  Opposing:        {total_opposing} ({total_opposing/(total_supporting+total_opposing)*100:.1f}%)\")\nprint(f\"  Avg per problem: {total_extracted/n:.1f} extracted, {total_unique/n:.1f} unique\")\nprint(f\"  Support ratio:   {total_supporting/total_opposing:.2f}\")\n\nPYEOF\n"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-18T15:39:07.777072+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'source /root/miniconda3/bin/activate && python3 << \\\\'PYEOF\\\\'\\\\nimport json\\\\n\\\\nwith open(\\\\'/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/contrastive_results.json\\\\') as f:\\\\n    d = json.load(f)\\\\n\\\\nresults = d[\\\\'results\\\\']\\\\nsummary = d[\\\\'summary\\\\']\\\\nn = summary[\\\\'n\\\\']\\\\n\\\\n# Core metrics\\\\ncont_correct = sum(1 for r in results if r[\\\\'contrastive_correct\\\\'])\\\\nsc_correct = sum(1 for r in results if r[\\\\'sc_correct\\\\'])\\\\ncont_acc = cont_correct / n\\\\nsc_acc = sc_correct / n\\\\ndelta = cont_acc - sc_acc\\\\n\\\\nprint(f\\\"=== CORE METRICS (n={n}) ===\\\")\\\\nprint(f\\\"Contrastive accuracy: {cont_acc:.4f} ({cont_correct}/{n})\\\")\\\\nprint(f\\\"SC accuracy:          {sc_acc:.4f} ({sc_correct}/{n})\\\")\\\\nprint(f\\\"Delta:                {delta:+.4f} ({delta*100:+.2f}pp)\\\")\\\\n\\\\n# Discriminative rate\\\\ndiscriminative = sum(1 for r in results if r[\\\\'contrastive_answer\\\\'] != r[\\\\'sc_answer\\\\'])\\\\ndisc_rate = discriminative / n\\\\nprint(f\\\"\\\\\\\\nDiscriminative rate:  {disc_rate:.4f} ({discriminative}/{n})\\\")\\\\n\\\\n# When contrastive disagrees with SC, who is right?\\\\ncont_wins = 0\\\\nsc_wins = 0\\\\nboth_wrong = 0\\\\nfor r in results:\\\\n    if r[\\\\'contrastive_answer\\\\'] != r[\\\\'sc_answer\\\\']:\\\\n        if r[\\\\'contrastive_correct\\\\'] and not r[\\\\'sc_correct\\\\']:\\\\n            cont_wins += 1\\\\n        elif r[\\\\'sc_correct\\\\'] and not r[\\\\'contrastive_correct\\\\']:\\\\n            sc_wins += 1\\\\n        else:\\\\n            both_wrong += 1\\\\n\\\\nprint(f\\\"\\\\\\\\nWhen disagree ({discriminative} cases):\\\")\\\\nprint(f\\\"  Contrastive wins: {cont_wins}\\\")\\\\nprint(f\\\"  SC wins:          {sc_wins}\\\")\\\\nprint(f\\\"  Both wrong:       {both_wrong}\\\")\\\\n\\\\n# McNemar test (2x2 conti
…[truncated 3349 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-18T15:39:07.777376+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "source /root/miniconda3/bin/activate && python3 -c \"\nimport json\nwith open('/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/contrastive_results.json') as f:\n    d = json.load(f)\nr0 = d['results'][0]\nprint('constraints_stats keys:', list(r0.get('constraints_stats',{}).keys()))\nprint('constraints_stats:', r0.get('constraints_stats'))\nprint('maxsat_stats:', r0.get('maxsat_stats'))\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "source /root/miniconda3/bin/activate && python3 -c \"\nimport json\nwith open('/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/contrastive_results.json') as f:\n    d = json.load(f)\nr0 = d['results'][0]\nprint('constraints_stats keys:', list(r0.get('constraints_stats',{}).keys()))\nprint('constraints_stats:', r0.get('constraints_stats'))\nprint('maxsat_stats:', r0.get('maxsat_stats'))\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-18T15:39:07.777592+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"constraints_stats keys: ['total_extracted', 'unique_after_dedup', 'stance_distribution']\\nconstraints_stats: {'total_extracted': 25, 'unique_after_dedup': 18, 'stance_distribution': {'supporting': 9, 'opposing': 16}}\\nmaxsat_stats: {'satisfied': 14, 'excluded': 4, 'total_weight': 16, 'solve_time_ms': 0.7929541170597076}\\n\", \"stderr\": \"Error while loading conda entry point: conda-libmamba-solver (module 'libmambapy' has no attribute 'QueryFormat')\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 27.96}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-18T15:39:07.777790+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "source /root/miniconda3/bin/activate && python3 -c \"\nimport json, math\n\nwith open('/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/contrastive_results.json') as f:\n    d = json.load(f)\n\nresults = d['results']\nn = len(results)\n\n# Core\ncont_correct = sum(1 for r in results if r['contrastive_correct'])\nsc_correct = sum(1 for r in results if r['sc_correct'])\ncont_acc = cont_correct / n\nsc_acc = sc_correct / n\ndelta = cont_acc - sc_acc\n\nprint(f'=== CORE METRICS (n={n}) ===')\nprint(f'Contrastive: {cont_acc:.4f} ({cont_correct}/{n})')\nprint(f'SC baseline: {sc_acc:.4f} ({sc_correct}/{n})')\nprint(f'Delta: {delta*100:+.2f}pp')\n\n# Discriminative\ndisc = sum(1 for r in results if r['contrastive_answer'] != r['sc_answer'])\nprint(f'Discriminative rate: {disc/n:.4f} ({disc}/{n})')\n\n# Disagree breakdown\ncw = sum(1 for r in results if r['contrastive_answer'] != r['sc_answer'] and r['contrastive_correct'] and not r['sc_correct'])\nsw = sum(1 for r in results if r['contrastive_answer'] != r['sc_answer'] and r['sc_correct'] and not r['contrastive_correct'])\nbw = disc - cw - sw\nprint(f'When disagree: cont_wins={cw}, sc_wins={sw}, both_wrong={bw}')\n\n# McNemar\na = sum(1 for r in results if r['contrastive_correct'] and r['sc_correct'])\nb = sum(1 for r in results if r['contrastive_correct'] and not r['sc_correct'])\nc = sum(1 for r in results if not r['contrastive_correct'] and r['sc_correct'])\ndd = sum(1 for r in results if not r['contrastive_correct'] and not r['sc_correct'])\nprint(f'McNemar: both_ok={a}, cont_only={b}, sc_only={c}, both_wrong={dd}')\nif b+c > 0:\n    chi2 = (abs(b-c)-1)**2 / (b+c)\n    z = math.sqrt(chi2)\n    p = 2*(1-0.5*(1+math.erf(z/math.sqrt(2))))\n    print(f'chi2={chi2:.4f}, p={p:.4f}')\n\n# Constraint distribution\nts = 0; to = 0; te = 0; tu = 0\nfor r in results:\n    cs = r.get('constraints_stats', {})\n    te += cs.get('total_extracted', 0)\n    tu += cs.get('unique_after_dedup', 0)\n    sd = cs.get('stance_distribution', {})\n    ts += sd.get('supporting', 0)\n    to += sd.get('opposing', 0)\n\nprint(f'Constraints: extracted={te}, unique={tu}')\nprint(f'Supporting={ts} ({ts/(ts+to)*100:.1f}%), Opposing={to} ({to/(ts+to)*100:.1f}%)')\nprint(f'Avg/problem: {te/n:.1f} extracted, {tu/n:.1f} unique')\nprint(f'Sup/Opp ratio: {ts/to:.2f}')\n\n# Recovery\nprint(f'Recovery rate: {delta*100/13.24*100:+.1f}% (vs oracle 13.24pp)')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "source /root/miniconda3/bin/activate && python3 -c \"\nimport json, math\n\nwith open('/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/contrastive_results.json') as f:\n    d = json.load(f)\n\nresults = d['results']\nn = len(results)\n\n# Core\ncont_correct = sum(1 for r in results if r['contrastive_correct'])\nsc_correct = sum(1 for r in results if r['sc_correct'])\ncont_acc = cont_correct / n\nsc_acc = sc_correct / n\ndelta = cont_acc - sc_acc\n\nprint(f'=== CORE METRICS (n={n}) ===')\nprint(f'Contrastive: {cont_acc:.4f} ({cont_correct}/{n})')\nprint(f'SC baseline: {sc_acc:.4f} ({sc_correct}/{n})')\nprint(f'Delta: {delta*100:+.2f}pp')\n\n# Discriminative\ndisc = sum(1 for r in results if r['contrastive_answer'] != r['sc_answer'])\nprint(f'Discriminative rate: {disc/n:.4f} ({disc}/{n})')\n\n# Disagree breakdown\ncw = sum(1 for r in results if r['contrastive_answer'] != r['sc_answer'] and r['contrastive_correct'] and not r['sc_correct'])\nsw = sum(1 for r in results if r['contrastive_answer'] != r['sc_answer'] and r['sc_correct'] and not r['contrastive_correct'])\nbw = disc - cw - sw\nprint(f'When disagree: cont_wins={cw}, sc_wins={sw}, both_wrong={bw}')\n\n# McNemar\na = sum(1 for r in results if r['contrastive_correct'] and r['sc_correct'])\nb = sum(1 for r in results if r['contrastive_correct'] and not r['sc_correct'])\nc = sum(1 for r in results if not r['contrastive_correct'] and r['sc_correct'])\ndd = sum(1 for r in results if not r['contrastive_correct'] and not r['sc_correct'])\nprint(f'McNemar: both_ok={a}, cont_only={b}, sc_only={c}, both_wrong={dd}')\nif b+c > 0:\n    chi2 = (abs(b-c)-1)**2 / (b+c)\n    z = math.sqrt(chi2)\n    p = 2*(1-0.5*(1+math.erf(z/math.sqrt(2))))\n    print(f'chi2={chi2:.4f}, p={p:.4f}')\n\n# Constraint distribution\nts = 0; to = 0; te = 0; tu = 0\nfor r in results:\n    cs = r.get('constraints_stats', {})\n    te += cs.get('total_extracted', 0)\n    tu += cs.get('unique_after_dedup', 0)\n    sd = cs.get('stance_distribution', {})\n    ts += sd.get('supporting', 0)\n    to += sd.get('opposing', 0)\n\nprint(f'Constraints: extracted={te}, unique={tu}')\nprint(f'Supporting={ts} ({ts/(ts+to)*100:.1f}%), Opposing={to} ({to/(ts+to)*100:.1f}%)')\nprint(f'Avg/problem: {te/n:.1f} extracted, {tu/n:.1f} unique')\nprint(f'Sup/Opp ratio: {ts/to:.2f}')\n\n# Recovery\nprint(f'Recovery rate: {delta*100/13.24*100:+.1f}% (vs oracle 13.24pp)')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-18T15:39:07.778050+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== CORE METRICS (n=182) ===\\nContrastive: 0.7253 (132/182)\\nSC baseline: 0.7363 (134/182)\\nDelta: -1.10pp\\nDiscriminative rate: 0.0604 (11/182)\\nWhen disagree: cont_wins=4, sc_wins=6, both_wrong=1\\nMcNemar: both_ok=128, cont_only=4, sc_only=6, both_wrong=44\\nchi2=0.1000, p=0.7518\\nConstraints: extracted=4436, unique=1899\\nSupporting=1917 (43.2%), Opposing=2519 (56.8%)\\nAvg/problem: 24.4 extracted, 10.4 unique\\nSup/Opp ratio: 0.76\\nRecovery rate: -8.3% (vs oracle 13.24pp)\\n\", \"stderr\": \"Error while loading conda entry point: conda-libmamba-solver (module 'libmambapy' has no attribute 'QueryFormat')\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.14}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-18T15:39:07.778296+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp-029-contrastive-folio204",
  "field": "status",
  "value": "DONE",
  "project": "symb_invariant_consensus",
  "spec": "{'checkpoint_path': '/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/contrastive_results.json', 'log_path': '/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/run.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp-029-contrastive-folio204",
    "field": "status",
    "value": "DONE",
    "project": "symb_invariant_consensus",
    "spec": "{'checkpoint_path': '/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/contrastive_results.json', 'log_path': '/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/run.log'}"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-18T15:39:07.778537+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp-029-contrastive-folio204\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T14:22:03.513Z\", \"updated_at\": \"2026-05-18T15:38:51.252Z\", \"hypothesis\": \"Contrastive constraint extraction (answer-conditioned supporting/opposing constraints with structured JSON output and MaxSAT integration) will achieve discriminative_rate >20% (vs baseline 8.2%) and positive recovery_rate on FOLIO 204, because per-candidate opposing constraints provide stronger signal than simple majority voting for disambiguating closely-scored answers.\", \"parent\": \"exp-026-folio204-trace-regen\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && bash /root/symb_invariant_consensus/scripts/run_exp029_contrastive.sh'\", \"server\": \"westd-25068\", \"gpu\": [\"cuda:3\"], \"pid\": \"42353\", \"log_path\": \"/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/run.log\", \"submitted_at\": \"2026-05-18T14:24:26.683Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/symb_invariant_consensus/results/folio_204_14b/intermediates/\", \"data_count\": 181, \"model_name\": \"Qwen2.5-14B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"exp-026-folio204-trace-regen\", \"eval_data\": \"FOLIO-204\", \"wall_clock_seconds\": 4354.6, \"gpu_hours\": 1.21, \"checkpoint_path\": \"/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/contrastive_results.json\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"results/exp-029-contrastive-folio204/contrastive_results.json\", \"log_path\": \"~/runs/symb_invariant_consensus/exp-029-contrastive-folio204.log\", \"completed_at\": \"2026-05-18T15:37:01.319Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.3426}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-18T15:39:07.778763+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp-029-contrastive-folio204",
  "field": "conclusion",
  "value": "negative",
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp-029-contrastive-folio204",
    "field": "conclusion",
    "value": "negative",
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-18T15:39:07.779169+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp-029-contrastive-folio204\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T14:22:03.513Z\", \"updated_at\": \"2026-05-18T15:38:55.924Z\", \"hypothesis\": \"Contrastive constraint extraction (answer-conditioned supporting/opposing constraints with structured JSON output and MaxSAT integration) will achieve discriminative_rate >20% (vs baseline 8.2%) and positive recovery_rate on FOLIO 204, because per-candidate opposing constraints provide stronger signal than simple majority voting for disambiguating closely-scored answers.\", \"parent\": \"exp-026-folio204-trace-regen\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && bash /root/symb_invariant_consensus/scripts/run_exp029_contrastive.sh'\", \"server\": \"westd-25068\", \"gpu\": [\"cuda:3\"], \"pid\": \"42353\", \"log_path\": \"/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/run.log\", \"submitted_at\": \"2026-05-18T14:24:26.683Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/symb_invariant_consensus/results/folio_204_14b/intermediates/\", \"data_count\": 181, \"model_name\": \"Qwen2.5-14B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"exp-026-folio204-trace-regen\", \"eval_data\": \"FOLIO-204\", \"wall_clock_seconds\": 4354.6, \"gpu_hours\": 1.21, \"checkpoint_path\": \"/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/contrastive_results.json\"}, \"conclusion\": \"negative\", \"checkpoint_path\": \"results/exp-029-contrastive-folio204/contrastive_results.json\", \"log_path\": \"~/runs/symb_invariant_consensus/exp-029-contrastive-folio204.log\", \"completed_at\": \"2026-05-18T15:37:01.319Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4361}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-18T15:39:07.779436+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp-029-contrastive-folio204",
  "field": "metrics",
  "value": "{'contrastive_accuracy': 0.7253, 'sc_accuracy': 0.7363, 'delta_pp': -1.1, 'discriminative_rate': 0.0604, 'discriminative_count': 11, 'n': 182, 'recovery_rate_pct': -8.3, 'mcnemar_chi2': 0.1, 'mcnemar_p': 0.7518, 'cont_only_correct': 4, 'sc_only_correct': 6, 'both_correct': 128, 'both_wrong': 44, 'supporting_pct': 43.2, 'opposing_pct': 56.8, 'avg_constraints_per_problem': 24.4, 'avg_unique_per_problem': 10.4, 'wall_time_min': 47.2}",
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp-029-contrastive-folio204",
    "field": "metrics",
    "value": "{'contrastive_accuracy': 0.7253, 'sc_accuracy': 0.7363, 'delta_pp': -1.1, 'discriminative_rate': 0.0604, 'discriminative_count': 11, 'n': 182, 'recovery_rate_pct': -8.3, 'mcnemar_chi2': 0.1, 'mcnemar_p': 0.7518, 'cont_only_correct': 4, 'sc_only_correct': 6, 'both_correct': 128, 'both_wrong': 44, 'supporting_pct': 43.2, 'opposing_pct': 56.8, 'avg_constraints_per_problem': 24.4, 'avg_unique_per_problem': 10.4, 'wall_time_min': 47.2}",
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-18T15:39:07.779655+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp-029-contrastive-folio204\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T14:22:03.513Z\", \"updated_at\": \"2026-05-18T15:38:58.925Z\", \"hypothesis\": \"Contrastive constraint extraction (answer-conditioned supporting/opposing constraints with structured JSON output and MaxSAT integration) will achieve discriminative_rate >20% (vs baseline 8.2%) and positive recovery_rate on FOLIO 204, because per-candidate opposing constraints provide stronger signal than simple majority voting for disambiguating closely-scored answers.\", \"parent\": \"exp-026-folio204-trace-regen\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && bash /root/symb_invariant_consensus/scripts/run_exp029_contrastive.sh'\", \"server\": \"westd-25068\", \"gpu\": [\"cuda:3\"], \"pid\": \"42353\", \"log_path\": \"/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/run.log\", \"submitted_at\": \"2026-05-18T14:24:26.683Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/symb_invariant_consensus/results/folio_204_14b/intermediates/\", \"data_count\": 181, \"model_name\": \"Qwen2.5-14B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"exp-026-folio204-trace-regen\", \"eval_data\": \"FOLIO-204\", \"wall_clock_seconds\": 4354.6, \"gpu_hours\": 1.21, \"checkpoint_path\": \"/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/contrastive_results.json\"}, \"conclusion\": \"negative\", \"checkpoint_path\": \"results/exp-029-contrastive-folio204/contrastive_results.json\", \"log_path\": \"~/runs/symb_invariant_consensus/exp-029-contrastive-folio204.log\", \"completed_at\": \"2026-05-18T15:37:01.319Z\", \"metrics\": {\"contrastive_accuracy\": 0.7253, \"sc_accuracy\": 0.7363, \"delta_pp\": -1.1, \"discriminative_rate\": 0.0604, \"discriminative_count\": 11, \"n\": 182, \"recovery_rate_pct\": 
…[truncated 359 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_exp-029-results_20260518T153603",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-18T15:39:07.779855+00:00_

Registry 已更新。

## exp-029 结果：**负结果**

| Metric | Value |
|---|---|
| **Contrastive accuracy** | 72.53% (132/182) |
| **SC baseline** | 73.63% (134/182) |
| **Delta** | **-1.10pp** |
| **Discriminative rate** | 6.04% (11/182) — 目标 >20%, baseline 8.2%, 更差 |
| **Recovery rate** | **-8.3%** (vs oracle 13.24pp gap) |
| **McNemar p-value** | 0.7518 (不显著) |

**Disagree breakdown** (11 cases): contrastive wins 4, SC wins 6, both wrong 1

**Constraint distribution**: Supporting 43.2%, Opposing 56.8%, avg 24.4 extracted / 10.4 unique per problem

**结论**: 假设被证伪。Contrastive constraint extraction 在全量 FOLIO 204 上不仅没有提升，反而略低于 SC baseline。discriminative rate (6.04%) 甚至低于之前的 baseline (8.2%)。早期 n=14 的 +14.3pp 增益是小样本偏差。opposing constraints 虽然数量略多 (56.8%)，但未能转化为有效的区分信号。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_check_exp-029-results_20260518T153603"
}
```

</details>

---
