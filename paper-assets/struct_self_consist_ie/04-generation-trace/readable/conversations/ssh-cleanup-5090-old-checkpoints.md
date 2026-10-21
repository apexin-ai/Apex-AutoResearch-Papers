# ssh cleanup 5090 old checkpoints

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_ssh_cleanup-5090-old-checkpoints_20260520T070723.jsonl`
- **Structured JSON:** [`5bc105ef46b81897924f.json`](../../sessions/5b/5bc105ef46b81897924f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-20T07:09:05.852977+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_cleanup-5090-old-checkpoints_20260520T070723",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T07:09:05.853342+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_cleanup-5090-old-checkpoints_20260520T070723",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T07:09:05.853509+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "hostname",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_cleanup-5090-old-checkpoints_20260520T070723",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "hostname",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T07:09:05.853649+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'hostname' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_cleanup-5090-old-checkpoints_20260520T070723",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T07:09:05.853775+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "hostname",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_cleanup-5090-old-checkpoints_20260520T070723",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "hostname",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T07:09:05.853901+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"autodl-container-31eb41bf76-61568de9\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.98}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_cleanup-5090-old-checkpoints_20260520T070723",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T07:09:05.854058+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -lhd /root/autodl-tmp/struct_self_consist_ie/checkpoints/*wnut17* /root/autodl-tmp/struct_self_consist_ie/checkpoints/*4b-conll* /root/autodl-tmp/struct_self_consist_ie/checkpoints/*scierc-v2* /root/autodl-tmp/struct_self_consist_ie/checkpoints/*llama* /root/autodl-tmp/struct_self_consist_ie/checkpoints/*smoke*",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_cleanup-5090-old-checkpoints_20260520T070723",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -lhd /root/autodl-tmp/struct_self_consist_ie/checkpoints/*wnut17* /root/autodl-tmp/struct_self_consist_ie/checkpoints/*4b-conll* /root/autodl-tmp/struct_self_consist_ie/checkpoints/*scierc-v2* /root/autodl-tmp/struct_self_consist_ie/checkpoints/*llama* /root/autodl-tmp/struct_self_consist_ie/checkpoints/*smoke*",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T07:09:05.854221+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"drwxr-xr-x 5 root root 4.0K May 17 00:25 /root/autodl-tmp/struct_self_consist_ie/checkpoints/ft_fewnerd_smoke\\ndrwxr-xr-x 5 root root 4.0K May 19 09:02 /root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-fewnerd-lora\\ndrwxr-xr-x 5 root root 4.0K May 14 21:08 /root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-scierc-lora\\n-rw-r--r-- 1 root root  32K May 18 16:36 /root/autodl-tmp/struct_self_consist_ie/checkpoints/llama_fewnerd_train.log\\n-rw-r--r-- 1 root root  64K May 18 16:38 /root/autodl-tmp/struct_self_consist_ie/checkpoints/llama_fewnerd_train_4gpu.log\\ndrwxr-xr-x 7 root root 4.0K May 16 03:35 /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-4b-conll2003-lora\\ndrwxr-xr-x 7 root root 4.0K May 14 23:59 /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-wnut17-lora\\n-rw-r--r-- 1 root root  27K May 14 20:11 /root/autodl-tmp/struct_self_consist_ie/checkpoints/wnut17_train.log\\n\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/struct_self_consist_ie/checkpoints/*scierc-v2*': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_cleanup-5090-old-checkpoints_20260520T070723",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T07:09:05.854369+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "du -sh /root/autodl-tmp/struct_self_consist_ie/checkpoints/*wnut17* /root/autodl-tmp/struct_self_consist_ie/checkpoints/*4b-conll* /root/autodl-tmp/struct_self_consist_ie/checkpoints/*scierc-v2* /root/autodl-tmp/struct_self_consist_ie/checkpoints/*llama* /root/autodl-tmp/struct_self_consist_ie/checkpoints/*smoke*",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_cleanup-5090-old-checkpoints_20260520T070723",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "du -sh /root/autodl-tmp/struct_self_consist_ie/checkpoints/*wnut17* /root/autodl-tmp/struct_self_consist_ie/checkpoints/*4b-conll* /root/autodl-tmp/struct_self_consist_ie/checkpoints/*scierc-v2* /root/autodl-tmp/struct_self_consist_ie/checkpoints/*llama* /root/autodl-tmp/struct_self_consist_ie/checkpoints/*smoke*",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T07:09:05.854494+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "df -h /root/autodl-tmp/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_cleanup-5090-old-checkpoints_20260520T070723",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "df -h /root/autodl-tmp/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-20T07:09:05.854655+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"5.3G\\t/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-wnut17-lora\\n28K\\t/root/autodl-tmp/struct_self_consist_ie/checkpoints/wnut17_train.log\\n4.1G\\t/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-4b-conll2003-lora\\n3.2G\\t/root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-fewnerd-lora\\n3.2G\\t/root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-scierc-lora\\n32K\\t/root/autodl-tmp/struct_self_consist_ie/checkpoints/llama_fewnerd_train.log\\n64K\\t/root/autodl-tmp/struct_self_consist_ie/checkpoints/llama_fewnerd_train_4gpu.log\\n1.7G\\t/root/autodl-tmp/struct_self_consist_ie/checkpoints/ft_fewnerd_smoke\\n\", \"stderr\": \"du: cannot access '/root/autodl-tmp/struct_self_consist_ie/checkpoints/*scierc-v2*': No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_cleanup-5090-old-checkpoints_20260520T070723",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T07:09:05.854813+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Filesystem      Size  Used Avail Use% Mounted on\\n/dev/md0        250G  172G   79G  69% /root/autodl-tmp\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_cleanup-5090-old-checkpoints_20260520T070723",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T07:09:05.854957+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/checkpoints/ -maxdepth 1 -type d -name \"*wnut17*\" -o -name \"*4b-conll*\" -o -name \"*scierc*\" -o -name \"*llama*\" -o -name \"*smoke*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_cleanup-5090-old-checkpoints_20260520T070723",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/checkpoints/ -maxdepth 1 -type d -name \"*wnut17*\" -o -name \"*4b-conll*\" -o -name \"*scierc*\" -o -name \"*llama*\" -o -name \"*smoke*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T07:09:05.855095+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora-v2\\n/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-wnut17-lora\\n/root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-scierc-lora\\n/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-4b-conll2003-lora\\n/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-4b-scierc-lora\\n/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora-rank8\\n/root/autodl-tmp/struct_self_consist_ie/checkpoints/ft_fewnerd_smoke\\n/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-10epoch-lora\\n/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-3epoch-lora\\n/root/autodl-tmp/struct_self_consist_ie/checkpoints/llama_fewnerd_train.log\\n/root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-fewnerd-lora\\n/root/autodl-tmp/struct_self_consist_ie/checkpoints/llama_fewnerd_train_4gpu.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_cleanup-5090-old-checkpoints_20260520T070723",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T07:09:05.855335+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "du -sh /root/autodl-tmp/struct_self_consist_ie/checkpoints/*scierc*",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_cleanup-5090-old-checkpoints_20260520T070723",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "du -sh /root/autodl-tmp/struct_self_consist_ie/checkpoints/*scierc*",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T07:09:05.855483+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"3.2G\\t/root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-scierc-lora\\n2.6G\\t/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-4b-scierc-lora\\n1.4G\\t/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-10epoch-lora\\n1.4G\\t/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-3epoch-lora\\n895M\\t/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora-rank8\\n3.4G\\t/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora-v2\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.68}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_cleanup-5090-old-checkpoints_20260520T070723",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T07:09:05.855660+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/struct_self_consist_ie/checkpoints/ && for dir in *wnut17* *4b-conll* *scierc-v2* *llama* *smoke*; do if [ -d \"$dir\" ]; then echo \"Deleting: $dir ($(du -sh \"$dir\" | cut -f1))\"; rm -rf \"$dir\"; echo \"  -> Deleted\"; else echo \"SKIP: $dir (not a directory or not found)\"; fi; done",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_cleanup-5090-old-checkpoints_20260520T070723",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/struct_self_consist_ie/checkpoints/ && for dir in *wnut17* *4b-conll* *scierc-v2* *llama* *smoke*; do if [ -d \"$dir\" ]; then echo \"Deleting: $dir ($(du -sh \"$dir\" | cut -f1))\"; rm -rf \"$dir\"; echo \"  -> Deleted\"; else echo \"SKIP: $dir (not a directory or not found)\"; fi; done",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T07:09:05.855800+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Deleting: qwen3-8b-wnut17-lora (5.3G)\\n  -> Deleted\\nSKIP: wnut17_train.log (not a directory or not found)\\nDeleting: qwen3-4b-conll2003-lora (4.1G)\\n  -> Deleted\\nSKIP: *scierc-v2* (not a directory or not found)\\nDeleting: llama3.1-8b-fewnerd-lora (3.2G)\\n  -> Deleted\\nDeleting: llama3.1-8b-scierc-lora (3.2G)\\n  -> Deleted\\nSKIP: llama_fewnerd_train.log (not a directory or not found)\\nSKIP: llama_fewnerd_train_4gpu.log (not a directory or not found)\\nDeleting: ft_fewnerd_smoke (1.7G)\\n  -> Deleted\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_cleanup-5090-old-checkpoints_20260520T070723",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T07:09:05.855941+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "df -h /root/autodl-tmp/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_cleanup-5090-old-checkpoints_20260520T070723",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "df -h /root/autodl-tmp/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T07:09:05.856067+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Filesystem      Size  Used Avail Use% Mounted on\\n/dev/md0        250G  154G   97G  62% /root/autodl-tmp\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_cleanup-5090-old-checkpoints_20260520T070723",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T07:09:05.856218+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -lhd /root/autodl-tmp/struct_self_consist_ie/checkpoints/*/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_cleanup-5090-old-checkpoints_20260520T070723",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -lhd /root/autodl-tmp/struct_self_consist_ie/checkpoints/*/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T07:09:05.856354+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"drwxr-xr-x 5 root root  123 May 20 14:54 /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-32b-fewnerd-qlora-s42/\\ndrwxr-xr-x 5 root root 4.0K May 16 03:47 /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-4b-scierc-lora/\\ndrwxr-xr-x 4 root root   91 May 14 20:04 /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll2003-lora/\\ndrwxr-xr-x 5 root root 4.0K May 18 04:04 /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-5epoch-lora/\\ndrwxr-xr-x 3 root root 4.0K May 18 10:35 /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-10epoch-lora/\\ndrwxr-xr-x 3 root root 4.0K May 18 09:54 /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-3epoch-lora/\\ndrwxr-xr-x 5 root root 4.0K May 16 18:58 /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora-rank8/\\ndrwxr-xr-x 5 root root 4.0K May 14 16:39 /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora-v2/\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.64}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_cleanup-5090-old-checkpoints_20260520T070723",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-20T07:09:05.856522+00:00_

## 清理结果

**已删除（5 个目录，~17.5G）：**

| 目录 | 大小 |
|------|------|
| qwen3-8b-wnut17-lora | 5.3G |
| qwen3-4b-conll2003-lora | 4.1G |
| llama3.1-8b-fewnerd-lora | 3.2G |
| llama3.1-8b-scierc-lora | 3.2G |
| ft_fewnerd_smoke | 1.7G |

**磁盘空间对比：**
- 删除前：79G 可用 (69% used)
- 删除后：**97G 可用 (62% used)**
- 释放：~18G

**剩余 checkpoints（8 个）：**
- qwen25-32b-fewnerd-qlora-s42
- qwen3-4b-scierc-lora
- qwen3-8b-conll2003-lora
- qwen3-8b-fewnerd-5epoch-lora
- qwen3-8b-scierc-10epoch-lora
- qwen3-8b-scierc-3epoch-lora
- qwen3-8b-scierc-lora-rank8
- qwen3-8b-scierc-lora-v2

**注意：可用空间 97G < 100G 目标。** `*scierc-v2*` glob 未匹配任何目录（`qwen3-8b-scierc-lora-v2` 的子串是 "scierc-lora-v2" 而非 "scierc-v2"）。如果也需要删除该目录（3.4G），删后可达 ~100G。另外还有 2 个 llama log 文件（共 96K）未删除（非目录，被脚本跳过）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ssh_cleanup-5090-old-checkpoints_20260520T070723"
}
```

</details>

---
