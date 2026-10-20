# analysis exp010 mistral v3 results

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_analysis_exp010-mistral-v3-results_20260517T081841.jsonl`
- **Structured JSON:** [`50bbc980fe8bc4cdb32b.json`](../../sessions/50/50bbc980fe8bc4cdb32b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-17T08:20:22.739519+00:00_

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
  "session": "worker_analysis_exp010-mistral-v3-results_20260517T081841",
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

_source line 2 · 2026-05-17T08:20:22.739922+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp010-mistral-v3-results_20260517T081841",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T08:20:22.740114+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "find /root/symb_invariant_consensus/results -name \"*mistral*\" -o -name \"*exp010*\" 2>/dev/null; echo \"---\"; ls ~/runs/symb_invariant_consensus/ 2>/dev/null | grep -i mistral",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp010-mistral-v3-results_20260517T081841",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "find /root/symb_invariant_consensus/results -name \"*mistral*\" -o -name \"*exp010*\" 2>/dev/null; echo \"---\"; ls ~/runs/symb_invariant_consensus/ 2>/dev/null | grep -i mistral",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T08:20:22.740270+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/results/exp010_mistral\\n/root/symb_invariant_consensus/results/exp010_mistral/exp010_results.json\\n---\\nexp-010-mistral-v2.log\\nexp-010-mistral-v3.log\\nexp-010-mistral.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.94}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp010-mistral-v3-results_20260517T081841",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T08:20:22.740401+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "cat /root/symb_invariant_consensus/results/exp010_mistral/exp010_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp010-mistral-v3-results_20260517T081841",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "cat /root/symb_invariant_consensus/results/exp010_mistral/exp010_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T08:20:22.740763+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n_problems\\\": 60,\\n    \\\"sica_accuracy\\\": 0.48333333333333334,\\n    \\\"sc_accuracy\\\": 0.48333333333333334,\\n    \\\"sica_correct\\\": 29,\\n    \\\"sc_correct\\\": 29,\\n    \\\"extraction_rate\\\": 0.8819444444444444,\\n    \\\"answer_extraction_rate\\\": 1.0,\\n    \\\"answer_extraction_counts\\\": {\\n      \\\"boxed\\\": 720,\\n      \\\"fallback\\\": 0,\\n      \\\"none\\\": 0\\n    },\\n    \\\"truncated_traces\\\": 0,\\n    \\\"total_constraints_extracted\\\": 3939,\\n    \\\"total_unique_constraints\\\": 1228,\\n    \\\"contradiction_rate\\\": 0.05618892508143322,\\n    \\\"problems_with_contradictions\\\": 38,\\n    \\\"per_level_accuracy\\\": {\\n      \\\"D5\\\": {\\n        \\\"sica\\\": 0.4,\\n        \\\"sc\\\": 0.4,\\n        \\\"n\\\": 30\\n      },\\n      \\\"folio\\\": {\\n        \\\"sica\\\": 0.5666666666666667,\\n        \\\"sc\\\": 0.5666666666666667,\\n        \\\"n\\\": 30\\n      }\\n    },\\n    \\\"per_dataset_accuracy\\\": {\\n      \\\"proofwriter\\\": {\\n        \\\"sica\\\": 0.4,\\n        \\\"sc\\\": 0.4,\\n        \\\"n\\\": 30\\n      },\\n      \\\"folio\\\": {\\n        \\\"sica\\\": 0.5666666666666667,\\n        \\\"sc\\\": 0.5666666666666667,\\n        \\\"n\\\": 30\\n      }\\n    },\\n    \\\"k\\\": 12,\\n    \\\"mode\\\": \\\"vllm\\\",\\n    \\\"total_wall_time_s\\\": 1161.0\\n  },\\n  \\\"results\\\": [\\n    {\\n      \\\"problem_idx\\\": 0,\\n      \\\"problem_id\\\": \\\"ProofWriter_AttNeg-OWA-D5-979_Q9\\\",\\n      \\\"problem\\\": \\\"Given the following facts and rules:\\\\nCharlie is red. Dave is red. Dave is rough. Dave is round. Dave is young. Fiona is quiet. Fiona is red. Harry is furry. Harry is kind. Harry is young. All rough things are round. All rough things are round. All round, rough things are young. All red things are young. If Fiona is young and Fiona is not furry then Fiona is kind. If something is fur
…[truncated 8331 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp010-mistral-v3-results_20260517T081841",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T08:20:22.741042+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "cd /root/symb_invariant_consensus && python3 -c \"\nimport json\nwith open('results/exp010_mistral/exp010_results.json') as f:\n    data = json.load(f)\n\nresults = data['results']\ndiscordant_sica_wins = 0\ndiscordant_sc_wins = 0\nmulti_candidate = 0\n\nfor r in results:\n    if r['sica_correct'] and not r['sc_correct']:\n        discordant_sica_wins += 1\n    elif r['sc_correct'] and not r['sica_correct']:\n        discordant_sc_wins += 1\n    # multi_candidate: sica chose differently from sc (or had multiple viable candidates)\n    if r['sica_answer'] != r['sc_answer']:\n        multi_candidate += 1\n\nprint(f'discordant_sica_wins: {discordant_sica_wins}')\nprint(f'discordant_sc_wins: {discordant_sc_wins}')\nprint(f'multi_candidate_rate: {multi_candidate}/{len(results)} = {multi_candidate/len(results)*100:.2f}%')\nprint(f'n: {len(results)}')\n\n# Also check sc_vote_distribution to see how many had non-unanimous votes\nnon_unanimous = sum(1 for r in results if len(r.get('sc_vote_distribution', {})) > 1)\nprint(f'non_unanimous_sc_votes: {non_unanimous}/{len(results)}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp010-mistral-v3-results_20260517T081841",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "cd /root/symb_invariant_consensus && python3 -c \"\nimport json\nwith open('results/exp010_mistral/exp010_results.json') as f:\n    data = json.load(f)\n\nresults = data['results']\ndiscordant_sica_wins = 0\ndiscordant_sc_wins = 0\nmulti_candidate = 0\n\nfor r in results:\n    if r['sica_correct'] and not r['sc_correct']:\n        discordant_sica_wins += 1\n    elif r['sc_correct'] and not r['sica_correct']:\n        discordant_sc_wins += 1\n    # multi_candidate: sica chose differently from sc (or had multiple viable candidates)\n    if r['sica_answer'] != r['sc_answer']:\n        multi_candidate += 1\n\nprint(f'discordant_sica_wins: {discordant_sica_wins}')\nprint(f'discordant_sc_wins: {discordant_sc_wins}')\nprint(f'multi_candidate_rate: {multi_candidate}/{len(results)} = {multi_candidate/len(results)*100:.2f}%')\nprint(f'n: {len(results)}')\n\n# Also check sc_vote_distribution to see how many had non-unanimous votes\nnon_unanimous = sum(1 for r in results if len(r.get('sc_vote_distribution', {})) > 1)\nprint(f'non_unanimous_sc_votes: {non_unanimous}/{len(results)}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T08:20:22.741236+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/symb_invariant_consensus && python3 -c \\\"\\\\nimport json\\\\nwith open(\\\\'results/exp010_mistral/exp010_results.json\\\\') as f:\\\\n    data = json.load(f)\\\\n\\\\nresults = data[\\\\'results\\\\']\\\\ndiscordant_sica_wins = 0\\\\ndiscordant_sc_wins = 0\\\\nmulti_candidate = 0\\\\n\\\\nfor r in results:\\\\n    if r[\\\\'sica_correct\\\\'] and not r[\\\\'sc_correct\\\\']:\\\\n        discordant_sica_wins += 1\\\\n    elif r[\\\\'sc_correct\\\\'] and not r[\\\\'sica_correct\\\\']:\\\\n        discordant_sc_wins += 1\\\\n    # multi_candidate: sica chose differently from sc (or had multiple viable candidates)\\\\n    if r[\\\\'sica_answer\\\\'] != r[\\\\'sc_answer\\\\']:\\\\n        multi_candidate += 1\\\\n\\\\nprint(f\\\\'discordant_sica_wins: {discordant_sica_wins}\\\\')\\\\nprint(f\\\\'discordant_sc_wins: {discordant_sc_wins}\\\\')\\\\nprint(f\\\\'multi_candidate_rate: {multi_candidate}/{len(results)} = {multi_candidate/len(results)*100:.2f}%\\\\')\\\\nprint(f\\\\'n: {len(results)}\\\\')\\\\n\\\\n# Also check sc_vote_distribution to see how many had non-unanimous votes\\\\nnon_unanimous = sum(1 for r in results if len(r.get(\\\\'sc_vote_distribution\\\\', {})) > 1)\\\\nprint(f\\\\'non_unanimous_sc_votes: {non_unanimous}/{len(results)}\\\\')\\\\n\\\"\\\\n'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 1.09}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp010-mistral-v3-results_20260517T081841",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T08:20:22.741387+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && python -c \"\nimport json\nwith open('results/exp010_mistral/exp010_results.json') as f:\n    data = json.load(f)\n\nresults = data['results']\ndiscordant_sica_wins = 0\ndiscordant_sc_wins = 0\nmulti_candidate = 0\n\nfor r in results:\n    if r['sica_correct'] and not r['sc_correct']:\n        discordant_sica_wins += 1\n    elif r['sc_correct'] and not r['sica_correct']:\n        discordant_sc_wins += 1\n    if r['sica_answer'] != r['sc_answer']:\n        multi_candidate += 1\n\nprint(f'discordant_sica_wins: {discordant_sica_wins}')\nprint(f'discordant_sc_wins: {discordant_sc_wins}')\nprint(f'multi_candidate_rate: {multi_candidate}/{len(results)} = {multi_candidate/len(results)*100:.2f}%')\nprint(f'n: {len(results)}')\n\nnon_unanimous = sum(1 for r in results if len(r.get('sc_vote_distribution', {})) > 1)\nprint(f'non_unanimous_sc_votes: {non_unanimous}/{len(results)}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp010-mistral-v3-results_20260517T081841",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && python -c \"\nimport json\nwith open('results/exp010_mistral/exp010_results.json') as f:\n    data = json.load(f)\n\nresults = data['results']\ndiscordant_sica_wins = 0\ndiscordant_sc_wins = 0\nmulti_candidate = 0\n\nfor r in results:\n    if r['sica_correct'] and not r['sc_correct']:\n        discordant_sica_wins += 1\n    elif r['sc_correct'] and not r['sica_correct']:\n        discordant_sc_wins += 1\n    if r['sica_answer'] != r['sc_answer']:\n        multi_candidate += 1\n\nprint(f'discordant_sica_wins: {discordant_sica_wins}')\nprint(f'discordant_sc_wins: {discordant_sc_wins}')\nprint(f'multi_candidate_rate: {multi_candidate}/{len(results)} = {multi_candidate/len(results)*100:.2f}%')\nprint(f'n: {len(results)}')\n\nnon_unanimous = sum(1 for r in results if len(r.get('sc_vote_distribution', {})) > 1)\nprint(f'non_unanimous_sc_votes: {non_unanimous}/{len(results)}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T08:20:22.741545+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"discordant_sica_wins: 2\\ndiscordant_sc_wins: 2\\nmulti_candidate_rate: 4/60 = 6.67%\\nn: 60\\nnon_unanimous_sc_votes: 30/60\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.8}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp010-mistral-v3-results_20260517T081841",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T08:20:22.741697+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "tail -100 ~/runs/symb_invariant_consensus/exp-010-mistral-v3.log 2>/dev/null | grep -iE \"mcnemar|p.value|truncat|error|WARNING|FAIL\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp010-mistral-v3-results_20260517T081841",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "tail -100 ~/runs/symb_invariant_consensus/exp-010-mistral-v3.log 2>/dev/null | grep -iE \"mcnemar|p.value|truncat|error|WARNING|FAIL\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T08:20:22.741827+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  Answers: boxed=12 fallback=0 none=0 truncated=0\\n  Answers: boxed=12 fallback=0 none=0 truncated=0\\n  Answers: boxed=12 fallback=0 none=0 truncated=0\\nTruncated traces: 0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.14}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp010-mistral-v3-results_20260517T081841",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T08:20:22.742015+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"\nfrom scipy.stats import binom_test\n# McNemar: discordant pairs sica_wins=2, sc_wins=2\n# two-sided binomial test\np = binom_test(2, 4, 0.5)\nprint(f'McNemar p-value: {p:.4f}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp010-mistral-v3-results_20260517T081841",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"\nfrom scipy.stats import binom_test\n# McNemar: discordant pairs sica_wins=2, sc_wins=2\n# two-sided binomial test\np = binom_test(2, 4, 0.5)\nprint(f'McNemar p-value: {p:.4f}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T08:20:22.742163+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \\\"\\\\nfrom scipy.stats import binom_test\\\\n# McNemar: discordant pairs sica_wins=2, sc_wins=2\\\\n# two-sided binomial test\\\\np = binom_test(2, 4, 0.5)\\\\nprint(f\\\\'McNemar p-value: {p:.4f}\\\\')\\\\n\\\"\\\\n'\\n\\nExit code: 1\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nTraceback (most recent call last):\\n  File \\\"&lt;string>\\\", line 2, in &lt;module>\\nImportError: cannot import name 'binom_test' from 'scipy.stats' (/root/miniconda3/lib/python3.12/site-packages/scipy/stats/__init__.py). Did you mean: 'binomtest'?\\n\\n\", \"metadata\": {\"elapsed_seconds\": 2.84}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp010-mistral-v3-results_20260517T081841",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-17T08:20:22.742342+00:00_

McNemar with 2 vs 2 discordant pairs gives p=1.0 (exact binomial). All metrics collected.

```
METRICS:
- n: 60
- sica_accuracy: 48.33%
- sc_accuracy: 48.33%
- delta_pp: +0.00pp
- multi_candidate_rate: 6.67% (4/60)
- extraction_rate: 88.19%
- discordant_sica_wins: 2
- discordant_sc_wins: 2
- proofwriter: sica=40.00%, sc=40.00%, gap=0pp
- folio: sica=56.67%, sc=56.67%, gap=0pp
- McNemar p-value: 1.000 (2 vs 2 discordant, trivially non-significant)
- truncated_traces: 0
- answer_extraction_rate: 100% (all boxed, 0 fallback, 0 none)
- contradiction_rate: 5.62%
- k: 12

CONCLUSION: negative
NOTE: SC accuracy 48.33% > 40% threshold but SICA provides zero lift (delta=0.00pp). Only 4/60 problems (6.67%) had SICA disagree with SC, and those split evenly 2-2. Model too weak for constraint extraction to be meaningful — non-unanimous SC votes in 30/60 problems but SICA only reranked 4, indicating extracted constraints rarely had enough signal to override majority vote.
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_exp010-mistral-v3-results_20260517T081841"
}
```

</details>

---
