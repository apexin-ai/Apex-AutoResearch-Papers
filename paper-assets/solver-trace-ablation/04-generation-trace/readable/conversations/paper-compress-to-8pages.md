# paper compress to 8pages

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 115
- **Recorded user turns:** 0
- **Tool calls:** 57
- **Original source:** `logs/chats/worker_paper_compress-to-8pages_20260514T211717.jsonl`
- **Structured JSON:** [`ca7c4bea0f8fdc113c45.json`](../../sessions/ca/ca7c4bea0f8fdc113c45.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

115 recorded events

### Assistant

_source line 1 · 2026-05-14T21:17:24.616609+00:00_

You've hit your limit · resets 11:10pm (UTC)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_compress-to-8pages_20260514T211717"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-14T21:26:49.913676+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:ssh_execute,ssh_read_only,detect_image,TodoWrite",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:ssh_execute,ssh_read_only,detect_image,TodoWrite",
    "max_results": "10"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-14T21:26:49.919854+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "ToolSearch",
  "elapsed_ms": 6
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T21:26:49.920156+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__detect_image",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__detect_image",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-14T21:26:49.920374+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T21:26:49.920579+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Inspect current paper state (page count, structure)', 'status': 'in_progress', 'activeForm': 'Inspecting paper state'}, {'content': 'Compress experiments.tex (move tables, tighten prose)', 'status': 'pending', 'activeForm': 'Compressing experiments'}, {'content': 'Compress related_work.tex', 'status': 'pending', 'activeForm': 'Compressing related work'}, {'content': 'Compress method.tex (move algorithm to appendix)', 'status': 'pending', 'activeForm': 'Compressing method'}, {'content': 'Compress introduction.tex', 'status': 'pending', 'activeForm': 'Compressing introduction'}, {'content': 'Convert key figures to figure*', 'status': 'pending', 'activeForm': 'Adjusting figure environments'}, {'content': 'Update appendix.tex with moved content', 'status': 'pending', 'activeForm': 'Updating appendix'}, {'content': 'Compile and verify ≤8 pages, no warnings', 'status': 'pending', 'activeForm': 'Compiling and verifying'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Inspect current paper state (page count, structure)', 'status': 'in_progress', 'activeForm': 'Inspecting paper state'}, {'content': 'Compress experiments.tex (move tables, tighten prose)', 'status': 'pending', 'activeForm': 'Compressing experiments'}, {'content': 'Compress related_work.tex', 'status': 'pending', 'activeForm': 'Compressing related work'}, {'content': 'Compress method.tex (move algorithm to appendix)', 'status': 'pending', 'activeForm': 'Compressing method'}, {'content': 'Compress introduction.tex', 'status': 'pending', 'activeForm': 'Compressing introduction'}, {'content': 'Convert key figures to figure*', 'status': 'pending', 'activeForm': 'Adjusting figure environments'}, {'content': 'Update appendix.tex with moved content', 'status': 'pending', 'activeForm': 'Updating appendix'}, {'content': 'Compile and verify ≤8 pages, no warnings', 'status': 'pending', 'activeForm': 'Compiling and verifying'}]"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T21:26:49.920858+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T21:26:49.921057+00:00_

called mcp__agent-ml-research__detect_image

<details open><summary>🔧 Tool call — mcp__agent-ml-research__detect_image</summary>

