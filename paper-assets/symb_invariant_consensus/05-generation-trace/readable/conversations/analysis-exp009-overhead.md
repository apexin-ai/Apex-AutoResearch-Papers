# analysis exp009 overhead

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_analysis_exp009-overhead_20260517T113105.jsonl`
- **Structured JSON:** [`e4564e178b77a4755c5d.json`](../../sessions/e4/e4564e178b77a4755c5d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-17T11:32:42.896351+00:00_

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
  "session": "worker_analysis_exp009-overhead_20260517T113105",
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

_source line 2 · 2026-05-17T11:32:42.896707+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp009-overhead_20260517T113105",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T11:32:42.896914+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "find /root/symb_invariant_consensus/results/ -name \"*.json\" -size +1M",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp009-overhead_20260517T113105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "find /root/symb_invariant_consensus/results/ -name \"*.json\" -size +1M",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-17T11:32:42.897060+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "ls -la /root/symb_invariant_consensus/results/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp009-overhead_20260517T113105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "ls -la /root/symb_invariant_consensus/results/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-17T11:32:42.897204+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/results/sica_expanded_14b.json\\n/root/symb_invariant_consensus/results/k_ablation/traces_k20.json\\n/root/symb_invariant_consensus/results/pilot_constraint_filtering/extracted_constraints.json\\n/root/symb_invariant_consensus/results/exp020_folio_200/exp020_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.24}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp009-overhead_20260517T113105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T11:32:42.897363+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 4736\\ndrwxr-xr-x 12 root root    4096 May 17 17:12 .\\ndrwxr-xr-x 13 root root    4096 May 16 13:30 ..\\n-rw-r--r--  1 root root    1947 May 15 21:08 aime30_t07.json\\n-rw-r--r--  1 root root   27082 May 16 03:06 aime30_v2.json\\n-rw-r--r--  1 root root    5571 May 15 23:48 aime30_v2_partial_backup.json\\n-rw-r--r--  1 root root    2677 May 16 00:56 aime30_v2_rescore_analysis.json\\n-rw-r--r--  1 root root    1248 May 16 16:04 analysis_expanded.json\\n-rw-r--r--  1 root root   10770 May 16 11:34 c0_precheck_qwen14b.json\\n-rw-r--r--  1 root root  335483 May 17 03:47 constraint_ablation.json\\ndrwxr-xr-x  2 root root   40960 May 17 03:46 constraint_cache\\n-rw-r--r--  1 root root  827224 May 17 03:47 constraint_cache_consolidated.json\\n-rw-r--r--  1 root root    3048 May 16 11:36 d016_smoke_test.json\\n-rw-r--r--  1 root root    7147 May 15 20:12 diversity_diagnosis.json\\n-rw-r--r--  1 root root    7233 May 17 03:23 exp001_analysis.md\\ndrwxr-xr-x  2 root root      41 May 17 11:24 exp010_mistral\\ndrwxr-xr-x  2 root root      82 May 17 18:53 exp011_llama8b\\ndrwxr-xr-x  2 root root      41 May 17 11:52 exp017_strategyqa\\ndrwxr-xr-x  2 root root      41 May 17 14:20 exp018_arc\\ndrwxr-xr-x  2 root root      41 May 17 16:19 exp019_strategyqa_200\\ndrwxr-xr-x  2 root root      41 May 17 17:14 exp020_folio_200\\n-rw-r--r--  1 root root    2554 May 16 06:27 folio_livetest.json\\ndrwxr-xr-x  2 root root    4096 May 17 08:32 k_ablation\\ndrwxr-xr-x  2 root root      78 May 17 13:27 pilot_constraint_filtering\\ndrwxr-xr-x  2 root root      52 May 17 14:20 pilot_contrastive\\n-rw-r--r--  1 root root   31655 May 16 09:35 proofwriter_30_v2.json\\n-rw-r--r--  1 root root    9679 May 16 10:56 proofwriter_5_l3l1_fix.json\\n-rw-r--r--  1 root root    5993 May 16 13:29 qwq_operating_regime.json\\n-rw-r--r--  1 root root    3946 May 16 13:30 qwq_operating_regime.md\\n-rw-r--r--  1 root root    8004 May 16 01:27 rescore
…[truncated 468 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp009-overhead_20260517T113105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T11:32:42.897539+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "head -c 3000 /root/symb_invariant_consensus/results/sica_expanded_14b.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp009-overhead_20260517T113105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "head -c 3000 /root/symb_invariant_consensus/results/sica_expanded_14b.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-17T11:32:42.897668+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "cat /root/symb_invariant_consensus/results/exp001_analysis.md",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp009-overhead_20260517T113105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "cat /root/symb_invariant_consensus/results/exp001_analysis.md",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-17T11:32:42.897868+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n_problems\\\": 804,\\n    \\\"sica_accuracy\\\": 0.7649253731343284,\\n    \\\"sc_accuracy\\\": 0.7624378109452736,\\n    \\\"sica_correct\\\": 615,\\n    \\\"sc_correct\\\": 613,\\n    \\\"extraction_rate\\\": 0.8904436152570481,\\n    \\\"answer_extraction_rate\\\": 1.0,\\n    \\\"answer_extraction_counts\\\": {\\n      \\\"boxed\\\": 9648,\\n      \\\"fallback\\\": 0,\\n      \\\"none\\\": 0\\n    },\\n    \\\"truncated_traces\\\": 0,\\n    \\\"total_constraints_extracted\\\": 88428,\\n    \\\"total_unique_constraints\\\": 17273,\\n    \\\"contradiction_rate\\\": 0.022347015573438316,\\n    \\\"problems_with_contradictions\\\": 331,\\n    \\\"per_level_accuracy\\\": {\\n      \\\"D5\\\": {\\n        \\\"sica\\\": 0.755,\\n        \\\"sc\\\": 0.7516666666666667,\\n        \\\"n\\\": 600\\n      },\\n      \\\"folio\\\": {\\n        \\\"sica\\\": 0.7941176470588235,\\n        \\\"sc\\\": 0.7941176470588235,\\n        \\\"n\\\": 204\\n      }\\n    },\\n    \\\"per_dataset_accuracy\\\": {\\n      \\\"proofwriter\\\": {\\n        \\\"sica\\\": 0.755,\\n        \\\"sc\\\": 0.7516666666666667,\\n        \\\"n\\\": 600\\n      },\\n      \\\"folio\\\": {\\n        \\\"sica\\\": 0.7941176470588235,\\n        \\\"sc\\\": 0.7941176470588235,\\n        \\\"n\\\": 204\\n      }\\n    },\\n    \\\"k\\\": 12,\\n    \\\"mode\\\": \\\"vllm\\\",\\n    \\\"total_wall_time_s\\\": 49558.9\\n  },\\n  \\\"results\\\": [\\n    {\\n      \\\"problem_idx\\\": 0,\\n      \\\"problem_id\\\": \\\"ProofWriter_AttNoneg-OWA-D5-1041_Q1\\\",\\n      \\\"problem\\\": \\\"Given the following facts and rules:\\\\nBob is cold. Bob is quiet. Bob is red. Bob is smart. Charlie is kind. Charlie is quiet. Charlie is red. Charlie is rough. Dave is cold. Dave is kind. Dave is smart. Fiona is quiet. If something is quiet and cold then it is smart. Red, cold things are round. If something is kind and rough then it is 
…[truncated 1920 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp009-overhead_20260517T113105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T11:32:42.898146+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# Exp-001 Analysis: SICA Expanded 14B (N=804)\\n\\n## 1. Summary Comparison\\n\\n| Metric | D012 Pilot (n=60) | Exp-001 Full (n=804) |\\n|--------|-------------------|---------------------|\\n| SICA Accuracy | ~76.7% | 76.49% |\\n| SC Accuracy | ~73.3% | 76.24% |\\n| Gap (SICA - SC) | +3.3 pp | +0.25 pp |\\n| Multi-candidate Rate | ~55% | 38.2% |\\n| Tie-break Cases | 10/60 (16.7%) | 38/804 (4.7%) |\\n| Bootstrap p-value | — | 0.7433 |\\n\\n## 2. Per-Domain Breakdown\\n\\n| Domain | N | SICA Acc | SC Acc | Gap (pp) | Multi-cand Rate | Tie-breaks |\\n|--------|---|----------|--------|----------|-----------------|------------|\\n| FOLIO | 204 | 79.41% | 79.41% | +0.00 | 35.3% | 6 |\\n| ProofWriter D5 | 600 | 75.50% | 75.17% | +0.33 | 39.2% | 32 |\\n| **Overall** | **804** | **76.49%** | **76.24%** | **+0.25** | **38.2%** | **38** |\\n\\n## 3. Statistical Significance\\n\\n### Bootstrap Paired Test (10,000 resamples)\\n- **Overall**: observed diff = +0.25 pp, p = 0.7433, 95% CI = [-1.12, 1.62] pp\\n- **ProofWriter D5**: observed diff = +0.33 pp, p = 0.7877, 95% CI = [-1.33, 2.00] pp\\n- **FOLIO**: diff = +0.00 pp (identical performance)\\n\\n**Interpretation**: Not statistically significant (p > 0.05)\\n\\n## 4. SICA ≠ SC Disagreement Analysis (n=31)\\n\\n### Outcome Breakdown\\n| Outcome | Count | % of Disagreements |\\n|---------|-------|-------------------|\\n| SICA wins (SICA correct, SC wrong) | 16 | 51.6% |\\n| SC wins (SC correct, SICA wrong) | 14 | 45.2% |\\n| Both wrong | 1 | 3.2% |\\n\\n### Tie-break Pattern\\n- Disagreements that are SC ties: **20/31** (64.5%)\\n- Non-tie disagreements: 11\\n\\n### Full Disagreement List\\n\\n| # | Problem ID | Dataset | GT | SICA | SC | Votes | Tie? | Winner |\\n|---|-----------|---------|-----|------|-----|-------|------|--------|\\n| 1 | ProofWriter_AttNoneg-OWA-D5-572_Q18 | proofwriter | Unknown | Unknown | False | False: 6, Unknown: 6 | Y | SICA |\\n| 2 | ProofWrit
…[truncated 5611 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp009-overhead_20260517T113105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T11:32:42.898366+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "cat << 'PYEOF' > /tmp/overhead_analysis.py\nimport json, csv, os, statistics\n\nwith open('/root/symb_invariant_consensus/results/sica_expanded_14b.json') as f:\n    data = json.load(f)\n\nresults = data['results']\nprint(f\"Total problems: {len(results)}\")\n\n# Check timing fields\nsample = results[0]['timing']\nprint(f\"Timing fields: {list(sample.keys())}\")\nprint(f\"Sample timing: {sample}\")\n\n# Extract per-problem timing\nrows = []\nfor r in results:\n    t = r['timing']\n    overhead_s = t['extraction_s'] + t['dedup_s'] + t['maxsat_s']\n    overhead_pct = (overhead_s / t['total_s'] * 100) if t['total_s'] > 0 else 0\n    rows.append({\n        'problem_id': r['problem_id'],\n        'dataset': r['dataset'],\n        'trace_gen_s': t['trace_gen_s'],\n        'extract_s': t['extraction_s'],\n        'dedup_s': t['dedup_s'],\n        'maxsat_s': t['maxsat_s'],\n        'total_s': t['total_s'],\n        'overhead_s': overhead_s,\n        'overhead_pct': overhead_pct,\n    })\n\n# Write CSV\noutdir = '/root/symb_invariant_consensus/results/exp009_overhead'\nos.makedirs(outdir, exist_ok=True)\ncsv_path = os.path.join(outdir, 'overhead_breakdown.csv')\nwith open(csv_path, 'w', newline='') as f:\n    w = csv.DictWriter(f, fieldnames=rows[0].keys())\n    w.writeheader()\n    w.writerows(rows)\nprint(f\"\\nCSV written: {csv_path} ({len(rows)} rows)\")\n\n# Summary stats\ndef stats(vals):\n    return {\n        'mean': statistics.mean(vals),\n        'median': statistics.median(vals),\n        'std': statistics.stdev(vals),\n        'min': min(vals),\n        'max': max(vals),\n    }\n\nfields = ['trace_gen_s', 'extract_s', 'dedup_s', 'maxsat_s', 'total_s', 'overhead_s', 'overhead_pct']\nprint(\"\\n\" + \"=\"*70)\nprint(f\"OVERHEAD ANALYSIS (n={len(rows)} problems):\")\nprint(\"=\"*70)\n\nfor field in fields:\n    vals = [r[field] for r in rows]\n    s = stats(vals)\n    print(f\"\\n{field}:\")\n    print(f\"  mean={s['mean']:.3f}  median={s['median']:.3f}  std={s['std']:.3f}  min={s['min']:.3f}  max={s['max']:.3f}\")\n\n# Formatted summary\ntrace_gen = [r['trace_gen_s'] for r in rows]\nextract = [r['extract_s'] for r in rows]\ndedup = [r['dedup_s'] for r in rows]\nmaxsat = [r['maxsat_s'] for r in rows]\ntotal = [r['total_s'] for r in rows]\noverhead = [r['overhead_s'] for r in rows]\n\nmean_total = statistics.mean(total)\nmean_trace = statistics.mean(trace_gen)\nmean_extract = statistics.mean(extract)\nmean_dedup = statistics.mean(dedup)\nmean_maxsat = statistics.mean(maxsat)\nmean_overhead = statistics.mean(overhead)\n\nprint(\"\\n\" + \"=\"*70)\nprint(f\"OVERHEAD ANALYSIS (n={len(rows)} problems):\")\nprint(f\"Mean total wall time: {mean_total:.1f}s/question\")\nprint(f\"  - Trace generation:       {mean_trace:.1f}s ({mean_trace/mean_total*100:.1f}%)\")\nprint(f\"  - Constraint extraction:  {mean_extract:.1f}s ({mean_extract/mean_total*100:.1f}%)\")\nprint(f\"  - Deduplication:          {mean_dedup:.1f}s ({mean_dedup/mean_total*100:.1f}%)\")\nprint(f\"  - MaxSAT solving:         {mean_maxsat:.3f}s ({mean_maxsat/mean_total*100:.2f}%)\")\nprint(f\"SICA overhead vs SC: +{mean_overhead:.1f}s/question (+{mean_overhead/mean_total*100:.1f}%)\")\nprint(f\"  (SC equivalent = trace generation only: {mean_trace:.1f}s)\")\nprint(\"=\"*70)\n\n# Per-dataset breakdown\nfor ds in ['proofwriter', 'folio']:\n    ds_rows = [r for r in rows if r['dataset'] == ds]\n    n = len(ds_rows)\n    mt = statistics.mean([r['total_s'] for r in ds_rows])\n    mtg = statistics.mean([r['trace_gen_s'] for r in ds_rows])\n    me = statistics.mean([r['extract_s'] for r in ds_rows])\n    md = statistics.mean([r['dedup_s'] for r in ds_rows])\n    mm = statistics.mean([r['maxsat_s'] for r in ds_rows])\n    mo = statistics.mean([r['overhead_s'] for r in ds_rows])\n    print(f\"\\n{ds.upper()} (n={n}):\")\n    print(f\"  Mean total: {mt:.1f}s | Trace: {mtg:.1f}s ({mtg/mt*100:.1f}%) | Extract: {me:.1f}s ({me/mt*100:.1f}%) | Dedup: {md:.1f}s ({md/mt*100:.1f}%) | MaxSAT: {mm:.3f}s ({mm/mt*100:.2f}%)\")\n    print(f\"  SICA overhead: +{mo:.1f}s (+{mo/mt*100:.1f}%)\")\n\n# Percentile distribution of overhead_pct\noverhead_pcts = sorted([r['overhead_pct'] for r in rows])\nn = len(overhead_pcts)\nprint(f\"\\nOverhead % distribution:\")\nfor p in [10, 25, 50, 75, 90, 95, 99]:\n    idx = int(n * p / 100)\n    print(f\"  P{p}: {overhead_pcts[min(idx, n-1)]:.1f}%\")\nPYEOF\npython3 /tmp/overhead_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp009-overhead_20260517T113105",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "cat << 'PYEOF' > /tmp/overhead_analysis.py\nimport json, csv, os, statistics\n\nwith open('/root/symb_invariant_consensus/results/sica_expanded_14b.json') as f:\n    data = json.load(f)\n\nresults = data['results']\nprint(f\"Total problems: {len(results)}\")\n\n# Check timing fields\nsample = results[0]['timing']\nprint(f\"Timing fields: {list(sample.keys())}\")\nprint(f\"Sample timing: {sample}\")\n\n# Extract per-problem timing\nrows = []\nfor r in results:\n    t = r['timing']\n    overhead_s = t['extraction_s'] + t['dedup_s'] + t['maxsat_s']\n    overhead_pct = (overhead_s / t['total_s'] * 100) if t['total_s'] > 0 else 0\n    rows.append({\n        'problem_id': r['problem_id'],\n        'dataset': r['dataset'],\n        'trace_gen_s': t['trace_gen_s'],\n        'extract_s': t['extraction_s'],\n        'dedup_s': t['dedup_s'],\n        'maxsat_s': t['maxsat_s'],\n        'total_s': t['total_s'],\n        'overhead_s': overhead_s,\n        'overhead_pct': overhead_pct,\n    })\n\n# Write CSV\noutdir = '/root/symb_invariant_consensus/results/exp009_overhead'\nos.makedirs(outdir, exist_ok=True)\ncsv_path = os.path.join(outdir, 'overhead_breakdown.csv')\nwith open(csv_path, 'w', newline='') as f:\n    w = csv.DictWriter(f, fieldnames=rows[0].keys())\n    w.writeheader()\n    w.writerows(rows)\nprint(f\"\\nCSV written: {csv_path} ({len(rows)} rows)\")\n\n# Summary stats\ndef stats(vals):\n    return {\n        'mean': statistics.mean(vals),\n        'median': statistics.median(vals),\n        'std': statistics.stdev(vals),\n        'min': min(vals),\n        'max': max(vals),\n    }\n\nfields = ['trace_gen_s', 'extract_s', 'dedup_s', 'maxsat_s', 'total_s', 'overhead_s', 'overhead_pct']\nprint(\"\\n\" + \"=\"*70)\nprint(f\"OVERHEAD ANALYSIS (n={len(rows)} problems):\")\nprint(\"=\"*70)\n\nfor field in fields:\n    vals = [r[field] for r in rows]\n    s = stats(vals)\n    print(f\"\\n{field}:\")\n    print(f\"  mean={s['mean']:.3f}  median={s['median']:.3f}  std={s['std']:.3f}  min={s['min']:.3f}  max={s['max']:.3f}\")\n\n# Formatted summary\ntrace_gen = [r['trace_gen_s'] for r in rows]\nextract = [r['extract_s'] for r in rows]\ndedup = [r['dedup_s'] for r in rows]\nmaxsat = [r['maxsat_s'] for r in rows]\ntotal = [r['total_s'] for r in rows]\noverhead = [r['overhead_s'] for r in rows]\n\nmean_total = statistics.mean(total)\nmean_trace = statistics.mean(trace_gen)\nmean_extract = statistics.mean(extract)\nmean_dedup = statistics.mean(dedup)\nmean_maxsat = statistics.mean(maxsat)\nmean_overhead = statistics.mean(overhead)\n\nprint(\"\\n\" + \"=\"*70)\nprint(f\"OVERHEAD ANALYSIS (n={len(rows)} problems):\")\nprint(f\"Mean total wall time: {mean_total:.1f}s/question\")\nprint(f\"  - Trace generation:       {mean_trace:.1f}s ({mean_trace/mean_total*100:.1f}%)\")\nprint(f\"  - Constraint extraction:  {mean_extract:.1f}s ({mean_extract/mean_total*100:.1f}%)\")\nprint(f\"  - Deduplication:          {mean_dedup:.1f}s ({mean_dedup/mean_total*100:.1f}%)\")\nprint(f\"  - MaxSAT solving:         {mean_maxsat:.3f}s ({mean_maxsat/mean_total*100:.2f}%)\")\nprint(f\"SICA overhead vs SC: +{mean_overhead:.1f}s/question (+{mean_overhead/mean_total*100:.1f}%)\")\nprint(f\"  (SC equivalent = trace generation only: {mean_trace:.1f}s)\")\nprint(\"=\"*70)\n\n# Per-dataset breakdown\nfor ds in ['proofwriter', 'folio']:\n    ds_rows = [r for r in rows if r['dataset'] == ds]\n    n = len(ds_rows)\n    mt = statistics.mean([r['total_s'] for r in ds_rows])\n    mtg = statistics.mean([r['trace_gen_s'] for r in ds_rows])\n    me = statistics.mean([r['extract_s'] for r in ds_rows])\n    md = statistics.mean([r['dedup_s'] for r in ds_rows])\n    mm = statistics.mean([r['maxsat_s'] for r in ds_rows])\n    mo = statistics.mean([r['overhead_s'] for r in ds_rows])\n    print(f\"\\n{ds.upper()} (n={n}):\")\n    print(f\"  Mean total: {mt:.1f}s | Trace: {mtg:.1f}s ({mtg/mt*100:.1f}%) | Extract: {me:.1f}s ({me/mt*100:.1f}%) | Dedup: {md:.1f}s ({md/mt*100:.1f}%) | MaxSAT: {mm:.3f}s ({mm/mt*100:.2f}%)\")\n    print(f\"  SICA overhead: +{mo:.1f}s (+{mo/mt*100:.1f}%)\")\n\n# Percentile distribution of overhead_pct\noverhead_pcts = sorted([r['overhead_pct'] for r in rows])\nn = len(overhead_pcts)\nprint(f\"\\nOverhead % distribution:\")\nfor p in [10, 25, 50, 75, 90, 95, 99]:\n    idx = int(n * p / 100)\n    print(f\"  P{p}: {overhead_pcts[min(idx, n-1)]:.1f}%\")\nPYEOF\npython3 /tmp/overhead_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T11:32:42.898630+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cat << \\\\'PYEOF\\\\' > /tmp/overhead_analysis.py\\\\nimport json, csv, os, statistics\\\\n\\\\nwith open(\\\\'/root/symb_invariant_consensus/results/sica_expanded_14b.json\\\\') as f:\\\\n    data = json.load(f)\\\\n\\\\nresults = data[\\\\'results\\\\']\\\\nprint(f\\\"Total problems: {len(results)}\\\")\\\\n\\\\n# Check timing fields\\\\nsample = results[0][\\\\'timing\\\\']\\\\nprint(f\\\"Timing fields: {list(sample.keys())}\\\")\\\\nprint(f\\\"Sample timing: {sample}\\\")\\\\n\\\\n# Extract per-problem timing\\\\nrows = []\\\\nfor r in results:\\\\n    t = r[\\\\'timing\\\\']\\\\n    overhead_s = t[\\\\'extraction_s\\\\'] + t[\\\\'dedup_s\\\\'] + t[\\\\'maxsat_s\\\\']\\\\n    overhead_pct = (overhead_s / t[\\\\'total_s\\\\'] * 100) if t[\\\\'total_s\\\\'] > 0 else 0\\\\n    rows.append({\\\\n        \\\\'problem_id\\\\': r[\\\\'problem_id\\\\'],\\\\n        \\\\'dataset\\\\': r[\\\\'dataset\\\\'],\\\\n        \\\\'trace_gen_s\\\\': t[\\\\'trace_gen_s\\\\'],\\\\n        \\\\'extract_s\\\\': t[\\\\'extraction_s\\\\'],\\\\n        \\\\'dedup_s\\\\': t[\\\\'dedup_s\\\\'],\\\\n        \\\\'maxsat_s\\\\': t[\\\\'maxsat_s\\\\'],\\\\n        \\\\'total_s\\\\': t[\\\\'total_s\\\\'],\\\\n        \\\\'overhead_s\\\\': overhead_s,\\\\n        \\\\'overhead_pct\\\\': overhead_pct,\\\\n    })\\\\n\\\\n# Write CSV\\\\noutdir = \\\\'/root/symb_invariant_consensus/results/exp009_overhead\\\\'\\\\nos.makedirs(outdir, exist_ok=True)\\\\ncsv_path = os.path.join(outdir, \\\\'overhead_breakdown.csv\\\\')\\\\nwith open(csv_path, \\\\'w\\\\', newline=\\\\'\\\\') as f:\\\\n    w = csv.DictWriter(f, fieldnames=rows[0].keys())\\\\n    w.writeheader()\\\\n    w.writerows(rows)\\\\nprint(f\\\"\\\\\\\\nCSV written: {csv_path} ({len(rows)} rows)\\\")\\\\n\\\\n# Summary stats\\\\ndef stats(vals):\\\\n    return {\\\\n        \\\\'mean\\\\': statistics.mean(vals),\\\\n        \\\\'med
…[truncated 3681 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp009-overhead_20260517T113105",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T11:32:42.898809+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "ls /usr/bin/python* /usr/local/bin/python* /root/miniconda3/bin/python* 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp009-overhead_20260517T113105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "ls /usr/bin/python* /usr/local/bin/python* /root/miniconda3/bin/python* 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T11:32:42.898966+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp009-overhead_20260517T113105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T11:32:42.899122+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "find /usr/bin /usr/local/bin /root/miniconda3/bin /opt -name \"python*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp009-overhead_20260517T113105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "find /usr/bin /usr/local/bin /root/miniconda3/bin /opt -name \"python*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T11:32:42.899263+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/bin/python3.12\\n/root/miniconda3/bin/python3.12-config\\n/opt/nvidia/nsight-compute/2025.1.1/host/target-linux-x64/python/bin/python\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.17}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp009-overhead_20260517T113105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T11:32:42.899395+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "export PATH=/root/miniconda3/bin:$PATH && python3 -c \"\nimport json, csv, os, statistics\n\nwith open('/root/symb_invariant_consensus/results/sica_expanded_14b.json') as f:\n    data = json.load(f)\n\nresults = data['results']\nprint(f'Total problems: {len(results)}')\n\nsample = results[0]['timing']\nprint(f'Timing fields: {list(sample.keys())}')\nprint(f'Sample: {sample}')\n\nrows = []\nfor r in results:\n    t = r['timing']\n    overhead_s = t['extraction_s'] + t['dedup_s'] + t['maxsat_s']\n    overhead_pct = (overhead_s / t['total_s'] * 100) if t['total_s'] > 0 else 0\n    rows.append({\n        'problem_id': r['problem_id'],\n        'dataset': r['dataset'],\n        'trace_gen_s': t['trace_gen_s'],\n        'extract_s': t['extraction_s'],\n        'dedup_s': t['dedup_s'],\n        'maxsat_s': t['maxsat_s'],\n        'total_s': t['total_s'],\n        'overhead_s': round(overhead_s, 3),\n        'overhead_pct': round(overhead_pct, 1),\n    })\n\noutdir = '/root/symb_invariant_consensus/results/exp009_overhead'\nos.makedirs(outdir, exist_ok=True)\ncsv_path = os.path.join(outdir, 'overhead_breakdown.csv')\nwith open(csv_path, 'w', newline='') as f:\n    w = csv.DictWriter(f, fieldnames=rows[0].keys())\n    w.writeheader()\n    w.writerows(rows)\nprint(f'CSV written: {csv_path} ({len(rows)} rows)')\n\ntrace_gen = [r['trace_gen_s'] for r in rows]\nextract = [r['extract_s'] for r in rows]\ndedup = [r['dedup_s'] for r in rows]\nmaxsat = [r['maxsat_s'] for r in rows]\ntotal = [r['total_s'] for r in rows]\noverhead = [r['overhead_s'] for r in rows]\n\nmt = statistics.mean(total)\nmtg = statistics.mean(trace_gen)\nme = statistics.mean(extract)\nmd = statistics.mean(dedup)\nmm = statistics.mean(maxsat)\nmo = statistics.mean(overhead)\n\nprint()\nprint('='*60)\nprint(f'OVERHEAD ANALYSIS (n={len(rows)} problems):')\nprint(f'Mean total wall time: {mt:.1f}s/question')\nprint(f'  - Trace generation:       {mtg:.1f}s ({mtg/mt*100:.1f}%)')\nprint(f'  - Constraint extraction:  {me:.1f}s ({me/mt*100:.1f}%)')\nprint(f'  - Deduplication:          {md:.1f}s ({md/mt*100:.1f}%)')\nprint(f'  - MaxSAT solving:         {mm:.3f}s ({mm/mt*100:.2f}%)')\nprint(f'SICA overhead vs SC: +{mo:.1f}s/question (+{mo/mt*100:.1f}%)')\nprint(f'  (SC equivalent = trace generation only: {mtg:.1f}s)')\nprint('='*60)\n\nfor ds in ['proofwriter', 'folio']:\n    dr = [r for r in rows if r['dataset'] == ds]\n    n = len(dr)\n    dmt = statistics.mean([r['total_s'] for r in dr])\n    dmtg = statistics.mean([r['trace_gen_s'] for r in dr])\n    dme = statistics.mean([r['extract_s'] for r in dr])\n    dmd = statistics.mean([r['dedup_s'] for r in dr])\n    dmm = statistics.mean([r['maxsat_s'] for r in dr])\n    dmo = statistics.mean([r['overhead_s'] for r in dr])\n    print(f'{ds.upper()} (n={n}):')\n    print(f'  Total: {dmt:.1f}s | Trace: {dmtg:.1f}s ({dmtg/dmt*100:.1f}%) | Extract: {dme:.1f}s ({dme/dmt*100:.1f}%) | Dedup: {dmd:.1f}s ({dmd/dmt*100:.1f}%) | MaxSAT: {dmm:.3f}s ({dmm/dmt*100:.2f}%)')\n    print(f'  SICA overhead: +{dmo:.1f}s (+{dmo/dmt*100:.1f}%)')\n\nprint()\nprint('Overhead % percentiles:')\nopcts = sorted([r['overhead_pct'] for r in rows])\nnn = len(opcts)\nfor p in [10, 25, 50, 75, 90, 95, 99]:\n    idx = int(nn * p / 100)\n    print(f'  P{p}: {opcts[min(idx, nn-1)]:.1f}%')\n\nprint()\nprint('Per-component stats (mean/median/std/min/max):')\nfor name, vals in [('trace_gen_s', trace_gen), ('extract_s', extract), ('dedup_s', dedup), ('maxsat_s', maxsat), ('total_s', total), ('overhead_s', overhead)]:\n    s = statistics.stdev(vals)\n    med = statistics.median(vals)\n    mn = min(vals)\n    mx = max(vals)\n    avg = statistics.mean(vals)\n    print(f'  {name:15s}: mean={avg:7.2f}  median={med:7.2f}  std={s:7.2f}  min={mn:7.3f}  max={mx:7.1f}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp009-overhead_20260517T113105",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "export PATH=/root/miniconda3/bin:$PATH && python3 -c \"\nimport json, csv, os, statistics\n\nwith open('/root/symb_invariant_consensus/results/sica_expanded_14b.json') as f:\n    data = json.load(f)\n\nresults = data['results']\nprint(f'Total problems: {len(results)}')\n\nsample = results[0]['timing']\nprint(f'Timing fields: {list(sample.keys())}')\nprint(f'Sample: {sample}')\n\nrows = []\nfor r in results:\n    t = r['timing']\n    overhead_s = t['extraction_s'] + t['dedup_s'] + t['maxsat_s']\n    overhead_pct = (overhead_s / t['total_s'] * 100) if t['total_s'] > 0 else 0\n    rows.append({\n        'problem_id': r['problem_id'],\n        'dataset': r['dataset'],\n        'trace_gen_s': t['trace_gen_s'],\n        'extract_s': t['extraction_s'],\n        'dedup_s': t['dedup_s'],\n        'maxsat_s': t['maxsat_s'],\n        'total_s': t['total_s'],\n        'overhead_s': round(overhead_s, 3),\n        'overhead_pct': round(overhead_pct, 1),\n    })\n\noutdir = '/root/symb_invariant_consensus/results/exp009_overhead'\nos.makedirs(outdir, exist_ok=True)\ncsv_path = os.path.join(outdir, 'overhead_breakdown.csv')\nwith open(csv_path, 'w', newline='') as f:\n    w = csv.DictWriter(f, fieldnames=rows[0].keys())\n    w.writeheader()\n    w.writerows(rows)\nprint(f'CSV written: {csv_path} ({len(rows)} rows)')\n\ntrace_gen = [r['trace_gen_s'] for r in rows]\nextract = [r['extract_s'] for r in rows]\ndedup = [r['dedup_s'] for r in rows]\nmaxsat = [r['maxsat_s'] for r in rows]\ntotal = [r['total_s'] for r in rows]\noverhead = [r['overhead_s'] for r in rows]\n\nmt = statistics.mean(total)\nmtg = statistics.mean(trace_gen)\nme = statistics.mean(extract)\nmd = statistics.mean(dedup)\nmm = statistics.mean(maxsat)\nmo = statistics.mean(overhead)\n\nprint()\nprint('='*60)\nprint(f'OVERHEAD ANALYSIS (n={len(rows)} problems):')\nprint(f'Mean total wall time: {mt:.1f}s/question')\nprint(f'  - Trace generation:       {mtg:.1f}s ({mtg/mt*100:.1f}%)')\nprint(f'  - Constraint extraction:  {me:.1f}s ({me/mt*100:.1f}%)')\nprint(f'  - Deduplication:          {md:.1f}s ({md/mt*100:.1f}%)')\nprint(f'  - MaxSAT solving:         {mm:.3f}s ({mm/mt*100:.2f}%)')\nprint(f'SICA overhead vs SC: +{mo:.1f}s/question (+{mo/mt*100:.1f}%)')\nprint(f'  (SC equivalent = trace generation only: {mtg:.1f}s)')\nprint('='*60)\n\nfor ds in ['proofwriter', 'folio']:\n    dr = [r for r in rows if r['dataset'] == ds]\n    n = len(dr)\n    dmt = statistics.mean([r['total_s'] for r in dr])\n    dmtg = statistics.mean([r['trace_gen_s'] for r in dr])\n    dme = statistics.mean([r['extract_s'] for r in dr])\n    dmd = statistics.mean([r['dedup_s'] for r in dr])\n    dmm = statistics.mean([r['maxsat_s'] for r in dr])\n    dmo = statistics.mean([r['overhead_s'] for r in dr])\n    print(f'{ds.upper()} (n={n}):')\n    print(f'  Total: {dmt:.1f}s | Trace: {dmtg:.1f}s ({dmtg/dmt*100:.1f}%) | Extract: {dme:.1f}s ({dme/dmt*100:.1f}%) | Dedup: {dmd:.1f}s ({dmd/dmt*100:.1f}%) | MaxSAT: {dmm:.3f}s ({dmm/dmt*100:.2f}%)')\n    print(f'  SICA overhead: +{dmo:.1f}s (+{dmo/dmt*100:.1f}%)')\n\nprint()\nprint('Overhead % percentiles:')\nopcts = sorted([r['overhead_pct'] for r in rows])\nnn = len(opcts)\nfor p in [10, 25, 50, 75, 90, 95, 99]:\n    idx = int(nn * p / 100)\n    print(f'  P{p}: {opcts[min(idx, nn-1)]:.1f}%')\n\nprint()\nprint('Per-component stats (mean/median/std/min/max):')\nfor name, vals in [('trace_gen_s', trace_gen), ('extract_s', extract), ('dedup_s', dedup), ('maxsat_s', maxsat), ('total_s', total), ('overhead_s', overhead)]:\n    s = statistics.stdev(vals)\n    med = statistics.median(vals)\n    mn = min(vals)\n    mx = max(vals)\n    avg = statistics.mean(vals)\n    print(f'  {name:15s}: mean={avg:7.2f}  median={med:7.2f}  std={s:7.2f}  min={mn:7.3f}  max={mx:7.1f}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T11:32:42.899577+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Total problems: 804\\nTiming fields: ['trace_gen_s', 'extraction_s', 'dedup_s', 'maxsat_s', 'total_s']\\nSample: {'trace_gen_s': 18.991, 'extraction_s': 17.003, 'dedup_s': 0.409, 'maxsat_s': 0.003, 'total_s': 36.406}\\nCSV written: /root/symb_invariant_consensus/results/exp009_overhead/overhead_breakdown.csv (804 rows)\\n\\n============================================================\\nOVERHEAD ANALYSIS (n=804 problems):\\nMean total wall time: 61.6s/question\\n  - Trace generation:       31.6s (51.3%)\\n  - Constraint extraction:  29.0s (47.0%)\\n  - Deduplication:          1.0s (1.6%)\\n  - MaxSAT solving:         0.003s (0.00%)\\nSICA overhead vs SC: +30.0s/question (+48.7%)\\n  (SC equivalent = trace generation only: 31.6s)\\n============================================================\\nPROOFWRITER (n=600):\\n  Total: 65.6s | Trace: 32.0s (48.7%) | Extract: 32.5s (49.6%) | Dedup: 1.1s (1.7%) | MaxSAT: 0.003s (0.00%)\\n  SICA overhead: +33.6s (+51.3%)\\nFOLIO (n=204):\\n  Total: 49.8s | Trace: 30.6s (61.4%) | Extract: 18.5s (37.2%) | Dedup: 0.7s (1.4%) | MaxSAT: 0.003s (0.01%)\\n  SICA overhead: +19.2s (+38.6%)\\n\\nOverhead % percentiles:\\n  P10: 33.3%\\n  P25: 41.0%\\n  P50: 48.9%\\n  P75: 54.7%\\n  P90: 57.6%\\n  P95: 59.8%\\n  P99: 63.7%\\n\\nPer-component stats (mean/median/std/min/max):\\n  trace_gen_s    : mean=  31.62  median=  31.22  std=   8.86  min= 12.877  max=   67.4\\n  extract_s      : mean=  28.97  median=  29.28  std=  12.52  min=  2.504  max=   49.1\\n  dedup_s        : mean=   1.00  median=   0.83  std=   0.73  min=  0.010  max=    4.3\\n  maxsat_s       : mean=   0.00  median=   0.00  std=   0.00  min=  0.001  max=    0.0\\n  total_s        : mean=  61.59  median=  63.49  std=  19.55  min= 16.283  max=  105.9\\n  overhead_s     : mean=  29.98  median=  30.27  std=  12.89  min=  2.530  max=   51.3\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seco
…[truncated 15 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp009-overhead_20260517T113105",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-17T11:32:42.899777+00:00_

CSV 已写入 `/root/symb_invariant_consensus/results/exp009_overhead/overhead_breakdown.csv`。

```
============================================================
OVERHEAD ANALYSIS (n=804 problems):
Mean total wall time: 61.6s/question
  - Trace generation:       31.6s (51.3%)
  - Constraint extraction:  29.0s (47.0%)
  - Deduplication:          1.0s (1.6%)
  - MaxSAT solving:         0.003s (0.00%)
SICA overhead vs SC: +30.0s/question (+48.7%)
  (SC equivalent = trace generation only: 31.6s)
============================================================

PROOFWRITER (n=600):
  Total: 65.6s | Trace: 32.0s (48.7%) | Extract: 32.5s (49.6%)
  SICA overhead: +33.6s (+51.3%)

FOLIO (n=204):
  Total: 49.8s | Trace: 30.6s (61.4%) | Extract: 18.5s (37.2%)
  SICA overhead: +19.2s (+38.6%)

Overhead % percentiles:
  P50: 48.9%  |  P90: 57.6%  |  P99: 63.7%
```

关键发现：
- SICA 的 overhead 几乎全部来自 **constraint extraction**（LLM 二次调用），占总时间 47%
- MaxSAT 求解和去重可忽略不计（合计 <2%）
- 相比纯 SC，SICA 平均每题多花 30s（+48.7%），即总时间约翻倍
- ProofWriter 的 overhead 比 FOLIO 更重（51.3% vs 38.6%），因为 ProofWriter 约束提取文本更长

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_exp009-overhead_20260517T113105"
}
```

</details>

---
