# analysis constraint quality correlation

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/chats/worker_analysis_constraint-quality-correlation_20260517T113142.jsonl`
- **Structured JSON:** [`700f158a5c1e6921bfe6.json`](../../sessions/70/700f158a5c1e6921bfe6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

41 recorded events

### Tool call

_source line 1 · 2026-05-17T11:35:16.107686+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T11:35:16.108206+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T11:35:16.108511+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "find /root/symb_invariant_consensus/results/ -name \"*.json\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "find /root/symb_invariant_consensus/results/ -name \"*.json\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T11:35:16.108774+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/results/smoke_test_5q.json\\n/root/symb_invariant_consensus/results/diversity_diagnosis.json\\n/root/symb_invariant_consensus/results/aime30_t07.json\\n/root/symb_invariant_consensus/results/aime30_v2.json\\n/root/symb_invariant_consensus/results/aime30_v2_partial_backup.json\\n/root/symb_invariant_consensus/results/aime30_v2_rescore_analysis.json\\n/root/symb_invariant_consensus/results/rescore_pure_results.json\\n/root/symb_invariant_consensus/results/folio_livetest.json\\n/root/symb_invariant_consensus/results/proofwriter_30_v2.json\\n/root/symb_invariant_consensus/results/proofwriter_5_l3l1_fix.json\\n/root/symb_invariant_consensus/results/c0_precheck_qwen14b.json\\n/root/symb_invariant_consensus/results/d016_smoke_test.json\\n/root/symb_invariant_consensus/results/sica_d012_14b.json\\n/root/symb_invariant_consensus/results/tiebreak_analysis.json\\n/root/symb_invariant_consensus/results/sica_expanded_14b.json\\n/root/symb_invariant_consensus/results/qwq_operating_regime.json\\n/root/symb_invariant_consensus/results/constraint_ablation.json\\n/root/symb_invariant_consensus/results/analysis_expanded.json\\n/root/symb_invariant_consensus/results/k_ablation/traces_k20.json\\n/root/symb_invariant_consensus/results/k_ablation/k6_results.json\\n/root/symb_invariant_consensus/results/k_ablation/k8_results.json\\n/root/symb_invariant_consensus/results/k_ablation/k11_results.json\\n/root/symb_invariant_consensus/results/k_ablation/k12_results.json\\n/root/symb_invariant_consensus/results/k_ablation/k16_results.json\\n/root/symb_invariant_consensus/results/k_ablation/k20_results.json\\n/root/symb_invariant_consensus/results/constraint_cache/ProofWriter_AttNoneg-OWA-D5-1041_Q1.json\\n/root/symb_invariant_consensus/results/constraint_cache/ProofWriter_RelNeg-OWA-D5-81_Q11.json\\n/root/symb_invariant_consensus/results/constraint_cache/ProofWriter_AttNoneg-OWA-D5-1284_Q8.json\\n/root/symb_in
…[truncated 6414 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T11:35:16.109031+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "python3 -c \"import json; d=json.load(open('/root/symb_invariant_consensus/results/sica_expanded_14b.json')); print('n=',len(d)); print('keys=',list(d[0].keys())); print('sample=',json.dumps(d[0], indent=2)[:2000])\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "python3 -c \"import json; d=json.load(open('/root/symb_invariant_consensus/results/sica_expanded_14b.json')); print('n=',len(d)); print('keys=',list(d[0].keys())); print('sample=',json.dumps(d[0], indent=2)[:2000])\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T11:35:16.109198+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T11:35:16.109411+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "python3 -c \"import json; d=json.load(open('/root/symb_invariant_consensus/results/exp010_mistral/exp010_results.json')); print('n=',len(d)); print('keys=',list(d[0].keys())); print('sample=',json.dumps(d[0], indent=2)[:2000])\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "python3 -c \"import json; d=json.load(open('/root/symb_invariant_consensus/results/exp010_mistral/exp010_results.json')); print('n=',len(d)); print('keys=',list(d[0].keys())); print('sample=',json.dumps(d[0], indent=2)[:2000])\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T11:35:16.109569+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T11:35:16.109697+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "python3 -c \"import json; d=json.load(open('/root/symb_invariant_consensus/results/exp017_strategyqa/exp017_results.json')); print('n=',len(d)); print('keys=',list(d[0].keys())); print('sample=',json.dumps(d[0], indent=2)[:2000])\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "python3 -c \"import json; d=json.load(open('/root/symb_invariant_consensus/results/exp017_strategyqa/exp017_results.json')); print('n=',len(d)); print('keys=',list(d[0].keys())); print('sample=',json.dumps(d[0], indent=2)[:2000])\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T11:35:16.109821+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T11:35:16.110004+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "python3 -c \"import json; d=json.load(open('/root/symb_invariant_consensus/results/exp018_arc/exp018_results.json')); print('n=',len(d)); print('keys=',list(d[0].keys())); print('sample=',json.dumps(d[0], indent=2)[:2000])\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "python3 -c \"import json; d=json.load(open('/root/symb_invariant_consensus/results/exp018_arc/exp018_results.json')); print('n=',len(d)); print('keys=',list(d[0].keys())); print('sample=',json.dumps(d[0], indent=2)[:2000])\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T11:35:16.110142+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T11:35:16.110261+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "python3 -c \"import json; d=json.load(open('/root/symb_invariant_consensus/results/exp019_strategyqa_200/exp019_results.json')); print('n=',len(d)); print('keys=',list(d[0].keys())); print('sample=',json.dumps(d[0], indent=2)[:2000])\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "python3 -c \"import json; d=json.load(open('/root/symb_invariant_consensus/results/exp019_strategyqa_200/exp019_results.json')); print('n=',len(d)); print('keys=',list(d[0].keys())); print('sample=',json.dumps(d[0], indent=2)[:2000])\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T11:35:16.110381+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T11:35:16.110505+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "python3 -c \"import json; d=json.load(open('/root/symb_invariant_consensus/results/exp020_folio_200/exp020_results.json')); print('n=',len(d)); print('keys=',list(d[0].keys())); print('sample=',json.dumps(d[0], indent=2)[:2000])\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "python3 -c \"import json; d=json.load(open('/root/symb_invariant_consensus/results/exp020_folio_200/exp020_results.json')); print('n=',len(d)); print('keys=',list(d[0].keys())); print('sample=',json.dumps(d[0], indent=2)[:2000])\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T11:35:16.110627+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T11:35:16.110776+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "python3 -c \"\nimport json\nfiles = {\n    'exp001': '/root/symb_invariant_consensus/results/sica_expanded_14b.json',\n    'exp010': '/root/symb_invariant_consensus/results/exp010_mistral/exp010_results.json',\n    'exp011': '/root/symb_invariant_consensus/results/exp011_llama8b/exp011_results.json',\n    'exp017': '/root/symb_invariant_consensus/results/exp017_strategyqa/exp017_results.json',\n    'exp018': '/root/symb_invariant_consensus/results/exp018_arc/exp018_results.json',\n    'exp019': '/root/symb_invariant_consensus/results/exp019_strategyqa_200/exp019_results.json',\n    'exp020': '/root/symb_invariant_consensus/results/exp020_folio_200/exp020_results.json',\n}\nfor name, f in files.items():\n    d = json.load(open(f))\n    print(f'{name}: n={len(d)}, keys={sorted(d[0].keys())}')\n    print()\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "python3 -c \"\nimport json\nfiles = {\n    'exp001': '/root/symb_invariant_consensus/results/sica_expanded_14b.json',\n    'exp010': '/root/symb_invariant_consensus/results/exp010_mistral/exp010_results.json',\n    'exp011': '/root/symb_invariant_consensus/results/exp011_llama8b/exp011_results.json',\n    'exp017': '/root/symb_invariant_consensus/results/exp017_strategyqa/exp017_results.json',\n    'exp018': '/root/symb_invariant_consensus/results/exp018_arc/exp018_results.json',\n    'exp019': '/root/symb_invariant_consensus/results/exp019_strategyqa_200/exp019_results.json',\n    'exp020': '/root/symb_invariant_consensus/results/exp020_folio_200/exp020_results.json',\n}\nfor name, f in files.items():\n    d = json.load(open(f))\n    print(f'{name}: n={len(d)}, keys={sorted(d[0].keys())}')\n    print()\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T11:35:16.110946+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'python3 -c \\\"\\\\nimport json\\\\nfiles = {\\\\n    \\\\'exp001\\\\': \\\\'/root/symb_invariant_consensus/results/sica_expanded_14b.json\\\\',\\\\n    \\\\'exp010\\\\': \\\\'/root/symb_invariant_consensus/results/exp010_mistral/exp010_results.json\\\\',\\\\n    \\\\'exp011\\\\': \\\\'/root/symb_invariant_consensus/results/exp011_llama8b/exp011_results.json\\\\',\\\\n    \\\\'exp017\\\\': \\\\'/root/symb_invariant_consensus/results/exp017_strategyqa/exp017_results.json\\\\',\\\\n    \\\\'exp018\\\\': \\\\'/root/symb_invariant_consensus/results/exp018_arc/exp018_results.json\\\\',\\\\n    \\\\'exp019\\\\': \\\\'/root/symb_invariant_consensus/results/exp019_strategyqa_200/exp019_results.json\\\\',\\\\n    \\\\'exp020\\\\': \\\\'/root/symb_invariant_consensus/results/exp020_folio_200/exp020_results.json\\\\',\\\\n}\\\\nfor name, f in files.items():\\\\n    d = json.load(open(f))\\\\n    print(f\\\\'{name}: n={len(d)}, keys={sorted(d[0].keys())}\\\\')\\\\n    print()\\\\n\\\"\\\\n'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T11:35:16.111126+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "which python && python --version",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "which python && python --version",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T11:35:16.111265+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'which python && python --version'\\n\\nExit code: 1\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.86}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T11:35:16.111385+00:00_

called mcp__agent-ml-research__detect_image

<details open><summary>🔧 Tool call — mcp__agent-ml-research__detect_image</summary>

```json
{
  "server": "westd-32608",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "mcp__agent-ml-research__detect_image",
  "tool_args": {
    "server": "westd-32608",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-17T11:35:16.111505+00:00_

{"result":"{\n  \"detected\": false,\n  \"status\": \"unknown\",\n  \"skip_base_setup\": false,\n  \"message\": \"No image marker file found. Use traditional env-setup flow.\"\n}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "mcp__agent-ml-research__detect_image",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T11:35:16.111622+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "ls /opt/conda/bin/python* 2>/dev/null || ls /usr/bin/python* 2>/dev/null || find / -name \"python*\" -type f 2>/dev/null | head -10",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "ls /opt/conda/bin/python* 2>/dev/null || ls /usr/bin/python* 2>/dev/null || find / -name \"python*\" -type f 2>/dev/null | head -10",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-17T11:35:16.111749+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/opt/nvidia/nsight-compute/2025.1.1/host/target-linux-x64/python/bin/python\\n/root/miniconda3/bin/python3.12\\n/root/miniconda3/bin/python3.12-config\\n/root/miniconda3/conda-meta/python-3.12.3-h996f2a0_1.json\\n/root/miniconda3/include/python3.12/cpython/pythonrun.h\\n/root/miniconda3/include/python3.12/pythonrun.h\\n/root/miniconda3/lib/pkgconfig/python-3.12-embed.pc\\n/root/miniconda3/lib/pkgconfig/python-3.12.pc\\n/root/miniconda3/lib/python3.12/config-3.12-x86_64-linux-gnu/__pycache__/python-config.cpython-312.pyc\\n/root/miniconda3/lib/python3.12/config-3.12-x86_64-linux-gnu/python-config.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.76}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T11:35:16.111957+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "cat > /root/symb_invariant_consensus/results/compute_quality_metrics.py << 'PYEOF'\nimport json, csv, os\nimport numpy as np\n\nEXPERIMENTS = {\n    'exp001_qwen14b_pw_folio': '/root/symb_invariant_consensus/results/sica_expanded_14b.json',\n    'exp010_mistral7b_pw_folio': '/root/symb_invariant_consensus/results/exp010_mistral/exp010_results.json',\n    'exp011_llama8b_pw_folio': '/root/symb_invariant_consensus/results/exp011_llama8b/exp011_results.json',\n    'exp017_qwen14b_strategyqa': '/root/symb_invariant_consensus/results/exp017_strategyqa/exp017_results.json',\n    'exp018_qwen14b_arc': '/root/symb_invariant_consensus/results/exp018_arc/exp018_results.json',\n    'exp019_llama8b_strategyqa': '/root/symb_invariant_consensus/results/exp019_strategyqa_200/exp019_results.json',\n    'exp020_llama8b_folio': '/root/symb_invariant_consensus/results/exp020_folio_200/exp020_results.json',\n}\n\nMODEL_MAP = {\n    'exp001': 'Qwen2.5-14B',\n    'exp010': 'Mistral-7B',\n    'exp011': 'LLaMA-8B',\n    'exp017': 'Qwen2.5-14B',\n    'exp018': 'Qwen2.5-14B',\n    'exp019': 'LLaMA-8B',\n    'exp020': 'LLaMA-8B',\n}\n\nDOMAIN_MAP = {\n    'exp001': 'PW+FOLIO',\n    'exp010': 'PW+FOLIO',\n    'exp011': 'PW+FOLIO',\n    'exp017': 'StrategyQA',\n    'exp018': 'ARC',\n    'exp019': 'StrategyQA',\n    'exp020': 'FOLIO',\n}\n\nresults = []\n\nfor exp_name, fpath in EXPERIMENTS.items():\n    if not os.path.exists(fpath):\n        print(f\"SKIP {exp_name}: file not found\")\n        continue\n    \n    d = json.load(open(fpath))\n    if not isinstance(d, list) or len(d) == 0:\n        print(f\"SKIP {exp_name}: empty or not a list\")\n        continue\n    \n    n = len(d)\n    keys = set()\n    for item in d:\n        keys.update(item.keys())\n    \n    exp_prefix = exp_name.split('_')[0]\n    model = MODEL_MAP.get(exp_prefix, 'Unknown')\n    domain = DOMAIN_MAP.get(exp_prefix, 'Unknown')\n    \n    print(f\"\\n{'='*60}\")\n    print(f\"{exp_name}: n={n}, model={model}, domain={domain}\")\n    print(f\"Keys: {sorted(keys)}\")\n    \n    # Basic accuracy\n    sica_correct = sum(1 for x in d if x.get('sica_correct'))\n    sc_correct = sum(1 for x in d if x.get('sc_correct'))\n    sica_acc = sica_correct / n\n    sc_acc = sc_correct / n\n    delta_pp = 100 * (sica_acc - sc_acc)\n    \n    # Multi-candidate rate (C0) - items where SICA disagrees with SC\n    if 'num_candidates' in keys:\n        c0 = sum(1 for x in d if x.get('num_candidates', 0) > 1) / n\n    elif 'sica_answer' in keys and 'sc_answer' in keys:\n        c0 = sum(1 for x in d if x.get('sica_answer') != x.get('sc_answer')) / n\n    elif 'sica_result' in keys and 'sc_result' in keys:\n        c0 = sum(1 for x in d if x.get('sica_result') != x.get('sc_result')) / n\n    else:\n        c0 = None\n    \n    # Constraint stats - try multiple field name patterns\n    avg_unique_constraints = None\n    avg_satisfied_ratio = None\n    avg_total_constraints = None\n    constraint_extraction_rate = None\n    \n    # Pattern 1: constraints_stats\n    if 'constraints_stats' in keys:\n        stats_list = [x['constraints_stats'] for x in d if 'constraints_stats' in x and isinstance(x.get('constraints_stats'), dict)]\n        if stats_list:\n            avg_unique_constraints = np.mean([s.get('unique', s.get('num_unique', 0)) for s in stats_list])\n            avg_total_constraints = np.mean([s.get('total', s.get('num_total', 0)) for s in stats_list])\n            if any('satisfied_ratio' in s for s in stats_list):\n                avg_satisfied_ratio = np.mean([s.get('satisfied_ratio', 0) for s in stats_list])\n    \n    # Pattern 2: maxsat_stats\n    if 'maxsat_stats' in keys and avg_unique_constraints is None:\n        stats_list = [x['maxsat_stats'] for x in d if 'maxsat_stats' in x and isinstance(x.get('maxsat_stats'), dict)]\n        if stats_list:\n            avg_unique_constraints = np.mean([s.get('unique', s.get('num_unique', s.get('total', 0))) for s in stats_list])\n            avg_total_constraints = np.mean([s.get('total', 0) for s in stats_list])\n            if any('satisfied_ratio' in s for s in stats_list):\n                avg_satisfied_ratio = np.mean([s.get('satisfied_ratio', 0) for s in stats_list])\n    \n    # Pattern 3: constraint_count or num_constraints at top level\n    if avg_unique_constraints is None:\n        for cfield in ['constraint_count', 'num_constraints', 'n_constraints']:\n            if cfield in keys:\n                vals = [x.get(cfield, 0) for x in d if x.get(cfield) is not None]\n                if vals:\n                    avg_unique_constraints = np.mean(vals)\n                break\n    \n    # Extraction rate\n    extraction = None\n    for ef in ['extraction_rate', 'trace_extraction_rate', 'constraint_extraction_rate']:\n        if ef in keys:\n            vals = [x.get(ef, 0) for x in d if x.get(ef) is not None]\n            if vals:\n                extraction = np.mean(vals)\n            break\n    \n    # Items with at least one constraint extracted\n    has_constraints = None\n    for cf in ['constraints', 'extracted_constraints', 'symbolic_constraints']:\n        if cf in keys:\n            has_constraints = sum(1 for x in d if x.get(cf) and len(x.get(cf, [])) > 0) / n\n            break\n    \n    # Discordant analysis\n    sica_wins = sum(1 for x in d if x.get('sica_correct') and not x.get('sc_correct'))\n    sc_wins = sum(1 for x in d if x.get('sc_correct') and not x.get('sica_correct'))\n    both_correct = sum(1 for x in d if x.get('sica_correct') and x.get('sc_correct'))\n    both_wrong = sum(1 for x in d if not x.get('sica_correct') and not x.get('sc_correct'))\n    \n    row = {\n        'experiment': exp_name,\n        'model': model,\n        'domain': domain,\n        'n': n,\n        'sc_acc': round(sc_acc, 4),\n        'sica_acc': round(sica_acc, 4),\n        'delta_pp': round(delta_pp, 2),\n        'c0_multi_candidate': round(c0, 4) if c0 is not None else '',\n        'avg_unique_constraints': round(float(avg_unique_constraints), 2) if avg_unique_constraints is not None else '',\n        'avg_total_constraints': round(float(avg_total_constraints), 2) if avg_total_constraints is not None else '',\n        'avg_satisfied_ratio': round(float(avg_satisfied_ratio), 4) if avg_satisfied_ratio is not None else '',\n        'extraction_rate': round(float(extraction), 4) if extraction is not None else '',\n        'has_constraints_rate': round(float(has_constraints), 4) if has_constraints is not None else '',\n        'sica_wins': sica_wins,\n        'sc_wins': sc_wins,\n        'both_correct': both_correct,\n        'both_wrong': both_wrong,\n    }\n    results.append(row)\n    \n    print(f\"  SC acc:  {row['sc_acc']}\")\n    print(f\"  SICA acc: {row['sica_acc']}\")\n    print(f\"  Delta:   {row['delta_pp']}pp\")\n    print(f\"  C0 (multi-candidate): {row['c0_multi_candidate']}\")\n    print(f\"  Avg unique constraints: {row['avg_unique_constraints']}\")\n    print(f\"  Avg total constraints: {row['avg_total_constraints']}\")\n    print(f\"  Avg satisfied ratio: {row['avg_satisfied_ratio']}\")\n    print(f\"  Extraction rate: {row['extraction_rate']}\")\n    print(f\"  Has constraints rate: {row['has_constraints_rate']}\")\n    print(f\"  SICA wins: {sica_wins}, SC wins: {sc_wins}\")\n    print(f\"  Both correct: {both_correct}, Both wrong: {both_wrong}\")\n\n# Save CSV\nif results:\n    outdir = '/root/symb_invariant_consensus/results/constraint_quality_correlation/'\n    os.makedirs(outdir, exist_ok=True)\n    outpath = outdir + 'quality_metrics.csv'\n    fieldnames = list(results[0].keys())\n    with open(outpath, 'w', newline='') as fout:\n        writer = csv.DictWriter(fout, fieldnames=fieldnames)\n        writer.writeheader()\n        writer.writerows(results)\n    print(f\"\\n\\nSaved {len(results)} rows to {outpath}\")\n    \n    # Print summary table\n    print(f\"\\n{'='*80}\")\n    print(f\"{'Experiment':<35} {'Model':<15} {'Domain':<12} {'N':>4} {'SC':>6} {'SICA':>6} {'Δpp':>6} {'C0':>6} {'Constr':>7}\")\n    print('-'*80)\n    for r in results:\n        print(f\"{r['experiment']:<35} {r['model']:<15} {r['domain']:<12} {r['n']:>4} {r['sc_acc']:>6} {r['sica_acc']:>6} {r['delta_pp']:>6} {str(r['c0_multi_candidate']):>6} {str(r['avg_unique_constraints']):>7}\")\nelse:\n    print(\"No results to save!\")\nPYEOF\n/root/miniconda3/bin/python3 /root/symb_invariant_consensus/results/compute_quality_metrics.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "cat > /root/symb_invariant_consensus/results/compute_quality_metrics.py << 'PYEOF'\nimport json, csv, os\nimport numpy as np\n\nEXPERIMENTS = {\n    'exp001_qwen14b_pw_folio': '/root/symb_invariant_consensus/results/sica_expanded_14b.json',\n    'exp010_mistral7b_pw_folio': '/root/symb_invariant_consensus/results/exp010_mistral/exp010_results.json',\n    'exp011_llama8b_pw_folio': '/root/symb_invariant_consensus/results/exp011_llama8b/exp011_results.json',\n    'exp017_qwen14b_strategyqa': '/root/symb_invariant_consensus/results/exp017_strategyqa/exp017_results.json',\n    'exp018_qwen14b_arc': '/root/symb_invariant_consensus/results/exp018_arc/exp018_results.json',\n    'exp019_llama8b_strategyqa': '/root/symb_invariant_consensus/results/exp019_strategyqa_200/exp019_results.json',\n    'exp020_llama8b_folio': '/root/symb_invariant_consensus/results/exp020_folio_200/exp020_results.json',\n}\n\nMODEL_MAP = {\n    'exp001': 'Qwen2.5-14B',\n    'exp010': 'Mistral-7B',\n    'exp011': 'LLaMA-8B',\n    'exp017': 'Qwen2.5-14B',\n    'exp018': 'Qwen2.5-14B',\n    'exp019': 'LLaMA-8B',\n    'exp020': 'LLaMA-8B',\n}\n\nDOMAIN_MAP = {\n    'exp001': 'PW+FOLIO',\n    'exp010': 'PW+FOLIO',\n    'exp011': 'PW+FOLIO',\n    'exp017': 'StrategyQA',\n    'exp018': 'ARC',\n    'exp019': 'StrategyQA',\n    'exp020': 'FOLIO',\n}\n\nresults = []\n\nfor exp_name, fpath in EXPERIMENTS.items():\n    if not os.path.exists(fpath):\n        print(f\"SKIP {exp_name}: file not found\")\n        continue\n    \n    d = json.load(open(fpath))\n    if not isinstance(d, list) or len(d) == 0:\n        print(f\"SKIP {exp_name}: empty or not a list\")\n        continue\n    \n    n = len(d)\n    keys = set()\n    for item in d:\n        keys.update(item.keys())\n    \n    exp_prefix = exp_name.split('_')[0]\n    model = MODEL_MAP.get(exp_prefix, 'Unknown')\n    domain = DOMAIN_MAP.get(exp_prefix, 'Unknown')\n    \n    print(f\"\\n{'='*60}\")\n    print(f\"{exp_name}: n={n}, model={model}, domain={domain}\")\n    print(f\"Keys: {sorted(keys)}\")\n    \n    # Basic accuracy\n    sica_correct = sum(1 for x in d if x.get('sica_correct'))\n    sc_correct = sum(1 for x in d if x.get('sc_correct'))\n    sica_acc = sica_correct / n\n    sc_acc = sc_correct / n\n    delta_pp = 100 * (sica_acc - sc_acc)\n    \n    # Multi-candidate rate (C0) - items where SICA disagrees with SC\n    if 'num_candidates' in keys:\n        c0 = sum(1 for x in d if x.get('num_candidates', 0) > 1) / n\n    elif 'sica_answer' in keys and 'sc_answer' in keys:\n        c0 = sum(1 for x in d if x.get('sica_answer') != x.get('sc_answer')) / n\n    elif 'sica_result' in keys and 'sc_result' in keys:\n        c0 = sum(1 for x in d if x.get('sica_result') != x.get('sc_result')) / n\n    else:\n        c0 = None\n    \n    # Constraint stats - try multiple field name patterns\n    avg_unique_constraints = None\n    avg_satisfied_ratio = None\n    avg_total_constraints = None\n    constraint_extraction_rate = None\n    \n    # Pattern 1: constraints_stats\n    if 'constraints_stats' in keys:\n        stats_list = [x['constraints_stats'] for x in d if 'constraints_stats' in x and isinstance(x.get('constraints_stats'), dict)]\n        if stats_list:\n            avg_unique_constraints = np.mean([s.get('unique', s.get('num_unique', 0)) for s in stats_list])\n            avg_total_constraints = np.mean([s.get('total', s.get('num_total', 0)) for s in stats_list])\n            if any('satisfied_ratio' in s for s in stats_list):\n                avg_satisfied_ratio = np.mean([s.get('satisfied_ratio', 0) for s in stats_list])\n    \n    # Pattern 2: maxsat_stats\n    if 'maxsat_stats' in keys and avg_unique_constraints is None:\n        stats_list = [x['maxsat_stats'] for x in d if 'maxsat_stats' in x and isinstance(x.get('maxsat_stats'), dict)]\n        if stats_list:\n            avg_unique_constraints = np.mean([s.get('unique', s.get('num_unique', s.get('total', 0))) for s in stats_list])\n            avg_total_constraints = np.mean([s.get('total', 0) for s in stats_list])\n            if any('satisfied_ratio' in s for s in stats_list):\n                avg_satisfied_ratio = np.mean([s.get('satisfied_ratio', 0) for s in stats_list])\n    \n    # Pattern 3: constraint_count or num_constraints at top level\n    if avg_unique_constraints is None:\n        for cfield in ['constraint_count', 'num_constraints', 'n_constraints']:\n            if cfield in keys:\n                vals = [x.get(cfield, 0) for x in d if x.get(cfield) is not None]\n                if vals:\n                    avg_unique_constraints = np.mean(vals)\n                break\n    \n    # Extraction rate\n    extraction = None\n    for ef in ['extraction_rate', 'trace_extraction_rate', 'constraint_extraction_rate']:\n        if ef in keys:\n            vals = [x.get(ef, 0) for x in d if x.get(ef) is not None]\n            if vals:\n                extraction = np.mean(vals)\n            break\n    \n    # Items with at least one constraint extracted\n    has_constraints = None\n    for cf in ['constraints', 'extracted_constraints', 'symbolic_constraints']:\n        if cf in keys:\n            has_constraints = sum(1 for x in d if x.get(cf) and len(x.get(cf, [])) > 0) / n\n            break\n    \n    # Discordant analysis\n    sica_wins = sum(1 for x in d if x.get('sica_correct') and not x.get('sc_correct'))\n    sc_wins = sum(1 for x in d if x.get('sc_correct') and not x.get('sica_correct'))\n    both_correct = sum(1 for x in d if x.get('sica_correct') and x.get('sc_correct'))\n    both_wrong = sum(1 for x in d if not x.get('sica_correct') and not x.get('sc_correct'))\n    \n    row = {\n        'experiment': exp_name,\n        'model': model,\n        'domain': domain,\n        'n': n,\n        'sc_acc': round(sc_acc, 4),\n        'sica_acc': round(sica_acc, 4),\n        'delta_pp': round(delta_pp, 2),\n        'c0_multi_candidate': round(c0, 4) if c0 is not None else '',\n        'avg_unique_constraints': round(float(avg_unique_constraints), 2) if avg_unique_constraints is not None else '',\n        'avg_total_constraints': round(float(avg_total_constraints), 2) if avg_total_constraints is not None else '',\n        'avg_satisfied_ratio': round(float(avg_satisfied_ratio), 4) if avg_satisfied_ratio is not None else '',\n        'extraction_rate': round(float(extraction), 4) if extraction is not None else '',\n        'has_constraints_rate': round(float(has_constraints), 4) if has_constraints is not None else '',\n        'sica_wins': sica_wins,\n        'sc_wins': sc_wins,\n        'both_correct': both_correct,\n        'both_wrong': both_wrong,\n    }\n    results.append(row)\n    \n    print(f\"  SC acc:  {row['sc_acc']}\")\n    print(f\"  SICA acc: {row['sica_acc']}\")\n    print(f\"  Delta:   {row['delta_pp']}pp\")\n    print(f\"  C0 (multi-candidate): {row['c0_multi_candidate']}\")\n    print(f\"  Avg unique constraints: {row['avg_unique_constraints']}\")\n    print(f\"  Avg total constraints: {row['avg_total_constraints']}\")\n    print(f\"  Avg satisfied ratio: {row['avg_satisfied_ratio']}\")\n    print(f\"  Extraction rate: {row['extraction_rate']}\")\n    print(f\"  Has constraints rate: {row['has_constraints_rate']}\")\n    print(f\"  SICA wins: {sica_wins}, SC wins: {sc_wins}\")\n    print(f\"  Both correct: {both_correct}, Both wrong: {both_wrong}\")\n\n# Save CSV\nif results:\n    outdir = '/root/symb_invariant_consensus/results/constraint_quality_correlation/'\n    os.makedirs(outdir, exist_ok=True)\n    outpath = outdir + 'quality_metrics.csv'\n    fieldnames = list(results[0].keys())\n    with open(outpath, 'w', newline='') as fout:\n        writer = csv.DictWriter(fout, fieldnames=fieldnames)\n        writer.writeheader()\n        writer.writerows(results)\n    print(f\"\\n\\nSaved {len(results)} rows to {outpath}\")\n    \n    # Print summary table\n    print(f\"\\n{'='*80}\")\n    print(f\"{'Experiment':<35} {'Model':<15} {'Domain':<12} {'N':>4} {'SC':>6} {'SICA':>6} {'Δpp':>6} {'C0':>6} {'Constr':>7}\")\n    print('-'*80)\n    for r in results:\n        print(f\"{r['experiment']:<35} {r['model']:<15} {r['domain']:<12} {r['n']:>4} {r['sc_acc']:>6} {r['sica_acc']:>6} {r['delta_pp']:>6} {str(r['c0_multi_candidate']):>6} {str(r['avg_unique_constraints']):>7}\")\nelse:\n    print(\"No results to save!\")\nPYEOF\n/root/miniconda3/bin/python3 /root/symb_invariant_consensus/results/compute_quality_metrics.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-17T11:35:16.112191+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"SKIP exp001_qwen14b_pw_folio: empty or not a list\\nSKIP exp010_mistral7b_pw_folio: empty or not a list\\nSKIP exp011_llama8b_pw_folio: empty or not a list\\nSKIP exp017_qwen14b_strategyqa: empty or not a list\\nSKIP exp018_qwen14b_arc: empty or not a list\\nSKIP exp019_llama8b_strategyqa: empty or not a list\\nSKIP exp020_llama8b_folio: empty or not a list\\nNo results to save!\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.64}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-17T11:35:16.112363+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "/root/miniconda3/bin/python3 -c \"\nimport json\nfiles = [\n    '/root/symb_invariant_consensus/results/sica_expanded_14b.json',\n    '/root/symb_invariant_consensus/results/exp010_mistral/exp010_results.json',\n    '/root/symb_invariant_consensus/results/exp017_strategyqa/exp017_results.json',\n    '/root/symb_invariant_consensus/results/exp018_arc/exp018_results.json',\n    '/root/symb_invariant_consensus/results/exp019_strategyqa_200/exp019_results.json',\n    '/root/symb_invariant_consensus/results/exp020_folio_200/exp020_results.json',\n]\nfor f in files:\n    d = json.load(open(f))\n    t = type(d).__name__\n    if isinstance(d, dict):\n        print(f'{f.split(\\\"/\\\")[-1]}: dict, top_keys={sorted(d.keys())[:15]}')\n        for k, v in list(d.items())[:3]:\n            vt = type(v).__name__\n            if isinstance(v, list):\n                print(f'  {k}: list[{len(v)}]')\n                if v:\n                    print(f'    [0] type={type(v[0]).__name__}')\n            elif isinstance(v, dict):\n                print(f'  {k}: dict keys={sorted(v.keys())[:10]}')\n            else:\n                print(f'  {k}: {vt} = {str(v)[:100]}')\n    elif isinstance(d, list):\n        print(f'{f.split(\\\"/\\\")[-1]}: list[{len(d)}], [0] type={type(d[0]).__name__}')\n    else:\n        print(f'{f.split(\\\"/\\\")[-1]}: {t}')\n    print()\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "/root/miniconda3/bin/python3 -c \"\nimport json\nfiles = [\n    '/root/symb_invariant_consensus/results/sica_expanded_14b.json',\n    '/root/symb_invariant_consensus/results/exp010_mistral/exp010_results.json',\n    '/root/symb_invariant_consensus/results/exp017_strategyqa/exp017_results.json',\n    '/root/symb_invariant_consensus/results/exp018_arc/exp018_results.json',\n    '/root/symb_invariant_consensus/results/exp019_strategyqa_200/exp019_results.json',\n    '/root/symb_invariant_consensus/results/exp020_folio_200/exp020_results.json',\n]\nfor f in files:\n    d = json.load(open(f))\n    t = type(d).__name__\n    if isinstance(d, dict):\n        print(f'{f.split(\\\"/\\\")[-1]}: dict, top_keys={sorted(d.keys())[:15]}')\n        for k, v in list(d.items())[:3]:\n            vt = type(v).__name__\n            if isinstance(v, list):\n                print(f'  {k}: list[{len(v)}]')\n                if v:\n                    print(f'    [0] type={type(v[0]).__name__}')\n            elif isinstance(v, dict):\n                print(f'  {k}: dict keys={sorted(v.keys())[:10]}')\n            else:\n                print(f'  {k}: {vt} = {str(v)[:100]}')\n    elif isinstance(d, list):\n        print(f'{f.split(\\\"/\\\")[-1]}: list[{len(d)}], [0] type={type(d[0]).__name__}')\n    else:\n        print(f'{f.split(\\\"/\\\")[-1]}: {t}')\n    print()\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-17T11:35:16.112602+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"sica_expanded_14b.json: dict, top_keys=['results', 'summary']\\n  summary: dict keys=['answer_extraction_counts', 'answer_extraction_rate', 'contradiction_rate', 'extraction_rate', 'k', 'mode', 'n_problems', 'per_dataset_accuracy', 'per_level_accuracy', 'problems_with_contradictions']\\n  results: list[804]\\n    [0] type=dict\\n\\nexp010_results.json: dict, top_keys=['results', 'summary']\\n  summary: dict keys=['answer_extraction_counts', 'answer_extraction_rate', 'contradiction_rate', 'extraction_rate', 'k', 'mode', 'n_problems', 'per_dataset_accuracy', 'per_level_accuracy', 'problems_with_contradictions']\\n  results: list[60]\\n    [0] type=dict\\n\\nexp017_results.json: dict, top_keys=['results', 'summary']\\n  summary: dict keys=['delta', 'k', 'mode', 'n_problems', 'sc_accuracy', 'sc_correct', 'sica_accuracy', 'sica_correct', 'temperature', 'total_wall_time_s']\\n  results: list[60]\\n    [0] type=dict\\n\\nexp018_results.json: dict, top_keys=['results', 'summary']\\n  summary: dict keys=['delta', 'k', 'mode', 'n_problems', 'sc_accuracy', 'sc_correct', 'sica_accuracy', 'sica_correct', 'temperature', 'total_wall_time_s']\\n  results: list[60]\\n    [0] type=dict\\n\\nexp019_results.json: dict, top_keys=['results', 'summary']\\n  summary: dict keys=['delta', 'k', 'mode', 'n_problems', 'sc_accuracy', 'sc_correct', 'sica_accuracy', 'sica_correct', 'temperature', 'total_wall_time_s']\\n  results: list[200]\\n    [0] type=dict\\n\\nexp020_results.json: dict, top_keys=['results', 'summary']\\n  summary: dict keys=['answer_extraction_counts', 'answer_extraction_rate', 'contradiction_rate', 'extraction_rate', 'k', 'mode', 'n_problems', 'per_dataset_accuracy', 'per_level_accuracy', 'problems_with_contradictions']\\n  results: list[204]\\n    [0] type=dict\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T11:35:16.113022+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "/root/miniconda3/bin/python3 -c \"\nimport json\nfiles = {\n    'exp001': '/root/symb_invariant_consensus/results/sica_expanded_14b.json',\n    'exp010': '/root/symb_invariant_consensus/results/exp010_mistral/exp010_results.json',\n    'exp011': '/root/symb_invariant_consensus/results/exp011_llama8b/exp011_results.json',\n    'exp017': '/root/symb_invariant_consensus/results/exp017_strategyqa/exp017_results.json',\n    'exp018': '/root/symb_invariant_consensus/results/exp018_arc/exp018_results.json',\n    'exp019': '/root/symb_invariant_consensus/results/exp019_strategyqa_200/exp019_results.json',\n    'exp020': '/root/symb_invariant_consensus/results/exp020_folio_200/exp020_results.json',\n}\nfor name, f in files.items():\n    d = json.load(open(f))\n    items = d.get('results', d if isinstance(d, list) else [])\n    if not items:\n        print(f'{name}: no results')\n        continue\n    all_keys = set()\n    for item in items:\n        all_keys.update(item.keys())\n    print(f'{name} (n={len(items)}): {sorted(all_keys)}')\n    # Show one sample item briefly\n    sample = items[0]\n    for k, v in sample.items():\n        vstr = str(v)\n        if len(vstr) > 120:\n            vstr = vstr[:120] + '...'\n        print(f'  {k}: {type(v).__name__} = {vstr}')\n    print()\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "/root/miniconda3/bin/python3 -c \"\nimport json\nfiles = {\n    'exp001': '/root/symb_invariant_consensus/results/sica_expanded_14b.json',\n    'exp010': '/root/symb_invariant_consensus/results/exp010_mistral/exp010_results.json',\n    'exp011': '/root/symb_invariant_consensus/results/exp011_llama8b/exp011_results.json',\n    'exp017': '/root/symb_invariant_consensus/results/exp017_strategyqa/exp017_results.json',\n    'exp018': '/root/symb_invariant_consensus/results/exp018_arc/exp018_results.json',\n    'exp019': '/root/symb_invariant_consensus/results/exp019_strategyqa_200/exp019_results.json',\n    'exp020': '/root/symb_invariant_consensus/results/exp020_folio_200/exp020_results.json',\n}\nfor name, f in files.items():\n    d = json.load(open(f))\n    items = d.get('results', d if isinstance(d, list) else [])\n    if not items:\n        print(f'{name}: no results')\n        continue\n    all_keys = set()\n    for item in items:\n        all_keys.update(item.keys())\n    print(f'{name} (n={len(items)}): {sorted(all_keys)}')\n    # Show one sample item briefly\n    sample = items[0]\n    for k, v in sample.items():\n        vstr = str(v)\n        if len(vstr) > 120:\n            vstr = vstr[:120] + '...'\n        print(f'  {k}: {type(v).__name__} = {vstr}')\n    print()\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-17T11:35:16.113269+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"exp001 (n=804): ['constraints_stats', 'dataset', 'ground_truth', 'level', 'maxsat_stats', 'per_trace', 'problem', 'problem_id', 'problem_idx', 'raw_constraints', 'sc_answer', 'sc_correct', 'sc_vote_count', 'sc_vote_distribution', 'sica_answer', 'sica_correct', 'sica_scores', 'timing', 'trace_extraction_stats', 'truncated_traces', 'wall_time_s']\\n  problem_idx: int = 0\\n  problem_id: str = ProofWriter_AttNoneg-OWA-D5-1041_Q1\\n  problem: str = Given the following facts and rules:\\nBob is cold. Bob is quiet. Bob is red. Bob is smart. Charlie is kind. Charlie is qu...\\n  dataset: str = proofwriter\\n  level: str = D5\\n  ground_truth: str = True\\n  sica_answer: str = True\\n  sica_scores: dict = {'True': 75.0}\\n  sica_correct: bool = True\\n  sc_answer: str = True\\n  sc_vote_count: int = 12\\n  sc_vote_distribution: dict = {'True': 12}\\n  sc_correct: bool = True\\n  constraints_stats: dict = {'total_extracted': 75, 'traces_with_constraints': 12, 'unique_after_dedup': 16}\\n  maxsat_stats: dict = {'satisfied': 16, 'excluded': 0, 'total_weight': 75, 'solve_time_ms': 0.9229059796780348}\\n  timing: dict = {'trace_gen_s': 18.991, 'extraction_s': 17.003, 'dedup_s': 0.409, 'maxsat_s': 0.003, 'total_s': 36.406}\\n  wall_time_s: float = 36.41\\n  trace_extraction_stats: dict = {'boxed': 12, 'fallback': 0, 'none': 0}\\n  truncated_traces: int = 0\\n  raw_constraints: list = []\\n  per_trace: list = [{'trace_idx': 0, 'answer': 'True', 'finish_reason': 'stop', 'extraction_method': 'boxed', 'trace_len': 426}, {'trace_id...\\n\\nexp010 (n=60): ['constraints_stats', 'dataset', 'ground_truth', 'level', 'maxsat_stats', 'per_trace', 'problem', 'problem_id', 'problem_idx', 'raw_constraints', 'sc_answer', 'sc_correct', 'sc_vote_count', 'sc_vote_distribution', 'sica_answer', 'sica_correct', 'sica_scores', 'timing', 'trace_extraction_stats', 'truncated_traces', 'wall_time_s']\\n  problem_idx: int = 0\\n  problem_id: str = Proo
…[truncated 6460 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-17T11:35:16.113791+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "cat > /root/symb_invariant_consensus/results/compute_quality_metrics.py << 'PYEOF'\nimport json, csv, os\nimport numpy as np\n\nEXPERIMENTS = {\n    'exp001_qwen14b_pw_folio': {\n        'path': '/root/symb_invariant_consensus/results/sica_expanded_14b.json',\n        'model': 'Qwen2.5-14B', 'domain': 'PW+FOLIO',\n    },\n    'exp010_mistral7b_pw_folio': {\n        'path': '/root/symb_invariant_consensus/results/exp010_mistral/exp010_results.json',\n        'model': 'Mistral-7B', 'domain': 'PW+FOLIO',\n    },\n    'exp011_llama8b_pw_folio': {\n        'path': '/root/symb_invariant_consensus/results/exp011_llama8b/exp011_results.json',\n        'model': 'LLaMA-8B', 'domain': 'PW+FOLIO',\n    },\n    'exp017_qwen14b_strategyqa': {\n        'path': '/root/symb_invariant_consensus/results/exp017_strategyqa/exp017_results.json',\n        'model': 'Qwen2.5-14B', 'domain': 'StrategyQA',\n    },\n    'exp018_qwen14b_arc': {\n        'path': '/root/symb_invariant_consensus/results/exp018_arc/exp018_results.json',\n        'model': 'Qwen2.5-14B', 'domain': 'ARC',\n    },\n    'exp019_llama8b_strategyqa': {\n        'path': '/root/symb_invariant_consensus/results/exp019_strategyqa_200/exp019_results.json',\n        'model': 'LLaMA-8B', 'domain': 'StrategyQA',\n    },\n    'exp020_llama8b_folio': {\n        'path': '/root/symb_invariant_consensus/results/exp020_folio_200/exp020_results.json',\n        'model': 'LLaMA-8B', 'domain': 'FOLIO',\n    },\n}\n\nrows = []\n\nfor exp_name, meta in EXPERIMENTS.items():\n    fpath = meta['path']\n    if not os.path.exists(fpath):\n        print(f\"SKIP {exp_name}: not found\")\n        continue\n\n    raw = json.load(open(fpath))\n    items = raw.get('results', raw if isinstance(raw, list) else [])\n    summary = raw.get('summary', {})\n    n = len(items)\n    if n == 0:\n        print(f\"SKIP {exp_name}: empty\")\n        continue\n\n    model = meta['model']\n    domain = meta['domain']\n\n    # Accuracy\n    sica_correct = sum(1 for x in items if x.get('sica_correct'))\n    sc_correct = sum(1 for x in items if x.get('sc_correct'))\n    sica_acc = sica_correct / n\n    sc_acc = sc_correct / n\n    delta_pp = 100 * (sica_acc - sc_acc)\n\n    # Multi-candidate rate: SICA disagrees with SC\n    c0 = sum(1 for x in items if x.get('sica_answer') != x.get('sc_answer')) / n\n\n    # Constraint quality from constraints_stats\n    cs_list = [x['constraints_stats'] for x in items if isinstance(x.get('constraints_stats'), dict)]\n    avg_total_extracted = np.mean([s['total_extracted'] for s in cs_list]) if cs_list else None\n    avg_unique = np.mean([s['unique_after_dedup'] for s in cs_list]) if cs_list else None\n    avg_traces_with = np.mean([s['traces_with_constraints'] for s in cs_list]) if cs_list else None\n\n    # MaxSAT quality\n    ms_list = [x['maxsat_stats'] for x in items if isinstance(x.get('maxsat_stats'), dict)]\n    avg_satisfied = np.mean([s['satisfied'] for s in ms_list]) if ms_list else None\n    avg_excluded = np.mean([s['excluded'] for s in ms_list]) if ms_list else None\n    # Satisfied ratio = satisfied / (satisfied + excluded) per item, then average\n    sat_ratios = []\n    for s in ms_list:\n        total = s['satisfied'] + s['excluded']\n        if total > 0:\n            sat_ratios.append(s['satisfied'] / total)\n    avg_sat_ratio = np.mean(sat_ratios) if sat_ratios else None\n\n    # Dedup ratio = unique / total_extracted\n    dedup_ratios = []\n    for s in cs_list:\n        if s['total_extracted'] > 0:\n            dedup_ratios.append(s['unique_after_dedup'] / s['total_extracted'])\n    avg_dedup_ratio = np.mean(dedup_ratios) if dedup_ratios else None\n\n    # Constraint density = total_extracted / traces_with_constraints\n    density_vals = []\n    for s in cs_list:\n        if s['traces_with_constraints'] > 0:\n            density_vals.append(s['total_extracted'] / s['traces_with_constraints'])\n    avg_density = np.mean(density_vals) if density_vals else None\n\n    # Discordant\n    sica_wins = sum(1 for x in items if x.get('sica_correct') and not x.get('sc_correct'))\n    sc_wins = sum(1 for x in items if x.get('sc_correct') and not x.get('sica_correct'))\n    both_correct = sum(1 for x in items if x.get('sica_correct') and x.get('sc_correct'))\n    both_wrong = sum(1 for x in items if not x.get('sica_correct') and not x.get('sc_correct'))\n\n    def fmt(v, decimals=4):\n        if v is None:\n            return ''\n        return round(float(v), decimals)\n\n    row = {\n        'experiment': exp_name,\n        'model': model,\n        'domain': domain,\n        'n': n,\n        'sc_acc': fmt(sc_acc),\n        'sica_acc': fmt(sica_acc),\n        'delta_pp': fmt(delta_pp, 2),\n        'c0_disagree_rate': fmt(c0),\n        'avg_total_extracted': fmt(avg_total_extracted, 1),\n        'avg_unique_constraints': fmt(avg_unique, 1),\n        'avg_traces_with_constraints': fmt(avg_traces_with, 1),\n        'avg_satisfied': fmt(avg_satisfied, 1),\n        'avg_excluded': fmt(avg_excluded, 1),\n        'avg_satisfied_ratio': fmt(avg_sat_ratio),\n        'avg_dedup_ratio': fmt(avg_dedup_ratio),\n        'avg_constraint_density': fmt(avg_density, 2),\n        'sica_wins': sica_wins,\n        'sc_wins': sc_wins,\n        'both_correct': both_correct,\n        'both_wrong': both_wrong,\n    }\n    rows.append(row)\n\n# Save CSV\noutdir = '/root/symb_invariant_consensus/results/constraint_quality_correlation/'\nos.makedirs(outdir, exist_ok=True)\noutpath = outdir + 'quality_metrics.csv'\nwith open(outpath, 'w', newline='') as fout:\n    writer = csv.DictWriter(fout, fieldnames=rows[0].keys())\n    writer.writeheader()\n    writer.writerows(rows)\nprint(f\"Saved {len(rows)} rows to {outpath}\\n\")\n\n# Print full table\nprint(f\"{'Experiment':<35} {'Model':<14} {'Domain':<12} {'N':>4} {'SC':>7} {'SICA':>7} {'Δpp':>7} {'C0':>7} {'Uniq':>6} {'Sat':>6} {'Excl':>5} {'SatR':>6} {'DedR':>6} {'Dens':>6} {'S>C':>4} {'C>S':>4}\")\nprint('-' * 160)\nfor r in rows:\n    print(f\"{r['experiment']:<35} {r['model']:<14} {r['domain']:<12} {r['n']:>4} {r['sc_acc']:>7} {r['sica_acc']:>7} {r['delta_pp']:>7} {r['c0_disagree_rate']:>7} {str(r['avg_unique_constraints']):>6} {str(r['avg_satisfied']):>6} {str(r['avg_excluded']):>5} {str(r['avg_satisfied_ratio']):>6} {str(r['avg_dedup_ratio']):>6} {str(r['avg_constraint_density']):>6} {r['sica_wins']:>4} {r['sc_wins']:>4}\")\n\n# Also print a readable summary\nprint(f\"\\n{'='*80}\")\nprint(\"SUMMARY BY (MODEL, DOMAIN)\")\nprint(f\"{'='*80}\")\nfor r in rows:\n    print(f\"\\n{r['model']} / {r['domain']} (n={r['n']})\")\n    print(f\"  Accuracy: SC={r['sc_acc']}, SICA={r['sica_acc']}, Δ={r['delta_pp']}pp\")\n    print(f\"  C0 (disagree): {r['c0_disagree_rate']}\")\n    print(f\"  Constraints: total_extr={r['avg_total_extracted']}, unique={r['avg_unique_constraints']}, density={r['avg_constraint_density']}\")\n    print(f\"  MaxSAT: satisfied={r['avg_satisfied']}, excluded={r['avg_excluded']}, sat_ratio={r['avg_satisfied_ratio']}, dedup_ratio={r['avg_dedup_ratio']}\")\n    print(f\"  Discordant: SICA_wins={r['sica_wins']}, SC_wins={r['sc_wins']}, both_correct={r['both_correct']}, both_wrong={r['both_wrong']}\")\nPYEOF\n/root/miniconda3/bin/python3 /root/symb_invariant_consensus/results/compute_quality_metrics.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "cat > /root/symb_invariant_consensus/results/compute_quality_metrics.py << 'PYEOF'\nimport json, csv, os\nimport numpy as np\n\nEXPERIMENTS = {\n    'exp001_qwen14b_pw_folio': {\n        'path': '/root/symb_invariant_consensus/results/sica_expanded_14b.json',\n        'model': 'Qwen2.5-14B', 'domain': 'PW+FOLIO',\n    },\n    'exp010_mistral7b_pw_folio': {\n        'path': '/root/symb_invariant_consensus/results/exp010_mistral/exp010_results.json',\n        'model': 'Mistral-7B', 'domain': 'PW+FOLIO',\n    },\n    'exp011_llama8b_pw_folio': {\n        'path': '/root/symb_invariant_consensus/results/exp011_llama8b/exp011_results.json',\n        'model': 'LLaMA-8B', 'domain': 'PW+FOLIO',\n    },\n    'exp017_qwen14b_strategyqa': {\n        'path': '/root/symb_invariant_consensus/results/exp017_strategyqa/exp017_results.json',\n        'model': 'Qwen2.5-14B', 'domain': 'StrategyQA',\n    },\n    'exp018_qwen14b_arc': {\n        'path': '/root/symb_invariant_consensus/results/exp018_arc/exp018_results.json',\n        'model': 'Qwen2.5-14B', 'domain': 'ARC',\n    },\n    'exp019_llama8b_strategyqa': {\n        'path': '/root/symb_invariant_consensus/results/exp019_strategyqa_200/exp019_results.json',\n        'model': 'LLaMA-8B', 'domain': 'StrategyQA',\n    },\n    'exp020_llama8b_folio': {\n        'path': '/root/symb_invariant_consensus/results/exp020_folio_200/exp020_results.json',\n        'model': 'LLaMA-8B', 'domain': 'FOLIO',\n    },\n}\n\nrows = []\n\nfor exp_name, meta in EXPERIMENTS.items():\n    fpath = meta['path']\n    if not os.path.exists(fpath):\n        print(f\"SKIP {exp_name}: not found\")\n        continue\n\n    raw = json.load(open(fpath))\n    items = raw.get('results', raw if isinstance(raw, list) else [])\n    summary = raw.get('summary', {})\n    n = len(items)\n    if n == 0:\n        print(f\"SKIP {exp_name}: empty\")\n        continue\n\n    model = meta['model']\n    domain = meta['domain']\n\n    # Accuracy\n    sica_correct = sum(1 for x in items if x.get('sica_correct'))\n    sc_correct = sum(1 for x in items if x.get('sc_correct'))\n    sica_acc = sica_correct / n\n    sc_acc = sc_correct / n\n    delta_pp = 100 * (sica_acc - sc_acc)\n\n    # Multi-candidate rate: SICA disagrees with SC\n    c0 = sum(1 for x in items if x.get('sica_answer') != x.get('sc_answer')) / n\n\n    # Constraint quality from constraints_stats\n    cs_list = [x['constraints_stats'] for x in items if isinstance(x.get('constraints_stats'), dict)]\n    avg_total_extracted = np.mean([s['total_extracted'] for s in cs_list]) if cs_list else None\n    avg_unique = np.mean([s['unique_after_dedup'] for s in cs_list]) if cs_list else None\n    avg_traces_with = np.mean([s['traces_with_constraints'] for s in cs_list]) if cs_list else None\n\n    # MaxSAT quality\n    ms_list = [x['maxsat_stats'] for x in items if isinstance(x.get('maxsat_stats'), dict)]\n    avg_satisfied = np.mean([s['satisfied'] for s in ms_list]) if ms_list else None\n    avg_excluded = np.mean([s['excluded'] for s in ms_list]) if ms_list else None\n    # Satisfied ratio = satisfied / (satisfied + excluded) per item, then average\n    sat_ratios = []\n    for s in ms_list:\n        total = s['satisfied'] + s['excluded']\n        if total > 0:\n            sat_ratios.append(s['satisfied'] / total)\n    avg_sat_ratio = np.mean(sat_ratios) if sat_ratios else None\n\n    # Dedup ratio = unique / total_extracted\n    dedup_ratios = []\n    for s in cs_list:\n        if s['total_extracted'] > 0:\n            dedup_ratios.append(s['unique_after_dedup'] / s['total_extracted'])\n    avg_dedup_ratio = np.mean(dedup_ratios) if dedup_ratios else None\n\n    # Constraint density = total_extracted / traces_with_constraints\n    density_vals = []\n    for s in cs_list:\n        if s['traces_with_constraints'] > 0:\n            density_vals.append(s['total_extracted'] / s['traces_with_constraints'])\n    avg_density = np.mean(density_vals) if density_vals else None\n\n    # Discordant\n    sica_wins = sum(1 for x in items if x.get('sica_correct') and not x.get('sc_correct'))\n    sc_wins = sum(1 for x in items if x.get('sc_correct') and not x.get('sica_correct'))\n    both_correct = sum(1 for x in items if x.get('sica_correct') and x.get('sc_correct'))\n    both_wrong = sum(1 for x in items if not x.get('sica_correct') and not x.get('sc_correct'))\n\n    def fmt(v, decimals=4):\n        if v is None:\n            return ''\n        return round(float(v), decimals)\n\n    row = {\n        'experiment': exp_name,\n        'model': model,\n        'domain': domain,\n        'n': n,\n        'sc_acc': fmt(sc_acc),\n        'sica_acc': fmt(sica_acc),\n        'delta_pp': fmt(delta_pp, 2),\n        'c0_disagree_rate': fmt(c0),\n        'avg_total_extracted': fmt(avg_total_extracted, 1),\n        'avg_unique_constraints': fmt(avg_unique, 1),\n        'avg_traces_with_constraints': fmt(avg_traces_with, 1),\n        'avg_satisfied': fmt(avg_satisfied, 1),\n        'avg_excluded': fmt(avg_excluded, 1),\n        'avg_satisfied_ratio': fmt(avg_sat_ratio),\n        'avg_dedup_ratio': fmt(avg_dedup_ratio),\n        'avg_constraint_density': fmt(avg_density, 2),\n        'sica_wins': sica_wins,\n        'sc_wins': sc_wins,\n        'both_correct': both_correct,\n        'both_wrong': both_wrong,\n    }\n    rows.append(row)\n\n# Save CSV\noutdir = '/root/symb_invariant_consensus/results/constraint_quality_correlation/'\nos.makedirs(outdir, exist_ok=True)\noutpath = outdir + 'quality_metrics.csv'\nwith open(outpath, 'w', newline='') as fout:\n    writer = csv.DictWriter(fout, fieldnames=rows[0].keys())\n    writer.writeheader()\n    writer.writerows(rows)\nprint(f\"Saved {len(rows)} rows to {outpath}\\n\")\n\n# Print full table\nprint(f\"{'Experiment':<35} {'Model':<14} {'Domain':<12} {'N':>4} {'SC':>7} {'SICA':>7} {'Δpp':>7} {'C0':>7} {'Uniq':>6} {'Sat':>6} {'Excl':>5} {'SatR':>6} {'DedR':>6} {'Dens':>6} {'S>C':>4} {'C>S':>4}\")\nprint('-' * 160)\nfor r in rows:\n    print(f\"{r['experiment']:<35} {r['model']:<14} {r['domain']:<12} {r['n']:>4} {r['sc_acc']:>7} {r['sica_acc']:>7} {r['delta_pp']:>7} {r['c0_disagree_rate']:>7} {str(r['avg_unique_constraints']):>6} {str(r['avg_satisfied']):>6} {str(r['avg_excluded']):>5} {str(r['avg_satisfied_ratio']):>6} {str(r['avg_dedup_ratio']):>6} {str(r['avg_constraint_density']):>6} {r['sica_wins']:>4} {r['sc_wins']:>4}\")\n\n# Also print a readable summary\nprint(f\"\\n{'='*80}\")\nprint(\"SUMMARY BY (MODEL, DOMAIN)\")\nprint(f\"{'='*80}\")\nfor r in rows:\n    print(f\"\\n{r['model']} / {r['domain']} (n={r['n']})\")\n    print(f\"  Accuracy: SC={r['sc_acc']}, SICA={r['sica_acc']}, Δ={r['delta_pp']}pp\")\n    print(f\"  C0 (disagree): {r['c0_disagree_rate']}\")\n    print(f\"  Constraints: total_extr={r['avg_total_extracted']}, unique={r['avg_unique_constraints']}, density={r['avg_constraint_density']}\")\n    print(f\"  MaxSAT: satisfied={r['avg_satisfied']}, excluded={r['avg_excluded']}, sat_ratio={r['avg_satisfied_ratio']}, dedup_ratio={r['avg_dedup_ratio']}\")\n    print(f\"  Discordant: SICA_wins={r['sica_wins']}, SC_wins={r['sc_wins']}, both_correct={r['both_correct']}, both_wrong={r['both_wrong']}\")\nPYEOF\n/root/miniconda3/bin/python3 /root/symb_invariant_consensus/results/compute_quality_metrics.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-17T11:35:16.114114+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Saved 7 rows to /root/symb_invariant_consensus/results/constraint_quality_correlation/quality_metrics.csv\\n\\nExperiment                          Model          Domain          N      SC    SICA     Δpp      C0   Uniq    Sat  Excl   SatR   DedR   Dens  S>C  C>S\\n----------------------------------------------------------------------------------------------------------------------------------------------------------------\\nexp001_qwen14b_pw_folio             Qwen2.5-14B    PW+FOLIO      804  0.7624  0.7649    0.25  0.0386   21.5   21.0   0.5 0.9773 0.2148   9.17   16   14\\nexp010_mistral7b_pw_folio           Mistral-7B     PW+FOLIO       60  0.4833  0.4833     0.0  0.0667   20.5   19.3   1.1 0.9477 0.2997   5.47    2    2\\nexp011_llama8b_pw_folio             LLaMA-8B       PW+FOLIO       60     0.6  0.6667    6.67  0.1167   30.1   28.5   1.6 0.9496 0.3025   8.73    5    1\\nexp017_qwen14b_strategyqa           Qwen2.5-14B    StrategyQA     60  0.5333  0.5667    3.33  0.0333    1.0    0.9   0.1 0.9537 0.1377   1.02    2    0\\nexp018_qwen14b_arc                  Qwen2.5-14B    ARC            60  0.9667    0.95   -1.67  0.0167    1.1    1.1   0.1  0.975 0.0903   1.02    0    1\\nexp019_llama8b_strategyqa           LLaMA-8B       StrategyQA    200    0.72    0.74     2.0    0.07    6.2    5.4   0.9 0.8534 0.2862   1.94    9    5\\nexp020_llama8b_folio                LLaMA-8B       FOLIO         204  0.6324  0.6078   -2.45  0.0637   33.3   31.2   2.1 0.9384 0.3423   8.05    4    9\\n\\n================================================================================\\nSUMMARY BY (MODEL, DOMAIN)\\n================================================================================\\n\\nQwen2.5-14B / PW+FOLIO (n=804)\\n  Accuracy: SC=0.7624, SICA=0.7649, Δ=0.25pp\\n  C0 (disagree): 0.0386\\n  Constraints: total_extr=110.0, unique=21.5, density=9.17\\n  MaxSAT: satisfied=21.0, excluded=0.5, sat_ratio=0.9773, dedup_ratio=
…[truncated 2067 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-17T11:35:16.114315+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "cat /root/symb_invariant_consensus/results/constraint_quality_correlation/quality_metrics.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "cat /root/symb_invariant_consensus/results/constraint_quality_correlation/quality_metrics.csv",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-17T11:35:16.114469+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"experiment,model,domain,n,sc_acc,sica_acc,delta_pp,c0_disagree_rate,avg_total_extracted,avg_unique_constraints,avg_traces_with_constraints,avg_satisfied,avg_excluded,avg_satisfied_ratio,avg_dedup_ratio,avg_constraint_density,sica_wins,sc_wins,both_correct,both_wrong\\r\\nexp001_qwen14b_pw_folio,Qwen2.5-14B,PW+FOLIO,804,0.7624,0.7649,0.25,0.0386,110.0,21.5,12.0,21.0,0.5,0.9773,0.2148,9.17,16,14,599,175\\r\\nexp010_mistral7b_pw_folio,Mistral-7B,PW+FOLIO,60,0.4833,0.4833,0.0,0.0667,65.7,20.5,12.0,19.3,1.1,0.9477,0.2997,5.47,2,2,27,29\\r\\nexp011_llama8b_pw_folio,LLaMA-8B,PW+FOLIO,60,0.6,0.6667,6.67,0.1167,101.0,30.1,11.6,28.5,1.6,0.9496,0.3025,8.73,5,1,35,19\\r\\nexp017_qwen14b_strategyqa,Qwen2.5-14B,StrategyQA,60,0.5333,0.5667,3.33,0.0333,8.6,1.0,8.4,0.9,0.1,0.9537,0.1377,1.02,2,0,32,26\\r\\nexp018_qwen14b_arc,Qwen2.5-14B,ARC,60,0.9667,0.95,-1.67,0.0167,12.3,1.1,12.0,1.1,0.1,0.975,0.0903,1.02,0,1,57,2\\r\\nexp019_llama8b_strategyqa,LLaMA-8B,StrategyQA,200,0.72,0.74,2.0,0.07,19.9,6.2,9.6,5.4,0.9,0.8534,0.2862,1.94,9,5,139,47\\r\\nexp020_llama8b_folio,LLaMA-8B,FOLIO,204,0.6324,0.6078,-2.45,0.0637,96.0,33.3,11.9,31.2,2.1,0.9384,0.3423,8.05,4,9,120,71\\r\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-17T11:35:16.114619+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts",
  "description": "Create local artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts",
    "description": "Create local artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-17T11:35:16.114746+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-17T11:35:16.114888+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/quality_metrics.csv",
  "content": "experiment,model,domain,n,sc_acc,sica_acc,delta_pp,c0_disagree_rate,avg_total_extracted,avg_unique_constraints,avg_traces_with_constraints,avg_satisfied,avg_excluded,avg_satisfied_ratio,avg_dedup_ratio,avg_constraint_density,sica_wins,sc_wins,both_correct,both_wrong\nexp001_qwen14b_pw_folio,Qwen2.5-14B,PW+FOLIO,804,0.7624,0.7649,0.25,0.0386,110.0,21.5,12.0,21.0,0.5,0.9773,0.2148,9.17,16,14,599,175\nexp010_mistral7b_pw_folio,Mistral-7B,PW+FOLIO,60,0.4833,0.4833,0.0,0.0667,65.7,20.5,12.0,19.3,1.1,0.9477,0.2997,5.47,2,2,27,29\nexp011_llama8b_pw_folio,LLaMA-8B,PW+FOLIO,60,0.6,0.6667,6.67,0.1167,101.0,30.1,11.6,28.5,1.6,0.9496,0.3025,8.73,5,1,35,19\nexp017_qwen14b_strategyqa,Qwen2.5-14B,StrategyQA,60,0.5333,0.5667,3.33,0.0333,8.6,1.0,8.4,0.9,0.1,0.9537,0.1377,1.02,2,0,32,26\nexp018_qwen14b_arc,Qwen2.5-14B,ARC,60,0.9667,0.95,-1.67,0.0167,12.3,1.1,12.0,1.1,0.1,0.975,0.0903,1.02,0,1,57,2\nexp019_llama8b_strategyqa,LLaMA-8B,StrategyQA,200,0.72,0.74,2.0,0.07,19.9,6.2,9.6,5.4,0.9,0.8534,0.2862,1.94,9,5,139,47\nexp020_llama8b_folio,LLaMA-8B,FOLIO,204,0.6324,0.6078,-2.45,0.0637,96.0,33.3,11.9,31.2,2.1,0.9384,0.3423,8.05,4,9,120,71\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/quality_metrics.csv",
    "content": "experiment,model,domain,n,sc_acc,sica_acc,delta_pp,c0_disagree_rate,avg_total_extracted,avg_unique_constraints,avg_traces_with_constraints,avg_satisfied,avg_excluded,avg_satisfied_ratio,avg_dedup_ratio,avg_constraint_density,sica_wins,sc_wins,both_correct,both_wrong\nexp001_qwen14b_pw_folio,Qwen2.5-14B,PW+FOLIO,804,0.7624,0.7649,0.25,0.0386,110.0,21.5,12.0,21.0,0.5,0.9773,0.2148,9.17,16,14,599,175\nexp010_mistral7b_pw_folio,Mistral-7B,PW+FOLIO,60,0.4833,0.4833,0.0,0.0667,65.7,20.5,12.0,19.3,1.1,0.9477,0.2997,5.47,2,2,27,29\nexp011_llama8b_pw_folio,LLaMA-8B,PW+FOLIO,60,0.6,0.6667,6.67,0.1167,101.0,30.1,11.6,28.5,1.6,0.9496,0.3025,8.73,5,1,35,19\nexp017_qwen14b_strategyqa,Qwen2.5-14B,StrategyQA,60,0.5333,0.5667,3.33,0.0333,8.6,1.0,8.4,0.9,0.1,0.9537,0.1377,1.02,2,0,32,26\nexp018_qwen14b_arc,Qwen2.5-14B,ARC,60,0.9667,0.95,-1.67,0.0167,12.3,1.1,12.0,1.1,0.1,0.975,0.0903,1.02,0,1,57,2\nexp019_llama8b_strategyqa,LLaMA-8B,StrategyQA,200,0.72,0.74,2.0,0.07,19.9,6.2,9.6,5.4,0.9,0.8534,0.2862,1.94,9,5,139,47\nexp020_llama8b_folio,LLaMA-8B,FOLIO,204,0.6324,0.6078,-2.45,0.0637,96.0,33.3,11.9,31.2,2.1,0.9384,0.3423,8.05,4,9,120,71\n"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-17T11:35:16.115028+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/quality_metrics.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-17T11:35:16.115180+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-17T11:35:16.115297+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-17T11:35:16.115449+00:00_

CSV 已保存到服务器 `/root/symb_invariant_consensus/results/constraint_quality_correlation/quality_metrics.csv` 和本地 `artifacts/quality_metrics.csv`。

**汇总表：**

| Model | Domain | N | SC | SICA | Δpp | C0 | Unique | Density | SatR | SICA>SC | SC>SICA |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Qwen2.5-14B | PW+FOLIO | 804 | 76.24 | 76.49 | +0.25 | 3.9% | 21.5 | 9.17 | 0.977 | 16 | 14 |
| Mistral-7B | PW+FOLIO | 60 | 48.33 | 48.33 | 0.0 | 6.7% | 20.5 | 5.47 | 0.948 | 2 | 2 |
| LLaMA-8B | PW+FOLIO | 60 | 60.0 | 66.67 | **+6.67** | 11.7% | 30.1 | 8.73 | 0.950 | 5 | 1 |
| Qwen2.5-14B | StrategyQA | 60 | 53.33 | 56.67 | +3.33 | 3.3% | 1.0 | 1.02 | 0.954 | 2 | 0 |
| Qwen2.5-14B | ARC | 60 | 96.67 | 95.0 | -1.67 | 1.7% | 1.1 | 1.02 | 0.975 | 0 | 1 |
| LLaMA-8B | StrategyQA | 200 | 72.0 | 74.0 | +2.0 | 7.0% | 6.2 | 1.94 | 0.853 | 9 | 5 |
| LLaMA-8B | FOLIO | 204 | 63.24 | 60.78 | -2.45 | 6.4% | 33.3 | 8.05 | 0.938 | 4 | 9 |

**F2 相关观察：**
- 逻辑推理域（PW+FOLIO, FOLIO）的约束密度高（5~9 constraints/trace），去重后 unique 多（20~33）
- 常识推理域（StrategyQA, ARC）约束密度极低（~1），几乎无法提取有意义的符号约束
- SICA 在高约束密度 + 中等 C0 时增益最大（LLaMA-8B PW+FOLIO: +6.67pp）；约束稀疏时增益有限或为负（ARC: -1.67pp, FOLIO-only: -2.45pp）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_constraint-quality-correlation_20260517T113142"
}
```

</details>

---