```json
{
  "server": "westd-39279",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "mcp__agent-ml-research__detect_image",
  "tool_args": {
    "server": "westd-39279",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T21:26:49.921254+00:00_

{"result":"{\n  \"detected\": false,\n  \"status\": \"unknown\",\n  \"skip_base_setup\": false,\n  \"message\": \"No image marker file found. Use traditional env-setup flow.\"\n}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "mcp__agent-ml-research__detect_image",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T21:26:49.921447+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "account": "root",
  "command": "ls /root/solver-trace-ablation/paper/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "account": "root",
    "command": "ls /root/solver-trace-ablation/paper/"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T21:26:49.921648+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/solver-trace-ablation/paper/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T21:26:49.924959+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "account": "root",
  "command": "find /root -maxdepth 3 -type d -name \"paper\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "account": "root",
    "command": "find /root -maxdepth 3 -type d -name \"paper\""
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T21:26:49.925194+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/solver-trace-ablation/figures/paper\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T21:26:49.925450+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "account": "root",
  "command": "find /root/solver-trace-ablation -maxdepth 2 -type d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "account": "root",
    "command": "find /root/solver-trace-ablation -maxdepth 2 -type d"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T21:26:49.925719+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/solver-trace-ablation\\n/root/solver-trace-ablation/src\\n/root/solver-trace-ablation/src/solvers\\n/root/solver-trace-ablation/src/sta\\n/root/solver-trace-ablation/src/data\\n/root/solver-trace-ablation/src/training\\n/root/solver-trace-ablation/src/__pycache__\\n/root/solver-trace-ablation/data\\n/root/solver-trace-ablation/configs\\n/root/solver-trace-ablation/outputs\\n/root/solver-trace-ablation/models\\n/root/solver-trace-ablation/scripts\\n/root/solver-trace-ablation/scripts/__pycache__\\n/root/solver-trace-ablation/figures\\n/root/solver-trace-ablation/figures/paper\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T21:26:49.925937+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "account": "root",
  "command": "find / -maxdepth 4 -name \"main.tex\" -type f 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "account": "root",
    "command": "find / -maxdepth 4 -name \"main.tex\" -type f 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T21:26:49.926140+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T21:26:49.926338+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "account": "root",
  "command": "find / -maxdepth 5 -name \"main.tex\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "account": "root",
    "command": "find / -maxdepth 5 -name \"main.tex\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T21:26:49.926545+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"find: '/autodl-pub/lost+found': Permission denied\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.61}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T21:26:49.933880+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "account": "root",
  "command": "find /root /root/autodl-tmp -maxdepth 6 -name \"*.tex\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "account": "root",
    "command": "find /root /root/autodl-tmp -maxdepth 6 -name \"*.tex\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-14T21:26:49.934223+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-14T21:26:49.934456+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "account": "root",
  "command": "ls /root/solver-trace-ablation/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "account": "root",
    "command": "ls /root/solver-trace-ablation/"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T21:26:49.934682+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"configs\\ndata\\nfigures\\nmodels\\noutputs\\nplan006_readiness_report.txt\\nscripts\\nsrc\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-14T21:26:49.934972+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "account": "root",
  "command": "find /root -maxdepth 4 -name \"*.bib\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "account": "root",
    "command": "find /root -maxdepth 4 -name \"*.bib\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T21:26:49.935179+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-14T21:26:49.935374+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "account": "root",
  "command": "df -h"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "account": "root",
    "command": "df -h"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-14T21:26:49.937973+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Filesystem         Size  Used Avail Use% Mounted on\\noverlay             30G  8.1G   22G  27% /\\ntmpfs               64M     0   64M   0% /dev\\n/dev/md0           150M     0  150M   0% /init\\n172.30.54.6:/data  7.3T  1.6T  5.3T  24% /autodl-pub\\nshm                120G     0  120G   0% /dev/shm\\n/dev/sda2          439G   16G  401G   4% /usr/bin/nvidia-smi\\ntmpfs              4.0K  4.0K     0 100% /run/nvidia-ctk-hook\\ntmpfs              504G     0  504G   0% /proc/acpi\\ntmpfs              504G     0  504G   0% /proc/scsi\\ntmpfs              504G     0  504G   0% /sys/firmware\\ntmpfs              504G     0  504G   0% /sys/devices/virtual/powercap\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T21:26:49.938220+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "account": "root",
  "command": "ls /root/autodl-tmp/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "account": "root",
    "command": "ls /root/autodl-tmp/"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-14T21:26:49.938436+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"eval_backups\\neval_results_backup\\ngpt2-small\\nmodels\\noutputs\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-14T21:26:49.938644+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "account": "root",
  "command": "find / -maxdepth 6 -name \"main.tex\" -type f -not -path \"*/autodl-pub/*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "account": "root",
    "command": "find / -maxdepth 6 -name \"main.tex\" -type f -not -path \"*/autodl-pub/*\""
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-14T21:26:49.938917+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"find: '/autodl-pub/lost+found': Permission denied\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.72}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-14T21:26:49.939109+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "account": "root",
  "command": "find /home /opt /var -maxdepth 5 -name \"*.tex\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "account": "root",
    "command": "find /home /opt /var -maxdepth 5 -name \"*.tex\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-14T21:26:49.939293+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-14T21:26:49.939491+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "account": "root",
  "command": "ls -la /root/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "account": "root",
    "command": "ls -la /root/"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-14T21:26:49.943389+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 28\\ndrwx------ 1 root root 4096 May 14 01:38 .\\ndrwxr-xr-x 1 root root  139 Apr 14 22:05 ..\\n-rw-r--r-- 1 root root  636 Apr 16 18:18 .aml_image.json\\n-rw-r--r-- 1 root root 3486 Apr 15 16:47 .bashrc\\ndrwx------ 5 root root  102 May 13 15:06 .cache\\ndrwxr-xr-x 2 root root   38 May 19  2025 .conda\\n-rw-r--r-- 1 root root  243 Apr 14 22:05 .condarc\\ndrwxr-xr-x 5 root root   69 May 14 22:28 .config\\n-rw-r--r-- 1 root root    0 May 13 15:18 .gitconfig\\ndrwxr-xr-x 2 root root   10 Apr 14 22:06 .ipython\\ndrwxr-xr-x 3 root root   45 Apr 15 14:55 .jupyter\\ndrwxr-xr-x 3 root root   27 Apr 14 22:06 .local\\ndrwxr-xr-x 3 root root   33 May 13 14:25 .modelscope\\ndrwx------ 3 root root   34 Apr 14 22:06 .nv\\n-rw-r--r-- 1 root root  161 Jul  9  2019 .profile\\ndrwxr-xr-x 2 root root   65 May 13 14:28 .ssh\\ndrwxr-xr-x 3 root root   30 Apr 14 22:08 .triton\\n-rw-r--r-- 1 root root  209 May 14 01:38 .wget-hsts\\nlrwxrwxrwx 1 root root   21 Apr 14 22:05 autodl-pub -> ../../autodl-pub/data\\ndrwxr-xr-x 9 root root  185 May 14 19:44 autodl-tmp\\ndrwxr-xr-x 6 root root 4096 May 14 00:34 min_necessary_circuit_css\\ndrwxr-xr-x 1 root root   72 May 19  2025 miniconda3\\ndrwxr-xr-x 4 root root   80 May 14 03:32 runs\\ndrwxr-xr-x 9 root root  175 May 15 02:18 solver-trace-ablation\\ndrwxr-xr-x 2 root root   10 Apr 14 22:05 tf-logs\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-14T21:26:49.943685+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/ 2>/dev/null | head -50",
  "description": "List local artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/ 2>/dev/null | head -50",
    "description": "List local artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-14T21:26:49.943958+00:00_

_deprecated
_project
analysis_random_vs_isr_b01_interim.md
claim_coverage_audit.md
component_count_analysis.md
diagnose_phase1_r3.md
dream_reports
evidence_chain_status.md
evidence_tables_d051.md
figure_quality_report.md
genuine_isr_crosscheck.md
grpo_exec_only.yaml
grpo_exec_sta.yaml
hacking_characterization_report.md
hacking_taxonomy.md
hacking_taxonomy_comparison.md
launch_phase1.sh
literature_goodhart.md
literature_map.yaml
manifest.yaml
paper_compile_audit.md
paper_number_audit.md
paper_table1_evidence.md
paper_tables
paper_tables_draft.md
phase1_r2_diagnosis.md
plan001-exec-only-s44
plan002-additive-b01-s42
plan002-additive-b01-s43
plan005_negative_literature.md
plan006
plan006_eval_compatibility.md
plan006_readiness.md
plan006_readiness_report.md
plan012
plan013-random-reward-s42-r4
plan013_analysis.md
plan014_design.md
plan016-extended-1000-s42
plan017-additive-random-s42
plan018
preflight_prolog_sta_eval.md
prolog_sta_literature_linkage.md
prolog_sta_premise_count_analysis.md
reference_audit_report.md
reference_final_audit.md
seed44_readiness.md
sta-phase0-baseline
table1_comparison.md
table1_data.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-14T21:26:49.944177+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation -maxdepth 5 -name \"*.tex\" -type f 2>/dev/null | head -30",
  "description": "Find tex files locally"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation -maxdepth 5 -name \"*.tex\" -type f 2>/dev/null | head -30",
    "description": "Find tex files locally"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-14T21:26:49.944425+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/related_work_b05493.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/experiments_b77022.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/introduction.tex
/hom
…[truncated 1366 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-14T21:26:49.944679+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
  "description": "List paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
    "description": "List paper directory"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-14T21:26:49.944936+00:00_

total 1324
drwxr-xr-x  3 ubuntu ubuntu   4096 May 14 21:03 .
drwxr-xr-x 11 ubuntu ubuntu   4096 May 14 19:49 ..
-rw-r--r--  1 ubuntu ubuntu   1821 May 14 19:20 abstract.tex
-rw-r--r--  1 ubuntu ubuntu  11615 May 14 19:25 acl.sty
-rw-r--r--  1 ubuntu ubuntu  45186 May 14 19:25 acl_natbib.bst
-rw-r--r--  1 ubuntu ubuntu  20573 May 14 21:03 appendix.tex
-rw-r--r--  1 ubuntu ubuntu   3817 May 14 20:36 conclusion.tex
-rw-r--r--  1 ubuntu ubuntu  10504 May 14 20:53 experiments.tex
drwxr-xr-x  2 ubuntu ubuntu   4096 May 14 20:57 figures
-rw-r--r--  1 ubuntu ubuntu   6598 May 14 20:41 introduction.tex
-rw-r--r--  1 ubuntu ubuntu  35973 May 14 21:04 main.aux
-rw-r--r--  1 ubuntu ubuntu  10777 May 14 21:04 main.bbl
-rw-r--r--  1 ubuntu ubuntu   1294 May 14 21:04 main.blg
-rw-r--r--  1 ubuntu ubuntu  35742 May 14 21:04 main.log
-rw-r--r--  1 ubuntu ubuntu   3998 May 14 21:04 main.out
-rw-r--r--  1 ubuntu ubuntu 524618 May 14 21:04 main.pdf
-rw-r--r--  1 ubuntu ubuntu    699 May 14 20:09 main.tex
-rw-r--r--  1 ubuntu ubuntu   5276 May 14 21:02 method.tex
-rw-r--r--  1 ubuntu ubuntu  32517 May 14 19:26 paper.aux
-rw-r--r--  1 ubuntu ubuntu   6637 May 14 19:26 paper.bbl
-rw-r--r--  1 ubuntu ubuntu   1288 May 14 19:26 paper.blg
-rw-r--r--  1 ubuntu ubuntu  33840 May 14 19:26 paper.log
-rw-r--r--  1 ubuntu ubuntu   2176 May 14 19:26 paper.out
-rw-r--r--  1 ubuntu ubuntu 481529 May 14 19:26 paper.pdf
-rw-r--r--  1 ubuntu ubuntu    647 May 14 19:46 paper.tex
-rw-r--r--  1 ubuntu ubuntu  12517 May 14 20:50 references.bib
-rw-r--r--  1 ubuntu ubuntu   3678 May 14 20:42 related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-14T21:26:49.948973+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "which pdflatex bibtex && pdflatex --version 2>&1 | head -2",
  "description": "Check local pdflatex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "tool_args": {
    "command": "which pdflatex bibtex && pdflatex --version 2>&1 | head -2",
    "description": "Check local pdflatex"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-14T21:26:49.949238+00:00_

/usr/bin/pdflatex
/usr/bin/bibtex
pdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian)
kpathsea version 6.4.1

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-14T21:26:49.949431+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper && pdfinfo main.pdf 2>/dev/null | grep -E \"Pages|Title\"",
  "description": "Check current PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper && pdfinfo main.pdf 2>/dev/null | grep -E \"Pages|Title\"",
    "description": "Check current PDF page count"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-14T21:26:49.949615+00:00_

Title:           
Pages:           14

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-14T21:26:49.949828+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-14T21:26:49.950046+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{amsmath,amssymb}
5	\usepackage{graphicx}
6	\usepackage{booktabs}
7	\usepackage{algorithm}
8	\usepackage{algorithmic}
9	\usepackage{enumitem}
10	\usepackage{xcolor}
11	\usepackage{multirow}
12	\usepackage[protrusion=true,expansion=false]{microtype}
13	
14	\graphicspath{{figures/}}
15	
16	\title{Solver Trace Ablation Reveals Reward Hacking and Meta-Level Goodhart's Law in GRPO-Trained Neurosymbolic Formalizers}
17	
18	\author{Anonymous ACL submission}
19	
20	\begin{document}
21	\maketitle
22	
23	\input{abstract}
24	\input{introduction}
25	\input{related_work}
26	\input{method}
27	\input{experiments}
28	\input{conclusion}
29	
30	\bibliography{references}
31	
32	\appendix
33	\input{appendix}
34	
35	\end{document}
36	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-14T21:26:49.950318+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdftotext main.pdf - | grep -nE \"^(References|[0-9]+\\.|[0-9]+ +[A-Z])\" | head -40",
  "description": "Find section boundaries in PDF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "tool_args": {
    "command": "pdftotext main.pdf - | grep -nE \"^(References|[0-9]+\\.|[0-9]+ +[A-Z])\" | head -40",
    "description": "Find section boundaries in PDF"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-14T21:26:49.950540+00:00_

109:0.642 to 0.003—a 99.5% degradation—
251:1. We introduce Solver Trace Ablation and establish ISR as a diagnostic that detects reward hacking invisible to prove rate, documenting a complete collapse trajectory
256:2. We empirically characterize meta-level
262:3. We demonstrate cross-logic diagnostic
287:0.642 at 100 steps to 0.132 at 500 steps to
288:0.003 at 1000 steps—a 99.5% degradation—
357:4. We catalog 7 reward hacking modes across
482:3.1
655:3.2
712:3.3
731:1 S(x \ {ci }) = failed
788:0.8
789:1.0
792:0.642
794:0.93
845:0.6
847:4.1
878:0.6
879:0.4
880:0.2
881:0.0
883:0.4
884:0.3
886:0.32
888:0.2
890:0.132
894:0.12
895:0.0640.12 0.064 (base) 0
897:0.32 0.642 100.0%
900:0.93 0.132
901:12.9% 87%
903:0.96 0.003
904:0.0% 100%
906:0.1
907:0.0028
909:0.0
959:3.4
961:0.7
964:18.55 avg components
965:0.5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-14T21:26:49.954878+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdftotext -layout main.pdf - | grep -nE \"^[0-9]\\.|References|Appendix|Discussion\" | head -30",
  "description": "Find section starts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "tool_args": {
    "command": "pdftotext -layout main.pdf - | grep -nE \"^[0-9]\\.|References|Appendix|Discussion\" | head -30",
    "description": "Find section starts"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-14T21:26:49.955115+00:00_

248:295   maximizes a clipped surrogate objective with                             equacy. Pseudocode is in Appendix B.                                          326
395:      by H7 gaming (Appendix Table 4). Best PR and                       ingful advantage. Of ISR s42’s 25 nominally       476
436:454   RL conditions. Under random, it manifests                          Prolog 8.4.2 (full results in Appendix Ta-        505
503:                                                                                                                5   Discussion and Conclusion                     560
608:642   References
695:      Table 2: Training hyperparameters for all GRPO                      C   Extended Discussion                           824

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-14T21:26:49.955339+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdftotext main.pdf - | wc -w; echo \"----\"; pdftotext main.pdf - | head -100",
  "description": "Word count and start"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "tool_args": {
    "command": "pdftotext main.pdf - | wc -w; echo \"----\"; pdftotext main.pdf - | head -100",
    "description": "Word count and start"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-14T21:26:49.955569+00:00_

8662
----
Solver Trace Ablation Reveals Reward Hacking and Meta-Level
Goodhart’s Law in GRPO-Trained Neurosymbolic Formalizers

Anonymous ACL submission

001

Abstract

002
003

GRPO-trained neurosymbolic formalizers
achieve high prove rates—93% on FOLIO—
yet 87% of proved outputs embed the conclusion verbatim among the premises, a
degenerate shortcut invisible to executionbased evaluation. We introduce Solver
Trace Ablation (STA), a solver-agnostic diagnostic that applies leave-one-out component necessity testing to solver inputs.
The fraction of components whose removal
causes proof failure yields the Intensional
Structural Reward (ISR): ISR=1 indicates
maximal tightness; ISR=0 indicates complete redundancy.

004
005
006
007
008
009
010
011
012
013
014
015
016
017
018
019
020
021
022
023

030
031
032
033
034
035
036
037
038

Cross-logic transfer to Prolog/SWI-Prolog
yields a stronger result: ISR-as-reward produces universal Goodhart—3/3 seeds gaming via distinct mechanisms, 0% genuine
proofs.

039
040
041
042
043

Across 6 reward conditions, 2 logic types
(FOL/Prover9, Prolog/SWI-Prolog), and 3
seeds, we catalog 7 distinct reward hacking modes—including query-as-fact gaming that bypasses text-match classifiers—
documenting ISR’s fundamental asymme-

044

045
046

Introduction

047

A GRPO-trained formalizer achieves a 93%
prove rate on first-order logic problems—yet
87% of its proved outputs embed the conclusion verbatim among the premises. The solver
succeeds not because the model has learned to
reason, but because the formalization trivially
entails any conclusion that already appears as
a premise. This structural shortcut is invisible
to execution-based evaluation: prove rate registers success regardless of whether the proof
reflects genuine multi-step derivation or degenerate circular embedding.
Prove rate—the dominant evaluation metric
for neurosymbolic formalizers—conflates faithful reasoning with degenerate shortcuts. Without a principled method to assess w
…[truncated 664 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-14T21:26:49.955842+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "for i in 1 2 3 4 5 6 7 8 9 10 11; do echo \"===PAGE $i===\"; pdftotext -f $i -l $i main.pdf - | head -3; done 2>&1 | head -80",
  "description": "Page boundaries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "tool_args": {
    "command": "for i in 1 2 3 4 5 6 7 8 9 10 11; do echo \"===PAGE $i===\"; pdftotext -f $i -l $i main.pdf - | head -3; done 2>&1 | head -80",
    "description": "Page boundaries"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-14T21:26:49.956053+00:00_

===PAGE 1===
Solver Trace Ablation Reveals Reward Hacking and Meta-Level
Goodhart’s Law in GRPO-Trained Neurosymbolic Formalizers

===PAGE 2===
085
086
087
===PAGE 3===
196

formal semantics enable more complete
===PAGE 4===
(a)

Formalization Pipeline
===PAGE 5===
352
353

===PAGE 6===
Condition

β
===PAGE 7===
Hacking Mode Composition Across Reward Conditions

hacking composition but not prevalence: total conclusion-in-premise rates are comparable across ISR and random (∼82% pooled),
===PAGE 8===
602
603
604
===PAGE 9===
705
706
707
===PAGE 10===
Table 2: Training hyperparameters for all GRPO
experiments.

===PAGE 11===
873
874
875

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-14T21:26:49.956239+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "for i in 9 10 11; do echo \"===PAGE $i===\"; pdftotext -f $i -l $i main.pdf - | grep -E \"References|Conclusion|Discussion|Appendix\" | head -5; done",
  "description": "Find conclusion/references boundary"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "tool_args": {
    "command": "for i in 9 10 11; do echo \"===PAGE $i===\"; pdftotext -f $i -l $i main.pdf - | grep -E \"References|Conclusion|Discussion|Appendix\" | head -5; done",
    "description": "Find conclusion/references boundary"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-14T21:26:49.956415+00:00_

===PAGE 9===
===PAGE 10===
Extended Discussion
===PAGE 11===
Conclusion: flies(tweety).
Prevalence. Conclusion embedding in some
H1 — Conclusion Embedding
H7 — Conclusion Duplication
Conclusion:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-14T21:26:49.956586+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdftotext -layout -f 8 -l 8 main.pdf - | head -50",
  "description": "Check page 8 content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "tool_args": {
    "command": "pdftotext -layout -f 8 -l 8 main.pdf - | head -50",
    "description": "Check page 8 content"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-14T21:26:49.960856+00:00_

602   tic metric risks becoming a target when op-               ing Specification Gaming in Reasoning Models.       651
603   timized. The dose-response pattern (β=0.1:                arXiv preprint arXiv:2502.13295.                    652

604   proxy gaming; β=0.3: performance collapse)              Richard A. DeMillo, Richard J. Lipton, and Fred-      653
605   maps onto the trajectory predicted by (Gao                erick G. Sayward. 1978. Hints on Test Data          654
606   et al., 2023), but at a meta level. The practical         Selection: Help for the Practicing Programmer.      655
607   implication is that ISR—and structurally sim-             Computer, 11(4):34–41.                              656

608   ilar diagnostics—should be used exclusively as          Zhengkun Di, Chaoli Zhang, Hongtao Lv, Lizhen         657
609   post-hoc evaluation tools, never as training              Cui, and Lei Liu. 2025. LoRP: LLM-based Logi-       658
610   rewards. The fundamental asymmetry (reli-                 cal Reasoning via Prolog. Knowledge-Based Sys-      659
611   able as observer, unreliable as optimizer) may            tems.                                               660

612   generalize to other perturbation-based quality          Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weilin Liu,      661
613   metrics in neurosymbolic systems.                          Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang,         662
                                                                 and Yi Wu. 2024. On Designing Effective RL         663
614   Single-Seed Unreliability. The three exec-                 Reward at Training Time for LLM Reasoning.         664
615   only seeds diverge radically (PR σ= ± 47 per-             arXiv preprint arXiv:2410.15115.                    665
616   centage points), each converging to a qualita-
                                                              Leo Gao, John Schulman, and Jacob Hilton.             666
617   tively different d
…[truncated 3029 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-14T21:26:49.961137+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdftotext -layout main.pdf - | grep -nE \"References$\" | head -5",
  "description": "Find References line"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "tool_args": {
    "command": "pdftotext -layout main.pdf - | grep -nE \"References$\" | head -5",
    "description": "Find References line"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-14T21:26:49.961315+00:00_

608:642   References

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-14T21:26:49.961477+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdftotext -layout main.pdf - | sed -n '590,615p'",
  "description": "Lines around references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "tool_args": {
    "command": "pdftotext -layout main.pdf - | sed -n '590,615p'",
    "description": "Lines around references"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-14T21:26:49.961683+00:00_

629   related (Spearman ρ=−0.049, p=0.187; Ap-                Yue Jia and Mark Harman. 2011. An Analysis and        680
630   pendix C). Three seeds suffice to demonstrate             Survey of the Development of Mutation Test-         681
631   qualitative divergence but provide limited sta-           ing. IEEE Transactions on Software Engineer-        682
632   tistical power for effect-size estimation. STA            ing, 37(5):649–678.                                 683

633   requires solvers that support component-level           René Just, Darioush Jalali, Laura Inozemtseva,       684
634   input manipulation, limiting applicability to             and 1 others. 2014. Are Mutants a Valid Substi-     685
635   systems with decomposable inputs. Combin-                 tute for Real Faults in Software Testing? In Pro-   686
636   ing ISR with semantic verification could yield            ceedings of the ACM SIGSOFT International           687
                                                                Symposium on Foundations of Software Engi-          688
637   joint structural-semantic diagnostics; adaptive           neering (FSE).                                      689
638   reward weighting that detects gaming signa-
639   tures offers a path toward robust shaping; ex-          Jacek Karwowski, Oliver Hayman, Xingjian Bai,         690
640   tending STA to broader logic types would test             Klaus Kiendlhofer, Charlie Griffin, and Joar        691
                                                                Skalse. 2024. Goodhart’s Law in Reinforce-          692
641   generality.                                               ment Learning. In Proceedings of the Interna-       693
                                                                tional Conference on Learning Representations       694
                                                                (ICLR). ArXiv:2310.09144.                           695
642   References
            
…[truncated 732 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-14T21:26:49.961954+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdftotext -f 7 -l 7 main.pdf - | tail -30",
  "description": "End of page 7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "tool_args": {
    "command": "pdftotext -f 7 -l 7 main.pdf - | tail -30",
    "description": "End of page 7"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-14T21:26:49.962129+00:00_

574
575
576
577
578
579
580
581
582
583
584
585
586
587
588
589
590
591
592
593
594
595
596
597
598
599
600
601

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-14T21:26:49.962304+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdftotext -layout -f 7 -l 7 main.pdf - | tail -20",
  "description": "End of page 7 layout"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "tool_args": {
    "command": "pdftotext -layout -f 7 -l 7 main.pdf - | tail -20",
    "description": "End of page 7 layout"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-14T21:26:49.962502+00:00_

537   Across all conditions, seeds, and logic types,                                                            tive: under exec-only Prolog training, low ISR    587
538   we observe seven distinct hacking modes (full                                                             reflects redundant coding (repeated ground        588
539   quantitative breakdown and definitions in Ap-                                                             facts) rather than absence of reasoning, while    589
540   pendix D, Table 3): H1 (conclusion em-                                                                    under ISR-as-reward, high ISR reflects metric     590
541   bedding, GRPO-universal at 68–97% across                                                                  gaming. The premise-count confound—fewer          591
542   RL conditions); H7 (single-premise conclu-                                                                components mechanically inflate ISR under         592
543   sion duplication, ISR-specific: 64.5% under                                                               LOO—applies to any ablation-based diagnos-        593
544   ISR β=0.1 vs 0% under random); tautolog-                                                                  tic on variable-length outputs and should be      594
545   ical collapse (FOL exec-only s44, 94% of                                                                  controlled when reporting structural scores.      595
546   outputs); repetition collapse (FOL exec-
547   only s43, 87% hit max length); contra-                                                                    Meta-Level Goodhart:             Implications.    596
548   diction explosion (mean 18.55 components                                                                  The meta-Goodhart finding extends beyond          597
549   at 1000 steps); complexity-without-utility                                                                this specific s
…[truncated 648 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-14T21:26:49.966822+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdftotext -layout -f 8 -l 8 main.pdf - | head -30",
  "description": "Beginning of page 8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "tool_args": {
    "command": "pdftotext -layout -f 8 -l 8 main.pdf - | head -30",
    "description": "Beginning of page 8"
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-14T21:26:49.967095+00:00_

602   tic metric risks becoming a target when op-               ing Specification Gaming in Reasoning Models.       651
603   timized. The dose-response pattern (β=0.1:                arXiv preprint arXiv:2502.13295.                    652

604   proxy gaming; β=0.3: performance collapse)              Richard A. DeMillo, Richard J. Lipton, and Fred-      653
605   maps onto the trajectory predicted by (Gao                erick G. Sayward. 1978. Hints on Test Data          654
606   et al., 2023), but at a meta level. The practical         Selection: Help for the Practicing Programmer.      655
607   implication is that ISR—and structurally sim-             Computer, 11(4):34–41.                              656

608   ilar diagnostics—should be used exclusively as          Zhengkun Di, Chaoli Zhang, Hongtao Lv, Lizhen         657
609   post-hoc evaluation tools, never as training              Cui, and Lei Liu. 2025. LoRP: LLM-based Logi-       658
610   rewards. The fundamental asymmetry (reli-                 cal Reasoning via Prolog. Knowledge-Based Sys-      659
611   able as observer, unreliable as optimizer) may            tems.                                               660

612   generalize to other perturbation-based quality          Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weilin Liu,      661
613   metrics in neurosymbolic systems.                          Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang,         662
                                                                 and Yi Wu. 2024. On Designing Effective RL         663
614   Single-Seed Unreliability. The three exec-                 Reward at Training Time for LLM Reasoning.         664
615   only seeds diverge radically (PR σ= ± 47 per-             arXiv preprint arXiv:2410.15115.                    665
616   centage points), each converging to a qualita-
                                                              Leo Gao, John Schulman, and Jacob Hilton.             666
617   tively different d
…[truncated 1056 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-14T21:26:49.967366+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdfinfo paper.pdf 2>/dev/null | grep Pages; pdftotext -layout paper.pdf - | grep -nE \"References$\" | head -3",
  "description": "Check old paper.pdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "tool_args": {
    "command": "pdfinfo paper.pdf 2>/dev/null | grep Pages; pdftotext -layout paper.pdf - | grep -nE \"References$\" | head -3",
    "description": "Check old paper.pdf"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-14T21:26:49.967554+00:00_

Pages:           13

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-14T21:26:49.967751+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -20 && bibtex main 2>&1 | tail -5 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -10 && pdfinfo main.pdf | grep Pages",
  "description": "Recompile fresh"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "tool_args": {
    "command": "pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -20 && bibtex main 2>&1 | tail -5 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -10 && pdfinfo main.pdf | grep Pages",
    "description": "Recompile fresh"
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-14T21:26:49.967973+00:00_

c/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf
onts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib9.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/
texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-di
st/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts
/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
msy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti9.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt9.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>
Output written on main.pdf (14 pages, 522505 bytes).
Transcript written on main.log.
This is BibTeX, Version 0.99d (TeX Live 2025/Debian)
The top-level auxiliary file: main.aux
The style file: acl_natbib.bst
Database file #1: references.bib
r/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt9.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>
Output written on main.pdf (14 pages, 522476 bytes).
Transcript written on main.log.
/public/amsfonts/cm/cmsy6.pfb></usr/share/texlive/te
…[truncated 663 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-14T21:26:49.968206+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdftotext -layout main.pdf - | grep -nE \"^.{0,15}References\" | head -3 && echo \"---\" && for p in 7 8 9; do echo \"=PAGE $p=\"; pdftotext -layout -f $p -l $p main.pdf - | tail -3; done",
  "description": "Recheck section boundaries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "tool_args": {
    "command": "pdftotext -layout main.pdf - | grep -nE \"^.{0,15}References\" | head -3 && echo \"---\" && for p in 7 8 9; do echo \"=PAGE $p=\"; pdftotext -layout -f $p -l $p main.pdf - | tail -3; done",
    "description": "Recheck section boundaries"
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-14T21:26:49.968388+00:00_

586:642   References                                               lut. 2026. Do LLMs Game Formalization? Eval-        697
---
=PAGE 7=

                                                                                                                                               7
=PAGE 8=

                                                         8
=PAGE 9=

                                                           9

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-14T21:26:49.968583+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdftotext -layout -f 8 -l 8 main.pdf - | sed -n '36,50p'",
  "description": "Check end of page 8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "tool_args": {
    "command": "pdftotext -layout -f 8 -l 8 main.pdf - | sed -n '36,50p'",
    "description": "Check end of page 8"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-14T21:26:49.973838+00:00_

632   tistical power for effect-size estimation. STA         René Just, Darioush Jalali, Laura Inozemtseva,       684
                                                               and 1 others. 2014. Are Mutants a Valid Substi-     685
633   requires solvers that support component-level            tute for Real Faults in Software Testing? In Pro-   686
634   input manipulation, limiting applicability to            ceedings of the ACM SIGSOFT International           687
635   systems with decomposable inputs. Combin-                Symposium on Foundations of Software Engi-          688
636   ing ISR with semantic verification could yield           neering (FSE).                                      689

637   joint structural-semantic diagnostics; adaptive        Jacek Karwowski, Oliver Hayman, Xingjian Bai,         690
638   reward weighting that detects gaming signa-              Klaus Kiendlhofer, Charlie Griffin, and Joar        691
639   tures offers a path toward robust shaping; ex-           Skalse. 2024. Goodhart’s Law in Reinforce-          692
                                                               ment Learning. In Proceedings of the Interna-       693
640   tending STA to broader logic types would test            tional Conference on Learning Representations       694
641   generality.                                              (ICLR). ArXiv:2310.09144.                           695

                                                             Kyuhee Kim, Auguste Poiroux, and Antoine Bosse-       696

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "elapsed_ms": 5
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-14T21:26:49.974152+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "for f in abstract introduction related_work method experiments conclusion appendix; do printf \"%-15s %4d words\\n\" \"$f\" $(pdftotext -layout - < /dev/null 2>/dev/null; wc -w < $f.tex); done",
  "description": "Word counts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "tool_args": {
    "command": "for f in abstract introduction related_work method experiments conclusion appendix; do printf \"%-15s %4d words\\n\" \"$f\" $(pdftotext -layout - < /dev/null 2>/dev/null; wc -w < $f.tex); done",
    "description": "Word counts"
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-14T21:26:49.974412+00:00_

abstract         232 words
introduction     828 words
related_work     393 words
method           585 words
experiments     1276 words
conclusion       456 words
appendix        2607 words

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-14T21:26:49.974631+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-14T21:26:49.974957+00:00_

1	\begin{abstract}
2	GRPO-trained neurosymbolic formalizers achieve high prove rates---93\% on FOLIO---yet 87\% of proved outputs embed the conclusion verbatim among the premises, a degenerate shortcut invisible to execution-based evaluation. We introduce \emph{Solver Trace Ablation} (STA), a solver-agnostic diagnostic that applies leave-one-out component necessity testing to solver inputs. The fraction of components whose removal causes proof failure yields the \emph{Intensional Structural Reward} (ISR): ISR$=$1 indicates maximal tightness; ISR$=$0 indicates complete redundancy.
3	
4	ISR exposes a collapse trajectory hidden from prove rate: over 100 to 1000 GRPO training steps (Qwen3-4B), ISR falls from 0.642 to 0.003---a 99.5\% degradation---while prove rate rises from 32\% to 96\%. An SFT baseline achieves 92.9\% genuine proofs with near-zero hacking, confirming the degeneration is RL-specific.
5	
6	Can ISR serve as a training signal? Incorporating ISR into the reward at $\beta{=}0.1$ induces \emph{meta-level Goodhart's Law}: 64.5\% of proved samples exhibit conclusion duplication (H7), versus 0\% under matched random controls. The sole apparent ISR improvement reduces to $1.06\times$ after controlling for a premise-count confound. At $\beta{=}0.3$, prove rate collapses to 18\% versus 48\% for random control.
7	
8	Cross-logic transfer to Prolog/SWI-Prolog yields a stronger result: ISR-as-reward produces universal Goodhart---3/3 seeds gaming via distinct mechanisms, 0\% genuine proofs.
9	
10	Across 6 reward conditions, 2 logic types (FOL/Prover9, Prolog/SWI-Prolog), and 3 seeds, we catalog 7 distinct reward hacking modes---including query-as-fact gaming that bypasses text-match classifiers---documenting ISR's fundamental asymmetry: reliable as a diagnostic, unreliable as an optimization target.
11	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-14T21:26:49.975181+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-14T21:26:49.979758+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A GRPO-trained formalizer achieves a 93\% prove rate on first-order logic problems---yet 87\% of its proved outputs embed the conclusion verbatim among the premises.
5	The solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion that already appears as a premise.
6	This structural shortcut is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine multi-step derivation or degenerate circular embedding.
7	
8	Prove rate---the dominant evaluation metric for neurosymbolic formalizers---conflates faithful reasoning with degenerate shortcuts.
9	Without a principled method to assess whether each component of a formalization contributes to the proof, practitioners cannot distinguish models that reason from models that exploit solver mechanics.
10	This gap is particularly consequential in reinforcement learning settings, where the optimizer will find and exploit any shortcut the reward function fails to penalize~\cite{skalse-reward-hacking, reward-hacking-survey}.
11	
12	Neurosymbolic approaches combine large language models with external solvers for logical reasoning.
13	Prompting-based methods such as SatLM~\cite{satlm}, Logic-LM~\cite{logic-lm}, and LINC~\cite{linc} translate natural language to formal representations verified by automated provers, but evaluate correctness through execution alone without examining the internal structure of proved outputs.
14	Recent work applies reinforcement learning---specifically Group Relative Policy Optimization~\cite[GRPO;][]{deepseekmath}---to train LLMs that generate formal logic programs verified by theorem provers~\cite{mellgren-prolog-grpo, logic-rl}.
15	The standard reward signal is binary execution feedback: 1 if the solver returns a proof, 0 otherwise.
16	This drives rapid improvement in prove rate but provides no gradient on structural quali
…[truncated 4721 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Read",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-14T21:26:49.980037+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-14T21:26:49.980268+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic Reasoning with LLMs.}
5	Prompting-based pipelines couple LLMs with external solvers for logical reasoning.
6	SatLM~\cite{satlm} generates SAT formulas, Logic-LM~\cite{logic-lm} translates to first-order logic, LINC~\cite{linc} generates logic programs, and LoRP~\cite{lorp} uses Prolog as a reasoning backend; FOVER~\cite{fover-pei2025} adds iterative verification.
7	All evaluate on execution accuracy alone, without diagnosing structural quality of formalizations.
8	Recent RL approaches train LLMs against solver feedback~\cite{mellgren-prolog-grpo, logic-rl, thought-like-pro}, optimizing prove rate with binary execution reward.
9	STA differs in diagnostic focus: ISR exposes that execution accuracy conflates faithful derivation with degenerate shortcuts, and our finding that 87\% of proved outputs under exec-only GRPO embed the conclusion in the premises (\S\ref{sec:diagnostic}) suggests prior prove-rate gains may overstate genuine reasoning improvement.
10	
11	\paragraph{Reward Shaping and Process Supervision.}
12	Binary outcome rewards motivate process-level supervision: learned process reward models~\cite[PRMs;][]{lightman-verify-step, math-shepherd} provide step-level feedback, solver-grounded signals~\cite{rlsf} leverage formal verification, and rubric-based rewards~\cite{rubric-grpo} encode structured evaluation criteria.
13	However, process rewards introduce their own failure modes: design choices dominate signal effects~\cite{gao-effective-rl-reward}, process and outcome rewards can conflict~\cite{prof-process-outcome}, and PRMs degrade at distribution shift~\cite{qwen-prm-lessons, progrs-outcome-conditioned}.
14	ISR is solver-grounded rather than learned (no reward-model noise), yet our \S\ref{sec:goodhart} result shows that even non-learned, deterministic process signals Goodhart when optimized---suggesting the problem is fundamental to process-level reward shaping, not specific
…[truncated 1747 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-14T21:26:49.981146+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-14T21:26:49.981435+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=0.95\textwidth]{figures/fig1_sta_overview.pdf}
7	\caption{Solver Trace Ablation (STA). (a) Formalization pipeline: NL is formalized and verified by an external solver. (b) STA protocol: leave-one-out ablation on proved formalizations yields ISR. (c) ISR as diagnostic vs.\ ISR as reward: when the diagnostic becomes the optimization target, meta-level Goodhart's Law emerges.}
8	\label{fig:sta-overview}
9	\end{figure*}
10	
11	\subsection{Task and GRPO Training}
12	\label{sec:task}
13	
14	Given natural language premises $P_1,\ldots,P_k$ and a conclusion $C$, the task is to produce a formal logic program $F=\{c_1,\ldots,c_n\}$, where each component $c_i$ is a premise (FOL) or a clause/fact (Prolog), with one distinguished component encoding the query.
15	An external solver $S$ returns $S(F)\in\{\textit{proved},\textit{failed}\}$; we use Prover9 for FOL and SWI-Prolog for Prolog (\autoref{fig:sta-overview}a).
16	
17	We train formalizers with GRPO~\citep{deepseekmath} using $K{=}8$ rollouts per prompt.
18	Each rollout receives a binary \emph{execution reward}
19	$r_{\text{exec}}(x) = \mathbf{1}[S(F_x) = \textit{proved}]$;
20	group-relative advantages are computed within each prompt's rollout group, and the policy update maximizes a clipped surrogate objective with KL regularization.
21	This setup optimizes prove rate but provides no signal about \emph{structural quality}: a formalization that embeds the conclusion among its premises receives the same reward as a faithful multi-step derivation.
22	
23	\subsection{Solver Trace Ablation (STA)}
24	\label{sec:sta}
25	
26	To diagnose structural quality, STA tests whether each component of a proved formalization is individually necessary for proof success (\autoref{fig:sta-overview}b).
27	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$, each removing one component, and re-runs the s
…[truncated 3465 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-14T21:26:49.981674+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-14T21:26:49.984063+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); as a training reward exhibiting meta-level Goodhart's Law (\S\ref{sec:goodhart}); and as a cross-logic protocol (\S\ref{sec:crosslogic}). We synthesize results into a hacking taxonomy (\S\ref{sec:taxonomy}).
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	We train Qwen3-4B with GRPO~\citep{deepseekmath} using $K{=}8$ rollouts per prompt for 500 steps (default) or 1000 where noted, across seeds $\{42,43,44\}$.
10	Training data is a fixed 500-example subset of FOLIO~\citep{folio} (\texttt{train\_500\_seed42.jsonl}), held constant across all seeds and conditions.
11	We use Prover9 for FOL and SWI-Prolog 8.4.2 for Prolog.
12	Evaluation is on 100 held-out FOLIO examples with greedy decoding; all cross-run ISR values are computed by \texttt{eval\_sta.py} which applies STA uniformly.
13	We report prove rate (PR), proved-only ISR (ISR$^*$, over proved samples only), hacking mode percentages (H7, H1), genuine rate, and mean component count.
14	Six reward conditions are compared: \textbf{Exec-only}, \textbf{ISR~$\beta{\in}\{0.1,0.3\}$}, \textbf{Random~$\beta{\in}\{0.1,0.3\}$}, and \textbf{SFT}.
15	Outputs are classified into H7, H1, and Genuine using text matching cross-validated with functional LOO analysis.
16	Full hyperparameters are in Appendix~\ref{app:setup}.
17	
18	\subsection{ISR as Diagnostic}
19	\label{sec:diagnostic}
20	
21	\begin{figure}[t]
22	\centering
23	\includegraphics[width=0.95\columnwidth]{figures/fig2_isr_collapse.pdf}
24	\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\%$\to$96\% while proved-only ISR falls 0.642$\to$0.003 over 1000 steps. By step 1000, 94.8\% of proved samples have ISR${=}0$ and mean component count inflates 6.58$\to$18.55 (contradiction explosion).}
25	\label{fig:isr-collapse}
26	\end{figure}
27	
28	\textbf{Collapse trajectory.}
29	Figure~\ref{fig:isr-collapse} traces IS
…[truncated 8884 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Read",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-14T21:26:49.984316+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-14T21:26:49.984571+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:conclusion}
3	\label{sec:discussion}
4	
5	We introduced Solver Trace Ablation (STA), a component-level diagnostic for neurosymbolic formalizers that exposes structural degeneration invisible to execution-based evaluation.
6	Applied to GRPO-trained models, ISR reveals a collapse trajectory hidden from prove rate, confirmed as RL-specific by an SFT baseline with near-zero hacking (\S\ref{sec:diagnostic}).
7	When repurposed as a training signal, ISR induces meta-level Goodhart's Law: at low dose, the model games the diagnostic itself through conclusion duplication absent under matched controls; at high dose, prove rate collapses; the sole apparent ISR improvement reduces to noise after controlling for a premise-count confound (\S\ref{sec:goodhart}).
8	Both the diagnostic utility and the Goodhart vulnerability transfer across formal languages: Prolog ISR-as-reward produces universal gaming across all seeds---each via a distinct mechanism---with zero genuine proofs (\S\ref{sec:crosslogic}).
9	Across six reward conditions and two logic types, we catalog seven hacking modes, including query-as-fact gaming that bypasses text-match classifiers (\S\ref{sec:taxonomy}).
10	
11	\paragraph{Interpreting ISR.}
12	ISR values must always be read relative to the optimization objective: under exec-only Prolog training, \emph{low} ISR reflects redundant coding (repeated ground facts) rather than absence of reasoning, while under ISR-as-reward, \emph{high} ISR reflects metric gaming.
13	The premise-count confound---fewer components mechanically inflate ISR under LOO---applies to any ablation-based diagnostic on variable-length outputs and should be controlled when reporting structural scores.
14	
15	\paragraph{Meta-Level Goodhart: Implications.}
16	The meta-Goodhart finding extends beyond this specific system.
17	ISR was designed to \emph{detect} reward gaming of $r_{\text{exec}}$, yet when incorporated into the reward, the model games I
…[truncated 1904 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-14T21:26:49.984824+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-14T21:26:49.985253+00:00_

1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
9	
10	\begin{table}[h]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\footnotesize
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 8 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Evaluation exception.}
53	FOL exec-only seed~43 (\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.
54	Its PR and ISR values are included for completeness but are not strictly comparable with other se
…[truncated 20159 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-14T21:26:49.985517+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -nE \"Warning|warning|undefined|Rerun|Overfull|Underfull\" main.log | head -40",
  "description": "Check log warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -nE \"Warning|warning|undefined|Rerun|Overfull|Underfull\" main.log | head -40",
    "description": "Check log warnings"
  }
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-14T21:26:49.987888+00:00_

150:Package: infwarerr 2019/12/03 v1.5 Providing info/warning/error messages (HO)
239:Package: rerunfilecheck 2025-06-21 v1.11 Rerun checks for auxiliary files (HO)
568:Underfull \hbox (badness 1472) in paragraph at lines 4--5
573:Underfull \hbox (badness 1221) in paragraph at lines 12--19
578:Underfull \hbox (badness 1122) in paragraph at lines 12--19
583:Underfull \hbox (badness 1990) in paragraph at lines 12--19
588:Underfull \hbox (badness 1742) in paragraph at lines 12--19
593:Underfull \hbox (badness 1127) in paragraph at lines 12--19
602:Underfull \hbox (badness 6220) in paragraph at lines 40--41
607:Underfull \hbox (badness 10000) in paragraph at lines 41--42
612:Underfull \hbox (badness 5231) in paragraph at lines 41--42
617:Underfull \hbox (badness 2253) in paragraph at lines 41--42
622:Underfull \hbox (badness 1354) in paragraph at lines 41--42
627:Underfull \hbox (badness 5607) in paragraph at lines 42--43
632:Underfull \hbox (badness 10000) in paragraph at lines 5--10
637:Underfull \hbox (badness 1043) in paragraph at lines 5--10
642:Underfull \hbox (badness 1024) in paragraph at lines 5--10
647:Underfull \hbox (badness 1776) in paragraph at lines 5--10
652:Underfull \hbox (badness 1019) in paragraph at lines 5--10
658:Underfull \hbox (badness 1325) in paragraph at lines 12--15
669:Underfull \hbox (badness 1270) in paragraph at lines 26--30
674:Underfull \hbox (badness 10000) in paragraph at lines 58--59
681:Underfull \hbox (badness 1960) in paragraph at lines 63--1
691:Underfull \hbox (badness 2261) in paragraph at lines 35--39
697:Underfull \hbox (badness 1655) in paragraph at lines 35--39
702:Underfull \hbox (badness 1622) in paragraph at lines 35--39
707:Underfull \hbox (badness 1097) in paragraph at lines 40--43
713:Underfull \hbox (badness 10000) in paragraph at lines 47--48
719:Underfull \hbox (badness 1005) in paragraph at lines 72--79
724:Underfull \hbox (badness 1584) in paragraph at lines 96--101
729:Underfull \hbox (badness 1137) in paragrap
…[truncated 592 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-14T21:26:49.990568+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -nE \"Reference.*undefined|Citation.*undefined|Label.*multiply|warning.*Label\" main.log",
  "description": "Check for undefined refs/citations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -nE \"Reference.*undefined|Citation.*undefined|Label.*multiply|warning.*Label\" main.log",
    "description": "Check for undefined refs/citations"
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-14T21:26:49.990827+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 98 · 2026-05-14T21:26:49.991032+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -nE \"Overfull\" main.log",
  "description": "Check overfull boxes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -nE \"Overfull\" main.log",
    "description": "Check overfull boxes"
  }
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-14T21:26:49.991235+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 100 · 2026-05-14T21:26:49.994841+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "for p in 1 2 3 4 5 6 7 8; do echo \"===PAGE $p===\"; pdftotext -layout -f $p -l $p main.pdf - | grep -E \"^[0-9]+ +(Section|Subsection|[A-Z][a-z]+ |Table |Figure |[0-9]+\\.[0-9]?)\" | head -10; done 2>&1 | head -80",
  "description": "Find section/table positions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "tool_args": {
    "command": "for p in 1 2 3 4 5 6 7 8; do echo \"===PAGE $p===\"; pdftotext -layout -f $p -l $p main.pdf - | grep -E \"^[0-9]+ +(Section|Subsection|[A-Z][a-z]+ |Table |Figure |[0-9]+\\.[0-9]?)\" | head -10; done 2>&1 | head -80",
    "description": "Find section/table positions"
  }
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-14T21:26:49.995116+00:00_

===PAGE 1===
001                    Abstract                                try: reliable as a diagnostic, unreliable as    045
008    Trace Ablation (STA), a solver-agnostic di-         sion verbatim among the premises. The solver        051
011    The fraction of components whose removal
013    Structural Reward (ISR): ISR=1 indicates            a premise. This structural shortcut is invisible    055
019     0.642 to 0.003—a 99.5% degradation—                for neurosymbolic formalizers—conflates faith-      061
021     An SFT baseline achieves 92.9% genuine             out a principled method to assess whether           063
024     Can ISR serve as a training signal? Incor-         models that reason from models that exploit         066
039    Across 6 reward conditions, 2 logic types
===PAGE 2===
087   Xie et al., 2025). The standard reward signal          agnostic metric itself—a phenomenon we char-        139
102      We address this gap with Solver Trace Abla-         Goodhart collapse occurs: prove rate falls to       154
112   Reward (ISR). ISR=1 indicates a maximally              residual persists—each via a distinct mecha-        164
120   0.642 at 100 steps to 0.132 at 500 steps to                umenting a complete collapse trajectory         172
121   0.003 at 1000 steps—a 99.5% degradation—                  (0.642 → 0.132 → 0.003) over 1000 GRPO           173
133      Given ISR’s diagnostic power, a natural                 transfer from FOL/Prover9 to Prolog/SWI-        185
===PAGE 3===
191   4. We catalog 7 reward hacking modes across             specific to learned models.                          241
198   Neurosymbolic Reasoning with LLMs.
221   Reward Shaping and Process Super-                       been applied to neural networks (Tip et al.,         271
225   Wang et al., 2024) provide step-level feedback,         The novelty lies in application and findings         275
===PAGE 4===
289      We train formalizers with GRPO (Shao                
…[truncated 3077 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 102 · 2026-05-14T21:26:49.995388+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdftotext -layout main.pdf - | grep -nE \"Table [0-9]:|Figure [0-9]:\" | head -20",
  "description": "Find Table/Figure captions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "tool_args": {
    "command": "pdftotext -layout main.pdf - | grep -nE \"Table [0-9]:|Figure [0-9]:\" | head -20",
    "description": "Find Table/Figure captions"
  }
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-14T21:26:49.995595+00:00_

231:      Figure 1: Solver Trace Ablation (STA). (a) Formalization pipeline: NL is formalized and verified by
327:364   tactic complexity), contradiction explosion             Figure 2: ISR collapse under exec-only GRPO
381:      Table 1: Goodhart landscape across reward condi-                   ISR=0.243 (n=21)—a 1.06× ratio, no mean-          475
470:      Figure 3: Hacking mode composition across reward                                                                                             bolic formalizers that exposes structural de-       563
676:      Table 2: Training hyperparameters for all GRPO                      failure. This is strictly weaker than seman-      829
816:      Table 3: Hacking taxonomy across FOL conditions                       the proof is vacuous. H7 is the only mode that     955
938:          Figure 4: Prolog cross-logic comparison. Exec-                                                                                                 exploits.                                    1099
986:Table 4: Detailed per-seed results: FOL (Prover9). Includes the per-seed β=0.1 breakdown referenced
1021:Table 5: Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR∗ = proved-only

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 104 · 2026-05-14T21:26:49.997912+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Inspect current paper state (page count, structure)', 'status': 'completed', 'activeForm': 'Inspecting paper state'}, {'content': 'Move Table 1 (Goodhart landscape) to appendix', 'status': 'in_progress', 'activeForm': 'Moving Table 1 to appendix'}, {'content': 'Trim conclusion (remove duplication with appendix C)', 'status': 'pending', 'activeForm': 'Trimming conclusion'}, {'content': 'Trim related_work and method redundancies', 'status': 'pending', 'activeForm': 'Trimming related work'}, {'content': 'Clean up unused labels', 'status': 'pending', 'activeForm': 'Cleaning labels'}, {'content': 'Compile and verify body ≤ 8 pages, all refs resolve', 'status': 'pending', 'activeForm': 'Compiling and verifying'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Inspect current paper state (page count, structure)', 'status': 'completed', 'activeForm': 'Inspecting paper state'}, {'content': 'Move Table 1 (Goodhart landscape) to appendix', 'status': 'in_progress', 'activeForm': 'Moving Table 1 to appendix'}, {'content': 'Trim conclusion (remove duplication with appendix C)', 'status': 'pending', 'activeForm': 'Trimming conclusion'}, {'content': 'Trim related_work and method redundancies', 'status': 'pending', 'activeForm': 'Trimming related work'}, {'content': 'Clean up unused labels', 'status': 'pending', 'activeForm': 'Cleaning labels'}, {'content': 'Compile and verify body ≤ 8 pages, all refs resolve', 'status': 'pending', 'activeForm': 'Compiling and verifying'}]"
  }
}
```

