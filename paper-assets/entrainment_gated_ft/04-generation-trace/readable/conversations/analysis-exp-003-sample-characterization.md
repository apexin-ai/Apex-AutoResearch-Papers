# analysis exp 003 sample characterization

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 71
- **Recorded user turns:** 0
- **Tool calls:** 35
- **Original source:** `logs/chats/worker_analysis_exp_003_sample_characterization_20260519T131141.jsonl`
- **Structured JSON:** [`62292da8e6a046bc811f.json`](../../sessions/62/62292da8e6a046bc811f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

71 recorded events

### Tool call

_source line 1 · 2026-05-19T13:18:01.909753+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__register_artifact",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__register_artifact",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T13:18:01.910085+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T13:18:01.910251+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "head -10 /root/entrainment_gated_ft/analysis/lambada_per_example.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "head -10 /root/entrainment_gated_ft/analysis/lambada_per_example.csv",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-19T13:18:01.910383+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "tail -5 /root/entrainment_gated_ft/analysis/lambada_per_example.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "tail -5 /root/entrainment_gated_ft/analysis/lambada_per_example.csv",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T13:18:01.910504+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "wc -l /root/entrainment_gated_ft/analysis/lambada_per_example.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "wc -l /root/entrainment_gated_ft/analysis/lambada_per_example.csv",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T13:18:01.910663+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"doc_id,context_length,target,gdn_pure_acc,gdn_pure_lp,gdn_h12_acc,gdn_h12_lp,hgrn2_pure_acc,hgrn2_pure_lp,hgrn2_h3_acc,hgrn2_h3_lp\\r\\n0,68,signs,0,-1.8828125,0,-2.921875,0,-3.46875,0,-3.078125\\r\\n1,48,Shane,0,-1.7421875,0,-2.96875,0,-3.234375,0,-3.171875\\r\\n2,76,insurance,0,-1.4765625,1,-0.98046875,1,-0.80859375,1,-0.55078125\\r\\n3,50,Helen,1,-0.158203125,1,-0.1953125,1,-0.53125,0,-1.0703125\\r\\n4,69,chains,1,-2.1875,1,-0.322265625,0,-1.3515625,0,-2.09375\\r\\n5,82,Hastin,0,-2.1875,0,-2.5625,0,-2.625,0,-3.953125\\r\\n6,51,Queen,1,-0.21484375,1,-0.74609375,1,-1.5234375,1,-0.95703125\\r\\n7,52,Aidan,1,-0.1748046875,1,-0.4140625,1,-0.7421875,1,-0.98828125\\r\\n8,36,Gabriel,0,-7.28125,1,-1.15625,0,-3.3125,1,-3.109375\\r\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.17}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T13:18:01.910820+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "head -10 /root/entrainment_gated_ft/analysis/lambada_matched_per_example.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "head -10 /root/entrainment_gated_ft/analysis/lambada_matched_per_example.csv",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T13:18:01.910954+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"5148,77,turbines,0,-4.28125,0,-3.984375,0,-2.8125,0,-1.6171875\\r\\n5149,67,recipe,1,-0.796875,1,-0.65625,1,-0.90234375,1,-0.412109375\\r\\n5150,57,tunnel,0,-4.125,0,-3.3125,0,-2.53125,1,-1.390625\\r\\n5151,62,whistling,0,-11.0625,0,-9.8125,0,-8.4375,0,-9.4375\\r\\n5152,50,Grandmother,1,-1.2734375,1,-1.25,1,-2.359375,0,-3.1875\\r\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.89}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T13:18:01.911085+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "wc -l /root/entrainment_gated_ft/analysis/lambada_matched_per_example.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "wc -l /root/entrainment_gated_ft/analysis/lambada_matched_per_example.csv",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T13:18:01.911212+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"5162 /root/entrainment_gated_ft/analysis/lambada_per_example.csv\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.94}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-19T13:18:01.911340+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"doc_id,context_length,target,gdn_pure_acc,gdn_pure_lp,gdn_h31_acc,gdn_h31_lp,hgrn2_pure_acc,hgrn2_pure_lp,hgrn2_h31_acc,hgrn2_h31_lp\\r\\n0,68,signs,0,-1.8828125,0,-2.453125,0,-3.46875,0,-3.078125\\r\\n1,48,Shane,0,-1.7421875,0,-2.640625,0,-3.234375,0,-3.171875\\r\\n2,76,insurance,0,-1.4765625,1,-0.83203125,1,-0.80859375,1,-0.55078125\\r\\n3,50,Helen,1,-0.158203125,1,-0.376953125,1,-0.53125,0,-1.0703125\\r\\n4,69,chains,1,-2.1875,1,-0.7421875,0,-1.3515625,0,-2.09375\\r\\n5,82,Hastin,0,-2.1875,0,-2.171875,0,-2.625,0,-3.953125\\r\\n6,51,Queen,1,-0.21484375,1,-1.515625,1,-1.5234375,1,-0.95703125\\r\\n7,52,Aidan,1,-0.1748046875,1,-0.5625,1,-0.7421875,1,-0.98828125\\r\\n8,36,Gabriel,0,-7.28125,1,-1.421875,0,-3.3125,1,-3.109375\\r\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.91}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T13:18:01.911503+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"5162 /root/entrainment_gated_ft/analysis/lambada_matched_per_example.csv\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.94}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T13:18:01.911685+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "tail -n +2 /root/entrainment_gated_ft/analysis/lambada_per_example.csv | cut -d',' -f1 | sort -n | uniq -d | head -20",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "tail -n +2 /root/entrainment_gated_ft/analysis/lambada_per_example.csv | cut -d',' -f1 | sort -n | uniq -d | head -20",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T13:18:01.911821+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T13:18:01.911939+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "tail -n +2 /root/entrainment_gated_ft/analysis/lambada_per_example.csv | cut -d',' -f1 | sort -n | tail -5",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "tail -n +2 /root/entrainment_gated_ft/analysis/lambada_per_example.csv | cut -d',' -f1 | sort -n | tail -5",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T13:18:01.912060+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T13:18:01.912195+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "tail -n +2 /root/entrainment_gated_ft/analysis/lambada_per_example.csv | cut -d',' -f1 | sort -n | uniq | wc -l",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "tail -n +2 /root/entrainment_gated_ft/analysis/lambada_per_example.csv | cut -d',' -f1 | sort -n | uniq | wc -l",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T13:18:01.912315+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T13:18:01.912429+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "ls /root/autodl-tmp/models_1.3b/1.3B-100B-GatedDeltaNet-pure/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "ls /root/autodl-tmp/models_1.3b/1.3B-100B-GatedDeltaNet-pure/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T13:18:01.912550+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"config.json\\ngeneration_config.json\\nmodel-00001-of-00002.safetensors\\nmodel-00002-of-00002.safetensors\\nmodel.safetensors.index.json\\nspecial_tokens_map.json\\ntokenizer.json\\ntokenizer_config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.84}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T13:18:01.912716+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-48145",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport pandas as pd\ndf = pd.read_csv('/root/entrainment_gated_ft/analysis/lambada_per_example.csv')\nprint('Shape:', df.shape)\nprint('Columns:', list(df.columns))\nprint('doc_id range:', df.doc_id.min(), '-', df.doc_id.max())\nprint('Unique doc_ids:', df.doc_id.nunique())\nprint('Duplicate doc_ids:', df.doc_id.duplicated().sum())\nif df.doc_id.duplicated().any():\n    dups = df[df.doc_id.duplicated(keep=False)].sort_values('doc_id')\n    print('Dup rows:')\n    print(dups.head(20))\nprint('---')\ndf2 = pd.read_csv('/root/entrainment_gated_ft/analysis/lambada_matched_per_example.csv')\nprint('Matched shape:', df2.shape)\nprint('Matched columns:', list(df2.columns))\nprint('Matched dup doc_ids:', df2.doc_id.duplicated().sum())\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-48145",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport pandas as pd\ndf = pd.read_csv('/root/entrainment_gated_ft/analysis/lambada_per_example.csv')\nprint('Shape:', df.shape)\nprint('Columns:', list(df.columns))\nprint('doc_id range:', df.doc_id.min(), '-', df.doc_id.max())\nprint('Unique doc_ids:', df.doc_id.nunique())\nprint('Duplicate doc_ids:', df.doc_id.duplicated().sum())\nif df.doc_id.duplicated().any():\n    dups = df[df.doc_id.duplicated(keep=False)].sort_values('doc_id')\n    print('Dup rows:')\n    print(dups.head(20))\nprint('---')\ndf2 = pd.read_csv('/root/entrainment_gated_ft/analysis/lambada_matched_per_example.csv')\nprint('Matched shape:', df2.shape)\nprint('Matched columns:', list(df2.columns))\nprint('Matched dup doc_ids:', df2.doc_id.duplicated().sum())\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T13:18:01.912859+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Shape: (5153, 11)\\nColumns: ['doc_id', 'context_length', 'target', 'gdn_pure_acc', 'gdn_pure_lp', 'gdn_h12_acc', 'gdn_h12_lp', 'hgrn2_pure_acc', 'hgrn2_pure_lp', 'hgrn2_h3_acc', 'hgrn2_h3_lp']\\ndoc_id range: 0 - 5152\\nUnique doc_ids: 5153\\nDuplicate doc_ids: 0\\n---\\nMatched shape: (5153, 11)\\nMatched columns: ['doc_id', 'context_length', 'target', 'gdn_pure_acc', 'gdn_pure_lp', 'gdn_h31_acc', 'gdn_h31_lp', 'hgrn2_pure_acc', 'hgrn2_pure_lp', 'hgrn2_h31_acc', 'hgrn2_h31_lp']\\nMatched dup doc_ids: 0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T13:18:01.913036+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "ls /root/entrainment_gated_ft/analysis/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "ls /root/entrainment_gated_ft/analysis/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T13:18:01.913177+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"convergence_analysis.pdf\\nconvergence_analysis.png\\nconvergence_analysis.py\\ncross_scale_convergence.pdf\\ncross_scale_convergence.png\\ncross_scale_convergence.py\\ncross_scale_summary.csv\\nlambada_attention_analysis.png\\nlambada_crossmodel_scatter.png\\nlambada_matched_comparison.pdf\\nlambada_matched_comparison.png\\nlambada_matched_comparison.py\\nlambada_matched_comparison.py.bak\\nlambada_matched_per_example.csv\\nlambada_per_example.csv\\nlambada_robustness_h6.pdf\\nlambada_robustness_h6.png\\nlambada_robustness_h6.py\\nlambada_three_arch_comparison.pdf\\nlambada_three_arch_comparison.png\\nlambada_three_arch_comparison.py\\nlogprob_analysis.py\\nlogprob_plots.py\\ntask_specificity_analysis.py\\ntask_specificity_figure.pdf\\ntask_specificity_figure.png\\ntask_specificity_results.csv\\nwang_et_al_differentiation.md\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.95}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T13:18:01.913321+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "head -50 /root/entrainment_gated_ft/analysis/lambada_three_arch_comparison.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "head -50 /root/entrainment_gated_ft/analysis/lambada_three_arch_comparison.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T13:18:01.913471+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"import json\\nimport os\\nimport numpy as np\\nimport matplotlib\\nmatplotlib.use('Agg')\\nimport matplotlib.pyplot as plt\\nimport matplotlib.gridspec as gridspec\\nfrom itertools import combinations\\n\\nOUT_DIR = '/root/entrainment_gated_ft/analysis'\\nDATA_DIR = '/root/entrainment_gated_ft/lm_eval_clean'\\n\\n# ── Load helpers ──────────────────────────────────────────────────\\ndef load_jsonl(path):\\n    samples = []\\n    with open(path) as f:\\n        for line in f:\\n            samples.append(json.loads(line))\\n    return samples\\n\\ndef load_json_samples(path, task='lambada_openai'):\\n    with open(path) as f:\\n        d = json.load(f)\\n    return d['samples'][task]\\n\\n# ── Load all 6 conditions ────────────────────────────────────────\\nprint(\\\"Loading data...\\\")\\nmodel_data = {}\\n\\nmodel_data['GDN-pure'] = sorted(\\n    load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-GatedDeltaNet-pure.json')),\\n    key=lambda x: x['doc_id']\\n)\\nmodel_data['GDN-h3-1'] = sorted(\\n    load_jsonl(os.path.join(DATA_DIR, '1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl')),\\n    key=lambda x: x['doc_id']\\n)\\nmodel_data['HGRN2-pure'] = sorted(\\n    load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-HGRN2-pure.json')),\\n    key=lambda x: x['doc_id']\\n)\\nmodel_data['HGRN2-h3-1'] = sorted(\\n    load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-HGRN2-hybrid-3-1.json')),\\n    key=lambda x: x['doc_id']\\n)\\nmodel_data['RetNet-pure'] = sorted(\\n    load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-RetNet-pure.json')),\\n    key=lambda x: x['doc_id']\\n)\\nmodel_data['RetNet-h3-1'] = sorted(\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T13:18:01.913653+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "ls /root/entrainment_gated_ft/lm_eval_clean/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "ls /root/entrainment_gated_ft/lm_eval_clean/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-19T13:18:01.913789+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "find /root/entrainment_gated_ft/lm_eval_clean/ -name \"*RetNet*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "find /root/entrainment_gated_ft/lm_eval_clean/ -name \"*RetNet*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-19T13:18:01.913928+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"1.3B-100B-GatedDeltaNet-hybrid-12-1.json\\n1.3B-100B-GatedDeltaNet-hybrid-12-1_final.log\\n1.3B-100B-GatedDeltaNet-hybrid-24-1_results.json\\n1.3B-100B-GatedDeltaNet-hybrid-3-1_results.json\\n1.3B-100B-GatedDeltaNet-hybrid-6-1_results.json\\n1.3B-100B-GatedDeltaNet-pure.json\\n1.3B-100B-GatedDeltaNet-pure.log\\n1.3B-100B-GatedDeltaNet-pure_final.log\\n1.3B-100B-GatedDeltaNet-pure_lambada_only.json\\n1.3B-100B-GatedDeltaNet-pure_results.json\\n1.3B-100B-HGRN2-hybrid-12-1.json\\n1.3B-100B-HGRN2-hybrid-24-1.json\\n1.3B-100B-HGRN2-hybrid-3-1.json\\n1.3B-100B-HGRN2-hybrid-6-1.json\\n1.3B-100B-HGRN2-pure.json\\n1.3B-100B-RetNet-hybrid-12-1.json\\n1.3B-100B-RetNet-hybrid-24-1.json\\n1.3B-100B-RetNet-hybrid-3-1.json\\n1.3B-100B-RetNet-hybrid-6-1.json\\n1.3B-100B-RetNet-pure.json\\n1.3B-100B-RetNet-pure_final.log\\n1.3B-100B-RetNet-pure_results.json\\n1.3b\\n340m\\ndebug\\neval_all.log\\neval_h24.log\\neval_remaining.log\\nfigures\\ngdn_pure_validation.log\\nhgrn2_debug.log\\nhgrn2_debug_lambada.log\\nmultiseed\\nremaining.log\\nretnet_hybrid12_eval.log\\nretnet_pure.log\\nretnet_pure_final.log\\nretnet_pure_v2.log\\nretnet_redownload_eval.log\\nretnet_reeval.log\\nsummary_all_1.3b.csv\\ntransformer_1.3B_baseline.json\\ntransformer_1.3B_baseline_final.log\\nvalidation.log\\nvalidation2.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.81}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T13:18:01.914110+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-RetNet-pure_results.json\\n/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-RetNet-pure_final.log\\n/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-RetNet-pure.json\\n/root/entrainment_gated_ft/lm_eval_clean/340m/340M-20B-RetNet-pure\\n/root/entrainment_gated_ft/lm_eval_clean/340m/340M-20B-RetNet-pure/340M-20B-RetNet-pure.json\\n/root/entrainment_gated_ft/lm_eval_clean/340m/340M-20B-RetNet-hybrid-3-1\\n/root/entrainment_gated_ft/lm_eval_clean/340m/340M-20B-RetNet-hybrid-3-1/340M-20B-RetNet-hybrid-3-1.json\\n/root/entrainment_gated_ft/lm_eval_clean/340m/340M-20B-RetNet-hybrid-6-1\\n/root/entrainment_gated_ft/lm_eval_clean/340m/340M-20B-RetNet-hybrid-6-1/340M-20B-RetNet-hybrid-6-1.json\\n/root/entrainment_gated_ft/lm_eval_clean/340m/340M-20B-RetNet-hybrid-12-1\\n/root/entrainment_gated_ft/lm_eval_clean/340m/340M-20B-RetNet-hybrid-12-1/340M-20B-RetNet-hybrid-12-1.json\\n/root/entrainment_gated_ft/lm_eval_clean/340m/340M-20B-RetNet-hybrid-24-1\\n/root/entrainment_gated_ft/lm_eval_clean/340m/340M-20B-RetNet-hybrid-24-1/340M-20B-RetNet-hybrid-24-1.json\\n/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-RetNet-hybrid-12-1.json\\n/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-RetNet-hybrid-24-1.json\\n/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-RetNet-hybrid-6-1.json\\n/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-RetNet-hybrid-3-1.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-19T13:18:01.914306+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-48145",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\n# Check RetNet pure\nwith open('/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-RetNet-pure.json') as f:\n    d = json.load(f)\nprint('RetNet-pure keys:', list(d.keys()))\nif 'samples' in d:\n    tasks = list(d['samples'].keys())\n    print('Tasks:', tasks)\n    if 'lambada_openai' in tasks:\n        s = d['samples']['lambada_openai'][0]\n        print('Sample keys:', list(s.keys()))\n        print('Sample 0:', {k: s[k] for k in ['doc_id', 'acc', 'target'] if k in s})\n\n# Check RetNet h3-1\nwith open('/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-RetNet-hybrid-3-1.json') as f:\n    d2 = json.load(f)\nprint()\nprint('RetNet-h31 keys:', list(d2.keys()))\nif 'samples' in d2:\n    tasks2 = list(d2['samples'].keys())\n    print('Tasks:', tasks2)\n    if 'lambada_openai' in tasks2:\n        s2 = d2['samples']['lambada_openai'][0]\n        print('Sample keys:', list(s2.keys()))\n        print('Sample 0:', {k: s2[k] for k in ['doc_id', 'acc', 'target', 'logprob'] if k in s2})\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-48145",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\n# Check RetNet pure\nwith open('/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-RetNet-pure.json') as f:\n    d = json.load(f)\nprint('RetNet-pure keys:', list(d.keys()))\nif 'samples' in d:\n    tasks = list(d['samples'].keys())\n    print('Tasks:', tasks)\n    if 'lambada_openai' in tasks:\n        s = d['samples']['lambada_openai'][0]\n        print('Sample keys:', list(s.keys()))\n        print('Sample 0:', {k: s[k] for k in ['doc_id', 'acc', 'target'] if k in s})\n\n# Check RetNet h3-1\nwith open('/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-RetNet-hybrid-3-1.json') as f:\n    d2 = json.load(f)\nprint()\nprint('RetNet-h31 keys:', list(d2.keys()))\nif 'samples' in d2:\n    tasks2 = list(d2['samples'].keys())\n    print('Tasks:', tasks2)\n    if 'lambada_openai' in tasks2:\n        s2 = d2['samples']['lambada_openai'][0]\n        print('Sample keys:', list(s2.keys()))\n        print('Sample 0:', {k: s2[k] for k in ['doc_id', 'acc', 'target', 'logprob'] if k in s2})\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T13:18:01.914472+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"RetNet-pure keys: ['results', 'groups', 'group_subtasks', 'configs', 'versions', 'n-shot', 'higher_is_better', 'n-samples', 'samples', 'config', 'git_hash', 'date', 'pretty_env_info', 'transformers_version', 'lm_eval_version', 'upper_git_hash', 'tokenizer_pad_token', 'tokenizer_eos_token', 'tokenizer_bos_token', 'eot_token_id', 'max_length']\\nTasks: ['lambada_openai', 'hellaswag', 'winogrande', 'arc_easy', 'arc_challenge', 'mmlu_abstract_algebra', 'mmlu_anatomy', 'mmlu_astronomy', 'mmlu_college_biology', 'mmlu_college_chemistry', 'mmlu_college_computer_science', 'mmlu_college_mathematics', 'mmlu_college_physics', 'mmlu_computer_security', 'mmlu_conceptual_physics', 'mmlu_electrical_engineering', 'mmlu_elementary_mathematics', 'mmlu_high_school_biology', 'mmlu_high_school_chemistry', 'mmlu_high_school_computer_science', 'mmlu_high_school_mathematics', 'mmlu_high_school_physics', 'mmlu_high_school_statistics', 'mmlu_machine_learning', 'mmlu_business_ethics', 'mmlu_clinical_knowledge', 'mmlu_college_medicine', 'mmlu_global_facts', 'mmlu_human_aging', 'mmlu_management', 'mmlu_marketing', 'mmlu_medical_genetics', 'mmlu_miscellaneous', 'mmlu_nutrition', 'mmlu_professional_accounting', 'mmlu_professional_medicine', 'mmlu_virology', 'mmlu_econometrics', 'mmlu_high_school_geography', 'mmlu_high_school_government_and_politics', 'mmlu_high_school_macroeconomics', 'mmlu_high_school_microeconomics', 'mmlu_high_school_psychology', 'mmlu_human_sexuality', 'mmlu_professional_psychology', 'mmlu_public_relations', 'mmlu_security_studies', 'mmlu_sociology', 'mmlu_us_foreign_policy', 'mmlu_formal_logic', 'mmlu_high_school_european_history', 'mmlu_high_school_us_history', 'mmlu_high_school_world_history', 'mmlu_international_law', 'mmlu_jurisprudence', 'mmlu_logical_fallacies', 'mmlu_moral_disputes', 'mmlu_moral_scenarios', 'mmlu_philosophy', 'mmlu_prehistory', 'mmlu_professional_law', 'mmlu_world_religions']\\nSample keys: ['doc_
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-19T13:18:01.914684+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-48145",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\nwith open('/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-RetNet-pure.json') as f:\n    d = json.load(f)\ns = d['samples']['lambada_openai'][0]\nprint('doc keys:', list(s['doc'].keys()) if isinstance(s['doc'], dict) else type(s['doc']))\nif isinstance(s['doc'], dict):\n    print('text preview:', s['doc'].get('text', '')[:200])\nprint('target:', repr(s['target']))\nprint('perplexity:', s.get('perplexity'))\nprint('acc:', s.get('acc'))\nprint('Total samples:', len(d['samples']['lambada_openai']))\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-48145",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\nwith open('/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-RetNet-pure.json') as f:\n    d = json.load(f)\ns = d['samples']['lambada_openai'][0]\nprint('doc keys:', list(s['doc'].keys()) if isinstance(s['doc'], dict) else type(s['doc']))\nif isinstance(s['doc'], dict):\n    print('text preview:', s['doc'].get('text', '')[:200])\nprint('target:', repr(s['target']))\nprint('perplexity:', s.get('perplexity'))\nprint('acc:', s.get('acc'))\nprint('Total samples:', len(d['samples']['lambada_openai']))\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T13:18:01.914846+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"doc keys: ['text']\\ntext preview: In my palm is a clear stone, and inside it is a small ivory statuette. A guardian angel.\\n\\n\\\"Figured if you're going to be out at night getting hit by cars, you might as well have some backup.\\\"\\n\\nI look \\ntarget: ' signs'\\nperplexity: -3.03125\\nacc: 0\\nTotal samples: 5153\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.8}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-19T13:18:01.915012+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-48145",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\n# Check GDN h3-1 JSONL\nwith open('/root/entrainment_gated_ft/lm_eval_clean/1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl') as f:\n    s = json.loads(f.readline())\nprint('GDN h3-1 keys:', list(s.keys()))\nprint('doc_id:', s.get('doc_id'), 'acc:', s.get('acc'))\nhas_doc = 'doc' in s\nprint('has doc:', has_doc)\nif has_doc:\n    print('doc type:', type(s['doc']))\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-48145",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\n# Check GDN h3-1 JSONL\nwith open('/root/entrainment_gated_ft/lm_eval_clean/1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl') as f:\n    s = json.loads(f.readline())\nprint('GDN h3-1 keys:', list(s.keys()))\nprint('doc_id:', s.get('doc_id'), 'acc:', s.get('acc'))\nhas_doc = 'doc' in s\nprint('has doc:', has_doc)\nif has_doc:\n    print('doc type:', type(s['doc']))\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T13:18:01.915211+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"GDN h3-1 keys: ['doc_id', 'doc', 'target', 'arguments', 'resps', 'filtered_resps', 'filter', 'metrics', 'doc_hash', 'prompt_hash', 'target_hash', 'perplexity', 'acc']\\ndoc_id: 0 acc: 0\\nhas doc: True\\ndoc type: &lt;class 'dict'>\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.09}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-19T13:18:01.915381+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "ls /root/entrainment_gated_ft/lm_eval_clean/1.3b/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "ls /root/entrainment_gated_ft/lm_eval_clean/1.3b/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T13:18:01.915524+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"GDN-h24-1-logsamples\\nGDN-h3-1-logsamples\\nGDN-h6-1-logsamples\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.96}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-19T13:18:01.915712+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:TodoWrite",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T13:18:01.915851+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-19T13:18:01.915974+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Phase 0: Data validation', 'status': 'completed', 'activeForm': 'Validating data files'}, {'content': 'Phase 1-2: Write sample_characterization.py script', 'status': 'in_progress', 'activeForm': 'Writing sample characterization script'}, {'content': 'Phase 3: Upload and run script on server', 'status': 'pending', 'activeForm': 'Running script on server'}, {'content': 'Phase 4: Verify outputs and register artifacts', 'status': 'pending', 'activeForm': 'Verifying outputs and registering artifacts'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Phase 0: Data validation', 'status': 'completed', 'activeForm': 'Validating data files'}, {'content': 'Phase 1-2: Write sample_characterization.py script', 'status': 'in_progress', 'activeForm': 'Writing sample characterization script'}, {'content': 'Phase 3: Upload and run script on server', 'status': 'pending', 'activeForm': 'Running script on server'}, {'content': 'Phase 4: Verify outputs and register artifacts', 'status': 'pending', 'activeForm': 'Verifying outputs and registering artifacts'}]"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-19T13:18:01.916108+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-19T13:18:01.916262+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/analysis/sample_characterization.py",
  "content": "# Sample characterization analysis for LAMBADA per-example data\n# Computes features for helped/hurt samples across GDN, HGRN2, RetNet architectures\n\nimport json\nimport os\nimport numpy as np\nimport pandas as pd\nfrom collections import Counter\nfrom scipy import stats\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport matplotlib.gridspec as gridspec\nfrom transformers import AutoTokenizer\n\nOUT_DIR = '/root/entrainment_gated_ft/analysis'\nDATA_DIR = '/root/entrainment_gated_ft/lm_eval_clean'\nTOKENIZER_PATH = '/root/autodl-tmp/models_1.3b/1.3B-100B-GatedDeltaNet-pure/'\n\n# ── Data loading ─────────────────────────────────────────────────\n\ndef load_json_samples(path, task='lambada_openai'):\n    with open(path) as f:\n        d = json.load(f)\n    return sorted(d['samples'][task], key=lambda x: x['doc_id'])\n\ndef load_jsonl_samples(path):\n    samples = []\n    with open(path) as f:\n        for line in f:\n            samples.append(json.loads(line))\n    return sorted(samples, key=lambda x: x['doc_id'])\n\nprint(\"Loading model predictions...\")\nmodels = {\n    'GDN-pure':   load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-GatedDeltaNet-pure.json')),\n    'GDN-h31':    load_jsonl_samples(os.path.join(DATA_DIR, '1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl')),\n    'HGRN2-pure': load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-HGRN2-pure.json')),\n    'HGRN2-h31':  load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-HGRN2-hybrid-3-1.json')),\n    'RetNet-pure': load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-RetNet-pure.json')),\n    'RetNet-h31':  load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-RetNet-hybrid-3-1.json')),\n}\n\nn_samples = len(models['GDN-pure'])\nprint(f\"Loaded {n_samples} samples per model\")\n\n# ── Feature extraction ───────────────────────────────────────────\n\nprint(\"Loading tokenizer...\")\ntokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH)\n\ntexts = [s['doc']['text'] for s in models['GDN-pure']]\ntargets = [s['target'].strip() for s in models['GDN-pure']]\n\nprint(\"Tokenizing...\")\ntarget_freq = Counter(targets)\n\ncontext_lengths = []\ncontext_unique_tokens_list = []\n\nfor i, text in enumerate(texts):\n    token_ids = tokenizer.encode(text, add_special_tokens=False)\n    target_text = targets[i]\n    target_ids = tokenizer.encode(' ' + target_text, add_special_tokens=False)\n    n_target = len(target_ids)\n    context_ids = token_ids[:-n_target] if n_target > 0 else token_ids\n    context_lengths.append(len(context_ids))\n    context_unique_tokens_list.append(len(set(context_ids)))\n\nfeatures = pd.DataFrame({\n    'doc_id': [s['doc_id'] for s in models['GDN-pure']],\n    'target_token': targets,\n    'context_length': context_lengths,\n    'target_token_frequency': [target_freq[t] for t in targets],\n    'context_unique_tokens': context_unique_tokens_list,\n})\n\nprint(f\"Feature stats:\\n{features[['context_length', 'target_token_frequency', 'context_unique_tokens']].describe()}\")\n\n# ── Helped/Hurt identification ───────────────────────────────────\n\nARCHS = ['GDN', 'HGRN2', 'RetNet']\n\nacc_arrays = {}\nfor name, samples in models.items():\n    acc_arrays[name] = np.array([s['acc'] for s in samples])\n\nhelped = {}  # hybrid=1, pure=0\nhurt = {}    # hybrid=0, pure=1\n\nfor arch in ARCHS:\n    pure_acc = acc_arrays[f'{arch}-pure']\n    hybrid_acc = acc_arrays[f'{arch}-h31']\n    helped[arch] = (hybrid_acc == 1) & (pure_acc == 0)\n    hurt[arch] = (hybrid_acc == 0) & (pure_acc == 1)\n    print(f\"{arch}: helped={helped[arch].sum()}, hurt={hurt[arch].sum()}, \"\n          f\"both_correct={(hybrid_acc & pure_acc).sum()}, both_wrong={((1-hybrid_acc) * (1-pure_acc)).astype(int).sum()}\")\n\n# ── Statistical tests ────────────────────────────────────────────\n\nFEATURE_COLS = ['context_length', 'target_token_frequency', 'context_unique_tokens']\n\nstat_rows = []\n\n# Per-architecture: helped vs hurt\nfor arch in ARCHS:\n    h_mask = helped[arch]\n    r_mask = hurt[arch]\n    if h_mask.sum() < 2 or r_mask.sum() < 2:\n        print(f\"WARNING: {arch} has too few helped/hurt samples for stats\")\n        continue\n    for feat in FEATURE_COLS:\n        vals_h = features.loc[h_mask, feat].values\n        vals_r = features.loc[r_mask, feat].values\n        u_stat, p_val = stats.mannwhitneyu(vals_h, vals_r, alternative='two-sided')\n        n1, n2 = len(vals_h), len(vals_r)\n        rank_biserial = 1 - (2 * u_stat) / (n1 * n2)\n        stat_rows.append({\n            'comparison': f'{arch}: helped vs hurt',\n            'feature': feat,\n            'helped_median': np.median(vals_h),\n            'hurt_median': np.median(vals_r),\n            'helped_mean': np.mean(vals_h),\n            'hurt_mean': np.mean(vals_r),\n            'helped_n': n1,\n            'hurt_n': n2,\n            'U_statistic': u_stat,\n            'p_value': p_val,\n            'rank_biserial_r': rank_biserial,\n        })\n\n# Cross-architecture: helped vs helped\nfor i, a1 in enumerate(ARCHS):\n    for a2 in ARCHS[i+1:]:\n        m1 = helped[a1]\n        m2 = helped[a2]\n        if m1.sum() < 2 or m2.sum() < 2:\n            continue\n        for feat in FEATURE_COLS:\n            v1 = features.loc[m1, feat].values\n            v2 = features.loc[m2, feat].values\n            u_stat, p_val = stats.mannwhitneyu(v1, v2, alternative='two-sided')\n            n1, n2 = len(v1), len(v2)\n            rank_biserial = 1 - (2 * u_stat) / (n1 * n2)\n            stat_rows.append({\n                'comparison': f'helped: {a1} vs {a2}',\n                'feature': feat,\n                'helped_median': np.median(v1),\n                'hurt_median': np.median(v2),\n                'helped_mean': np.mean(v1),\n                'hurt_mean': np.mean(v2),\n                'helped_n': n1,\n                'hurt_n': n2,\n                'U_statistic': u_stat,\n                'p_value': p_val,\n                'rank_biserial_r': rank_biserial,\n            })\n\nstats_df = pd.DataFrame(stat_rows)\nstats_path = os.path.join(OUT_DIR, 'sample_characterization_results.csv')\nstats_df.to_csv(stats_path, index=False)\nprint(f\"\\nStatistical results saved to {stats_path}\")\nprint(stats_df.to_string(index=False))\n\n# ── Visualization ────────────────────────────────────────────────\n\nfig = plt.figure(figsize=(18, 14))\ngs = gridspec.GridSpec(2, 3, hspace=0.35, wspace=0.3)\n\nfeat_labels = {\n    'context_length': 'Context Length\\n(tokens)',\n    'target_token_frequency': 'Target Token\\nFrequency',\n    'context_unique_tokens': 'Context Unique\\nTokens',\n}\n\narch_colors = {\n    'GDN': ('#2196F3', '#90CAF9'),\n    'HGRN2': ('#FF5722', '#FFAB91'),\n    'RetNet': ('#4CAF50', '#A5D6A7'),\n}\n\n# Upper row: per-architecture helped vs hurt\nfor col, arch in enumerate(ARCHS):\n    ax = fig.add_subplot(gs[0, col])\n    h_mask = helped[arch]\n    r_mask = hurt[arch]\n\n    data_helped = []\n    data_hurt = []\n    positions = []\n    for fi, feat in enumerate(FEATURE_COLS):\n        data_helped.append(features.loc[h_mask, feat].values)\n        data_hurt.append(features.loc[r_mask, feat].values)\n        positions.append(fi)\n\n    # Normalize each feature to [0,1] for comparable violin plots\n    all_vals = [np.concatenate([data_helped[i], data_hurt[i]]) for i in range(len(FEATURE_COLS))]\n    mins = [v.min() for v in all_vals]\n    maxs = [v.max() for v in all_vals]\n\n    bp_positions_h = [p - 0.18 for p in positions]\n    bp_positions_r = [p + 0.18 for p in positions]\n\n    norm_h = [(data_helped[i] - mins[i]) / (maxs[i] - mins[i] + 1e-8) for i in range(len(FEATURE_COLS))]\n    norm_r = [(data_hurt[i] - mins[i]) / (maxs[i] - mins[i] + 1e-8) for i in range(len(FEATURE_COLS))]\n\n    vp1 = ax.violinplot(norm_h, positions=bp_positions_h, widths=0.3, showextrema=False)\n    for body in vp1['bodies']:\n        body.set_facecolor(arch_colors[arch][0])\n        body.set_alpha(0.7)\n\n    vp2 = ax.violinplot(norm_r, positions=bp_positions_r, widths=0.3, showextrema=False)\n    for body in vp2['bodies']:\n        body.set_facecolor(arch_colors[arch][1])\n        body.set_alpha(0.7)\n\n    # Add median markers\n    for i in range(len(FEATURE_COLS)):\n        med_h = np.median(norm_h[i])\n        med_r = np.median(norm_r[i])\n        ax.plot(bp_positions_h[i], med_h, 'o', color='white', markeredgecolor=arch_colors[arch][0], markersize=6, zorder=5)\n        ax.plot(bp_positions_r[i], med_r, 'o', color='white', markeredgecolor=arch_colors[arch][1], markersize=6, zorder=5)\n\n    ax.set_xticks(positions)\n    ax.set_xticklabels([feat_labels[f] for f in FEATURE_COLS], fontsize=8)\n    ax.set_ylabel('Normalized value', fontsize=9)\n    ax.set_title(f'{arch} (h={helped[arch].sum()}, r={hurt[arch].sum()})', fontsize=11, fontweight='bold')\n\n    if col == 0:\n        from matplotlib.patches import Patch\n        ax.legend(handles=[\n            Patch(facecolor=arch_colors[arch][0], alpha=0.7, label='Helped'),\n            Patch(facecolor=arch_colors[arch][1], alpha=0.7, label='Hurt'),\n        ], fontsize=8, loc='upper right')\n\n    # Add p-value annotations\n    for i, feat in enumerate(FEATURE_COLS):\n        match = stats_df[(stats_df['comparison'] == f'{arch}: helped vs hurt') & (stats_df['feature'] == feat)]\n        if len(match) > 0:\n            p = match.iloc[0]['p_value']\n            sig = '***' if p < 0.001 else '**' if p < 0.01 else '*' if p < 0.05 else 'n.s.'\n            ax.text(positions[i], 1.05, sig, ha='center', fontsize=8, color='black')\n\n    ax.set_ylim(-0.1, 1.2)\n\n# Lower row: cross-architecture helped comparison\nfor col, feat in enumerate(FEATURE_COLS):\n    ax = fig.add_subplot(gs[1, col])\n\n    data = []\n    labels = []\n    colors = []\n    for arch in ARCHS:\n        h_mask = helped[arch]\n        if h_mask.sum() > 0:\n            data.append(features.loc[h_mask, feat].values)\n            labels.append(f'{arch}\\n(n={h_mask.sum()})')\n            colors.append(arch_colors[arch][0])\n\n    vp = ax.violinplot(data, positions=range(len(data)), widths=0.6, showextrema=False)\n    for i, body in enumerate(vp['bodies']):\n        body.set_facecolor(colors[i])\n        body.set_alpha(0.7)\n\n    # Median + IQR\n    for i, d in enumerate(data):\n        med = np.median(d)\n        q1, q3 = np.percentile(d, [25, 75])\n        ax.vlines(i, q1, q3, color='black', linewidth=2)\n        ax.scatter(i, med, color='white', edgecolor='black', s=40, zorder=5)\n\n    ax.set_xticks(range(len(labels)))\n    ax.set_xticklabels(labels, fontsize=9)\n    ax.set_ylabel(feat.replace('_', ' ').title(), fontsize=9)\n    ax.set_title(f'Helped samples: {feat_labels[feat].replace(chr(10), \" \")}', fontsize=10, fontweight='bold')\n\n    # Add cross-arch p-values\n    y_max = max(d.max() for d in data)\n    y_step = (y_max - min(d.min() for d in data)) * 0.08\n    y_pos = y_max + y_step\n    for i, a1 in enumerate(ARCHS):\n        for j, a2 in enumerate(ARCHS):\n            if j <= i:\n                continue\n            match = stats_df[(stats_df['comparison'] == f'helped: {a1} vs {a2}') & (stats_df['feature'] == feat)]\n            if len(match) > 0:\n                p = match.iloc[0]['p_value']\n                sig = '***' if p < 0.001 else '**' if p < 0.01 else '*' if p < 0.05 else 'n.s.'\n                if sig != 'n.s.':\n                    idx_a1 = ARCHS.index(a1)\n                    idx_a2 = ARCHS.index(a2)\n                    ax.plot([idx_a1, idx_a2], [y_pos, y_pos], 'k-', linewidth=0.8)\n                    ax.text((idx_a1 + idx_a2) / 2, y_pos, sig, ha='center', va='bottom', fontsize=7)\n                    y_pos += y_step * 1.5\n\nfig.suptitle('LAMBADA Sample Characterization: Helped vs Hurt by Attention Hybridization',\n             fontsize=14, fontweight='bold', y=0.98)\n\nfor fmt in ['pdf', 'png']:\n    path = os.path.join(OUT_DIR, f'sample_characterization.{fmt}')\n    fig.savefig(path, dpi=200, bbox_inches='tight')\n    print(f\"Figure saved: {path}\")\n\nplt.close()\nprint(\"\\nDone.\")\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/analysis/sample_characterization.py",
    "content": "# Sample characterization analysis for LAMBADA per-example data\n# Computes features for helped/hurt samples across GDN, HGRN2, RetNet architectures\n\nimport json\nimport os\nimport numpy as np\nimport pandas as pd\nfrom collections import Counter\nfrom scipy import stats\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport matplotlib.gridspec as gridspec\nfrom transformers import AutoTokenizer\n\nOUT_DIR = '/root/entrainment_gated_ft/analysis'\nDATA_DIR = '/root/entrainment_gated_ft/lm_eval_clean'\nTOKENIZER_PATH = '/root/autodl-tmp/models_1.3b/1.3B-100B-GatedDeltaNet-pure/'\n\n# ── Data loading ─────────────────────────────────────────────────\n\ndef load_json_samples(path, task='lambada_openai'):\n    with open(path) as f:\n        d = json.load(f)\n    return sorted(d['samples'][task], key=lambda x: x['doc_id'])\n\ndef load_jsonl_samples(path):\n    samples = []\n    with open(path) as f:\n        for line in f:\n            samples.append(json.loads(line))\n    return sorted(samples, key=lambda x: x['doc_id'])\n\nprint(\"Loading model predictions...\")\nmodels = {\n    'GDN-pure':   load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-GatedDeltaNet-pure.json')),\n    'GDN-h31':    load_jsonl_samples(os.path.join(DATA_DIR, '1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl')),\n    'HGRN2-pure': load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-HGRN2-pure.json')),\n    'HGRN2-h31':  load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-HGRN2-hybrid-3-1.json')),\n    'RetNet-pure': load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-RetNet-pure.json')),\n    'RetNet-h31':  load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-RetNet-hybrid-3-1.json')),\n}\n\nn_samples = len(models['GDN-pure'])\nprint(f\"Loaded {n_samples} samples per model\")\n\n# ── Feature extraction ───────────────────────────────────────────\n\nprint(\"Loading tokenizer...\")\ntokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH)\n\ntexts = [s['doc']['text'] for s in models['GDN-pure']]\ntargets = [s['target'].strip() for s in models['GDN-pure']]\n\nprint(\"Tokenizing...\")\ntarget_freq = Counter(targets)\n\ncontext_lengths = []\ncontext_unique_tokens_list = []\n\nfor i, text in enumerate(texts):\n    token_ids = tokenizer.encode(text, add_special_tokens=False)\n    target_text = targets[i]\n    target_ids = tokenizer.encode(' ' + target_text, add_special_tokens=False)\n    n_target = len(target_ids)\n    context_ids = token_ids[:-n_target] if n_target > 0 else token_ids\n    context_lengths.append(len(context_ids))\n    context_unique_tokens_list.append(len(set(context_ids)))\n\nfeatures = pd.DataFrame({\n    'doc_id': [s['doc_id'] for s in models['GDN-pure']],\n    'target_token': targets,\n    'context_length': context_lengths,\n    'target_token_frequency': [target_freq[t] for t in targets],\n    'context_unique_tokens': context_unique_tokens_list,\n})\n\nprint(f\"Feature stats:\\n{features[['context_length', 'target_token_frequency', 'context_unique_tokens']].describe()}\")\n\n# ── Helped/Hurt identification ───────────────────────────────────\n\nARCHS = ['GDN', 'HGRN2', 'RetNet']\n\nacc_arrays = {}\nfor name, samples in models.items():\n    acc_arrays[name] = np.array([s['acc'] for s in samples])\n\nhelped = {}  # hybrid=1, pure=0\nhurt = {}    # hybrid=0, pure=1\n\nfor arch in ARCHS:\n    pure_acc = acc_arrays[f'{arch}-pure']\n    hybrid_acc = acc_arrays[f'{arch}-h31']\n    helped[arch] = (hybrid_acc == 1) & (pure_acc == 0)\n    hurt[arch] = (hybrid_acc == 0) & (pure_acc == 1)\n    print(f\"{arch}: helped={helped[arch].sum()}, hurt={hurt[arch].sum()}, \"\n          f\"both_correct={(hybrid_acc & pure_acc).sum()}, both_wrong={((1-hybrid_acc) * (1-pure_acc)).astype(int).sum()}\")\n\n# ── Statistical tests ────────────────────────────────────────────\n\nFEATURE_COLS = ['context_length', 'target_token_frequency', 'context_unique_tokens']\n\nstat_rows = []\n\n# Per-architecture: helped vs hurt\nfor arch in ARCHS:\n    h_mask = helped[arch]\n    r_mask = hurt[arch]\n    if h_mask.sum() < 2 or r_mask.sum() < 2:\n        print(f\"WARNING: {arch} has too few helped/hurt samples for stats\")\n        continue\n    for feat in FEATURE_COLS:\n        vals_h = features.loc[h_mask, feat].values\n        vals_r = features.loc[r_mask, feat].values\n        u_stat, p_val = stats.mannwhitneyu(vals_h, vals_r, alternative='two-sided')\n        n1, n2 = len(vals_h), len(vals_r)\n        rank_biserial = 1 - (2 * u_stat) / (n1 * n2)\n        stat_rows.append({\n            'comparison': f'{arch}: helped vs hurt',\n            'feature': feat,\n            'helped_median': np.median(vals_h),\n            'hurt_median': np.median(vals_r),\n            'helped_mean': np.mean(vals_h),\n            'hurt_mean': np.mean(vals_r),\n            'helped_n': n1,\n            'hurt_n': n2,\n            'U_statistic': u_stat,\n            'p_value': p_val,\n            'rank_biserial_r': rank_biserial,\n        })\n\n# Cross-architecture: helped vs helped\nfor i, a1 in enumerate(ARCHS):\n    for a2 in ARCHS[i+1:]:\n        m1 = helped[a1]\n        m2 = helped[a2]\n        if m1.sum() < 2 or m2.sum() < 2:\n            continue\n        for feat in FEATURE_COLS:\n            v1 = features.loc[m1, feat].values\n            v2 = features.loc[m2, feat].values\n            u_stat, p_val = stats.mannwhitneyu(v1, v2, alternative='two-sided')\n            n1, n2 = len(v1), len(v2)\n            rank_biserial = 1 - (2 * u_stat) / (n1 * n2)\n            stat_rows.append({\n                'comparison': f'helped: {a1} vs {a2}',\n                'feature': feat,\n                'helped_median': np.median(v1),\n                'hurt_median': np.median(v2),\n                'helped_mean': np.mean(v1),\n                'hurt_mean': np.mean(v2),\n                'helped_n': n1,\n                'hurt_n': n2,\n                'U_statistic': u_stat,\n                'p_value': p_val,\n                'rank_biserial_r': rank_biserial,\n            })\n\nstats_df = pd.DataFrame(stat_rows)\nstats_path = os.path.join(OUT_DIR, 'sample_characterization_results.csv')\nstats_df.to_csv(stats_path, index=False)\nprint(f\"\\nStatistical results saved to {stats_path}\")\nprint(stats_df.to_string(index=False))\n\n# ── Visualization ────────────────────────────────────────────────\n\nfig = plt.figure(figsize=(18, 14))\ngs = gridspec.GridSpec(2, 3, hspace=0.35, wspace=0.3)\n\nfeat_labels = {\n    'context_length': 'Context Length\\n(tokens)',\n    'target_token_frequency': 'Target Token\\nFrequency',\n    'context_unique_tokens': 'Context Unique\\nTokens',\n}\n\narch_colors = {\n    'GDN': ('#2196F3', '#90CAF9'),\n    'HGRN2': ('#FF5722', '#FFAB91'),\n    'RetNet': ('#4CAF50', '#A5D6A7'),\n}\n\n# Upper row: per-architecture helped vs hurt\nfor col, arch in enumerate(ARCHS):\n    ax = fig.add_subplot(gs[0, col])\n    h_mask = helped[arch]\n    r_mask = hurt[arch]\n\n    data_helped = []\n    data_hurt = []\n    positions = []\n    for fi, feat in enumerate(FEATURE_COLS):\n        data_helped.append(features.loc[h_mask, feat].values)\n        data_hurt.append(features.loc[r_mask, feat].values)\n        positions.append(fi)\n\n    # Normalize each feature to [0,1] for comparable violin plots\n    all_vals = [np.concatenate([data_helped[i], data_hurt[i]]) for i in range(len(FEATURE_COLS))]\n    mins = [v.min() for v in all_vals]\n    maxs = [v.max() for v in all_vals]\n\n    bp_positions_h = [p - 0.18 for p in positions]\n    bp_positions_r = [p + 0.18 for p in positions]\n\n    norm_h = [(data_helped[i] - mins[i]) / (maxs[i] - mins[i] + 1e-8) for i in range(len(FEATURE_COLS))]\n    norm_r = [(data_hurt[i] - mins[i]) / (maxs[i] - mins[i] + 1e-8) for i in range(len(FEATURE_COLS))]\n\n    vp1 = ax.violinplot(norm_h, positions=bp_positions_h, widths=0.3, showextrema=False)\n    for body in vp1['bodies']:\n        body.set_facecolor(arch_colors[arch][0])\n        body.set_alpha(0.7)\n\n    vp2 = ax.violinplot(norm_r, positions=bp_positions_r, widths=0.3, showextrema=False)\n    for body in vp2['bodies']:\n        body.set_facecolor(arch_colors[arch][1])\n        body.set_alpha(0.7)\n\n    # Add median markers\n    for i in range(len(FEATURE_COLS)):\n        med_h = np.median(norm_h[i])\n        med_r = np.median(norm_r[i])\n        ax.plot(bp_positions_h[i], med_h, 'o', color='white', markeredgecolor=arch_colors[arch][0], markersize=6, zorder=5)\n        ax.plot(bp_positions_r[i], med_r, 'o', color='white', markeredgecolor=arch_colors[arch][1], markersize=6, zorder=5)\n\n    ax.set_xticks(positions)\n    ax.set_xticklabels([feat_labels[f] for f in FEATURE_COLS], fontsize=8)\n    ax.set_ylabel('Normalized value', fontsize=9)\n    ax.set_title(f'{arch} (h={helped[arch].sum()}, r={hurt[arch].sum()})', fontsize=11, fontweight='bold')\n\n    if col == 0:\n        from matplotlib.patches import Patch\n        ax.legend(handles=[\n            Patch(facecolor=arch_colors[arch][0], alpha=0.7, label='Helped'),\n            Patch(facecolor=arch_colors[arch][1], alpha=0.7, label='Hurt'),\n        ], fontsize=8, loc='upper right')\n\n    # Add p-value annotations\n    for i, feat in enumerate(FEATURE_COLS):\n        match = stats_df[(stats_df['comparison'] == f'{arch}: helped vs hurt') & (stats_df['feature'] == feat)]\n        if len(match) > 0:\n            p = match.iloc[0]['p_value']\n            sig = '***' if p < 0.001 else '**' if p < 0.01 else '*' if p < 0.05 else 'n.s.'\n            ax.text(positions[i], 1.05, sig, ha='center', fontsize=8, color='black')\n\n    ax.set_ylim(-0.1, 1.2)\n\n# Lower row: cross-architecture helped comparison\nfor col, feat in enumerate(FEATURE_COLS):\n    ax = fig.add_subplot(gs[1, col])\n\n    data = []\n    labels = []\n    colors = []\n    for arch in ARCHS:\n        h_mask = helped[arch]\n        if h_mask.sum() > 0:\n            data.append(features.loc[h_mask, feat].values)\n            labels.append(f'{arch}\\n(n={h_mask.sum()})')\n            colors.append(arch_colors[arch][0])\n\n    vp = ax.violinplot(data, positions=range(len(data)), widths=0.6, showextrema=False)\n    for i, body in enumerate(vp['bodies']):\n        body.set_facecolor(colors[i])\n        body.set_alpha(0.7)\n\n    # Median + IQR\n    for i, d in enumerate(data):\n        med = np.median(d)\n        q1, q3 = np.percentile(d, [25, 75])\n        ax.vlines(i, q1, q3, color='black', linewidth=2)\n        ax.scatter(i, med, color='white', edgecolor='black', s=40, zorder=5)\n\n    ax.set_xticks(range(len(labels)))\n    ax.set_xticklabels(labels, fontsize=9)\n    ax.set_ylabel(feat.replace('_', ' ').title(), fontsize=9)\n    ax.set_title(f'Helped samples: {feat_labels[feat].replace(chr(10), \" \")}', fontsize=10, fontweight='bold')\n\n    # Add cross-arch p-values\n    y_max = max(d.max() for d in data)\n    y_step = (y_max - min(d.min() for d in data)) * 0.08\n    y_pos = y_max + y_step\n    for i, a1 in enumerate(ARCHS):\n        for j, a2 in enumerate(ARCHS):\n            if j <= i:\n                continue\n            match = stats_df[(stats_df['comparison'] == f'helped: {a1} vs {a2}') & (stats_df['feature'] == feat)]\n            if len(match) > 0:\n                p = match.iloc[0]['p_value']\n                sig = '***' if p < 0.001 else '**' if p < 0.01 else '*' if p < 0.05 else 'n.s.'\n                if sig != 'n.s.':\n                    idx_a1 = ARCHS.index(a1)\n                    idx_a2 = ARCHS.index(a2)\n                    ax.plot([idx_a1, idx_a2], [y_pos, y_pos], 'k-', linewidth=0.8)\n                    ax.text((idx_a1 + idx_a2) / 2, y_pos, sig, ha='center', va='bottom', fontsize=7)\n                    y_pos += y_step * 1.5\n\nfig.suptitle('LAMBADA Sample Characterization: Helped vs Hurt by Attention Hybridization',\n             fontsize=14, fontweight='bold', y=0.98)\n\nfor fmt in ['pdf', 'png']:\n    path = os.path.join(OUT_DIR, f'sample_characterization.{fmt}')\n    fig.savefig(path, dpi=200, bbox_inches='tight')\n    print(f\"Figure saved: {path}\")\n\nplt.close()\nprint(\"\\nDone.\")\n"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-19T13:18:01.916548+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/analysis/sample_characterization.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-19T13:18:01.916720+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Phase 0: Data validation', 'status': 'completed', 'activeForm': 'Validating data files'}, {'content': 'Phase 1-2: Write sample_characterization.py script', 'status': 'completed', 'activeForm': 'Writing sample characterization script'}, {'content': 'Phase 3: Upload and run script on server', 'status': 'in_progress', 'activeForm': 'Running script on server'}, {'content': 'Phase 4: Verify outputs and register artifacts', 'status': 'pending', 'activeForm': 'Verifying outputs and registering artifacts'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Phase 0: Data validation', 'status': 'completed', 'activeForm': 'Validating data files'}, {'content': 'Phase 1-2: Write sample_characterization.py script', 'status': 'completed', 'activeForm': 'Writing sample characterization script'}, {'content': 'Phase 3: Upload and run script on server', 'status': 'in_progress', 'activeForm': 'Running script on server'}, {'content': 'Phase 4: Verify outputs and register artifacts', 'status': 'pending', 'activeForm': 'Verifying outputs and registering artifacts'}]"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-19T13:18:01.916864+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-19T13:18:01.916986+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/analysis/sample_characterization.py | ssh connect.westb.seetacloud.com \"cat > /root/entrainment_gated_ft/analysis/sample_characterization.py\"",
  "description": "Upload script to remote server",
  "timeout": "15000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/analysis/sample_characterization.py | ssh connect.westb.seetacloud.com \"cat > /root/entrainment_gated_ft/analysis/sample_characterization.py\"",
    "description": "Upload script to remote server",
    "timeout": "15000"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-19T13:18:01.917112+00:00_

