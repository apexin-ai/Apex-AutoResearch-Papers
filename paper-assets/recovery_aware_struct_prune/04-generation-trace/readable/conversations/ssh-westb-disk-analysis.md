# ssh westb disk analysis

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 0
- **Tool calls:** 25
- **Original source:** `logs/chats/worker_ssh_westb_disk_analysis_20260523T122458.jsonl`
- **Structured JSON:** [`6ad64873930cfa05e985.json`](../../sessions/6a/6ad64873930cfa05e985.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

51 recorded events

### Tool call

_source line 1 · 2026-05-23T12:26:43.590020+00:00_

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
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
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

_source line 2 · 2026-05-23T12:26:43.590351+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T12:26:43.590525+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "df -h /root/autodl-tmp",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "df -h /root/autodl-tmp",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-23T12:26:43.590663+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "du -h --max-depth=2 /root/autodl-tmp/ 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "du -h --max-depth=2 /root/autodl-tmp/ 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-23T12:26:43.590800+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Filesystem      Size  Used Avail Use% Mounted on\\n/dev/md0        250G  241G  9.2G  97% /root/autodl-tmp\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.77}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T12:26:43.590928+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T12:26:43.591051+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "find /root/autodl-tmp/ -size +1G -exec ls -lh {} \\; 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "find /root/autodl-tmp/ -size +1G -exec ls -lh {} \\; 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T12:26:43.591175+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T12:26:43.591314+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "ls -la /root/autodl-tmp/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "ls -la /root/autodl-tmp/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T12:26:43.591454+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 12\\ndrwxr-xr-x  9 root root  160 May 22 06:41 .\\ndrwx------  1 root root 4096 May 21 05:02 ..\\ndrwxr-xr-x  2 root root   75 May 23 20:25 .autodl\\ndrwxr-xr-x  6 root root  120 May 14 23:26 .hf_cache\\ndrwxr-xr-x  3 root root   27 May 14 10:52 .ms_cache\\ndrwxr-xr-x  4 root root   48 May 12 18:20 data\\ndrwxr-xr-x  2 root root 4096 May 14 09:55 logs\\ndrwxr-xr-x  3 root root   37 May 20 12:26 models\\ndrwxr-xr-x 35 root root 4096 May 23 10:56 recovery_aware_struct_prune\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.75}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T12:26:43.591608+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "du -h --max-depth=2 /root/autodl-tmp/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "du -h --max-depth=2 /root/autodl-tmp/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-23T12:26:43.591732+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "find /root/autodl-tmp/ -size +1G -ls 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "find /root/autodl-tmp/ -size +1G -ls 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-23T12:26:43.591896+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"4.7M\\t/root/autodl-tmp/.autodl\\n15G\\t/root/autodl-tmp/models/Qwen2.5-Math-7B\\n15G\\t/root/autodl-tmp/models\\n1.4G\\t/root/autodl-tmp/data/scierc\\n2.2M\\t/root/autodl-tmp/data/crossner\\n1.5G\\t/root/autodl-tmp/data\\n64M\\t/root/autodl-tmp/logs\\n0\\t/root/autodl-tmp/.ms_cache/.lock\\n0\\t/root/autodl-tmp/.ms_cache\\n4.0K\\t/root/autodl-tmp/.hf_cache/models--deepseek-ai--DeepSeek-R1-Distill-Qwen-7B\\n2.7M\\t/root/autodl-tmp/.hf_cache/hub\\n44M\\t/root/autodl-tmp/.hf_cache/datasets\\n28K\\t/root/autodl-tmp/.hf_cache/xet\\n46M\\t/root/autodl-tmp/.hf_cache\\n3.4G\\t/root/autodl-tmp/recovery_aware_struct_prune/models\\n26M\\t/root/autodl-tmp/recovery_aware_struct_prune/results\\n21M\\t/root/autodl-tmp/recovery_aware_struct_prune/logs\\n8.0K\\t/root/autodl-tmp/recovery_aware_struct_prune/eval_results\\n12G\\t/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20\\n280K\\t/root/autodl-tmp/recovery_aware_struct_prune/wandb\\n0\\t/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456\\n11G\\t/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25\\n12G\\t/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_rlvr_20\\n12G\\t/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_rlvr_20\\n8.0K\\t/root/autodl-tmp/recovery_aware_struct_prune/artifacts\\n12G\\t/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\\n12G\\t/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20\\n2.8G\\t/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_20_1p5b\\n2.8G\\t/root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_20_1p5b\\n2.8G\\t/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_20_1p5b\\n2.8G\\t/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b\\n2.8G\\t/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\\n2.8G\\t/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b\\n2.8G\\t/root/autodl-tmp/recovery_aware_struct_prune/grpo_ck
…[truncated 1218 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T12:26:43.592041+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T12:26:43.592226+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "find /root/autodl-tmp/ -size +1G -name \"*.pt\" -ls",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "find /root/autodl-tmp/ -size +1G -name \"*.pt\" -ls",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-23T12:26:43.592405+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "find /root/autodl-tmp/ -size +1G -name \"*.safetensors\" -ls",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "find /root/autodl-tmp/ -size +1G -name \"*.safetensors\" -ls",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-23T12:26:43.592548+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.75}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-23T12:26:43.592671+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "find /root/autodl-tmp/ -size +1G -name \"*.bin\" -ls",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "find /root/autodl-tmp/ -size +1G -name \"*.bin\" -ls",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-23T12:26:43.592839+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"20436620917 3774148 -rw-r--r--   1 root     root     3864726424 May 20 12:36 /root/autodl-tmp/models/Qwen2.5-Math-7B/model-00003-of-00004.safetensors\\n20436620918 3473028 -rw-r--r--   1 root     root     3556377672 May 20 12:40 /root/autodl-tmp/models/Qwen2.5-Math-7B/model-00004-of-00004.safetensors\\n20436620915 3852972 -rw-r--r--   1 root     root     3945441440 May 20 12:40 /root/autodl-tmp/models/Qwen2.5-Math-7B/model-00001-of-00004.safetensors\\n20436620916 3774148 -rw-r--r--   1 root     root     3864726352 May 20 12:41 /root/autodl-tmp/models/Qwen2.5-Math-7B/model-00002-of-00004.safetensors\\n18307973760 3470916 -rw-r--r--   1 root     root     3554214621 May 18 18:40 /root/autodl-tmp/recovery_aware_struct_prune/models/DeepSeek-R1-Distill-Qwen-1.5B/model.safetensors\\n19330958605 11889292 -rw-r--r--   1 root     root     12174631264 May 22 20:22 /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20/model.safetensors\\n23626073987 11311096 -rw-r--r--   1 root     root     11582559224 May 16 12:54 /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25/model.safetensors\\n19349735044 12035092 -rw-r--r--   1 root     root     12323931184 May 16 17:53 /root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_rlvr_20/model.safetensors\\n 2159714119 12035092 -rw-r--r--   1 root     root     12323931184 May 16 22:19 /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_rlvr_20/checkpoint-1870/model.safetensors\\n18299039841 12035092 -rw-r--r--   1 root     root     12323931248 May 17 22:23 /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20/model.safetensors\\n30090014992 12035092 -rw-r--r--   1 root     root     12323931248 May 18 10:14 /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100/model.safetensors\\n15064413748  2859940 -rw-r--r--   1 root     root      2928577360 May 18 19:11 /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_20_1p5b/model.safet
…[truncated 3542 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T12:26:43.592990+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T12:26:43.593148+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "ls -la /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_rlvr_20/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "ls -la /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_rlvr_20/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-23T12:26:43.593301+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 8\\ndrwxr-xr-x  3 root root   58 May 16 22:51 .\\ndrwxr-xr-x 35 root root 4096 May 23 10:56 ..\\n-rw-r--r--  1 root root 1329 May 16 22:19 README.md\\ndrwxr-xr-x  2 root root  186 May 19 00:35 checkpoint-1870\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.77}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T12:26:43.593437+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "ls -la /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "ls -la /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-23T12:26:43.593561+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "ls -la /root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "ls -la /root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-23T12:26:43.593691+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 11192\\ndrwxr-xr-x  4 root root     4096 May 19 00:35 .\\ndrwxr-xr-x 35 root root     4096 May 23 10:56 ..\\n-rw-r--r--  1 root root     2092 May 18 10:14 README.md\\n-rw-r--r--  1 root root     2246 May 18 10:15 chat_template.jinja\\ndrwxr-xr-x  2 root root     4096 May 19 00:35 checkpoint-100\\ndrwxr-xr-x  2 root root     4096 May 18 10:14 completions\\n-rw-r--r--  1 root root     1732 May 18 10:14 config.json\\n-rw-r--r--  1 root root      241 May 18 10:14 generation_config.json\\n-rw-r--r--  1 root root 11421907 May 18 10:15 tokenizer.json\\n-rw-r--r--  1 root root      420 May 18 10:15 tokenizer_config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.79}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-23T12:26:43.593824+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 12060488\\ndrwxr-xr-x  4 root root        4096 May 22 17:40 .\\ndrwxr-xr-x 35 root root        4096 May 23 10:56 ..\\n-rw-r--r--  1 root root        2112 May 22 17:40 README.md\\n-rw-r--r--  1 root root        2513 May 22 17:40 chat_template.jinja\\ndrwxr-xr-x  2 root root        4096 May 22 22:27 checkpoint-100\\ndrwxr-xr-x  2 root root        4096 May 22 17:40 completions\\n-rw-r--r--  1 root root        1727 May 22 17:40 config.json\\n-rw-r--r--  1 root root         215 May 22 17:40 generation_config.json\\n-rw-r--r--  1 root root 12338467960 May 22 17:40 model.safetensors\\n-rw-r--r--  1 root root    11421892 May 22 17:40 tokenizer.json\\n-rw-r--r--  1 root root         695 May 22 17:40 tokenizer_config.json\\n-rw-r--r--  1 root root        7313 May 22 17:40 training_args.bin\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.87}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-23T12:26:43.593948+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "ls -la /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha0p5_20/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "ls -la /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha0p5_20/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-23T12:26:43.594077+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 12032084\\ndrwxr-xr-x  4 root root        4096 May 23 10:58 .\\ndrwxr-xr-x 35 root root        4096 May 23 10:56 ..\\n-rw-r--r--  1 root root        2102 May 23 10:57 README.md\\n-rw-r--r--  1 root root        2246 May 23 10:58 chat_template.jinja\\ndrwxr-xr-x  2 root root        4096 May 23 10:57 checkpoint-100\\ndrwxr-xr-x  2 root root          10 May 23 10:57 completions\\n-rw-r--r--  1 root root        1732 May 23 10:57 config.json\\n-rw-r--r--  1 root root         240 May 23 10:57 generation_config.json\\n-rw-r--r--  1 root root 12309394504 May 23 10:58 model.safetensors\\n-rw-r--r--  1 root root    11421907 May 23 10:58 tokenizer.json\\n-rw-r--r--  1 root root         419 May 23 10:58 tokenizer_config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.87}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-23T12:26:43.594208+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "ls -la /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha3p0_20/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "ls -la /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha3p0_20/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-23T12:26:43.594357+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 12\\ndrwxr-xr-x  3 root root   57 May 22 16:08 .\\ndrwxr-xr-x 35 root root 4096 May 23 10:56 ..\\n-rw-r--r--  1 root root 1337 May 22 16:08 README.md\\ndrwxr-xr-x  2 root root 4096 May 22 17:10 checkpoint-935\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.83}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-23T12:26:43.594477+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "ls -la /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_1p5b/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "ls -la /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_1p5b/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-23T12:26:43.594596+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "ls -la /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_20_1p5b/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "ls -la /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_20_1p5b/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-23T12:26:43.594719+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 24\\ndrwxr-xr-x  4 root root  137 May 19 00:08 .\\ndrwxr-xr-x 35 root root 4096 May 23 10:56 ..\\n-rw-r--r--  1 root root 2102 May 19 00:05 README.md\\ndrwxr-xr-x  2 root root 4096 May 19 00:08 checkpoint-100\\ndrwxr-xr-x  2 root root 4096 May 19 00:05 completions\\n-rw-r--r--  1 root root 1714 May 19 00:05 config.json\\n-rw-r--r--  1 root root  241 May 19 00:05 generation_config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.79}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-23T12:26:43.594843+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 12\\ndrwxr-xr-x  4 root root   80 May 19 00:09 .\\ndrwxr-xr-x 35 root root 4096 May 23 10:56 ..\\n-rw-r--r--  1 root root 2094 May 19 00:09 README.md\\ndrwxr-xr-x  2 root root  186 May 19 00:35 checkpoint-100\\ndrwxr-xr-x  2 root root 4096 May 19 00:09 completions\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.89}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-23T12:26:43.594967+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "du -h --max-depth=1 /root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "du -h --max-depth=1 /root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-23T12:26:43.595092+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"144K\\t/root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20/completions\\n12G\\t/root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20/checkpoint-100\\n24G\\t/root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20/\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.89}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-23T12:26:43.595210+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "du -h --max-depth=1 /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha0p5_20/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "du -h --max-depth=1 /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha0p5_20/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-23T12:26:43.595354+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"12G\\t/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha0p5_20/checkpoint-100\\n0\\t/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha0p5_20/completions\\n23G\\t/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha0p5_20/\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.75}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-23T12:26:43.595473+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "du -h --max-depth=1 /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_rlvr_20/checkpoint-1870/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "du -h --max-depth=1 /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_rlvr_20/checkpoint-1870/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-23T12:26:43.595590+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "du -h --max-depth=1 /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "du -h --max-depth=1 /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-23T12:26:43.595707+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"12G\\t/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_rlvr_20/checkpoint-1870/\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.76}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-23T12:26:43.595823+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"12G\\t/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100/\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.89}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-23T12:26:43.595944+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "du -h --max-depth=1 /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha3p0_20/checkpoint-935/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "du -h --max-depth=1 /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha3p0_20/checkpoint-935/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-23T12:26:43.596061+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "ls /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha0p5_20/checkpoint-100/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "ls /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha0p5_20/checkpoint-100/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-23T12:26:43.596180+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"12G\\t/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha3p0_20/checkpoint-935/\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.75}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-23T12:26:43.596313+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "ls /root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20/checkpoint-100/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "ls /root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20/checkpoint-100/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-23T12:26:43.596440+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"chat_template.jinja\\nconfig.json\\ngeneration_config.json\\nmodel.safetensors\\nscheduler.pt\\ntokenizer.json\\ntokenizer_config.json\\ntrainer_state.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-23T12:26:43.596558+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "ls /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "ls /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-23T12:26:43.596679+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"chat_template.jinja\\nconfig.json\\ngeneration_config.json\\nmodel.safetensors\\nrng_state.pth\\nscheduler.pt\\ntokenizer.json\\ntokenizer_config.json\\ntrainer_state.json\\ntraining_args.bin\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-23T12:26:43.596797+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"README.md\\ncompletions\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-23T12:26:43.596995+00:00_

