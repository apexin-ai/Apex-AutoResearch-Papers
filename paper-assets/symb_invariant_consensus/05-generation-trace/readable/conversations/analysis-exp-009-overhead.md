# analysis exp 009 overhead

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/chats/worker_analysis_exp-009-overhead_20260516T202925.jsonl`
- **Structured JSON:** [`a9531c1014f4070b9497.json`](../../sessions/a9/a9531c1014f4070b9497.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

31 recorded events

### Tool call

_source line 1 · 2026-05-16T20:32:08.804494+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-009-overhead_20260516T202925",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T20:32:08.804856+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-009-overhead_20260516T202925",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T20:32:08.805062+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "ls /root/symb_invariant_consensus/results/sica_expanded_14b/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-009-overhead_20260516T202925",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "ls /root/symb_invariant_consensus/results/sica_expanded_14b/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T20:32:08.805206+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/symb_invariant_consensus/results/sica_expanded_14b/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 1.28}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-009-overhead_20260516T202925",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T20:32:08.805332+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "ls /root/symb_invariant_consensus/results/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-009-overhead_20260516T202925",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "ls /root/symb_invariant_consensus/results/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T20:32:08.805465+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"aime30_t07.json\\naime30_v2.json\\naime30_v2_partial_backup.json\\naime30_v2_rescore_analysis.json\\nanalysis_expanded.json\\nc0_precheck_qwen14b.json\\nconstraint_ablation.json\\nconstraint_cache\\nconstraint_cache_consolidated.json\\nd016_smoke_test.json\\ndiversity_diagnosis.json\\nexp001_analysis.md\\nfolio_livetest.json\\nk_ablation\\nproofwriter_30_v2.json\\nproofwriter_5_l3l1_fix.json\\nqwq_operating_regime.json\\nqwq_operating_regime.md\\nrescore_pure_results.json\\nsica_d012_14b.json\\nsica_expanded_14b.json\\nsmoke_test_5q.json\\ntiebreak_analysis.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-009-overhead_20260516T202925",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T20:32:08.805618+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "head -100 /root/symb_invariant_consensus/results/sica_expanded_14b.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-009-overhead_20260516T202925",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "head -100 /root/symb_invariant_consensus/results/sica_expanded_14b.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T20:32:08.805812+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n_problems\\\": 804,\\n    \\\"sica_accuracy\\\": 0.7649253731343284,\\n    \\\"sc_accuracy\\\": 0.7624378109452736,\\n    \\\"sica_correct\\\": 615,\\n    \\\"sc_correct\\\": 613,\\n    \\\"extraction_rate\\\": 0.8904436152570481,\\n    \\\"answer_extraction_rate\\\": 1.0,\\n    \\\"answer_extraction_counts\\\": {\\n      \\\"boxed\\\": 9648,\\n      \\\"fallback\\\": 0,\\n      \\\"none\\\": 0\\n    },\\n    \\\"truncated_traces\\\": 0,\\n    \\\"total_constraints_extracted\\\": 88428,\\n    \\\"total_unique_constraints\\\": 17273,\\n    \\\"contradiction_rate\\\": 0.022347015573438316,\\n    \\\"problems_with_contradictions\\\": 331,\\n    \\\"per_level_accuracy\\\": {\\n      \\\"D5\\\": {\\n        \\\"sica\\\": 0.755,\\n        \\\"sc\\\": 0.7516666666666667,\\n        \\\"n\\\": 600\\n      },\\n      \\\"folio\\\": {\\n        \\\"sica\\\": 0.7941176470588235,\\n        \\\"sc\\\": 0.7941176470588235,\\n        \\\"n\\\": 204\\n      }\\n    },\\n    \\\"per_dataset_accuracy\\\": {\\n      \\\"proofwriter\\\": {\\n        \\\"sica\\\": 0.755,\\n        \\\"sc\\\": 0.7516666666666667,\\n        \\\"n\\\": 600\\n      },\\n      \\\"folio\\\": {\\n        \\\"sica\\\": 0.7941176470588235,\\n        \\\"sc\\\": 0.7941176470588235,\\n        \\\"n\\\": 204\\n      }\\n    },\\n    \\\"k\\\": 12,\\n    \\\"mode\\\": \\\"vllm\\\",\\n    \\\"total_wall_time_s\\\": 49558.9\\n  },\\n  \\\"results\\\": [\\n    {\\n      \\\"problem_idx\\\": 0,\\n      \\\"problem_id\\\": \\\"ProofWriter_AttNoneg-OWA-D5-1041_Q1\\\",\\n      \\\"problem\\\": \\\"Given the following facts and rules:\\\\nBob is cold. Bob is quiet. Bob is red. Bob is smart. Charlie is kind. Charlie is quiet. Charlie is red. Charlie is rough. Dave is cold. Dave is kind. Dave is smart. Fiona is quiet. If something is quiet and cold then it is smart. Red, cold things are round. If something is kind and rough then it is 
…[truncated 1960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-009-overhead_20260516T202925",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T20:32:08.806028+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "cd /root/symb_invariant_consensus && python3 -c \"\nimport json, numpy as np\n\nwith open('results/sica_expanded_14b.json') as f:\n    data = json.load(f)\n\nresults = data['results']\nn = len(results)\nprint(f'Total problems: {n}')\n\n# Extract timing data\ntrace_gen = []\nextraction = []\ndedup = []\nmaxsat = []\ntotal = []\nmissing = 0\n\nfor r in results:\n    t = r.get('timing')\n    if t:\n        trace_gen.append(t['trace_gen_s'])\n        extraction.append(t['extraction_s'])\n        dedup.append(t['dedup_s'])\n        maxsat.append(t['maxsat_s'])\n        total.append(t['total_s'])\n    else:\n        missing += 1\n\nprint(f'Problems with timing: {len(total)}, missing: {missing}')\nprint(f'Total wall time from summary: {data[\\\"summary\\\"][\\\"total_wall_time_s\\\"]:.1f}s = {data[\\\"summary\\\"][\\\"total_wall_time_s\\\"]/60:.1f}min')\nprint(f'Sum of per-problem total_s: {sum(total):.1f}s = {sum(total)/60:.1f}min')\nprint()\n\n# Per-stage stats\nfor name, arr in [('trace_gen', trace_gen), ('extraction', extraction), ('dedup', dedup), ('maxsat', maxsat), ('total', total)]:\n    a = np.array(arr)\n    print(f'{name:12s}: mean={a.mean():.2f}s, median={np.median(a):.2f}s, p95={np.percentile(a,95):.2f}s, sum={a.sum():.1f}s ({a.sum()/sum(total)*100:.1f}%)')\n\nprint()\n# SC baseline overhead = only trace_gen\nsc_time = sum(trace_gen)\nsica_overhead = sum(extraction) + sum(dedup) + sum(maxsat)\nprint(f'SC baseline time (trace_gen only): {sc_time:.1f}s = {sc_time/60:.1f}min')\nprint(f'SICA extra overhead (extraction+dedup+maxsat): {sica_overhead:.1f}s = {sica_overhead/60:.1f}min')\nprint(f'Overhead ratio: {sica_overhead/sc_time*100:.1f}% extra over SC')\nprint(f'Overhead per problem: {sica_overhead/len(total):.2f}s avg')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-009-overhead_20260516T202925",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "cd /root/symb_invariant_consensus && python3 -c \"\nimport json, numpy as np\n\nwith open('results/sica_expanded_14b.json') as f:\n    data = json.load(f)\n\nresults = data['results']\nn = len(results)\nprint(f'Total problems: {n}')\n\n# Extract timing data\ntrace_gen = []\nextraction = []\ndedup = []\nmaxsat = []\ntotal = []\nmissing = 0\n\nfor r in results:\n    t = r.get('timing')\n    if t:\n        trace_gen.append(t['trace_gen_s'])\n        extraction.append(t['extraction_s'])\n        dedup.append(t['dedup_s'])\n        maxsat.append(t['maxsat_s'])\n        total.append(t['total_s'])\n    else:\n        missing += 1\n\nprint(f'Problems with timing: {len(total)}, missing: {missing}')\nprint(f'Total wall time from summary: {data[\\\"summary\\\"][\\\"total_wall_time_s\\\"]:.1f}s = {data[\\\"summary\\\"][\\\"total_wall_time_s\\\"]/60:.1f}min')\nprint(f'Sum of per-problem total_s: {sum(total):.1f}s = {sum(total)/60:.1f}min')\nprint()\n\n# Per-stage stats\nfor name, arr in [('trace_gen', trace_gen), ('extraction', extraction), ('dedup', dedup), ('maxsat', maxsat), ('total', total)]:\n    a = np.array(arr)\n    print(f'{name:12s}: mean={a.mean():.2f}s, median={np.median(a):.2f}s, p95={np.percentile(a,95):.2f}s, sum={a.sum():.1f}s ({a.sum()/sum(total)*100:.1f}%)')\n\nprint()\n# SC baseline overhead = only trace_gen\nsc_time = sum(trace_gen)\nsica_overhead = sum(extraction) + sum(dedup) + sum(maxsat)\nprint(f'SC baseline time (trace_gen only): {sc_time:.1f}s = {sc_time/60:.1f}min')\nprint(f'SICA extra overhead (extraction+dedup+maxsat): {sica_overhead:.1f}s = {sica_overhead/60:.1f}min')\nprint(f'Overhead ratio: {sica_overhead/sc_time*100:.1f}% extra over SC')\nprint(f'Overhead per problem: {sica_overhead/len(total):.2f}s avg')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T20:32:08.806222+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/symb_invariant_consensus && python3 -c \\\"\\\\nimport json, numpy as np\\\\n\\\\nwith open(\\\\'results/sica_expanded_14b.json\\\\') as f:\\\\n    data = json.load(f)\\\\n\\\\nresults = data[\\\\'results\\\\']\\\\nn = len(results)\\\\nprint(f\\\\'Total problems: {n}\\\\')\\\\n\\\\n# Extract timing data\\\\ntrace_gen = []\\\\nextraction = []\\\\ndedup = []\\\\nmaxsat = []\\\\ntotal = []\\\\nmissing = 0\\\\n\\\\nfor r in results:\\\\n    t = r.get(\\\\'timing\\\\')\\\\n    if t:\\\\n        trace_gen.append(t[\\\\'trace_gen_s\\\\'])\\\\n        extraction.append(t[\\\\'extraction_s\\\\'])\\\\n        dedup.append(t[\\\\'dedup_s\\\\'])\\\\n        maxsat.append(t[\\\\'maxsat_s\\\\'])\\\\n        total.append(t[\\\\'total_s\\\\'])\\\\n    else:\\\\n        missing += 1\\\\n\\\\nprint(f\\\\'Problems with timing: {len(total)}, missing: {missing}\\\\')\\\\nprint(f\\\\'Total wall time from summary: {data[\\\\\\\\\\\"summary\\\\\\\\\\\"][\\\\\\\\\\\"total_wall_time_s\\\\\\\\\\\"]:.1f}s = {data[\\\\\\\\\\\"summary\\\\\\\\\\\"][\\\\\\\\\\\"total_wall_time_s\\\\\\\\\\\"]/60:.1f}min\\\\')\\\\nprint(f\\\\'Sum of per-problem total_s: {sum(total):.1f}s = {sum(total)/60:.1f}min\\\\')\\\\nprint()\\\\n\\\\n# Per-stage stats\\\\nfor name, arr in [(\\\\'trace_gen\\\\', trace_gen), (\\\\'extraction\\\\', extraction), (\\\\'dedup\\\\', dedup), (\\\\'maxsat\\\\', maxsat), (\\\\'total\\\\', total)]:\\\\n    a = np.array(arr)\\\\n    print(f\\\\'{name:12s}: mean={a.mean():.2f}s, median={np.median(a):.2f}s, p95={np.percentile(a,95):.2f}s, sum={a.sum():.1f}s ({a.sum()/sum(total)*100:.1f}%)\\\\')\\\\n\\\\nprint()\\\\n# SC baseline overhead = only trace_gen\\\\nsc_time = sum(trace_gen)\\\\nsica_overhead = sum(extraction) + sum(dedup) + sum(maxsat)\\\\nprint(f\\\\'SC baseline time (trace_gen only): {sc_time:.1f}s = {sc_time/60:.1f}min\\\\')\\\\nprint(f\\\\'SICA extra overhead (
…[truncated 412 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-009-overhead_20260516T202925",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T20:32:08.806376+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "find /root -name python3 -o -name python 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-009-overhead_20260516T202925",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "find /root -name python3 -o -name python 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T20:32:08.806501+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-009-overhead_20260516T202925",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T20:32:08.806618+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "find /root/miniconda3/bin -name python3",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-009-overhead_20260516T202925",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "find /root/miniconda3/bin -name python3",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T20:32:08.806736+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/bin/python3\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-009-overhead_20260516T202925",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T20:32:08.806859+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "export PATH=/root/miniconda3/bin:$PATH && cd /root/symb_invariant_consensus && python3 << 'PYEOF'\nimport json\nimport numpy as np\n\nwith open('results/sica_expanded_14b.json') as f:\n    data = json.load(f)\n\nresults = data['results']\nn = len(results)\nprint(f'Total problems: {n}')\n\n# Extract timing data\ntrace_gen = []\nextraction = []\ndedup = []\nmaxsat = []\ntotal = []\nmissing = 0\n\nfor r in results:\n    t = r.get('timing')\n    if t:\n        trace_gen.append(t['trace_gen_s'])\n        extraction.append(t['extraction_s'])\n        dedup.append(t['dedup_s'])\n        maxsat.append(t['maxsat_s'])\n        total.append(t['total_s'])\n    else:\n        missing += 1\n\nprint(f'Problems with timing: {len(total)}, missing: {missing}')\nprint(f'Total wall time from summary: {data[\"summary\"][\"total_wall_time_s\"]:.1f}s = {data[\"summary\"][\"total_wall_time_s\"]/60:.1f}min')\nprint(f'Sum of per-problem total_s: {sum(total):.1f}s = {sum(total)/60:.1f}min')\nprint()\n\n# Per-stage stats\nfor name, arr in [('trace_gen', trace_gen), ('extraction', extraction), ('dedup', dedup), ('maxsat', maxsat), ('total', total)]:\n    a = np.array(arr)\n    print(f'{name:12s}: mean={a.mean():.2f}s, median={np.median(a):.2f}s, p95={np.percentile(a,95):.2f}s, sum={a.sum():.1f}s ({a.sum()/sum(total)*100:.1f}%)')\n\nprint()\n# SC baseline overhead = only trace_gen\nsc_time = sum(trace_gen)\nsica_overhead = sum(extraction) + sum(dedup) + sum(maxsat)\nprint(f'SC baseline time (trace_gen only): {sc_time:.1f}s = {sc_time/60:.1f}min')\nprint(f'SICA extra overhead (extraction+dedup+maxsat): {sica_overhead:.1f}s = {sica_overhead/60:.1f}min')\nprint(f'Overhead ratio: {sica_overhead/sc_time*100:.1f}% extra over SC')\nprint(f'Overhead per problem: {sica_overhead/len(total):.2f}s avg')\nprint()\n\n# Histogram data (for report)\ntotal_arr = np.array(total)\nbins = [0, 20, 40, 60, 80, 100, 150, 200, 300, 500, 1000]\nhist, _ = np.histogram(total_arr, bins=bins)\nprint('Per-problem total time distribution:')\nfor i in range(len(hist)):\n    print(f'  {bins[i]:4d}-{bins[i+1]:4d}s: {hist[i]:4d} problems ({hist[i]/len(total)*100:.1f}%)')\n\n# Overhead distribution\noverhead_arr = np.array(extraction) + np.array(dedup) + np.array(maxsat)\nprint(f'\\nOverhead (extraction+dedup+maxsat) distribution:')\nprint(f'  mean={overhead_arr.mean():.2f}s, median={np.median(overhead_arr):.2f}s, p95={np.percentile(overhead_arr,95):.2f}s')\noh_bins = [0, 5, 10, 15, 20, 30, 50, 100, 200]\noh_hist, _ = np.histogram(overhead_arr, bins=oh_bins)\nfor i in range(len(oh_hist)):\n    print(f'  {oh_bins[i]:3d}-{oh_bins[i+1]:3d}s: {oh_hist[i]:4d} problems ({oh_hist[i]/len(total)*100:.1f}%)')\n\n# Per-dataset breakdown\nprint('\\nPer-dataset timing:')\ndatasets = {}\nfor r in results:\n    ds = r.get('dataset', 'unknown')\n    t = r.get('timing')\n    if t:\n        if ds not in datasets:\n            datasets[ds] = {'trace_gen': [], 'extraction': [], 'overhead': [], 'total': []}\n        datasets[ds]['trace_gen'].append(t['trace_gen_s'])\n        datasets[ds]['extraction'].append(t['extraction_s'])\n        datasets[ds]['overhead'].append(t['extraction_s'] + t['dedup_s'] + t['maxsat_s'])\n        datasets[ds]['total'].append(t['total_s'])\n\nfor ds, d in datasets.items():\n    tg = np.array(d['trace_gen'])\n    oh = np.array(d['overhead'])\n    tot = np.array(d['total'])\n    print(f'  {ds}: n={len(tot)}, mean_total={tot.mean():.1f}s, mean_trace_gen={tg.mean():.1f}s, mean_overhead={oh.mean():.1f}s ({oh.mean()/tot.mean()*100:.1f}%)')\nPYEOF\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-009-overhead_20260516T202925",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "export PATH=/root/miniconda3/bin:$PATH && cd /root/symb_invariant_consensus && python3 << 'PYEOF'\nimport json\nimport numpy as np\n\nwith open('results/sica_expanded_14b.json') as f:\n    data = json.load(f)\n\nresults = data['results']\nn = len(results)\nprint(f'Total problems: {n}')\n\n# Extract timing data\ntrace_gen = []\nextraction = []\ndedup = []\nmaxsat = []\ntotal = []\nmissing = 0\n\nfor r in results:\n    t = r.get('timing')\n    if t:\n        trace_gen.append(t['trace_gen_s'])\n        extraction.append(t['extraction_s'])\n        dedup.append(t['dedup_s'])\n        maxsat.append(t['maxsat_s'])\n        total.append(t['total_s'])\n    else:\n        missing += 1\n\nprint(f'Problems with timing: {len(total)}, missing: {missing}')\nprint(f'Total wall time from summary: {data[\"summary\"][\"total_wall_time_s\"]:.1f}s = {data[\"summary\"][\"total_wall_time_s\"]/60:.1f}min')\nprint(f'Sum of per-problem total_s: {sum(total):.1f}s = {sum(total)/60:.1f}min')\nprint()\n\n# Per-stage stats\nfor name, arr in [('trace_gen', trace_gen), ('extraction', extraction), ('dedup', dedup), ('maxsat', maxsat), ('total', total)]:\n    a = np.array(arr)\n    print(f'{name:12s}: mean={a.mean():.2f}s, median={np.median(a):.2f}s, p95={np.percentile(a,95):.2f}s, sum={a.sum():.1f}s ({a.sum()/sum(total)*100:.1f}%)')\n\nprint()\n# SC baseline overhead = only trace_gen\nsc_time = sum(trace_gen)\nsica_overhead = sum(extraction) + sum(dedup) + sum(maxsat)\nprint(f'SC baseline time (trace_gen only): {sc_time:.1f}s = {sc_time/60:.1f}min')\nprint(f'SICA extra overhead (extraction+dedup+maxsat): {sica_overhead:.1f}s = {sica_overhead/60:.1f}min')\nprint(f'Overhead ratio: {sica_overhead/sc_time*100:.1f}% extra over SC')\nprint(f'Overhead per problem: {sica_overhead/len(total):.2f}s avg')\nprint()\n\n# Histogram data (for report)\ntotal_arr = np.array(total)\nbins = [0, 20, 40, 60, 80, 100, 150, 200, 300, 500, 1000]\nhist, _ = np.histogram(total_arr, bins=bins)\nprint('Per-problem total time distribution:')\nfor i in range(len(hist)):\n    print(f'  {bins[i]:4d}-{bins[i+1]:4d}s: {hist[i]:4d} problems ({hist[i]/len(total)*100:.1f}%)')\n\n# Overhead distribution\noverhead_arr = np.array(extraction) + np.array(dedup) + np.array(maxsat)\nprint(f'\\nOverhead (extraction+dedup+maxsat) distribution:')\nprint(f'  mean={overhead_arr.mean():.2f}s, median={np.median(overhead_arr):.2f}s, p95={np.percentile(overhead_arr,95):.2f}s')\noh_bins = [0, 5, 10, 15, 20, 30, 50, 100, 200]\noh_hist, _ = np.histogram(overhead_arr, bins=oh_bins)\nfor i in range(len(oh_hist)):\n    print(f'  {oh_bins[i]:3d}-{oh_bins[i+1]:3d}s: {oh_hist[i]:4d} problems ({oh_hist[i]/len(total)*100:.1f}%)')\n\n# Per-dataset breakdown\nprint('\\nPer-dataset timing:')\ndatasets = {}\nfor r in results:\n    ds = r.get('dataset', 'unknown')\n    t = r.get('timing')\n    if t:\n        if ds not in datasets:\n            datasets[ds] = {'trace_gen': [], 'extraction': [], 'overhead': [], 'total': []}\n        datasets[ds]['trace_gen'].append(t['trace_gen_s'])\n        datasets[ds]['extraction'].append(t['extraction_s'])\n        datasets[ds]['overhead'].append(t['extraction_s'] + t['dedup_s'] + t['maxsat_s'])\n        datasets[ds]['total'].append(t['total_s'])\n\nfor ds, d in datasets.items():\n    tg = np.array(d['trace_gen'])\n    oh = np.array(d['overhead'])\n    tot = np.array(d['total'])\n    print(f'  {ds}: n={len(tot)}, mean_total={tot.mean():.1f}s, mean_trace_gen={tg.mean():.1f}s, mean_overhead={oh.mean():.1f}s ({oh.mean()/tot.mean()*100:.1f}%)')\nPYEOF\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T20:32:08.807054+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Total problems: 804\\nProblems with timing: 804, missing: 0\\nTotal wall time from summary: 49558.9s = 826.0min\\nSum of per-problem total_s: 49522.2s = 825.4min\\n\\ntrace_gen   : mean=31.62s, median=31.22s, p95=46.72s, sum=25419.7s (51.3%)\\nextraction  : mean=28.97s, median=29.28s, p95=46.92s, sum=23295.0s (47.0%)\\ndedup       : mean=1.00s, median=0.83s, p95=2.34s, sum=805.2s (1.6%)\\nmaxsat      : mean=0.00s, median=0.00s, p95=0.00s, sum=2.1s (0.0%)\\ntotal       : mean=61.59s, median=63.49s, p95=91.07s, sum=49522.2s (100.0%)\\n\\nSC baseline time (trace_gen only): 25419.7s = 423.7min\\nSICA extra overhead (extraction+dedup+maxsat): 24102.3s = 401.7min\\nOverhead ratio: 94.8% extra over SC\\nOverhead per problem: 29.98s avg\\n\\nPer-problem total time distribution:\\n     0-  20s:    4 problems (0.5%)\\n    20-  40s:  125 problems (15.5%)\\n    40-  60s:  231 problems (28.7%)\\n    60-  80s:  268 problems (33.3%)\\n    80- 100s:  172 problems (21.4%)\\n   100- 150s:    4 problems (0.5%)\\n   150- 200s:    0 problems (0.0%)\\n   200- 300s:    0 problems (0.0%)\\n   300- 500s:    0 problems (0.0%)\\n   500-1000s:    0 problems (0.0%)\\n\\nOverhead (extraction+dedup+maxsat) distribution:\\n  mean=29.98s, median=30.27s, p95=47.73s\\n    0-  5s:   21 problems (2.6%)\\n    5- 10s:   35 problems (4.4%)\\n   10- 15s:   56 problems (7.0%)\\n   15- 20s:   96 problems (11.9%)\\n   20- 30s:  188 problems (23.4%)\\n   30- 50s:  406 problems (50.5%)\\n   50-100s:    2 problems (0.2%)\\n  100-200s:    0 problems (0.0%)\\n\\nPer-dataset timing:\\n  proofwriter: n=600, mean_total=65.6s, mean_trace_gen=32.0s, mean_overhead=33.6s (51.3%)\\n  folio: n=204, mean_total=49.8s, mean_trace_gen=30.6s, mean_overhead=19.2s (38.6%)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.66}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-009-overhead_20260516T202925",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T20:32:08.807275+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "export PATH=/root/miniconda3/bin:$PATH && cd /root/symb_invariant_consensus && python3 << 'PYEOF'\nimport json\nimport numpy as np\n\nwith open('results/sica_expanded_14b.json') as f:\n    data = json.load(f)\n\nresults = data['results']\n\ntrace_gen, extraction, dedup, maxsat, total = [], [], [], [], []\nfor r in results:\n    t = r['timing']\n    trace_gen.append(t['trace_gen_s'])\n    extraction.append(t['extraction_s'])\n    dedup.append(t['dedup_s'])\n    maxsat.append(t['maxsat_s'])\n    total.append(t['total_s'])\n\ntrace_gen = np.array(trace_gen)\nextraction = np.array(extraction)\ndedup = np.array(dedup)\nmaxsat = np.array(maxsat)\ntotal = np.array(total)\noverhead = extraction + dedup + maxsat\n\n# Build structured JSON\noutput = {\n    \"experiment\": \"exp-009\",\n    \"source\": \"exp-001 (sica_expanded_14b)\",\n    \"n_problems\": 804,\n    \"total_wall_time_s\": float(data[\"summary\"][\"total_wall_time_s\"]),\n    \"sum_per_problem_s\": float(total.sum()),\n    \"stages\": {\n        \"trace_generation\": {\n            \"description\": \"vLLM inference, K=12 parallel traces\",\n            \"mean_s\": round(float(trace_gen.mean()), 2),\n            \"median_s\": round(float(np.median(trace_gen)), 2),\n            \"p5_s\": round(float(np.percentile(trace_gen, 5)), 2),\n            \"p95_s\": round(float(np.percentile(trace_gen, 95)), 2),\n            \"std_s\": round(float(trace_gen.std()), 2),\n            \"total_s\": round(float(trace_gen.sum()), 1),\n            \"fraction_of_total\": round(float(trace_gen.sum() / total.sum()), 4)\n        },\n        \"constraint_extraction\": {\n            \"description\": \"LLM call per trace to extract constraints\",\n            \"mean_s\": round(float(extraction.mean()), 2),\n            \"median_s\": round(float(np.median(extraction)), 2),\n            \"p5_s\": round(float(np.percentile(extraction, 5)), 2),\n            \"p95_s\": round(float(np.percentile(extraction)), 2),\n            \"std_s\": round(float(extraction.std()), 2),\n            \"total_s\": round(float(extraction.sum()), 1),\n            \"fraction_of_total\": round(float(extraction.sum() / total.sum()), 4)\n        },\n        \"deduplication\": {\n            \"description\": \"Constraint deduplication (embedding similarity)\",\n            \"mean_s\": round(float(dedup.mean()), 2),\n            \"median_s\": round(float(np.median(dedup)), 2),\n            \"p5_s\": round(float(np.percentile(dedup, 5)), 2),\n            \"p95_s\": round(float(np.percentile(dedup, 95)), 2),\n            \"std_s\": round(float(dedup.std()), 2),\n            \"total_s\": round(float(dedup.sum()), 1),\n            \"fraction_of_total\": round(float(dedup.sum() / total.sum()), 4)\n        },\n        \"maxsat_solving\": {\n            \"description\": \"Z3 MaxSAT solver for consensus\",\n            \"mean_s\": round(float(maxsat.mean()), 4),\n            \"median_s\": round(float(np.median(maxsat)), 4),\n            \"p5_s\": round(float(np.percentile(maxsat, 5)), 4),\n            \"p95_s\": round(float(np.percentile(maxsat, 95)), 4),\n            \"std_s\": round(float(maxsat.std()), 4),\n            \"total_s\": round(float(maxsat.sum()), 2),\n            \"fraction_of_total\": round(float(maxsat.sum() / total.sum()), 6)\n        }\n    },\n    \"overhead_analysis\": {\n        \"sc_baseline_time_s\": round(float(trace_gen.sum()), 1),\n        \"sc_baseline_time_min\": round(float(trace_gen.sum() / 60), 1),\n        \"sica_extra_overhead_s\": round(float(overhead.sum()), 1),\n        \"sica_extra_overhead_min\": round(float(overhead.sum() / 60), 1),\n        \"overhead_ratio_pct\": round(float(overhead.sum() / trace_gen.sum() * 100), 1),\n        \"overhead_per_problem_mean_s\": round(float(overhead.mean()), 2),\n        \"overhead_per_problem_median_s\": round(float(np.median(overhead)), 2),\n        \"overhead_per_problem_p95_s\": round(float(np.percentile(overhead, 95)), 2)\n    },\n    \"per_dataset\": {},\n    \"total_time_distribution\": {},\n    \"overhead_distribution\": {}\n}\n\n# Per-dataset\nfor ds in ['proofwriter', 'folio']:\n    idx = [i for i, r in enumerate(results) if r['dataset'] == ds]\n    tg = trace_gen[idx]\n    oh = overhead[idx]\n    tot = total[idx]\n    output[\"per_dataset\"][ds] = {\n        \"n\": len(idx),\n        \"mean_total_s\": round(float(tot.mean()), 1),\n        \"mean_trace_gen_s\": round(float(tg.mean()), 1),\n        \"mean_overhead_s\": round(float(oh.mean()), 1),\n        \"overhead_fraction\": round(float(oh.sum() / tot.sum()), 4)\n    }\n\n# Distributions\nbins = [0, 20, 40, 60, 80, 100, 150]\nhist, _ = np.histogram(total, bins=bins)\noutput[\"total_time_distribution\"] = {f\"{bins[i]}-{bins[i+1]}s\": int(hist[i]) for i in range(len(hist))}\n\noh_bins = [0, 5, 10, 15, 20, 30, 50, 100]\noh_hist, _ = np.histogram(overhead, bins=oh_bins)\noutput[\"overhead_distribution\"] = {f\"{oh_bins[i]}-{oh_bins[i+1]}s\": int(oh_hist[i]) for i in range(len(oh_hist))}\n\nprint(json.dumps(output, indent=2))\nPYEOF\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-009-overhead_20260516T202925",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "export PATH=/root/miniconda3/bin:$PATH && cd /root/symb_invariant_consensus && python3 << 'PYEOF'\nimport json\nimport numpy as np\n\nwith open('results/sica_expanded_14b.json') as f:\n    data = json.load(f)\n\nresults = data['results']\n\ntrace_gen, extraction, dedup, maxsat, total = [], [], [], [], []\nfor r in results:\n    t = r['timing']\n    trace_gen.append(t['trace_gen_s'])\n    extraction.append(t['extraction_s'])\n    dedup.append(t['dedup_s'])\n    maxsat.append(t['maxsat_s'])\n    total.append(t['total_s'])\n\ntrace_gen = np.array(trace_gen)\nextraction = np.array(extraction)\ndedup = np.array(dedup)\nmaxsat = np.array(maxsat)\ntotal = np.array(total)\noverhead = extraction + dedup + maxsat\n\n# Build structured JSON\noutput = {\n    \"experiment\": \"exp-009\",\n    \"source\": \"exp-001 (sica_expanded_14b)\",\n    \"n_problems\": 804,\n    \"total_wall_time_s\": float(data[\"summary\"][\"total_wall_time_s\"]),\n    \"sum_per_problem_s\": float(total.sum()),\n    \"stages\": {\n        \"trace_generation\": {\n            \"description\": \"vLLM inference, K=12 parallel traces\",\n            \"mean_s\": round(float(trace_gen.mean()), 2),\n            \"median_s\": round(float(np.median(trace_gen)), 2),\n            \"p5_s\": round(float(np.percentile(trace_gen, 5)), 2),\n            \"p95_s\": round(float(np.percentile(trace_gen, 95)), 2),\n            \"std_s\": round(float(trace_gen.std()), 2),\n            \"total_s\": round(float(trace_gen.sum()), 1),\n            \"fraction_of_total\": round(float(trace_gen.sum() / total.sum()), 4)\n        },\n        \"constraint_extraction\": {\n            \"description\": \"LLM call per trace to extract constraints\",\n            \"mean_s\": round(float(extraction.mean()), 2),\n            \"median_s\": round(float(np.median(extraction)), 2),\n            \"p5_s\": round(float(np.percentile(extraction, 5)), 2),\n            \"p95_s\": round(float(np.percentile(extraction)), 2),\n            \"std_s\": round(float(extraction.std()), 2),\n            \"total_s\": round(float(extraction.sum()), 1),\n            \"fraction_of_total\": round(float(extraction.sum() / total.sum()), 4)\n        },\n        \"deduplication\": {\n            \"description\": \"Constraint deduplication (embedding similarity)\",\n            \"mean_s\": round(float(dedup.mean()), 2),\n            \"median_s\": round(float(np.median(dedup)), 2),\n            \"p5_s\": round(float(np.percentile(dedup, 5)), 2),\n            \"p95_s\": round(float(np.percentile(dedup, 95)), 2),\n            \"std_s\": round(float(dedup.std()), 2),\n            \"total_s\": round(float(dedup.sum()), 1),\n            \"fraction_of_total\": round(float(dedup.sum() / total.sum()), 4)\n        },\n        \"maxsat_solving\": {\n            \"description\": \"Z3 MaxSAT solver for consensus\",\n            \"mean_s\": round(float(maxsat.mean()), 4),\n            \"median_s\": round(float(np.median(maxsat)), 4),\n            \"p5_s\": round(float(np.percentile(maxsat, 5)), 4),\n            \"p95_s\": round(float(np.percentile(maxsat, 95)), 4),\n            \"std_s\": round(float(maxsat.std()), 4),\n            \"total_s\": round(float(maxsat.sum()), 2),\n            \"fraction_of_total\": round(float(maxsat.sum() / total.sum()), 6)\n        }\n    },\n    \"overhead_analysis\": {\n        \"sc_baseline_time_s\": round(float(trace_gen.sum()), 1),\n        \"sc_baseline_time_min\": round(float(trace_gen.sum() / 60), 1),\n        \"sica_extra_overhead_s\": round(float(overhead.sum()), 1),\n        \"sica_extra_overhead_min\": round(float(overhead.sum() / 60), 1),\n        \"overhead_ratio_pct\": round(float(overhead.sum() / trace_gen.sum() * 100), 1),\n        \"overhead_per_problem_mean_s\": round(float(overhead.mean()), 2),\n        \"overhead_per_problem_median_s\": round(float(np.median(overhead)), 2),\n        \"overhead_per_problem_p95_s\": round(float(np.percentile(overhead, 95)), 2)\n    },\n    \"per_dataset\": {},\n    \"total_time_distribution\": {},\n    \"overhead_distribution\": {}\n}\n\n# Per-dataset\nfor ds in ['proofwriter', 'folio']:\n    idx = [i for i, r in enumerate(results) if r['dataset'] == ds]\n    tg = trace_gen[idx]\n    oh = overhead[idx]\n    tot = total[idx]\n    output[\"per_dataset\"][ds] = {\n        \"n\": len(idx),\n        \"mean_total_s\": round(float(tot.mean()), 1),\n        \"mean_trace_gen_s\": round(float(tg.mean()), 1),\n        \"mean_overhead_s\": round(float(oh.mean()), 1),\n        \"overhead_fraction\": round(float(oh.sum() / tot.sum()), 4)\n    }\n\n# Distributions\nbins = [0, 20, 40, 60, 80, 100, 150]\nhist, _ = np.histogram(total, bins=bins)\noutput[\"total_time_distribution\"] = {f\"{bins[i]}-{bins[i+1]}s\": int(hist[i]) for i in range(len(hist))}\n\noh_bins = [0, 5, 10, 15, 20, 30, 50, 100]\noh_hist, _ = np.histogram(overhead, bins=oh_bins)\noutput[\"overhead_distribution\"] = {f\"{oh_bins[i]}-{oh_bins[i+1]}s\": int(oh_hist[i]) for i in range(len(oh_hist))}\n\nprint(json.dumps(output, indent=2))\nPYEOF\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T20:32:08.807533+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'export PATH=/root/miniconda3/bin:$PATH && cd /root/symb_invariant_consensus && python3 << \\\\'PYEOF\\\\'\\\\nimport json\\\\nimport numpy as np\\\\n\\\\nwith open(\\\\'results/sica_expanded_14b.json\\\\') as f:\\\\n    data = json.load(f)\\\\n\\\\nresults = data[\\\\'results\\\\']\\\\n\\\\ntrace_gen, extraction, dedup, maxsat, total = [], [], [], [], []\\\\nfor r in results:\\\\n    t = r[\\\\'timing\\\\']\\\\n    trace_gen.append(t[\\\\'trace_gen_s\\\\'])\\\\n    extraction.append(t[\\\\'extraction_s\\\\'])\\\\n    dedup.append(t[\\\\'dedup_s\\\\'])\\\\n    maxsat.append(t[\\\\'maxsat_s\\\\'])\\\\n    total.append(t[\\\\'total_s\\\\'])\\\\n\\\\ntrace_gen = np.array(trace_gen)\\\\nextraction = np.array(extraction)\\\\ndedup = np.array(dedup)\\\\nmaxsat = np.array(maxsat)\\\\ntotal = np.array(total)\\\\noverhead = extraction + dedup + maxsat\\\\n\\\\n# Build structured JSON\\\\noutput = {\\\\n    \\\"experiment\\\": \\\"exp-009\\\",\\\\n    \\\"source\\\": \\\"exp-001 (sica_expanded_14b)\\\",\\\\n    \\\"n_problems\\\": 804,\\\\n    \\\"total_wall_time_s\\\": float(data[\\\"summary\\\"][\\\"total_wall_time_s\\\"]),\\\\n    \\\"sum_per_problem_s\\\": float(total.sum()),\\\\n    \\\"stages\\\": {\\\\n        \\\"trace_generation\\\": {\\\\n            \\\"description\\\": \\\"vLLM inference, K=12 parallel traces\\\",\\\\n            \\\"mean_s\\\": round(float(trace_gen.mean()), 2),\\\\n            \\\"median_s\\\": round(float(np.median(trace_gen)), 2),\\\\n            \\\"p5_s\\\": round(float(np.percentile(trace_gen, 5)), 2),\\\\n            \\\"p95_s\\\": round(float(np.percentile(trace_gen, 95)), 2),\\\\n            \\\"std_s\\\": round(float(trace_gen.std()), 2),\\\\n            \\\"total_s\\\": round(float(trace_gen.sum()), 1),\\\\n            \\\"fraction_of_total\\\": round(float(trace_gen.sum() / total.sum()), 4)\\\\n        },\\\\n        \\\"const
…[truncated 4148 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-009-overhead_20260516T202925",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T20:32:08.807740+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "export PATH=/root/miniconda3/bin:$PATH && cd /root/symb_invariant_consensus && python3 << 'PYEOF'\nimport json\nimport numpy as np\n\nwith open('results/sica_expanded_14b.json') as f:\n    data = json.load(f)\n\nresults = data['results']\n\ntrace_gen, extraction, dedup, maxsat, total = [], [], [], [], []\nfor r in results:\n    t = r['timing']\n    trace_gen.append(t['trace_gen_s'])\n    extraction.append(t['extraction_s'])\n    dedup.append(t['dedup_s'])\n    maxsat.append(t['maxsat_s'])\n    total.append(t['total_s'])\n\ntrace_gen = np.array(trace_gen)\nextraction = np.array(extraction)\ndedup = np.array(dedup)\nmaxsat = np.array(maxsat)\ntotal = np.array(total)\noverhead = extraction + dedup + maxsat\n\noutput = {\n    \"experiment\": \"exp-009\",\n    \"source\": \"exp-001 (sica_expanded_14b)\",\n    \"n_problems\": 804,\n    \"total_wall_time_s\": float(data[\"summary\"][\"total_wall_time_s\"]),\n    \"sum_per_problem_s\": float(total.sum()),\n    \"stages\": {\n        \"trace_generation\": {\n            \"description\": \"vLLM inference, K=12 parallel traces\",\n            \"mean_s\": round(float(trace_gen.mean()), 2),\n            \"median_s\": round(float(np.median(trace_gen)), 2),\n            \"p5_s\": round(float(np.percentile(trace_gen, 5)), 2),\n            \"p95_s\": round(float(np.percentile(trace_gen, 95)), 2),\n            \"std_s\": round(float(trace_gen.std()), 2),\n            \"total_s\": round(float(trace_gen.sum()), 1),\n            \"fraction_of_total\": round(float(trace_gen.sum() / total.sum()), 4)\n        },\n        \"constraint_extraction\": {\n            \"description\": \"LLM call per trace to extract constraints\",\n            \"mean_s\": round(float(extraction.mean()), 2),\n            \"median_s\": round(float(np.median(extraction)), 2),\n            \"p5_s\": round(float(np.percentile(extraction, 5)), 2),\n            \"p95_s\": round(float(np.percentile(extraction, 95)), 2),\n            \"std_s\": round(float(extraction.std()), 2),\n            \"total_s\": round(float(extraction.sum()), 1),\n            \"fraction_of_total\": round(float(extraction.sum() / total.sum()), 4)\n        },\n        \"deduplication\": {\n            \"description\": \"Constraint deduplication (embedding similarity)\",\n            \"mean_s\": round(float(dedup.mean()), 2),\n            \"median_s\": round(float(np.median(dedup)), 2),\n            \"p5_s\": round(float(np.percentile(dedup, 5)), 2),\n            \"p95_s\": round(float(np.percentile(dedup, 95)), 2),\n            \"std_s\": round(float(dedup.std()), 2),\n            \"total_s\": round(float(dedup.sum()), 1),\n            \"fraction_of_total\": round(float(dedup.sum() / total.sum()), 4)\n        },\n        \"maxsat_solving\": {\n            \"description\": \"Z3 MaxSAT solver for consensus\",\n            \"mean_s\": round(float(maxsat.mean()), 4),\n            \"median_s\": round(float(np.median(maxsat)), 4),\n            \"p5_s\": round(float(np.percentile(maxsat, 5)), 4),\n            \"p95_s\": round(float(np.percentile(maxsat, 95)), 4),\n            \"std_s\": round(float(maxsat.std()), 4),\n            \"total_s\": round(float(maxsat.sum()), 2),\n            \"fraction_of_total\": round(float(maxsat.sum() / total.sum()), 6)\n        }\n    },\n    \"overhead_analysis\": {\n        \"sc_baseline_time_s\": round(float(trace_gen.sum()), 1),\n        \"sc_baseline_time_min\": round(float(trace_gen.sum() / 60), 1),\n        \"sica_extra_overhead_s\": round(float(overhead.sum()), 1),\n        \"sica_extra_overhead_min\": round(float(overhead.sum() / 60), 1),\n        \"overhead_ratio_pct\": round(float(overhead.sum() / trace_gen.sum() * 100), 1),\n        \"overhead_per_problem_mean_s\": round(float(overhead.mean()), 2),\n        \"overhead_per_problem_median_s\": round(float(np.median(overhead)), 2),\n        \"overhead_per_problem_p95_s\": round(float(np.percentile(overhead, 95)), 2)\n    },\n    \"per_dataset\": {},\n    \"total_time_distribution\": {},\n    \"overhead_distribution\": {}\n}\n\nfor ds in ['proofwriter', 'folio']:\n    idx = [i for i, r in enumerate(results) if r['dataset'] == ds]\n    tg = trace_gen[idx]\n    oh = overhead[idx]\n    tot = total[idx]\n    output[\"per_dataset\"][ds] = {\n        \"n\": len(idx),\n        \"mean_total_s\": round(float(tot.mean()), 1),\n        \"mean_trace_gen_s\": round(float(tg.mean()), 1),\n        \"mean_overhead_s\": round(float(oh.mean()), 1),\n        \"overhead_fraction\": round(float(oh.sum() / tot.sum()), 4)\n    }\n\nbins = [0, 20, 40, 60, 80, 100, 150]\nhist, _ = np.histogram(total, bins=bins)\noutput[\"total_time_distribution\"] = {f\"{bins[i]}-{bins[i+1]}s\": int(hist[i]) for i in range(len(hist))}\n\noh_bins = [0, 5, 10, 15, 20, 30, 50, 100]\noh_hist, _ = np.histogram(overhead, bins=oh_bins)\noutput[\"overhead_distribution\"] = {f\"{oh_bins[i]}-{oh_bins[i+1]}s\": int(oh_hist[i]) for i in range(len(oh_hist))}\n\nprint(json.dumps(output, indent=2))\nPYEOF\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-009-overhead_20260516T202925",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "export PATH=/root/miniconda3/bin:$PATH && cd /root/symb_invariant_consensus && python3 << 'PYEOF'\nimport json\nimport numpy as np\n\nwith open('results/sica_expanded_14b.json') as f:\n    data = json.load(f)\n\nresults = data['results']\n\ntrace_gen, extraction, dedup, maxsat, total = [], [], [], [], []\nfor r in results:\n    t = r['timing']\n    trace_gen.append(t['trace_gen_s'])\n    extraction.append(t['extraction_s'])\n    dedup.append(t['dedup_s'])\n    maxsat.append(t['maxsat_s'])\n    total.append(t['total_s'])\n\ntrace_gen = np.array(trace_gen)\nextraction = np.array(extraction)\ndedup = np.array(dedup)\nmaxsat = np.array(maxsat)\ntotal = np.array(total)\noverhead = extraction + dedup + maxsat\n\noutput = {\n    \"experiment\": \"exp-009\",\n    \"source\": \"exp-001 (sica_expanded_14b)\",\n    \"n_problems\": 804,\n    \"total_wall_time_s\": float(data[\"summary\"][\"total_wall_time_s\"]),\n    \"sum_per_problem_s\": float(total.sum()),\n    \"stages\": {\n        \"trace_generation\": {\n            \"description\": \"vLLM inference, K=12 parallel traces\",\n            \"mean_s\": round(float(trace_gen.mean()), 2),\n            \"median_s\": round(float(np.median(trace_gen)), 2),\n            \"p5_s\": round(float(np.percentile(trace_gen, 5)), 2),\n            \"p95_s\": round(float(np.percentile(trace_gen, 95)), 2),\n            \"std_s\": round(float(trace_gen.std()), 2),\n            \"total_s\": round(float(trace_gen.sum()), 1),\n            \"fraction_of_total\": round(float(trace_gen.sum() / total.sum()), 4)\n        },\n        \"constraint_extraction\": {\n            \"description\": \"LLM call per trace to extract constraints\",\n            \"mean_s\": round(float(extraction.mean()), 2),\n            \"median_s\": round(float(np.median(extraction)), 2),\n            \"p5_s\": round(float(np.percentile(extraction, 5)), 2),\n            \"p95_s\": round(float(np.percentile(extraction, 95)), 2),\n            \"std_s\": round(float(extraction.std()), 2),\n            \"total_s\": round(float(extraction.sum()), 1),\n            \"fraction_of_total\": round(float(extraction.sum() / total.sum()), 4)\n        },\n        \"deduplication\": {\n            \"description\": \"Constraint deduplication (embedding similarity)\",\n            \"mean_s\": round(float(dedup.mean()), 2),\n            \"median_s\": round(float(np.median(dedup)), 2),\n            \"p5_s\": round(float(np.percentile(dedup, 5)), 2),\n            \"p95_s\": round(float(np.percentile(dedup, 95)), 2),\n            \"std_s\": round(float(dedup.std()), 2),\n            \"total_s\": round(float(dedup.sum()), 1),\n            \"fraction_of_total\": round(float(dedup.sum() / total.sum()), 4)\n        },\n        \"maxsat_solving\": {\n            \"description\": \"Z3 MaxSAT solver for consensus\",\n            \"mean_s\": round(float(maxsat.mean()), 4),\n            \"median_s\": round(float(np.median(maxsat)), 4),\n            \"p5_s\": round(float(np.percentile(maxsat, 5)), 4),\n            \"p95_s\": round(float(np.percentile(maxsat, 95)), 4),\n            \"std_s\": round(float(maxsat.std()), 4),\n            \"total_s\": round(float(maxsat.sum()), 2),\n            \"fraction_of_total\": round(float(maxsat.sum() / total.sum()), 6)\n        }\n    },\n    \"overhead_analysis\": {\n        \"sc_baseline_time_s\": round(float(trace_gen.sum()), 1),\n        \"sc_baseline_time_min\": round(float(trace_gen.sum() / 60), 1),\n        \"sica_extra_overhead_s\": round(float(overhead.sum()), 1),\n        \"sica_extra_overhead_min\": round(float(overhead.sum() / 60), 1),\n        \"overhead_ratio_pct\": round(float(overhead.sum() / trace_gen.sum() * 100), 1),\n        \"overhead_per_problem_mean_s\": round(float(overhead.mean()), 2),\n        \"overhead_per_problem_median_s\": round(float(np.median(overhead)), 2),\n        \"overhead_per_problem_p95_s\": round(float(np.percentile(overhead, 95)), 2)\n    },\n    \"per_dataset\": {},\n    \"total_time_distribution\": {},\n    \"overhead_distribution\": {}\n}\n\nfor ds in ['proofwriter', 'folio']:\n    idx = [i for i, r in enumerate(results) if r['dataset'] == ds]\n    tg = trace_gen[idx]\n    oh = overhead[idx]\n    tot = total[idx]\n    output[\"per_dataset\"][ds] = {\n        \"n\": len(idx),\n        \"mean_total_s\": round(float(tot.mean()), 1),\n        \"mean_trace_gen_s\": round(float(tg.mean()), 1),\n        \"mean_overhead_s\": round(float(oh.mean()), 1),\n        \"overhead_fraction\": round(float(oh.sum() / tot.sum()), 4)\n    }\n\nbins = [0, 20, 40, 60, 80, 100, 150]\nhist, _ = np.histogram(total, bins=bins)\noutput[\"total_time_distribution\"] = {f\"{bins[i]}-{bins[i+1]}s\": int(hist[i]) for i in range(len(hist))}\n\noh_bins = [0, 5, 10, 15, 20, 30, 50, 100]\noh_hist, _ = np.histogram(overhead, bins=oh_bins)\noutput[\"overhead_distribution\"] = {f\"{oh_bins[i]}-{oh_bins[i+1]}s\": int(oh_hist[i]) for i in range(len(oh_hist))}\n\nprint(json.dumps(output, indent=2))\nPYEOF\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T20:32:08.807994+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp-009\\\",\\n  \\\"source\\\": \\\"exp-001 (sica_expanded_14b)\\\",\\n  \\\"n_problems\\\": 804,\\n  \\\"total_wall_time_s\\\": 49558.9,\\n  \\\"sum_per_problem_s\\\": 49522.248,\\n  \\\"stages\\\": {\\n    \\\"trace_generation\\\": {\\n      \\\"description\\\": \\\"vLLM inference, K=12 parallel traces\\\",\\n      \\\"mean_s\\\": 31.62,\\n      \\\"median_s\\\": 31.22,\\n      \\\"p5_s\\\": 18.1,\\n      \\\"p95_s\\\": 46.72,\\n      \\\"std_s\\\": 8.86,\\n      \\\"total_s\\\": 25419.7,\\n      \\\"fraction_of_total\\\": 0.5133\\n    },\\n    \\\"constraint_extraction\\\": {\\n      \\\"description\\\": \\\"LLM call per trace to extract constraints\\\",\\n      \\\"mean_s\\\": 28.97,\\n      \\\"median_s\\\": 29.28,\\n      \\\"p5_s\\\": 7.94,\\n      \\\"p95_s\\\": 46.92,\\n      \\\"std_s\\\": 12.51,\\n      \\\"total_s\\\": 23295.0,\\n      \\\"fraction_of_total\\\": 0.4704\\n    },\\n    \\\"deduplication\\\": {\\n      \\\"description\\\": \\\"Constraint deduplication (embedding similarity)\\\",\\n      \\\"mean_s\\\": 1.0,\\n      \\\"median_s\\\": 0.83,\\n      \\\"p5_s\\\": 0.12,\\n      \\\"p95_s\\\": 2.34,\\n      \\\"std_s\\\": 0.72,\\n      \\\"total_s\\\": 805.2,\\n      \\\"fraction_of_total\\\": 0.0163\\n    },\\n    \\\"maxsat_solving\\\": {\\n      \\\"description\\\": \\\"Z3 MaxSAT solver for consensus\\\",\\n      \\\"mean_s\\\": 0.0026,\\n      \\\"median_s\\\": 0.003,\\n      \\\"p5_s\\\": 0.002,\\n      \\\"p95_s\\\": 0.004,\\n      \\\"std_s\\\": 0.0008,\\n      \\\"total_s\\\": 2.12,\\n      \\\"fraction_of_total\\\": 4.3e-05\\n    }\\n  },\\n  \\\"overhead_analysis\\\": {\\n    \\\"sc_baseline_time_s\\\": 25419.7,\\n    \\\"sc_baseline_time_min\\\": 423.7,\\n    \\\"sica_extra_overhead_s\\\": 24102.3,\\n    \\\"sica_extra_overhead_min\\\": 401.7,\\n    \\\"overhead_ratio_pct\\\": 94.8,\\n    \\\"overhead_per_problem_mean_s\\\": 29.98,\\n    \\\"overhea
…[truncated 1093 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-009-overhead_20260516T202925",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T20:32:08.808173+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/exp_009_overhead",
  "description": "Create exp_009 artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-009-overhead_20260516T202925",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/exp_009_overhead",
    "description": "Create exp_009 artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T20:32:08.808297+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-009-overhead_20260516T202925",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T20:32:08.808428+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/exp_009_overhead/overhead_analysis.json",
  "content": "{\n  \"experiment\": \"exp-009\",\n  \"source\": \"exp-001 (sica_expanded_14b)\",\n  \"n_problems\": 804,\n  \"total_wall_time_s\": 49558.9,\n  \"sum_per_problem_s\": 49522.248,\n  \"stages\": {\n    \"trace_generation\": {\n      \"description\": \"vLLM inference, K=12 parallel traces\",\n      \"mean_s\": 31.62,\n      \"median_s\": 31.22,\n      \"p5_s\": 18.1,\n      \"p95_s\": 46.72,\n      \"std_s\": 8.86,\n      \"total_s\": 25419.7,\n      \"fraction_of_total\": 0.5133\n    },\n    \"constraint_extraction\": {\n      \"description\": \"LLM call per trace to extract constraints\",\n      \"mean_s\": 28.97,\n      \"median_s\": 29.28,\n      \"p5_s\": 7.94,\n      \"p95_s\": 46.92,\n      \"std_s\": 12.51,\n      \"total_s\": 23295.0,\n      \"fraction_of_total\": 0.4704\n    },\n    \"deduplication\": {\n      \"description\": \"Constraint deduplication (embedding similarity)\",\n      \"mean_s\": 1.0,\n      \"median_s\": 0.83,\n      \"p5_s\": 0.12,\n      \"p95_s\": 2.34,\n      \"std_s\": 0.72,\n      \"total_s\": 805.2,\n      \"fraction_of_total\": 0.0163\n    },\n    \"maxsat_solving\": {\n      \"description\": \"Z3 MaxSAT solver for consensus\",\n      \"mean_s\": 0.0026,\n      \"median_s\": 0.003,\n      \"p5_s\": 0.002,\n      \"p95_s\": 0.004,\n      \"std_s\": 0.0008,\n      \"total_s\": 2.12,\n      \"fraction_of_total\": 4.3e-05\n    }\n  },\n  \"overhead_analysis\": {\n    \"sc_baseline_time_s\": 25419.7,\n    \"sc_baseline_time_min\": 423.7,\n    \"sica_extra_overhead_s\": 24102.3,\n    \"sica_extra_overhead_min\": 401.7,\n    \"overhead_ratio_pct\": 94.8,\n    \"overhead_per_problem_mean_s\": 29.98,\n    \"overhead_per_problem_median_s\": 30.27,\n    \"overhead_per_problem_p95_s\": 47.73\n  },\n  \"per_dataset\": {\n    \"proofwriter\": {\n      \"n\": 600,\n      \"mean_total_s\": 65.6,\n      \"mean_trace_gen_s\": 32.0,\n      \"mean_overhead_s\": 33.6,\n      \"overhead_fraction\": 0.5128\n    },\n    \"folio\": {\n      \"n\": 204,\n      \"mean_total_s\": 49.8,\n      \"mean_trace_gen_s\": 30.6,\n      \"mean_overhead_s\": 19.2,\n      \"overhead_fraction\": 0.3856\n    }\n  },\n  \"total_time_distribution\": {\n    \"0-20s\": 4,\n    \"20-40s\": 125,\n    \"40-60s\": 231,\n    \"60-80s\": 268,\n    \"80-100s\": 172,\n    \"100-150s\": 4\n  },\n  \"overhead_distribution\": {\n    \"0-5s\": 21,\n    \"5-10s\": 35,\n    \"10-15s\": 56,\n    \"15-20s\": 96,\n    \"20-30s\": 188,\n    \"30-50s\": 406,\n    \"50-100s\": 2\n  }\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-009-overhead_20260516T202925",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/exp_009_overhead/overhead_analysis.json",
    "content": "{\n  \"experiment\": \"exp-009\",\n  \"source\": \"exp-001 (sica_expanded_14b)\",\n  \"n_problems\": 804,\n  \"total_wall_time_s\": 49558.9,\n  \"sum_per_problem_s\": 49522.248,\n  \"stages\": {\n    \"trace_generation\": {\n      \"description\": \"vLLM inference, K=12 parallel traces\",\n      \"mean_s\": 31.62,\n      \"median_s\": 31.22,\n      \"p5_s\": 18.1,\n      \"p95_s\": 46.72,\n      \"std_s\": 8.86,\n      \"total_s\": 25419.7,\n      \"fraction_of_total\": 0.5133\n    },\n    \"constraint_extraction\": {\n      \"description\": \"LLM call per trace to extract constraints\",\n      \"mean_s\": 28.97,\n      \"median_s\": 29.28,\n      \"p5_s\": 7.94,\n      \"p95_s\": 46.92,\n      \"std_s\": 12.51,\n      \"total_s\": 23295.0,\n      \"fraction_of_total\": 0.4704\n    },\n    \"deduplication\": {\n      \"description\": \"Constraint deduplication (embedding similarity)\",\n      \"mean_s\": 1.0,\n      \"median_s\": 0.83,\n      \"p5_s\": 0.12,\n      \"p95_s\": 2.34,\n      \"std_s\": 0.72,\n      \"total_s\": 805.2,\n      \"fraction_of_total\": 0.0163\n    },\n    \"maxsat_solving\": {\n      \"description\": \"Z3 MaxSAT solver for consensus\",\n      \"mean_s\": 0.0026,\n      \"median_s\": 0.003,\n      \"p5_s\": 0.002,\n      \"p95_s\": 0.004,\n      \"std_s\": 0.0008,\n      \"total_s\": 2.12,\n      \"fraction_of_total\": 4.3e-05\n    }\n  },\n  \"overhead_analysis\": {\n    \"sc_baseline_time_s\": 25419.7,\n    \"sc_baseline_time_min\": 423.7,\n    \"sica_extra_overhead_s\": 24102.3,\n    \"sica_extra_overhead_min\": 401.7,\n    \"overhead_ratio_pct\": 94.8,\n    \"overhead_per_problem_mean_s\": 29.98,\n    \"overhead_per_problem_median_s\": 30.27,\n    \"overhead_per_problem_p95_s\": 47.73\n  },\n  \"per_dataset\": {\n    \"proofwriter\": {\n      \"n\": 600,\n      \"mean_total_s\": 65.6,\n      \"mean_trace_gen_s\": 32.0,\n      \"mean_overhead_s\": 33.6,\n      \"overhead_fraction\": 0.5128\n    },\n    \"folio\": {\n      \"n\": 204,\n      \"mean_total_s\": 49.8,\n      \"mean_trace_gen_s\": 30.6,\n      \"mean_overhead_s\": 19.2,\n      \"overhead_fraction\": 0.3856\n    }\n  },\n  \"total_time_distribution\": {\n    \"0-20s\": 4,\n    \"20-40s\": 125,\n    \"40-60s\": 231,\n    \"60-80s\": 268,\n    \"80-100s\": 172,\n    \"100-150s\": 4\n  },\n  \"overhead_distribution\": {\n    \"0-5s\": 21,\n    \"5-10s\": 35,\n    \"10-15s\": 56,\n    \"15-20s\": 96,\n    \"20-30s\": 188,\n    \"30-50s\": 406,\n    \"50-100s\": 2\n  }\n}\n"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T20:32:08.808583+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/exp_009_overhead/overhead_analysis.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-009-overhead_20260516T202925",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T20:32:08.808715+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/exp_009_overhead/overhead_report.md",
  "content": "# Exp-009: SICA Pipeline Overhead Analysis\n\n**Source**: exp-001 (sica_expanded_14b), 804 problems, Qwen2.5-14B via vLLM, K=12  \n**Total wall time**: 49,559s (826 min / 13.8h)  \n**All 804 problems have complete per-stage timing data.**\n\n## Stage Breakdown\n\n| Stage | Mean | Median | P95 | Total | % of Total |\n|-------|------|--------|-----|-------|------------|\n| Trace Generation (vLLM, K=12) | 31.6s | 31.2s | 46.7s | 25,420s (423.7min) | 51.3% |\n| Constraint Extraction (LLM) | 29.0s | 29.3s | 46.9s | 23,295s (388.3min) | 47.0% |\n| Deduplication (embeddings) | 1.0s | 0.8s | 2.3s | 805s (13.4min) | 1.6% |\n| MaxSAT Solving (Z3) | 0.003s | 0.003s | 0.004s | 2.1s | ~0% |\n\n## Key Finding: Overhead Ratio\n\n- **SC baseline** (trace generation only): **423.7 min**\n- **SICA extra overhead** (extraction + dedup + MaxSAT): **401.7 min**\n- **Overhead ratio**: **+94.8%** wall time over SC baseline\n- Per-problem overhead: mean 30.0s, median 30.3s, P95 47.7s\n\n## Is the Overhead Worth It?\n\n**Cost**: SICA nearly doubles wall time (+94.8%) vs. SC.\n\n**Benefit**: SICA accuracy 76.49% vs. SC 76.24% = **+0.25pp** on this benchmark. Only 2 net problems flipped (615 vs 613 correct).\n\n**Verdict**: At current accuracy gain, the overhead is **not justified** for this benchmark/model combination. The constraint extraction stage (47% of total time) dominates the overhead — it's essentially another full inference pass. The symbolic stages (dedup + MaxSAT) are negligible (<2%).\n\n## Optimization Opportunities\n\n1. **Constraint extraction is the bottleneck** — uses same LLM for extraction as for trace generation. Batching or a smaller extraction model could cut this ~50%.\n2. **Dedup + MaxSAT are already fast** — no optimization needed (1.6% combined).\n3. **Pipeline parallelism** — extraction could start as soon as each trace completes, overlapping with trace generation. Theoretical speedup: ~30% if extraction runs in parallel with later traces.\n\n## Per-Dataset Breakdown\n\n| Dataset | N | Mean Total | Mean Overhead | Overhead % |\n|---------|---|-----------|---------------|------------|\n| ProofWriter (D5) | 600 | 65.6s | 33.6s | 51.3% |\n| FOLIO | 204 | 49.8s | 19.2s | 38.6% |\n\nProofWriter has higher overhead because longer traces produce more constraints to extract. FOLIO's shorter traces yield less extraction work.\n\n## Time Distribution\n\n**Per-problem total time** (83% of problems fall in 40-100s):\n- 0-20s: 4 (0.5%)\n- 20-40s: 125 (15.5%)\n- 40-60s: 231 (28.7%)\n- 60-80s: 268 (33.3%)\n- 80-100s: 172 (21.4%)\n- 100-150s: 4 (0.5%)\n\n**Per-problem overhead** (extraction+dedup+maxsat):\n- 0-10s: 56 (7.0%)\n- 10-20s: 152 (18.9%)\n- 20-30s: 188 (23.4%)\n- 30-50s: 406 (50.5%)\n- 50-100s: 2 (0.2%)\n\n## Validation\n\n- 804/804 problems have timing data (0 missing)\n- Sum of per-problem `total_s` = 49,522s ≈ reported wall time 49,559s (0.07% difference — within tolerance)\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-009-overhead_20260516T202925",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/exp_009_overhead/overhead_report.md",
    "content": "# Exp-009: SICA Pipeline Overhead Analysis\n\n**Source**: exp-001 (sica_expanded_14b), 804 problems, Qwen2.5-14B via vLLM, K=12  \n**Total wall time**: 49,559s (826 min / 13.8h)  \n**All 804 problems have complete per-stage timing data.**\n\n## Stage Breakdown\n\n| Stage | Mean | Median | P95 | Total | % of Total |\n|-------|------|--------|-----|-------|------------|\n| Trace Generation (vLLM, K=12) | 31.6s | 31.2s | 46.7s | 25,420s (423.7min) | 51.3% |\n| Constraint Extraction (LLM) | 29.0s | 29.3s | 46.9s | 23,295s (388.3min) | 47.0% |\n| Deduplication (embeddings) | 1.0s | 0.8s | 2.3s | 805s (13.4min) | 1.6% |\n| MaxSAT Solving (Z3) | 0.003s | 0.003s | 0.004s | 2.1s | ~0% |\n\n## Key Finding: Overhead Ratio\n\n- **SC baseline** (trace generation only): **423.7 min**\n- **SICA extra overhead** (extraction + dedup + MaxSAT): **401.7 min**\n- **Overhead ratio**: **+94.8%** wall time over SC baseline\n- Per-problem overhead: mean 30.0s, median 30.3s, P95 47.7s\n\n## Is the Overhead Worth It?\n\n**Cost**: SICA nearly doubles wall time (+94.8%) vs. SC.\n\n**Benefit**: SICA accuracy 76.49% vs. SC 76.24% = **+0.25pp** on this benchmark. Only 2 net problems flipped (615 vs 613 correct).\n\n**Verdict**: At current accuracy gain, the overhead is **not justified** for this benchmark/model combination. The constraint extraction stage (47% of total time) dominates the overhead — it's essentially another full inference pass. The symbolic stages (dedup + MaxSAT) are negligible (<2%).\n\n## Optimization Opportunities\n\n1. **Constraint extraction is the bottleneck** — uses same LLM for extraction as for trace generation. Batching or a smaller extraction model could cut this ~50%.\n2. **Dedup + MaxSAT are already fast** — no optimization needed (1.6% combined).\n3. **Pipeline parallelism** — extraction could start as soon as each trace completes, overlapping with trace generation. Theoretical speedup: ~30% if extraction runs in parallel with later traces.\n\n## Per-Dataset Breakdown\n\n| Dataset | N | Mean Total | Mean Overhead | Overhead % |\n|---------|---|-----------|---------------|------------|\n| ProofWriter (D5) | 600 | 65.6s | 33.6s | 51.3% |\n| FOLIO | 204 | 49.8s | 19.2s | 38.6% |\n\nProofWriter has higher overhead because longer traces produce more constraints to extract. FOLIO's shorter traces yield less extraction work.\n\n## Time Distribution\n\n**Per-problem total time** (83% of problems fall in 40-100s):\n- 0-20s: 4 (0.5%)\n- 20-40s: 125 (15.5%)\n- 40-60s: 231 (28.7%)\n- 60-80s: 268 (33.3%)\n- 80-100s: 172 (21.4%)\n- 100-150s: 4 (0.5%)\n\n**Per-problem overhead** (extraction+dedup+maxsat):\n- 0-10s: 56 (7.0%)\n- 10-20s: 152 (18.9%)\n- 20-30s: 188 (23.4%)\n- 30-50s: 406 (50.5%)\n- 50-100s: 2 (0.2%)\n\n## Validation\n\n- 804/804 problems have timing data (0 missing)\n- Sum of per-problem `total_s` = 49,522s ≈ reported wall time 49,559s (0.07% difference — within tolerance)\n"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T20:32:08.808898+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/exp_009_overhead/overhead_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-009-overhead_20260516T202925",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T20:32:08.809031+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "exp-009 overhead analysis (JSON)",
  "type": "data",
  "description": "Structured per-stage timing breakdown of SICA pipeline overhead from 804-problem exp-001 run",
  "project": "symb_invariant_consensus",
  "exp_id": "exp-009",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/exp_009_overhead/overhead_analysis.json",
  "tags": "['overhead', 'timing', 'pipeline']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-009-overhead_20260516T202925",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "exp-009 overhead analysis (JSON)",
    "type": "data",
    "description": "Structured per-stage timing breakdown of SICA pipeline overhead from 804-problem exp-001 run",
    "project": "symb_invariant_consensus",
    "exp_id": "exp-009",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/exp_009_overhead/overhead_analysis.json",
    "tags": "['overhead', 'timing', 'pipeline']"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T20:32:08.809173+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_890595\", \"name\": \"exp-009 overhead analysis (JSON)\", \"type\": \"data\", \"description\": \"Structured per-stage timing breakdown of SICA pipeline overhead from 804-problem exp-001 run\", \"path\": \"projects/symb_invariant_consensus/artifacts/exp-009/data/overhead_analysis.json\", \"url\": null, \"project\": \"symb_invariant_consensus\", \"exp_id\": \"exp-009\", \"skill\": \"\", \"created_at\": \"2026-05-16T20:31:59.012114+00:00\", \"tags\": [\"overhead\", \"timing\", \"pipeline\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-009-overhead_20260516T202925",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T20:32:08.809295+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "exp-009 overhead report",
  "type": "report",
  "description": "Readable analysis of SICA pipeline overhead: 94.8% extra wall time over SC, dominated by constraint extraction stage",
  "project": "symb_invariant_consensus",
  "exp_id": "exp-009",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/exp_009_overhead/overhead_report.md",
  "tags": "['overhead', 'timing', 'pipeline', 'analysis']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-009-overhead_20260516T202925",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "exp-009 overhead report",
    "type": "report",
    "description": "Readable analysis of SICA pipeline overhead: 94.8% extra wall time over SC, dominated by constraint extraction stage",
    "project": "symb_invariant_consensus",
    "exp_id": "exp-009",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/exp_009_overhead/overhead_report.md",
    "tags": "['overhead', 'timing', 'pipeline', 'analysis']"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T20:32:08.809432+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_e85558\", \"name\": \"exp-009 overhead report\", \"type\": \"report\", \"description\": \"Readable analysis of SICA pipeline overhead: 94.8% extra wall time over SC, dominated by constraint extraction stage\", \"path\": \"projects/symb_invariant_consensus/artifacts/exp-009/report/overhead_report.md\", \"url\": null, \"project\": \"symb_invariant_consensus\", \"exp_id\": \"exp-009\", \"skill\": \"\", \"created_at\": \"2026-05-16T20:32:00.936957+00:00\", \"tags\": [\"overhead\", \"timing\", \"pipeline\", \"analysis\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-009-overhead_20260516T202925",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-16T20:32:08.809597+00:00_

完成。核心结论：

**SICA pipeline overhead = +94.8% wall time over SC baseline**

| 阶段 | 占比 | 特征 |
|------|------|------|
| Trace Generation (vLLM) | 51.3% | SC 也需要，不算 overhead |
| Constraint Extraction (LLM) | 47.0% | **主要 overhead 来源**，相当于又跑了一轮推理 |
| Dedup (embeddings) | 1.6% | 可忽略 |
| MaxSAT (Z3) | ~0% | 可忽略 |

以 +0.25pp accuracy gain（76.49% vs 76.24%）换取近 2x wall time，当前 ROI 不高。优化方向：extraction 阶段用更小模型或 pipeline 并行。

两份产出已注册：`overhead_analysis.json`（结构化数据）+ `overhead_report.md`（可读报告）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_exp-009-overhead_20260516T202925"
}
```

</details>

---
