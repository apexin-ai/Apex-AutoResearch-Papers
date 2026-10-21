# analysis c0 domain split

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_analysis_c0-domain-split_20260517T172311.jsonl`
- **Structured JSON:** [`88617459607f54b81387.json`](../../sessions/88/88617459607f54b81387.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-17T17:24:42.892307+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_c0-domain-split_20260517T172311",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T17:24:42.892654+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_c0-domain-split_20260517T172311",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T17:24:42.892836+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "ls /root/symb_invariant_consensus/results/ | head -30",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_c0-domain-split_20260517T172311",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "ls /root/symb_invariant_consensus/results/ | head -30",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T17:24:42.893019+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"aime30_t07.json\\naime30_v2.json\\naime30_v2_partial_backup.json\\naime30_v2_rescore_analysis.json\\nanalysis_expanded.json\\nc0_precheck_qwen14b.json\\ncompute_quality_metrics.py\\nconstraint_ablation.json\\nconstraint_cache\\nconstraint_cache_consolidated.json\\nconstraint_quality_correlation\\nd016_smoke_test.json\\ndiversity_diagnosis.json\\nexp001_analysis.md\\nexp004_qwen7b\\nexp009_overhead\\nexp010_mistral\\nexp011_llama8b\\nexp012_gsm8k\\nexp014_deepseek_r1_7b\\nexp015_logic_lm\\nexp017_strategyqa\\nexp018_arc\\nexp019_constraint_quality_analysis.json\\nexp019_constraint_quality_summary.csv\\nexp019_strategyqa_200\\nexp020_folio_200\\nexp021_oracle_folio\\nfolio_livetest.json\\nk_ablation\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.6}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_c0-domain-split_20260517T172311",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T17:24:42.893156+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "ls /root/symb_invariant_consensus/results/ | grep -i \"sica_expanded\\|full_mvp\\|exp001\\|expanded_14b\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_c0-domain-split_20260517T172311",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "ls /root/symb_invariant_consensus/results/ | grep -i \"sica_expanded\\|full_mvp\\|exp001\\|expanded_14b\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T17:24:42.893284+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"exp001_analysis.md\\nsica_expanded_14b.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.76}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_c0-domain-split_20260517T172311",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T17:24:42.893409+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "python3 -c \"\nimport json\nwith open('/root/symb_invariant_consensus/results/sica_expanded_14b.json') as f:\n    data = json.load(f)\n# Check structure\nif isinstance(data, list):\n    print(f'List of {len(data)} items')\n    print('Keys in first item:', list(data[0].keys()) if data else 'empty')\n    # Check for dataset field\n    if data:\n        print('Sample item:', json.dumps(data[0], indent=2)[:1000])\nelif isinstance(data, dict):\n    print('Dict with keys:', list(data.keys())[:20])\n    # Check nested structure\n    for k in list(data.keys())[:3]:\n        v = data[k]\n        if isinstance(v, dict):\n            print(f'  {k} keys:', list(v.keys())[:10])\n        else:\n            print(f'  {k}: {type(v).__name__} = {str(v)[:200]}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_c0-domain-split_20260517T172311",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "python3 -c \"\nimport json\nwith open('/root/symb_invariant_consensus/results/sica_expanded_14b.json') as f:\n    data = json.load(f)\n# Check structure\nif isinstance(data, list):\n    print(f'List of {len(data)} items')\n    print('Keys in first item:', list(data[0].keys()) if data else 'empty')\n    # Check for dataset field\n    if data:\n        print('Sample item:', json.dumps(data[0], indent=2)[:1000])\nelif isinstance(data, dict):\n    print('Dict with keys:', list(data.keys())[:20])\n    # Check nested structure\n    for k in list(data.keys())[:3]:\n        v = data[k]\n        if isinstance(v, dict):\n            print(f'  {k} keys:', list(v.keys())[:10])\n        else:\n            print(f'  {k}: {type(v).__name__} = {str(v)[:200]}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T17:24:42.893553+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'python3 -c \\\"\\\\nimport json\\\\nwith open(\\\\'/root/symb_invariant_consensus/results/sica_expanded_14b.json\\\\') as f:\\\\n    data = json.load(f)\\\\n# Check structure\\\\nif isinstance(data, list):\\\\n    print(f\\\\'List of {len(data)} items\\\\')\\\\n    print(\\\\'Keys in first item:\\\\', list(data[0].keys()) if data else \\\\'empty\\\\')\\\\n    # Check for dataset field\\\\n    if data:\\\\n        print(\\\\'Sample item:\\\\', json.dumps(data[0], indent=2)[:1000])\\\\nelif isinstance(data, dict):\\\\n    print(\\\\'Dict with keys:\\\\', list(data.keys())[:20])\\\\n    # Check nested structure\\\\n    for k in list(data.keys())[:3]:\\\\n        v = data[k]\\\\n        if isinstance(v, dict):\\\\n            print(f\\\\'  {k} keys:\\\\', list(v.keys())[:10])\\\\n        else:\\\\n            print(f\\\\'  {k}: {type(v).__name__} = {str(v)[:200]}\\\\')\\\\n\\\"\\\\n'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.78}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_c0-domain-split_20260517T172311",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T17:24:42.893696+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "source /root/miniconda3/bin/activate && python3 -c \"\nimport json\nwith open('/root/symb_invariant_consensus/results/sica_expanded_14b.json') as f:\n    data = json.load(f)\nif isinstance(data, list):\n    print(f'List of {len(data)} items')\n    print('Keys in first item:', list(data[0].keys()) if data else 'empty')\n    if data:\n        print('Sample item:', json.dumps(data[0], indent=2)[:1500])\nelif isinstance(data, dict):\n    print('Dict with keys:', list(data.keys())[:20])\n    for k in list(data.keys())[:3]:\n        v = data[k]\n        if isinstance(v, dict):\n            print(f'  {k} keys:', list(v.keys())[:10])\n        else:\n            print(f'  {k}: {type(v).__name__} = {str(v)[:200]}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_c0-domain-split_20260517T172311",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "source /root/miniconda3/bin/activate && python3 -c \"\nimport json\nwith open('/root/symb_invariant_consensus/results/sica_expanded_14b.json') as f:\n    data = json.load(f)\nif isinstance(data, list):\n    print(f'List of {len(data)} items')\n    print('Keys in first item:', list(data[0].keys()) if data else 'empty')\n    if data:\n        print('Sample item:', json.dumps(data[0], indent=2)[:1500])\nelif isinstance(data, dict):\n    print('Dict with keys:', list(data.keys())[:20])\n    for k in list(data.keys())[:3]:\n        v = data[k]\n        if isinstance(v, dict):\n            print(f'  {k} keys:', list(v.keys())[:10])\n        else:\n            print(f'  {k}: {type(v).__name__} = {str(v)[:200]}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T17:24:42.893831+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Dict with keys: ['summary', 'results']\\n  summary keys: ['n_problems', 'sica_accuracy', 'sc_accuracy', 'sica_correct', 'sc_correct', 'extraction_rate', 'answer_extraction_rate', 'answer_extraction_counts', 'truncated_traces', 'total_constraints_extracted']\\n  results: list = [{'problem_idx': 0, 'problem_id': 'ProofWriter_AttNoneg-OWA-D5-1041_Q1', 'problem': 'Given the following facts and rules:\\\\nBob is cold. Bob is quiet. Bob is red. Bob is smart. Charlie is kind. Charlie\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_c0-domain-split_20260517T172311",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T17:24:42.893980+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "source /root/miniconda3/bin/activate && python3 -c \"\nimport json\nwith open('/root/symb_invariant_consensus/results/sica_expanded_14b.json') as f:\n    data = json.load(f)\n\n# Check summary\nprint('Summary:', json.dumps(data['summary'], indent=2))\nprint()\n\n# Check first result item keys\nr0 = data['results'][0]\nprint('Result item keys:', list(r0.keys()))\nprint()\nprint('Sample problem_id:', r0['problem_id'])\nprint('Sample votes:', r0.get('votes', 'N/A'))\nprint('Sample gold:', r0.get('gold_answer', r0.get('gold', 'N/A')))\nprint('Sample sc_answer:', r0.get('sc_answer', 'N/A'))\nprint('Sample sica_answer:', r0.get('sica_answer', 'N/A'))\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_c0-domain-split_20260517T172311",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "source /root/miniconda3/bin/activate && python3 -c \"\nimport json\nwith open('/root/symb_invariant_consensus/results/sica_expanded_14b.json') as f:\n    data = json.load(f)\n\n# Check summary\nprint('Summary:', json.dumps(data['summary'], indent=2))\nprint()\n\n# Check first result item keys\nr0 = data['results'][0]\nprint('Result item keys:', list(r0.keys()))\nprint()\nprint('Sample problem_id:', r0['problem_id'])\nprint('Sample votes:', r0.get('votes', 'N/A'))\nprint('Sample gold:', r0.get('gold_answer', r0.get('gold', 'N/A')))\nprint('Sample sc_answer:', r0.get('sc_answer', 'N/A'))\nprint('Sample sica_answer:', r0.get('sica_answer', 'N/A'))\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T17:24:42.894147+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Summary: {\\n  \\\"n_problems\\\": 804,\\n  \\\"sica_accuracy\\\": 0.7649253731343284,\\n  \\\"sc_accuracy\\\": 0.7624378109452736,\\n  \\\"sica_correct\\\": 615,\\n  \\\"sc_correct\\\": 613,\\n  \\\"extraction_rate\\\": 0.8904436152570481,\\n  \\\"answer_extraction_rate\\\": 1.0,\\n  \\\"answer_extraction_counts\\\": {\\n    \\\"boxed\\\": 9648,\\n    \\\"fallback\\\": 0,\\n    \\\"none\\\": 0\\n  },\\n  \\\"truncated_traces\\\": 0,\\n  \\\"total_constraints_extracted\\\": 88428,\\n  \\\"total_unique_constraints\\\": 17273,\\n  \\\"contradiction_rate\\\": 0.022347015573438316,\\n  \\\"problems_with_contradictions\\\": 331,\\n  \\\"per_level_accuracy\\\": {\\n    \\\"D5\\\": {\\n      \\\"sica\\\": 0.755,\\n      \\\"sc\\\": 0.7516666666666667,\\n      \\\"n\\\": 600\\n    },\\n    \\\"folio\\\": {\\n      \\\"sica\\\": 0.7941176470588235,\\n      \\\"sc\\\": 0.7941176470588235,\\n      \\\"n\\\": 204\\n    }\\n  },\\n  \\\"per_dataset_accuracy\\\": {\\n    \\\"proofwriter\\\": {\\n      \\\"sica\\\": 0.755,\\n      \\\"sc\\\": 0.7516666666666667,\\n      \\\"n\\\": 600\\n    },\\n    \\\"folio\\\": {\\n      \\\"sica\\\": 0.7941176470588235,\\n      \\\"sc\\\": 0.7941176470588235,\\n      \\\"n\\\": 204\\n    }\\n  },\\n  \\\"k\\\": 12,\\n  \\\"mode\\\": \\\"vllm\\\",\\n  \\\"total_wall_time_s\\\": 49558.9\\n}\\n\\nResult item keys: ['problem_idx', 'problem_id', 'problem', 'dataset', 'level', 'ground_truth', 'sica_answer', 'sica_scores', 'sica_correct', 'sc_answer', 'sc_vote_count', 'sc_vote_distribution', 'sc_correct', 'constraints_stats', 'maxsat_stats', 'timing', 'wall_time_s', 'trace_extraction_stats', 'truncated_traces', 'raw_constraints', 'per_trace']\\n\\nSample problem_id: ProofWriter_AttNoneg-OWA-D5-1041_Q1\\nSample votes: N/A\\nSample gold: N/A\\nSample sc_answer: True\\nSample sica_answer: True\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_c0-domain-split_20260517T172311",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T17:24:42.894306+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "source /root/miniconda3/bin/activate && python3 -c \"\nimport json\nwith open('/root/symb_invariant_consensus/results/sica_expanded_14b.json') as f:\n    data = json.load(f)\n\nr0 = data['results'][0]\nprint('sc_vote_distribution:', r0['sc_vote_distribution'])\nprint('sc_vote_count:', r0['sc_vote_count'])\nprint('dataset:', r0['dataset'])\nprint('ground_truth:', r0['ground_truth'])\n\n# Check a few more\nfor i in [0, 1, 100, 600, 700]:\n    r = data['results'][i]\n    print(f'  [{i}] dataset={r[\\\"dataset\\\"]}, sc_vote_dist={r[\\\"sc_vote_distribution\\\"]}, n_unique={len(r[\\\"sc_vote_distribution\\\"])}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_c0-domain-split_20260517T172311",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "source /root/miniconda3/bin/activate && python3 -c \"\nimport json\nwith open('/root/symb_invariant_consensus/results/sica_expanded_14b.json') as f:\n    data = json.load(f)\n\nr0 = data['results'][0]\nprint('sc_vote_distribution:', r0['sc_vote_distribution'])\nprint('sc_vote_count:', r0['sc_vote_count'])\nprint('dataset:', r0['dataset'])\nprint('ground_truth:', r0['ground_truth'])\n\n# Check a few more\nfor i in [0, 1, 100, 600, 700]:\n    r = data['results'][i]\n    print(f'  [{i}] dataset={r[\\\"dataset\\\"]}, sc_vote_dist={r[\\\"sc_vote_distribution\\\"]}, n_unique={len(r[\\\"sc_vote_distribution\\\"])}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T17:24:42.894691+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"sc_vote_distribution: {'True': 12}\\nsc_vote_count: 12\\ndataset: proofwriter\\nground_truth: True\\n  [0] dataset=proofwriter, sc_vote_dist={'True': 12}, n_unique=1\\n  [1] dataset=proofwriter, sc_vote_dist={'Unknown': 9, 'True': 3}, n_unique=2\\n  [100] dataset=proofwriter, sc_vote_dist={'Unknown': 9, 'True': 3}, n_unique=2\\n  [600] dataset=folio, sc_vote_dist={'True': 3, 'Unknown': 8, 'False': 1}, n_unique=3\\n  [700] dataset=folio, sc_vote_dist={'True': 12}, n_unique=1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.6}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_c0-domain-split_20260517T172311",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T17:24:42.895182+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "source /root/miniconda3/bin/activate && python3 << 'EOF'\nimport json, os\n\nwith open('/root/symb_invariant_consensus/results/sica_expanded_14b.json') as f:\n    data = json.load(f)\n\nresults = data['results']\n\n# Split by dataset\nfolio = [r for r in results if r['dataset'] == 'folio']\npw = [r for r in results if r['dataset'] == 'proofwriter']\n\ndef compute_metrics(subset):\n    n = len(subset)\n    c0_count = sum(1 for r in subset if len(r['sc_vote_distribution']) > 1)\n    sc_correct = sum(1 for r in subset if r['sc_correct'])\n    sica_correct = sum(1 for r in subset if r['sica_correct'])\n    return {\n        \"n\": n,\n        \"c0\": round(c0_count / n, 4),\n        \"c0_count\": c0_count,\n        \"sc_acc\": round(sc_correct / n, 4),\n        \"sc_correct\": sc_correct,\n        \"sica_acc\": round(sica_correct / n, 4),\n        \"sica_correct\": sica_correct\n    }\n\nfolio_m = compute_metrics(folio)\npw_m = compute_metrics(pw)\ncombined_m = compute_metrics(results)\n\noutput = {\n    \"experiment\": \"exp-001 (sica_expanded_14b)\",\n    \"model\": \"Qwen2.5-14B-Instruct\",\n    \"k\": 12,\n    \"folio\": folio_m,\n    \"proofwriter\": pw_m,\n    \"combined\": combined_m\n}\n\n# Write to analysis dir\nos.makedirs('/root/symb_invariant_consensus/analysis', exist_ok=True)\nwith open('/root/symb_invariant_consensus/analysis/c0_domain_split.json', 'w') as f:\n    json.dump(output, f, indent=2)\n\n# Print summary\nprint(\"=\" * 50)\nprint(\"exp-001 C0 Domain Split Analysis\")\nprint(\"=\" * 50)\nprint(f\"{'Domain':<14} {'n':>4} {'C0':>8} {'SC Acc':>8} {'SICA Acc':>9}\")\nprint(\"-\" * 50)\nprint(f\"{'FOLIO':<14} {folio_m['n']:>4} {folio_m['c0']:>7.1%} {folio_m['sc_acc']:>7.1%} {folio_m['sica_acc']:>8.1%}\")\nprint(f\"{'ProofWriter':<14} {pw_m['n']:>4} {pw_m['c0']:>7.1%} {pw_m['sc_acc']:>7.1%} {pw_m['sica_acc']:>8.1%}\")\nprint(f\"{'Combined':<14} {combined_m['n']:>4} {combined_m['c0']:>7.1%} {combined_m['sc_acc']:>7.1%} {combined_m['sica_acc']:>8.1%}\")\nprint(\"-\" * 50)\nprint(f\"\\nVerification vs registry:\")\nprint(f\"  Combined C0:  {combined_m['c0']:.3f} (expected ~0.382)\")\nprint(f\"  Combined SC:  {combined_m['sc_acc']:.3f} (expected ~0.762)\")\nprint(f\"  Combined SICA:{combined_m['sica_acc']:.3f} (expected ~0.765)\")\nprint(f\"\\nWritten to: /root/symb_invariant_consensus/analysis/c0_domain_split.json\")\nEOF\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_c0-domain-split_20260517T172311",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "source /root/miniconda3/bin/activate && python3 << 'EOF'\nimport json, os\n\nwith open('/root/symb_invariant_consensus/results/sica_expanded_14b.json') as f:\n    data = json.load(f)\n\nresults = data['results']\n\n# Split by dataset\nfolio = [r for r in results if r['dataset'] == 'folio']\npw = [r for r in results if r['dataset'] == 'proofwriter']\n\ndef compute_metrics(subset):\n    n = len(subset)\n    c0_count = sum(1 for r in subset if len(r['sc_vote_distribution']) > 1)\n    sc_correct = sum(1 for r in subset if r['sc_correct'])\n    sica_correct = sum(1 for r in subset if r['sica_correct'])\n    return {\n        \"n\": n,\n        \"c0\": round(c0_count / n, 4),\n        \"c0_count\": c0_count,\n        \"sc_acc\": round(sc_correct / n, 4),\n        \"sc_correct\": sc_correct,\n        \"sica_acc\": round(sica_correct / n, 4),\n        \"sica_correct\": sica_correct\n    }\n\nfolio_m = compute_metrics(folio)\npw_m = compute_metrics(pw)\ncombined_m = compute_metrics(results)\n\noutput = {\n    \"experiment\": \"exp-001 (sica_expanded_14b)\",\n    \"model\": \"Qwen2.5-14B-Instruct\",\n    \"k\": 12,\n    \"folio\": folio_m,\n    \"proofwriter\": pw_m,\n    \"combined\": combined_m\n}\n\n# Write to analysis dir\nos.makedirs('/root/symb_invariant_consensus/analysis', exist_ok=True)\nwith open('/root/symb_invariant_consensus/analysis/c0_domain_split.json', 'w') as f:\n    json.dump(output, f, indent=2)\n\n# Print summary\nprint(\"=\" * 50)\nprint(\"exp-001 C0 Domain Split Analysis\")\nprint(\"=\" * 50)\nprint(f\"{'Domain':<14} {'n':>4} {'C0':>8} {'SC Acc':>8} {'SICA Acc':>9}\")\nprint(\"-\" * 50)\nprint(f\"{'FOLIO':<14} {folio_m['n']:>4} {folio_m['c0']:>7.1%} {folio_m['sc_acc']:>7.1%} {folio_m['sica_acc']:>8.1%}\")\nprint(f\"{'ProofWriter':<14} {pw_m['n']:>4} {pw_m['c0']:>7.1%} {pw_m['sc_acc']:>7.1%} {pw_m['sica_acc']:>8.1%}\")\nprint(f\"{'Combined':<14} {combined_m['n']:>4} {combined_m['c0']:>7.1%} {combined_m['sc_acc']:>7.1%} {combined_m['sica_acc']:>8.1%}\")\nprint(\"-\" * 50)\nprint(f\"\\nVerification vs registry:\")\nprint(f\"  Combined C0:  {combined_m['c0']:.3f} (expected ~0.382)\")\nprint(f\"  Combined SC:  {combined_m['sc_acc']:.3f} (expected ~0.762)\")\nprint(f\"  Combined SICA:{combined_m['sica_acc']:.3f} (expected ~0.765)\")\nprint(f\"\\nWritten to: /root/symb_invariant_consensus/analysis/c0_domain_split.json\")\nEOF\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T17:24:42.895438+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"==================================================\\nexp-001 C0 Domain Split Analysis\\n==================================================\\nDomain            n       C0   SC Acc  SICA Acc\\n--------------------------------------------------\\nFOLIO           204   35.3%   79.4%    79.4%\\nProofWriter     600   39.2%   75.2%    75.5%\\nCombined        804   38.2%   76.2%    76.5%\\n--------------------------------------------------\\n\\nVerification vs registry:\\n  Combined C0:  0.382 (expected ~0.382)\\n  Combined SC:  0.762 (expected ~0.762)\\n  Combined SICA:0.765 (expected ~0.765)\\n\\nWritten to: /root/symb_invariant_consensus/analysis/c0_domain_split.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.57}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_c0-domain-split_20260517T172311",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-17T17:24:42.895639+00:00_

完成。结果已写入 `analysis/c0_domain_split.json`。

**域内 C0 拆分：**

| Domain | n | C0 | SC Acc | SICA Acc |
|--------|---:|-----:|-------:|---------:|
| FOLIO | 204 | 35.3% | 79.4% | 79.4% |
| ProofWriter | 600 | 39.2% | 75.2% | 75.5% |
| Combined | 804 | 38.2% | 76.2% | 76.5% |

Combined 数字与 registry 完全一致。ProofWriter 的 C0 (39.2%) 高于 FOLIO (35.3%)，说明 PW 的 D5 难度下模型回答分歧更大。FOLIO 上 SC 和 SICA 表现相同（79.4%），SICA 的增益主要来自 ProofWriter（75.2% → 75.5%）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_c0-domain-split_20260517T172311"
}
```

</details>

---