Exit code 255
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
ssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory
Permission denied, please try again.
ssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory
Permission denied, please try again.
ssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory
ubuntu@connect.westb.seetacloud.com: Permission denied ().

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-19T13:18:01.917260+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/analysis/sample_characterization.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/analysis/sample_characterization.py"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-19T13:18:01.917461+00:00_

1	# Sample characterization analysis for LAMBADA per-example data
2	# Computes features for helped/hurt samples across GDN, HGRN2, RetNet architectures
3	
4	import json
5	import os
6	import numpy as np
7	import pandas as pd
8	from collections import Counter
9	from scipy import stats
10	import matplotlib
11	matplotlib.use('Agg')
12	import matplotlib.pyplot as plt
13	import matplotlib.gridspec as gridspec
14	from transformers import AutoTokenizer
15	
16	OUT_DIR = '/root/entrainment_gated_ft/analysis'
17	DATA_DIR = '/root/entrainment_gated_ft/lm_eval_clean'
18	TOKENIZER_PATH = '/root/autodl-tmp/models_1.3b/1.3B-100B-GatedDeltaNet-pure/'
19	
20	# ── Data loading ─────────────────────────────────────────────────
21	
22	def load_json_samples(path, task='lambada_openai'):
23	    with open(path) as f:
24	        d = json.load(f)
25	    return sorted(d['samples'][task], key=lambda x: x['doc_id'])
26	
27	def load_jsonl_samples(path):
28	    samples = []
29	    with open(path) as f:
30	        for line in f:
31	            samples.append(json.loads(line))
32	    return sorted(samples, key=lambda x: x['doc_id'])
33	
34	print("Loading model predictions...")
35	models = {
36	    'GDN-pure':   load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-GatedDeltaNet-pure.json')),
37	    'GDN-h31':    load_jsonl_samples(os.path.join(DATA_DIR, '1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl')),
38	    'HGRN2-pure': load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-HGRN2-pure.json')),
39	    'HGRN2-h31':  load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-HGRN2-hybrid-3-1.json')),
40	    'RetNet-pure': load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-RetNet-pure.json')),
41	    'RetNet-h31':  load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-RetNet-hybrid-3-1.json')),
42	}
43	
44	n_samples = len(models['GDN-pure'])
45	print(f"Loaded {n_samples} samples per model")
46	
47	# ── Feature extraction ───────────────────────────────────────────
48	
49	print("Loading tokenizer...")
50
…[truncated 10856 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-19T13:18:01.917661+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-48145",
  "command": "cat << 'PYEOF' > /root/entrainment_gated_ft/analysis/sample_characterization.py\n# Sample characterization analysis for LAMBADA per-example data\n# Computes features for helped/hurt samples across GDN, HGRN2, RetNet architectures\n\nimport json\nimport os\nimport numpy as np\nimport pandas as pd\nfrom collections import Counter\nfrom scipy import stats\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport matplotlib.gridspec as gridspec\nfrom transformers import AutoTokenizer\n\nOUT_DIR = '/root/entrainment_gated_ft/analysis'\nDATA_DIR = '/root/entrainment_gated_ft/lm_eval_clean'\nTOKENIZER_PATH = '/root/autodl-tmp/models_1.3b/1.3B-100B-GatedDeltaNet-pure/'\n\n# ── Data loading ─────────────────────────────────────────────────\n\ndef load_json_samples(path, task='lambada_openai'):\n    with open(path) as f:\n        d = json.load(f)\n    return sorted(d['samples'][task], key=lambda x: x['doc_id'])\n\ndef load_jsonl_samples(path):\n    samples = []\n    with open(path) as f:\n        for line in f:\n            samples.append(json.loads(line))\n    return sorted(samples, key=lambda x: x['doc_id'])\n\nprint(\"Loading model predictions...\")\nmodels = {\n    'GDN-pure':   load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-GatedDeltaNet-pure.json')),\n    'GDN-h31':    load_jsonl_samples(os.path.join(DATA_DIR, '1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl')),\n    'HGRN2-pure': load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-HGRN2-pure.json')),\n    'HGRN2-h31':  load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-HGRN2-hybrid-3-1.json')),\n    'RetNet-pure': load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-RetNet-pure.json')),\n    'RetNet-h31':  load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-RetNet-hybrid-3-1.json')),\n}\n\nn_samples = len(models['GDN-pure'])\nprint(f\"Loaded {n_samples} samples per model\")\n\n# ── Feature extraction ───────────────────────────────────────────\n\nprint(\"Loading tokenizer...\")\ntokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH)\n\ntexts = [s['doc']['text'] for s in models['GDN-pure']]\ntargets = [s['target'].strip() for s in models['GDN-pure']]\n\nprint(\"Tokenizing...\")\ntarget_freq = Counter(targets)\n\ncontext_lengths = []\ncontext_unique_tokens_list = []\n\nfor i, text in enumerate(texts):\n    token_ids = tokenizer.encode(text, add_special_tokens=False)\n    target_text = targets[i]\n    target_ids = tokenizer.encode(' ' + target_text, add_special_tokens=False)\n    n_target = len(target_ids)\n    context_ids = token_ids[:-n_target] if n_target > 0 else token_ids\n    context_lengths.append(len(context_ids))\n    context_unique_tokens_list.append(len(set(context_ids)))\n\nfeatures = pd.DataFrame({\n    'doc_id': [s['doc_id'] for s in models['GDN-pure']],\n    'target_token': targets,\n    'context_length': context_lengths,\n    'target_token_frequency': [target_freq[t] for t in targets],\n    'context_unique_tokens': context_unique_tokens_list,\n})\n\nprint(f\"Feature stats:\\n{features[['context_length', 'target_token_frequency', 'context_unique_tokens']].describe()}\")\n\n# ── Helped/Hurt identification ───────────────────────────────────\n\nARCHS = ['GDN', 'HGRN2', 'RetNet']\n\nacc_arrays = {}\nfor name, samples in models.items():\n    acc_arrays[name] = np.array([s['acc'] for s in samples])\n\nhelped = {}  # hybrid=1, pure=0\nhurt = {}    # hybrid=0, pure=1\n\nfor arch in ARCHS:\n    pure_acc = acc_arrays[f'{arch}-pure']\n    hybrid_acc = acc_arrays[f'{arch}-h31']\n    helped[arch] = (hybrid_acc == 1) & (pure_acc == 0)\n    hurt[arch] = (hybrid_acc == 0) & (pure_acc == 1)\n    print(f\"{arch}: helped={helped[arch].sum()}, hurt={hurt[arch].sum()}, \"\n          f\"both_correct={(hybrid_acc & pure_acc).sum()}, both_wrong={((1-hybrid_acc) * (1-pure_acc)).astype(int).sum()}\")\n\n# ── Statistical tests ────────────────────────────────────────────\n\nFEATURE_COLS = ['context_length', 'target_token_frequency', 'context_unique_tokens']\n\nstat_rows = []\n\n# Per-architecture: helped vs hurt\nfor arch in ARCHS:\n    h_mask = helped[arch]\n    r_mask = hurt[arch]\n    if h_mask.sum() < 2 or r_mask.sum() < 2:\n        print(f\"WARNING: {arch} has too few helped/hurt samples for stats\")\n        continue\n    for feat in FEATURE_COLS:\n        vals_h = features.loc[h_mask, feat].values\n        vals_r = features.loc[r_mask, feat].values\n        u_stat, p_val = stats.mannwhitneyu(vals_h, vals_r, alternative='two-sided')\n        n1, n2 = len(vals_h), len(vals_r)\n        rank_biserial = 1 - (2 * u_stat) / (n1 * n2)\n        stat_rows.append({\n            'comparison': f'{arch}: helped vs hurt',\n            'feature': feat,\n            'helped_median': np.median(vals_h),\n            'hurt_median': np.median(vals_r),\n            'helped_mean': np.mean(vals_h),\n            'hurt_mean': np.mean(vals_r),\n            'helped_n': n1,\n            'hurt_n': n2,\n            'U_statistic': u_stat,\n            'p_value': p_val,\n            'rank_biserial_r': rank_biserial,\n        })\n\n# Cross-architecture: helped vs helped\nfor i, a1 in enumerate(ARCHS):\n    for a2 in ARCHS[i+1:]:\n        m1 = helped[a1]\n        m2 = helped[a2]\n        if m1.sum() < 2 or m2.sum() < 2:\n            continue\n        for feat in FEATURE_COLS:\n            v1 = features.loc[m1, feat].values\n            v2 = features.loc[m2, feat].values\n            u_stat, p_val = stats.mannwhitneyu(v1, v2, alternative='two-sided')\n            n1, n2 = len(v1), len(v2)\n            rank_biserial = 1 - (2 * u_stat) / (n1 * n2)\n            stat_rows.append({\n                'comparison': f'helped: {a1} vs {a2}',\n                'feature': feat,\n                'helped_median': np.median(v1),\n                'hurt_median': np.median(v2),\n                'helped_mean': np.mean(v1),\n                'hurt_mean': np.mean(v2),\n                'helped_n': n1,\n                'hurt_n': n2,\n                'U_statistic': u_stat,\n                'p_value': p_val,\n                'rank_biserial_r': rank_biserial,\n            })\n\nstats_df = pd.DataFrame(stat_rows)\nstats_path = os.path.join(OUT_DIR, 'sample_characterization_results.csv')\nstats_df.to_csv(stats_path, index=False)\nprint(f\"\\nStatistical results saved to {stats_path}\")\nprint(stats_df.to_string(index=False))\n\n# ── Visualization ────────────────────────────────────────────────\n\nfig = plt.figure(figsize=(18, 14))\ngs = gridspec.GridSpec(2, 3, hspace=0.35, wspace=0.3)\n\nfeat_labels = {\n    'context_length': 'Context Length\\n(tokens)',\n    'target_token_frequency': 'Target Token\\nFrequency',\n    'context_unique_tokens': 'Context Unique\\nTokens',\n}\n\narch_colors = {\n    'GDN': ('#2196F3', '#90CAF9'),\n    'HGRN2': ('#FF5722', '#FFAB91'),\n    'RetNet': ('#4CAF50', '#A5D6A7'),\n}\n\n# Upper row: per-architecture helped vs hurt\nfor col, arch in enumerate(ARCHS):\n    ax = fig.add_subplot(gs[0, col])\n    h_mask = helped[arch]\n    r_mask = hurt[arch]\n\n    data_helped = []\n    data_hurt = []\n    positions = []\n    for fi, feat in enumerate(FEATURE_COLS):\n        data_helped.append(features.loc[h_mask, feat].values)\n        data_hurt.append(features.loc[r_mask, feat].values)\n        positions.append(fi)\n\n    # Normalize each feature to [0,1] for comparable violin plots\n    all_vals = [np.concatenate([data_helped[i], data_hurt[i]]) for i in range(len(FEATURE_COLS))]\n    mins = [v.min() for v in all_vals]\n    maxs = [v.max() for v in all_vals]\n\n    bp_positions_h = [p - 0.18 for p in positions]\n    bp_positions_r = [p + 0.18 for p in positions]\n\n    norm_h = [(data_helped[i] - mins[i]) / (maxs[i] - mins[i] + 1e-8) for i in range(len(FEATURE_COLS))]\n    norm_r = [(data_hurt[i] - mins[i]) / (maxs[i] - mins[i] + 1e-8) for i in range(len(FEATURE_COLS))]\n\n    vp1 = ax.violinplot(norm_h, positions=bp_positions_h, widths=0.3, showextrema=False)\n    for body in vp1['bodies']:\n        body.set_facecolor(arch_colors[arch][0])\n        body.set_alpha(0.7)\n\n    vp2 = ax.violinplot(norm_r, positions=bp_positions_r, widths=0.3, showextrema=False)\n    for body in vp2['bodies']:\n        body.set_facecolor(arch_colors[arch][1])\n        body.set_alpha(0.7)\n\n    # Add median markers\n    for i in range(len(FEATURE_COLS)):\n        med_h = np.median(norm_h[i])\n        med_r = np.median(norm_r[i])\n        ax.plot(bp_positions_h[i], med_h, 'o', color='white', markeredgecolor=arch_colors[arch][0], markersize=6, zorder=5)\n        ax.plot(bp_positions_r[i], med_r, 'o', color='white', markeredgecolor=arch_colors[arch][1], markersize=6, zorder=5)\n\n    ax.set_xticks(positions)\n    ax.set_xticklabels([feat_labels[f] for f in FEATURE_COLS], fontsize=8)\n    ax.set_ylabel('Normalized value', fontsize=9)\n    ax.set_title(f'{arch} (h={helped[arch].sum()}, r={hurt[arch].sum()})', fontsize=11, fontweight='bold')\n\n    if col == 0:\n        from matplotlib.patches import Patch\n        ax.legend(handles=[\n            Patch(facecolor=arch_colors[arch][0], alpha=0.7, label='Helped'),\n            Patch(facecolor=arch_colors[arch][1], alpha=0.7, label='Hurt'),\n        ], fontsize=8, loc='upper right')\n\n    # Add p-value annotations\n    for i, feat in enumerate(FEATURE_COLS):\n        match = stats_df[(stats_df['comparison'] == f'{arch}: helped vs hurt') & (stats_df['feature'] == feat)]\n        if len(match) > 0:\n            p = match.iloc[0]['p_value']\n            sig = '***' if p < 0.001 else '**' if p < 0.01 else '*' if p < 0.05 else 'n.s.'\n            ax.text(positions[i], 1.05, sig, ha='center', fontsize=8, color='black')\n\n    ax.set_ylim(-0.1, 1.2)\n\n# Lower row: cross-architecture helped comparison\nfor col, feat in enumerate(FEATURE_COLS):\n    ax = fig.add_subplot(gs[1, col])\n\n    data = []\n    labels = []\n    colors = []\n    for arch in ARCHS:\n        h_mask = helped[arch]\n        if h_mask.sum() > 0:\n            data.append(features.loc[h_mask, feat].values)\n            labels.append(f'{arch}\\n(n={h_mask.sum()})')\n            colors.append(arch_colors[arch][0])\n\n    vp = ax.violinplot(data, positions=range(len(data)), widths=0.6, showextrema=False)\n    for i, body in enumerate(vp['bodies']):\n        body.set_facecolor(colors[i])\n        body.set_alpha(0.7)\n\n    # Median + IQR\n    for i, d in enumerate(data):\n        med = np.median(d)\n        q1, q3 = np.percentile(d, [25, 75])\n        ax.vlines(i, q1, q3, color='black', linewidth=2)\n        ax.scatter(i, med, color='white', edgecolor='black', s=40, zorder=5)\n\n    ax.set_xticks(range(len(labels)))\n    ax.set_xticklabels(labels, fontsize=9)\n    ax.set_ylabel(feat.replace('_', ' ').title(), fontsize=9)\n    ax.set_title(f'Helped samples: {feat_labels[feat].replace(chr(10), \" \")}', fontsize=10, fontweight='bold')\n\n    # Add cross-arch p-values\n    y_max = max(d.max() for d in data)\n    y_step = (y_max - min(d.min() for d in data)) * 0.08\n    y_pos = y_max + y_step\n    for i, a1 in enumerate(ARCHS):\n        for j, a2 in enumerate(ARCHS):\n            if j <= i:\n                continue\n            match = stats_df[(stats_df['comparison'] == f'helped: {a1} vs {a2}') & (stats_df['feature'] == feat)]\n            if len(match) > 0:\n                p = match.iloc[0]['p_value']\n                sig = '***' if p < 0.001 else '**' if p < 0.01 else '*' if p < 0.05 else 'n.s.'\n                if sig != 'n.s.':\n                    idx_a1 = ARCHS.index(a1)\n                    idx_a2 = ARCHS.index(a2)\n                    ax.plot([idx_a1, idx_a2], [y_pos, y_pos], 'k-', linewidth=0.8)\n                    ax.text((idx_a1 + idx_a2) / 2, y_pos, sig, ha='center', va='bottom', fontsize=7)\n                    y_pos += y_step * 1.5\n\nfig.suptitle('LAMBADA Sample Characterization: Helped vs Hurt by Attention Hybridization',\n             fontsize=14, fontweight='bold', y=0.98)\n\nfor fmt in ['pdf', 'png']:\n    path = os.path.join(OUT_DIR, f'sample_characterization.{fmt}')\n    fig.savefig(path, dpi=200, bbox_inches='tight')\n    print(f\"Figure saved: {path}\")\n\nplt.close()\nprint(\"\\nDone.\")\nPYEOF\necho \"Script written: $(wc -l /root/entrainment_gated_ft/analysis/sample_characterization.py)\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-48145",
    "command": "cat << 'PYEOF' > /root/entrainment_gated_ft/analysis/sample_characterization.py\n# Sample characterization analysis for LAMBADA per-example data\n# Computes features for helped/hurt samples across GDN, HGRN2, RetNet architectures\n\nimport json\nimport os\nimport numpy as np\nimport pandas as pd\nfrom collections import Counter\nfrom scipy import stats\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport matplotlib.gridspec as gridspec\nfrom transformers import AutoTokenizer\n\nOUT_DIR = '/root/entrainment_gated_ft/analysis'\nDATA_DIR = '/root/entrainment_gated_ft/lm_eval_clean'\nTOKENIZER_PATH = '/root/autodl-tmp/models_1.3b/1.3B-100B-GatedDeltaNet-pure/'\n\n# ── Data loading ─────────────────────────────────────────────────\n\ndef load_json_samples(path, task='lambada_openai'):\n    with open(path) as f:\n        d = json.load(f)\n    return sorted(d['samples'][task], key=lambda x: x['doc_id'])\n\ndef load_jsonl_samples(path):\n    samples = []\n    with open(path) as f:\n        for line in f:\n            samples.append(json.loads(line))\n    return sorted(samples, key=lambda x: x['doc_id'])\n\nprint(\"Loading model predictions...\")\nmodels = {\n    'GDN-pure':   load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-GatedDeltaNet-pure.json')),\n    'GDN-h31':    load_jsonl_samples(os.path.join(DATA_DIR, '1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl')),\n    'HGRN2-pure': load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-HGRN2-pure.json')),\n    'HGRN2-h31':  load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-HGRN2-hybrid-3-1.json')),\n    'RetNet-pure': load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-RetNet-pure.json')),\n    'RetNet-h31':  load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-RetNet-hybrid-3-1.json')),\n}\n\nn_samples = len(models['GDN-pure'])\nprint(f\"Loaded {n_samples} samples per model\")\n\n# ── Feature extraction ───────────────────────────────────────────\n\nprint(\"Loading tokenizer...\")\ntokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH)\n\ntexts = [s['doc']['text'] for s in models['GDN-pure']]\ntargets = [s['target'].strip() for s in models['GDN-pure']]\n\nprint(\"Tokenizing...\")\ntarget_freq = Counter(targets)\n\ncontext_lengths = []\ncontext_unique_tokens_list = []\n\nfor i, text in enumerate(texts):\n    token_ids = tokenizer.encode(text, add_special_tokens=False)\n    target_text = targets[i]\n    target_ids = tokenizer.encode(' ' + target_text, add_special_tokens=False)\n    n_target = len(target_ids)\n    context_ids = token_ids[:-n_target] if n_target > 0 else token_ids\n    context_lengths.append(len(context_ids))\n    context_unique_tokens_list.append(len(set(context_ids)))\n\nfeatures = pd.DataFrame({\n    'doc_id': [s['doc_id'] for s in models['GDN-pure']],\n    'target_token': targets,\n    'context_length': context_lengths,\n    'target_token_frequency': [target_freq[t] for t in targets],\n    'context_unique_tokens': context_unique_tokens_list,\n})\n\nprint(f\"Feature stats:\\n{features[['context_length', 'target_token_frequency', 'context_unique_tokens']].describe()}\")\n\n# ── Helped/Hurt identification ───────────────────────────────────\n\nARCHS = ['GDN', 'HGRN2', 'RetNet']\n\nacc_arrays = {}\nfor name, samples in models.items():\n    acc_arrays[name] = np.array([s['acc'] for s in samples])\n\nhelped = {}  # hybrid=1, pure=0\nhurt = {}    # hybrid=0, pure=1\n\nfor arch in ARCHS:\n    pure_acc = acc_arrays[f'{arch}-pure']\n    hybrid_acc = acc_arrays[f'{arch}-h31']\n    helped[arch] = (hybrid_acc == 1) & (pure_acc == 0)\n    hurt[arch] = (hybrid_acc == 0) & (pure_acc == 1)\n    print(f\"{arch}: helped={helped[arch].sum()}, hurt={hurt[arch].sum()}, \"\n          f\"both_correct={(hybrid_acc & pure_acc).sum()}, both_wrong={((1-hybrid_acc) * (1-pure_acc)).astype(int).sum()}\")\n\n# ── Statistical tests ────────────────────────────────────────────\n\nFEATURE_COLS = ['context_length', 'target_token_frequency', 'context_unique_tokens']\n\nstat_rows = []\n\n# Per-architecture: helped vs hurt\nfor arch in ARCHS:\n    h_mask = helped[arch]\n    r_mask = hurt[arch]\n    if h_mask.sum() < 2 or r_mask.sum() < 2:\n        print(f\"WARNING: {arch} has too few helped/hurt samples for stats\")\n        continue\n    for feat in FEATURE_COLS:\n        vals_h = features.loc[h_mask, feat].values\n        vals_r = features.loc[r_mask, feat].values\n        u_stat, p_val = stats.mannwhitneyu(vals_h, vals_r, alternative='two-sided')\n        n1, n2 = len(vals_h), len(vals_r)\n        rank_biserial = 1 - (2 * u_stat) / (n1 * n2)\n        stat_rows.append({\n            'comparison': f'{arch}: helped vs hurt',\n            'feature': feat,\n            'helped_median': np.median(vals_h),\n            'hurt_median': np.median(vals_r),\n            'helped_mean': np.mean(vals_h),\n            'hurt_mean': np.mean(vals_r),\n            'helped_n': n1,\n            'hurt_n': n2,\n            'U_statistic': u_stat,\n            'p_value': p_val,\n            'rank_biserial_r': rank_biserial,\n        })\n\n# Cross-architecture: helped vs helped\nfor i, a1 in enumerate(ARCHS):\n    for a2 in ARCHS[i+1:]:\n        m1 = helped[a1]\n        m2 = helped[a2]\n        if m1.sum() < 2 or m2.sum() < 2:\n            continue\n        for feat in FEATURE_COLS:\n            v1 = features.loc[m1, feat].values\n            v2 = features.loc[m2, feat].values\n            u_stat, p_val = stats.mannwhitneyu(v1, v2, alternative='two-sided')\n            n1, n2 = len(v1), len(v2)\n            rank_biserial = 1 - (2 * u_stat) / (n1 * n2)\n            stat_rows.append({\n                'comparison': f'helped: {a1} vs {a2}',\n                'feature': feat,\n                'helped_median': np.median(v1),\n                'hurt_median': np.median(v2),\n                'helped_mean': np.mean(v1),\n                'hurt_mean': np.mean(v2),\n                'helped_n': n1,\n                'hurt_n': n2,\n                'U_statistic': u_stat,\n                'p_value': p_val,\n                'rank_biserial_r': rank_biserial,\n            })\n\nstats_df = pd.DataFrame(stat_rows)\nstats_path = os.path.join(OUT_DIR, 'sample_characterization_results.csv')\nstats_df.to_csv(stats_path, index=False)\nprint(f\"\\nStatistical results saved to {stats_path}\")\nprint(stats_df.to_string(index=False))\n\n# ── Visualization ────────────────────────────────────────────────\n\nfig = plt.figure(figsize=(18, 14))\ngs = gridspec.GridSpec(2, 3, hspace=0.35, wspace=0.3)\n\nfeat_labels = {\n    'context_length': 'Context Length\\n(tokens)',\n    'target_token_frequency': 'Target Token\\nFrequency',\n    'context_unique_tokens': 'Context Unique\\nTokens',\n}\n\narch_colors = {\n    'GDN': ('#2196F3', '#90CAF9'),\n    'HGRN2': ('#FF5722', '#FFAB91'),\n    'RetNet': ('#4CAF50', '#A5D6A7'),\n}\n\n# Upper row: per-architecture helped vs hurt\nfor col, arch in enumerate(ARCHS):\n    ax = fig.add_subplot(gs[0, col])\n    h_mask = helped[arch]\n    r_mask = hurt[arch]\n\n    data_helped = []\n    data_hurt = []\n    positions = []\n    for fi, feat in enumerate(FEATURE_COLS):\n        data_helped.append(features.loc[h_mask, feat].values)\n        data_hurt.append(features.loc[r_mask, feat].values)\n        positions.append(fi)\n\n    # Normalize each feature to [0,1] for comparable violin plots\n    all_vals = [np.concatenate([data_helped[i], data_hurt[i]]) for i in range(len(FEATURE_COLS))]\n    mins = [v.min() for v in all_vals]\n    maxs = [v.max() for v in all_vals]\n\n    bp_positions_h = [p - 0.18 for p in positions]\n    bp_positions_r = [p + 0.18 for p in positions]\n\n    norm_h = [(data_helped[i] - mins[i]) / (maxs[i] - mins[i] + 1e-8) for i in range(len(FEATURE_COLS))]\n    norm_r = [(data_hurt[i] - mins[i]) / (maxs[i] - mins[i] + 1e-8) for i in range(len(FEATURE_COLS))]\n\n    vp1 = ax.violinplot(norm_h, positions=bp_positions_h, widths=0.3, showextrema=False)\n    for body in vp1['bodies']:\n        body.set_facecolor(arch_colors[arch][0])\n        body.set_alpha(0.7)\n\n    vp2 = ax.violinplot(norm_r, positions=bp_positions_r, widths=0.3, showextrema=False)\n    for body in vp2['bodies']:\n        body.set_facecolor(arch_colors[arch][1])\n        body.set_alpha(0.7)\n\n    # Add median markers\n    for i in range(len(FEATURE_COLS)):\n        med_h = np.median(norm_h[i])\n        med_r = np.median(norm_r[i])\n        ax.plot(bp_positions_h[i], med_h, 'o', color='white', markeredgecolor=arch_colors[arch][0], markersize=6, zorder=5)\n        ax.plot(bp_positions_r[i], med_r, 'o', color='white', markeredgecolor=arch_colors[arch][1], markersize=6, zorder=5)\n\n    ax.set_xticks(positions)\n    ax.set_xticklabels([feat_labels[f] for f in FEATURE_COLS], fontsize=8)\n    ax.set_ylabel('Normalized value', fontsize=9)\n    ax.set_title(f'{arch} (h={helped[arch].sum()}, r={hurt[arch].sum()})', fontsize=11, fontweight='bold')\n\n    if col == 0:\n        from matplotlib.patches import Patch\n        ax.legend(handles=[\n            Patch(facecolor=arch_colors[arch][0], alpha=0.7, label='Helped'),\n            Patch(facecolor=arch_colors[arch][1], alpha=0.7, label='Hurt'),\n        ], fontsize=8, loc='upper right')\n\n    # Add p-value annotations\n    for i, feat in enumerate(FEATURE_COLS):\n        match = stats_df[(stats_df['comparison'] == f'{arch}: helped vs hurt') & (stats_df['feature'] == feat)]\n        if len(match) > 0:\n            p = match.iloc[0]['p_value']\n            sig = '***' if p < 0.001 else '**' if p < 0.01 else '*' if p < 0.05 else 'n.s.'\n            ax.text(positions[i], 1.05, sig, ha='center', fontsize=8, color='black')\n\n    ax.set_ylim(-0.1, 1.2)\n\n# Lower row: cross-architecture helped comparison\nfor col, feat in enumerate(FEATURE_COLS):\n    ax = fig.add_subplot(gs[1, col])\n\n    data = []\n    labels = []\n    colors = []\n    for arch in ARCHS:\n        h_mask = helped[arch]\n        if h_mask.sum() > 0:\n            data.append(features.loc[h_mask, feat].values)\n            labels.append(f'{arch}\\n(n={h_mask.sum()})')\n            colors.append(arch_colors[arch][0])\n\n    vp = ax.violinplot(data, positions=range(len(data)), widths=0.6, showextrema=False)\n    for i, body in enumerate(vp['bodies']):\n        body.set_facecolor(colors[i])\n        body.set_alpha(0.7)\n\n    # Median + IQR\n    for i, d in enumerate(data):\n        med = np.median(d)\n        q1, q3 = np.percentile(d, [25, 75])\n        ax.vlines(i, q1, q3, color='black', linewidth=2)\n        ax.scatter(i, med, color='white', edgecolor='black', s=40, zorder=5)\n\n    ax.set_xticks(range(len(labels)))\n    ax.set_xticklabels(labels, fontsize=9)\n    ax.set_ylabel(feat.replace('_', ' ').title(), fontsize=9)\n    ax.set_title(f'Helped samples: {feat_labels[feat].replace(chr(10), \" \")}', fontsize=10, fontweight='bold')\n\n    # Add cross-arch p-values\n    y_max = max(d.max() for d in data)\n    y_step = (y_max - min(d.min() for d in data)) * 0.08\n    y_pos = y_max + y_step\n    for i, a1 in enumerate(ARCHS):\n        for j, a2 in enumerate(ARCHS):\n            if j <= i:\n                continue\n            match = stats_df[(stats_df['comparison'] == f'helped: {a1} vs {a2}') & (stats_df['feature'] == feat)]\n            if len(match) > 0:\n                p = match.iloc[0]['p_value']\n                sig = '***' if p < 0.001 else '**' if p < 0.01 else '*' if p < 0.05 else 'n.s.'\n                if sig != 'n.s.':\n                    idx_a1 = ARCHS.index(a1)\n                    idx_a2 = ARCHS.index(a2)\n                    ax.plot([idx_a1, idx_a2], [y_pos, y_pos], 'k-', linewidth=0.8)\n                    ax.text((idx_a1 + idx_a2) / 2, y_pos, sig, ha='center', va='bottom', fontsize=7)\n                    y_pos += y_step * 1.5\n\nfig.suptitle('LAMBADA Sample Characterization: Helped vs Hurt by Attention Hybridization',\n             fontsize=14, fontweight='bold', y=0.98)\n\nfor fmt in ['pdf', 'png']:\n    path = os.path.join(OUT_DIR, f'sample_characterization.{fmt}')\n    fig.savefig(path, dpi=200, bbox_inches='tight')\n    print(f\"Figure saved: {path}\")\n\nplt.close()\nprint(\"\\nDone.\")\nPYEOF\necho \"Script written: $(wc -l /root/entrainment_gated_ft/analysis/sample_characterization.py)\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-19T13:18:01.917928+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written: 305 /root/entrainment_gated_ft/analysis/sample_characterization.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.92}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-19T13:18:01.918074+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-48145",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 python3 /root/entrainment_gated_ft/analysis/sample_characterization.py 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-48145",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 python3 /root/entrainment_gated_ft/analysis/sample_characterization.py 2>&1",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-19T13:18:01.918232+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[transformers] You are using a model of type `gated_deltanet` to instantiate a model of type ``. This may be expected if you are loading a checkpoint that shares a subset of the architecture (e.g., loading a `sam2_video` checkpoint into `Sam2Model`), but is otherwise not supported and can yield errors. Please verify that the checkpoint is compatible with the model you are instantiating.\\nLoading model predictions...\\nLoaded 5153 samples per model\\nLoading tokenizer...\\nTokenizing...\\nFeature stats:\\n       context_length  target_token_frequency  context_unique_tokens\\ncount     5153.000000             5153.000000            5153.000000\\nmean        83.772366                2.673976              61.937512\\nstd         13.117970                2.377605               9.601552\\nmin         59.000000                1.000000              26.000000\\n25%         75.000000                1.000000              55.000000\\n50%         81.000000                2.000000              61.000000\\n75%         90.000000                3.000000              67.000000\\nmax        228.000000               16.000000             124.000000\\nGDN: helped=462, hurt=615, both_correct=2183, both_wrong=1893\\nHGRN2: helped=548, hurt=395, both_correct=2100, both_wrong=2110\\nRetNet: helped=426, hurt=495, both_correct=2167, both_wrong=2065\\n\\nStatistical results saved to /root/entrainment_gated_ft/analysis/sample_characterization_results.csv\\n             comparison                feature  helped_median  hurt_median  helped_mean  hurt_mean  helped_n  hurt_n  U_statistic  p_value  rank_biserial_r\\n    GDN: helped vs hurt         context_length           81.0         81.0    83.796537  83.256911       462     615     141635.5 0.932297         0.003023\\n    GDN: helped vs hurt target_token_frequency            2.0          2.0     2.790043   2.702439       462     615     145298.0 0.502770        -0.022757\\n    GDN: helped v
…[truncated 2787 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-19T13:18:01.918410+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Phase 0: Data validation', 'status': 'completed', 'activeForm': 'Validating data files'}, {'content': 'Phase 1-2: Write sample_characterization.py script', 'status': 'completed', 'activeForm': 'Writing sample characterization script'}, {'content': 'Phase 3: Upload and run script on server', 'status': 'completed', 'activeForm': 'Running script on server'}, {'content': 'Phase 4: Verify outputs and register artifacts', 'status': 'in_progress', 'activeForm': 'Verifying outputs and registering artifacts'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Phase 0: Data validation', 'status': 'completed', 'activeForm': 'Validating data files'}, {'content': 'Phase 1-2: Write sample_characterization.py script', 'status': 'completed', 'activeForm': 'Writing sample characterization script'}, {'content': 'Phase 3: Upload and run script on server', 'status': 'completed', 'activeForm': 'Running script on server'}, {'content': 'Phase 4: Verify outputs and register artifacts', 'status': 'in_progress', 'activeForm': 'Verifying outputs and registering artifacts'}]"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-19T13:18:01.918555+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-19T13:18:01.918693+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "ls -lh /root/entrainment_gated_ft/analysis/sample_characterization*",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "ls -lh /root/entrainment_gated_ft/analysis/sample_characterization*",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-19T13:18:01.918822+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root  84K May 19 21:17 /root/entrainment_gated_ft/analysis/sample_characterization.pdf\\n-rw-r--r-- 1 root root 349K May 19 21:17 /root/entrainment_gated_ft/analysis/sample_characterization.png\\n-rw-r--r-- 1 root root  12K May 19 21:16 /root/entrainment_gated_ft/analysis/sample_characterization.py\\n-rw-r--r-- 1 root root 2.7K May 19 21:17 /root/entrainment_gated_ft/analysis/sample_characterization_results.csv\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.76}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-19T13:18:01.918960+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "sample_characterization_results",
  "type": "data",
  "description": "LAMBADA sample characterization: Mann-Whitney U tests for helped vs hurt samples across GDN/HGRN2/RetNet h3-1 architectures",
  "project": "entrainment_gated_ft",
  "exp_id": "exp-003",
  "source_path": "/root/entrainment_gated_ft/analysis/sample_characterization_results.csv",
  "tags": "['sample-characterization', 'lambada', 'statistics']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "sample_characterization_results",
    "type": "data",
    "description": "LAMBADA sample characterization: Mann-Whitney U tests for helped vs hurt samples across GDN/HGRN2/RetNet h3-1 architectures",
    "project": "entrainment_gated_ft",
    "exp_id": "exp-003",
    "source_path": "/root/entrainment_gated_ft/analysis/sample_characterization_results.csv",
    "tags": "['sample-characterization', 'lambada', 'statistics']"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-19T13:18:01.919086+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"source_path not found: /root/entrainment_gated_ft/analysis/sample_characterization_results.csv\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-19T13:18:01.919202+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "sample_characterization_figure",
  "type": "chart",
  "description": "6-panel violin plot: upper=per-arch helped vs hurt feature distributions, lower=cross-arch helped comparison",
  "project": "entrainment_gated_ft",
  "exp_id": "exp-003",
  "source_path": "/root/entrainment_gated_ft/analysis/sample_characterization.png",
  "tags": "['sample-characterization', 'lambada', 'visualization']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "sample_characterization_figure",
    "type": "chart",
    "description": "6-panel violin plot: upper=per-arch helped vs hurt feature distributions, lower=cross-arch helped comparison",
    "project": "entrainment_gated_ft",
    "exp_id": "exp-003",
    "source_path": "/root/entrainment_gated_ft/analysis/sample_characterization.png",
    "tags": "['sample-characterization', 'lambada', 'visualization']"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-19T13:18:01.919323+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"source_path not found: /root/entrainment_gated_ft/analysis/sample_characterization.png\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-19T13:18:01.919508+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "cat /root/entrainment_gated_ft/analysis/sample_characterization_results.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "cat /root/entrainment_gated_ft/analysis/sample_characterization_results.csv",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-19T13:18:01.919672+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"comparison,feature,helped_median,hurt_median,helped_mean,hurt_mean,helped_n,hurt_n,U_statistic,p_value,rank_biserial_r\\nGDN: helped vs hurt,context_length,81.0,81.0,83.7965367965368,83.25691056910568,462,615,141635.5,0.9322969149305119,0.0030232639988737597\\nGDN: helped vs hurt,target_token_frequency,2.0,2.0,2.79004329004329,2.702439024390244,462,615,145298.0,0.5027700073387493,-0.02275718861084708\\nGDN: helped vs hurt,context_unique_tokens,61.0,61.0,62.17965367965368,61.68130081300813,462,615,144090.0,0.6884121512855317,-0.014254038644282652\\nHGRN2: helped vs hurt,context_length,82.0,81.0,83.99270072992701,83.26835443037974,548,395,113423.0,0.20806873405293358,-0.04798115125196345\\nHGRN2: helped vs hurt,target_token_frequency,2.0,2.0,2.923357664233577,2.8177215189873417,548,395,111962.5,0.3460715823877467,-0.03448674119929773\\nHGRN2: helped vs hurt,context_unique_tokens,62.0,60.0,62.39598540145985,61.93164556962025,548,395,113510.0,0.2004578470626196,-0.04878499491822974\\nRetNet: helped vs hurt,context_length,82.0,81.0,85.01643192488262,82.61818181818182,426,495,115506.5,0.012309186168587033,-0.0955233081993645\\nRetNet: helped vs hurt,target_token_frequency,2.0,2.0,2.9225352112676055,3.0202020202020203,426,495,102511.5,0.45274753212040164,0.02772798406601229\\nRetNet: helped vs hurt,context_unique_tokens,61.5,61.0,62.863849765258216,61.074747474747475,426,495,115907.5,0.009229335849670483,-0.09932659932659926\\nhelped: GDN vs HGRN2,context_length,81.0,82.0,83.7965367965368,83.99270072992701,462,548,122083.0,0.3291788360797804,0.03558789142730745\\nhelped: GDN vs HGRN2,target_token_frequency,2.0,2.0,2.79004329004329,2.923357664233577,462,548,123104.0,0.43219407331505766,0.02752235598950925\\nhelped: GDN vs HGRN2,context_unique_tokens,61.0,62.0,62.17965367965368,62.39598540145985,462,548,122218.5,0.3438110659606932,0.034517489809460566\\nhelped: GDN vs RetNet,context_length,81.0,82.0,83.7965367965368,85.
