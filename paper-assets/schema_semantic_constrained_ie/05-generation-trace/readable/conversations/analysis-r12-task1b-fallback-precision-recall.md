# analysis r12 task1b fallback precision recall

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 63
- **Recorded user turns:** 0
- **Tool calls:** 31
- **Original source:** `logs/chats/worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440.jsonl`
- **Structured JSON:** [`867eeed45ab3afa2cea3.json`](../../sessions/86/867eeed45ab3afa2cea3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

63 recorded events

### Tool call

_source line 1 · 2026-05-20T18:10:42.471492+00:00_

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
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
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

_source line 2 · 2026-05-20T18:10:42.471989+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T18:10:42.472201+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "head -100 /root/schema_semantic_constrained_ie/outputs/fallback_estimation_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "head -100 /root/schema_semantic_constrained_ie/outputs/fallback_estimation_results.json"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T18:10:42.472345+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "head -5 /root/schema_semantic_constrained_ie/outputs/phase2_scierc_full_s1_v2.jsonl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "head -5 /root/schema_semantic_constrained_ie/outputs/phase2_scierc_full_s1_v2.jsonl"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T18:10:42.472473+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "head -5 /root/schema_semantic_constrained_ie/outputs/docred_full_s1.jsonl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "head -5 /root/schema_semantic_constrained_ie/outputs/docred_full_s1.jsonl"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T18:10:42.472694+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"qwen_docred_full_s1\\\": {\\n    \\\"total_docs\\\": 998,\\n    \\\"total_triples\\\": 17341,\\n    \\\"matched_triples\\\": 17336,\\n    \\\"fallback_triples\\\": 1770,\\n    \\\"fallback_rate\\\": 0.1021,\\n    \\\"avg_fallback_per_doc\\\": 1.77,\\n    \\\"unmatched_relations\\\": {\\n      \\\"membericipant of\\\": 5\\n    },\\n    \\\"per_relation_fallback\\\": {\\n      \\\"P1001 (applies to jurisdiction)\\\": {\\n        \\\"total\\\": 966,\\n        \\\"fallback\\\": 194,\\n        \\\"rate\\\": 0.2008\\n      },\\n      \\\"P102 (member of political party)\\\": {\\n        \\\"total\\\": 37,\\n        \\\"fallback\\\": 0,\\n        \\\"rate\\\": 0.0\\n      },\\n      \\\"P1056 (product or material produced)\\\": {\\n        \\\"total\\\": 156,\\n        \\\"fallback\\\": 48,\\n        \\\"rate\\\": 0.3077\\n      },\\n      \\\"P108 (employer)\\\": {\\n        \\\"total\\\": 173,\\n        \\\"fallback\\\": 30,\\n        \\\"rate\\\": 0.1734\\n      },\\n      \\\"P112 (founded by)\\\": {\\n        \\\"total\\\": 135,\\n        \\\"fallback\\\": 29,\\n        \\\"rate\\\": 0.2148\\n      },\\n      \\\"P118 (league)\\\": {\\n        \\\"total\\\": 1,\\n        \\\"fallback\\\": 0,\\n        \\\"rate\\\": 0.0\\n      },\\n      \\\"P1198 (unemployment rate)\\\": {\\n        \\\"total\\\": 6,\\n        \\\"fallback\\\": 5,\\n        \\\"rate\\\": 0.8333\\n      },\\n      \\\"P123 (publisher)\\\": {\\n        \\\"total\\\": 54,\\n        \\\"fallback\\\": 0,\\n        \\\"rate\\\": 0.0\\n      },\\n      \\\"P127 (owned by)\\\": {\\n        \\\"total\\\": 67,\\n        \\\"fallback\\\": 0,\\n        \\\"rate\\\": 0.0\\n      },\\n      \\\"P131 (located in the administrative territorial entity)\\\": {\\n        \\\"total\\\": 1207,\\n        \\\"fallback\\\": 15,\\n        \\\"rate\\\": 0.0124\\n      },\\n      \\\"P1336 (territory claimed by)\\\": {\\n        \\\"total\\\": 20,\\n        \\\"
…[truncated 1095 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-20T18:10:42.473193+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"doc_id\\\": \\\"X96-1059_sent0\\\", \\\"input_text\\\": \\\"Recognition of proper nouns in Japanese text has been studied as a part of the more general problem of morphological analysis in Japanese text processing -LRB- -LSB- 1 -RSB- -LSB- 2 -RSB- -RRB- .\\\", \\\"gold_entities\\\": [{\\\"text\\\": \\\"Recognition of proper nouns\\\", \\\"type\\\": \\\"Task\\\"}, {\\\"text\\\": \\\"proper nouns\\\", \\\"type\\\": \\\"OtherScientificTerm\\\"}, {\\\"text\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"Material\\\"}, {\\\"text\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"Task\\\"}, {\\\"text\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"Task\\\"}], \\\"gold_relations\\\": [{\\\"head\\\": \\\"Recognition of proper nouns\\\", \\\"tail\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"Part-of\\\", \\\"head_type\\\": \\\"Task\\\", \\\"tail_type\\\": \\\"Task\\\"}, {\\\"head\\\": \\\"proper nouns\\\", \\\"tail\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"Part-of\\\", \\\"head_type\\\": \\\"OtherScientificTerm\\\", \\\"tail_type\\\": \\\"Material\\\"}, {\\\"head\\\": \\\"morphological analysis\\\", \\\"tail\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"Used-for\\\", \\\"head_type\\\": \\\"Task\\\", \\\"tail_type\\\": \\\"Task\\\"}], \\\"raw_output\\\": \\\"{\\\\n  \\\\\\\"entities\\\\\\\": [\\\\n    {\\\\n      \\\\\\\"text\\\\\\\": \\\\\\\"Recognition of proper nouns in Japanese text\\\\\\\",\\\\n      \\\\\\\"type\\\\\\\": \\\\\\\"Task\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"text\\\\\\\": \\\\\\\"morphological analysis in Japanese text processing\\\\\\\",\\\\n      \\\\\\\"type\\\\\\\": \\\\\\\"Task\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"text\\\\\\\": \\\\\\\"1\\\\\\\",\\\\n      \\\\\\\"type\\\\\\\": \\\\\\\"OtherScientificTerm\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"text\\\\\\\": \\\\\\\"2\\\\\\\",\\\\n      \\\\\\\"type\\\\\\\": \\\\\\\"OtherScientificT
…[truncated 10073 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-20T18:10:42.473375+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "find /root/schema_semantic_constrained_ie -name \"*estimate*fallback*\" -o -name \"*fallback*rate*\" -o -name \"*eval*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "find /root/schema_semantic_constrained_ie -name \"*estimate*fallback*\" -o -name \"*fallback*rate*\" -o -name \"*eval*\""
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-20T18:10:42.473841+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"doc_id\\\": \\\"Skai TV\\\", \\\"input_text\\\": \\\"Skai TV is a Greek free - to - air television network based in Piraeus . It is part of the Skai Group , one of the largest media groups in the country . It was relaunched in its present form on 1st of April 2006 in the Athens metropolitan area , and gradually spread its coverage nationwide . Besides digital terrestrial transmission , it is available on the subscription - based encrypted services of Nova and Cosmote TV . Skai TV is also a member of Digea , a consortium of private television networks introducing digital terrestrial transmission in Greece . At launch , Skai TV opted for dubbing all foreign language content into Greek , instead of using subtitles . This is very uncommon in Greece for anything except documentaries ( using voiceover dubbing ) and children 's programmes ( using lip - synced dubbing ) , so after intense criticism the station switched to using subtitles for almost all foreign shows .\\\", \\\"gold_entities\\\": [{\\\"text\\\": \\\"Skai TV\\\", \\\"type\\\": \\\"ORG\\\"}, {\\\"text\\\": \\\"Greek\\\", \\\"type\\\": \\\"LOC\\\"}, {\\\"text\\\": \\\"Piraeus\\\", \\\"type\\\": \\\"LOC\\\"}, {\\\"text\\\": \\\"Skai Group\\\", \\\"type\\\": \\\"ORG\\\"}, {\\\"text\\\": \\\"1st of April 2006\\\", \\\"type\\\": \\\"TIME\\\"}, {\\\"text\\\": \\\"Athens\\\", \\\"type\\\": \\\"LOC\\\"}, {\\\"text\\\": \\\"Nova\\\", \\\"type\\\": \\\"ORG\\\"}, {\\\"text\\\": \\\"Cosmote TV\\\", \\\"type\\\": \\\"ORG\\\"}, {\\\"text\\\": \\\"Digea\\\", \\\"type\\\": \\\"ORG\\\"}, {\\\"text\\\": \\\"Greece\\\", \\\"type\\\": \\\"LOC\\\"}, {\\\"text\\\": \\\"Greek\\\", \\\"type\\\": \\\"MISC\\\"}], \\\"gold_relations\\\": [{\\\"head\\\": \\\"Piraeus\\\", \\\"tail\\\": \\\"Greece\\\", \\\"type\\\": \\\"P17\\\", \\\"head_type\\\": \\\"LOC\\\", \\\"tail_type\\\": \\\"LOC\\\"}, {\\\"head\\\": \\\"Skai Group\\\", \\\"tail\\\": \\\"Greece\\\", \\\"type\\\": \\\"P17\\
…[truncated 10773 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T18:10:42.474060+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/schema_semantic_constrained_ie/outputs/tcr/w5_lora_scierc_full_s1_eval_tcr.jsonl\\n/root/schema_semantic_constrained_ie/outputs/tcr/w5_lora_scierc_full_s1_eval_tcr_report.json\\n/root/schema_semantic_constrained_ie/outputs/w5_lora_scierc_unconstrained_eval.log\\n/root/schema_semantic_constrained_ie/outputs/w5_lora_scierc_unconstrained_eval.jsonl\\n/root/schema_semantic_constrained_ie/outputs/w5_lora_scierc_unconstrained_eval_fallback_stats.json\\n/root/schema_semantic_constrained_ie/outputs/w5_lora_scierc_full_s1_eval.jsonl\\n/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_unconstrained_eval.jsonl\\n/root/schema_semantic_constrained_ie/outputs/w5_qwen_docred_lora_unconstrained_eval.jsonl\\n/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_constrained_eval.jsonl\\n/root/schema_semantic_constrained_ie/outputs/w5_qwen_docred_lora_constrained_eval.jsonl\\n/root/schema_semantic_constrained_ie/outputs/eval_unconstrained.json\\n/root/schema_semantic_constrained_ie/outputs/eval_constrained.json\\n/root/schema_semantic_constrained_ie/outputs/eval_report_llama_unconstrained.json\\n/root/schema_semantic_constrained_ie/outputs/eval_report_qwen_unconstrained.json\\n/root/schema_semantic_constrained_ie/outputs/eval_report_qwen_constrained.json\\n/root/schema_semantic_constrained_ie/outputs/eval_report_llama_constrained.json\\n/root/schema_semantic_constrained_ie/outputs/w5_qwen_docred_lora_constrained_eval_cf_corrected.jsonl\\n/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_constrained_eval_cf_corrected.jsonl\\n/root/schema_semantic_constrained_ie/outputs/eval_report_qwen_retry_16k.json\\n/root/schema_semantic_constrained_ie/outputs/eval_report_llama_grammar_only.json\\n/root/schema_semantic_constrained_ie/outputs/eval_report_llama_full_s1.json\\n/root/schema_semantic_constrained_ie/outputs/eval_report_llama_full_s1_r2.json\\n/root/schema_semantic_constrained_ie/outpu
…[truncated 1086 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T18:10:42.474263+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "python3 -c \"import json; d=json.load(open('/root/schema_semantic_constrained_ie/outputs/fallback_estimation_results.json')); print(list(d.keys())); [print(k, list(v.keys()) if isinstance(v,dict) else type(v)) for k,v in d.items()]\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "python3 -c \"import json; d=json.load(open('/root/schema_semantic_constrained_ie/outputs/fallback_estimation_results.json')); print(list(d.keys())); [print(k, list(v.keys()) if isinstance(v,dict) else type(v)) for k,v in d.items()]\""
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T18:10:42.474407+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T18:10:42.474532+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "head -100 /root/schema_semantic_constrained_ie/estimate_fallback_rate.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "head -100 /root/schema_semantic_constrained_ie/estimate_fallback_rate.py"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T18:10:42.474655+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "head -80 /root/schema_semantic_constrained_ie/scripts/eval_d064.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "head -80 /root/schema_semantic_constrained_ie/scripts/eval_d064.py"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-20T18:10:42.474960+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Post-hoc estimation of semantic fallback frequency for Qwen outputs.\\\"\\\"\\\"\\nimport json\\nfrom collections import defaultdict\\nfrom pathlib import Path\\n\\n\\n# === DocRED entity type aliases (from violation_checker_docred.py) ===\\nDOCRED_TYPE_ALIASES = {\\n    'PERSON': 'PER', 'PEOPLE': 'PER',\\n    'ORGANIZATION': 'ORG', 'ORGANISATION': 'ORG',\\n    'LOCATION': 'LOC', 'NUMBER': 'NUM', 'NUMERICAL': 'NUM',\\n    'MISCELLANEOUS': 'MISC',\\n}\\n\\n# === SciERC entity type aliases (from violation_checker.py) ===\\nSCIERC_TYPE_MAP = {\\n    \\\"otherscientificterm\\\": \\\"OtherScientificTerm\\\",\\n    \\\"other-scientificterm\\\": \\\"OtherScientificTerm\\\",\\n    \\\"other_scientific_term\\\": \\\"OtherScientificTerm\\\",\\n    \\\"scientificterm\\\": \\\"OtherScientificTerm\\\",\\n    \\\"other\\\": \\\"OtherScientificTerm\\\",\\n}\\n\\n\\ndef normalize_docred_type(raw):\\n    t = raw.strip().upper()\\n    return DOCRED_TYPE_ALIASES.get(t, t)\\n\\n\\ndef normalize_scierc_type(raw, valid_types):\\n    t_lower = raw.strip().lower().replace(\\\" \\\", \\\"\\\").replace(\\\"_\\\", \\\"\\\").replace(\\\"-\\\", \\\"\\\")\\n    for vt in valid_types:\\n        if t_lower == vt.lower().replace(\\\" \\\", \\\"\\\").replace(\\\"_\\\", \\\"\\\").replace(\\\"-\\\", \\\"\\\"):\\n            return vt\\n    return SCIERC_TYPE_MAP.get(t_lower, None)\\n\\n\\ndef build_docred_name_to_id(rel_types):\\n    m = {}\\n    for rid, rname in rel_types.items():\\n        m[rname.lower().strip()] = rid\\n        m[rid.lower()] = rid\\n    return m\\n\\n\\ndef estimate_docred(output_path, constraints_path):\\n    with open(constraints_path) as f:\\n        C = json.load(f)\\n\\n    rel_types = C[\\\"relation_types\\\"]\\n    rel_constraints = C[\\\"relation_constraints\\\"]\\n    name_to_id = build_docred_name_to_id(rel_types)\\n\\n    # Build valid_pairs sets keyed by PID\\n    valid_pairs = {}\\n    for pid, info
…[truncated 2123 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T18:10:42.475187+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Unified evaluation for d064 beam search experiments (multi-dataset).\\nUsage: python scripts/eval_d064.py --input_path &lt;output.jsonl> --dataset scierc [--label &lt;name>]\\nComputes: ET%, RV%, DR%, CF%, Entity F1, Relation F1, Parse Fail%\\n\\\"\\\"\\\"\\nimport json\\nimport argparse\\nimport sys\\nfrom collections import defaultdict\\nfrom pathlib import Path\\n\\nDATASET_ONTOLOGY = {\\n    \\\"docred\\\": \\\"/root/schema_semantic_constrained_ie/data/docred/ontology_constraints_docred.json\\\",\\n    \\\"scierc\\\": \\\"/root/schema_semantic_constrained_ie/ontology_constraints.json\\\",\\n    \\\"ace05\\\": \\\"/root/schema_semantic_constrained_ie/data/ace05/ontology_constraints_ace05.json\\\",\\n    \\\"wikievents\\\": \\\"/root/schema_semantic_constrained_ie/data/wikievents/ontology_constraints_wikievents.json\\\",\\n}\\n\\nENTITY_TYPE_ALIASES = {\\n    'PERSON': 'PER', 'PEOPLE': 'PER',\\n    'ORGANIZATION': 'ORG', 'ORGANISATION': 'ORG',\\n    'LOCATION': 'LOC', 'NUMBER': 'NUM', 'NUMERICAL': 'NUM',\\n    'MISCELLANEOUS': 'MISC',\\n}\\n\\ndef normalize_etype(raw):\\n    t = raw.strip().upper()\\n    return ENTITY_TYPE_ALIASES.get(t, t)\\n\\ndef main():\\n    parser = argparse.ArgumentParser()\\n    parser.add_argument(\\\"--input_path\\\", required=True)\\n    parser.add_argument(\\\"--dataset\\\", default=\\\"docred\\\", choices=DATASET_ONTOLOGY.keys())\\n    parser.add_argument(\\\"--label\\\", default=\\\"\\\")\\n    parser.add_argument(\\\"--output_json\\\", default=\\\"\\\")\\n    args = parser.parse_args()\\n\\n    ontology_file = DATASET_ONTOLOGY[args.dataset]\\n    with open(ontology_file) as f:\\n        ontology = json.load(f)\\n\\n    VALID_ENTITY_TYPES = set(t.upper() for t in ontology[\\\"entity_types\\\"])\\n\\n    rel_types_raw = ontology[\\\"relation_types\\\"]\\n    if isinstance(rel_types_raw, dict):\\n        pcode_to_name = rel_types_raw\\n        use_pcodes = True\\n    else:\\
…[truncated 1204 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T18:10:42.475377+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "tail -200 /root/schema_semantic_constrained_ie/scripts/eval_d064.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "tail -200 /root/schema_semantic_constrained_ie/scripts/eval_d064.py"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T18:10:42.475535+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "tail -100 /root/schema_semantic_constrained_ie/estimate_fallback_rate.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "tail -100 /root/schema_semantic_constrained_ie/estimate_fallback_rate.py"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T18:10:42.475698+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "head -30 /root/schema_semantic_constrained_ie/ontology_constraints.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "head -30 /root/schema_semantic_constrained_ie/ontology_constraints.json"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T18:10:42.475944+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Unified evaluation for d064 beam search experiments (multi-dataset).\\nUsage: python scripts/eval_d064.py --input_path &lt;output.jsonl> --dataset scierc [--label &lt;name>]\\nComputes: ET%, RV%, DR%, CF%, Entity F1, Relation F1, Parse Fail%\\n\\\"\\\"\\\"\\nimport json\\nimport argparse\\nimport sys\\nfrom collections import defaultdict\\nfrom pathlib import Path\\n\\nDATASET_ONTOLOGY = {\\n    \\\"docred\\\": \\\"/root/schema_semantic_constrained_ie/data/docred/ontology_constraints_docred.json\\\",\\n    \\\"scierc\\\": \\\"/root/schema_semantic_constrained_ie/ontology_constraints.json\\\",\\n    \\\"ace05\\\": \\\"/root/schema_semantic_constrained_ie/data/ace05/ontology_constraints_ace05.json\\\",\\n    \\\"wikievents\\\": \\\"/root/schema_semantic_constrained_ie/data/wikievents/ontology_constraints_wikievents.json\\\",\\n}\\n\\nENTITY_TYPE_ALIASES = {\\n    'PERSON': 'PER', 'PEOPLE': 'PER',\\n    'ORGANIZATION': 'ORG', 'ORGANISATION': 'ORG',\\n    'LOCATION': 'LOC', 'NUMBER': 'NUM', 'NUMERICAL': 'NUM',\\n    'MISCELLANEOUS': 'MISC',\\n}\\n\\ndef normalize_etype(raw):\\n    t = raw.strip().upper()\\n    return ENTITY_TYPE_ALIASES.get(t, t)\\n\\ndef main():\\n    parser = argparse.ArgumentParser()\\n    parser.add_argument(\\\"--input_path\\\", required=True)\\n    parser.add_argument(\\\"--dataset\\\", default=\\\"docred\\\", choices=DATASET_ONTOLOGY.keys())\\n    parser.add_argument(\\\"--label\\\", default=\\\"\\\")\\n    parser.add_argument(\\\"--output_json\\\", default=\\\"\\\")\\n    args = parser.parse_args()\\n\\n    ontology_file = DATASET_ONTOLOGY[args.dataset]\\n    with open(ontology_file) as f:\\n        ontology = json.load(f)\\n\\n    VALID_ENTITY_TYPES = set(t.upper() for t in ontology[\\\"entity_types\\\"])\\n\\n    rel_types_raw = ontology[\\\"relation_types\\\"]\\n    if isinstance(rel_types_raw, dict):\\n        pcode_to_name = rel_types_raw\\n        use_pcodes = True\\n    else:\\
…[truncated 6998 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-20T18:10:42.476173+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n    with open(output_path) as f:\\n        for line in f:\\n            doc = json.loads(line)\\n            n_docs += 1\\n            parsed = doc.get(\\\"parsed_output\\\") or {}\\n            rels = parsed.get(\\\"relations\\\", []) if parsed else []\\n\\n            for r in rels:\\n                total_triples += 1\\n                rel_name = r.get(\\\"type\\\", \\\"\\\")\\n                ht = normalize_scierc_type(r.get(\\\"head_type\\\", \\\"\\\"), valid_entity_types)\\n                tt = normalize_scierc_type(r.get(\\\"tail_type\\\", \\\"\\\"), valid_entity_types)\\n\\n                if ht is None or tt is None:\\n                    continue\\n\\n                # Match relation\\n                rel_key = rel_name.lower().replace(\\\"-\\\", \\\"\\\").replace(\\\" \\\", \\\"\\\").replace(\\\"_\\\", \\\"\\\")\\n                canon = canon_map.get(rel_key)\\n                if canon is None:\\n                    unmatched_relations[rel_name] += 1\\n                    continue\\n\\n                per_rel_stats[canon][\\\"total\\\"] += 1\\n                pair = (ht, tt)\\n                if canon in valid_pairs and pair not in valid_pairs[canon]:\\n                    fallback_triples += 1\\n                    per_rel_stats[canon][\\\"fallback\\\"] += 1\\n                    if len(fallback_examples) < 10:\\n                        fallback_examples.append({\\n                            \\\"doc_id\\\": doc.get(\\\"doc_id\\\", \\\"\\\"),\\n                            \\\"relation\\\": rel_name, \\\"canonical\\\": canon,\\n                            \\\"head_type\\\": ht, \\\"tail_type\\\": tt,\\n                            \\\"head\\\": r.get(\\\"head\\\", \\\"\\\"), \\\"tail\\\": r.get(\\\"tail\\\", \\\"\\\"),\\n                        })\\n\\n    per_rel_fallback = {}\\n    for rname, s in sorted(per_rel_stats.items()):\\n        if s[\\\"total\\\"] > 0:\\n            per_rel_fallback[rn
…[truncated 3021 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T18:10:42.476362+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"entity_types\\\": [\\n    \\\"Task\\\",\\n    \\\"Method\\\",\\n    \\\"Material\\\",\\n    \\\"Metric\\\",\\n    \\\"OtherScientificTerm\\\",\\n    \\\"Generic\\\"\\n  ],\\n  \\\"relation_types\\\": [\\n    \\\"Used-for\\\",\\n    \\\"Feature-of\\\",\\n    \\\"Hyponym-of\\\",\\n    \\\"Part-of\\\",\\n    \\\"Compare\\\",\\n    \\\"Conjunction\\\",\\n    \\\"Evaluate-for\\\"\\n  ],\\n  \\\"raw_to_canonical\\\": {\\n    \\\"USED-FOR\\\": \\\"Used-for\\\",\\n    \\\"FEATURE-OF\\\": \\\"Feature-of\\\",\\n    \\\"HYPONYM-OF\\\": \\\"Hyponym-of\\\",\\n    \\\"PART-OF\\\": \\\"Part-of\\\",\\n    \\\"COMPARE\\\": \\\"Compare\\\",\\n    \\\"CONJUNCTION\\\": \\\"Conjunction\\\",\\n    \\\"EVALUATE-FOR\\\": \\\"Evaluate-for\\\"\\n  },\\n  \\\"entity_type_stats\\\": {\\n    \\\"total\\\": 5598,\\n    \\\"distribution\\\": {\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T18:10:42.476555+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "head -60 /root/schema_semantic_constrained_ie/data/docred/ontology_constraints_docred.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "head -60 /root/schema_semantic_constrained_ie/data/docred/ontology_constraints_docred.json"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T18:10:42.476707+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "ls /root/autodl-tmp/schema_outputs/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "ls /root/autodl-tmp/schema_outputs/"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-20T18:10:42.476900+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"entity_types\\\": [\\n    \\\"LOC\\\",\\n    \\\"MISC\\\",\\n    \\\"NUM\\\",\\n    \\\"ORG\\\",\\n    \\\"PER\\\",\\n    \\\"TIME\\\"\\n  ],\\n  \\\"relation_types\\\": {\\n    \\\"P6\\\": \\\"head of government\\\",\\n    \\\"P17\\\": \\\"country\\\",\\n    \\\"P19\\\": \\\"place of birth\\\",\\n    \\\"P20\\\": \\\"place of death\\\",\\n    \\\"P22\\\": \\\"father\\\",\\n    \\\"P25\\\": \\\"mother\\\",\\n    \\\"P26\\\": \\\"spouse\\\",\\n    \\\"P27\\\": \\\"country of citizenship\\\",\\n    \\\"P30\\\": \\\"continent\\\",\\n    \\\"P31\\\": \\\"instance of\\\",\\n    \\\"P35\\\": \\\"head of state\\\",\\n    \\\"P36\\\": \\\"capital\\\",\\n    \\\"P37\\\": \\\"official language\\\",\\n    \\\"P39\\\": \\\"position held\\\",\\n    \\\"P40\\\": \\\"child\\\",\\n    \\\"P50\\\": \\\"author\\\",\\n    \\\"P54\\\": \\\"member of sports team\\\",\\n    \\\"P57\\\": \\\"director\\\",\\n    \\\"P58\\\": \\\"screenwriter\\\",\\n    \\\"P69\\\": \\\"educated at\\\",\\n    \\\"P86\\\": \\\"composer\\\",\\n    \\\"P102\\\": \\\"member of political party\\\",\\n    \\\"P108\\\": \\\"employer\\\",\\n    \\\"P112\\\": \\\"founded by\\\",\\n    \\\"P118\\\": \\\"league\\\",\\n    \\\"P123\\\": \\\"publisher\\\",\\n    \\\"P127\\\": \\\"owned by\\\",\\n    \\\"P131\\\": \\\"located in the administrative territorial entity\\\",\\n    \\\"P136\\\": \\\"genre\\\",\\n    \\\"P137\\\": \\\"operator\\\",\\n    \\\"P140\\\": \\\"religion\\\",\\n    \\\"P150\\\": \\\"contains administrative territorial entity\\\",\\n    \\\"P155\\\": \\\"follows\\\",\\n    \\\"P156\\\": \\\"followed by\\\",\\n    \\\"P159\\\": \\\"headquarters location\\\",\\n    \\\"P161\\\": \\\"cast member\\\",\\n    \\\"P162\\\": \\\"producer\\\",\\n    \\\"P166\\\": \\\"award received\\\",\\n    \\\"P170\\\": \\\"creator\\\",\\n    \\\"P171\\\": \\\"parent taxon\\\",\\n    \\\"P172\\\": \\\"ethnic group\\\",\\n    \\\"P175\\\": \\\"performer\\\",\\
…[truncated 462 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T18:10:42.477076+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"70b_docred_constrained.jsonl\\n70b_docred_unconstrained.jsonl\\nd064_beam4_con_16980.log\\nd064_beam4_unc_16980.log\\nd064_eval_llama_beam4_con.json\\nd064_eval_llama_beam4_unc.json\\nd064_llama_docred_beam4_constrained_16980.jsonl\\nd064_llama_docred_beam4_unconstrained_16980.jsonl\\nd065_cascade.log\\nd065_cascade_qwen.sh\\nd065_eval_llama_con_4096.json\\nd065_eval_llama_unc_4096.json\\nd065_llama_docred_greedy_con_4096.jsonl\\nd065_llama_docred_greedy_unc_4096.jsonl\\nd065_llama_greedy_con.log\\nd065_llama_greedy_unc.log\\nd065_qwen_docred_greedy_con_4096.jsonl\\nd065_violation_llama_con_4096.json\\nd065_violation_llama_unc_4096.json\\nd065_watcher.log\\nd066_beam_sweep\\nd066_qwen_beam_sweep.log\\nd066_qwen_beam_sweep.sh\\ndocred_dev_200.json\\nr12_dr_f1_impact.json\\nr12_fallback_cascade_analysis.json\\nr12_fallback_cascade_text.txt\\nr12_wikievents_bootstrap.json\\nunified_eval\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T18:10:42.477233+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "grep -c \"valid_pairs\" /root/schema_semantic_constrained_ie/ontology_constraints.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "grep -c \"valid_pairs\" /root/schema_semantic_constrained_ie/ontology_constraints.json"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T18:10:42.477359+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "grep -c \"valid_pairs\" /root/schema_semantic_constrained_ie/data/docred/ontology_constraints_docred.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "grep -c \"valid_pairs\" /root/schema_semantic_constrained_ie/data/docred/ontology_constraints_docred.json"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-20T18:10:42.477487+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"7\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T18:10:42.477622+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"99\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T18:10:42.477858+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-16980",
  "command": "cat > /root/schema_semantic_constrained_ie/scripts/analyze_fallback_precision_recall.py << 'PYEOF'\n\"\"\"Fallback triples precision/recall analysis.\n\nPartitions predicted triples into fallback vs non-fallback (based on\nontology type-pair constraints), then computes precision and recall\nseparately for each partition.\n\"\"\"\nimport json\nfrom collections import defaultdict\nfrom pathlib import Path\n\n# --- Type normalization (from estimate_fallback_rate.py / eval_d064.py) ---\n\nDOCRED_TYPE_ALIASES = {\n    'PERSON': 'PER', 'PEOPLE': 'PER',\n    'ORGANIZATION': 'ORG', 'ORGANISATION': 'ORG',\n    'LOCATION': 'LOC', 'NUMBER': 'NUM', 'NUMERICAL': 'NUM',\n    'MISCELLANEOUS': 'MISC',\n}\n\nSCIERC_TYPE_MAP = {\n    \"otherscientificterm\": \"OtherScientificTerm\",\n    \"other-scientificterm\": \"OtherScientificTerm\",\n    \"other_scientific_term\": \"OtherScientificTerm\",\n    \"scientificterm\": \"OtherScientificTerm\",\n    \"other\": \"OtherScientificTerm\",\n}\n\n\ndef normalize_docred_type(raw):\n    t = raw.strip().upper()\n    return DOCRED_TYPE_ALIASES.get(t, t)\n\n\ndef normalize_scierc_type(raw, valid_types):\n    t_lower = raw.strip().lower().replace(\" \", \"\").replace(\"_\", \"\").replace(\"-\", \"\")\n    for vt in valid_types:\n        if t_lower == vt.lower().replace(\" \", \"\").replace(\"_\", \"\").replace(\"-\", \"\"):\n            return vt\n    return SCIERC_TYPE_MAP.get(t_lower, None)\n\n\ndef prf(tp, fp, fn):\n    p = tp / (tp + fp) if (tp + fp) > 0 else 0.0\n    r = tp / (tp + fn) if (tp + fn) > 0 else 0.0\n    f1 = 2 * p * r / (p + r) if (p + r) > 0 else 0.0\n    return round(p, 4), round(r, 4), round(f1, 4)\n\n\n# --- DocRED analysis ---\n\ndef analyze_docred(output_path, constraints_path):\n    with open(constraints_path) as f:\n        C = json.load(f)\n\n    rel_types = C[\"relation_types\"]  # {P-code: name}\n    rel_constraints = C[\"relation_constraints\"]\n\n    # name -> P-code mapping\n    name_to_pid = {}\n    for pid, name in rel_types.items():\n        name_to_pid[name.lower().strip()] = pid\n        name_to_pid[pid.lower()] = pid\n\n    # pcode -> name (lowercase) for gold matching\n    pcode_to_name_lower = {pid: name.lower().strip() for pid, name in rel_types.items()}\n\n    # valid_pairs per P-code\n    valid_pairs = {}\n    for pid, info in rel_constraints.items():\n        valid_pairs[pid] = set(tuple(p) for p in info[\"valid_pairs\"])\n\n    # Counters\n    fb_tp = fb_fp = 0\n    nfb_tp = nfb_fp = 0\n    total_gold = 0\n    gold_matched_by_fb = 0\n    gold_matched_by_nfb = 0\n\n    with open(output_path) as f:\n        for line in f:\n            doc = json.loads(line)\n            parsed = doc.get(\"parsed_output\") or {}\n            pred_rels = parsed.get(\"relations\", []) if parsed else []\n            gold_rels = doc.get(\"gold_relations\", [])\n\n            # Build gold set: (head, tail, relation_name_lower)\n            gold_set = set()\n            for r in gold_rels:\n                rtype_name = pcode_to_name_lower.get(r[\"type\"], r[\"type\"].lower().strip())\n                gold_set.add((r[\"head\"], r[\"tail\"], rtype_name))\n            total_gold += len(gold_set)\n\n            # Classify predictions and check matches\n            fb_matched_this_doc = set()\n            nfb_matched_this_doc = set()\n\n            for r in pred_rels:\n                rel_name = r.get(\"type\", \"\")\n                ht = normalize_docred_type(r.get(\"head_type\", \"\"))\n                tt = normalize_docred_type(r.get(\"tail_type\", \"\"))\n\n                pid = name_to_pid.get(rel_name.lower().strip())\n                pred_key = (r.get(\"head\", \"\"), r.get(\"tail\", \"\"), rel_name.lower().strip())\n\n                # Determine fallback\n                is_fallback = False\n                if pid and pid in valid_pairs:\n                    pair = (ht, tt)\n                    if pair not in valid_pairs[pid]:\n                        is_fallback = True\n\n                matched = pred_key in gold_set\n\n                if is_fallback:\n                    if matched:\n                        fb_tp += 1\n                        fb_matched_this_doc.add(pred_key)\n                    else:\n                        fb_fp += 1\n                else:\n                    if matched:\n                        nfb_tp += 1\n                        nfb_matched_this_doc.add(pred_key)\n                    else:\n                        nfb_fp += 1\n\n            gold_matched_by_fb += len(fb_matched_this_doc)\n            gold_matched_by_nfb += len(nfb_matched_this_doc)\n\n    # FN for each group: gold triples not matched by that group\n    # But total recall = (fb_matched + nfb_matched) / total_gold\n    fb_fn = total_gold - gold_matched_by_fb\n    nfb_fn = total_gold - gold_matched_by_nfb\n\n    p_fb, r_fb, f1_fb = prf(fb_tp, fb_fp, fb_fn)\n    p_nfb, r_nfb, f1_nfb = prf(nfb_tp, nfb_fp, nfb_fn)\n\n    # Overall\n    total_tp = fb_tp + nfb_tp\n    total_fp = fb_fp + nfb_fp\n    total_fn = total_gold - (gold_matched_by_fb + gold_matched_by_nfb)\n    p_all, r_all, f1_all = prf(total_tp, total_fp, total_fn)\n\n    return {\n        \"fallback_triples\": {\n            \"count\": fb_tp + fb_fp,\n            \"tp\": fb_tp, \"fp\": fb_fp,\n            \"precision\": p_fb,\n            \"recall_contribution\": round(gold_matched_by_fb / max(total_gold, 1), 4),\n        },\n        \"non_fallback_triples\": {\n            \"count\": nfb_tp + nfb_fp,\n            \"tp\": nfb_tp, \"fp\": nfb_fp,\n            \"precision\": p_nfb,\n            \"recall_contribution\": round(gold_matched_by_nfb / max(total_gold, 1), 4),\n        },\n        \"overall\": {\n            \"count\": fb_tp + fb_fp + nfb_tp + nfb_fp,\n            \"precision\": p_all, \"recall\": r_all, \"f1\": f1_all,\n            \"total_gold\": total_gold,\n        },\n        \"delta_precision\": round(p_fb - p_nfb, 4),\n    }\n\n\n# --- SciERC analysis ---\n\ndef analyze_scierc(output_path, constraints_path):\n    with open(constraints_path) as f:\n        C = json.load(f)\n\n    valid_entity_types = C[\"entity_types\"]\n    relation_types = C[\"relation_types\"]  # list of strings\n    rel_constraints = C.get(\"relation_constraints\", {})\n\n    # Build canonical relation name map\n    canon_map = {}\n    for rt in relation_types:\n        k = rt.lower().replace(\"-\", \"\").replace(\" \", \"\").replace(\"_\", \"\")\n        canon_map[k] = rt\n\n    # valid_pairs per relation\n    valid_pairs = {}\n    for rname, info in rel_constraints.items():\n        valid_pairs[rname] = set(tuple(p) for p in info[\"valid_pairs\"])\n\n    fb_tp = fb_fp = 0\n    nfb_tp = nfb_fp = 0\n    total_gold = 0\n    gold_matched_by_fb = 0\n    gold_matched_by_nfb = 0\n\n    with open(output_path) as f:\n        for line in f:\n            doc = json.loads(line)\n            parsed = doc.get(\"parsed_output\") or {}\n            pred_rels = parsed.get(\"relations\", []) if parsed else []\n            gold_rels = doc.get(\"gold_relations\", [])\n\n            # Gold set: (head, tail, relation_name_lower)\n            gold_set = set()\n            for r in gold_rels:\n                gold_set.add((r[\"head\"], r[\"tail\"], r[\"type\"].lower().strip()))\n            total_gold += len(gold_set)\n\n            fb_matched_this_doc = set()\n            nfb_matched_this_doc = set()\n\n            for r in pred_rels:\n                rel_name = r.get(\"type\", \"\")\n                ht = normalize_scierc_type(r.get(\"head_type\", \"\"), valid_entity_types)\n                tt = normalize_scierc_type(r.get(\"tail_type\", \"\"), valid_entity_types)\n\n                pred_key = (r.get(\"head\", \"\"), r.get(\"tail\", \"\"), rel_name.lower().strip())\n\n                # Canonicalize relation\n                rel_key = rel_name.lower().replace(\"-\", \"\").replace(\" \", \"\").replace(\"_\", \"\")\n                canon = canon_map.get(rel_key)\n\n                # Determine fallback\n                is_fallback = False\n                if ht is not None and tt is not None and canon and canon in valid_pairs:\n                    pair = (ht, tt)\n                    if pair not in valid_pairs[canon]:\n                        is_fallback = True\n\n                matched = pred_key in gold_set\n\n                if is_fallback:\n                    if matched:\n                        fb_tp += 1\n                        fb_matched_this_doc.add(pred_key)\n                    else:\n                        fb_fp += 1\n                else:\n                    if matched:\n                        nfb_tp += 1\n                        nfb_matched_this_doc.add(pred_key)\n                    else:\n                        nfb_fp += 1\n\n            gold_matched_by_fb += len(fb_matched_this_doc)\n            gold_matched_by_nfb += len(nfb_matched_this_doc)\n\n    fb_fn = total_gold - gold_matched_by_fb\n    nfb_fn = total_gold - gold_matched_by_nfb\n\n    p_fb, r_fb, f1_fb = prf(fb_tp, fb_fp, fb_fn)\n    p_nfb, r_nfb, f1_nfb = prf(nfb_tp, nfb_fp, nfb_fn)\n\n    total_tp = fb_tp + nfb_tp\n    total_fp = fb_fp + nfb_fp\n    total_fn = total_gold - (gold_matched_by_fb + gold_matched_by_nfb)\n    p_all, r_all, f1_all = prf(total_tp, total_fp, total_fn)\n\n    return {\n        \"fallback_triples\": {\n            \"count\": fb_tp + fb_fp,\n            \"tp\": fb_tp, \"fp\": fb_fp,\n            \"precision\": p_fb,\n            \"recall_contribution\": round(gold_matched_by_fb / max(total_gold, 1), 4),\n        },\n        \"non_fallback_triples\": {\n            \"count\": nfb_tp + nfb_fp,\n            \"tp\": nfb_tp, \"fp\": nfb_fp,\n            \"precision\": p_nfb,\n            \"recall_contribution\": round(gold_matched_by_nfb / max(total_gold, 1), 4),\n        },\n        \"overall\": {\n            \"count\": fb_tp + fb_fp + nfb_tp + nfb_fp,\n            \"precision\": p_all, \"recall\": r_all, \"f1\": f1_all,\n            \"total_gold\": total_gold,\n        },\n        \"delta_precision\": round(p_fb - p_nfb, 4),\n    }\n\n\nif __name__ == \"__main__\":\n    base = Path(\"/root/schema_semantic_constrained_ie\")\n    out_dir = Path(\"/root/autodl-tmp/schema_outputs\")\n    out_dir.mkdir(parents=True, exist_ok=True)\n\n    results = {}\n\n    # DocRED\n    print(\"=== DocRED Qwen ZS (full_s1) ===\")\n    results[\"docred_qwen_zs\"] = analyze_docred(\n        base / \"outputs/docred_full_s1.jsonl\",\n        base / \"data/docred/ontology_constraints_docred.json\",\n    )\n    d = results[\"docred_qwen_zs\"]\n    print(f\"  Fallback:     n={d['fallback_triples']['count']:>5}, \"\n          f\"P={d['fallback_triples']['precision']:.4f}, \"\n          f\"recall_contrib={d['fallback_triples']['recall_contribution']:.4f}\")\n    print(f\"  Non-fallback: n={d['non_fallback_triples']['count']:>5}, \"\n          f\"P={d['non_fallback_triples']['precision']:.4f}, \"\n          f\"recall_contrib={d['non_fallback_triples']['recall_contribution']:.4f}\")\n    print(f\"  Overall:      P={d['overall']['precision']:.4f}, \"\n          f\"R={d['overall']['recall']:.4f}, F1={d['overall']['f1']:.4f}\")\n    print(f\"  Delta P (fb - nfb): {d['delta_precision']:+.4f}\")\n\n    # SciERC\n    print(\"\\n=== SciERC Qwen ZS (full_s1) ===\")\n    results[\"scierc_qwen_zs\"] = analyze_scierc(\n        base / \"outputs/phase2_scierc_full_s1_v2.jsonl\",\n        base / \"ontology_constraints.json\",\n    )\n    s = results[\"scierc_qwen_zs\"]\n    print(f\"  Fallback:     n={s['fallback_triples']['count']:>5}, \"\n          f\"P={s['fallback_triples']['precision']:.4f}, \"\n          f\"recall_contrib={s['fallback_triples']['recall_contribution']:.4f}\")\n    print(f\"  Non-fallback: n={s['non_fallback_triples']['count']:>5}, \"\n          f\"P={s['non_fallback_triples']['precision']:.4f}, \"\n          f\"recall_contrib={s['non_fallback_triples']['recall_contribution']:.4f}\")\n    print(f\"  Overall:      P={s['overall']['precision']:.4f}, \"\n          f\"R={s['overall']['recall']:.4f}, F1={s['overall']['f1']:.4f}\")\n    print(f\"  Delta P (fb - nfb): {s['delta_precision']:+.4f}\")\n\n    # Save JSON\n    json_path = out_dir / \"r12_fallback_precision_recall.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(results, f, indent=2, ensure_ascii=False)\n    print(f\"\\nJSON saved to {json_path}\")\n\n    # Generate text summary\n    lines = []\n    lines.append(\"Fallback Precision/Recall Analysis (Qwen ZS, S1 constrained)\")\n    lines.append(\"=\" * 60)\n\n    for label, key in [(\"DocRED\", \"docred_qwen_zs\"), (\"SciERC\", \"scierc_qwen_zs\")]:\n        r = results[key]\n        fb = r[\"fallback_triples\"]\n        nfb = r[\"non_fallback_triples\"]\n        ov = r[\"overall\"]\n        lines.append(f\"\\n{label}:\")\n        lines.append(f\"  Fallback triples:     n={fb['count']}, \"\n                     f\"P={fb['precision']:.4f}, recall_contrib={fb['recall_contribution']:.4f} \"\n                     f\"(TP={fb['tp']}, FP={fb['fp']})\")\n        lines.append(f\"  Non-fallback triples: n={nfb['count']}, \"\n                     f\"P={nfb['precision']:.4f}, recall_contrib={nfb['recall_contribution']:.4f} \"\n                     f\"(TP={nfb['tp']}, FP={nfb['fp']})\")\n        lines.append(f\"  Overall: P={ov['precision']:.4f}, R={ov['recall']:.4f}, F1={ov['f1']:.4f} \"\n                     f\"(gold={ov['total_gold']})\")\n        lines.append(f\"  Precision gap (fb - nfb): {r['delta_precision']:+.4f}\")\n\n    lines.append(\"\\n\" + \"=\" * 60)\n    lines.append(\"Key finding:\")\n    dp_doc = results[\"docred_qwen_zs\"][\"delta_precision\"]\n    dp_sci = results[\"scierc_qwen_zs\"][\"delta_precision\"]\n    fb_p_doc = results[\"docred_qwen_zs\"][\"fallback_triples\"][\"precision\"]\n    nfb_p_doc = results[\"docred_qwen_zs\"][\"non_fallback_triples\"][\"precision\"]\n    fb_rc_doc = results[\"docred_qwen_zs\"][\"fallback_triples\"][\"recall_contribution\"]\n    nfb_rc_doc = results[\"docred_qwen_zs\"][\"non_fallback_triples\"][\"recall_contribution\"]\n\n    if dp_doc < 0:\n        lines.append(f\"On DocRED (n=1770 fallback triples), fallback precision ({fb_p_doc:.1%}) \"\n                     f\"is {abs(dp_doc):.1%} lower than non-fallback ({nfb_p_doc:.1%}), \"\n                     f\"confirming that type-pair constraint violations correlate with lower extraction quality. \"\n                     f\"Fallback triples contribute {fb_rc_doc:.1%} of total recall \"\n                     f\"vs {nfb_rc_doc:.1%} from non-fallback.\")\n    else:\n        lines.append(f\"On DocRED, fallback precision ({fb_p_doc:.1%}) \"\n                     f\"is comparable to or higher than non-fallback ({nfb_p_doc:.1%}), \"\n                     f\"suggesting type-pair violations do not degrade extraction quality. \"\n                     f\"Fallback triples contribute {fb_rc_doc:.1%} of total recall \"\n                     f\"vs {nfb_rc_doc:.1%} from non-fallback.\")\n\n    text = \"\\n\".join(lines)\n    text_path = out_dir / \"r12_fallback_pr_text.txt\"\n    with open(text_path, \"w\") as f:\n        f.write(text)\n    print(f\"Text saved to {text_path}\")\nPYEOF\necho \"Script written.\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-16980",
    "command": "cat > /root/schema_semantic_constrained_ie/scripts/analyze_fallback_precision_recall.py << 'PYEOF'\n\"\"\"Fallback triples precision/recall analysis.\n\nPartitions predicted triples into fallback vs non-fallback (based on\nontology type-pair constraints), then computes precision and recall\nseparately for each partition.\n\"\"\"\nimport json\nfrom collections import defaultdict\nfrom pathlib import Path\n\n# --- Type normalization (from estimate_fallback_rate.py / eval_d064.py) ---\n\nDOCRED_TYPE_ALIASES = {\n    'PERSON': 'PER', 'PEOPLE': 'PER',\n    'ORGANIZATION': 'ORG', 'ORGANISATION': 'ORG',\n    'LOCATION': 'LOC', 'NUMBER': 'NUM', 'NUMERICAL': 'NUM',\n    'MISCELLANEOUS': 'MISC',\n}\n\nSCIERC_TYPE_MAP = {\n    \"otherscientificterm\": \"OtherScientificTerm\",\n    \"other-scientificterm\": \"OtherScientificTerm\",\n    \"other_scientific_term\": \"OtherScientificTerm\",\n    \"scientificterm\": \"OtherScientificTerm\",\n    \"other\": \"OtherScientificTerm\",\n}\n\n\ndef normalize_docred_type(raw):\n    t = raw.strip().upper()\n    return DOCRED_TYPE_ALIASES.get(t, t)\n\n\ndef normalize_scierc_type(raw, valid_types):\n    t_lower = raw.strip().lower().replace(\" \", \"\").replace(\"_\", \"\").replace(\"-\", \"\")\n    for vt in valid_types:\n        if t_lower == vt.lower().replace(\" \", \"\").replace(\"_\", \"\").replace(\"-\", \"\"):\n            return vt\n    return SCIERC_TYPE_MAP.get(t_lower, None)\n\n\ndef prf(tp, fp, fn):\n    p = tp / (tp + fp) if (tp + fp) > 0 else 0.0\n    r = tp / (tp + fn) if (tp + fn) > 0 else 0.0\n    f1 = 2 * p * r / (p + r) if (p + r) > 0 else 0.0\n    return round(p, 4), round(r, 4), round(f1, 4)\n\n\n# --- DocRED analysis ---\n\ndef analyze_docred(output_path, constraints_path):\n    with open(constraints_path) as f:\n        C = json.load(f)\n\n    rel_types = C[\"relation_types\"]  # {P-code: name}\n    rel_constraints = C[\"relation_constraints\"]\n\n    # name -> P-code mapping\n    name_to_pid = {}\n    for pid, name in rel_types.items():\n        name_to_pid[name.lower().strip()] = pid\n        name_to_pid[pid.lower()] = pid\n\n    # pcode -> name (lowercase) for gold matching\n    pcode_to_name_lower = {pid: name.lower().strip() for pid, name in rel_types.items()}\n\n    # valid_pairs per P-code\n    valid_pairs = {}\n    for pid, info in rel_constraints.items():\n        valid_pairs[pid] = set(tuple(p) for p in info[\"valid_pairs\"])\n\n    # Counters\n    fb_tp = fb_fp = 0\n    nfb_tp = nfb_fp = 0\n    total_gold = 0\n    gold_matched_by_fb = 0\n    gold_matched_by_nfb = 0\n\n    with open(output_path) as f:\n        for line in f:\n            doc = json.loads(line)\n            parsed = doc.get(\"parsed_output\") or {}\n            pred_rels = parsed.get(\"relations\", []) if parsed else []\n            gold_rels = doc.get(\"gold_relations\", [])\n\n            # Build gold set: (head, tail, relation_name_lower)\n            gold_set = set()\n            for r in gold_rels:\n                rtype_name = pcode_to_name_lower.get(r[\"type\"], r[\"type\"].lower().strip())\n                gold_set.add((r[\"head\"], r[\"tail\"], rtype_name))\n            total_gold += len(gold_set)\n\n            # Classify predictions and check matches\n            fb_matched_this_doc = set()\n            nfb_matched_this_doc = set()\n\n            for r in pred_rels:\n                rel_name = r.get(\"type\", \"\")\n                ht = normalize_docred_type(r.get(\"head_type\", \"\"))\n                tt = normalize_docred_type(r.get(\"tail_type\", \"\"))\n\n                pid = name_to_pid.get(rel_name.lower().strip())\n                pred_key = (r.get(\"head\", \"\"), r.get(\"tail\", \"\"), rel_name.lower().strip())\n\n                # Determine fallback\n                is_fallback = False\n                if pid and pid in valid_pairs:\n                    pair = (ht, tt)\n                    if pair not in valid_pairs[pid]:\n                        is_fallback = True\n\n                matched = pred_key in gold_set\n\n                if is_fallback:\n                    if matched:\n                        fb_tp += 1\n                        fb_matched_this_doc.add(pred_key)\n                    else:\n                        fb_fp += 1\n                else:\n                    if matched:\n                        nfb_tp += 1\n                        nfb_matched_this_doc.add(pred_key)\n                    else:\n                        nfb_fp += 1\n\n            gold_matched_by_fb += len(fb_matched_this_doc)\n            gold_matched_by_nfb += len(nfb_matched_this_doc)\n\n    # FN for each group: gold triples not matched by that group\n    # But total recall = (fb_matched + nfb_matched) / total_gold\n    fb_fn = total_gold - gold_matched_by_fb\n    nfb_fn = total_gold - gold_matched_by_nfb\n\n    p_fb, r_fb, f1_fb = prf(fb_tp, fb_fp, fb_fn)\n    p_nfb, r_nfb, f1_nfb = prf(nfb_tp, nfb_fp, nfb_fn)\n\n    # Overall\n    total_tp = fb_tp + nfb_tp\n    total_fp = fb_fp + nfb_fp\n    total_fn = total_gold - (gold_matched_by_fb + gold_matched_by_nfb)\n    p_all, r_all, f1_all = prf(total_tp, total_fp, total_fn)\n\n    return {\n        \"fallback_triples\": {\n            \"count\": fb_tp + fb_fp,\n            \"tp\": fb_tp, \"fp\": fb_fp,\n            \"precision\": p_fb,\n            \"recall_contribution\": round(gold_matched_by_fb / max(total_gold, 1), 4),\n        },\n        \"non_fallback_triples\": {\n            \"count\": nfb_tp + nfb_fp,\n            \"tp\": nfb_tp, \"fp\": nfb_fp,\n            \"precision\": p_nfb,\n            \"recall_contribution\": round(gold_matched_by_nfb / max(total_gold, 1), 4),\n        },\n        \"overall\": {\n            \"count\": fb_tp + fb_fp + nfb_tp + nfb_fp,\n            \"precision\": p_all, \"recall\": r_all, \"f1\": f1_all,\n            \"total_gold\": total_gold,\n        },\n        \"delta_precision\": round(p_fb - p_nfb, 4),\n    }\n\n\n# --- SciERC analysis ---\n\ndef analyze_scierc(output_path, constraints_path):\n    with open(constraints_path) as f:\n        C = json.load(f)\n\n    valid_entity_types = C[\"entity_types\"]\n    relation_types = C[\"relation_types\"]  # list of strings\n    rel_constraints = C.get(\"relation_constraints\", {})\n\n    # Build canonical relation name map\n    canon_map = {}\n    for rt in relation_types:\n        k = rt.lower().replace(\"-\", \"\").replace(\" \", \"\").replace(\"_\", \"\")\n        canon_map[k] = rt\n\n    # valid_pairs per relation\n    valid_pairs = {}\n    for rname, info in rel_constraints.items():\n        valid_pairs[rname] = set(tuple(p) for p in info[\"valid_pairs\"])\n\n    fb_tp = fb_fp = 0\n    nfb_tp = nfb_fp = 0\n    total_gold = 0\n    gold_matched_by_fb = 0\n    gold_matched_by_nfb = 0\n\n    with open(output_path) as f:\n        for line in f:\n            doc = json.loads(line)\n            parsed = doc.get(\"parsed_output\") or {}\n            pred_rels = parsed.get(\"relations\", []) if parsed else []\n            gold_rels = doc.get(\"gold_relations\", [])\n\n            # Gold set: (head, tail, relation_name_lower)\n            gold_set = set()\n            for r in gold_rels:\n                gold_set.add((r[\"head\"], r[\"tail\"], r[\"type\"].lower().strip()))\n            total_gold += len(gold_set)\n\n            fb_matched_this_doc = set()\n            nfb_matched_this_doc = set()\n\n            for r in pred_rels:\n                rel_name = r.get(\"type\", \"\")\n                ht = normalize_scierc_type(r.get(\"head_type\", \"\"), valid_entity_types)\n                tt = normalize_scierc_type(r.get(\"tail_type\", \"\"), valid_entity_types)\n\n                pred_key = (r.get(\"head\", \"\"), r.get(\"tail\", \"\"), rel_name.lower().strip())\n\n                # Canonicalize relation\n                rel_key = rel_name.lower().replace(\"-\", \"\").replace(\" \", \"\").replace(\"_\", \"\")\n                canon = canon_map.get(rel_key)\n\n                # Determine fallback\n                is_fallback = False\n                if ht is not None and tt is not None and canon and canon in valid_pairs:\n                    pair = (ht, tt)\n                    if pair not in valid_pairs[canon]:\n                        is_fallback = True\n\n                matched = pred_key in gold_set\n\n                if is_fallback:\n                    if matched:\n                        fb_tp += 1\n                        fb_matched_this_doc.add(pred_key)\n                    else:\n                        fb_fp += 1\n                else:\n                    if matched:\n                        nfb_tp += 1\n                        nfb_matched_this_doc.add(pred_key)\n                    else:\n                        nfb_fp += 1\n\n            gold_matched_by_fb += len(fb_matched_this_doc)\n            gold_matched_by_nfb += len(nfb_matched_this_doc)\n\n    fb_fn = total_gold - gold_matched_by_fb\n    nfb_fn = total_gold - gold_matched_by_nfb\n\n    p_fb, r_fb, f1_fb = prf(fb_tp, fb_fp, fb_fn)\n    p_nfb, r_nfb, f1_nfb = prf(nfb_tp, nfb_fp, nfb_fn)\n\n    total_tp = fb_tp + nfb_tp\n    total_fp = fb_fp + nfb_fp\n    total_fn = total_gold - (gold_matched_by_fb + gold_matched_by_nfb)\n    p_all, r_all, f1_all = prf(total_tp, total_fp, total_fn)\n\n    return {\n        \"fallback_triples\": {\n            \"count\": fb_tp + fb_fp,\n            \"tp\": fb_tp, \"fp\": fb_fp,\n            \"precision\": p_fb,\n            \"recall_contribution\": round(gold_matched_by_fb / max(total_gold, 1), 4),\n        },\n        \"non_fallback_triples\": {\n            \"count\": nfb_tp + nfb_fp,\n            \"tp\": nfb_tp, \"fp\": nfb_fp,\n            \"precision\": p_nfb,\n            \"recall_contribution\": round(gold_matched_by_nfb / max(total_gold, 1), 4),\n        },\n        \"overall\": {\n            \"count\": fb_tp + fb_fp + nfb_tp + nfb_fp,\n            \"precision\": p_all, \"recall\": r_all, \"f1\": f1_all,\n            \"total_gold\": total_gold,\n        },\n        \"delta_precision\": round(p_fb - p_nfb, 4),\n    }\n\n\nif __name__ == \"__main__\":\n    base = Path(\"/root/schema_semantic_constrained_ie\")\n    out_dir = Path(\"/root/autodl-tmp/schema_outputs\")\n    out_dir.mkdir(parents=True, exist_ok=True)\n\n    results = {}\n\n    # DocRED\n    print(\"=== DocRED Qwen ZS (full_s1) ===\")\n    results[\"docred_qwen_zs\"] = analyze_docred(\n        base / \"outputs/docred_full_s1.jsonl\",\n        base / \"data/docred/ontology_constraints_docred.json\",\n    )\n    d = results[\"docred_qwen_zs\"]\n    print(f\"  Fallback:     n={d['fallback_triples']['count']:>5}, \"\n          f\"P={d['fallback_triples']['precision']:.4f}, \"\n          f\"recall_contrib={d['fallback_triples']['recall_contribution']:.4f}\")\n    print(f\"  Non-fallback: n={d['non_fallback_triples']['count']:>5}, \"\n          f\"P={d['non_fallback_triples']['precision']:.4f}, \"\n          f\"recall_contrib={d['non_fallback_triples']['recall_contribution']:.4f}\")\n    print(f\"  Overall:      P={d['overall']['precision']:.4f}, \"\n          f\"R={d['overall']['recall']:.4f}, F1={d['overall']['f1']:.4f}\")\n    print(f\"  Delta P (fb - nfb): {d['delta_precision']:+.4f}\")\n\n    # SciERC\n    print(\"\\n=== SciERC Qwen ZS (full_s1) ===\")\n    results[\"scierc_qwen_zs\"] = analyze_scierc(\n        base / \"outputs/phase2_scierc_full_s1_v2.jsonl\",\n        base / \"ontology_constraints.json\",\n    )\n    s = results[\"scierc_qwen_zs\"]\n    print(f\"  Fallback:     n={s['fallback_triples']['count']:>5}, \"\n          f\"P={s['fallback_triples']['precision']:.4f}, \"\n          f\"recall_contrib={s['fallback_triples']['recall_contribution']:.4f}\")\n    print(f\"  Non-fallback: n={s['non_fallback_triples']['count']:>5}, \"\n          f\"P={s['non_fallback_triples']['precision']:.4f}, \"\n          f\"recall_contrib={s['non_fallback_triples']['recall_contribution']:.4f}\")\n    print(f\"  Overall:      P={s['overall']['precision']:.4f}, \"\n          f\"R={s['overall']['recall']:.4f}, F1={s['overall']['f1']:.4f}\")\n    print(f\"  Delta P (fb - nfb): {s['delta_precision']:+.4f}\")\n\n    # Save JSON\n    json_path = out_dir / \"r12_fallback_precision_recall.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(results, f, indent=2, ensure_ascii=False)\n    print(f\"\\nJSON saved to {json_path}\")\n\n    # Generate text summary\n    lines = []\n    lines.append(\"Fallback Precision/Recall Analysis (Qwen ZS, S1 constrained)\")\n    lines.append(\"=\" * 60)\n\n    for label, key in [(\"DocRED\", \"docred_qwen_zs\"), (\"SciERC\", \"scierc_qwen_zs\")]:\n        r = results[key]\n        fb = r[\"fallback_triples\"]\n        nfb = r[\"non_fallback_triples\"]\n        ov = r[\"overall\"]\n        lines.append(f\"\\n{label}:\")\n        lines.append(f\"  Fallback triples:     n={fb['count']}, \"\n                     f\"P={fb['precision']:.4f}, recall_contrib={fb['recall_contribution']:.4f} \"\n                     f\"(TP={fb['tp']}, FP={fb['fp']})\")\n        lines.append(f\"  Non-fallback triples: n={nfb['count']}, \"\n                     f\"P={nfb['precision']:.4f}, recall_contrib={nfb['recall_contribution']:.4f} \"\n                     f\"(TP={nfb['tp']}, FP={nfb['fp']})\")\n        lines.append(f\"  Overall: P={ov['precision']:.4f}, R={ov['recall']:.4f}, F1={ov['f1']:.4f} \"\n                     f\"(gold={ov['total_gold']})\")\n        lines.append(f\"  Precision gap (fb - nfb): {r['delta_precision']:+.4f}\")\n\n    lines.append(\"\\n\" + \"=\" * 60)\n    lines.append(\"Key finding:\")\n    dp_doc = results[\"docred_qwen_zs\"][\"delta_precision\"]\n    dp_sci = results[\"scierc_qwen_zs\"][\"delta_precision\"]\n    fb_p_doc = results[\"docred_qwen_zs\"][\"fallback_triples\"][\"precision\"]\n    nfb_p_doc = results[\"docred_qwen_zs\"][\"non_fallback_triples\"][\"precision\"]\n    fb_rc_doc = results[\"docred_qwen_zs\"][\"fallback_triples\"][\"recall_contribution\"]\n    nfb_rc_doc = results[\"docred_qwen_zs\"][\"non_fallback_triples\"][\"recall_contribution\"]\n\n    if dp_doc < 0:\n        lines.append(f\"On DocRED (n=1770 fallback triples), fallback precision ({fb_p_doc:.1%}) \"\n                     f\"is {abs(dp_doc):.1%} lower than non-fallback ({nfb_p_doc:.1%}), \"\n                     f\"confirming that type-pair constraint violations correlate with lower extraction quality. \"\n                     f\"Fallback triples contribute {fb_rc_doc:.1%} of total recall \"\n                     f\"vs {nfb_rc_doc:.1%} from non-fallback.\")\n    else:\n        lines.append(f\"On DocRED, fallback precision ({fb_p_doc:.1%}) \"\n                     f\"is comparable to or higher than non-fallback ({nfb_p_doc:.1%}), \"\n                     f\"suggesting type-pair violations do not degrade extraction quality. \"\n                     f\"Fallback triples contribute {fb_rc_doc:.1%} of total recall \"\n                     f\"vs {nfb_rc_doc:.1%} from non-fallback.\")\n\n    text = \"\\n\".join(lines)\n    text_path = out_dir / \"r12_fallback_pr_text.txt\"\n    with open(text_path, \"w\") as f:\n        f.write(text)\n    print(f\"Text saved to {text_path}\")\nPYEOF\necho \"Script written.\""
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T18:10:42.478134+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T18:10:42.478267+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-16980",
  "command": "cd /root/schema_semantic_constrained_ie && python3 scripts/analyze_fallback_precision_recall.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-16980",
    "command": "cd /root/schema_semantic_constrained_ie && python3 scripts/analyze_fallback_precision_recall.py"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T18:10:42.478660+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== DocRED Qwen ZS (full_s1) ===\\n  Fallback:     n= 1770, P=0.0000, recall_contrib=0.0000\\n  Non-fallback: n=15571, P=0.0781, recall_contrib=0.0987\\n  Overall:      P=0.0701, R=0.0998, F1=0.0824\\n  Delta P (fb - nfb): -0.0781\\n\\n=== SciERC Qwen ZS (full_s1) ===\\n  Fallback:     n=   16, P=0.0000, recall_contrib=0.0000\\n  Non-fallback: n= 1713, P=0.0660, recall_contrib=0.1160\\n  Overall:      P=0.0654, R=0.1160, F1=0.0836\\n  Delta P (fb - nfb): -0.0660\\n\\nJSON saved to /root/autodl-tmp/schema_outputs/r12_fallback_precision_recall.json\\nText saved to /root/autodl-tmp/schema_outputs/r12_fallback_pr_text.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T18:10:42.479082+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "head -20 /root/schema_semantic_constrained_ie/outputs/eval_report_qwen_constrained.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "head -20 /root/schema_semantic_constrained_ie/outputs/eval_report_qwen_constrained.json"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T18:10:42.479275+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"meta\\\": {\\n    \\\"input_path\\\": \\\"outputs/wikievents_qwen_constrained_full.jsonl\\\",\\n    \\\"total_documents\\\": 246,\\n    \\\"documents_evaluated\\\": 197,\\n    \\\"parse_failures\\\": 49\\n  },\\n  \\\"entity_f1\\\": {\\n    \\\"precision\\\": 0.4352,\\n    \\\"recall\\\": 0.0823,\\n    \\\"f1\\\": 0.1384,\\n    \\\"tp\\\": 974,\\n    \\\"gold\\\": 11839,\\n    \\\"pred\\\": 2238\\n  },\\n  \\\"trigger_identification_f1\\\": {\\n    \\\"precision\\\": 0.1314,\\n    \\\"recall\\\": 0.1454,\\n    \\\"f1\\\": 0.138,\\n    \\\"tp\\\": 282,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T18:10:42.479722+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-16980",
  "command": "cd /root/schema_semantic_constrained_ie && python3 -c \"\nimport json\n\n# Check one DocRED doc\nwith open('outputs/docred_full_s1.jsonl') as f:\n    doc = json.loads(f.readline())\n\n# Load ontology\nwith open('data/docred/ontology_constraints_docred.json') as f:\n    C = json.load(f)\npcode_to_name = C['relation_types']\n\nprint('=== Doc:', doc['doc_id'], '===')\nprint()\nprint('Gold relations:')\nfor r in doc['gold_relations'][:5]:\n    name = pcode_to_name.get(r['type'], r['type']).lower().strip()\n    print(f'  ({r[\\\"head\\\"]}, {r[\\\"tail\\\"]}, {name})')\n\nparsed = doc.get('parsed_output', {})\npred_rels = parsed.get('relations', [])\nprint()\nprint('Pred relations:')\nfor r in pred_rels[:5]:\n    print(f'  ({r[\\\"head\\\"]}, {r[\\\"tail\\\"]}, {r[\\\"type\\\"].lower().strip()})')\n\n# Check for matches\ngold_set = set()\nfor r in doc['gold_relations']:\n    name = pcode_to_name.get(r['type'], r['type']).lower().strip()\n    gold_set.add((r['head'], r['tail'], name))\n\npred_set = set()\nfor r in pred_rels:\n    pred_set.add((r.get('head',''), r.get('tail',''), r.get('type','').lower().strip()))\n\nmatches = gold_set & pred_set\nprint(f'\\nGold: {len(gold_set)}, Pred: {len(pred_set)}, Matches: {len(matches)}')\nif matches:\n    for m in list(matches)[:3]:\n        print(f'  Match: {m}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-16980",
    "command": "cd /root/schema_semantic_constrained_ie && python3 -c \"\nimport json\n\n# Check one DocRED doc\nwith open('outputs/docred_full_s1.jsonl') as f:\n    doc = json.loads(f.readline())\n\n# Load ontology\nwith open('data/docred/ontology_constraints_docred.json') as f:\n    C = json.load(f)\npcode_to_name = C['relation_types']\n\nprint('=== Doc:', doc['doc_id'], '===')\nprint()\nprint('Gold relations:')\nfor r in doc['gold_relations'][:5]:\n    name = pcode_to_name.get(r['type'], r['type']).lower().strip()\n    print(f'  ({r[\\\"head\\\"]}, {r[\\\"tail\\\"]}, {name})')\n\nparsed = doc.get('parsed_output', {})\npred_rels = parsed.get('relations', [])\nprint()\nprint('Pred relations:')\nfor r in pred_rels[:5]:\n    print(f'  ({r[\\\"head\\\"]}, {r[\\\"tail\\\"]}, {r[\\\"type\\\"].lower().strip()})')\n\n# Check for matches\ngold_set = set()\nfor r in doc['gold_relations']:\n    name = pcode_to_name.get(r['type'], r['type']).lower().strip()\n    gold_set.add((r['head'], r['tail'], name))\n\npred_set = set()\nfor r in pred_rels:\n    pred_set.add((r.get('head',''), r.get('tail',''), r.get('type','').lower().strip()))\n\nmatches = gold_set & pred_set\nprint(f'\\nGold: {len(gold_set)}, Pred: {len(pred_set)}, Matches: {len(matches)}')\nif matches:\n    for m in list(matches)[:3]:\n        print(f'  Match: {m}')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T18:10:42.479989+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== Doc: Skai TV ===\\n\\nGold relations:\\n  (Piraeus, Greece, country)\\n  (Skai Group, Greece, country)\\n  (Athens, Greece, country)\\n  (Skai TV, Piraeus, headquarters location)\\n  (Skai TV, Skai Group, owned by)\\n\\nPred relations:\\n  (Skai TV, Greece, country of origin)\\n  (Skai TV, Piraeus, headquarters location)\\n  (Skai TV, Skai Group, part of)\\n  (Skai TV, Athens metropolitan area, location of formation)\\n  (Skai TV, Nova, operator)\\n\\nGold: 7, Pred: 14, Matches: 1\\n  Match: ('Skai TV', 'Piraeus', 'headquarters location')\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T18:10:42.480181+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-16980",
  "command": "cd /root/schema_semantic_constrained_ie && python3 scripts/eval_d064.py --input_path outputs/docred_full_s1.jsonl --dataset docred --label docred_s1_verify 2>&1 | tail -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-16980",
    "command": "cd /root/schema_semantic_constrained_ie && python3 scripts/eval_d064.py --input_path outputs/docred_full_s1.jsonl --dataset docred --label docred_s1_verify 2>&1 | tail -10"
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-20T18:10:42.480321+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-16980",
  "command": "cd /root/schema_semantic_constrained_ie && python3 scripts/eval_d064.py --input_path outputs/phase2_scierc_full_s1_v2.jsonl --dataset scierc --label scierc_s1_verify 2>&1 | tail -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-16980",
    "command": "cd /root/schema_semantic_constrained_ie && python3 scripts/eval_d064.py --input_path outputs/phase2_scierc_full_s1_v2.jsonl --dataset scierc --label scierc_s1_verify 2>&1 | tail -10"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-20T18:10:42.480469+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n=== docred_s1_verify ===\\nSamples: 998, Parse Fail: 11 (1.1%)\\nEntities pred: 20187, Relations pred: 17341\\nET%=0.00  RV%=0.03  DR%=10.21  CF%=2.57\\nE-F1=58.96 (P=58.40 R=59.54)\\nR-F1=8.17 (P=6.97 R=9.87)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.55}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-20T18:10:42.480602+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n=== scierc_s1_verify ===\\nSamples: 551, Parse Fail: 0 (0.0%)\\nEntities pred: 2474, Relations pred: 1729\\nET%=0.00  RV%=0.00  DR%=0.93  CF%=1.62\\nE-F1=30.98 (P=25.98 R=38.37)\\nR-F1=8.36 (P=6.54 R=11.60)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.56}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T18:10:42.481168+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-16980",
  "command": "cd /root/schema_semantic_constrained_ie && python3 -c \"\nimport json\nfrom collections import defaultdict\n\n# Load ontology\nwith open('data/docred/ontology_constraints_docred.json') as f:\n    C = json.load(f)\nrel_types = C['relation_types']\nrel_constraints = C['relation_constraints']\n\nname_to_pid = {}\nfor pid, name in rel_types.items():\n    name_to_pid[name.lower().strip()] = pid\n    name_to_pid[pid.lower()] = pid\n\npcode_to_name_lower = {pid: name.lower().strip() for pid, name in rel_types.items()}\nvalid_relation_names = set(name.lower().strip() for name in rel_types.values())\n\nDOCRED_TYPE_ALIASES = {\n    'PERSON': 'PER', 'PEOPLE': 'PER',\n    'ORGANIZATION': 'ORG', 'ORGANISATION': 'ORG',\n    'LOCATION': 'LOC', 'NUMBER': 'NUM', 'NUMERICAL': 'NUM',\n    'MISCELLANEOUS': 'MISC',\n}\n\nvalid_pairs = {}\nfor pid, info in rel_constraints.items():\n    valid_pairs[pid] = set(tuple(p) for p in info['valid_pairs'])\n\ndef norm_type(raw):\n    t = raw.strip().upper()\n    return DOCRED_TYPE_ALIASES.get(t, t)\n\n# Analyze fallback triples\nfb_valid_relname = 0\nfb_invalid_relname = 0\nfb_head_in_gold_entities = 0\nfb_tail_in_gold_entities = 0\nfb_pair_in_gold_entities = 0\nfb_total = 0\n\n# Also check: among fallback, entity pair (h,t) matches a gold entity pair?\nwith open('outputs/docred_full_s1.jsonl') as f:\n    for line in f:\n        doc = json.loads(line)\n        parsed = doc.get('parsed_output') or {}\n        pred_rels = parsed.get('relations', []) if parsed else []\n        gold_rels = doc.get('gold_relations', [])\n\n        gold_heads = set(r['head'] for r in gold_rels)\n        gold_tails = set(r['tail'] for r in gold_rels)\n        gold_pairs = set((r['head'], r['tail']) for r in gold_rels)\n\n        for r in pred_rels:\n            rel_name = r.get('type', '')\n            ht = norm_type(r.get('head_type', ''))\n            tt = norm_type(r.get('tail_type', ''))\n            pid = name_to_pid.get(rel_name.lower().strip())\n\n            is_fallback = False\n            if pid and pid in valid_pairs:\n                pair = (ht, tt)\n                if pair not in valid_pairs[pid]:\n                    is_fallback = True\n\n            if is_fallback:\n                fb_total += 1\n                if rel_name.lower().strip() in valid_relation_names:\n                    fb_valid_relname += 1\n                else:\n                    fb_invalid_relname += 1\n                if r.get('head','') in gold_heads:\n                    fb_head_in_gold_entities += 1\n                if r.get('tail','') in gold_tails:\n                    fb_tail_in_gold_entities += 1\n                if (r.get('head',''), r.get('tail','')) in gold_pairs:\n                    fb_pair_in_gold_entities += 1\n\nprint(f'Total fallback triples: {fb_total}')\nprint(f'  Valid relation name: {fb_valid_relname} ({fb_valid_relname/fb_total*100:.1f}%)')\nprint(f'  Invalid relation name: {fb_invalid_relname} ({fb_invalid_relname/fb_total*100:.1f}%)')\nprint(f'  Head in gold entities: {fb_head_in_gold_entities} ({fb_head_in_gold_entities/fb_total*100:.1f}%)')\nprint(f'  Tail in gold entities: {fb_tail_in_gold_entities} ({fb_tail_in_gold_entities/fb_total*100:.1f}%)')\nprint(f'  (head,tail) pair in gold: {fb_pair_in_gold_entities} ({fb_pair_in_gold_entities/fb_total*100:.1f}%)')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-16980",
    "command": "cd /root/schema_semantic_constrained_ie && python3 -c \"\nimport json\nfrom collections import defaultdict\n\n# Load ontology\nwith open('data/docred/ontology_constraints_docred.json') as f:\n    C = json.load(f)\nrel_types = C['relation_types']\nrel_constraints = C['relation_constraints']\n\nname_to_pid = {}\nfor pid, name in rel_types.items():\n    name_to_pid[name.lower().strip()] = pid\n    name_to_pid[pid.lower()] = pid\n\npcode_to_name_lower = {pid: name.lower().strip() for pid, name in rel_types.items()}\nvalid_relation_names = set(name.lower().strip() for name in rel_types.values())\n\nDOCRED_TYPE_ALIASES = {\n    'PERSON': 'PER', 'PEOPLE': 'PER',\n    'ORGANIZATION': 'ORG', 'ORGANISATION': 'ORG',\n    'LOCATION': 'LOC', 'NUMBER': 'NUM', 'NUMERICAL': 'NUM',\n    'MISCELLANEOUS': 'MISC',\n}\n\nvalid_pairs = {}\nfor pid, info in rel_constraints.items():\n    valid_pairs[pid] = set(tuple(p) for p in info['valid_pairs'])\n\ndef norm_type(raw):\n    t = raw.strip().upper()\n    return DOCRED_TYPE_ALIASES.get(t, t)\n\n# Analyze fallback triples\nfb_valid_relname = 0\nfb_invalid_relname = 0\nfb_head_in_gold_entities = 0\nfb_tail_in_gold_entities = 0\nfb_pair_in_gold_entities = 0\nfb_total = 0\n\n# Also check: among fallback, entity pair (h,t) matches a gold entity pair?\nwith open('outputs/docred_full_s1.jsonl') as f:\n    for line in f:\n        doc = json.loads(line)\n        parsed = doc.get('parsed_output') or {}\n        pred_rels = parsed.get('relations', []) if parsed else []\n        gold_rels = doc.get('gold_relations', [])\n\n        gold_heads = set(r['head'] for r in gold_rels)\n        gold_tails = set(r['tail'] for r in gold_rels)\n        gold_pairs = set((r['head'], r['tail']) for r in gold_rels)\n\n        for r in pred_rels:\n            rel_name = r.get('type', '')\n            ht = norm_type(r.get('head_type', ''))\n            tt = norm_type(r.get('tail_type', ''))\n            pid = name_to_pid.get(rel_name.lower().strip())\n\n            is_fallback = False\n            if pid and pid in valid_pairs:\n                pair = (ht, tt)\n                if pair not in valid_pairs[pid]:\n                    is_fallback = True\n\n            if is_fallback:\n                fb_total += 1\n                if rel_name.lower().strip() in valid_relation_names:\n                    fb_valid_relname += 1\n                else:\n                    fb_invalid_relname += 1\n                if r.get('head','') in gold_heads:\n                    fb_head_in_gold_entities += 1\n                if r.get('tail','') in gold_tails:\n                    fb_tail_in_gold_entities += 1\n                if (r.get('head',''), r.get('tail','')) in gold_pairs:\n                    fb_pair_in_gold_entities += 1\n\nprint(f'Total fallback triples: {fb_total}')\nprint(f'  Valid relation name: {fb_valid_relname} ({fb_valid_relname/fb_total*100:.1f}%)')\nprint(f'  Invalid relation name: {fb_invalid_relname} ({fb_invalid_relname/fb_total*100:.1f}%)')\nprint(f'  Head in gold entities: {fb_head_in_gold_entities} ({fb_head_in_gold_entities/fb_total*100:.1f}%)')\nprint(f'  Tail in gold entities: {fb_tail_in_gold_entities} ({fb_tail_in_gold_entities/fb_total*100:.1f}%)')\nprint(f'  (head,tail) pair in gold: {fb_pair_in_gold_entities} ({fb_pair_in_gold_entities/fb_total*100:.1f}%)')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-20T18:10:42.481412+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Total fallback triples: 1770\\n  Valid relation name: 1770 (100.0%)\\n  Invalid relation name: 0 (0.0%)\\n  Head in gold entities: 969 (54.7%)\\n  Tail in gold entities: 237 (13.4%)\\n  (head,tail) pair in gold: 65 (3.7%)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-20T18:10:42.481613+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-16980",
  "command": "cd /root/schema_semantic_constrained_ie && python3 -c \"\nimport json\n\nwith open('data/docred/ontology_constraints_docred.json') as f:\n    C = json.load(f)\nrel_types = C['relation_types']\nrel_constraints = C['relation_constraints']\n\nname_to_pid = {}\nfor pid, name in rel_types.items():\n    name_to_pid[name.lower().strip()] = pid\npcode_to_name = {pid: name.lower().strip() for pid, name in rel_types.items()}\n\nALIASES = {'PERSON':'PER','PEOPLE':'PER','ORGANIZATION':'ORG','ORGANISATION':'ORG',\n           'LOCATION':'LOC','NUMBER':'NUM','NUMERICAL':'NUM','MISCELLANEOUS':'MISC'}\ndef nt(raw):\n    t = raw.strip().upper()\n    return ALIASES.get(t, t)\n\nvalid_pairs = {}\nfor pid, info in rel_constraints.items():\n    valid_pairs[pid] = set(tuple(p) for p in info['valid_pairs'])\n\nmismatches = []\nwith open('outputs/docred_full_s1.jsonl') as f:\n    for line in f:\n        doc = json.loads(line)\n        parsed = doc.get('parsed_output') or {}\n        pred_rels = parsed.get('relations', []) if parsed else []\n        gold_rels = doc.get('gold_relations', [])\n        \n        gold_map = {}\n        for r in gold_rels:\n            key = (r['head'], r['tail'])\n            gold_map.setdefault(key, []).append(pcode_to_name.get(r['type'], r['type'].lower()))\n\n        for r in pred_rels:\n            rel_name = r.get('type','')\n            ht = nt(r.get('head_type',''))\n            tt = nt(r.get('tail_type',''))\n            pid = name_to_pid.get(rel_name.lower().strip())\n            is_fb = False\n            if pid and pid in valid_pairs:\n                if (ht, tt) not in valid_pairs[pid]:\n                    is_fb = True\n            if is_fb:\n                key = (r.get('head',''), r.get('tail',''))\n                if key in gold_map:\n                    mismatches.append({\n                        'pred_rel': rel_name.lower().strip(),\n                        'gold_rels': gold_map[key],\n                        'pred_types': f'{ht}/{tt}',\n                    })\n\nprint(f'Fallback triples with matching entity pair: {len(mismatches)}')\nprint()\n# Show distribution\nfrom collections import Counter\nmatch_count = 0\nfor m in mismatches:\n    if m['pred_rel'] in m['gold_rels']:\n        match_count += 1\n\nprint(f'Of those, pred_rel matches gold: {match_count}')\nprint(f'Pred_rel != gold: {len(mismatches) - match_count}')\nprint()\nprint('Examples (pred_rel vs gold_rels):')\nfor m in mismatches[:15]:\n    marker = 'MATCH' if m['pred_rel'] in m['gold_rels'] else 'MISS'\n    print(f'  [{marker}] pred={m[\\\"pred_rel\\\"]:40s} gold={m[\\\"gold_rels\\\"]} types={m[\\\"pred_types\\\"]}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-16980",
    "command": "cd /root/schema_semantic_constrained_ie && python3 -c \"\nimport json\n\nwith open('data/docred/ontology_constraints_docred.json') as f:\n    C = json.load(f)\nrel_types = C['relation_types']\nrel_constraints = C['relation_constraints']\n\nname_to_pid = {}\nfor pid, name in rel_types.items():\n    name_to_pid[name.lower().strip()] = pid\npcode_to_name = {pid: name.lower().strip() for pid, name in rel_types.items()}\n\nALIASES = {'PERSON':'PER','PEOPLE':'PER','ORGANIZATION':'ORG','ORGANISATION':'ORG',\n           'LOCATION':'LOC','NUMBER':'NUM','NUMERICAL':'NUM','MISCELLANEOUS':'MISC'}\ndef nt(raw):\n    t = raw.strip().upper()\n    return ALIASES.get(t, t)\n\nvalid_pairs = {}\nfor pid, info in rel_constraints.items():\n    valid_pairs[pid] = set(tuple(p) for p in info['valid_pairs'])\n\nmismatches = []\nwith open('outputs/docred_full_s1.jsonl') as f:\n    for line in f:\n        doc = json.loads(line)\n        parsed = doc.get('parsed_output') or {}\n        pred_rels = parsed.get('relations', []) if parsed else []\n        gold_rels = doc.get('gold_relations', [])\n        \n        gold_map = {}\n        for r in gold_rels:\n            key = (r['head'], r['tail'])\n            gold_map.setdefault(key, []).append(pcode_to_name.get(r['type'], r['type'].lower()))\n\n        for r in pred_rels:\n            rel_name = r.get('type','')\n            ht = nt(r.get('head_type',''))\n            tt = nt(r.get('tail_type',''))\n            pid = name_to_pid.get(rel_name.lower().strip())\n            is_fb = False\n            if pid and pid in valid_pairs:\n                if (ht, tt) not in valid_pairs[pid]:\n                    is_fb = True\n            if is_fb:\n                key = (r.get('head',''), r.get('tail',''))\n                if key in gold_map:\n                    mismatches.append({\n                        'pred_rel': rel_name.lower().strip(),\n                        'gold_rels': gold_map[key],\n                        'pred_types': f'{ht}/{tt}',\n                    })\n\nprint(f'Fallback triples with matching entity pair: {len(mismatches)}')\nprint()\n# Show distribution\nfrom collections import Counter\nmatch_count = 0\nfor m in mismatches:\n    if m['pred_rel'] in m['gold_rels']:\n        match_count += 1\n\nprint(f'Of those, pred_rel matches gold: {match_count}')\nprint(f'Pred_rel != gold: {len(mismatches) - match_count}')\nprint()\nprint('Examples (pred_rel vs gold_rels):')\nfor m in mismatches[:15]:\n    marker = 'MATCH' if m['pred_rel'] in m['gold_rels'] else 'MISS'\n    print(f'  [{marker}] pred={m[\\\"pred_rel\\\"]:40s} gold={m[\\\"gold_rels\\\"]} types={m[\\\"pred_types\\\"]}')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T18:10:42.481847+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Fallback triples with matching entity pair: 65\\n\\nOf those, pred_rel matches gold: 0\\nPred_rel != gold: 65\\n\\nExamples (pred_rel vs gold_rels):\\n  [MISS] pred=location                                 gold=['residence'] types=PER/LOC\\n  [MISS] pred=influenced by                            gold=['production company'] types=MISC/ORG\\n  [MISS] pred=cast member                              gold=['member of sports team'] types=PER/ORG\\n  [MISS] pred=participant of                           gold=['conflict'] types=PER/TIME\\n  [MISS] pred=producer                                 gold=['manufacturer'] types=ORG/ORG\\n  [MISS] pred=award received                           gold=['author'] types=MISC/PER\\n  [MISS] pred=participant of                           gold=['cast member'] types=MISC/PER\\n  [MISS] pred=participant of                           gold=['cast member'] types=MISC/PER\\n  [MISS] pred=applies to jurisdiction                  gold=['conflict'] types=ORG/TIME\\n  [MISS] pred=member of                                gold=['has part'] types=ORG/PER\\n  [MISS] pred=member of                                gold=['has part'] types=ORG/PER\\n  [MISS] pred=member of                                gold=['has part'] types=ORG/PER\\n  [MISS] pred=member of                                gold=['has part'] types=ORG/PER\\n  [MISS] pred=applies to jurisdiction                  gold=['country of citizenship'] types=PER/LOC\\n  [MISS] pred=applies to jurisdiction                  gold=['country of citizenship'] types=PER/LOC\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-20T18:10:42.482209+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-16980",
  "command": "cat > /root/schema_semantic_constrained_ie/scripts/analyze_fallback_precision_recall.py << 'PYEOF'\n\"\"\"Fallback triples precision/recall analysis with diagnostics.\"\"\"\nimport json\nfrom collections import defaultdict\nfrom pathlib import Path\n\nDOCRED_TYPE_ALIASES = {\n    'PERSON': 'PER', 'PEOPLE': 'PER',\n    'ORGANIZATION': 'ORG', 'ORGANISATION': 'ORG',\n    'LOCATION': 'LOC', 'NUMBER': 'NUM', 'NUMERICAL': 'NUM',\n    'MISCELLANEOUS': 'MISC',\n}\n\nSCIERC_TYPE_MAP = {\n    \"otherscientificterm\": \"OtherScientificTerm\",\n    \"other-scientificterm\": \"OtherScientificTerm\",\n    \"other_scientific_term\": \"OtherScientificTerm\",\n    \"scientificterm\": \"OtherScientificTerm\",\n    \"other\": \"OtherScientificTerm\",\n}\n\n\ndef normalize_docred_type(raw):\n    t = raw.strip().upper()\n    return DOCRED_TYPE_ALIASES.get(t, t)\n\n\ndef normalize_scierc_type(raw, valid_types):\n    t_lower = raw.strip().lower().replace(\" \", \"\").replace(\"_\", \"\").replace(\"-\", \"\")\n    for vt in valid_types:\n        if t_lower == vt.lower().replace(\" \", \"\").replace(\"_\", \"\").replace(\"-\", \"\"):\n            return vt\n    return SCIERC_TYPE_MAP.get(t_lower, None)\n\n\ndef prf(tp, fp, fn):\n    p = tp / (tp + fp) if (tp + fp) > 0 else 0.0\n    r = tp / (tp + fn) if (tp + fn) > 0 else 0.0\n    f1 = 2 * p * r / (p + r) if (p + r) > 0 else 0.0\n    return round(p, 4), round(r, 4), round(f1, 4)\n\n\ndef analyze_docred(output_path, constraints_path):\n    with open(constraints_path) as f:\n        C = json.load(f)\n\n    rel_types = C[\"relation_types\"]\n    rel_constraints = C[\"relation_constraints\"]\n\n    name_to_pid = {}\n    for pid, name in rel_types.items():\n        name_to_pid[name.lower().strip()] = pid\n        name_to_pid[pid.lower()] = pid\n\n    pcode_to_name_lower = {pid: name.lower().strip() for pid, name in rel_types.items()}\n\n    valid_pairs = {}\n    for pid, info in rel_constraints.items():\n        valid_pairs[pid] = set(tuple(p) for p in info[\"valid_pairs\"])\n\n    fb_tp = fb_fp = nfb_tp = nfb_fp = 0\n    total_gold = 0\n    gold_matched_by_fb = gold_matched_by_nfb = 0\n\n    # Diagnostics for fallback triples\n    fb_head_in_gold = 0\n    fb_tail_in_gold = 0\n    fb_pair_in_gold = 0\n    fb_pair_in_gold_wrong_rel = 0\n    fb_total = 0\n\n    with open(output_path) as f:\n        for line in f:\n            doc = json.loads(line)\n            parsed = doc.get(\"parsed_output\") or {}\n            pred_rels = parsed.get(\"relations\", []) if parsed else []\n            gold_rels = doc.get(\"gold_relations\", [])\n\n            gold_set = set()\n            for r in gold_rels:\n                rtype_name = pcode_to_name_lower.get(r[\"type\"], r[\"type\"].lower().strip())\n                gold_set.add((r[\"head\"], r[\"tail\"], rtype_name))\n            total_gold += len(gold_set)\n\n            gold_heads = set(r[\"head\"] for r in gold_rels)\n            gold_tails = set(r[\"tail\"] for r in gold_rels)\n            gold_pair_rels = defaultdict(set)\n            for r in gold_rels:\n                gold_pair_rels[(r[\"head\"], r[\"tail\"])].add(\n                    pcode_to_name_lower.get(r[\"type\"], r[\"type\"].lower().strip()))\n\n            fb_matched_doc = set()\n            nfb_matched_doc = set()\n\n            for r in pred_rels:\n                rel_name = r.get(\"type\", \"\")\n                ht = normalize_docred_type(r.get(\"head_type\", \"\"))\n                tt = normalize_docred_type(r.get(\"tail_type\", \"\"))\n                pid = name_to_pid.get(rel_name.lower().strip())\n                pred_key = (r.get(\"head\", \"\"), r.get(\"tail\", \"\"), rel_name.lower().strip())\n\n                is_fallback = False\n                if pid and pid in valid_pairs:\n                    if (ht, tt) not in valid_pairs[pid]:\n                        is_fallback = True\n\n                matched = pred_key in gold_set\n\n                if is_fallback:\n                    fb_total += 1\n                    if r.get(\"head\", \"\") in gold_heads:\n                        fb_head_in_gold += 1\n                    if r.get(\"tail\", \"\") in gold_tails:\n                        fb_tail_in_gold += 1\n                    pair_key = (r.get(\"head\", \"\"), r.get(\"tail\", \"\"))\n                    if pair_key in gold_pair_rels:\n                        fb_pair_in_gold += 1\n                        if rel_name.lower().strip() not in gold_pair_rels[pair_key]:\n                            fb_pair_in_gold_wrong_rel += 1\n                    if matched:\n                        fb_tp += 1\n                        fb_matched_doc.add(pred_key)\n                    else:\n                        fb_fp += 1\n                else:\n                    if matched:\n                        nfb_tp += 1\n                        nfb_matched_doc.add(pred_key)\n                    else:\n                        nfb_fp += 1\n\n            gold_matched_by_fb += len(fb_matched_doc)\n            gold_matched_by_nfb += len(nfb_matched_doc)\n\n    total_tp = fb_tp + nfb_tp\n    total_fp = fb_fp + nfb_fp\n    total_fn = total_gold - (gold_matched_by_fb + gold_matched_by_nfb)\n    p_all, r_all, f1_all = prf(total_tp, total_fp, total_fn)\n\n    p_fb = round(fb_tp / max(fb_tp + fb_fp, 1), 4)\n    p_nfb = round(nfb_tp / max(nfb_tp + nfb_fp, 1), 4)\n\n    return {\n        \"fallback_triples\": {\n            \"count\": fb_tp + fb_fp,\n            \"tp\": fb_tp, \"fp\": fb_fp,\n            \"precision\": p_fb,\n            \"recall_contribution\": round(gold_matched_by_fb / max(total_gold, 1), 4),\n        },\n        \"non_fallback_triples\": {\n            \"count\": nfb_tp + nfb_fp,\n            \"tp\": nfb_tp, \"fp\": nfb_fp,\n            \"precision\": p_nfb,\n            \"recall_contribution\": round(gold_matched_by_nfb / max(total_gold, 1), 4),\n        },\n        \"overall\": {\n            \"count\": fb_tp + fb_fp + nfb_tp + nfb_fp,\n            \"precision\": p_all, \"recall\": r_all, \"f1\": f1_all,\n            \"total_gold\": total_gold,\n        },\n        \"delta_precision\": round(p_fb - p_nfb, 4),\n        \"diagnostics\": {\n            \"fb_total\": fb_total,\n            \"fb_head_in_gold_entities\": fb_head_in_gold,\n            \"fb_tail_in_gold_entities\": fb_tail_in_gold,\n            \"fb_entity_pair_in_gold\": fb_pair_in_gold,\n            \"fb_entity_pair_in_gold_wrong_rel\": fb_pair_in_gold_wrong_rel,\n            \"fb_head_rate\": round(fb_head_in_gold / max(fb_total, 1), 4),\n            \"fb_tail_rate\": round(fb_tail_in_gold / max(fb_total, 1), 4),\n            \"fb_pair_rate\": round(fb_pair_in_gold / max(fb_total, 1), 4),\n        },\n    }\n\n\ndef analyze_scierc(output_path, constraints_path):\n    with open(constraints_path) as f:\n        C = json.load(f)\n\n    valid_entity_types = C[\"entity_types\"]\n    relation_types = C[\"relation_types\"]\n    rel_constraints = C.get(\"relation_constraints\", {})\n\n    canon_map = {}\n    for rt in relation_types:\n        k = rt.lower().replace(\"-\", \"\").replace(\" \", \"\").replace(\"_\", \"\")\n        canon_map[k] = rt\n\n    valid_pairs = {}\n    for rname, info in rel_constraints.items():\n        valid_pairs[rname] = set(tuple(p) for p in info[\"valid_pairs\"])\n\n    fb_tp = fb_fp = nfb_tp = nfb_fp = 0\n    total_gold = 0\n    gold_matched_by_fb = gold_matched_by_nfb = 0\n\n    fb_head_in_gold = fb_tail_in_gold = fb_pair_in_gold = fb_pair_in_gold_wrong_rel = 0\n    fb_total = 0\n\n    with open(output_path) as f:\n        for line in f:\n            doc = json.loads(line)\n            parsed = doc.get(\"parsed_output\") or {}\n            pred_rels = parsed.get(\"relations\", []) if parsed else []\n            gold_rels = doc.get(\"gold_relations\", [])\n\n            gold_set = set()\n            for r in gold_rels:\n                gold_set.add((r[\"head\"], r[\"tail\"], r[\"type\"].lower().strip()))\n            total_gold += len(gold_set)\n\n            gold_heads = set(r[\"head\"] for r in gold_rels)\n            gold_tails = set(r[\"tail\"] for r in gold_rels)\n            gold_pair_rels = defaultdict(set)\n            for r in gold_rels:\n                gold_pair_rels[(r[\"head\"], r[\"tail\"])].add(r[\"type\"].lower().strip())\n\n            fb_matched_doc = set()\n            nfb_matched_doc = set()\n\n            for r in pred_rels:\n                rel_name = r.get(\"type\", \"\")\n                ht = normalize_scierc_type(r.get(\"head_type\", \"\"), valid_entity_types)\n                tt = normalize_scierc_type(r.get(\"tail_type\", \"\"), valid_entity_types)\n                pred_key = (r.get(\"head\", \"\"), r.get(\"tail\", \"\"), rel_name.lower().strip())\n\n                rel_key = rel_name.lower().replace(\"-\", \"\").replace(\" \", \"\").replace(\"_\", \"\")\n                canon = canon_map.get(rel_key)\n\n                is_fallback = False\n                if ht is not None and tt is not None and canon and canon in valid_pairs:\n                    if (ht, tt) not in valid_pairs[canon]:\n                        is_fallback = True\n\n                matched = pred_key in gold_set\n\n                if is_fallback:\n                    fb_total += 1\n                    if r.get(\"head\", \"\") in gold_heads:\n                        fb_head_in_gold += 1\n                    if r.get(\"tail\", \"\") in gold_tails:\n                        fb_tail_in_gold += 1\n                    pair_key = (r.get(\"head\", \"\"), r.get(\"tail\", \"\"))\n                    if pair_key in gold_pair_rels:\n                        fb_pair_in_gold += 1\n                        if rel_name.lower().strip() not in gold_pair_rels[pair_key]:\n                            fb_pair_in_gold_wrong_rel += 1\n                    if matched:\n                        fb_tp += 1\n                        fb_matched_doc.add(pred_key)\n                    else:\n                        fb_fp += 1\n                else:\n                    if matched:\n                        nfb_tp += 1\n                        nfb_matched_doc.add(pred_key)\n                    else:\n                        nfb_fp += 1\n\n            gold_matched_by_fb += len(fb_matched_doc)\n            gold_matched_by_nfb += len(nfb_matched_doc)\n\n    total_tp = fb_tp + nfb_tp\n    total_fp = fb_fp + nfb_fp\n    total_fn = total_gold - (gold_matched_by_fb + gold_matched_by_nfb)\n    p_all, r_all, f1_all = prf(total_tp, total_fp, total_fn)\n\n    p_fb = round(fb_tp / max(fb_tp + fb_fp, 1), 4)\n    p_nfb = round(nfb_tp / max(nfb_tp + nfb_fp, 1), 4)\n\n    return {\n        \"fallback_triples\": {\n            \"count\": fb_tp + fb_fp,\n            \"tp\": fb_tp, \"fp\": fb_fp,\n            \"precision\": p_fb,\n            \"recall_contribution\": round(gold_matched_by_fb / max(total_gold, 1), 4),\n        },\n        \"non_fallback_triples\": {\n            \"count\": nfb_tp + nfb_fp,\n            \"tp\": nfb_tp, \"fp\": nfb_fp,\n            \"precision\": p_nfb,\n            \"recall_contribution\": round(gold_matched_by_nfb / max(total_gold, 1), 4),\n        },\n        \"overall\": {\n            \"count\": fb_tp + fb_fp + nfb_tp + nfb_fp,\n            \"precision\": p_all, \"recall\": r_all, \"f1\": f1_all,\n            \"total_gold\": total_gold,\n        },\n        \"delta_precision\": round(p_fb - p_nfb, 4),\n        \"diagnostics\": {\n            \"fb_total\": fb_total,\n            \"fb_head_in_gold_entities\": fb_head_in_gold,\n            \"fb_tail_in_gold_entities\": fb_tail_in_gold,\n            \"fb_entity_pair_in_gold\": fb_pair_in_gold,\n            \"fb_entity_pair_in_gold_wrong_rel\": fb_pair_in_gold_wrong_rel,\n            \"fb_head_rate\": round(fb_head_in_gold / max(fb_total, 1), 4),\n            \"fb_tail_rate\": round(fb_tail_in_gold / max(fb_total, 1), 4),\n            \"fb_pair_rate\": round(fb_pair_in_gold / max(fb_total, 1), 4),\n        },\n    }\n\n\nif __name__ == \"__main__\":\n    base = Path(\"/root/schema_semantic_constrained_ie\")\n    out_dir = Path(\"/root/autodl-tmp/schema_outputs\")\n    out_dir.mkdir(parents=True, exist_ok=True)\n\n    results = {}\n\n    # DocRED\n    print(\"=== DocRED Qwen ZS (full_s1) ===\")\n    results[\"docred_qwen_zs\"] = analyze_docred(\n        base / \"outputs/docred_full_s1.jsonl\",\n        base / \"data/docred/ontology_constraints_docred.json\",\n    )\n    d = results[\"docred_qwen_zs\"]\n    fb, nfb, ov, diag = d[\"fallback_triples\"], d[\"non_fallback_triples\"], d[\"overall\"], d[\"diagnostics\"]\n    print(f\"  Fallback:     n={fb['count']:>5}, P={fb['precision']:.4f}, recall_contrib={fb['recall_contribution']:.4f}\")\n    print(f\"  Non-fallback: n={nfb['count']:>5}, P={nfb['precision']:.4f}, recall_contrib={nfb['recall_contribution']:.4f}\")\n    print(f\"  Overall: P={ov['precision']:.4f}, R={ov['recall']:.4f}, F1={ov['f1']:.4f}\")\n    print(f\"  Delta P: {d['delta_precision']:+.4f}\")\n    print(f\"  Diagnostics: head_in_gold={diag['fb_head_rate']:.1%}, tail_in_gold={diag['fb_tail_rate']:.1%}, \"\n          f\"pair_in_gold={diag['fb_pair_rate']:.1%} ({diag['fb_entity_pair_in_gold']}/{diag['fb_total']}), \"\n          f\"all {diag['fb_entity_pair_in_gold_wrong_rel']} with wrong relation\")\n\n    # SciERC\n    print(\"\\n=== SciERC Qwen ZS (full_s1) ===\")\n    results[\"scierc_qwen_zs\"] = analyze_scierc(\n        base / \"outputs/phase2_scierc_full_s1_v2.jsonl\",\n        base / \"ontology_constraints.json\",\n    )\n    s = results[\"scierc_qwen_zs\"]\n    fb, nfb, ov, diag = s[\"fallback_triples\"], s[\"non_fallback_triples\"], s[\"overall\"], s[\"diagnostics\"]\n    print(f\"  Fallback:     n={fb['count']:>5}, P={fb['precision']:.4f}, recall_contrib={fb['recall_contribution']:.4f}\")\n    print(f\"  Non-fallback: n={nfb['count']:>5}, P={nfb['precision']:.4f}, recall_contrib={nfb['recall_contribution']:.4f}\")\n    print(f\"  Overall: P={ov['precision']:.4f}, R={ov['recall']:.4f}, F1={ov['f1']:.4f}\")\n    print(f\"  Delta P: {s['delta_precision']:+.4f}\")\n    print(f\"  Diagnostics: head_in_gold={diag['fb_head_rate']:.1%}, tail_in_gold={diag['fb_tail_rate']:.1%}, \"\n          f\"pair_in_gold={diag['fb_pair_rate']:.1%} ({diag['fb_entity_pair_in_gold']}/{diag['fb_total']}), \"\n          f\"all {diag['fb_entity_pair_in_gold_wrong_rel']} with wrong relation\")\n\n    # Save JSON\n    json_path = out_dir / \"r12_fallback_precision_recall.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(results, f, indent=2, ensure_ascii=False)\n    print(f\"\\nJSON saved to {json_path}\")\n\n    # Text summary\n    d_res = results[\"docred_qwen_zs\"]\n    s_res = results[\"scierc_qwen_zs\"]\n    d_fb = d_res[\"fallback_triples\"]\n    d_nfb = d_res[\"non_fallback_triples\"]\n    d_diag = d_res[\"diagnostics\"]\n\n    text = f\"\"\"Fallback Precision/Recall Analysis (Qwen ZS, S1 constrained)\n{'='*60}\n\nDocRED (n_fb={d_fb['count']}, n_nfb={d_nfb['count']}):\n  Fallback P={d_fb['precision']:.4f}, Non-fallback P={d_nfb['precision']:.4f}, Delta={d_res['delta_precision']:+.4f}\n  Fallback recall contribution: {d_fb['recall_contribution']:.4f} vs non-fallback: {d_nfb['recall_contribution']:.4f}\n  Diagnostic: {d_diag['fb_pair_rate']:.1%} of fallback triples have entity pair in gold, but all with wrong relation\n\nSciERC (n_fb={s_res['fallback_triples']['count']}, n_nfb={s_res['non_fallback_triples']['count']}):\n  Fallback P={s_res['fallback_triples']['precision']:.4f}, Non-fallback P={s_res['non_fallback_triples']['precision']:.4f}, Delta={s_res['delta_precision']:+.4f}\n  Fallback recall contribution: {s_res['fallback_triples']['recall_contribution']:.4f} vs non-fallback: {s_res['non_fallback_triples']['recall_contribution']:.4f}\n\n{'='*60}\nKey finding: Fallback triples (type-pair constraint violations) achieve 0% precision on both\ndatasets — they contribute zero correct extractions. On DocRED (1770 fallback triples, 10.2%\nof total), only 3.7% even have entity pairs matching gold, and all 65 of those assign the\nwrong relation. This confirms that type-pair violations are a reliable indicator of extraction\nfailure: the S1 semantic layer's fallback mechanism masks errors that would otherwise produce\ncompletely spurious triples. Removing or correcting fallback triples would eliminate ~10%\nof false positives on DocRED with no recall loss.\"\"\"\n\n    text_path = out_dir / \"r12_fallback_pr_text.txt\"\n    with open(text_path, \"w\") as f:\n        f.write(text)\n    print(f\"Text saved to {text_path}\")\nPYEOF\necho \"Script updated.\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-16980",
    "command": "cat > /root/schema_semantic_constrained_ie/scripts/analyze_fallback_precision_recall.py << 'PYEOF'\n\"\"\"Fallback triples precision/recall analysis with diagnostics.\"\"\"\nimport json\nfrom collections import defaultdict\nfrom pathlib import Path\n\nDOCRED_TYPE_ALIASES = {\n    'PERSON': 'PER', 'PEOPLE': 'PER',\n    'ORGANIZATION': 'ORG', 'ORGANISATION': 'ORG',\n    'LOCATION': 'LOC', 'NUMBER': 'NUM', 'NUMERICAL': 'NUM',\n    'MISCELLANEOUS': 'MISC',\n}\n\nSCIERC_TYPE_MAP = {\n    \"otherscientificterm\": \"OtherScientificTerm\",\n    \"other-scientificterm\": \"OtherScientificTerm\",\n    \"other_scientific_term\": \"OtherScientificTerm\",\n    \"scientificterm\": \"OtherScientificTerm\",\n    \"other\": \"OtherScientificTerm\",\n}\n\n\ndef normalize_docred_type(raw):\n    t = raw.strip().upper()\n    return DOCRED_TYPE_ALIASES.get(t, t)\n\n\ndef normalize_scierc_type(raw, valid_types):\n    t_lower = raw.strip().lower().replace(\" \", \"\").replace(\"_\", \"\").replace(\"-\", \"\")\n    for vt in valid_types:\n        if t_lower == vt.lower().replace(\" \", \"\").replace(\"_\", \"\").replace(\"-\", \"\"):\n            return vt\n    return SCIERC_TYPE_MAP.get(t_lower, None)\n\n\ndef prf(tp, fp, fn):\n    p = tp / (tp + fp) if (tp + fp) > 0 else 0.0\n    r = tp / (tp + fn) if (tp + fn) > 0 else 0.0\n    f1 = 2 * p * r / (p + r) if (p + r) > 0 else 0.0\n    return round(p, 4), round(r, 4), round(f1, 4)\n\n\ndef analyze_docred(output_path, constraints_path):\n    with open(constraints_path) as f:\n        C = json.load(f)\n\n    rel_types = C[\"relation_types\"]\n    rel_constraints = C[\"relation_constraints\"]\n\n    name_to_pid = {}\n    for pid, name in rel_types.items():\n        name_to_pid[name.lower().strip()] = pid\n        name_to_pid[pid.lower()] = pid\n\n    pcode_to_name_lower = {pid: name.lower().strip() for pid, name in rel_types.items()}\n\n    valid_pairs = {}\n    for pid, info in rel_constraints.items():\n        valid_pairs[pid] = set(tuple(p) for p in info[\"valid_pairs\"])\n\n    fb_tp = fb_fp = nfb_tp = nfb_fp = 0\n    total_gold = 0\n    gold_matched_by_fb = gold_matched_by_nfb = 0\n\n    # Diagnostics for fallback triples\n    fb_head_in_gold = 0\n    fb_tail_in_gold = 0\n    fb_pair_in_gold = 0\n    fb_pair_in_gold_wrong_rel = 0\n    fb_total = 0\n\n    with open(output_path) as f:\n        for line in f:\n            doc = json.loads(line)\n            parsed = doc.get(\"parsed_output\") or {}\n            pred_rels = parsed.get(\"relations\", []) if parsed else []\n            gold_rels = doc.get(\"gold_relations\", [])\n\n            gold_set = set()\n            for r in gold_rels:\n                rtype_name = pcode_to_name_lower.get(r[\"type\"], r[\"type\"].lower().strip())\n                gold_set.add((r[\"head\"], r[\"tail\"], rtype_name))\n            total_gold += len(gold_set)\n\n            gold_heads = set(r[\"head\"] for r in gold_rels)\n            gold_tails = set(r[\"tail\"] for r in gold_rels)\n            gold_pair_rels = defaultdict(set)\n            for r in gold_rels:\n                gold_pair_rels[(r[\"head\"], r[\"tail\"])].add(\n                    pcode_to_name_lower.get(r[\"type\"], r[\"type\"].lower().strip()))\n\n            fb_matched_doc = set()\n            nfb_matched_doc = set()\n\n            for r in pred_rels:\n                rel_name = r.get(\"type\", \"\")\n                ht = normalize_docred_type(r.get(\"head_type\", \"\"))\n                tt = normalize_docred_type(r.get(\"tail_type\", \"\"))\n                pid = name_to_pid.get(rel_name.lower().strip())\n                pred_key = (r.get(\"head\", \"\"), r.get(\"tail\", \"\"), rel_name.lower().strip())\n\n                is_fallback = False\n                if pid and pid in valid_pairs:\n                    if (ht, tt) not in valid_pairs[pid]:\n                        is_fallback = True\n\n                matched = pred_key in gold_set\n\n                if is_fallback:\n                    fb_total += 1\n                    if r.get(\"head\", \"\") in gold_heads:\n                        fb_head_in_gold += 1\n                    if r.get(\"tail\", \"\") in gold_tails:\n                        fb_tail_in_gold += 1\n                    pair_key = (r.get(\"head\", \"\"), r.get(\"tail\", \"\"))\n                    if pair_key in gold_pair_rels:\n                        fb_pair_in_gold += 1\n                        if rel_name.lower().strip() not in gold_pair_rels[pair_key]:\n                            fb_pair_in_gold_wrong_rel += 1\n                    if matched:\n                        fb_tp += 1\n                        fb_matched_doc.add(pred_key)\n                    else:\n                        fb_fp += 1\n                else:\n                    if matched:\n                        nfb_tp += 1\n                        nfb_matched_doc.add(pred_key)\n                    else:\n                        nfb_fp += 1\n\n            gold_matched_by_fb += len(fb_matched_doc)\n            gold_matched_by_nfb += len(nfb_matched_doc)\n\n    total_tp = fb_tp + nfb_tp\n    total_fp = fb_fp + nfb_fp\n    total_fn = total_gold - (gold_matched_by_fb + gold_matched_by_nfb)\n    p_all, r_all, f1_all = prf(total_tp, total_fp, total_fn)\n\n    p_fb = round(fb_tp / max(fb_tp + fb_fp, 1), 4)\n    p_nfb = round(nfb_tp / max(nfb_tp + nfb_fp, 1), 4)\n\n    return {\n        \"fallback_triples\": {\n            \"count\": fb_tp + fb_fp,\n            \"tp\": fb_tp, \"fp\": fb_fp,\n            \"precision\": p_fb,\n            \"recall_contribution\": round(gold_matched_by_fb / max(total_gold, 1), 4),\n        },\n        \"non_fallback_triples\": {\n            \"count\": nfb_tp + nfb_fp,\n            \"tp\": nfb_tp, \"fp\": nfb_fp,\n            \"precision\": p_nfb,\n            \"recall_contribution\": round(gold_matched_by_nfb / max(total_gold, 1), 4),\n        },\n        \"overall\": {\n            \"count\": fb_tp + fb_fp + nfb_tp + nfb_fp,\n            \"precision\": p_all, \"recall\": r_all, \"f1\": f1_all,\n            \"total_gold\": total_gold,\n        },\n        \"delta_precision\": round(p_fb - p_nfb, 4),\n        \"diagnostics\": {\n            \"fb_total\": fb_total,\n            \"fb_head_in_gold_entities\": fb_head_in_gold,\n            \"fb_tail_in_gold_entities\": fb_tail_in_gold,\n            \"fb_entity_pair_in_gold\": fb_pair_in_gold,\n            \"fb_entity_pair_in_gold_wrong_rel\": fb_pair_in_gold_wrong_rel,\n            \"fb_head_rate\": round(fb_head_in_gold / max(fb_total, 1), 4),\n            \"fb_tail_rate\": round(fb_tail_in_gold / max(fb_total, 1), 4),\n            \"fb_pair_rate\": round(fb_pair_in_gold / max(fb_total, 1), 4),\n        },\n    }\n\n\ndef analyze_scierc(output_path, constraints_path):\n    with open(constraints_path) as f:\n        C = json.load(f)\n\n    valid_entity_types = C[\"entity_types\"]\n    relation_types = C[\"relation_types\"]\n    rel_constraints = C.get(\"relation_constraints\", {})\n\n    canon_map = {}\n    for rt in relation_types:\n        k = rt.lower().replace(\"-\", \"\").replace(\" \", \"\").replace(\"_\", \"\")\n        canon_map[k] = rt\n\n    valid_pairs = {}\n    for rname, info in rel_constraints.items():\n        valid_pairs[rname] = set(tuple(p) for p in info[\"valid_pairs\"])\n\n    fb_tp = fb_fp = nfb_tp = nfb_fp = 0\n    total_gold = 0\n    gold_matched_by_fb = gold_matched_by_nfb = 0\n\n    fb_head_in_gold = fb_tail_in_gold = fb_pair_in_gold = fb_pair_in_gold_wrong_rel = 0\n    fb_total = 0\n\n    with open(output_path) as f:\n        for line in f:\n            doc = json.loads(line)\n            parsed = doc.get(\"parsed_output\") or {}\n            pred_rels = parsed.get(\"relations\", []) if parsed else []\n            gold_rels = doc.get(\"gold_relations\", [])\n\n            gold_set = set()\n            for r in gold_rels:\n                gold_set.add((r[\"head\"], r[\"tail\"], r[\"type\"].lower().strip()))\n            total_gold += len(gold_set)\n\n            gold_heads = set(r[\"head\"] for r in gold_rels)\n            gold_tails = set(r[\"tail\"] for r in gold_rels)\n            gold_pair_rels = defaultdict(set)\n            for r in gold_rels:\n                gold_pair_rels[(r[\"head\"], r[\"tail\"])].add(r[\"type\"].lower().strip())\n\n            fb_matched_doc = set()\n            nfb_matched_doc = set()\n\n            for r in pred_rels:\n                rel_name = r.get(\"type\", \"\")\n                ht = normalize_scierc_type(r.get(\"head_type\", \"\"), valid_entity_types)\n                tt = normalize_scierc_type(r.get(\"tail_type\", \"\"), valid_entity_types)\n                pred_key = (r.get(\"head\", \"\"), r.get(\"tail\", \"\"), rel_name.lower().strip())\n\n                rel_key = rel_name.lower().replace(\"-\", \"\").replace(\" \", \"\").replace(\"_\", \"\")\n                canon = canon_map.get(rel_key)\n\n                is_fallback = False\n                if ht is not None and tt is not None and canon and canon in valid_pairs:\n                    if (ht, tt) not in valid_pairs[canon]:\n                        is_fallback = True\n\n                matched = pred_key in gold_set\n\n                if is_fallback:\n                    fb_total += 1\n                    if r.get(\"head\", \"\") in gold_heads:\n                        fb_head_in_gold += 1\n                    if r.get(\"tail\", \"\") in gold_tails:\n                        fb_tail_in_gold += 1\n                    pair_key = (r.get(\"head\", \"\"), r.get(\"tail\", \"\"))\n                    if pair_key in gold_pair_rels:\n                        fb_pair_in_gold += 1\n                        if rel_name.lower().strip() not in gold_pair_rels[pair_key]:\n                            fb_pair_in_gold_wrong_rel += 1\n                    if matched:\n                        fb_tp += 1\n                        fb_matched_doc.add(pred_key)\n                    else:\n                        fb_fp += 1\n                else:\n                    if matched:\n                        nfb_tp += 1\n                        nfb_matched_doc.add(pred_key)\n                    else:\n                        nfb_fp += 1\n\n            gold_matched_by_fb += len(fb_matched_doc)\n            gold_matched_by_nfb += len(nfb_matched_doc)\n\n    total_tp = fb_tp + nfb_tp\n    total_fp = fb_fp + nfb_fp\n    total_fn = total_gold - (gold_matched_by_fb + gold_matched_by_nfb)\n    p_all, r_all, f1_all = prf(total_tp, total_fp, total_fn)\n\n    p_fb = round(fb_tp / max(fb_tp + fb_fp, 1), 4)\n    p_nfb = round(nfb_tp / max(nfb_tp + nfb_fp, 1), 4)\n\n    return {\n        \"fallback_triples\": {\n            \"count\": fb_tp + fb_fp,\n            \"tp\": fb_tp, \"fp\": fb_fp,\n            \"precision\": p_fb,\n            \"recall_contribution\": round(gold_matched_by_fb / max(total_gold, 1), 4),\n        },\n        \"non_fallback_triples\": {\n            \"count\": nfb_tp + nfb_fp,\n            \"tp\": nfb_tp, \"fp\": nfb_fp,\n            \"precision\": p_nfb,\n            \"recall_contribution\": round(gold_matched_by_nfb / max(total_gold, 1), 4),\n        },\n        \"overall\": {\n            \"count\": fb_tp + fb_fp + nfb_tp + nfb_fp,\n            \"precision\": p_all, \"recall\": r_all, \"f1\": f1_all,\n            \"total_gold\": total_gold,\n        },\n        \"delta_precision\": round(p_fb - p_nfb, 4),\n        \"diagnostics\": {\n            \"fb_total\": fb_total,\n            \"fb_head_in_gold_entities\": fb_head_in_gold,\n            \"fb_tail_in_gold_entities\": fb_tail_in_gold,\n            \"fb_entity_pair_in_gold\": fb_pair_in_gold,\n            \"fb_entity_pair_in_gold_wrong_rel\": fb_pair_in_gold_wrong_rel,\n            \"fb_head_rate\": round(fb_head_in_gold / max(fb_total, 1), 4),\n            \"fb_tail_rate\": round(fb_tail_in_gold / max(fb_total, 1), 4),\n            \"fb_pair_rate\": round(fb_pair_in_gold / max(fb_total, 1), 4),\n        },\n    }\n\n\nif __name__ == \"__main__\":\n    base = Path(\"/root/schema_semantic_constrained_ie\")\n    out_dir = Path(\"/root/autodl-tmp/schema_outputs\")\n    out_dir.mkdir(parents=True, exist_ok=True)\n\n    results = {}\n\n    # DocRED\n    print(\"=== DocRED Qwen ZS (full_s1) ===\")\n    results[\"docred_qwen_zs\"] = analyze_docred(\n        base / \"outputs/docred_full_s1.jsonl\",\n        base / \"data/docred/ontology_constraints_docred.json\",\n    )\n    d = results[\"docred_qwen_zs\"]\n    fb, nfb, ov, diag = d[\"fallback_triples\"], d[\"non_fallback_triples\"], d[\"overall\"], d[\"diagnostics\"]\n    print(f\"  Fallback:     n={fb['count']:>5}, P={fb['precision']:.4f}, recall_contrib={fb['recall_contribution']:.4f}\")\n    print(f\"  Non-fallback: n={nfb['count']:>5}, P={nfb['precision']:.4f}, recall_contrib={nfb['recall_contribution']:.4f}\")\n    print(f\"  Overall: P={ov['precision']:.4f}, R={ov['recall']:.4f}, F1={ov['f1']:.4f}\")\n    print(f\"  Delta P: {d['delta_precision']:+.4f}\")\n    print(f\"  Diagnostics: head_in_gold={diag['fb_head_rate']:.1%}, tail_in_gold={diag['fb_tail_rate']:.1%}, \"\n          f\"pair_in_gold={diag['fb_pair_rate']:.1%} ({diag['fb_entity_pair_in_gold']}/{diag['fb_total']}), \"\n          f\"all {diag['fb_entity_pair_in_gold_wrong_rel']} with wrong relation\")\n\n    # SciERC\n    print(\"\\n=== SciERC Qwen ZS (full_s1) ===\")\n    results[\"scierc_qwen_zs\"] = analyze_scierc(\n        base / \"outputs/phase2_scierc_full_s1_v2.jsonl\",\n        base / \"ontology_constraints.json\",\n    )\n    s = results[\"scierc_qwen_zs\"]\n    fb, nfb, ov, diag = s[\"fallback_triples\"], s[\"non_fallback_triples\"], s[\"overall\"], s[\"diagnostics\"]\n    print(f\"  Fallback:     n={fb['count']:>5}, P={fb['precision']:.4f}, recall_contrib={fb['recall_contribution']:.4f}\")\n    print(f\"  Non-fallback: n={nfb['count']:>5}, P={nfb['precision']:.4f}, recall_contrib={nfb['recall_contribution']:.4f}\")\n    print(f\"  Overall: P={ov['precision']:.4f}, R={ov['recall']:.4f}, F1={ov['f1']:.4f}\")\n    print(f\"  Delta P: {s['delta_precision']:+.4f}\")\n    print(f\"  Diagnostics: head_in_gold={diag['fb_head_rate']:.1%}, tail_in_gold={diag['fb_tail_rate']:.1%}, \"\n          f\"pair_in_gold={diag['fb_pair_rate']:.1%} ({diag['fb_entity_pair_in_gold']}/{diag['fb_total']}), \"\n          f\"all {diag['fb_entity_pair_in_gold_wrong_rel']} with wrong relation\")\n\n    # Save JSON\n    json_path = out_dir / \"r12_fallback_precision_recall.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(results, f, indent=2, ensure_ascii=False)\n    print(f\"\\nJSON saved to {json_path}\")\n\n    # Text summary\n    d_res = results[\"docred_qwen_zs\"]\n    s_res = results[\"scierc_qwen_zs\"]\n    d_fb = d_res[\"fallback_triples\"]\n    d_nfb = d_res[\"non_fallback_triples\"]\n    d_diag = d_res[\"diagnostics\"]\n\n    text = f\"\"\"Fallback Precision/Recall Analysis (Qwen ZS, S1 constrained)\n{'='*60}\n\nDocRED (n_fb={d_fb['count']}, n_nfb={d_nfb['count']}):\n  Fallback P={d_fb['precision']:.4f}, Non-fallback P={d_nfb['precision']:.4f}, Delta={d_res['delta_precision']:+.4f}\n  Fallback recall contribution: {d_fb['recall_contribution']:.4f} vs non-fallback: {d_nfb['recall_contribution']:.4f}\n  Diagnostic: {d_diag['fb_pair_rate']:.1%} of fallback triples have entity pair in gold, but all with wrong relation\n\nSciERC (n_fb={s_res['fallback_triples']['count']}, n_nfb={s_res['non_fallback_triples']['count']}):\n  Fallback P={s_res['fallback_triples']['precision']:.4f}, Non-fallback P={s_res['non_fallback_triples']['precision']:.4f}, Delta={s_res['delta_precision']:+.4f}\n  Fallback recall contribution: {s_res['fallback_triples']['recall_contribution']:.4f} vs non-fallback: {s_res['non_fallback_triples']['recall_contribution']:.4f}\n\n{'='*60}\nKey finding: Fallback triples (type-pair constraint violations) achieve 0% precision on both\ndatasets — they contribute zero correct extractions. On DocRED (1770 fallback triples, 10.2%\nof total), only 3.7% even have entity pairs matching gold, and all 65 of those assign the\nwrong relation. This confirms that type-pair violations are a reliable indicator of extraction\nfailure: the S1 semantic layer's fallback mechanism masks errors that would otherwise produce\ncompletely spurious triples. Removing or correcting fallback triples would eliminate ~10%\nof false positives on DocRED with no recall loss.\"\"\"\n\n    text_path = out_dir / \"r12_fallback_pr_text.txt\"\n    with open(text_path, \"w\") as f:\n        f.write(text)\n    print(f\"Text saved to {text_path}\")\nPYEOF\necho \"Script updated.\""
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-20T18:10:42.482615+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script updated.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-20T18:10:42.482844+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-16980",
  "command": "cd /root/schema_semantic_constrained_ie && python3 scripts/analyze_fallback_precision_recall.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-16980",
    "command": "cd /root/schema_semantic_constrained_ie && python3 scripts/analyze_fallback_precision_recall.py"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-20T18:10:42.483008+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== DocRED Qwen ZS (full_s1) ===\\n  Fallback:     n= 1770, P=0.0000, recall_contrib=0.0000\\n  Non-fallback: n=15571, P=0.0781, recall_contrib=0.0987\\n  Overall: P=0.0701, R=0.0998, F1=0.0824\\n  Delta P: -0.0781\\n  Diagnostics: head_in_gold=54.8%, tail_in_gold=13.4%, pair_in_gold=3.7% (65/1770), all 65 with wrong relation\\n\\n=== SciERC Qwen ZS (full_s1) ===\\n  Fallback:     n=   16, P=0.0000, recall_contrib=0.0000\\n  Non-fallback: n= 1713, P=0.0660, recall_contrib=0.1160\\n  Overall: P=0.0654, R=0.1160, F1=0.0836\\n  Delta P: -0.0660\\n  Diagnostics: head_in_gold=6.2%, tail_in_gold=0.0%, pair_in_gold=0.0% (0/16), all 0 with wrong relation\\n\\nJSON saved to /root/autodl-tmp/schema_outputs/r12_fallback_precision_recall.json\\nText saved to /root/autodl-tmp/schema_outputs/r12_fallback_pr_text.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-20T18:10:42.483174+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "cat /root/autodl-tmp/schema_outputs/r12_fallback_pr_text.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "cat /root/autodl-tmp/schema_outputs/r12_fallback_pr_text.txt"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-20T18:10:42.483336+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Fallback Precision/Recall Analysis (Qwen ZS, S1 constrained)\\n============================================================\\n\\nDocRED (n_fb=1770, n_nfb=15571):\\n  Fallback P=0.0000, Non-fallback P=0.0781, Delta=-0.0781\\n  Fallback recall contribution: 0.0000 vs non-fallback: 0.0987\\n  Diagnostic: 3.7% of fallback triples have entity pair in gold, but all with wrong relation\\n\\nSciERC (n_fb=16, n_nfb=1713):\\n  Fallback P=0.0000, Non-fallback P=0.0660, Delta=-0.0660\\n  Fallback recall contribution: 0.0000 vs non-fallback: 0.1160\\n\\n============================================================\\nKey finding: Fallback triples (type-pair constraint violations) achieve 0% precision on both\\ndatasets — they contribute zero correct extractions. On DocRED (1770 fallback triples, 10.2%\\nof total), only 3.7% even have entity pairs matching gold, and all 65 of those assign the\\nwrong relation. This confirms that type-pair violations are a reliable indicator of extraction\\nfailure: the S1 semantic layer's fallback mechanism masks errors that would otherwise produce\\ncompletely spurious triples. Removing or correcting fallback triples would eliminate ~10%\\nof false positives on DocRED with no recall loss.\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-20T18:10:42.483602+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "cat /root/autodl-tmp/schema_outputs/r12_fallback_precision_recall.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "cat /root/autodl-tmp/schema_outputs/r12_fallback_precision_recall.json"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-20T18:10:42.483852+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"docred_qwen_zs\\\": {\\n    \\\"fallback_triples\\\": {\\n      \\\"count\\\": 1770,\\n      \\\"tp\\\": 0,\\n      \\\"fp\\\": 1770,\\n      \\\"precision\\\": 0.0,\\n      \\\"recall_contribution\\\": 0.0\\n    },\\n    \\\"non_fallback_triples\\\": {\\n      \\\"count\\\": 15571,\\n      \\\"tp\\\": 1216,\\n      \\\"fp\\\": 14355,\\n      \\\"precision\\\": 0.0781,\\n      \\\"recall_contribution\\\": 0.0987\\n    },\\n    \\\"overall\\\": {\\n      \\\"count\\\": 17341,\\n      \\\"precision\\\": 0.0701,\\n      \\\"recall\\\": 0.0998,\\n      \\\"f1\\\": 0.0824,\\n      \\\"total_gold\\\": 12164\\n    },\\n    \\\"delta_precision\\\": -0.0781,\\n    \\\"diagnostics\\\": {\\n      \\\"fb_total\\\": 1770,\\n      \\\"fb_head_in_gold_entities\\\": 969,\\n      \\\"fb_tail_in_gold_entities\\\": 237,\\n      \\\"fb_entity_pair_in_gold\\\": 65,\\n      \\\"fb_entity_pair_in_gold_wrong_rel\\\": 65,\\n      \\\"fb_head_rate\\\": 0.5475,\\n      \\\"fb_tail_rate\\\": 0.1339,\\n      \\\"fb_pair_rate\\\": 0.0367\\n    }\\n  },\\n  \\\"scierc_qwen_zs\\\": {\\n    \\\"fallback_triples\\\": {\\n      \\\"count\\\": 16,\\n      \\\"tp\\\": 0,\\n      \\\"fp\\\": 16,\\n      \\\"precision\\\": 0.0,\\n      \\\"recall_contribution\\\": 0.0\\n    },\\n    \\\"non_fallback_triples\\\": {\\n      \\\"count\\\": 1713,\\n      \\\"tp\\\": 113,\\n      \\\"fp\\\": 1600,\\n      \\\"precision\\\": 0.066,\\n      \\\"recall_contribution\\\": 0.116\\n    },\\n    \\\"overall\\\": {\\n      \\\"count\\\": 1729,\\n      \\\"precision\\\": 0.0654,\\n      \\\"recall\\\": 0.116,\\n      \\\"f1\\\": 0.0836,\\n      \\\"total_gold\\\": 974\\n    },\\n    \\\"delta_precision\\\": -0.066,\\n    \\\"diagnostics\\\": {\\n      \\\"fb_total\\\": 16,\\n      \\\"fb_head_in_gold_entities\\\": 1,\\n      \\\"fb_tail_in_gold_entities\\\": 0,\\n      \\\"fb_entity_pair_in_gold\\\": 0,\\n      \\\"fb_entity_pair_in_gold_wrong_rel\\\": 0
…[truncated 230 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-20T18:10:42.484048+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "r12_fallback_precision_recall",
  "type": "data",
  "description": "Fallback vs non-fallback triples precision/recall analysis for Qwen ZS S1 on DocRED and SciERC. Shows fallback triples achieve 0% precision (all 1770 DocRED fallback triples are FP).",
  "project": "schema_semantic_constrained_ie",
  "source_path": "/root/autodl-tmp/schema_outputs/r12_fallback_precision_recall.json",
  "tags": "['fallback', 'precision-recall', 'r12', 'analysis']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "r12_fallback_precision_recall",
    "type": "data",
    "description": "Fallback vs non-fallback triples precision/recall analysis for Qwen ZS S1 on DocRED and SciERC. Shows fallback triples achieve 0% precision (all 1770 DocRED fallback triples are FP).",
    "project": "schema_semantic_constrained_ie",
    "source_path": "/root/autodl-tmp/schema_outputs/r12_fallback_precision_recall.json",
    "tags": "['fallback', 'precision-recall', 'r12', 'analysis']"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-20T18:10:42.484427+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"source_path not found: /root/autodl-tmp/schema_outputs/r12_fallback_precision_recall.json\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-20T18:10:42.484601+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "r12_fallback_precision_recall",
  "type": "data",
  "description": "Fallback vs non-fallback triples precision/recall analysis for Qwen ZS S1 on DocRED and SciERC. Shows fallback triples achieve 0% precision (all 1770 DocRED fallback triples are FP).",
  "project": "schema_semantic_constrained_ie",
  "content": "{\n  \"docred_qwen_zs\": {\n    \"fallback_triples\": {\"count\": 1770, \"tp\": 0, \"fp\": 1770, \"precision\": 0.0, \"recall_contribution\": 0.0},\n    \"non_fallback_triples\": {\"count\": 15571, \"tp\": 1216, \"fp\": 14355, \"precision\": 0.0781, \"recall_contribution\": 0.0987},\n    \"overall\": {\"count\": 17341, \"precision\": 0.0701, \"recall\": 0.0998, \"f1\": 0.0824, \"total_gold\": 12164},\n    \"delta_precision\": -0.0781,\n    \"diagnostics\": {\"fb_total\": 1770, \"fb_head_in_gold_entities\": 969, \"fb_tail_in_gold_entities\": 237, \"fb_entity_pair_in_gold\": 65, \"fb_entity_pair_in_gold_wrong_rel\": 65, \"fb_head_rate\": 0.5475, \"fb_tail_rate\": 0.1339, \"fb_pair_rate\": 0.0367}\n  },\n  \"scierc_qwen_zs\": {\n    \"fallback_triples\": {\"count\": 16, \"tp\": 0, \"fp\": 16, \"precision\": 0.0, \"recall_contribution\": 0.0},\n    \"non_fallback_triples\": {\"count\": 1713, \"tp\": 113, \"fp\": 1600, \"precision\": 0.066, \"recall_contribution\": 0.116},\n    \"overall\": {\"count\": 1729, \"precision\": 0.0654, \"recall\": 0.116, \"f1\": 0.0836, \"total_gold\": 974},\n    \"delta_precision\": -0.066,\n    \"diagnostics\": {\"fb_total\": 16, \"fb_head_in_gold_entities\": 1, \"fb_tail_in_gold_entities\": 0, \"fb_entity_pair_in_gold\": 0, \"fb_entity_pair_in_gold_wrong_rel\": 0, \"fb_head_rate\": 0.0625, \"fb_tail_rate\": 0.0, \"fb_pair_rate\": 0.0}\n  }\n}",
  "content_filename": "r12_fallback_precision_recall.json",
  "tags": "['fallback', 'precision-recall', 'r12', 'analysis']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "r12_fallback_precision_recall",
    "type": "data",
    "description": "Fallback vs non-fallback triples precision/recall analysis for Qwen ZS S1 on DocRED and SciERC. Shows fallback triples achieve 0% precision (all 1770 DocRED fallback triples are FP).",
    "project": "schema_semantic_constrained_ie",
    "content": "{\n  \"docred_qwen_zs\": {\n    \"fallback_triples\": {\"count\": 1770, \"tp\": 0, \"fp\": 1770, \"precision\": 0.0, \"recall_contribution\": 0.0},\n    \"non_fallback_triples\": {\"count\": 15571, \"tp\": 1216, \"fp\": 14355, \"precision\": 0.0781, \"recall_contribution\": 0.0987},\n    \"overall\": {\"count\": 17341, \"precision\": 0.0701, \"recall\": 0.0998, \"f1\": 0.0824, \"total_gold\": 12164},\n    \"delta_precision\": -0.0781,\n    \"diagnostics\": {\"fb_total\": 1770, \"fb_head_in_gold_entities\": 969, \"fb_tail_in_gold_entities\": 237, \"fb_entity_pair_in_gold\": 65, \"fb_entity_pair_in_gold_wrong_rel\": 65, \"fb_head_rate\": 0.5475, \"fb_tail_rate\": 0.1339, \"fb_pair_rate\": 0.0367}\n  },\n  \"scierc_qwen_zs\": {\n    \"fallback_triples\": {\"count\": 16, \"tp\": 0, \"fp\": 16, \"precision\": 0.0, \"recall_contribution\": 0.0},\n    \"non_fallback_triples\": {\"count\": 1713, \"tp\": 113, \"fp\": 1600, \"precision\": 0.066, \"recall_contribution\": 0.116},\n    \"overall\": {\"count\": 1729, \"precision\": 0.0654, \"recall\": 0.116, \"f1\": 0.0836, \"total_gold\": 974},\n    \"delta_precision\": -0.066,\n    \"diagnostics\": {\"fb_total\": 16, \"fb_head_in_gold_entities\": 1, \"fb_tail_in_gold_entities\": 0, \"fb_entity_pair_in_gold\": 0, \"fb_entity_pair_in_gold_wrong_rel\": 0, \"fb_head_rate\": 0.0625, \"fb_tail_rate\": 0.0, \"fb_pair_rate\": 0.0}\n  }\n}",
    "content_filename": "r12_fallback_precision_recall.json",
    "tags": "['fallback', 'precision-recall', 'r12', 'analysis']"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-20T18:10:42.484784+00:00_

Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'docred_qwen_zs': {'fall..., 'fb_pair_rate': 0.0}}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-20T18:10:42.484928+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "r12_fallback_precision_recall",
  "type": "data",
  "description": "Fallback vs non-fallback triples precision/recall analysis for Qwen ZS S1 on DocRED and SciERC. Shows fallback triples achieve 0% precision (all 1770 DocRED fallback triples are FP).",
  "project": "schema_semantic_constrained_ie",
  "content": "{\"docred_qwen_zs\":{\"fallback_triples\":{\"count\":1770,\"tp\":0,\"fp\":1770,\"precision\":0.0,\"recall_contribution\":0.0},\"non_fallback_triples\":{\"count\":15571,\"tp\":1216,\"fp\":14355,\"precision\":0.0781,\"recall_contribution\":0.0987},\"overall\":{\"count\":17341,\"precision\":0.0701,\"recall\":0.0998,\"f1\":0.0824,\"total_gold\":12164},\"delta_precision\":-0.0781,\"diagnostics\":{\"fb_total\":1770,\"fb_head_in_gold_entities\":969,\"fb_tail_in_gold_entities\":237,\"fb_entity_pair_in_gold\":65,\"fb_entity_pair_in_gold_wrong_rel\":65}},\"scierc_qwen_zs\":{\"fallback_triples\":{\"count\":16,\"tp\":0,\"fp\":16,\"precision\":0.0,\"recall_contribution\":0.0},\"non_fallback_triples\":{\"count\":1713,\"tp\":113,\"fp\":1600,\"precision\":0.066,\"recall_contribution\":0.116},\"overall\":{\"count\":1729,\"precision\":0.0654,\"recall\":0.116,\"f1\":0.0836,\"total_gold\":974},\"delta_precision\":-0.066}}",
  "content_filename": "r12_fallback_precision_recall.json",
  "tags": "['fallback', 'precision-recall', 'r12', 'analysis']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "r12_fallback_precision_recall",
    "type": "data",
    "description": "Fallback vs non-fallback triples precision/recall analysis for Qwen ZS S1 on DocRED and SciERC. Shows fallback triples achieve 0% precision (all 1770 DocRED fallback triples are FP).",
    "project": "schema_semantic_constrained_ie",
    "content": "{\"docred_qwen_zs\":{\"fallback_triples\":{\"count\":1770,\"tp\":0,\"fp\":1770,\"precision\":0.0,\"recall_contribution\":0.0},\"non_fallback_triples\":{\"count\":15571,\"tp\":1216,\"fp\":14355,\"precision\":0.0781,\"recall_contribution\":0.0987},\"overall\":{\"count\":17341,\"precision\":0.0701,\"recall\":0.0998,\"f1\":0.0824,\"total_gold\":12164},\"delta_precision\":-0.0781,\"diagnostics\":{\"fb_total\":1770,\"fb_head_in_gold_entities\":969,\"fb_tail_in_gold_entities\":237,\"fb_entity_pair_in_gold\":65,\"fb_entity_pair_in_gold_wrong_rel\":65}},\"scierc_qwen_zs\":{\"fallback_triples\":{\"count\":16,\"tp\":0,\"fp\":16,\"precision\":0.0,\"recall_contribution\":0.0},\"non_fallback_triples\":{\"count\":1713,\"tp\":113,\"fp\":1600,\"precision\":0.066,\"recall_contribution\":0.116},\"overall\":{\"count\":1729,\"precision\":0.0654,\"recall\":0.116,\"f1\":0.0836,\"total_gold\":974},\"delta_precision\":-0.066}}",
    "content_filename": "r12_fallback_precision_recall.json",
    "tags": "['fallback', 'precision-recall', 'r12', 'analysis']"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-20T18:10:42.485172+00:00_

Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'docred_qwen_zs': {'fall...lta_precision': -0.066}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-20T18:10:42.485426+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "r12_fallback_precision_recall",
  "type": "data",
  "description": "Fallback vs non-fallback triples precision/recall analysis for Qwen ZS S1 on DocRED and SciERC. Fallback triples achieve 0% precision on both datasets.",
  "project": "schema_semantic_constrained_ie",
  "url": "westd-16980:/root/autodl-tmp/schema_outputs/r12_fallback_precision_recall.json",
  "tags": "['fallback', 'precision-recall', 'r12', 'analysis']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "r12_fallback_precision_recall",
    "type": "data",
    "description": "Fallback vs non-fallback triples precision/recall analysis for Qwen ZS S1 on DocRED and SciERC. Fallback triples achieve 0% precision on both datasets.",
    "project": "schema_semantic_constrained_ie",
    "url": "westd-16980:/root/autodl-tmp/schema_outputs/r12_fallback_precision_recall.json",
    "tags": "['fallback', 'precision-recall', 'r12', 'analysis']"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-20T18:10:42.485635+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260520_925821\", \"name\": \"r12_fallback_precision_recall\", \"type\": \"data\", \"description\": \"Fallback vs non-fallback triples precision/recall analysis for Qwen ZS S1 on DocRED and SciERC. Fallback triples achieve 0% precision on both datasets.\", \"path\": null, \"url\": \"westd-16980:/root/autodl-tmp/schema_outputs/r12_fallback_precision_recall.json\", \"project\": \"schema_semantic_constrained_ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-20T18:10:30.913402+00:00\", \"tags\": [\"fallback\", \"precision-recall\", \"r12\", \"analysis\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 63 · 2026-05-20T18:10:42.485862+00:00_

分析完成。结果：

**DocRED** (1770 fallback / 15571 non-fallback triples):
| | Count | Precision | Recall Contrib |
|---|---|---|---|
| Fallback | 1,770 | **0.00%** | 0.00% |
| Non-fallback | 15,571 | **7.81%** | 9.87% |
| Delta P | | **-7.81pp** | |

**SciERC** (16 fallback / 1713 non-fallback triples):
| | Count | Precision | Recall Contrib |
|---|---|---|---|
| Fallback | 16 | **0.00%** | 0.00% |
| Non-fallback | 1,713 | **6.60%** | 11.60% |

**诊断细节** (DocRED 1770 fallback triples):
- 54.8% head 文本出现在 gold entities 中
- 13.4% tail 文本出现在 gold entities 中
- 仅 3.7% (65/1770) entity pair 匹配 gold，但这 65 个全部关系名错误

**核心结论**：Fallback triples（type-pair 约束违反）precision 为 0%，recall 贡献也为 0%。它们是纯噪声。在 DocRED 上，移除 fallback triples 可以消除 ~10% 的 false positives 且不损失任何 recall。Type-pair 约束违反是提取失败的可靠指标。

输出文件：
- JSON: `westd-16980:/root/autodl-tmp/schema_outputs/r12_fallback_precision_recall.json`
- 文本: `westd-16980:/root/autodl-tmp/schema_outputs/r12_fallback_pr_text.txt`
- 脚本: `westd-16980:/root/schema_semantic_constrained_ie/scripts/analyze_fallback_precision_recall.py`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440"
}
```

</details>

---
