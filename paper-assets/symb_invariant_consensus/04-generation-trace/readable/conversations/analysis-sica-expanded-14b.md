# analysis sica expanded 14b

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_analysis_sica_expanded_14b_20260516T192141.jsonl`
- **Structured JSON:** [`3153243cb1f6dc032db9.json`](../../sessions/31/3153243cb1f6dc032db9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-16T19:24:14.422506+00:00_

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
  "session": "worker_analysis_sica_expanded_14b_20260516T192141",
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

_source line 2 · 2026-05-16T19:24:14.422864+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sica_expanded_14b_20260516T192141",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T19:24:14.423160+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "ls -la /root/symb_invariant_consensus/results/sica_expanded_14b.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_sica_expanded_14b_20260516T192141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "ls -la /root/symb_invariant_consensus/results/sica_expanded_14b.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-16T19:24:14.423322+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "find /root/symb_invariant_consensus -name \"analyze_expanded*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_sica_expanded_14b_20260516T192141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "find /root/symb_invariant_consensus -name \"analyze_expanded*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-16T19:24:14.423484+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 3208559 May 17 03:01 /root/symb_invariant_consensus/results/sica_expanded_14b.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.17}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sica_expanded_14b_20260516T192141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T19:24:14.423668+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/scripts/analyze_expanded.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sica_expanded_14b_20260516T192141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T19:24:14.423818+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "cat /root/symb_invariant_consensus/scripts/analyze_expanded.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_sica_expanded_14b_20260516T192141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "cat /root/symb_invariant_consensus/scripts/analyze_expanded.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T19:24:14.424156+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nexp-001 expanded analysis: per-dataset accuracy, tiebreak stats, McNemar tests.\\n\\nInput:  results/sica_expanded_14b.json (single JSON with summary + results array)\\nOutput: markdown summary table (stdout) + analysis.json\\n\\nDependencies: Python 3.8+ (no external packages required; scipy optional for chi2 McNemar)\\n\\nUsage:\\n  python scripts/analyze_expanded.py\\n  python scripts/analyze_expanded.py --results-dir results/sica_expanded_14b.json\\n  python scripts/analyze_expanded.py --results-dir results/ --output results/analysis.json\\n  python scripts/analyze_expanded.py --d012 results/sica_d012_14b.json\\n\\\"\\\"\\\"\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport math\\nimport os\\nimport sys\\nfrom collections import Counter, defaultdict\\n\\n\\n# ── Answer normalization ─────────────────────────────────────────\\n\\ndef _normalize_logic(ans: str) -> str:\\n    s = str(ans).strip().lower()\\n    mapping = {\\n        \\\"true\\\": \\\"True\\\", \\\"t\\\": \\\"True\\\", \\\"yes\\\": \\\"True\\\",\\n        \\\"false\\\": \\\"False\\\", \\\"f\\\": \\\"False\\\", \\\"no\\\": \\\"False\\\",\\n        \\\"unknown\\\": \\\"Unknown\\\", \\\"u\\\": \\\"Unknown\\\", \\\"uncertain\\\": \\\"Unknown\\\",\\n    }\\n    return mapping.get(s, str(ans).strip())\\n\\n\\n# ── McNemar's test (exact binomial, no scipy needed) ─────────────\\n\\ndef mcnemar_pvalue(a_correct: list[bool], b_correct: list[bool]) -> float:\\n    \\\"\\\"\\\"Two-sided McNemar's test using exact binomial distribution.\\\"\\\"\\\"\\n    n10 = sum(a and not b for a, b in zip(a_correct, b_correct))\\n    n01 = sum(not a and b for a, b in zip(a_correct, b_correct))\\n    n = n10 + n01\\n    if n == 0:\\n        return 1.0\\n    k = min(n10, n01)\\n    p = sum(math.comb(n, i) * 0.5 ** n for i in range(k + 1))\\n    return min(2.0 * p, 1.0)\\n\\n\\n# ── Core analysis ───────
…[truncated 7287 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sica_expanded_14b_20260516T192141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T19:24:14.424395+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "python3 -c \"import json; d=json.load(open('/root/symb_invariant_consensus/results/sica_expanded_14b.json')); print('Keys:', list(d.keys())); print('N results:', len(d['results'])); p=d['results'][0]; print('Problem keys:', list(p.keys())); print('Example:', json.dumps(p, indent=2)[:3000])\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_sica_expanded_14b_20260516T192141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "python3 -c \"import json; d=json.load(open('/root/symb_invariant_consensus/results/sica_expanded_14b.json')); print('Keys:', list(d.keys())); print('N results:', len(d['results'])); p=d['results'][0]; print('Problem keys:', list(p.keys())); print('Example:', json.dumps(p, indent=2)[:3000])\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T19:24:14.424536+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sica_expanded_14b_20260516T192141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T19:24:14.424658+00:00_

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
  "session": "worker_analysis_sica_expanded_14b_20260516T192141",
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

_source line 12 · 2026-05-16T19:24:14.424775+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sica_expanded_14b_20260516T192141",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T19:24:14.424909+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\nd = json.load(open('/root/symb_invariant_consensus/results/sica_expanded_14b.json'))\nprint('Top keys:', list(d.keys()))\nprint('N results:', len(d['results']))\np = d['results'][0]\nprint('Problem keys:', sorted(p.keys()))\nprint()\nprint('Example problem:')\nprint(json.dumps(p, indent=2)[:3000])\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_sica_expanded_14b_20260516T192141",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\nd = json.load(open('/root/symb_invariant_consensus/results/sica_expanded_14b.json'))\nprint('Top keys:', list(d.keys()))\nprint('N results:', len(d['results']))\np = d['results'][0]\nprint('Problem keys:', sorted(p.keys()))\nprint()\nprint('Example problem:')\nprint(json.dumps(p, indent=2)[:3000])\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T19:24:14.425122+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Top keys: ['summary', 'results']\\nN results: 804\\nProblem keys: ['constraints_stats', 'dataset', 'ground_truth', 'level', 'maxsat_stats', 'per_trace', 'problem', 'problem_id', 'problem_idx', 'raw_constraints', 'sc_answer', 'sc_correct', 'sc_vote_count', 'sc_vote_distribution', 'sica_answer', 'sica_correct', 'sica_scores', 'timing', 'trace_extraction_stats', 'truncated_traces', 'wall_time_s']\\n\\nExample problem:\\n{\\n  \\\"problem_idx\\\": 0,\\n  \\\"problem_id\\\": \\\"ProofWriter_AttNoneg-OWA-D5-1041_Q1\\\",\\n  \\\"problem\\\": \\\"Given the following facts and rules:\\\\nBob is cold. Bob is quiet. Bob is red. Bob is smart. Charlie is kind. Charlie is quiet. Charlie is red. Charlie is rough. Dave is cold. Dave is kind. Dave is smart. Fiona is quiet. If something is quiet and cold then it is smart. Red, cold things are round. If something is kind and rough then it is red. All quiet things are rough. Cold, smart things are red. If something is rough then it is cold. All red things are rough. If Dave is smart and Dave is kind then Dave is quiet.\\\\n\\\\nDetermine whether the following statement is true, false, or unknown:\\\\nCharlie is kind.\\\",\\n  \\\"dataset\\\": \\\"proofwriter\\\",\\n  \\\"level\\\": \\\"D5\\\",\\n  \\\"ground_truth\\\": \\\"True\\\",\\n  \\\"sica_answer\\\": \\\"True\\\",\\n  \\\"sica_scores\\\": {\\n    \\\"True\\\": 75.0\\n  },\\n  \\\"sica_correct\\\": true,\\n  \\\"sc_answer\\\": \\\"True\\\",\\n  \\\"sc_vote_count\\\": 12,\\n  \\\"sc_vote_distribution\\\": {\\n    \\\"True\\\": 12\\n  },\\n  \\\"sc_correct\\\": true,\\n  \\\"constraints_stats\\\": {\\n    \\\"total_extracted\\\": 75,\\n    \\\"traces_with_constraints\\\": 12,\\n    \\\"unique_after_dedup\\\": 16\\n  },\\n  \\\"maxsat_stats\\\": {\\n    \\\"satisfied\\\": 16,\\n    \\\"excluded\\\": 0,\\n    \\\"total_weight\\\": 75,\\n    \\\"solve_time_ms\\\": 0.9229059796780348\\n  },\\n  \\\"timing\\\": {\\n    \\\"trace_ge
…[truncated 2561 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sica_expanded_14b_20260516T192141",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T19:24:14.425313+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\nd = json.load(open('/root/symb_invariant_consensus/results/sica_expanded_14b.json'))\nprint('Summary:')\nprint(json.dumps(d['summary'], indent=2))\nprint()\n# Check disagreements\ndisagree = [p for p in d['results'] if p['sica_answer'] != p['sc_answer']]\nprint(f'Disagreements: {len(disagree)}')\nif disagree:\n    print('First 3 disagree examples:')\n    for p in disagree[:3]:\n        print(f\\\"  {p['problem_id']}: SICA={p['sica_answer']} SC={p['sc_answer']} GT={p['ground_truth']} votes={p['sc_vote_distribution']}\\\")\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_sica_expanded_14b_20260516T192141",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\nd = json.load(open('/root/symb_invariant_consensus/results/sica_expanded_14b.json'))\nprint('Summary:')\nprint(json.dumps(d['summary'], indent=2))\nprint()\n# Check disagreements\ndisagree = [p for p in d['results'] if p['sica_answer'] != p['sc_answer']]\nprint(f'Disagreements: {len(disagree)}')\nif disagree:\n    print('First 3 disagree examples:')\n    for p in disagree[:3]:\n        print(f\\\"  {p['problem_id']}: SICA={p['sica_answer']} SC={p['sc_answer']} GT={p['ground_truth']} votes={p['sc_vote_distribution']}\\\")\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T19:24:14.425484+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Summary:\\n{\\n  \\\"n_problems\\\": 804,\\n  \\\"sica_accuracy\\\": 0.7649253731343284,\\n  \\\"sc_accuracy\\\": 0.7624378109452736,\\n  \\\"sica_correct\\\": 615,\\n  \\\"sc_correct\\\": 613,\\n  \\\"extraction_rate\\\": 0.8904436152570481,\\n  \\\"answer_extraction_rate\\\": 1.0,\\n  \\\"answer_extraction_counts\\\": {\\n    \\\"boxed\\\": 9648,\\n    \\\"fallback\\\": 0,\\n    \\\"none\\\": 0\\n  },\\n  \\\"truncated_traces\\\": 0,\\n  \\\"total_constraints_extracted\\\": 88428,\\n  \\\"total_unique_constraints\\\": 17273,\\n  \\\"contradiction_rate\\\": 0.022347015573438316,\\n  \\\"problems_with_contradictions\\\": 331,\\n  \\\"per_level_accuracy\\\": {\\n    \\\"D5\\\": {\\n      \\\"sica\\\": 0.755,\\n      \\\"sc\\\": 0.7516666666666667,\\n      \\\"n\\\": 600\\n    },\\n    \\\"folio\\\": {\\n      \\\"sica\\\": 0.7941176470588235,\\n      \\\"sc\\\": 0.7941176470588235,\\n      \\\"n\\\": 204\\n    }\\n  },\\n  \\\"per_dataset_accuracy\\\": {\\n    \\\"proofwriter\\\": {\\n      \\\"sica\\\": 0.755,\\n      \\\"sc\\\": 0.7516666666666667,\\n      \\\"n\\\": 600\\n    },\\n    \\\"folio\\\": {\\n      \\\"sica\\\": 0.7941176470588235,\\n      \\\"sc\\\": 0.7941176470588235,\\n      \\\"n\\\": 204\\n    }\\n  },\\n  \\\"k\\\": 12,\\n  \\\"mode\\\": \\\"vllm\\\",\\n  \\\"total_wall_time_s\\\": 49558.9\\n}\\n\\nDisagreements: 31\\nFirst 3 disagree examples:\\n  ProofWriter_AttNoneg-OWA-D5-572_Q18: SICA=Unknown SC=False GT=Unknown votes={'False': 6, 'Unknown': 6}\\n  ProofWriter_AttNoneg-OWA-D5-735_Q9: SICA=True SC=Unknown GT=True votes={'True': 4, 'Unknown': 8}\\n  ProofWriter_RelNoneg-OWA-D5-173_Q11: SICA=Unknown SC=True GT=True votes={'True': 6, 'Unknown': 6}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.58}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sica_expanded_14b_20260516T192141",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T19:24:14.425695+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cat > /tmp/full_analysis.py << 'SCRIPT'\nimport json, math, random, os\nfrom collections import defaultdict, Counter\n\nrandom.seed(42)\n\n# Load data\nd = json.load(open('/root/symb_invariant_consensus/results/sica_expanded_14b.json'))\nproblems = d['results']\nsummary = d['summary']\n\n# ═══ 1. Per-domain breakdown ═══\ndef is_tie(vote_dist):\n    if not vote_dist or len(vote_dist) < 2:\n        return False\n    counts = sorted(vote_dist.values(), reverse=True)\n    return counts[0] == counts[1]\n\ndef domain_stats(probs, label):\n    n = len(probs)\n    sica_c = sum(1 for p in probs if p['sica_correct'])\n    sc_c = sum(1 for p in probs if p['sc_correct'])\n    multi = sum(1 for p in probs if len(p.get('sc_vote_distribution', {})) >= 2)\n    ties = sum(1 for p in probs if is_tie(p.get('sc_vote_distribution', {})))\n    return {\n        'label': label, 'n': n,\n        'sica_acc': sica_c/n, 'sc_acc': sc_c/n,\n        'gap_pp': (sica_c - sc_c)/n * 100,\n        'multi_rate': multi/n, 'n_ties': ties\n    }\n\nfolio = [p for p in problems if p['dataset'] == 'folio']\npw = [p for p in problems if p['dataset'] == 'proofwriter']\n\nfolio_s = domain_stats(folio, 'FOLIO')\npw_s = domain_stats(pw, 'ProofWriter D5')\noverall_s = domain_stats(problems, 'Overall')\n\n# ═══ 2. Bootstrap paired significance test ═══\ndef bootstrap_paired(probs, n_resamples=10000):\n    sica_c = [1 if p['sica_correct'] else 0 for p in probs]\n    sc_c = [1 if p['sc_correct'] else 0 for p in probs]\n    n = len(probs)\n    obs_diff = sum(sica_c)/n - sum(sc_c)/n\n    \n    count_extreme = 0\n    for _ in range(n_resamples):\n        idx = [random.randint(0, n-1) for _ in range(n)]\n        s_diff = sum(sica_c[i] for i in idx)/n - sum(sc_c[i] for i in idx)/n\n        if abs(s_diff) >= abs(obs_diff):\n            count_extreme += 1\n    \n    p_value = count_extreme / n_resamples\n    \n    # CI for difference\n    diffs = []\n    for _ in range(n_resamples):\n        idx = [random.randint(0, n-1) for _ in range(n)]\n        s_diff = sum(sica_c[i] for i in idx)/n - sum(sc_c[i] for i in idx)/n\n        diffs.append(s_diff)\n    diffs.sort()\n    ci_low = diffs[int(0.025 * n_resamples)]\n    ci_high = diffs[int(0.975 * n_resamples)]\n    \n    return obs_diff, p_value, ci_low, ci_high\n\nobs_diff, p_val, ci_lo, ci_hi = bootstrap_paired(problems)\npw_diff, pw_pval, pw_ci_lo, pw_ci_hi = bootstrap_paired(pw)\n\n# ═══ 3. Disagreement analysis ═══\ndisagree = []\nfor p in problems:\n    if p['sica_answer'] != p['sc_answer']:\n        sica_win = p['sica_correct'] and not p['sc_correct']\n        sc_win = p['sc_correct'] and not p['sica_correct']\n        both_wrong = not p['sica_correct'] and not p['sc_correct']\n        disagree.append({\n            'id': p['problem_id'],\n            'dataset': p['dataset'],\n            'gt': p['ground_truth'],\n            'sica': p['sica_answer'],\n            'sc': p['sc_answer'],\n            'votes': p['sc_vote_distribution'],\n            'is_tie': is_tie(p.get('sc_vote_distribution', {})),\n            'sica_win': sica_win,\n            'sc_win': sc_win,\n            'both_wrong': both_wrong,\n            'sica_scores': p.get('sica_scores', {}),\n        })\n\nsica_wins = sum(1 for d2 in disagree if d2['sica_win'])\nsc_wins = sum(1 for d2 in disagree if d2['sc_win'])\nboth_wrong = sum(1 for d2 in disagree if d2['both_wrong'])\ntie_disagree = sum(1 for d2 in disagree if d2['is_tie'])\n\n# ═══ 4. Constraint quality metrics ═══\ntotal_unique = []\ntotal_extracted = []\nexclusion_rates = []\nextraction_rates_by_domain = {'folio': [], 'proofwriter': []}\n\nfor p in problems:\n    cs = p.get('constraints_stats', {})\n    ms = p.get('maxsat_stats', {})\n    \n    total_unique.append(cs.get('unique_after_dedup', 0))\n    total_extracted.append(cs.get('total_extracted', 0))\n    \n    sat = ms.get('satisfied', 0)\n    exc = ms.get('excluded', 0)\n    total = sat + exc\n    if total > 0:\n        exclusion_rates.append(exc / total)\n    \n    tes = p.get('trace_extraction_stats', {})\n    boxed = tes.get('boxed', 0)\n    fallback = tes.get('fallback', 0)\n    none_count = tes.get('none', 0)\n    total_traces = boxed + fallback + none_count\n    if total_traces > 0:\n        extraction_rates_by_domain[p['dataset']].append((boxed + fallback) / total_traces)\n\n# Contradictions by domain\ncontradictions_by_domain = {'folio': 0, 'proofwriter': 0}\nfor p in problems:\n    ms = p.get('maxsat_stats', {})\n    if ms.get('excluded', 0) > 0:\n        # check if any constraint was contradicted\n        pass\n# Actually use raw_constraints or contradiction info\n# The summary says contradiction_rate and problems_with_contradictions\n# Let's compute per-domain\ncontra_folio = sum(1 for p in folio if p.get('maxsat_stats', {}).get('excluded', 0) > 0 \n                   or any('contradict' in str(c).lower() for c in p.get('raw_constraints', [])))\ncontra_pw = sum(1 for p in pw if p.get('maxsat_stats', {}).get('excluded', 0) > 0\n                or any('contradict' in str(c).lower() for c in p.get('raw_constraints', [])))\n\n# Better: use exclusion as proxy for contradictions\ncontra_folio_exc = sum(1 for p in folio if p.get('maxsat_stats', {}).get('excluded', 0) > 0)\ncontra_pw_exc = sum(1 for p in pw if p.get('maxsat_stats', {}).get('excluded', 0) > 0)\n\n# ═══ 5. Capability trap analysis ═══\n# C0 multi-candidate problems where SICA helps\nmulti_probs = [p for p in problems if len(p.get('sc_vote_distribution', {})) >= 2]\nuni_probs = [p for p in problems if len(p.get('sc_vote_distribution', {})) < 2]\n\nmulti_sica_acc = sum(1 for p in multi_probs if p['sica_correct']) / len(multi_probs) if multi_probs else 0\nmulti_sc_acc = sum(1 for p in multi_probs if p['sc_correct']) / len(multi_probs) if multi_probs else 0\nuni_sica_acc = sum(1 for p in uni_probs if p['sica_correct']) / len(uni_probs) if uni_probs else 0\nuni_sc_acc = sum(1 for p in uni_probs if p['sc_correct']) / len(uni_probs) if uni_probs else 0\n\n# Exclusion rate vs accuracy correlation\n# Split by exclusion terciles\nprobs_with_exc = [(p, p['maxsat_stats'].get('excluded',0)/(p['maxsat_stats'].get('satisfied',0)+p['maxsat_stats'].get('excluded',0)+1e-9)) for p in problems]\nprobs_with_exc.sort(key=lambda x: x[1])\nn3 = len(probs_with_exc) // 3\nlow_exc = probs_with_exc[:n3]\nmid_exc = probs_with_exc[n3:2*n3]\nhigh_exc = probs_with_exc[2*n3:]\n\ndef tercile_stats(group):\n    ps = [g[0] for g in group]\n    n = len(ps)\n    sica_a = sum(1 for p in ps if p['sica_correct'])/n\n    sc_a = sum(1 for p in ps if p['sc_correct'])/n\n    avg_exc = sum(g[1] for g in group)/n\n    return sica_a, sc_a, avg_exc\n\nlow_s, low_sc, low_e = tercile_stats(low_exc)\nmid_s, mid_sc, mid_e = tercile_stats(mid_exc)\nhigh_s, high_sc, high_e = tercile_stats(high_exc)\n\n# ═══ Generate markdown report ═══\nreport = f\"\"\"# Exp-001 Analysis: SICA Expanded 14B (N=804)\n\n## 1. Summary Comparison\n\n| Metric | D012 Pilot (n=60) | Exp-001 Full (n=804) |\n|--------|-------------------|---------------------|\n| SICA Accuracy | ~76.7% | {overall_s['sica_acc']*100:.2f}% |\n| SC Accuracy | ~73.3% | {overall_s['sc_acc']*100:.2f}% |\n| Gap (SICA - SC) | +3.3 pp | +{overall_s['gap_pp']:.2f} pp |\n| Multi-candidate Rate | ~55% | {overall_s['multi_rate']*100:.1f}% |\n| Tie-break Cases | 10/60 (16.7%) | {overall_s['n_ties']}/{overall_s['n']} ({overall_s['n_ties']/overall_s['n']*100:.1f}%) |\n| Bootstrap p-value | — | {p_val:.4f} |\n\n## 2. Per-Domain Breakdown\n\n| Domain | N | SICA Acc | SC Acc | Gap (pp) | Multi-cand Rate | Tie-breaks |\n|--------|---|----------|--------|----------|-----------------|------------|\n| FOLIO | {folio_s['n']} | {folio_s['sica_acc']*100:.2f}% | {folio_s['sc_acc']*100:.2f}% | {folio_s['gap_pp']:+.2f} | {folio_s['multi_rate']*100:.1f}% | {folio_s['n_ties']} |\n| ProofWriter D5 | {pw_s['n']} | {pw_s['sica_acc']*100:.2f}% | {pw_s['sc_acc']*100:.2f}% | {pw_s['gap_pp']:+.2f} | {pw_s['multi_rate']*100:.1f}% | {pw_s['n_ties']} |\n| **Overall** | **{overall_s['n']}** | **{overall_s['sica_acc']*100:.2f}%** | **{overall_s['sc_acc']*100:.2f}%** | **{overall_s['gap_pp']:+.2f}** | **{overall_s['multi_rate']*100:.1f}%** | **{overall_s['n_ties']}** |\n\n## 3. Statistical Significance\n\n### Bootstrap Paired Test (10,000 resamples)\n- **Overall**: observed diff = {obs_diff*100:+.2f} pp, p = {p_val:.4f}, 95% CI = [{ci_lo*100:.2f}, {ci_hi*100:.2f}] pp\n- **ProofWriter D5**: observed diff = {pw_diff*100:+.2f} pp, p = {pw_pval:.4f}, 95% CI = [{pw_ci_lo*100:.2f}, {pw_ci_hi*100:.2f}] pp\n- **FOLIO**: diff = {folio_s['gap_pp']:+.2f} pp (identical performance)\n\n**Interpretation**: {'Not statistically significant (p > 0.05)' if p_val > 0.05 else 'Statistically significant (p < 0.05)'}\n\n## 4. SICA ≠ SC Disagreement Analysis (n={len(disagree)})\n\n### Outcome Breakdown\n| Outcome | Count | % of Disagreements |\n|---------|-------|-------------------|\n| SICA wins (SICA correct, SC wrong) | {sica_wins} | {sica_wins/len(disagree)*100:.1f}% |\n| SC wins (SC correct, SICA wrong) | {sc_wins} | {sc_wins/len(disagree)*100:.1f}% |\n| Both wrong | {both_wrong} | {both_wrong/len(disagree)*100:.1f}% |\n\n### Tie-break Pattern\n- Disagreements that are SC ties: **{tie_disagree}/{len(disagree)}** ({tie_disagree/len(disagree)*100:.1f}%)\n- Non-tie disagreements: {len(disagree) - tie_disagree}\n\n### Full Disagreement List\n\n| # | Problem ID | Dataset | GT | SICA | SC | Votes | Tie? | Winner |\n|---|-----------|---------|-----|------|-----|-------|------|--------|\n\"\"\"\n\nfor i, dd in enumerate(disagree):\n    winner = \"SICA\" if dd['sica_win'] else (\"SC\" if dd['sc_win'] else \"Neither\")\n    votes_str = str(dd['votes']).replace('{','').replace('}','').replace(\"'\",\"\")\n    report += f\"| {i+1} | {dd['id'][:45]} | {dd['dataset']} | {dd['gt']} | {dd['sica']} | {dd['sc']} | {votes_str} | {'Y' if dd['is_tie'] else 'N'} | {winner} |\\n\"\n\nreport += f\"\"\"\n## 5. Constraint Quality Metrics\n\n| Metric | FOLIO | ProofWriter D5 | Overall |\n|--------|-------|----------------|---------|\n| Avg unique constraints/problem | {sum(cs.get('unique_after_dedup',0) for p in folio for cs in [p.get('constraints_stats',{})])/len(folio):.1f} | {sum(cs.get('unique_after_dedup',0) for p in pw for cs in [p.get('constraints_stats',{})])/len(pw):.1f} | {sum(total_unique)/len(problems):.1f} |\n| Avg total extracted/problem | {sum(cs.get('total_extracted',0) for p in folio for cs in [p.get('constraints_stats',{})])/len(folio):.1f} | {sum(cs.get('total_extracted',0) for p in pw for cs in [p.get('constraints_stats',{})])/len(pw):.1f} | {sum(total_extracted)/len(problems):.1f} |\n| MaxSAT exclusion rate (mean) | {sum(p.get('maxsat_stats',{}).get('excluded',0)/(p.get('maxsat_stats',{}).get('satisfied',0)+p.get('maxsat_stats',{}).get('excluded',0)+1e-9) for p in folio)/len(folio)*100:.2f}% | {sum(p.get('maxsat_stats',{}).get('excluded',0)/(p.get('maxsat_stats',{}).get('satisfied',0)+p.get('maxsat_stats',{}).get('excluded',0)+1e-9) for p in pw)/len(pw)*100:.2f}% | {sum(exclusion_rates)/len(exclusion_rates)*100:.2f}% |\n| Problems with exclusions | {contra_folio_exc}/{len(folio)} ({contra_folio_exc/len(folio)*100:.1f}%) | {contra_pw_exc}/{len(pw)} ({contra_pw_exc/len(pw)*100:.1f}%) | {contra_folio_exc+contra_pw_exc}/{len(problems)} ({(contra_folio_exc+contra_pw_exc)/len(problems)*100:.1f}%) |\n| Answer extraction rate | {sum(extraction_rates_by_domain['folio'])/len(extraction_rates_by_domain['folio'])*100:.1f}% | {sum(extraction_rates_by_domain['proofwriter'])/len(extraction_rates_by_domain['proofwriter'])*100:.1f}% | {summary['answer_extraction_rate']*100:.1f}% |\n| Problems with contradictions (summary) | — | — | {summary['problems_with_contradictions']}/804 ({summary['problems_with_contradictions']/804*100:.1f}%) |\n\n## 6. Capability Trap Evidence\n\n### C0 Conditioning: Multi-candidate vs Unanimous Problems\n\n| Subset | N | SICA Acc | SC Acc | SICA-SC Gap |\n|--------|---|----------|--------|-------------|\n| Multi-candidate (≥2 answers) | {len(multi_probs)} | {multi_sica_acc*100:.2f}% | {multi_sc_acc*100:.2f}% | {(multi_sica_acc-multi_sc_acc)*100:+.2f} pp |\n| Unanimous (1 answer) | {len(uni_probs)} | {uni_sica_acc*100:.2f}% | {uni_sc_acc*100:.2f}% | {(uni_sica_acc-uni_sc_acc)*100:+.2f} pp |\n\n### Exclusion Rate Tercile Analysis\n\n| Exclusion Tercile | Avg Exclusion Rate | SICA Acc | SC Acc | Gap |\n|-------------------|-------------------|----------|--------|-----|\n| Low (bottom 1/3) | {low_e*100:.2f}% | {low_s*100:.2f}% | {low_sc*100:.2f}% | {(low_s-low_sc)*100:+.2f} pp |\n| Mid (middle 1/3) | {mid_e*100:.2f}% | {mid_s*100:.2f}% | {mid_sc*100:.2f}% | {(mid_s-mid_sc)*100:+.2f} pp |\n| High (top 1/3) | {high_e*100:.2f}% | {high_s*100:.2f}% | {high_sc*100:.2f}% | {(high_s-high_sc)*100:+.2f} pp |\n\n### Key Observations\n\n1. **Overall gap is minimal (+{overall_s['gap_pp']:.2f} pp)** — dramatically smaller than D012 pilot (+3.3 pp)\n2. **FOLIO shows zero gap** — SICA and SC perform identically at 79.41%\n3. **ProofWriter carries all the signal** — +{pw_s['gap_pp']:.2f} pp gap, but {'not significant' if pw_pval > 0.05 else 'significant'} (p={pw_pval:.4f})\n4. **Disagreements are mostly ties**: {tie_disagree}/{len(disagree)} ({tie_disagree/len(disagree)*100:.0f}%) of SICA≠SC cases are SC tie-break scenarios\n5. **SICA net wins = {sica_wins - sc_wins}** in disagreements ({sica_wins} wins vs {sc_wins} losses)\n6. **Constraint filtering is active** — {sum(exclusion_rates)/len(exclusion_rates)*100:.1f}% average exclusion rate, {summary['problems_with_contradictions']} problems with contradictions\n7. **Capability trap pattern**: SICA benefit concentrates in multi-candidate problems ({(multi_sica_acc-multi_sc_acc)*100:+.2f} pp) vs unanimous ({(uni_sica_acc-uni_sc_acc)*100:+.2f} pp)\n8. **Higher exclusion → larger gap**: {(high_s-high_sc)*100:+.2f} pp in high-exclusion tercile vs {(low_s-low_sc)*100:+.2f} pp in low\n\n---\n*Generated: 2026-05-16 | Model: Qwen2.5-14B-Instruct | K=12 traces | Total wall time: {summary['total_wall_time_s']/3600:.1f}h*\n\"\"\"\n\nos.makedirs('/root/symb_invariant_consensus/results', exist_ok=True)\nwith open('/root/symb_invariant_consensus/results/exp001_analysis.md', 'w') as f:\n    f.write(report)\n\nprint(\"Report written to /root/symb_invariant_consensus/results/exp001_analysis.md\")\nprint()\nprint(\"=== KEY RESULTS ===\")\nprint(f\"Overall: SICA {overall_s['sica_acc']*100:.2f}% vs SC {overall_s['sc_acc']*100:.2f}% (gap: +{overall_s['gap_pp']:.2f} pp)\")\nprint(f\"Bootstrap p = {p_val:.4f}, 95% CI = [{ci_lo*100:.2f}, {ci_hi*100:.2f}] pp\")\nprint(f\"Disagreements: {len(disagree)}, SICA wins {sica_wins}, SC wins {sc_wins}, both wrong {both_wrong}\")\nprint(f\"Tie-break disagrees: {tie_disagree}/{len(disagree)}\")\nprint(f\"Multi-cand gap: +{(multi_sica_acc-multi_sc_acc)*100:.2f} pp | Unanimous gap: {(uni_sica_acc-uni_sc_acc)*100:+.2f} pp\")\nSCRIPT\npython3 /tmp/full_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_sica_expanded_14b_20260516T192141",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cat > /tmp/full_analysis.py << 'SCRIPT'\nimport json, math, random, os\nfrom collections import defaultdict, Counter\n\nrandom.seed(42)\n\n# Load data\nd = json.load(open('/root/symb_invariant_consensus/results/sica_expanded_14b.json'))\nproblems = d['results']\nsummary = d['summary']\n\n# ═══ 1. Per-domain breakdown ═══\ndef is_tie(vote_dist):\n    if not vote_dist or len(vote_dist) < 2:\n        return False\n    counts = sorted(vote_dist.values(), reverse=True)\n    return counts[0] == counts[1]\n\ndef domain_stats(probs, label):\n    n = len(probs)\n    sica_c = sum(1 for p in probs if p['sica_correct'])\n    sc_c = sum(1 for p in probs if p['sc_correct'])\n    multi = sum(1 for p in probs if len(p.get('sc_vote_distribution', {})) >= 2)\n    ties = sum(1 for p in probs if is_tie(p.get('sc_vote_distribution', {})))\n    return {\n        'label': label, 'n': n,\n        'sica_acc': sica_c/n, 'sc_acc': sc_c/n,\n        'gap_pp': (sica_c - sc_c)/n * 100,\n        'multi_rate': multi/n, 'n_ties': ties\n    }\n\nfolio = [p for p in problems if p['dataset'] == 'folio']\npw = [p for p in problems if p['dataset'] == 'proofwriter']\n\nfolio_s = domain_stats(folio, 'FOLIO')\npw_s = domain_stats(pw, 'ProofWriter D5')\noverall_s = domain_stats(problems, 'Overall')\n\n# ═══ 2. Bootstrap paired significance test ═══\ndef bootstrap_paired(probs, n_resamples=10000):\n    sica_c = [1 if p['sica_correct'] else 0 for p in probs]\n    sc_c = [1 if p['sc_correct'] else 0 for p in probs]\n    n = len(probs)\n    obs_diff = sum(sica_c)/n - sum(sc_c)/n\n    \n    count_extreme = 0\n    for _ in range(n_resamples):\n        idx = [random.randint(0, n-1) for _ in range(n)]\n        s_diff = sum(sica_c[i] for i in idx)/n - sum(sc_c[i] for i in idx)/n\n        if abs(s_diff) >= abs(obs_diff):\n            count_extreme += 1\n    \n    p_value = count_extreme / n_resamples\n    \n    # CI for difference\n    diffs = []\n    for _ in range(n_resamples):\n        idx = [random.randint(0, n-1) for _ in range(n)]\n        s_diff = sum(sica_c[i] for i in idx)/n - sum(sc_c[i] for i in idx)/n\n        diffs.append(s_diff)\n    diffs.sort()\n    ci_low = diffs[int(0.025 * n_resamples)]\n    ci_high = diffs[int(0.975 * n_resamples)]\n    \n    return obs_diff, p_value, ci_low, ci_high\n\nobs_diff, p_val, ci_lo, ci_hi = bootstrap_paired(problems)\npw_diff, pw_pval, pw_ci_lo, pw_ci_hi = bootstrap_paired(pw)\n\n# ═══ 3. Disagreement analysis ═══\ndisagree = []\nfor p in problems:\n    if p['sica_answer'] != p['sc_answer']:\n        sica_win = p['sica_correct'] and not p['sc_correct']\n        sc_win = p['sc_correct'] and not p['sica_correct']\n        both_wrong = not p['sica_correct'] and not p['sc_correct']\n        disagree.append({\n            'id': p['problem_id'],\n            'dataset': p['dataset'],\n            'gt': p['ground_truth'],\n            'sica': p['sica_answer'],\n            'sc': p['sc_answer'],\n            'votes': p['sc_vote_distribution'],\n            'is_tie': is_tie(p.get('sc_vote_distribution', {})),\n            'sica_win': sica_win,\n            'sc_win': sc_win,\n            'both_wrong': both_wrong,\n            'sica_scores': p.get('sica_scores', {}),\n        })\n\nsica_wins = sum(1 for d2 in disagree if d2['sica_win'])\nsc_wins = sum(1 for d2 in disagree if d2['sc_win'])\nboth_wrong = sum(1 for d2 in disagree if d2['both_wrong'])\ntie_disagree = sum(1 for d2 in disagree if d2['is_tie'])\n\n# ═══ 4. Constraint quality metrics ═══\ntotal_unique = []\ntotal_extracted = []\nexclusion_rates = []\nextraction_rates_by_domain = {'folio': [], 'proofwriter': []}\n\nfor p in problems:\n    cs = p.get('constraints_stats', {})\n    ms = p.get('maxsat_stats', {})\n    \n    total_unique.append(cs.get('unique_after_dedup', 0))\n    total_extracted.append(cs.get('total_extracted', 0))\n    \n    sat = ms.get('satisfied', 0)\n    exc = ms.get('excluded', 0)\n    total = sat + exc\n    if total > 0:\n        exclusion_rates.append(exc / total)\n    \n    tes = p.get('trace_extraction_stats', {})\n    boxed = tes.get('boxed', 0)\n    fallback = tes.get('fallback', 0)\n    none_count = tes.get('none', 0)\n    total_traces = boxed + fallback + none_count\n    if total_traces > 0:\n        extraction_rates_by_domain[p['dataset']].append((boxed + fallback) / total_traces)\n\n# Contradictions by domain\ncontradictions_by_domain = {'folio': 0, 'proofwriter': 0}\nfor p in problems:\n    ms = p.get('maxsat_stats', {})\n    if ms.get('excluded', 0) > 0:\n        # check if any constraint was contradicted\n        pass\n# Actually use raw_constraints or contradiction info\n# The summary says contradiction_rate and problems_with_contradictions\n# Let's compute per-domain\ncontra_folio = sum(1 for p in folio if p.get('maxsat_stats', {}).get('excluded', 0) > 0 \n                   or any('contradict' in str(c).lower() for c in p.get('raw_constraints', [])))\ncontra_pw = sum(1 for p in pw if p.get('maxsat_stats', {}).get('excluded', 0) > 0\n                or any('contradict' in str(c).lower() for c in p.get('raw_constraints', [])))\n\n# Better: use exclusion as proxy for contradictions\ncontra_folio_exc = sum(1 for p in folio if p.get('maxsat_stats', {}).get('excluded', 0) > 0)\ncontra_pw_exc = sum(1 for p in pw if p.get('maxsat_stats', {}).get('excluded', 0) > 0)\n\n# ═══ 5. Capability trap analysis ═══\n# C0 multi-candidate problems where SICA helps\nmulti_probs = [p for p in problems if len(p.get('sc_vote_distribution', {})) >= 2]\nuni_probs = [p for p in problems if len(p.get('sc_vote_distribution', {})) < 2]\n\nmulti_sica_acc = sum(1 for p in multi_probs if p['sica_correct']) / len(multi_probs) if multi_probs else 0\nmulti_sc_acc = sum(1 for p in multi_probs if p['sc_correct']) / len(multi_probs) if multi_probs else 0\nuni_sica_acc = sum(1 for p in uni_probs if p['sica_correct']) / len(uni_probs) if uni_probs else 0\nuni_sc_acc = sum(1 for p in uni_probs if p['sc_correct']) / len(uni_probs) if uni_probs else 0\n\n# Exclusion rate vs accuracy correlation\n# Split by exclusion terciles\nprobs_with_exc = [(p, p['maxsat_stats'].get('excluded',0)/(p['maxsat_stats'].get('satisfied',0)+p['maxsat_stats'].get('excluded',0)+1e-9)) for p in problems]\nprobs_with_exc.sort(key=lambda x: x[1])\nn3 = len(probs_with_exc) // 3\nlow_exc = probs_with_exc[:n3]\nmid_exc = probs_with_exc[n3:2*n3]\nhigh_exc = probs_with_exc[2*n3:]\n\ndef tercile_stats(group):\n    ps = [g[0] for g in group]\n    n = len(ps)\n    sica_a = sum(1 for p in ps if p['sica_correct'])/n\n    sc_a = sum(1 for p in ps if p['sc_correct'])/n\n    avg_exc = sum(g[1] for g in group)/n\n    return sica_a, sc_a, avg_exc\n\nlow_s, low_sc, low_e = tercile_stats(low_exc)\nmid_s, mid_sc, mid_e = tercile_stats(mid_exc)\nhigh_s, high_sc, high_e = tercile_stats(high_exc)\n\n# ═══ Generate markdown report ═══\nreport = f\"\"\"# Exp-001 Analysis: SICA Expanded 14B (N=804)\n\n## 1. Summary Comparison\n\n| Metric | D012 Pilot (n=60) | Exp-001 Full (n=804) |\n|--------|-------------------|---------------------|\n| SICA Accuracy | ~76.7% | {overall_s['sica_acc']*100:.2f}% |\n| SC Accuracy | ~73.3% | {overall_s['sc_acc']*100:.2f}% |\n| Gap (SICA - SC) | +3.3 pp | +{overall_s['gap_pp']:.2f} pp |\n| Multi-candidate Rate | ~55% | {overall_s['multi_rate']*100:.1f}% |\n| Tie-break Cases | 10/60 (16.7%) | {overall_s['n_ties']}/{overall_s['n']} ({overall_s['n_ties']/overall_s['n']*100:.1f}%) |\n| Bootstrap p-value | — | {p_val:.4f} |\n\n## 2. Per-Domain Breakdown\n\n| Domain | N | SICA Acc | SC Acc | Gap (pp) | Multi-cand Rate | Tie-breaks |\n|--------|---|----------|--------|----------|-----------------|------------|\n| FOLIO | {folio_s['n']} | {folio_s['sica_acc']*100:.2f}% | {folio_s['sc_acc']*100:.2f}% | {folio_s['gap_pp']:+.2f} | {folio_s['multi_rate']*100:.1f}% | {folio_s['n_ties']} |\n| ProofWriter D5 | {pw_s['n']} | {pw_s['sica_acc']*100:.2f}% | {pw_s['sc_acc']*100:.2f}% | {pw_s['gap_pp']:+.2f} | {pw_s['multi_rate']*100:.1f}% | {pw_s['n_ties']} |\n| **Overall** | **{overall_s['n']}** | **{overall_s['sica_acc']*100:.2f}%** | **{overall_s['sc_acc']*100:.2f}%** | **{overall_s['gap_pp']:+.2f}** | **{overall_s['multi_rate']*100:.1f}%** | **{overall_s['n_ties']}** |\n\n## 3. Statistical Significance\n\n### Bootstrap Paired Test (10,000 resamples)\n- **Overall**: observed diff = {obs_diff*100:+.2f} pp, p = {p_val:.4f}, 95% CI = [{ci_lo*100:.2f}, {ci_hi*100:.2f}] pp\n- **ProofWriter D5**: observed diff = {pw_diff*100:+.2f} pp, p = {pw_pval:.4f}, 95% CI = [{pw_ci_lo*100:.2f}, {pw_ci_hi*100:.2f}] pp\n- **FOLIO**: diff = {folio_s['gap_pp']:+.2f} pp (identical performance)\n\n**Interpretation**: {'Not statistically significant (p > 0.05)' if p_val > 0.05 else 'Statistically significant (p < 0.05)'}\n\n## 4. SICA ≠ SC Disagreement Analysis (n={len(disagree)})\n\n### Outcome Breakdown\n| Outcome | Count | % of Disagreements |\n|---------|-------|-------------------|\n| SICA wins (SICA correct, SC wrong) | {sica_wins} | {sica_wins/len(disagree)*100:.1f}% |\n| SC wins (SC correct, SICA wrong) | {sc_wins} | {sc_wins/len(disagree)*100:.1f}% |\n| Both wrong | {both_wrong} | {both_wrong/len(disagree)*100:.1f}% |\n\n### Tie-break Pattern\n- Disagreements that are SC ties: **{tie_disagree}/{len(disagree)}** ({tie_disagree/len(disagree)*100:.1f}%)\n- Non-tie disagreements: {len(disagree) - tie_disagree}\n\n### Full Disagreement List\n\n| # | Problem ID | Dataset | GT | SICA | SC | Votes | Tie? | Winner |\n|---|-----------|---------|-----|------|-----|-------|------|--------|\n\"\"\"\n\nfor i, dd in enumerate(disagree):\n    winner = \"SICA\" if dd['sica_win'] else (\"SC\" if dd['sc_win'] else \"Neither\")\n    votes_str = str(dd['votes']).replace('{','').replace('}','').replace(\"'\",\"\")\n    report += f\"| {i+1} | {dd['id'][:45]} | {dd['dataset']} | {dd['gt']} | {dd['sica']} | {dd['sc']} | {votes_str} | {'Y' if dd['is_tie'] else 'N'} | {winner} |\\n\"\n\nreport += f\"\"\"\n## 5. Constraint Quality Metrics\n\n| Metric | FOLIO | ProofWriter D5 | Overall |\n|--------|-------|----------------|---------|\n| Avg unique constraints/problem | {sum(cs.get('unique_after_dedup',0) for p in folio for cs in [p.get('constraints_stats',{})])/len(folio):.1f} | {sum(cs.get('unique_after_dedup',0) for p in pw for cs in [p.get('constraints_stats',{})])/len(pw):.1f} | {sum(total_unique)/len(problems):.1f} |\n| Avg total extracted/problem | {sum(cs.get('total_extracted',0) for p in folio for cs in [p.get('constraints_stats',{})])/len(folio):.1f} | {sum(cs.get('total_extracted',0) for p in pw for cs in [p.get('constraints_stats',{})])/len(pw):.1f} | {sum(total_extracted)/len(problems):.1f} |\n| MaxSAT exclusion rate (mean) | {sum(p.get('maxsat_stats',{}).get('excluded',0)/(p.get('maxsat_stats',{}).get('satisfied',0)+p.get('maxsat_stats',{}).get('excluded',0)+1e-9) for p in folio)/len(folio)*100:.2f}% | {sum(p.get('maxsat_stats',{}).get('excluded',0)/(p.get('maxsat_stats',{}).get('satisfied',0)+p.get('maxsat_stats',{}).get('excluded',0)+1e-9) for p in pw)/len(pw)*100:.2f}% | {sum(exclusion_rates)/len(exclusion_rates)*100:.2f}% |\n| Problems with exclusions | {contra_folio_exc}/{len(folio)} ({contra_folio_exc/len(folio)*100:.1f}%) | {contra_pw_exc}/{len(pw)} ({contra_pw_exc/len(pw)*100:.1f}%) | {contra_folio_exc+contra_pw_exc}/{len(problems)} ({(contra_folio_exc+contra_pw_exc)/len(problems)*100:.1f}%) |\n| Answer extraction rate | {sum(extraction_rates_by_domain['folio'])/len(extraction_rates_by_domain['folio'])*100:.1f}% | {sum(extraction_rates_by_domain['proofwriter'])/len(extraction_rates_by_domain['proofwriter'])*100:.1f}% | {summary['answer_extraction_rate']*100:.1f}% |\n| Problems with contradictions (summary) | — | — | {summary['problems_with_contradictions']}/804 ({summary['problems_with_contradictions']/804*100:.1f}%) |\n\n## 6. Capability Trap Evidence\n\n### C0 Conditioning: Multi-candidate vs Unanimous Problems\n\n| Subset | N | SICA Acc | SC Acc | SICA-SC Gap |\n|--------|---|----------|--------|-------------|\n| Multi-candidate (≥2 answers) | {len(multi_probs)} | {multi_sica_acc*100:.2f}% | {multi_sc_acc*100:.2f}% | {(multi_sica_acc-multi_sc_acc)*100:+.2f} pp |\n| Unanimous (1 answer) | {len(uni_probs)} | {uni_sica_acc*100:.2f}% | {uni_sc_acc*100:.2f}% | {(uni_sica_acc-uni_sc_acc)*100:+.2f} pp |\n\n### Exclusion Rate Tercile Analysis\n\n| Exclusion Tercile | Avg Exclusion Rate | SICA Acc | SC Acc | Gap |\n|-------------------|-------------------|----------|--------|-----|\n| Low (bottom 1/3) | {low_e*100:.2f}% | {low_s*100:.2f}% | {low_sc*100:.2f}% | {(low_s-low_sc)*100:+.2f} pp |\n| Mid (middle 1/3) | {mid_e*100:.2f}% | {mid_s*100:.2f}% | {mid_sc*100:.2f}% | {(mid_s-mid_sc)*100:+.2f} pp |\n| High (top 1/3) | {high_e*100:.2f}% | {high_s*100:.2f}% | {high_sc*100:.2f}% | {(high_s-high_sc)*100:+.2f} pp |\n\n### Key Observations\n\n1. **Overall gap is minimal (+{overall_s['gap_pp']:.2f} pp)** — dramatically smaller than D012 pilot (+3.3 pp)\n2. **FOLIO shows zero gap** — SICA and SC perform identically at 79.41%\n3. **ProofWriter carries all the signal** — +{pw_s['gap_pp']:.2f} pp gap, but {'not significant' if pw_pval > 0.05 else 'significant'} (p={pw_pval:.4f})\n4. **Disagreements are mostly ties**: {tie_disagree}/{len(disagree)} ({tie_disagree/len(disagree)*100:.0f}%) of SICA≠SC cases are SC tie-break scenarios\n5. **SICA net wins = {sica_wins - sc_wins}** in disagreements ({sica_wins} wins vs {sc_wins} losses)\n6. **Constraint filtering is active** — {sum(exclusion_rates)/len(exclusion_rates)*100:.1f}% average exclusion rate, {summary['problems_with_contradictions']} problems with contradictions\n7. **Capability trap pattern**: SICA benefit concentrates in multi-candidate problems ({(multi_sica_acc-multi_sc_acc)*100:+.2f} pp) vs unanimous ({(uni_sica_acc-uni_sc_acc)*100:+.2f} pp)\n8. **Higher exclusion → larger gap**: {(high_s-high_sc)*100:+.2f} pp in high-exclusion tercile vs {(low_s-low_sc)*100:+.2f} pp in low\n\n---\n*Generated: 2026-05-16 | Model: Qwen2.5-14B-Instruct | K=12 traces | Total wall time: {summary['total_wall_time_s']/3600:.1f}h*\n\"\"\"\n\nos.makedirs('/root/symb_invariant_consensus/results', exist_ok=True)\nwith open('/root/symb_invariant_consensus/results/exp001_analysis.md', 'w') as f:\n    f.write(report)\n\nprint(\"Report written to /root/symb_invariant_consensus/results/exp001_analysis.md\")\nprint()\nprint(\"=== KEY RESULTS ===\")\nprint(f\"Overall: SICA {overall_s['sica_acc']*100:.2f}% vs SC {overall_s['sc_acc']*100:.2f}% (gap: +{overall_s['gap_pp']:.2f} pp)\")\nprint(f\"Bootstrap p = {p_val:.4f}, 95% CI = [{ci_lo*100:.2f}, {ci_hi*100:.2f}] pp\")\nprint(f\"Disagreements: {len(disagree)}, SICA wins {sica_wins}, SC wins {sc_wins}, both wrong {both_wrong}\")\nprint(f\"Tie-break disagrees: {tie_disagree}/{len(disagree)}\")\nprint(f\"Multi-cand gap: +{(multi_sica_acc-multi_sc_acc)*100:.2f} pp | Unanimous gap: {(uni_sica_acc-uni_sc_acc)*100:+.2f} pp\")\nSCRIPT\npython3 /tmp/full_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T19:24:14.426049+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Report written to /root/symb_invariant_consensus/results/exp001_analysis.md\\n\\n=== KEY RESULTS ===\\nOverall: SICA 76.49% vs SC 76.24% (gap: +0.25 pp)\\nBootstrap p = 0.7433, 95% CI = [-1.12, 1.62] pp\\nDisagreements: 31, SICA wins 16, SC wins 14, both wrong 1\\nTie-break disagrees: 20/31\\nMulti-cand gap: +0.65 pp | Unanimous gap: +0.00 pp\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 11.17}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sica_expanded_14b_20260516T192141",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T19:24:14.426211+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "wc -l /root/symb_invariant_consensus/results/exp001_analysis.md",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_sica_expanded_14b_20260516T192141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "wc -l /root/symb_invariant_consensus/results/exp001_analysis.md",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T19:24:14.426342+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"120 /root/symb_invariant_consensus/results/exp001_analysis.md\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sica_expanded_14b_20260516T192141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-16T19:24:14.426503+00:00_

分析完成。核心结论：

**Exp-001 (N=804) 结果：SICA 几乎无优势**

| | SICA | SC | Gap |
|--|--|--|--|
| Overall (804) | 76.49% | 76.24% | +0.25 pp |
| ProofWriter D5 (600) | 75.50% | 75.17% | +0.33 pp |
| FOLIO (204) | 79.41% | 79.41% | 0.00 pp |

- **Bootstrap p = 0.7433** — 完全不显著，95% CI = [-1.12, +1.62] pp
- **Disagreements**: 31 题中 SICA wins 16, SC wins 14, both wrong 1 → 净收益仅 +2 题
- **Tie-break 模式确认**: 20/31 (65%) 的 disagreements 是 SC tie-break (如 6:6 投票)
- **Capability trap**: SICA 仅在 multi-candidate 问题上有微弱优势 (+0.65 pp)，unanimous 问题为 0
- **Constraint quality**: 平均 21.5 unique constraints/题，exclusion rate 约在活跃使用中，但过滤力度不足以改变最终答案

与 D012 pilot (+3.3 pp) 相比，full-scale 实验的 gap 从 3.3 pp 坍缩到 0.25 pp，说明 pilot 的正向信号是小样本偏差。

报告已输出到 `/root/symb_invariant_consensus/results/exp001_analysis.md`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_sica_expanded_14b_20260516T192141"
}
```

</details>

---