…[truncated 919 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-19T13:18:01.919824+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "sample_characterization_results",
  "type": "data",
  "description": "LAMBADA sample characterization: Mann-Whitney U tests for helped vs hurt samples across GDN/HGRN2/RetNet h3-1 architectures",
  "project": "entrainment_gated_ft",
  "exp_id": "exp-003",
  "content": "comparison,feature,helped_median,hurt_median,helped_mean,hurt_mean,helped_n,hurt_n,U_statistic,p_value,rank_biserial_r\nGDN: helped vs hurt,context_length,81.0,81.0,83.80,83.26,462,615,141635.5,0.932,0.003\nGDN: helped vs hurt,target_token_frequency,2.0,2.0,2.79,2.70,462,615,145298.0,0.503,-0.023\nGDN: helped vs hurt,context_unique_tokens,61.0,61.0,62.18,61.68,462,615,144090.0,0.688,-0.014\nHGRN2: helped vs hurt,context_length,82.0,81.0,83.99,83.27,548,395,113423.0,0.208,-0.048\nHGRN2: helped vs hurt,target_token_frequency,2.0,2.0,2.92,2.82,548,395,111962.5,0.346,-0.034\nHGRN2: helped vs hurt,context_unique_tokens,62.0,60.0,62.40,61.93,548,395,113510.0,0.200,-0.049\nRetNet: helped vs hurt,context_length,82.0,81.0,85.02,82.62,426,495,115506.5,0.012,-0.096\nRetNet: helped vs hurt,target_token_frequency,2.0,2.0,2.92,3.02,426,495,102511.5,0.453,0.028\nRetNet: helped vs hurt,context_unique_tokens,61.5,61.0,62.86,61.07,426,495,115907.5,0.009,-0.099\nhelped: GDN vs HGRN2,context_length,81.0,82.0,83.80,83.99,462,548,122083.0,0.329,0.036\nhelped: GDN vs HGRN2,target_token_frequency,2.0,2.0,2.79,2.92,462,548,123104.0,0.432,0.028\nhelped: GDN vs HGRN2,context_unique_tokens,61.0,62.0,62.18,62.40,462,548,122218.5,0.344,0.035\nhelped: GDN vs RetNet,context_length,81.0,82.0,83.80,85.02,462,426,91805.5,0.084,0.067\nhelped: GDN vs RetNet,target_token_frequency,2.0,2.0,2.79,2.92,462,426,95517.0,0.432,0.029\nhelped: GDN vs RetNet,context_unique_tokens,61.0,61.5,62.18,62.86,462,426,93547.5,0.203,0.049\nhelped: HGRN2 vs RetNet,context_length,82.0,82.0,83.99,85.02,548,426,112892.0,0.379,0.033\nhelped: HGRN2 vs RetNet,target_token_frequency,2.0,2.0,2.92,2.92,548,426,116557.5,0.968,0.001\nhelped: HGRN2 vs RetNet,context_unique_tokens,62.0,61.5,62.40,62.86,548,426,114863.5,0.669,0.016",
  "content_filename": "sample_characterization_results.csv",
  "tags": "['sample-characterization', 'lambada', 'statistics']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "sample_characterization_results",
    "type": "data",
    "description": "LAMBADA sample characterization: Mann-Whitney U tests for helped vs hurt samples across GDN/HGRN2/RetNet h3-1 architectures",
    "project": "entrainment_gated_ft",
    "exp_id": "exp-003",
    "content": "comparison,feature,helped_median,hurt_median,helped_mean,hurt_mean,helped_n,hurt_n,U_statistic,p_value,rank_biserial_r\nGDN: helped vs hurt,context_length,81.0,81.0,83.80,83.26,462,615,141635.5,0.932,0.003\nGDN: helped vs hurt,target_token_frequency,2.0,2.0,2.79,2.70,462,615,145298.0,0.503,-0.023\nGDN: helped vs hurt,context_unique_tokens,61.0,61.0,62.18,61.68,462,615,144090.0,0.688,-0.014\nHGRN2: helped vs hurt,context_length,82.0,81.0,83.99,83.27,548,395,113423.0,0.208,-0.048\nHGRN2: helped vs hurt,target_token_frequency,2.0,2.0,2.92,2.82,548,395,111962.5,0.346,-0.034\nHGRN2: helped vs hurt,context_unique_tokens,62.0,60.0,62.40,61.93,548,395,113510.0,0.200,-0.049\nRetNet: helped vs hurt,context_length,82.0,81.0,85.02,82.62,426,495,115506.5,0.012,-0.096\nRetNet: helped vs hurt,target_token_frequency,2.0,2.0,2.92,3.02,426,495,102511.5,0.453,0.028\nRetNet: helped vs hurt,context_unique_tokens,61.5,61.0,62.86,61.07,426,495,115907.5,0.009,-0.099\nhelped: GDN vs HGRN2,context_length,81.0,82.0,83.80,83.99,462,548,122083.0,0.329,0.036\nhelped: GDN vs HGRN2,target_token_frequency,2.0,2.0,2.79,2.92,462,548,123104.0,0.432,0.028\nhelped: GDN vs HGRN2,context_unique_tokens,61.0,62.0,62.18,62.40,462,548,122218.5,0.344,0.035\nhelped: GDN vs RetNet,context_length,81.0,82.0,83.80,85.02,462,426,91805.5,0.084,0.067\nhelped: GDN vs RetNet,target_token_frequency,2.0,2.0,2.79,2.92,462,426,95517.0,0.432,0.029\nhelped: GDN vs RetNet,context_unique_tokens,61.0,61.5,62.18,62.86,462,426,93547.5,0.203,0.049\nhelped: HGRN2 vs RetNet,context_length,82.0,82.0,83.99,85.02,548,426,112892.0,0.379,0.033\nhelped: HGRN2 vs RetNet,target_token_frequency,2.0,2.0,2.92,2.92,548,426,116557.5,0.968,0.001\nhelped: HGRN2 vs RetNet,context_unique_tokens,62.0,61.5,62.40,62.86,548,426,114863.5,0.669,0.016",
    "content_filename": "sample_characterization_results.csv",
    "tags": "['sample-characterization', 'lambada', 'statistics']"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-19T13:18:01.919981+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_35e8b7\", \"name\": \"sample_characterization_results\", \"type\": \"data\", \"description\": \"LAMBADA sample characterization: Mann-Whitney U tests for helped vs hurt samples across GDN/HGRN2/RetNet h3-1 architectures\", \"path\": \"projects/entrainment_gated_ft/artifacts/exp-003/data/sample_characterization_results.csv\", \"url\": null, \"project\": \"entrainment_gated_ft\", \"exp_id\": \"exp-003\", \"skill\": \"\", \"created_at\": \"2026-05-19T13:17:44.204906+00:00\", \"tags\": [\"sample-characterization\", \"lambada\", \"statistics\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-19T13:18:01.920109+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "sample_characterization_figure",
  "type": "chart",
  "description": "6-panel violin plot: upper=per-arch helped vs hurt feature distributions, lower=cross-arch helped comparison. Remote path: /root/entrainment_gated_ft/analysis/sample_characterization.png",
  "project": "entrainment_gated_ft",
  "exp_id": "exp-003",
  "content": "Remote file: /root/entrainment_gated_ft/analysis/sample_characterization.png (349K) and sample_characterization.pdf (84K) on westb-48145",
  "content_filename": "sample_characterization_figure_pointer.txt",
  "tags": "['sample-characterization', 'lambada', 'visualization']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "sample_characterization_figure",
    "type": "chart",
    "description": "6-panel violin plot: upper=per-arch helped vs hurt feature distributions, lower=cross-arch helped comparison. Remote path: /root/entrainment_gated_ft/analysis/sample_characterization.png",
    "project": "entrainment_gated_ft",
    "exp_id": "exp-003",
    "content": "Remote file: /root/entrainment_gated_ft/analysis/sample_characterization.png (349K) and sample_characterization.pdf (84K) on westb-48145",
    "content_filename": "sample_characterization_figure_pointer.txt",
    "tags": "['sample-characterization', 'lambada', 'visualization']"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-19T13:18:01.920248+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_69044b\", \"name\": \"sample_characterization_figure\", \"type\": \"chart\", \"description\": \"6-panel violin plot: upper=per-arch helped vs hurt feature distributions, lower=cross-arch helped comparison. Remote path: /root/entrainment_gated_ft/analysis/sample_characterization.png\", \"path\": \"projects/entrainment_gated_ft/artifacts/exp-003/chart/sample_characterization_figure_pointer.txt\", \"url\": null, \"project\": \"entrainment_gated_ft\", \"exp_id\": \"exp-003\", \"skill\": \"\", \"created_at\": \"2026-05-19T13:17:46.779137+00:00\", \"tags\": [\"sample-characterization\", \"lambada\", \"visualization\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-19T13:18:01.920379+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Phase 0: Data validation', 'status': 'completed', 'activeForm': 'Validating data files'}, {'content': 'Phase 1-2: Write sample_characterization.py script', 'status': 'completed', 'activeForm': 'Writing sample characterization script'}, {'content': 'Phase 3: Upload and run script on server', 'status': 'completed', 'activeForm': 'Running script on server'}, {'content': 'Phase 4: Verify outputs and register artifacts', 'status': 'completed', 'activeForm': 'Verifying outputs and registering artifacts'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Phase 0: Data validation', 'status': 'completed', 'activeForm': 'Validating data files'}, {'content': 'Phase 1-2: Write sample_characterization.py script', 'status': 'completed', 'activeForm': 'Writing sample characterization script'}, {'content': 'Phase 3: Upload and run script on server', 'status': 'completed', 'activeForm': 'Running script on server'}, {'content': 'Phase 4: Verify outputs and register artifacts', 'status': 'completed', 'activeForm': 'Verifying outputs and registering artifacts'}]"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-19T13:18:01.920512+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 71 · 2026-05-19T13:18:01.920681+00:00_

完成。结果摘要：

**Helped/Hurt 统计（h3-1 hybrid vs pure）：**

| 架构 | Helped | Hurt | Both Correct | Both Wrong |
|------|--------|------|-------------|------------|
| GDN | 462 | 615 | 2183 | 1893 |
| HGRN2 | 548 | 395 | 2100 | 2110 |
| RetNet | 426 | 495 | 2167 | 2065 |

HGRN2 是唯一 helped > hurt 的架构（净正效果）；GDN 和 RetNet 的 attention 层反而 hurt 更多。

**统计检验关键发现：**
- **GDN、HGRN2**：helped vs hurt 在所有特征上均无显著差异（p > 0.2）
- **RetNet**：helped 样本的 context_length 显著更长（p=0.012, r=-0.096）且 context_unique_tokens 显著更多（p=0.009, r=-0.099）——attention 更倾向帮助长上下文、高词汇多样性的样本
- **跨架构比较**：三个架构的 helped 样本特征分布之间无显著差异

**输出文件（westb-48145）：**
- `analysis/sample_characterization.py`（脚本）
- `analysis/sample_characterization_results.csv`（统计表）
- `analysis/sample_characterization.pdf` + `.png`（6-panel violin plot）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_exp_003_sample_characterization_20260519T131141"
}
```

</details>

---