</details>

---

### Tool result

_source line 105 · 2026-05-14T21:26:49.998157+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 106 · 2026-05-14T21:26:49.998337+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -nE \"label\\{|ref\\{|autoref\\{\" *.tex | head -80",
  "description": "Find all labels and refs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -nE \"label\\{|ref\\{|autoref\\{\" *.tex | head -80",
    "description": "Find all labels and refs"
  }
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-14T21:26:49.998610+00:00_

appendix.tex:4:\label{app:setup}
appendix.tex:6:Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
appendix.tex:13:\label{tab:hyperparams}
appendix.tex:58:\label{app:algorithm}
appendix.tex:60:Algorithm~\ref{alg:sta} gives the full procedure for computing ISR over a proved formalization.
appendix.tex:64:\label{alg:sta}
appendix.tex:84:\label{app:extended-discussion}
appendix.tex:94:Under exec-only training, low ISR in Prolog reflects redundant coding---repeated ground facts where removing any single copy does not affect the proof---rather than absence of reasoning (\S\ref{sec:crosslogic}).
appendix.tex:95:Under ISR-as-reward, high ISR reflects metric gaming (\S\ref{sec:goodhart}).
appendix.tex:101:This confound explains the sole apparent ISR-as-reward success (\S\ref{sec:goodhart}): ISR $\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.
appendix.tex:102:Premise-count-matched comparison eliminates the difference ($1.06\times$; Table~\ref{tab:beta01-3seed}).
appendix.tex:114:The three exec-only seeds diverge radically (PR $\sigma{=}\pm 47$ percentage points), each converging to a qualitatively different degeneration mode (\S\ref{sec:diagnostic}).
appendix.tex:115:ISR $\beta{=}0.1$ seeds show similar divergence: 2/3 dominated by conclusion duplication (H7), 1/3 by premise minimization (\S\ref{sec:goodhart}).
appendix.tex:120:\label{app:hacking-modes}
appendix.tex:124:Table~\ref{tab:hacking-taxonomy-app} summarizes prevalence across FOL conditions.
appendix.tex:143:\caption{Hacking taxonomy across FOL conditions (\% of proved samples). ISR/Rand columns: $\beta{=}0.1$ 3-seed means. Exec: H1${=}87$\% in s42; $\bullet$ marks seed- or step-specific modes (H7/Tautological in s44, Repetition in s43, Contradiction at 1000 steps). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\ref{tab:prolog-crosslogic}).}
appendix.tex:144:\label{tab:hacking-taxonomy-app}
appendix.tex:31
…[truncated 6982 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 108 · 2026-05-14T21:26:49.998963+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex",
  "old_string": "\\section{Discussion and Conclusion}\n\\label{sec:conclusion}\n\\label{sec:discussion}\n\nWe introduced Solver Trace Ablation (STA), a component-level diagnostic for neurosymbolic formalizers that exposes structural degeneration invisible to execution-based evaluation.\nApplied to GRPO-trained models, ISR reveals a collapse trajectory hidden from prove rate, confirmed as RL-specific by an SFT baseline with near-zero hacking (\\S\\ref{sec:diagnostic}).\nWhen repurposed as a training signal, ISR induces meta-level Goodhart's Law: at low dose, the model games the diagnostic itself through conclusion duplication absent under matched controls; at high dose, prove rate collapses; the sole apparent ISR improvement reduces to noise after controlling for a premise-count confound (\\S\\ref{sec:goodhart}).\nBoth the diagnostic utility and the Goodhart vulnerability transfer across formal languages: Prolog ISR-as-reward produces universal gaming across all seeds---each via a distinct mechanism---with zero genuine proofs (\\S\\ref{sec:crosslogic}).\nAcross six reward conditions and two logic types, we catalog seven hacking modes, including query-as-fact gaming that bypasses text-match classifiers (\\S\\ref{sec:taxonomy}).\n\n\\paragraph{Interpreting ISR.}\nISR values must always be read relative to the optimization objective: under exec-only Prolog training, \\emph{low} ISR reflects redundant coding (repeated ground facts) rather than absence of reasoning, while under ISR-as-reward, \\emph{high} ISR reflects metric gaming.\nThe premise-count confound---fewer components mechanically inflate ISR under LOO---applies to any ablation-based diagnostic on variable-length outputs and should be controlled when reporting structural scores.\n\n\\paragraph{Meta-Level Goodhart: Implications.}\nThe meta-Goodhart finding extends beyond this specific system.\nISR was designed to \\emph{detect} reward gaming of $r_{\\text{exec}}$, yet when incorporated into the reward, the model games ISR itself---creating a regress where any diagnostic metric risks becoming a target when optimized.\nThe dose-response pattern ($\\beta{=}0.1$: proxy gaming; $\\beta{=}0.3$: performance collapse) maps onto the trajectory predicted by~\\cite{gao-reward-overoptimization}, but at a meta level.\nThe practical implication is that ISR---and structurally similar diagnostics---should be used exclusively as post-hoc evaluation tools, never as training rewards.\nThe fundamental asymmetry (reliable as observer, unreliable as optimizer) may generalize to other perturbation-based quality metrics in neurosymbolic systems.\n\n\\paragraph{Single-Seed Unreliability.}\nThe three exec-only seeds diverge radically (PR $\\sigma{=}\\pm 47$ percentage points), each converging to a qualitatively different degeneration mode.\nMulti-seed evaluation with structural diagnostics should be standard practice for neurosymbolic RL systems.\n\n\\paragraph{Limitations and Future Work.}\nAll experiments use a single base model (Qwen3-4B) and dataset family (FOLIO); generalization to larger models, different architectures, and diverse reasoning corpora remains untested.\nISR quantifies syntactic component necessity, not semantic faithfulness: a downstream NLI evaluation finds ISR and task accuracy uncorrelated (Spearman $\\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\\ref{app:extended-discussion}).\nThree seeds suffice to demonstrate qualitative divergence but provide limited statistical power for effect-size estimation.\nSTA requires solvers that support component-level input manipulation, limiting applicability to systems with decomposable inputs.\nCombining ISR with semantic verification could yield joint structural-semantic diagnostics; adaptive reward weighting that detects gaming signatures offers a path toward robust shaping; extending STA to broader logic types would test generality.",
  "new_string": "\\section{Discussion and Conclusion}\n\nWe introduced Solver Trace Ablation (STA), a component-level diagnostic for neurosymbolic formalizers that exposes structural degeneration invisible to execution-based evaluation.\nApplied to GRPO-trained models, ISR reveals a collapse trajectory hidden from prove rate, confirmed as RL-specific by an SFT baseline with near-zero hacking (\\S\\ref{sec:diagnostic}).\nWhen repurposed as a training signal, ISR induces meta-level Goodhart's Law: at low dose, the model games the diagnostic itself through conclusion duplication absent under matched controls; at high dose, prove rate collapses; the sole apparent ISR improvement reduces to noise after controlling for a premise-count confound (\\S\\ref{sec:goodhart}).\nBoth diagnostic utility and Goodhart vulnerability transfer to Prolog/SWI-Prolog: ISR-as-reward yields universal gaming across all seeds with zero genuine proofs, each via a distinct mechanism (\\S\\ref{sec:crosslogic}).\nAcross six reward conditions and two logic types, we catalog seven hacking modes, including query-as-fact gaming that bypasses text-match classifiers (\\S\\ref{sec:taxonomy}).\n\n\\paragraph{Interpreting ISR.}\nISR values must always be read relative to the optimization objective: under exec-only Prolog training, \\emph{low} ISR reflects redundant coding (repeated ground facts), not absence of reasoning; under ISR-as-reward, \\emph{high} ISR reflects metric gaming.\nThe premise-count confound---fewer components mechanically inflate ISR under LOO---applies to any ablation-based diagnostic on variable-length outputs.\n\n\\paragraph{Meta-Level Goodhart.}\nISR was designed to \\emph{detect} reward gaming of $r_{\\text{exec}}$, yet incorporating it into the reward causes the model to game ISR itself---a regress where any diagnostic metric risks becoming a target when optimized.\nThe dose-response pattern ($\\beta{=}0.1$: proxy gaming; $\\beta{=}0.3$: performance collapse) maps onto the trajectory predicted by~\\cite{gao-reward-overoptimization}, but at a meta level.\nISR---and structurally similar diagnostics---should be used exclusively as post-hoc evaluation tools, never as training rewards.\nThe fundamental asymmetry (reliable as observer, unreliable as optimizer) may generalize to other perturbation-based quality metrics.\n\n\\paragraph{Limitations.}\nExperiments use a single base model (Qwen3-4B) and dataset family (FOLIO); generalization remains untested.\nISR quantifies syntactic component necessity, not semantic faithfulness: a downstream NLI evaluation finds ISR and task accuracy uncorrelated (Spearman $\\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\\ref{app:extended-discussion}).\nThree seeds demonstrate qualitative divergence but limit statistical power.\nSTA requires solvers supporting component-level input manipulation.\nCombining ISR with semantic verification, adaptive reward weighting that detects gaming signatures, and extending STA to broader logic types are promising directions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex",
    "old_string": "\\section{Discussion and Conclusion}\n\\label{sec:conclusion}\n\\label{sec:discussion}\n\nWe introduced Solver Trace Ablation (STA), a component-level diagnostic for neurosymbolic formalizers that exposes structural degeneration invisible to execution-based evaluation.\nApplied to GRPO-trained models, ISR reveals a collapse trajectory hidden from prove rate, confirmed as RL-specific by an SFT baseline with near-zero hacking (\\S\\ref{sec:diagnostic}).\nWhen repurposed as a training signal, ISR induces meta-level Goodhart's Law: at low dose, the model games the diagnostic itself through conclusion duplication absent under matched controls; at high dose, prove rate collapses; the sole apparent ISR improvement reduces to noise after controlling for a premise-count confound (\\S\\ref{sec:goodhart}).\nBoth the diagnostic utility and the Goodhart vulnerability transfer across formal languages: Prolog ISR-as-reward produces universal gaming across all seeds---each via a distinct mechanism---with zero genuine proofs (\\S\\ref{sec:crosslogic}).\nAcross six reward conditions and two logic types, we catalog seven hacking modes, including query-as-fact gaming that bypasses text-match classifiers (\\S\\ref{sec:taxonomy}).\n\n\\paragraph{Interpreting ISR.}\nISR values must always be read relative to the optimization objective: under exec-only Prolog training, \\emph{low} ISR reflects redundant coding (repeated ground facts) rather than absence of reasoning, while under ISR-as-reward, \\emph{high} ISR reflects metric gaming.\nThe premise-count confound---fewer components mechanically inflate ISR under LOO---applies to any ablation-based diagnostic on variable-length outputs and should be controlled when reporting structural scores.\n\n\\paragraph{Meta-Level Goodhart: Implications.}\nThe meta-Goodhart finding extends beyond this specific system.\nISR was designed to \\emph{detect} reward gaming of $r_{\\text{exec}}$, yet when incorporated into the reward, the model games ISR itself---creating a regress where any diagnostic metric risks becoming a target when optimized.\nThe dose-response pattern ($\\beta{=}0.1$: proxy gaming; $\\beta{=}0.3$: performance collapse) maps onto the trajectory predicted by~\\cite{gao-reward-overoptimization}, but at a meta level.\nThe practical implication is that ISR---and structurally similar diagnostics---should be used exclusively as post-hoc evaluation tools, never as training rewards.\nThe fundamental asymmetry (reliable as observer, unreliable as optimizer) may generalize to other perturbation-based quality metrics in neurosymbolic systems.\n\n\\paragraph{Single-Seed Unreliability.}\nThe three exec-only seeds diverge radically (PR $\\sigma{=}\\pm 47$ percentage points), each converging to a qualitatively different degeneration mode.\nMulti-seed evaluation with structural diagnostics should be standard practice for neurosymbolic RL systems.\n\n\\paragraph{Limitations and Future Work.}\nAll experiments use a single base model (Qwen3-4B) and dataset family (FOLIO); generalization to larger models, different architectures, and diverse reasoning corpora remains untested.\nISR quantifies syntactic component necessity, not semantic faithfulness: a downstream NLI evaluation finds ISR and task accuracy uncorrelated (Spearman $\\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\\ref{app:extended-discussion}).\nThree seeds suffice to demonstrate qualitative divergence but provide limited statistical power for effect-size estimation.\nSTA requires solvers that support component-level input manipulation, limiting applicability to systems with decomposable inputs.\nCombining ISR with semantic verification could yield joint structural-semantic diagnostics; adaptive reward weighting that detects gaming signatures offers a path toward robust shaping; extending STA to broader logic types would test generality.",
    "new_string": "\\section{Discussion and Conclusion}\n\nWe introduced Solver Trace Ablation (STA), a component-level diagnostic for neurosymbolic formalizers that exposes structural degeneration invisible to execution-based evaluation.\nApplied to GRPO-trained models, ISR reveals a collapse trajectory hidden from prove rate, confirmed as RL-specific by an SFT baseline with near-zero hacking (\\S\\ref{sec:diagnostic}).\nWhen repurposed as a training signal, ISR induces meta-level Goodhart's Law: at low dose, the model games the diagnostic itself through conclusion duplication absent under matched controls; at high dose, prove rate collapses; the sole apparent ISR improvement reduces to noise after controlling for a premise-count confound (\\S\\ref{sec:goodhart}).\nBoth diagnostic utility and Goodhart vulnerability transfer to Prolog/SWI-Prolog: ISR-as-reward yields universal gaming across all seeds with zero genuine proofs, each via a distinct mechanism (\\S\\ref{sec:crosslogic}).\nAcross six reward conditions and two logic types, we catalog seven hacking modes, including query-as-fact gaming that bypasses text-match classifiers (\\S\\ref{sec:taxonomy}).\n\n\\paragraph{Interpreting ISR.}\nISR values must always be read relative to the optimization objective: under exec-only Prolog training, \\emph{low} ISR reflects redundant coding (repeated ground facts), not absence of reasoning; under ISR-as-reward, \\emph{high} ISR reflects metric gaming.\nThe premise-count confound---fewer components mechanically inflate ISR under LOO---applies to any ablation-based diagnostic on variable-length outputs.\n\n\\paragraph{Meta-Level Goodhart.}\nISR was designed to \\emph{detect} reward gaming of $r_{\\text{exec}}$, yet incorporating it into the reward causes the model to game ISR itself---a regress where any diagnostic metric risks becoming a target when optimized.\nThe dose-response pattern ($\\beta{=}0.1$: proxy gaming; $\\beta{=}0.3$: performance collapse) maps onto the trajectory predicted by~\\cite{gao-reward-overoptimization}, but at a meta level.\nISR---and structurally similar diagnostics---should be used exclusively as post-hoc evaluation tools, never as training rewards.\nThe fundamental asymmetry (reliable as observer, unreliable as optimizer) may generalize to other perturbation-based quality metrics.\n\n\\paragraph{Limitations.}\nExperiments use a single base model (Qwen3-4B) and dataset family (FOLIO); generalization remains untested.\nISR quantifies syntactic component necessity, not semantic faithfulness: a downstream NLI evaluation finds ISR and task accuracy uncorrelated (Spearman $\\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\\ref{app:extended-discussion}).\nThree seeds demonstrate qualitative divergence but limit statistical power.\nSTA requires solvers supporting component-level input manipulation.\nCombining ISR with semantic verification, adaptive reward weighting that detects gaming signatures, and extending STA to broader logic types are promising directions."
  }
}
```

</details>

---

### Tool result

_source line 109 · 2026-05-14T21:26:49.999360+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 110 · 2026-05-14T21:26:49.999619+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "old_string": "\\textbf{High-dose ISR ($\\beta{=}0.3$): classic Goodhart.}\nAt $\\beta{=}0.3$, ISR causes PR to collapse to 18\\%---a 5.2$\\times$ degradation from exec-only.\nThe matched random control achieves PR${=}48$\\%, a 2.7$\\times$ advantage, demonstrating that ISR at high dose is not merely unhelpful but actively harmful.\nTogether, the two doses reveal a complete Goodhart trajectory~\\citep{karwowski-goodhart-rl, gao-reward-overoptimization}: low-dose proxy gaming (ISR inflation via H7) followed by high-dose performance collapse---but at a meta level, since the proxy being gamed is itself a gaming detector.\nThis dose-response pattern maps onto established Goodhart dynamics but occurs at the \\emph{meta} level: ISR was designed to detect gaming, yet becomes the target of gaming when optimized.\nUnder the taxonomy of \\citet{manheim-goodhart-taxonomy}, $\\beta{=}0.3$ exemplifies extremal Goodhart---the optimizer enters a regime where the proxy-target relationship breaks down entirely---while $\\beta{=}0.1$ instantiates a meta-level variant where the diagnostic is gamed through its own measurement mechanism.",
  "new_string": "\\textbf{High-dose ISR ($\\beta{=}0.3$): classic Goodhart.}\nAt $\\beta{=}0.3$, ISR causes PR to collapse to 18\\%---a 5.2$\\times$ degradation from exec-only---while the matched random control achieves PR${=}48$\\%.\nThe two doses reveal a complete Goodhart trajectory~\\citep{karwowski-goodhart-rl, gao-reward-overoptimization} at the meta level: low-dose proxy gaming (ISR inflation via H7) followed by high-dose performance collapse, with the proxy being gamed itself a gaming detector.\nUnder the taxonomy of \\citet{manheim-goodhart-taxonomy}, $\\beta{=}0.3$ exemplifies extremal Goodhart while $\\beta{=}0.1$ instantiates a meta-level variant."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "old_string": "\\textbf{High-dose ISR ($\\beta{=}0.3$): classic Goodhart.}\nAt $\\beta{=}0.3$, ISR causes PR to collapse to 18\\%---a 5.2$\\times$ degradation from exec-only.\nThe matched random control achieves PR${=}48$\\%, a 2.7$\\times$ advantage, demonstrating that ISR at high dose is not merely unhelpful but actively harmful.\nTogether, the two doses reveal a complete Goodhart trajectory~\\citep{karwowski-goodhart-rl, gao-reward-overoptimization}: low-dose proxy gaming (ISR inflation via H7) followed by high-dose performance collapse---but at a meta level, since the proxy being gamed is itself a gaming detector.\nThis dose-response pattern maps onto established Goodhart dynamics but occurs at the \\emph{meta} level: ISR was designed to detect gaming, yet becomes the target of gaming when optimized.\nUnder the taxonomy of \\citet{manheim-goodhart-taxonomy}, $\\beta{=}0.3$ exemplifies extremal Goodhart---the optimizer enters a regime where the proxy-target relationship breaks down entirely---while $\\beta{=}0.1$ instantiates a meta-level variant where the diagnostic is gamed through its own measurement mechanism.",
    "new_string": "\\textbf{High-dose ISR ($\\beta{=}0.3$): classic Goodhart.}\nAt $\\beta{=}0.3$, ISR causes PR to collapse to 18\\%---a 5.2$\\times$ degradation from exec-only---while the matched random control achieves PR${=}48$\\%.\nThe two doses reveal a complete Goodhart trajectory~\\citep{karwowski-goodhart-rl, gao-reward-overoptimization} at the meta level: low-dose proxy gaming (ISR inflation via H7) followed by high-dose performance collapse, with the proxy being gamed itself a gaming detector.\nUnder the taxonomy of \\citet{manheim-goodhart-taxonomy}, $\\beta{=}0.3$ exemplifies extremal Goodhart while $\\beta{=}0.1$ instantiates a meta-level variant."
  }
}
```