分析完成。

```
总磁盘：250G，已用 241G，剩余 9.2G (97%)

=== 占用分布 ===
recovery_aware_struct_prune/     226G  (94%)
models/Qwen2.5-Math-7B           15G  (6%)
data/                            1.5G
其他 (.hf_cache/logs/etc.)       <1G

=== 清理方案 ===

【可删 — 中间 checkpoint 副本（final model 已存在）】~24G
1. grpo_qwen_math_cka_only_20/checkpoint-100/  — 12G
   已有顶层 model.safetensors，checkpoint-100 是冗余副本（含 scheduler.pt/rng_state.pth 等训练恢复文件）
2. grpo_rasp_alpha0p5_20/checkpoint-100/        — 12G
   同上，顶层已有 final model.safetensors

【可删 — 空目录】~0
3. grpo_random_20_seed456/   — 0 (空目录)
4. grpo_rasp_alpha3p0_20/    — 132K (仅 README + completions，无模型文件，疑似失败/未完成的 run)

可释放空间：~24G（97% → 87%）

=== 需确认 ===
5. models/Qwen2.5-Math-7B                 — 15G  — Qwen Math base model，如果 Qwen Math 实验已完成且不再需要 base model，可删
6. pruned_standard_25/                     — 11G  — 25% 剪枝率实验，其他实验均为 20%，确认是否仍需要
7. pruned_rasp_rlvr_20/ + sft_rasp_rlvr_20/ — 24G — 早期 RLVR 方案实验，如已被 alpha 系列取代可删
8. grpo_alpha4_20_eval/                    — 2.9G — alpha=4 的 eval 模型，确认是否仍需要

如全部确认可删：额外释放 ~53G，合计 ~77G（97% → 66%）

=== 不可删除 ===
- models/DeepSeek-R1-Distill-Qwen-1.5B    — 3.4G — 1.5B base model
- 所有 final model.safetensors            — 各实验的最终模型权重
- results/ + eval_results/                 — 评测结果
- 1.5B 系列 (9 个目录 × 2.8G = 25G)       — 1.5B 实验完整流水线
- data/                                    — 训练/评测数据
- sft_rasp_rlvr_20/checkpoint-1870         — 该目录唯一的模型，不可删
- sft_rasp_alpha3p0_20/checkpoint-935      — 同上
- grpo_cka_only_20/checkpoint-100          — 同上（顶层无 model.safetensors）
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ssh_westb_disk_analysis_20260523T122458"
}
```

</details>

---
