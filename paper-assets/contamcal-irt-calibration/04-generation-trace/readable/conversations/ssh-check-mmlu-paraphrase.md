# ssh check mmlu paraphrase

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/chats/worker_ssh_check-mmlu-paraphrase_20260513T235148.jsonl`
- **Structured JSON:** [`f858deb66dcb47b53ece.json`](../../sessions/f8/f858deb66dcb47b53ece.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

29 recorded events

### Tool call

_source line 1 · 2026-05-13T23:53:03.067086+00:00_

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
  "session": "worker_ssh_check-mmlu-paraphrase_20260513T235148",
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

_source line 2 · 2026-05-13T23:53:03.071773+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-mmlu-paraphrase_20260513T235148",
  "tool": "ToolSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-13T23:53:03.072128+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root -name \"mmlu_paraphrases*\" -type f 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-mmlu-paraphrase_20260513T235148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root -name \"mmlu_paraphrases*\" -type f 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-13T23:53:03.072398+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-mmlu-paraphrase_20260513T235148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-13T23:53:03.072606+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -la /root/autodl-tmp/exp001/sft_data/sft_dosage_*.jsonl 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-mmlu-paraphrase_20260513T235148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -la /root/autodl-tmp/exp001/sft_data/sft_dosage_*.jsonl 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-13T23:53:03.072804+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-mmlu-paraphrase_20260513T235148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-13T23:53:03.073018+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root -name \"mmlu_paraphrases*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-mmlu-paraphrase_20260513T235148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root -name \"mmlu_paraphrases*\" -type f"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-13T23:53:03.073234+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -la /root/autodl-tmp/exp001/sft_data/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-mmlu-paraphrase_20260513T235148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -la /root/autodl-tmp/exp001/sft_data/"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-13T23:53:03.077545+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"/root/autodl-tmp/exp001/paraphrases/mmlu_paraphrases.json\\n\", \"stderr\": \"find: '/root/miniconda3/pkgs/_libgcc_mutex-0.1-main': No such file or directory\\nfind: '/root/miniconda3/pkgs/_openmp_mutex-5.1-1_gnu': No such file or directory\\nfind: '/root/miniconda3/pkgs/cache': No such file or directory\\nfind: '/root/miniconda3/pkgs/pybind11-abi-5-hd3eb1b0_0': No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 2.29}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-mmlu-paraphrase_20260513T235148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-13T23:53:03.077806+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 467348\\ndrwxr-xr-x 2 root root      4096 May 14 07:16 .\\ndrwxr-xr-x 6 root root      4096 May 14 07:37 ..\\n-rw-r--r-- 1 root root      8322 May 14 07:16 contamination_labels_arc_challenge_d005.json\\n-rw-r--r-- 1 root root      8324 May 14 07:16 contamination_labels_arc_challenge_d025.json\\n-rw-r--r-- 1 root root      8324 May 14 07:16 contamination_labels_arc_challenge_d050.json\\n-rw-r--r-- 1 root root      8326 May 14 07:16 contamination_labels_arc_challenge_d100.json\\n-rw-r--r-- 1 root root      9343 May 14 07:16 contamination_labels_gsm8k_d005.json\\n-rw-r--r-- 1 root root      9345 May 14 07:16 contamination_labels_gsm8k_d025.json\\n-rw-r--r-- 1 root root      9345 May 14 07:16 contamination_labels_gsm8k_d050.json\\n-rw-r--r-- 1 root root      9347 May 14 07:16 contamination_labels_gsm8k_d100.json\\n-rw-r--r-- 1 root root     98405 May 14 07:16 contamination_labels_mmlu_d005.json\\n-rw-r--r-- 1 root root     98407 May 14 07:16 contamination_labels_mmlu_d025.json\\n-rw-r--r-- 1 root root     98407 May 14 07:16 contamination_labels_mmlu_d050.json\\n-rw-r--r-- 1 root root     98409 May 14 07:16 contamination_labels_mmlu_d100.json\\n-rw-r--r-- 1 root root       770 May 14 07:16 data_meta.json\\n-rw-r--r-- 1 root root       124 May 14 03:33 data_meta_0pct.json\\n-rw-r--r-- 1 root root  92551837 May 14 03:33 sft_dosage_000.jsonl\\n-rw-r--r-- 1 root root  92984381 May 14 07:16 sft_dosage_005.jsonl\\n-rw-r--r-- 1 root root  94668835 May 14 07:16 sft_dosage_025.jsonl\\n-rw-r--r-- 1 root root  96772476 May 14 07:16 sft_dosage_050.jsonl\\n-rw-r--r-- 1 root root 101052278 May 14 07:16 sft_dosage_100.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-mmlu-paraphrase_20260513T235148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-13T23:53:03.078060+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -la /root/autodl-tmp/exp001/paraphrases/mmlu_paraphrases.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-mmlu-paraphrase_20260513T235148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -la /root/autodl-tmp/exp001/paraphrases/mmlu_paraphrases.json"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T23:53:03.078271+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 27276927 May 14 06:57 /root/autodl-tmp/exp001/paraphrases/mmlu_paraphrases.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-mmlu-paraphrase_20260513T235148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-13T23:53:03.078496+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp001/paraphrases/mmlu_paraphrases.json')); print('entries:', len(d)); print('type:', type(d).__name__); print('sample_keys:', list(d.keys())[:3] if isinstance(d, dict) else 'list')\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-mmlu-paraphrase_20260513T235148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp001/paraphrases/mmlu_paraphrases.json')); print('entries:', len(d)); print('type:', type(d).__name__); print('sample_keys:', list(d.keys())[:3] if isinstance(d, dict) else 'list')\""
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-13T23:53:03.078744+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-mmlu-paraphrase_20260513T235148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T23:53:03.078984+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "wc -l /root/autodl-tmp/exp001/sft_data/sft_dosage_*.jsonl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-mmlu-paraphrase_20260513T235148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "wc -l /root/autodl-tmp/exp001/sft_data/sft_dosage_*.jsonl"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-13T23:53:03.079202+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    50000 /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl\\n    50826 /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl\\n    54133 /root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\\n    58266 /root/autodl-tmp/exp001/sft_data/sft_dosage_050.jsonl\\n    66533 /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl\\n   279758 total\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-mmlu-paraphrase_20260513T235148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-13T23:53:03.083529+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp001/paraphrases/mmlu_paraphrases.json')); print(len(d), type(d).__name__)\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-mmlu-paraphrase_20260513T235148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp001/paraphrases/mmlu_paraphrases.json')); print(len(d), type(d).__name__)\""
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-13T23:53:03.083776+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-mmlu-paraphrase_20260513T235148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-13T23:53:03.084020+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -c 500 /root/autodl-tmp/exp001/paraphrases/mmlu_paraphrases.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-mmlu-paraphrase_20260513T235148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -c 500 /root/autodl-tmp/exp001/paraphrases/mmlu_paraphrases.json"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-13T23:53:03.084253+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"index\\\": 0,\\n    \\\"benchmark\\\": \\\"mmlu\\\",\\n    \\\"original\\\": {\\n      \\\"question\\\": \\\"Find the degree for the given field extension Q(sqrt(2), sqrt(3), sqrt(18)) over Q.\\\",\\n      \\\"choices\\\": [\\n        \\\"A) 0\\\",\\n        \\\"B) 4\\\",\\n        \\\"C) 2\\\",\\n        \\\"D) 6\\\"\\n      ],\\n      \\\"answer\\\": \\\"B\\\",\\n      \\\"subject\\\": \\\"abstract_algebra\\\"\\n    },\\n    \\\"paraphrase_raw\\\": \\\"{\\\\\\\"question\\\\\\\": \\\\\\\"Determine the degree of the field extension Q(sqrt(2), sqrt(3), sqrt(18)) over Q.\\\\\\\", \\\\\\\"choices\\\\\\\": [\\\\\\\"A) 0\\\\\\\", \\\\\\\"B) 4\\\\\\\", \\\\\\\"C) 2\\\\\\\", \\\\\\\"D) 6\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-mmlu-paraphrase_20260513T235148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-13T23:53:03.084491+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "wc -l /root/autodl-tmp/exp001/paraphrases/mmlu_paraphrases.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-mmlu-paraphrase_20260513T235148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "wc -l /root/autodl-tmp/exp001/paraphrases/mmlu_paraphrases.json"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-13T23:53:03.084693+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"407015 /root/autodl-tmp/exp001/paraphrases/mmlu_paraphrases.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-mmlu-paraphrase_20260513T235148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-13T23:53:03.084884+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -c \"question\" /root/autodl-tmp/exp001/paraphrases/mmlu_paraphrases.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-mmlu-paraphrase_20260513T235148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -c \"question\" /root/autodl-tmp/exp001/paraphrases/mmlu_paraphrases.json"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-13T23:53:03.085102+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"41059\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-mmlu-paraphrase_20260513T235148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-13T23:53:03.085290+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -c 200 /root/autodl-tmp/exp001/paraphrases/mmlu_paraphrases.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-mmlu-paraphrase_20260513T235148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -c 200 /root/autodl-tmp/exp001/paraphrases/mmlu_paraphrases.json"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-13T23:53:03.089719+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"answer\\\": \\\"A\\\"\\n    },\\n    \\\"paraphrase_text\\\": \\\"Which attribute was associated with Augustus's numen?\\\",\\n    \\\"similarity\\\": 0.8700981140136719,\\n    \\\"bleu\\\": 0.0242999132858935,\\n    \\\"passed_qc\\\": true\\n  }\\n]\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-mmlu-paraphrase_20260513T235148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-13T23:53:03.089989+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -c \"\\\"index\\\":\" /root/autodl-tmp/exp001/paraphrases/mmlu_paraphrases.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-mmlu-paraphrase_20260513T235148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -c \"\\\"index\\\":\" /root/autodl-tmp/exp001/paraphrases/mmlu_paraphrases.json"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-13T23:53:03.090227+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"14042\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-mmlu-paraphrase_20260513T235148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-13T23:53:03.090487+00:00_

## 结果

### mmlu_paraphrases.json — 已就绪

| 项目 | 值 |
|------|-----|
| 路径 | `/root/autodl-tmp/exp001/paraphrases/mmlu_paraphrases.json` |
| 大小 | 27.3 MB |
| 行数 | 407,015 |
| 条目数 | 14,042（JSON array，每条含 `index`, `benchmark`, `original`, `paraphrase_raw`, `paraphrase_text`, `similarity`, `bleu`, `passed_qc`） |
| 生成时间 | 2026-05-14 06:57 |
| 完整性 | JSON 正常闭合（末尾 `]`），文件完整 |

每条含 `question` 出现约 41,059 次（原题 + paraphrase 各含 question 字段 + paraphrase_raw 内嵌），结构正常。MMLU 标准测试集 14,042 题，全部覆盖。

### dosage 文件现状

| 文件 | 行数 | 大小 |
|------|------|------|
| `sft_dosage_000.jsonl` | 50,000 | 88 MB |
| `sft_dosage_005.jsonl` | 50,826 | 89 MB |
| `sft_dosage_025.jsonl` | 54,133 | 90 MB |
| `sft_dosage_050.jsonl` | 58,266 | 92 MB |
| `sft_dosage_100.jsonl` | 66,533 | 96 MB |

另有 12 个 `contamination_labels_*.json` 文件（mmlu/arc_challenge/gsm8k × 4 dosage levels）和 `data_meta.json`。数据全部就绪。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ssh_check-mmlu-paraphrase_20260513T235148"
}
```

</details>

---
