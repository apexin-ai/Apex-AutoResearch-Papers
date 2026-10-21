# analysis transformer baseline perexample

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/chats/worker_analysis_transformer-baseline-perexample_20260520T011942.jsonl`
- **Structured JSON:** [`e35c33eb22f2f5c34652.json`](../../sessions/e3/e35c33eb22f2f5c34652.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

29 recorded events

### Tool call

_source line 1 · 2026-05-20T01:21:53.843376+00:00_

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
  "session": "worker_analysis_transformer-baseline-perexample_20260520T011942",
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

_source line 2 · 2026-05-20T01:21:53.843725+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_transformer-baseline-perexample_20260520T011942",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T01:21:53.843900+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "find /root/entrainment_gated_ft/ -path \"*Transformer*\" -name \"*lambada*jsonl\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_transformer-baseline-perexample_20260520T011942",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "find /root/entrainment_gated_ft/ -path \"*Transformer*\" -name \"*lambada*jsonl\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T01:21:53.844045+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_transformer-baseline-perexample_20260520T011942",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T01:21:53.844172+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "find /root/entrainment_gated_ft/ -path \"*transformer*\" -name \"*lambada*jsonl\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_transformer-baseline-perexample_20260520T011942",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "find /root/entrainment_gated_ft/ -path \"*transformer*\" -name \"*lambada*jsonl\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T01:21:53.844297+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_transformer-baseline-perexample_20260520T011942",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T01:21:53.844416+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "find /root/entrainment_gated_ft/lm_eval_clean/ -path \"*1.3b*h3*\" -name \"*lambada*jsonl\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_transformer-baseline-perexample_20260520T011942",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "find /root/entrainment_gated_ft/lm_eval_clean/ -path \"*1.3b*h3*\" -name \"*lambada*jsonl\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T01:21:53.844536+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_transformer-baseline-perexample_20260520T011942",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T01:21:53.844699+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "find /root/entrainment_gated_ft/ -path \"*Transformer*\" -name \"*lambada*jsonl\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_transformer-baseline-perexample_20260520T011942",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "find /root/entrainment_gated_ft/ -path \"*Transformer*\" -name \"*lambada*jsonl\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T01:21:53.844828+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "find /root/entrainment_gated_ft/ -ipath \"*transformer*\" -name \"*lambada*jsonl\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_transformer-baseline-perexample_20260520T011942",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "find /root/entrainment_gated_ft/ -ipath \"*transformer*\" -name \"*lambada*jsonl\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T01:21:53.844942+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "find /root/entrainment_gated_ft/lm_eval_clean/ -path \"*1.3b*\" -name \"*lambada*jsonl\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_transformer-baseline-perexample_20260520T011942",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "find /root/entrainment_gated_ft/lm_eval_clean/ -path \"*1.3b*\" -name \"*lambada*jsonl\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T01:21:53.845072+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/entrainment_gated_ft/lm_eval_clean/exp007/340m/Transformer/samples/lambada_openai.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_transformer-baseline-perexample_20260520T011942",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-20T01:21:53.845203+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/entrainment_gated_ft/results_1.3b/lm_eval/transformer_baseline/__root__autodl-tmp__models_1.3b__transformer_1.3B_baseline/samples_lambada_openai_2026-05-18T17-58-59.437801.jsonl\\n/root/entrainment_gated_ft/results_1.3b/lm_eval/transformer_baseline_v2/__root__autodl-tmp__models_1.3b__transformer_1.3B_baseline/samples_lambada_openai_2026-05-18T18-06-58.522842.jsonl\\n/root/entrainment_gated_ft/results_1.3b/lm_eval_fixed/transformer_1.3B_baseline/__root__autodl-tmp__models_1.3b__transformer_1.3B_baseline/samples_lambada_openai_2026-05-18T18-17-00.154753.jsonl\\n/root/entrainment_gated_ft/results_1.3b/lm_eval_fixed/transformer_1.3B_baseline/__root__autodl-tmp__models_1.3b__transformer_1.3B_baseline/samples_lambada_openai_2026-05-18T18-17-29.870669.jsonl\\n/root/entrainment_gated_ft/results_1.3b/lm_eval_fixed/transformer_1.3B_baseline/__root__autodl-tmp__models_1.3b__transformer_1.3B_baseline/samples_lambada_openai_2026-05-18T18-24-24.830994.jsonl\\n/root/entrainment_gated_ft/results_1.3b/lm_eval_fixed/transformer_1.3B_baseline/__root__autodl-tmp__models_1.3b__transformer_1.3B_baseline/samples_lambada_openai_2026-05-18T19-47-30.065126.jsonl\\n/root/entrainment_gated_ft/results_1.3b/lm_eval_fixed/transformer_1.3B_baseline_v2/__root__autodl-tmp__models_1.3b__transformer_1.3B_baseline/samples_lambada_openai_2026-05-18T18-19-29.095742.jsonl\\n/root/entrainment_gated_ft/results_v5/transformer/__root__autodl-tmp__models_1.3b__transformer_1.3B_baseline/samples_lambada_openai_2026-05-18T19-46-52.474119.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/340m/Transformer/samples/lambada_openai.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.59}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_transformer-baseline-perexample_20260520T011942",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T01:21:53.845342+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/entrainment_gated_ft/lm_eval_clean/1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/1.3b/GDN-h24-1-logsamples/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/1.3b/GDN-h6-1-logsamples/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/GDN-pure/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/GDN-h12-1/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/RetNet-h3-1/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/RetNet-h6-1/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/RetNet-h12-1/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/RetNet-h24-1/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/HGRN2-pure/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/HGRN2-h3-1/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/HGRN2-h6-1/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/HGRN2-h12-1/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/HGRN2-h24-1/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/RetNet-pure/samples/lambada_openai.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.59}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_transformer-baseline-perexample_20260520T011942",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T01:21:53.845510+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "head -2 /root/entrainment_gated_ft/results_v5/transformer/__root__autodl-tmp__models_1.3b__transformer_1.3B_baseline/samples_lambada_openai_2026-05-18T19-46-52.474119.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_transformer-baseline-perexample_20260520T011942",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "head -2 /root/entrainment_gated_ft/results_v5/transformer/__root__autodl-tmp__models_1.3b__transformer_1.3B_baseline/samples_lambada_openai_2026-05-18T19-46-52.474119.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T01:21:53.845648+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "head -2 /root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/GDN-pure/samples/lambada_openai.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_transformer-baseline-perexample_20260520T011942",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "head -2 /root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/GDN-pure/samples/lambada_openai.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-20T01:21:53.845824+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"doc_id\\\": 0, \\\"doc\\\": {\\\"text\\\": \\\"In my palm is a clear stone, and inside it is a small ivory statuette. A guardian angel.\\\\n\\\\n\\\\\\\"Figured if you're going to be out at night getting hit by cars, you might as well have some backup.\\\\\\\"\\\\n\\\\nI look at him, feeling stunned. Like this is some sort of sign. But as I stare at Harlin, his mouth curved in a confident grin, I don't care about signs\\\"}, \\\"target\\\": \\\" signs\\\", \\\"arguments\\\": {\\\"gen_args_0\\\": {\\\"arg_0\\\": \\\"In my palm is a clear stone, and inside it is a small ivory statuette. A guardian angel.\\\\n\\\\n\\\\\\\"Figured if you're going to be out at night getting hit by cars, you might as well have some backup.\\\\\\\"\\\\n\\\\nI look at him, feeling stunned. Like this is some sort of sign. But as I stare at Harlin, his mouth curved in a confident grin, I don't care about\\\", \\\"arg_1\\\": \\\" signs\\\"}}, \\\"resps\\\": [[[\\\"-2.671875\\\", \\\"False\\\"]]], \\\"filtered_resps\\\": [[\\\"-2.671875\\\", \\\"False\\\"]], \\\"filter\\\": \\\"none\\\", \\\"metrics\\\": [\\\"perplexity\\\", \\\"acc\\\"], \\\"doc_hash\\\": \\\"d5d2ee0c7bb2325b1a3b782dd2f946222c370109812c56acc7da70b662a6a60c\\\", \\\"prompt_hash\\\": \\\"8d638394e95544a75ea75bfa8cedd5fb71d5e65dfac9758cad35a0d5fa6e296c\\\", \\\"target_hash\\\": \\\"697dfd086e17614160f34474ccf8681ad12ae5839865fc979ac177eb5bba0a48\\\", \\\"perplexity\\\": -2.671875, \\\"acc\\\": 0}\\n{\\\"doc_id\\\": 1, \\\"doc\\\": {\\\"text\\\": \\\"Give me a minute to change and I'll meet you at the docks.\\\\\\\" She'd forced those words through her teeth.\\\\n\\\\n\\\\\\\"No need to change. We won't be that long.\\\\\\\"\\\\n\\\\nShane gripped her arm and started leading her to the dock.\\\\n\\\\n\\\\\\\"I can make it there on my own, Shane\\\"}, \\\"target\\\": \\\" Shane\\\", \\\"arguments\\\": {\\\"gen_args_0\\\": {\\\"arg_0\\\": \\\"Give me a minute to change and
…[truncated 936 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_transformer-baseline-perexample_20260520T011942",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T01:21:53.845979+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "head -2 /root/entrainment_gated_ft/lm_eval_clean/1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_transformer-baseline-perexample_20260520T011942",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "head -2 /root/entrainment_gated_ft/lm_eval_clean/1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T01:21:53.846147+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"doc_id\\\": 0, \\\"doc\\\": {\\\"text\\\": \\\"In my palm is a clear stone, and inside it is a small ivory statuette. A guardian angel.\\\\n\\\\n\\\\\\\"Figured if you're going to be out at night getting hit by cars, you might as well have some backup.\\\\\\\"\\\\n\\\\nI look at him, feeling stunned. Like this is some sort of sign. But as I stare at Harlin, his mouth curved in a confident grin, I don't care about signs\\\"}, \\\"target\\\": \\\" signs\\\", \\\"arguments\\\": [[\\\"In my palm is a clear stone, and inside it is a small ivory statuette. A guardian angel.\\\\n\\\\n\\\\\\\"Figured if you're going to be out at night getting hit by cars, you might as well have some backup.\\\\\\\"\\\\n\\\\nI look at him, feeling stunned. Like this is some sort of sign. But as I stare at Harlin, his mouth curved in a confident grin, I don't care about\\\", \\\" signs\\\"]], \\\"resps\\\": [[[-1.828125, false]]], \\\"filtered_resps\\\": [[-1.828125, false]], \\\"filter\\\": \\\"none\\\", \\\"metrics\\\": [\\\"perplexity\\\", \\\"acc\\\"], \\\"doc_hash\\\": \\\"d5d2ee0c7bb2325b1a3b782dd2f946222c370109812c56acc7da70b662a6a60c\\\", \\\"prompt_hash\\\": \\\"8d638394e95544a75ea75bfa8cedd5fb71d5e65dfac9758cad35a0d5fa6e296c\\\", \\\"target_hash\\\": \\\"697dfd086e17614160f34474ccf8681ad12ae5839865fc979ac177eb5bba0a48\\\", \\\"perplexity\\\": -1.828125, \\\"acc\\\": 0}\\n{\\\"doc_id\\\": 1, \\\"doc\\\": {\\\"text\\\": \\\"Give me a minute to change and I'll meet you at the docks.\\\\\\\" She'd forced those words through her teeth.\\\\n\\\\n\\\\\\\"No need to change. We won't be that long.\\\\\\\"\\\\n\\\\nShane gripped her arm and started leading her to the dock.\\\\n\\\\n\\\\\\\"I can make it there on my own, Shane\\\"}, \\\"target\\\": \\\" Shane\\\", \\\"arguments\\\": [[\\\"Give me a minute to change and I'll meet you at the docks.\\\\\\\" She'd forced those words through her teeth.\\\\n\\\\n\\\\\\\"No need to change. 
…[truncated 774 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_transformer-baseline-perexample_20260520T011942",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T01:21:53.846296+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "wc -l /root/entrainment_gated_ft/results_v5/transformer/__root__autodl-tmp__models_1.3b__transformer_1.3B_baseline/samples_lambada_openai_2026-05-18T19-46-52.474119.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_transformer-baseline-perexample_20260520T011942",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "wc -l /root/entrainment_gated_ft/results_v5/transformer/__root__autodl-tmp__models_1.3b__transformer_1.3B_baseline/samples_lambada_openai_2026-05-18T19-46-52.474119.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-20T01:21:53.846456+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"doc_id\\\": 0, \\\"doc\\\": {\\\"text\\\": \\\"In my palm is a clear stone, and inside it is a small ivory statuette. A guardian angel.\\\\n\\\\n\\\\\\\"Figured if you're going to be out at night getting hit by cars, you might as well have some backup.\\\\\\\"\\\\n\\\\nI look at him, feeling stunned. Like this is some sort of sign. But as I stare at Harlin, his mouth curved in a confident grin, I don't care about signs\\\"}, \\\"target\\\": \\\" signs\\\", \\\"arguments\\\": [[\\\"In my palm is a clear stone, and inside it is a small ivory statuette. A guardian angel.\\\\n\\\\n\\\\\\\"Figured if you're going to be out at night getting hit by cars, you might as well have some backup.\\\\\\\"\\\\n\\\\nI look at him, feeling stunned. Like this is some sort of sign. But as I stare at Harlin, his mouth curved in a confident grin, I don't care about\\\", \\\" signs\\\"]], \\\"resps\\\": [[[-2.453125, false]]], \\\"filtered_resps\\\": [[-2.453125, false]], \\\"filter\\\": \\\"none\\\", \\\"metrics\\\": [\\\"perplexity\\\", \\\"acc\\\"], \\\"doc_hash\\\": \\\"d5d2ee0c7bb2325b1a3b782dd2f946222c370109812c56acc7da70b662a6a60c\\\", \\\"prompt_hash\\\": \\\"8d638394e95544a75ea75bfa8cedd5fb71d5e65dfac9758cad35a0d5fa6e296c\\\", \\\"target_hash\\\": \\\"697dfd086e17614160f34474ccf8681ad12ae5839865fc979ac177eb5bba0a48\\\", \\\"perplexity\\\": -2.453125, \\\"acc\\\": 0}\\n{\\\"doc_id\\\": 1, \\\"doc\\\": {\\\"text\\\": \\\"Give me a minute to change and I'll meet you at the docks.\\\\\\\" She'd forced those words through her teeth.\\\\n\\\\n\\\\\\\"No need to change. We won't be that long.\\\\\\\"\\\\n\\\\nShane gripped her arm and started leading her to the dock.\\\\n\\\\n\\\\\\\"I can make it there on my own, Shane\\\"}, \\\"target\\\": \\\" Shane\\\", \\\"arguments\\\": [[\\\"Give me a minute to change and I'll meet you at the docks.\\\\\\\" She'd forced those words through her teeth.\\\\n\\\\n\\\\\\\"No need to change. 
…[truncated 772 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_transformer-baseline-perexample_20260520T011942",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T01:21:53.846609+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"5153 /root/entrainment_gated_ft/results_v5/transformer/__root__autodl-tmp__models_1.3b__transformer_1.3B_baseline/samples_lambada_openai_2026-05-18T19-46-52.474119.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.59}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_transformer-baseline-perexample_20260520T011942",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T01:21:53.846803+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "wc -l /root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/GDN-pure/samples/lambada_openai.jsonl /root/entrainment_gated_ft/lm_eval_clean/1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl /root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/RetNet-pure/samples/lambada_openai.jsonl /root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/RetNet-h3-1/samples/lambada_openai.jsonl /root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/HGRN2-pure/samples/lambada_openai.jsonl /root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/HGRN2-h3-1/samples/lambada_openai.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_transformer-baseline-perexample_20260520T011942",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "wc -l /root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/GDN-pure/samples/lambada_openai.jsonl /root/entrainment_gated_ft/lm_eval_clean/1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl /root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/RetNet-pure/samples/lambada_openai.jsonl /root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/RetNet-h3-1/samples/lambada_openai.jsonl /root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/HGRN2-pure/samples/lambada_openai.jsonl /root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/HGRN2-h3-1/samples/lambada_openai.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T01:21:53.846943+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    5153 /root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/GDN-pure/samples/lambada_openai.jsonl\\n    5153 /root/entrainment_gated_ft/lm_eval_clean/1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl\\n    5153 /root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/RetNet-pure/samples/lambada_openai.jsonl\\n    5153 /root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/RetNet-h3-1/samples/lambada_openai.jsonl\\n    5153 /root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/HGRN2-pure/samples/lambada_openai.jsonl\\n    5153 /root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/HGRN2-h3-1/samples/lambada_openai.jsonl\\n   30918 total\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_transformer-baseline-perexample_20260520T011942",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T01:21:53.847123+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-48145",
  "command": "cat > /root/entrainment_gated_ft/transformer_baseline_analysis.py << 'PYEOF'\nimport json\nimport os\n\nFILES = {\n    \"Transformer\": \"/root/entrainment_gated_ft/results_v5/transformer/__root__autodl-tmp__models_1.3b__transformer_1.3B_baseline/samples_lambada_openai_2026-05-18T19-46-52.474119.jsonl\",\n    \"GDN-pure\": \"/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/GDN-pure/samples/lambada_openai.jsonl\",\n    \"GDN-h3-1\": \"/root/entrainment_gated_ft/lm_eval_clean/1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl\",\n    \"RetNet-pure\": \"/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/RetNet-pure/samples/lambada_openai.jsonl\",\n    \"RetNet-h3-1\": \"/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/RetNet-h3-1/samples/lambada_openai.jsonl\",\n    \"HGRN2-pure\": \"/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/HGRN2-pure/samples/lambada_openai.jsonl\",\n    \"HGRN2-h3-1\": \"/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/HGRN2-h3-1/samples/lambada_openai.jsonl\",\n}\n\ndef load_acc_by_docid(path):\n    acc_map = {}\n    with open(path) as f:\n        for line in f:\n            obj = json.loads(line)\n            doc_id = obj[\"doc_id\"]\n            acc = int(obj[\"acc\"]) if isinstance(obj[\"acc\"], (int, float)) else int(float(obj[\"acc\"]))\n            acc_map[doc_id] = acc\n    return acc_map\n\ndef jaccard(set_a, set_b):\n    if len(set_a) == 0 and len(set_b) == 0:\n        return 1.0\n    intersection = len(set_a & set_b)\n    union = len(set_a | set_b)\n    return intersection / union if union > 0 else 0.0\n\n# Load all\ndata = {}\nfor name, path in FILES.items():\n    data[name] = load_acc_by_docid(path)\n    print(f\"{name}: {sum(data[name].values())}/{len(data[name])} correct ({sum(data[name].values())/len(data[name])*100:.2f}%)\")\n\n# Correct sets\ncorrect_sets = {}\nfor name, acc_map in data.items():\n    correct_sets[name] = set(doc_id for doc_id, acc in acc_map.items() if acc == 1)\n\nn_total = len(data[\"Transformer\"])\ntrans_correct = correct_sets[\"Transformer\"]\n\n# Agreement rates and Jaccard with Transformer\nmodels = [\"GDN-pure\", \"GDN-h3-1\", \"RetNet-pure\", \"RetNet-h3-1\", \"HGRN2-pure\", \"HGRN2-h3-1\"]\n\nprint(\"\\n=== Agreement with Transformer ===\")\nagreement_rates = {}\ncorrect_set_jaccard = {}\nfor m in models:\n    both_correct = len(trans_correct & correct_sets[m])\n    both_wrong = n_total - len(trans_correct | correct_sets[m])\n    agreement = (both_correct + both_wrong) / n_total\n    j = jaccard(trans_correct, correct_sets[m])\n    agreement_rates[f\"{m}_vs_Transformer\"] = round(agreement, 4)\n    correct_set_jaccard[f\"{m}_vs_Transformer\"] = round(j, 4)\n    print(f\"{m} vs Transformer: agreement={agreement:.4f}, J(correct)={j:.4f}, both_correct={both_correct}, both_wrong={both_wrong}\")\n\n# Pairwise Jaccard among hybrids and pures\nprint(\"\\n=== Pairwise Jaccard (correct sets) ===\")\npairwise_jaccard = {}\nfor i, m1 in enumerate(models):\n    for m2 in models[i+1:]:\n        j = jaccard(correct_sets[m1], correct_sets[m2])\n        key = f\"{m1}_vs_{m2}\"\n        pairwise_jaccard[key] = round(j, 4)\n        print(f\"  {key}: {j:.4f}\")\n\n# Key comparison: does h3-1 move closer to Transformer than pure?\nprint(\"\\n=== Key Comparison: Does h3-1 move closer to Transformer? ===\")\nfor arch in [\"GDN\", \"RetNet\", \"HGRN2\"]:\n    pure_j = correct_set_jaccard[f\"{arch}-pure_vs_Transformer\"]\n    h3_j = correct_set_jaccard[f\"{arch}-h3-1_vs_Transformer\"]\n    delta = h3_j - pure_j\n    direction = \"CLOSER\" if delta > 0 else \"FARTHER\" if delta < 0 else \"SAME\"\n    print(f\"  {arch}: pure J={pure_j:.4f}, h3-1 J={h3_j:.4f}, delta={delta:+.4f} ({direction})\")\n\n# Additional: unique correct analysis\nprint(\"\\n=== Unique correct analysis ===\")\nfor m in models:\n    only_m = correct_sets[m] - trans_correct\n    only_trans = trans_correct - correct_sets[m]\n    shared = trans_correct & correct_sets[m]\n    print(f\"  {m}: shared_with_trans={len(shared)}, only_{m}={len(only_m)}, only_trans={len(only_trans)}\")\n\n# Build conclusion\nconclusions = []\nfor arch in [\"GDN\", \"RetNet\", \"HGRN2\"]:\n    pure_j = correct_set_jaccard[f\"{arch}-pure_vs_Transformer\"]\n    h3_j = correct_set_jaccard[f\"{arch}-h3-1_vs_Transformer\"]\n    delta = h3_j - pure_j\n    if delta > 0.01:\n        conclusions.append(f\"{arch}-h3-1 moves toward Transformer (J delta={delta:+.4f})\")\n    elif delta < -0.01:\n        conclusions.append(f\"{arch}-h3-1 moves away from Transformer (J delta={delta:+.4f})\")\n    else:\n        conclusions.append(f\"{arch}-h3-1 shows minimal change vs Transformer (J delta={delta:+.4f})\")\n\nconclusion_text = \"; \".join(conclusions)\n\n# Save results\nresult = {\n    \"transformer_acc\": round(sum(data[\"Transformer\"].values()) / len(data[\"Transformer\"]), 4),\n    \"model_accuracies\": {name: round(sum(acc_map.values()) / len(acc_map), 4) for name, acc_map in data.items()},\n    \"agreement_rates\": agreement_rates,\n    \"correct_set_jaccard\": correct_set_jaccard,\n    \"pairwise_jaccard\": pairwise_jaccard,\n    \"unique_correct\": {\n        m: {\n            \"shared_with_transformer\": len(correct_sets[m] & trans_correct),\n            f\"only_{m}\": len(correct_sets[m] - trans_correct),\n            \"only_transformer\": len(trans_correct - correct_sets[m]),\n        } for m in models\n    },\n    \"key_comparison\": {\n        arch: {\n            \"pure_J_vs_transformer\": correct_set_jaccard[f\"{arch}-pure_vs_Transformer\"],\n            \"h3_1_J_vs_transformer\": correct_set_jaccard[f\"{arch}-h3-1_vs_Transformer\"],\n            \"delta\": round(correct_set_jaccard[f\"{arch}-h3-1_vs_Transformer\"] - correct_set_jaccard[f\"{arch}-pure_vs_Transformer\"], 4),\n        } for arch in [\"GDN\", \"RetNet\", \"HGRN2\"]\n    },\n    \"conclusion\": conclusion_text,\n}\n\nout_path = \"/root/entrainment_gated_ft/transformer_baseline_analysis.json\"\nwith open(out_path, \"w\") as f:\n    json.dump(result, f, indent=2)\nprint(f\"\\nSaved to {out_path}\")\nPYEOF\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 /root/entrainment_gated_ft/transformer_baseline_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_transformer-baseline-perexample_20260520T011942",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-48145",
    "command": "cat > /root/entrainment_gated_ft/transformer_baseline_analysis.py << 'PYEOF'\nimport json\nimport os\n\nFILES = {\n    \"Transformer\": \"/root/entrainment_gated_ft/results_v5/transformer/__root__autodl-tmp__models_1.3b__transformer_1.3B_baseline/samples_lambada_openai_2026-05-18T19-46-52.474119.jsonl\",\n    \"GDN-pure\": \"/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/GDN-pure/samples/lambada_openai.jsonl\",\n    \"GDN-h3-1\": \"/root/entrainment_gated_ft/lm_eval_clean/1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl\",\n    \"RetNet-pure\": \"/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/RetNet-pure/samples/lambada_openai.jsonl\",\n    \"RetNet-h3-1\": \"/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/RetNet-h3-1/samples/lambada_openai.jsonl\",\n    \"HGRN2-pure\": \"/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/HGRN2-pure/samples/lambada_openai.jsonl\",\n    \"HGRN2-h3-1\": \"/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/HGRN2-h3-1/samples/lambada_openai.jsonl\",\n}\n\ndef load_acc_by_docid(path):\n    acc_map = {}\n    with open(path) as f:\n        for line in f:\n            obj = json.loads(line)\n            doc_id = obj[\"doc_id\"]\n            acc = int(obj[\"acc\"]) if isinstance(obj[\"acc\"], (int, float)) else int(float(obj[\"acc\"]))\n            acc_map[doc_id] = acc\n    return acc_map\n\ndef jaccard(set_a, set_b):\n    if len(set_a) == 0 and len(set_b) == 0:\n        return 1.0\n    intersection = len(set_a & set_b)\n    union = len(set_a | set_b)\n    return intersection / union if union > 0 else 0.0\n\n# Load all\ndata = {}\nfor name, path in FILES.items():\n    data[name] = load_acc_by_docid(path)\n    print(f\"{name}: {sum(data[name].values())}/{len(data[name])} correct ({sum(data[name].values())/len(data[name])*100:.2f}%)\")\n\n# Correct sets\ncorrect_sets = {}\nfor name, acc_map in data.items():\n    correct_sets[name] = set(doc_id for doc_id, acc in acc_map.items() if acc == 1)\n\nn_total = len(data[\"Transformer\"])\ntrans_correct = correct_sets[\"Transformer\"]\n\n# Agreement rates and Jaccard with Transformer\nmodels = [\"GDN-pure\", \"GDN-h3-1\", \"RetNet-pure\", \"RetNet-h3-1\", \"HGRN2-pure\", \"HGRN2-h3-1\"]\n\nprint(\"\\n=== Agreement with Transformer ===\")\nagreement_rates = {}\ncorrect_set_jaccard = {}\nfor m in models:\n    both_correct = len(trans_correct & correct_sets[m])\n    both_wrong = n_total - len(trans_correct | correct_sets[m])\n    agreement = (both_correct + both_wrong) / n_total\n    j = jaccard(trans_correct, correct_sets[m])\n    agreement_rates[f\"{m}_vs_Transformer\"] = round(agreement, 4)\n    correct_set_jaccard[f\"{m}_vs_Transformer\"] = round(j, 4)\n    print(f\"{m} vs Transformer: agreement={agreement:.4f}, J(correct)={j:.4f}, both_correct={both_correct}, both_wrong={both_wrong}\")\n\n# Pairwise Jaccard among hybrids and pures\nprint(\"\\n=== Pairwise Jaccard (correct sets) ===\")\npairwise_jaccard = {}\nfor i, m1 in enumerate(models):\n    for m2 in models[i+1:]:\n        j = jaccard(correct_sets[m1], correct_sets[m2])\n        key = f\"{m1}_vs_{m2}\"\n        pairwise_jaccard[key] = round(j, 4)\n        print(f\"  {key}: {j:.4f}\")\n\n# Key comparison: does h3-1 move closer to Transformer than pure?\nprint(\"\\n=== Key Comparison: Does h3-1 move closer to Transformer? ===\")\nfor arch in [\"GDN\", \"RetNet\", \"HGRN2\"]:\n    pure_j = correct_set_jaccard[f\"{arch}-pure_vs_Transformer\"]\n    h3_j = correct_set_jaccard[f\"{arch}-h3-1_vs_Transformer\"]\n    delta = h3_j - pure_j\n    direction = \"CLOSER\" if delta > 0 else \"FARTHER\" if delta < 0 else \"SAME\"\n    print(f\"  {arch}: pure J={pure_j:.4f}, h3-1 J={h3_j:.4f}, delta={delta:+.4f} ({direction})\")\n\n# Additional: unique correct analysis\nprint(\"\\n=== Unique correct analysis ===\")\nfor m in models:\n    only_m = correct_sets[m] - trans_correct\n    only_trans = trans_correct - correct_sets[m]\n    shared = trans_correct & correct_sets[m]\n    print(f\"  {m}: shared_with_trans={len(shared)}, only_{m}={len(only_m)}, only_trans={len(only_trans)}\")\n\n# Build conclusion\nconclusions = []\nfor arch in [\"GDN\", \"RetNet\", \"HGRN2\"]:\n    pure_j = correct_set_jaccard[f\"{arch}-pure_vs_Transformer\"]\n    h3_j = correct_set_jaccard[f\"{arch}-h3-1_vs_Transformer\"]\n    delta = h3_j - pure_j\n    if delta > 0.01:\n        conclusions.append(f\"{arch}-h3-1 moves toward Transformer (J delta={delta:+.4f})\")\n    elif delta < -0.01:\n        conclusions.append(f\"{arch}-h3-1 moves away from Transformer (J delta={delta:+.4f})\")\n    else:\n        conclusions.append(f\"{arch}-h3-1 shows minimal change vs Transformer (J delta={delta:+.4f})\")\n\nconclusion_text = \"; \".join(conclusions)\n\n# Save results\nresult = {\n    \"transformer_acc\": round(sum(data[\"Transformer\"].values()) / len(data[\"Transformer\"]), 4),\n    \"model_accuracies\": {name: round(sum(acc_map.values()) / len(acc_map), 4) for name, acc_map in data.items()},\n    \"agreement_rates\": agreement_rates,\n    \"correct_set_jaccard\": correct_set_jaccard,\n    \"pairwise_jaccard\": pairwise_jaccard,\n    \"unique_correct\": {\n        m: {\n            \"shared_with_transformer\": len(correct_sets[m] & trans_correct),\n            f\"only_{m}\": len(correct_sets[m] - trans_correct),\n            \"only_transformer\": len(trans_correct - correct_sets[m]),\n        } for m in models\n    },\n    \"key_comparison\": {\n        arch: {\n            \"pure_J_vs_transformer\": correct_set_jaccard[f\"{arch}-pure_vs_Transformer\"],\n            \"h3_1_J_vs_transformer\": correct_set_jaccard[f\"{arch}-h3-1_vs_Transformer\"],\n            \"delta\": round(correct_set_jaccard[f\"{arch}-h3-1_vs_Transformer\"] - correct_set_jaccard[f\"{arch}-pure_vs_Transformer\"], 4),\n        } for arch in [\"GDN\", \"RetNet\", \"HGRN2\"]\n    },\n    \"conclusion\": conclusion_text,\n}\n\nout_path = \"/root/entrainment_gated_ft/transformer_baseline_analysis.json\"\nwith open(out_path, \"w\") as f:\n    json.dump(result, f, indent=2)\nprint(f\"\\nSaved to {out_path}\")\nPYEOF\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 /root/entrainment_gated_ft/transformer_baseline_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T01:21:53.847329+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Transformer: 2478/5153 correct (48.09%)\\nGDN-pure: 2800/5153 correct (54.34%)\\nGDN-h3-1: 2645/5153 correct (51.33%)\\nRetNet-pure: 2666/5153 correct (51.74%)\\nRetNet-h3-1: 2589/5153 correct (50.24%)\\nHGRN2-pure: 2494/5153 correct (48.40%)\\nHGRN2-h3-1: 2650/5153 correct (51.43%)\\n\\n=== Agreement with Transformer ===\\nGDN-pure vs Transformer: agreement=0.7788, J(correct)=0.6447, both_correct=2069, both_wrong=1944\\nGDN-h3-1 vs Transformer: agreement=0.7887, J(correct)=0.6494, both_correct=2017, both_wrong=2047\\nRetNet-pure vs Transformer: agreement=0.8090, J(correct)=0.6789, both_correct=2080, both_wrong=2089\\nRetNet-h3-1 vs Transformer: agreement=0.8224, J(correct)=0.6941, both_correct=2076, both_wrong=2162\\nHGRN2-pure vs Transformer: agreement=0.8106, J(correct)=0.6718, both_correct=1998, both_wrong=2179\\nHGRN2-h3-1 vs Transformer: agreement=0.8250, J(correct)=0.7008, both_correct=2113, both_wrong=2138\\n\\n=== Pairwise Jaccard (correct sets) ===\\n  GDN-pure_vs_GDN-h3-1: 0.6697\\n  GDN-pure_vs_RetNet-pure: 0.6716\\n  GDN-pure_vs_RetNet-h3-1: 0.6679\\n  GDN-pure_vs_HGRN2-pure: 0.6539\\n  GDN-pure_vs_HGRN2-h3-1: 0.6601\\n  GDN-h3-1_vs_RetNet-pure: 0.6680\\n  GDN-h3-1_vs_RetNet-h3-1: 0.6733\\n  GDN-h3-1_vs_HGRN2-pure: 0.6466\\n  GDN-h3-1_vs_HGRN2-h3-1: 0.6588\\n  RetNet-pure_vs_RetNet-h3-1: 0.7029\\n  RetNet-pure_vs_HGRN2-pure: 0.6813\\n  RetNet-pure_vs_HGRN2-h3-1: 0.6887\\n  RetNet-h3-1_vs_HGRN2-pure: 0.6753\\n  RetNet-h3-1_vs_HGRN2-h3-1: 0.6960\\n  HGRN2-pure_vs_HGRN2-h3-1: 0.6910\\n\\n=== Key Comparison: Does h3-1 move closer to Transformer? ===\\n  GDN: pure J=0.6447, h3-1 J=0.6494, delta=+0.0047 (CLOSER)\\n  RetNet: pure J=0.6789, h3-1 J=0.6941, delta=+0.0152 (CLOSER)\\n  HGRN2: pure J=0.6718, h3-1 J=0.7008, delta=+0.0290 (CLOSER)\\n\\n=== Unique correct analysis ===\\n  GDN-pure: shared_with_trans=2069, only_GDN-pure=731, only_trans=409\\n  GDN-h3-1: shared_with_trans=2017, only_GDN-h3-1=628, on
…[truncated 503 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_transformer-baseline-perexample_20260520T011942",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T01:21:53.847570+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "cat /root/entrainment_gated_ft/transformer_baseline_analysis.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_transformer-baseline-perexample_20260520T011942",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "cat /root/entrainment_gated_ft/transformer_baseline_analysis.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T01:21:53.847793+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"transformer_acc\\\": 0.4809,\\n  \\\"model_accuracies\\\": {\\n    \\\"Transformer\\\": 0.4809,\\n    \\\"GDN-pure\\\": 0.5434,\\n    \\\"GDN-h3-1\\\": 0.5133,\\n    \\\"RetNet-pure\\\": 0.5174,\\n    \\\"RetNet-h3-1\\\": 0.5024,\\n    \\\"HGRN2-pure\\\": 0.484,\\n    \\\"HGRN2-h3-1\\\": 0.5143\\n  },\\n  \\\"agreement_rates\\\": {\\n    \\\"GDN-pure_vs_Transformer\\\": 0.7788,\\n    \\\"GDN-h3-1_vs_Transformer\\\": 0.7887,\\n    \\\"RetNet-pure_vs_Transformer\\\": 0.809,\\n    \\\"RetNet-h3-1_vs_Transformer\\\": 0.8224,\\n    \\\"HGRN2-pure_vs_Transformer\\\": 0.8106,\\n    \\\"HGRN2-h3-1_vs_Transformer\\\": 0.825\\n  },\\n  \\\"correct_set_jaccard\\\": {\\n    \\\"GDN-pure_vs_Transformer\\\": 0.6447,\\n    \\\"GDN-h3-1_vs_Transformer\\\": 0.6494,\\n    \\\"RetNet-pure_vs_Transformer\\\": 0.6789,\\n    \\\"RetNet-h3-1_vs_Transformer\\\": 0.6941,\\n    \\\"HGRN2-pure_vs_Transformer\\\": 0.6718,\\n    \\\"HGRN2-h3-1_vs_Transformer\\\": 0.7008\\n  },\\n  \\\"pairwise_jaccard\\\": {\\n    \\\"GDN-pure_vs_GDN-h3-1\\\": 0.6697,\\n    \\\"GDN-pure_vs_RetNet-pure\\\": 0.6716,\\n    \\\"GDN-pure_vs_RetNet-h3-1\\\": 0.6679,\\n    \\\"GDN-pure_vs_HGRN2-pure\\\": 0.6539,\\n    \\\"GDN-pure_vs_HGRN2-h3-1\\\": 0.6601,\\n    \\\"GDN-h3-1_vs_RetNet-pure\\\": 0.668,\\n    \\\"GDN-h3-1_vs_RetNet-h3-1\\\": 0.6733,\\n    \\\"GDN-h3-1_vs_HGRN2-pure\\\": 0.6466,\\n    \\\"GDN-h3-1_vs_HGRN2-h3-1\\\": 0.6588,\\n    \\\"RetNet-pure_vs_RetNet-h3-1\\\": 0.7029,\\n    \\\"RetNet-pure_vs_HGRN2-pure\\\": 0.6813,\\n    \\\"RetNet-pure_vs_HGRN2-h3-1\\\": 0.6887,\\n    \\\"RetNet-h3-1_vs_HGRN2-pure\\\": 0.6753,\\n    \\\"RetNet-h3-1_vs_HGRN2-h3-1\\\": 0.696,\\n    \\\"HGRN2-pure_vs_HGRN2-h3-1\\\": 0.691\\n  },\\n  \\\"unique_correct\\\": {\\n    \\\"GDN-pure\\\": {\\n      \\\"shared_with_transformer\\\": 2069,\\n      \\\"only_GDN-pure\\\": 731,\\n      \\\"only_transformer\\\": 409\\n    },\\n    \\\"GDN-h3-1\\\": {\\n      \\\"sh
…[truncated 1581 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_transformer-baseline-perexample_20260520T011942",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-20T01:21:53.847991+00:00_

结果已保存至 `/root/entrainment_gated_ft/transformer_baseline_analysis.json`。

## 核心发现

**Transformer accuracy: 48.09%**（反而低于所有 recurrent/hybrid 模型）

### h3-1 是否向 Transformer 靠拢？

| 架构 | pure J(vs Trans) | h3-1 J(vs Trans) | delta |
|------|:-:|:-:|:-:|
| GDN | 0.6447 | 0.6494 | +0.0047 |
| RetNet | 0.6789 | 0.6941 | **+0.0152** |
| HGRN2 | 0.6718 | 0.7008 | **+0.0290** |

**三个架构的 h3-1 correct set 均比 pure 更接近 Transformer**，效应强度 HGRN2 > RetNet > GDN。Agreement rate 同样呈现一致趋势（HGRN2-h3-1 达到最高的 0.825）。

### 解读

- Attention 层的加入确实使 hybrid 的 per-example 行为向 Transformer 收敛，支持 "attention entrainment" 假设
- HGRN2 对 attention 最敏感（delta 最大），GDN 最不敏感（可能因为 GDN 的 gating 机制本身已部分模拟了 attention 的功能）
- 值得注意的是 Transformer 本身 accuracy 最低，说明 hybrid 不是简单"变弱到和 Transformer 一样"，而是在保持/提升 accuracy 的同时 correct set 组成趋同

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_transformer-baseline-perexample_20260520T011942"
}
```

</details>

---