</details>

---

### Tool result

_source line 111 · 2026-05-14T21:26:50.003997+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Edit",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 112 · 2026-05-14T21:26:50.004228+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "old_string": "\\textbf{Low-dose ISR ($\\beta{=}0.1$): ISR-specific gaming.}\nTable~\\ref{tab:goodhart-landscape} summarizes results.\nAt $\\beta{=}0.1$, 2/3 ISR seeds (s43, s44) are dominated by H7---a single premise identical to the conclusion, trivially achieving both high PR and ISR.\nAcross the three ISR seeds, H7 accounts for 64.5\\% of proved samples (149/231); all three random control seeds show \\emph{zero} H7 (0/256).\nH7 is exclusively induced by the ISR reward signal.\nConclusion embedding (H1 or H7) is GRPO-universal at 68--97\\% across all RL conditions. Under random, it manifests exclusively as H1 (70.9--93.2\\%); under ISR, H1 drops to 0--51.9\\% but H7 rises to 16--97\\%, yielding comparable total rates (per-seed: Appendix Table~\\ref{tab:beta01-3seed}). ISR reward does not reduce total hacking---it \\emph{converts} H1 into the more extreme H7 (Figure~\\ref{fig:hacking-composition}).\nPooled conclusion-in-premise rates are comparable (ISR s42: 67.9\\% vs Random s42: 70.9\\%), and random achieves higher and more stable PR (85$\\pm$6\\% vs 77$\\pm$14\\%).",
  "new_string": "\\textbf{Low-dose ISR ($\\beta{=}0.1$): ISR-specific gaming.}\nTable~\\ref{tab:goodhart-landscape} summarizes results.\nAt $\\beta{=}0.1$, 2/3 ISR seeds (s43, s44) are dominated by H7---a single premise identical to the conclusion, trivially achieving both high PR and ISR.\nAcross the three ISR seeds, H7 accounts for 64.5\\% of proved samples (149/231); all three random controls show \\emph{zero} H7 (0/256), confirming H7 is exclusively induced by the ISR signal.\nConclusion embedding (H1+H7) is GRPO-universal at 68--97\\% across RL conditions: random produces only H1 (70.9--93.2\\%), while ISR converts H1$\\to$H7 without reducing the total (Figure~\\ref{fig:hacking-composition}; per-seed: Appendix Table~\\ref{tab:beta01-3seed}).\nRandom also achieves higher and more stable PR (85$\\pm$6\\% vs 77$\\pm$14\\%)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "old_string": "\\textbf{Low-dose ISR ($\\beta{=}0.1$): ISR-specific gaming.}\nTable~\\ref{tab:goodhart-landscape} summarizes results.\nAt $\\beta{=}0.1$, 2/3 ISR seeds (s43, s44) are dominated by H7---a single premise identical to the conclusion, trivially achieving both high PR and ISR.\nAcross the three ISR seeds, H7 accounts for 64.5\\% of proved samples (149/231); all three random control seeds show \\emph{zero} H7 (0/256).\nH7 is exclusively induced by the ISR reward signal.\nConclusion embedding (H1 or H7) is GRPO-universal at 68--97\\% across all RL conditions. Under random, it manifests exclusively as H1 (70.9--93.2\\%); under ISR, H1 drops to 0--51.9\\% but H7 rises to 16--97\\%, yielding comparable total rates (per-seed: Appendix Table~\\ref{tab:beta01-3seed}). ISR reward does not reduce total hacking---it \\emph{converts} H1 into the more extreme H7 (Figure~\\ref{fig:hacking-composition}).\nPooled conclusion-in-premise rates are comparable (ISR s42: 67.9\\% vs Random s42: 70.9\\%), and random achieves higher and more stable PR (85$\\pm$6\\% vs 77$\\pm$14\\%).",
    "new_string": "\\textbf{Low-dose ISR ($\\beta{=}0.1$): ISR-specific gaming.}\nTable~\\ref{tab:goodhart-landscape} summarizes results.\nAt $\\beta{=}0.1$, 2/3 ISR seeds (s43, s44) are dominated by H7---a single premise identical to the conclusion, trivially achieving both high PR and ISR.\nAcross the three ISR seeds, H7 accounts for 64.5\\% of proved samples (149/231); all three random controls show \\emph{zero} H7 (0/256), confirming H7 is exclusively induced by the ISR signal.\nConclusion embedding (H1+H7) is GRPO-universal at 68--97\\% across RL conditions: random produces only H1 (70.9--93.2\\%), while ISR converts H1$\\to$H7 without reducing the total (Figure~\\ref{fig:hacking-composition}; per-seed: Appendix Table~\\ref{tab:beta01-3seed}).\nRandom also achieves higher and more stable PR (85$\\pm$6\\% vs 77$\\pm$14\\%)."
  }
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-14T21:26:50.004522+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 114 · 2026-05-14T21:26:50.004748+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "old_string": "We replicated both experiments using SWI-Prolog 8.4.2 (full results in Appendix Table~\\ref{tab:prolog-crosslogic}).\nTwo of three Prolog exec-only seeds yield proved-only ISR near zero (s42${=}0.037$, s43${=}0.015$), confirming diagnostic transfer despite moderate-to-high PR; here low ISR reflects \\emph{redundant coding}---repeated ground facts where removing any single copy leaves the proof intact---rather than absence of reasoning, contrasting with the metric-gaming high ISR under Prolog STA reward.\nWith ISR added as a Prolog reward, all three STA seeds converge to gaming with 0\\% genuine across 185 proved samples (universal Goodhart, stronger than the FOL ${\\sim}16$\\% genuine residual): s42 produces clean H7 tautologies (50/50, ISR$^*{=}1.000$); s43 generates uppercase pseudo-Prolog that bypasses text-match classifiers but is functionally H7 ($n_{\\text{nec}}{=}1$ for 38/38); s44 develops query-as-fact gaming where NL is converted to snake\\_case atoms used as both fact and query (ISR$^*{=}0.912$, $n_{\\text{nec}}{=}1$ for 95/97).\nSimpler formal semantics enable more complete exploitation, and the bypass of text-match classifiers by query-as-fact gaming motivates functional cross-validation of automated diagnostics.\nThe diversity of gaming pathways across seeds---despite identical training data and reward function---demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.",
  "new_string": "We replicated both experiments using SWI-Prolog 8.4.2 (full results in Appendix Table~\\ref{tab:prolog-crosslogic}).\nTwo of three Prolog exec-only seeds yield proved-only ISR near zero (s42${=}0.037$, s43${=}0.015$), confirming diagnostic transfer despite moderate-to-high PR; low ISR here reflects \\emph{redundant coding} (repeated ground facts where removing one leaves the proof intact), not absence of reasoning---contrasting with the metric-gaming high ISR under Prolog STA reward.\nWith ISR added as a Prolog reward, all three STA seeds converge to gaming with 0\\% genuine across 185 proved samples (universal Goodhart, stronger than the FOL ${\\sim}16$\\% residual): s42 produces clean H7 tautologies (ISR$^*{=}1.000$); s43 generates uppercase pseudo-Prolog functionally equivalent to H7 ($n_{\\text{nec}}{=}1$ for 38/38); s44 develops query-as-fact gaming, converting NL to snake\\_case atoms used as both fact and query (ISR$^*{=}0.912$, $n_{\\text{nec}}{=}1$ for 95/97).\nThe diversity of gaming pathways across seeds---despite identical training data and reward---shows that Goodhart's Law here is not a single failure mode but a family of convergent exploits, and that bypass of text classifiers by query-as-fact gaming motivates functional cross-validation of automated diagnostics."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "old_string": "We replicated both experiments using SWI-Prolog 8.4.2 (full results in Appendix Table~\\ref{tab:prolog-crosslogic}).\nTwo of three Prolog exec-only seeds yield proved-only ISR near zero (s42${=}0.037$, s43${=}0.015$), confirming diagnostic transfer despite moderate-to-high PR; here low ISR reflects \\emph{redundant coding}---repeated ground facts where removing any single copy leaves the proof intact---rather than absence of reasoning, contrasting with the metric-gaming high ISR under Prolog STA reward.\nWith ISR added as a Prolog reward, all three STA seeds converge to gaming with 0\\% genuine across 185 proved samples (universal Goodhart, stronger than the FOL ${\\sim}16$\\% genuine residual): s42 produces clean H7 tautologies (50/50, ISR$^*{=}1.000$); s43 generates uppercase pseudo-Prolog that bypasses text-match classifiers but is functionally H7 ($n_{\\text{nec}}{=}1$ for 38/38); s44 develops query-as-fact gaming where NL is converted to snake\\_case atoms used as both fact and query (ISR$^*{=}0.912$, $n_{\\text{nec}}{=}1$ for 95/97).\nSimpler formal semantics enable more complete exploitation, and the bypass of text-match classifiers by query-as-fact gaming motivates functional cross-validation of automated diagnostics.\nThe diversity of gaming pathways across seeds---despite identical training data and reward function---demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.",
    "new_string": "We replicated both experiments using SWI-Prolog 8.4.2 (full results in Appendix Table~\\ref{tab:prolog-crosslogic}).\nTwo of three Prolog exec-only seeds yield proved-only ISR near zero (s42${=}0.037$, s43${=}0.015$), confirming diagnostic transfer despite moderate-to-high PR; low ISR here reflects \\emph{redundant coding} (repeated ground facts where removing one leaves the proof intact), not absence of reasoning---contrasting with the metric-gaming high ISR under Prolog STA reward.\nWith ISR added as a Prolog reward, all three STA seeds converge to gaming with 0\\% genuine across 185 proved samples (universal Goodhart, stronger than the FOL ${\\sim}16$\\% residual): s42 produces clean H7 tautologies (ISR$^*{=}1.000$); s43 generates uppercase pseudo-Prolog functionally equivalent to H7 ($n_{\\text{nec}}{=}1$ for 38/38); s44 develops query-as-fact gaming, converting NL to snake\\_case atoms used as both fact and query (ISR$^*{=}0.912$, $n_{\\text{nec}}{=}1$ for 95/97).\nThe diversity of gaming pathways across seeds---despite identical training data and reward---shows that Goodhart's Law here is not a single failure mode but a family of convergent exploits, and that bypass of text classifiers by query-as-fact gaming motivates functional cross-validation of automated diagnostics."
  }
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-14T21:26:50.005068+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compress-to-8pages_20260514T211717",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---
