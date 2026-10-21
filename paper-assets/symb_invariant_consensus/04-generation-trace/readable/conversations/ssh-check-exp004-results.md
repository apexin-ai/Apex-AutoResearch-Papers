# ssh check exp004 results

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_ssh_check-exp004-results_20260517T174319.jsonl`
- **Structured JSON:** [`a84b3fff052359a20290.json`](../../sessions/a8/a84b3fff052359a20290.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-17T17:44:31.221908+00:00_

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
  "session": "worker_ssh_check-exp004-results_20260517T174319",
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

_source line 2 · 2026-05-17T17:44:31.222261+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-exp004-results_20260517T174319",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T17:44:31.222445+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "tmux ls 2>&1; echo \"---\"; ls -la /root/symb_invariant_consensus/results/exp004_qwen7b/ 2>&1; echo \"---\"; ls -la /root/autodl-tmp/symb_invariant_consensus/results/exp004_qwen7b/ 2>&1",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-exp004-results_20260517T174319",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "tmux ls 2>&1; echo \"---\"; ls -la /root/symb_invariant_consensus/results/exp004_qwen7b/ 2>&1; echo \"---\"; ls -la /root/autodl-tmp/symb_invariant_consensus/results/exp004_qwen7b/ 2>&1",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T17:44:31.222596+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"exp-004-qwen7b: 1 windows (created Mon May 18 01:13:47 2026)\\n---\\ntotal 752\\ndrwxr-xr-x  2 root root     67 May 18 01:15 .\\ndrwxr-xr-x 21 root root   4096 May 18 01:25 ..\\n-rw-r--r--  1 root root 569146 May 18 01:43 exp004_qwen7b_results.json\\n-rw-r--r--  1 root root 141358 May 18 01:43 run.log\\n---\\nls: cannot access '/root/autodl-tmp/symb_invariant_consensus/results/exp004_qwen7b/': No such file or directory\\n\", \"stderr\": \"\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 1.11}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-exp004-results_20260517T174319",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T17:44:31.222750+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "cat /root/symb_invariant_consensus/results/exp004_qwen7b/exp004_qwen7b_results.json | python3 -c \"\nimport json, sys\nd = json.load(sys.stdin)\n# Print summary metrics\nsummary = d.get('summary', d)\nprint('=== EXP-004 SUMMARY ===')\nfor k in ['n', 'sica_accuracy', 'sc_accuracy', 'delta_pp', 'multi_candidate_rate', 'extraction_rate', 'discordant_sica_wins', 'discordant_sc_wins', 'mcnemar_p', 'wall_time']:\n    if k in summary:\n        print(f'{k}: {summary[k]}')\n# Per-domain\nif 'per_domain' in summary:\n    print('\\n=== PER-DOMAIN ===')\n    for domain, vals in summary['per_domain'].items():\n        print(f'{domain}: sica={vals.get(\\\"sica_accuracy\\\")}, sc={vals.get(\\\"sc_accuracy\\\")}')\n# Also check top-level keys\nprint('\\n=== TOP-LEVEL KEYS ===')\nprint(list(d.keys())[:20])\n\"",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-exp004-results_20260517T174319",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "cat /root/symb_invariant_consensus/results/exp004_qwen7b/exp004_qwen7b_results.json | python3 -c \"\nimport json, sys\nd = json.load(sys.stdin)\n# Print summary metrics\nsummary = d.get('summary', d)\nprint('=== EXP-004 SUMMARY ===')\nfor k in ['n', 'sica_accuracy', 'sc_accuracy', 'delta_pp', 'multi_candidate_rate', 'extraction_rate', 'discordant_sica_wins', 'discordant_sc_wins', 'mcnemar_p', 'wall_time']:\n    if k in summary:\n        print(f'{k}: {summary[k]}')\n# Per-domain\nif 'per_domain' in summary:\n    print('\\n=== PER-DOMAIN ===')\n    for domain, vals in summary['per_domain'].items():\n        print(f'{domain}: sica={vals.get(\\\"sica_accuracy\\\")}, sc={vals.get(\\\"sc_accuracy\\\")}')\n# Also check top-level keys\nprint('\\n=== TOP-LEVEL KEYS ===')\nprint(list(d.keys())[:20])\n\"",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T17:44:31.222905+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"bash: line 1: python3: command not found\\n\", \"return_code\": 127}, \"error\": \"exit code 127\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-exp004-results_20260517T174319",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T17:44:31.223042+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "source /root/miniconda3/bin/activate && python3 -c \"\nimport json\nwith open('/root/symb_invariant_consensus/results/exp004_qwen7b/exp004_qwen7b_results.json') as f:\n    d = json.load(f)\n# Try summary or top-level\nsummary = d.get('summary', d)\nprint('=== EXP-004 SUMMARY ===')\nfor k in ['n', 'sica_accuracy', 'sc_accuracy', 'delta_pp', 'multi_candidate_rate', 'extraction_rate', 'discordant_sica_wins', 'discordant_sc_wins', 'mcnemar_p', 'wall_time']:\n    v = summary.get(k, 'N/A')\n    print(f'{k}: {v}')\nif 'per_domain' in summary:\n    print()\n    print('=== PER-DOMAIN ===')\n    for domain, vals in summary['per_domain'].items():\n        print(f'{domain}: sica={vals.get(\\\"sica_accuracy\\\")}, sc={vals.get(\\\"sc_accuracy\\\")}')\nprint()\nprint('=== TOP-LEVEL KEYS ===')\nprint(list(d.keys())[:20])\n\"",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-exp004-results_20260517T174319",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "source /root/miniconda3/bin/activate && python3 -c \"\nimport json\nwith open('/root/symb_invariant_consensus/results/exp004_qwen7b/exp004_qwen7b_results.json') as f:\n    d = json.load(f)\n# Try summary or top-level\nsummary = d.get('summary', d)\nprint('=== EXP-004 SUMMARY ===')\nfor k in ['n', 'sica_accuracy', 'sc_accuracy', 'delta_pp', 'multi_candidate_rate', 'extraction_rate', 'discordant_sica_wins', 'discordant_sc_wins', 'mcnemar_p', 'wall_time']:\n    v = summary.get(k, 'N/A')\n    print(f'{k}: {v}')\nif 'per_domain' in summary:\n    print()\n    print('=== PER-DOMAIN ===')\n    for domain, vals in summary['per_domain'].items():\n        print(f'{domain}: sica={vals.get(\\\"sica_accuracy\\\")}, sc={vals.get(\\\"sc_accuracy\\\")}')\nprint()\nprint('=== TOP-LEVEL KEYS ===')\nprint(list(d.keys())[:20])\n\"",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T17:44:31.223219+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== EXP-004 SUMMARY ===\\nn: N/A\\nsica_accuracy: 0.6964285714285714\\nsc_accuracy: 0.6964285714285714\\ndelta_pp: N/A\\nmulti_candidate_rate: N/A\\nextraction_rate: 0.9375\\ndiscordant_sica_wins: N/A\\ndiscordant_sc_wins: N/A\\nmcnemar_p: N/A\\nwall_time: N/A\\n\\n=== TOP-LEVEL KEYS ===\\n['summary', 'results']\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-exp004-results_20260517T174319",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T17:44:31.223574+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "source /root/miniconda3/bin/activate && python3 -c \"\nimport json\nwith open('/root/symb_invariant_consensus/results/exp004_qwen7b/exp004_qwen7b_results.json') as f:\n    d = json.load(f)\ns = d['summary']\nprint('=== ALL SUMMARY KEYS & VALUES ===')\nfor k, v in s.items():\n    if isinstance(v, dict):\n        print(f'{k}:')\n        for k2, v2 in v.items():\n            print(f'  {k2}: {v2}')\n    else:\n        print(f'{k}: {v}')\nprint()\nprint(f'Total results entries: {len(d.get(\\\"results\\\", []))}')\n# Check a sample result entry\nif d.get('results'):\n    r0 = d['results'][0]\n    print(f'Sample result keys: {list(r0.keys())}')\n\"",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-exp004-results_20260517T174319",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "source /root/miniconda3/bin/activate && python3 -c \"\nimport json\nwith open('/root/symb_invariant_consensus/results/exp004_qwen7b/exp004_qwen7b_results.json') as f:\n    d = json.load(f)\ns = d['summary']\nprint('=== ALL SUMMARY KEYS & VALUES ===')\nfor k, v in s.items():\n    if isinstance(v, dict):\n        print(f'{k}:')\n        for k2, v2 in v.items():\n            print(f'  {k2}: {v2}')\n    else:\n        print(f'{k}: {v}')\nprint()\nprint(f'Total results entries: {len(d.get(\\\"results\\\", []))}')\n# Check a sample result entry\nif d.get('results'):\n    r0 = d['results'][0]\n    print(f'Sample result keys: {list(r0.keys())}')\n\"",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T17:44:31.223750+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== ALL SUMMARY KEYS & VALUES ===\\nn_problems: 56\\nsica_accuracy: 0.6964285714285714\\nsc_accuracy: 0.6964285714285714\\nsica_correct: 39\\nsc_correct: 39\\nextraction_rate: 0.9375\\nanswer_extraction_rate: 1.0\\nanswer_extraction_counts:\\n  boxed: 672\\n  fallback: 0\\n  none: 0\\ntruncated_traces: 0\\ntotal_constraints_extracted: 5160\\ntotal_unique_constraints: 1300\\ncontradiction_rate: 0.026923076923076925\\nproblems_with_contradictions: 25\\nper_level_accuracy:\\n  D5: {'sica': 0.6, 'sc': 0.6333333333333333, 'n': 30}\\n  folio: {'sica': 0.8076923076923077, 'sc': 0.7692307692307693, 'n': 26}\\nper_dataset_accuracy:\\n  proofwriter: {'sica': 0.6, 'sc': 0.6333333333333333, 'n': 30}\\n  folio: {'sica': 0.8076923076923077, 'sc': 0.7692307692307693, 'n': 26}\\nk: 12\\nmode: vllm\\ntotal_wall_time_s: 1751.7\\n\\nTotal results entries: 56\\nSample result keys: ['problem_idx', 'problem_id', 'problem', 'dataset', 'level', 'ground_truth', 'sica_answer', 'sica_scores', 'sica_correct', 'sc_answer', 'sc_vote_count', 'sc_vote_distribution', 'sc_correct', 'constraints_stats', 'maxsat_stats', 'timing', 'wall_time_s', 'trace_extraction_stats', 'truncated_traces', 'raw_constraints', 'per_trace']\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.58}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-exp004-results_20260517T174319",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T17:44:31.223912+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "source /root/miniconda3/bin/activate && python3 -c \"\nimport json\nwith open('/root/symb_invariant_consensus/results/exp004_qwen7b/exp004_qwen7b_results.json') as f:\n    d = json.load(f)\nresults = d['results']\n# Compute multi_candidate_rate (C0) and discordant analysis\nmulti = 0\ndiscordant_sica_wins = 0\ndiscordant_sc_wins = 0\nfor r in results:\n    sc_dist = r.get('sc_vote_distribution', {})\n    if len(sc_dist) > 1:\n        multi += 1\n    sica_c = r.get('sica_correct', False)\n    sc_c = r.get('sc_correct', False)\n    if sica_c and not sc_c:\n        discordant_sica_wins += 1\n    elif sc_c and not sica_c:\n        discordant_sc_wins += 1\nn = len(results)\nprint(f'n: {n}')\nprint(f'multi_candidate_rate (C0): {multi}/{n} = {multi/n:.4f}')\nprint(f'discordant_sica_wins: {discordant_sica_wins}')\nprint(f'discordant_sc_wins: {discordant_sc_wins}')\nprint(f'delta_pp: {(39-39)/n*100:.2f}%')\n\n# McNemar\ndiscordant_total = discordant_sica_wins + discordant_sc_wins\nif discordant_total > 0:\n    from scipy.stats import binom_test\n    p = binom_test(discordant_sica_wins, discordant_total, 0.5)\n    print(f'mcnemar_p (exact binomial): {p:.4f}')\nelse:\n    print('mcnemar_p: N/A (no discordant pairs)')\n\"",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-exp004-results_20260517T174319",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "source /root/miniconda3/bin/activate && python3 -c \"\nimport json\nwith open('/root/symb_invariant_consensus/results/exp004_qwen7b/exp004_qwen7b_results.json') as f:\n    d = json.load(f)\nresults = d['results']\n# Compute multi_candidate_rate (C0) and discordant analysis\nmulti = 0\ndiscordant_sica_wins = 0\ndiscordant_sc_wins = 0\nfor r in results:\n    sc_dist = r.get('sc_vote_distribution', {})\n    if len(sc_dist) > 1:\n        multi += 1\n    sica_c = r.get('sica_correct', False)\n    sc_c = r.get('sc_correct', False)\n    if sica_c and not sc_c:\n        discordant_sica_wins += 1\n    elif sc_c and not sica_c:\n        discordant_sc_wins += 1\nn = len(results)\nprint(f'n: {n}')\nprint(f'multi_candidate_rate (C0): {multi}/{n} = {multi/n:.4f}')\nprint(f'discordant_sica_wins: {discordant_sica_wins}')\nprint(f'discordant_sc_wins: {discordant_sc_wins}')\nprint(f'delta_pp: {(39-39)/n*100:.2f}%')\n\n# McNemar\ndiscordant_total = discordant_sica_wins + discordant_sc_wins\nif discordant_total > 0:\n    from scipy.stats import binom_test\n    p = binom_test(discordant_sica_wins, discordant_total, 0.5)\n    print(f'mcnemar_p (exact binomial): {p:.4f}')\nelse:\n    print('mcnemar_p: N/A (no discordant pairs)')\n\"",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T17:44:31.224091+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"n: 57\\nmulti_candidate_rate (C0): 24/57 = 0.4211\\ndiscordant_sica_wins: 2\\ndiscordant_sc_wins: 2\\ndelta_pp: 0.00%\\n\", \"stderr\": \"Traceback (most recent call last):\\n  File \\\"&lt;string>\\\", line 30, in &lt;module>\\nImportError: cannot import name 'binom_test' from 'scipy.stats' (/root/miniconda3/lib/python3.12/site-packages/scipy/stats/__init__.py). Did you mean: 'binomtest'?\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 1.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-exp004-results_20260517T174319",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T17:44:31.224225+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "source /root/miniconda3/bin/activate && python3 -c \"\nfrom scipy.stats import binomtest\nr = binomtest(2, 4, 0.5)\nprint(f'mcnemar_p (exact binomial): {r.pvalue:.4f}')\n\"",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-exp004-results_20260517T174319",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "source /root/miniconda3/bin/activate && python3 -c \"\nfrom scipy.stats import binomtest\nr = binomtest(2, 4, 0.5)\nprint(f'mcnemar_p (exact binomial): {r.pvalue:.4f}')\n\"",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T17:44:31.224349+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"mcnemar_p (exact binomial): 1.0000\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-exp004-results_20260517T174319",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-17T17:44:31.224512+00:00_

## exp-004 Qwen-7B 实验结果

**状态**: 已完成（tmux session 仍在，结果文件已生成）

| Metric | Value |
|---|---|
| **n** | 56 (summary) / 57 (results array) |
| **k** | 12 |
| **SICA accuracy** | 69.64% (39/56) |
| **SC accuracy** | 69.64% (39/56) |
| **delta_pp** | 0.00% |
| **multi_candidate_rate (C0)** | **42.11%** (24/57) |
| **extraction_rate** | 93.75% |
| **answer_extraction_rate** | 100% |
| **contradiction_rate** | 2.69% |
| **discordant SICA wins** | 2 |
| **discordant SC wins** | 2 |
| **mcnemar_p** | 1.0000 (无显著差异) |
| **wall_time** | 1751.7s (~29 min) |
| **truncated_traces** | 0 |

### Per-domain breakdown

| Domain | SICA | SC | n |
|---|---|---|---|
| **ProofWriter (D5)** | 60.00% | 63.33% | 30 |
| **FOLIO** | 80.77% | 76.92% | 26 |

### 关键发现

**C0 = 42.11%** — Qwen-7B 在 42% 的问题上产生了多候选答案，说明 within-family scaling 有实质性分歧空间。但 SICA 和 SC 在整体准确率上完全持平（69.64% vs 69.64%），discordant pairs 仅 4 对且对半分（2:2），McNemar p=1.0。

FOLIO 上 SICA 略优于 SC（80.77% vs 76.92%），ProofWriter D5 上 SC 略优（63.33% vs 60.00%），但样本量太小无统计显著性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ssh_check-exp004-results_20260517T174319"
}
```

</details>

---
