# analysis exp070 mcnemar kappa

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_analysis_exp070-mcnemar-kappa_20260519T135944.jsonl`
- **Structured JSON:** [`617969a43f3208049b70.json`](../../sessions/61/617969a43f3208049b70.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-19T14:01:06.314236+00:00_

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
  "session": "worker_analysis_exp070-mcnemar-kappa_20260519T135944",
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

_source line 2 · 2026-05-19T14:01:06.314604+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp070-mcnemar-kappa_20260519T135944",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T14:01:06.314851+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "cat /root/symb_invariant_consensus/results/exp070_qwen7b_logiqa200/exp070_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp070-mcnemar-kappa_20260519T135944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "cat /root/symb_invariant_consensus/results/exp070_qwen7b_logiqa200/exp070_results.json"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T14:01:06.315249+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n\\\": 200,\\n    \\\"sica_accuracy\\\": 0.71,\\n    \\\"sc_accuracy\\\": 0.685,\\n    \\\"delta\\\": 0.025,\\n    \\\"k\\\": 12,\\n    \\\"mode\\\": \\\"vllm\\\",\\n    \\\"total_wall_time_s\\\": 3560.2,\\n    \\\"extraction_stats\\\": {\\n      \\\"success\\\": 2303,\\n      \\\"fail_json_parse\\\": 1,\\n      \\\"fail_empty\\\": 95,\\n      \\\"fail_invalid_expr\\\": 1\\n    }\\n  },\\n  \\\"results\\\": [\\n    {\\n      \\\"problem_idx\\\": 0,\\n      \\\"problem_id\\\": \\\"logiqa_000\\\",\\n      \\\"problem\\\": \\\"Context: One seminar had 18 participants. It is known that :(1) At least 5 young teachers are female; (2) At least 6 female teachers are over middle age; (3) At least seven young women are teachers;\\\\n\\\\nQuestion: According to the above information, which of the following can be concluded about the participants?\\\\n\\\\nA. Some young teachers are not women\\\\nB. Some young women are not teachers\\\\nC. There are at least 11 young teachers\\\\nD. There are at least 13 female teachers\\\",\\n      \\\"dataset\\\": \\\"logiqa\\\",\\n      \\\"ground_truth\\\": \\\"D\\\",\\n      \\\"sica_answer\\\": \\\"D\\\",\\n      \\\"sica_scores\\\": {\\n        \\\"A\\\": 22.0,\\n        \\\"B\\\": 12.0,\\n        \\\"C\\\": 31.0,\\n        \\\"D\\\": 33.0\\n      },\\n      \\\"sica_correct\\\": true,\\n      \\\"sc_answer\\\": \\\"D\\\",\\n      \\\"sc_vote_count\\\": 6,\\n      \\\"sc_vote_distribution\\\": {\\n        \\\"A\\\": 2,\\n        \\\"D\\\": 6,\\n        \\\"C\\\": 3,\\n        \\\"B\\\": 1\\n      },\\n      \\\"sc_correct\\\": true,\\n      \\\"constraints_stats\\\": {\\n        \\\"total_extracted\\\": 41,\\n        \\\"traces_with_constraints\\\": 12,\\n        \\\"unique_after_dedup\\\": 15\\n      },\\n      \\\"maxsat_stats\\\": {\\n        \\\"satisfied\\\": 15,\\n        \\\"excluded\\\": 0,\\n        \\\"total_weight\\\": 39,\\n        \\\"
…[truncated 7923 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp070-mcnemar-kappa_20260519T135944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T14:01:06.315446+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "python3 -c \"import json; d=json.load(open('/root/symb_invariant_consensus/results/exp070_qwen7b_logiqa200/exp070_results.json')); r=d['results']; a=sum(1 for x in r if x['sc_correct'] and x['sica_correct']); b=sum(1 for x in r if x['sc_correct'] and not x['sica_correct']); c=sum(1 for x in r if not x['sc_correct'] and x['sica_correct']); d2=sum(1 for x in r if not x['sc_correct'] and not x['sica_correct']); print(f'a={a} b={b} c={c} d={d2} n={a+b+c+d2}')\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp070-mcnemar-kappa_20260519T135944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "python3 -c \"import json; d=json.load(open('/root/symb_invariant_consensus/results/exp070_qwen7b_logiqa200/exp070_results.json')); r=d['results']; a=sum(1 for x in r if x['sc_correct'] and x['sica_correct']); b=sum(1 for x in r if x['sc_correct'] and not x['sica_correct']); c=sum(1 for x in r if not x['sc_correct'] and x['sica_correct']); d2=sum(1 for x in r if not x['sc_correct'] and not x['sica_correct']); print(f'a={a} b={b} c={c} d={d2} n={a+b+c+d2}')\""
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T14:01:06.315603+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp070-mcnemar-kappa_20260519T135944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T14:01:06.315773+00:00_

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
  "session": "worker_analysis_exp070-mcnemar-kappa_20260519T135944",
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

_source line 8 · 2026-05-19T14:01:06.315952+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp070-mcnemar-kappa_20260519T135944",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T14:01:06.316098+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "python3 << 'PYEOF'\nimport json, math\n\nwith open('/root/symb_invariant_consensus/results/exp070_qwen7b_logiqa200/exp070_results.json') as f:\n    data = json.load(f)\n\nresults = data['results']\nn = len(results)\n\na = sum(1 for x in results if x['sc_correct'] and x['sica_correct'])\nb = sum(1 for x in results if x['sc_correct'] and not x['sica_correct'])\nc = sum(1 for x in results if not x['sc_correct'] and x['sica_correct'])\nd = sum(1 for x in results if not x['sc_correct'] and not x['sica_correct'])\n\nprint(f\"Contingency table: a={a}, b={b}, c={c}, d={d}, n={a+b+c+d}\")\nprint(f\"SC accuracy: {(a+b)/n:.3f}, SICA accuracy: {(a+c)/n:.3f}\")\n\n# McNemar's test\ndisc = b + c\nif disc > 0:\n    chi2 = (abs(b - c) - 1)**2 / disc\nelse:\n    chi2 = 0.0\n\n# Chi-squared CDF approximation (regularized incomplete gamma function)\n# For df=1, chi2 CDF = erf(sqrt(x/2))\ndef erf_approx(x):\n    # Abramowitz and Stegun approximation 7.1.26\n    a1, a2, a3, a4, a5 = 0.254829592, -0.284496736, 1.421413741, -1.453152027, 1.061405429\n    p = 0.3275911\n    sign = 1 if x >= 0 else -1\n    x = abs(x)\n    t = 1.0 / (1.0 + p * x)\n    y = 1.0 - (((((a5*t + a4)*t) + a3)*t + a2)*t + a1)*t * math.exp(-x*x)\n    return sign * y\n\nchi2_cdf = erf_approx(math.sqrt(chi2 / 2))\np_value = 1 - chi2_cdf\n\n# Exact binomial test (two-sided) if b+c < 25\nfrom math import comb\nif disc > 0 and disc < 25:\n    k = min(b, c)\n    p_exact = 2 * sum(comb(disc, i) * (0.5**disc) for i in range(k+1))\n    p_exact = min(p_exact, 1.0)\nelif disc > 0:\n    p_exact = None  # not needed\nelse:\n    p_exact = 1.0\n\n# Cohen's kappa\np_o = (a + d) / n\np_e = ((a+b)/n * (a+c)/n) + ((c+d)/n * (b+d)/n)\nkappa = (p_o - p_e) / (1 - p_e) if p_e < 1 else 0\n\n# Kappa interpretation\nif kappa < 0:\n    interp = \"poor\"\nelif kappa < 0.21:\n    interp = \"slight\"\nelif kappa < 0.41:\n    interp = \"fair\"\nelif kappa < 0.61:\n    interp = \"moderate\"\nelif kappa < 0.81:\n    interp = \"substantial\"\nelse:\n    interp = \"almost_perfect\"\n\nresult = {\n    \"contingency_table\": {\"a\": a, \"b\": b, \"c\": c, \"d\": d},\n    \"n\": n,\n    \"discordant_b\": f\"{b} (SC correct, SICA wrong)\",\n    \"discordant_c\": f\"{c} (SC wrong, SICA correct)\",\n    \"mcnemar_chi2\": round(chi2, 4),\n    \"mcnemar_p\": round(p_value, 6),\n    \"mcnemar_p_exact\": round(p_exact, 6) if p_exact is not None else \"N/A (b+c>=25, use asymptotic)\",\n    \"significant_005\": p_value < 0.05 or (p_exact is not None and p_exact < 0.05),\n    \"cohens_kappa\": round(kappa, 4),\n    \"kappa_interpretation\": interp\n}\n\nprint(json.dumps(result, indent=2))\nPYEOF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp070-mcnemar-kappa_20260519T135944",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "python3 << 'PYEOF'\nimport json, math\n\nwith open('/root/symb_invariant_consensus/results/exp070_qwen7b_logiqa200/exp070_results.json') as f:\n    data = json.load(f)\n\nresults = data['results']\nn = len(results)\n\na = sum(1 for x in results if x['sc_correct'] and x['sica_correct'])\nb = sum(1 for x in results if x['sc_correct'] and not x['sica_correct'])\nc = sum(1 for x in results if not x['sc_correct'] and x['sica_correct'])\nd = sum(1 for x in results if not x['sc_correct'] and not x['sica_correct'])\n\nprint(f\"Contingency table: a={a}, b={b}, c={c}, d={d}, n={a+b+c+d}\")\nprint(f\"SC accuracy: {(a+b)/n:.3f}, SICA accuracy: {(a+c)/n:.3f}\")\n\n# McNemar's test\ndisc = b + c\nif disc > 0:\n    chi2 = (abs(b - c) - 1)**2 / disc\nelse:\n    chi2 = 0.0\n\n# Chi-squared CDF approximation (regularized incomplete gamma function)\n# For df=1, chi2 CDF = erf(sqrt(x/2))\ndef erf_approx(x):\n    # Abramowitz and Stegun approximation 7.1.26\n    a1, a2, a3, a4, a5 = 0.254829592, -0.284496736, 1.421413741, -1.453152027, 1.061405429\n    p = 0.3275911\n    sign = 1 if x >= 0 else -1\n    x = abs(x)\n    t = 1.0 / (1.0 + p * x)\n    y = 1.0 - (((((a5*t + a4)*t) + a3)*t + a2)*t + a1)*t * math.exp(-x*x)\n    return sign * y\n\nchi2_cdf = erf_approx(math.sqrt(chi2 / 2))\np_value = 1 - chi2_cdf\n\n# Exact binomial test (two-sided) if b+c < 25\nfrom math import comb\nif disc > 0 and disc < 25:\n    k = min(b, c)\n    p_exact = 2 * sum(comb(disc, i) * (0.5**disc) for i in range(k+1))\n    p_exact = min(p_exact, 1.0)\nelif disc > 0:\n    p_exact = None  # not needed\nelse:\n    p_exact = 1.0\n\n# Cohen's kappa\np_o = (a + d) / n\np_e = ((a+b)/n * (a+c)/n) + ((c+d)/n * (b+d)/n)\nkappa = (p_o - p_e) / (1 - p_e) if p_e < 1 else 0\n\n# Kappa interpretation\nif kappa < 0:\n    interp = \"poor\"\nelif kappa < 0.21:\n    interp = \"slight\"\nelif kappa < 0.41:\n    interp = \"fair\"\nelif kappa < 0.61:\n    interp = \"moderate\"\nelif kappa < 0.81:\n    interp = \"substantial\"\nelse:\n    interp = \"almost_perfect\"\n\nresult = {\n    \"contingency_table\": {\"a\": a, \"b\": b, \"c\": c, \"d\": d},\n    \"n\": n,\n    \"discordant_b\": f\"{b} (SC correct, SICA wrong)\",\n    \"discordant_c\": f\"{c} (SC wrong, SICA correct)\",\n    \"mcnemar_chi2\": round(chi2, 4),\n    \"mcnemar_p\": round(p_value, 6),\n    \"mcnemar_p_exact\": round(p_exact, 6) if p_exact is not None else \"N/A (b+c>=25, use asymptotic)\",\n    \"significant_005\": p_value < 0.05 or (p_exact is not None and p_exact < 0.05),\n    \"cohens_kappa\": round(kappa, 4),\n    \"kappa_interpretation\": interp\n}\n\nprint(json.dumps(result, indent=2))\nPYEOF"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T14:01:06.316299+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'python3 << \\\\'PYEOF\\\\'\\\\nimport json, math\\\\n\\\\nwith open(\\\\'/root/symb_invariant_consensus/results/exp070_qwen7b_logiqa200/exp070_results.json\\\\') as f:\\\\n    data = json.load(f)\\\\n\\\\nresults = data[\\\\'results\\\\']\\\\nn = len(results)\\\\n\\\\na = sum(1 for x in results if x[\\\\'sc_correct\\\\'] and x[\\\\'sica_correct\\\\'])\\\\nb = sum(1 for x in results if x[\\\\'sc_correct\\\\'] and not x[\\\\'sica_correct\\\\'])\\\\nc = sum(1 for x in results if not x[\\\\'sc_correct\\\\'] and x[\\\\'sica_correct\\\\'])\\\\nd = sum(1 for x in results if not x[\\\\'sc_correct\\\\'] and not x[\\\\'sica_correct\\\\'])\\\\n\\\\nprint(f\\\"Contingency table: a={a}, b={b}, c={c}, d={d}, n={a+b+c+d}\\\")\\\\nprint(f\\\"SC accuracy: {(a+b)/n:.3f}, SICA accuracy: {(a+c)/n:.3f}\\\")\\\\n\\\\n# McNemar\\\\'s test\\\\ndisc = b + c\\\\nif disc > 0:\\\\n    chi2 = (abs(b - c) - 1)**2 / disc\\\\nelse:\\\\n    chi2 = 0.0\\\\n\\\\n# Chi-squared CDF approximation (regularized incomplete gamma function)\\\\n# For df=1, chi2 CDF = erf(sqrt(x/2))\\\\ndef erf_approx(x):\\\\n    # Abramowitz and Stegun approximation 7.1.26\\\\n    a1, a2, a3, a4, a5 = 0.254829592, -0.284496736, 1.421413741, -1.453152027, 1.061405429\\\\n    p = 0.3275911\\\\n    sign = 1 if x >= 0 else -1\\\\n    x = abs(x)\\\\n    t = 1.0 / (1.0 + p * x)\\\\n    y = 1.0 - (((((a5*t + a4)*t) + a3)*t + a2)*t + a1)*t * math.exp(-x*x)\\\\n    return sign * y\\\\n\\\\nchi2_cdf = erf_approx(math.sqrt(chi2 / 2))\\\\np_value = 1 - chi2_cdf\\\\n\\\\n# Exact binomial test (two-sided) if b+c < 25\\\\nfrom math import comb\\\\nif disc > 0 and disc < 25:\\\\n    k = min(b, c)\\\\n    p_exact = 2 * sum(comb(disc, i) * (0.5**disc) for i in range(k+1))\\\\n    p_exact = min(p_exact, 1.0)\\\\nelif disc > 0:\\\\n    p_exact = None  # not needed\\\\nelse:\\\\n    p_exact = 1.0\\\\n\\\\n# Cohen\\\\'s kappa\\\\np_o = (
…[truncated 1353 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp070-mcnemar-kappa_20260519T135944",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T14:01:06.316469+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/miniconda3/bin/python3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp070-mcnemar-kappa_20260519T135944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/miniconda3/bin/python3"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T14:01:06.316596+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/bin/python3\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.05}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp070-mcnemar-kappa_20260519T135944",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T14:01:06.316721+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 << 'PYEOF'\nimport json, math\nfrom math import comb\n\nwith open('/root/symb_invariant_consensus/results/exp070_qwen7b_logiqa200/exp070_results.json') as f:\n    data = json.load(f)\n\nresults = data['results']\nn = len(results)\n\na = sum(1 for x in results if x['sc_correct'] and x['sica_correct'])\nb = sum(1 for x in results if x['sc_correct'] and not x['sica_correct'])\nc = sum(1 for x in results if not x['sc_correct'] and x['sica_correct'])\nd = sum(1 for x in results if not x['sc_correct'] and not x['sica_correct'])\n\nprint(f\"Contingency table: a={a}, b={b}, c={c}, d={d}, n={a+b+c+d}\")\nprint(f\"SC accuracy: {(a+b)/n:.3f}, SICA accuracy: {(a+c)/n:.3f}\")\n\n# McNemar's test\ndisc = b + c\nif disc > 0:\n    chi2_stat = (abs(b - c) - 1)**2 / disc\nelse:\n    chi2_stat = 0.0\n\n# Chi-squared CDF for df=1: P(X<=x) = erf(sqrt(x/2))\ndef erf_approx(x):\n    a1, a2, a3, a4, a5 = 0.254829592, -0.284496736, 1.421413741, -1.453152027, 1.061405429\n    p = 0.3275911\n    sign = 1 if x >= 0 else -1\n    x = abs(x)\n    t = 1.0 / (1.0 + p * x)\n    y = 1.0 - (((((a5*t + a4)*t) + a3)*t + a2)*t + a1)*t * math.exp(-x*x)\n    return sign * y\n\nchi2_cdf = erf_approx(math.sqrt(chi2_stat / 2))\np_value = 1 - chi2_cdf\n\n# Exact binomial test (two-sided)\nif disc > 0:\n    k = min(b, c)\n    p_exact = 2 * sum(comb(disc, i) * (0.5**disc) for i in range(k+1))\n    p_exact = min(p_exact, 1.0)\nelse:\n    p_exact = 1.0\n\n# Cohen's kappa\np_o = (a + d) / n\np_e = ((a+b)/n * (a+c)/n) + ((c+d)/n * (b+d)/n)\nkappa = (p_o - p_e) / (1 - p_e) if p_e < 1 else 0\n\nif kappa < 0: interp = \"poor\"\nelif kappa < 0.21: interp = \"slight\"\nelif kappa < 0.41: interp = \"fair\"\nelif kappa < 0.61: interp = \"moderate\"\nelif kappa < 0.81: interp = \"substantial\"\nelse: interp = \"almost_perfect\"\n\nresult = {\n    \"contingency_table\": {\"a\": a, \"b\": b, \"c\": c, \"d\": d},\n    \"n\": n,\n    \"discordant_b\": f\"{b} (SC correct, SICA wrong)\",\n    \"discordant_c\": f\"{c} (SC wrong, SICA correct)\",\n    \"mcnemar_chi2\": round(chi2_stat, 4),\n    \"mcnemar_p\": round(p_value, 6),\n    \"mcnemar_p_exact\": round(p_exact, 6),\n    \"significant_005\": p_value < 0.05 or p_exact < 0.05,\n    \"cohens_kappa\": round(kappa, 4),\n    \"kappa_interpretation\": interp\n}\n\nprint(json.dumps(result, indent=2))\nPYEOF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp070-mcnemar-kappa_20260519T135944",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 << 'PYEOF'\nimport json, math\nfrom math import comb\n\nwith open('/root/symb_invariant_consensus/results/exp070_qwen7b_logiqa200/exp070_results.json') as f:\n    data = json.load(f)\n\nresults = data['results']\nn = len(results)\n\na = sum(1 for x in results if x['sc_correct'] and x['sica_correct'])\nb = sum(1 for x in results if x['sc_correct'] and not x['sica_correct'])\nc = sum(1 for x in results if not x['sc_correct'] and x['sica_correct'])\nd = sum(1 for x in results if not x['sc_correct'] and not x['sica_correct'])\n\nprint(f\"Contingency table: a={a}, b={b}, c={c}, d={d}, n={a+b+c+d}\")\nprint(f\"SC accuracy: {(a+b)/n:.3f}, SICA accuracy: {(a+c)/n:.3f}\")\n\n# McNemar's test\ndisc = b + c\nif disc > 0:\n    chi2_stat = (abs(b - c) - 1)**2 / disc\nelse:\n    chi2_stat = 0.0\n\n# Chi-squared CDF for df=1: P(X<=x) = erf(sqrt(x/2))\ndef erf_approx(x):\n    a1, a2, a3, a4, a5 = 0.254829592, -0.284496736, 1.421413741, -1.453152027, 1.061405429\n    p = 0.3275911\n    sign = 1 if x >= 0 else -1\n    x = abs(x)\n    t = 1.0 / (1.0 + p * x)\n    y = 1.0 - (((((a5*t + a4)*t) + a3)*t + a2)*t + a1)*t * math.exp(-x*x)\n    return sign * y\n\nchi2_cdf = erf_approx(math.sqrt(chi2_stat / 2))\np_value = 1 - chi2_cdf\n\n# Exact binomial test (two-sided)\nif disc > 0:\n    k = min(b, c)\n    p_exact = 2 * sum(comb(disc, i) * (0.5**disc) for i in range(k+1))\n    p_exact = min(p_exact, 1.0)\nelse:\n    p_exact = 1.0\n\n# Cohen's kappa\np_o = (a + d) / n\np_e = ((a+b)/n * (a+c)/n) + ((c+d)/n * (b+d)/n)\nkappa = (p_o - p_e) / (1 - p_e) if p_e < 1 else 0\n\nif kappa < 0: interp = \"poor\"\nelif kappa < 0.21: interp = \"slight\"\nelif kappa < 0.41: interp = \"fair\"\nelif kappa < 0.61: interp = \"moderate\"\nelif kappa < 0.81: interp = \"substantial\"\nelse: interp = \"almost_perfect\"\n\nresult = {\n    \"contingency_table\": {\"a\": a, \"b\": b, \"c\": c, \"d\": d},\n    \"n\": n,\n    \"discordant_b\": f\"{b} (SC correct, SICA wrong)\",\n    \"discordant_c\": f\"{c} (SC wrong, SICA correct)\",\n    \"mcnemar_chi2\": round(chi2_stat, 4),\n    \"mcnemar_p\": round(p_value, 6),\n    \"mcnemar_p_exact\": round(p_exact, 6),\n    \"significant_005\": p_value < 0.05 or p_exact < 0.05,\n    \"cohens_kappa\": round(kappa, 4),\n    \"kappa_interpretation\": interp\n}\n\nprint(json.dumps(result, indent=2))\nPYEOF"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T14:01:06.316902+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Contingency table: a=136, b=1, c=6, d=57, n=200\\nSC accuracy: 0.685, SICA accuracy: 0.710\\n{\\n  \\\"contingency_table\\\": {\\n    \\\"a\\\": 136,\\n    \\\"b\\\": 1,\\n    \\\"c\\\": 6,\\n    \\\"d\\\": 57\\n  },\\n  \\\"n\\\": 200,\\n  \\\"discordant_b\\\": \\\"1 (SC correct, SICA wrong)\\\",\\n  \\\"discordant_c\\\": \\\"6 (SC wrong, SICA correct)\\\",\\n  \\\"mcnemar_chi2\\\": 2.2857,\\n  \\\"mcnemar_p\\\": 0.13057,\\n  \\\"mcnemar_p_exact\\\": 0.125,\\n  \\\"significant_005\\\": false,\\n  \\\"cohens_kappa\\\": 0.9171,\\n  \\\"kappa_interpretation\\\": \\\"almost_perfect\\\"\\n}\\n\", \"stderr\": \"Error while loading conda entry point: conda-libmamba-solver (module 'libmambapy' has no attribute 'QueryFormat')\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.66}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp070-mcnemar-kappa_20260519T135944",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T14:01:06.317072+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nfrom scipy.stats import chi2, binomtest\nb, c = 1, 6\ndisc = b + c\nchi2_stat = (abs(b-c)-1)**2 / disc\np_asymp = 1 - chi2.cdf(chi2_stat, df=1)\np_exact = binomtest(b, disc, 0.5, alternative='two-sided').pvalue\nprint(f'chi2={chi2_stat:.4f}, p_asymptotic={p_asymp:.6f}, p_exact={p_exact:.6f}')\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp070-mcnemar-kappa_20260519T135944",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nfrom scipy.stats import chi2, binomtest\nb, c = 1, 6\ndisc = b + c\nchi2_stat = (abs(b-c)-1)**2 / disc\np_asymp = 1 - chi2.cdf(chi2_stat, df=1)\np_exact = binomtest(b, disc, 0.5, alternative='two-sided').pvalue\nprint(f'chi2={chi2_stat:.4f}, p_asymptotic={p_asymp:.6f}, p_exact={p_exact:.6f}')\n\""
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T14:01:06.317203+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"chi2=2.2857, p_asymptotic=0.130570, p_exact=0.125000\\n\", \"stderr\": \"Error while loading conda entry point: conda-libmamba-solver (module 'libmambapy' has no attribute 'QueryFormat')\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.21}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp070-mcnemar-kappa_20260519T135944",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-19T14:01:06.317368+00:00_

Scipy 验证通过，数值一致。结果：

```json
{
  "contingency_table": {"a": 136, "b": 1, "c": 6, "d": 57},
  "n": 200,
  "discordant_b": "1 (SC correct, SICA wrong)",
  "discordant_c": "6 (SC wrong, SICA correct)",
  "mcnemar_chi2": 2.2857,
  "mcnemar_p": 0.130570,
  "mcnemar_p_exact": 0.125000,
  "significant_005": false,
  "cohens_kappa": 0.9171,
  "kappa_interpretation": "almost_perfect"
}
```

**关键发现：**

- **Discordant pairs 极少**：仅 7 对 (b=1, c=6)。SICA 翻转了 6 题从错到对，仅丢失 1 题。
- **McNemar's test 不显著**：p=0.131 (asymptotic), p=0.125 (exact binomial)，均 >0.05。discordant pairs 太少，统计功效不足。
- **Cohen's κ=0.917 (almost perfect)**：SC 和 SICA 在 193/200 题上决策一致，两方法高度一致。

Δ=+2.5pp 的改进方向正确（c=6 > b=1），但 n=200 下 discordant pairs 仅 7 对，无法达到统计显著性。需要更大样本量或更多 discordant pairs 才能确认显著性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_exp070-mcnemar-kappa_20260519T135944"
}
```

</details>

---
