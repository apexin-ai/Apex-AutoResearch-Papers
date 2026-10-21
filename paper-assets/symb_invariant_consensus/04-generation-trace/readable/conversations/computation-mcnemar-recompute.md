# computation mcnemar recompute

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 75
- **Recorded user turns:** 0
- **Tool calls:** 37
- **Original source:** `logs/chats/worker_computation_mcnemar-recompute_20260519T061929.jsonl`
- **Structured JSON:** [`c8e0dfd888d2e066ae2f.json`](../../sessions/c8/c8e0dfd888d2e066ae2f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

75 recorded events

### Tool call

_source line 1 · 2026-05-19T06:27:42.700785+00:00_

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
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
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

_source line 2 · 2026-05-19T06:27:42.701209+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T06:27:42.701445+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/symb_invariant_consensus/baselines/self_consistency.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/symb_invariant_consensus/baselines/self_consistency.py"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-19T06:27:42.701672+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "cat /root/symb_invariant_consensus/sc_tiebreak_revalidation_25068.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "cat /root/symb_invariant_consensus/sc_tiebreak_revalidation_25068.json"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T06:27:42.701869+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/symb_invariant_consensus/experiments/exp-033-mistral-folio204/results/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/symb_invariant_consensus/experiments/exp-033-mistral-folio204/results/"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T06:27:42.702100+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/baselines/self_consistency.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.11}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-19T06:27:42.702299+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"cat: /root/symb_invariant_consensus/sc_tiebreak_revalidation_25068.json: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 1.28}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T06:27:42.702494+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/symb_invariant_consensus/experiments/exp-033-mistral-folio204/results/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 1.29}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T06:27:42.702682+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "find /root/symb_invariant_consensus -name \"sc_tiebreak*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "find /root/symb_invariant_consensus -name \"sc_tiebreak*\" -type f"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-19T06:27:42.702894+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/symb_invariant_consensus/experiments/exp-033-mistral-folio204/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/symb_invariant_consensus/experiments/exp-033-mistral-folio204/"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-19T06:27:42.703105+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/results/sc_tiebreak_revalidation_25068.json\\n/root/symb_invariant_consensus/sc_tiebreak_revalidation.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.18}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T06:27:42.703312+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/symb_invariant_consensus/experiments/exp-033-mistral-folio204/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 48.33}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T06:27:42.703503+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "cat /root/symb_invariant_consensus/results/sc_tiebreak_revalidation_25068.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "cat /root/symb_invariant_consensus/results/sc_tiebreak_revalidation_25068.json"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-19T06:27:42.703692+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/symb_invariant_consensus/experiments/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/symb_invariant_consensus/experiments/"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-19T06:27:42.704333+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": [\\n    {\\n      \\\"exp_id\\\": \\\"exp-033\\\",\\n      \\\"label\\\": \\\"Mistral-7B FOLIO-204 seed=42 T=0.7 K=12\\\",\\n      \\\"model\\\": \\\"Mistral-7B\\\",\\n      \\\"dataset\\\": \\\"FOLIO-204\\\",\\n      \\\"n\\\": 204,\\n      \\\"registry_sc\\\": 54.41,\\n      \\\"old_sc_pct\\\": 54.41,\\n      \\\"new_sc_pct\\\": 55.88,\\n      \\\"change\\\": 1.47,\\n      \\\"sica_pct\\\": 59.31,\\n      \\\"old_delta_pp\\\": 4.9,\\n      \\\"new_delta_pp\\\": 3.43,\\n      \\\"n_affected\\\": 7\\n    },\\n    {\\n      \\\"exp_id\\\": \\\"exp-057\\\",\\n      \\\"label\\\": \\\"Mistral-7B FOLIO-204 T=0.3\\\",\\n      \\\"model\\\": \\\"Mistral-7B\\\",\\n      \\\"dataset\\\": \\\"FOLIO-204\\\",\\n      \\\"n\\\": 204,\\n      \\\"registry_sc\\\": 57.35,\\n      \\\"old_sc_pct\\\": 57.35,\\n      \\\"new_sc_pct\\\": 58.33,\\n      \\\"change\\\": 0.98,\\n      \\\"sica_pct\\\": 56.86,\\n      \\\"old_delta_pp\\\": -0.49,\\n      \\\"new_delta_pp\\\": -1.47,\\n      \\\"n_affected\\\": 6\\n    },\\n    {\\n      \\\"exp_id\\\": \\\"exp-058\\\",\\n      \\\"label\\\": \\\"Mistral-7B FOLIO-204 T=0.5\\\",\\n      \\\"model\\\": \\\"Mistral-7B\\\",\\n      \\\"dataset\\\": \\\"FOLIO-204\\\",\\n      \\\"n\\\": 204,\\n      \\\"registry_sc\\\": 57.84,\\n      \\\"old_sc_pct\\\": 57.84,\\n      \\\"new_sc_pct\\\": 58.33,\\n      \\\"change\\\": 0.49,\\n      \\\"sica_pct\\\": 57.35,\\n      \\\"old_delta_pp\\\": -0.49,\\n      \\\"new_delta_pp\\\": -0.98,\\n      \\\"n_affected\\\": 3\\n    },\\n    {\\n      \\\"exp_id\\\": \\\"exp-054\\\",\\n      \\\"label\\\": \\\"Mistral-7B FOLIO-204 T=1.0\\\",\\n      \\\"model\\\": \\\"Mistral-7B\\\",\\n      \\\"dataset\\\": \\\"FOLIO-204\\\",\\n      \\\"n\\\": 204,\\n      \\\"registry_sc\\\": 55.39,\\n      \\\"old_sc_pct\\\": 54.9,\\n      \\\"new_sc_pct\\\": 55.39,\\n      \\\"change\\\": 0.49,\\n      \\\"sica_pct\\\": 55.39,\\n      \\\"old_del
…[truncated 9024 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T06:27:42.704608+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/symb_invariant_consensus/experiments/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 1.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T06:27:42.704862+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "find /root/symb_invariant_consensus -maxdepth 1 -type d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "find /root/symb_invariant_consensus -maxdepth 1 -type d"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-19T06:27:42.705095+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "find /root/symb_invariant_consensus/results -maxdepth 1 -type f -name \"*.json\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "find /root/symb_invariant_consensus/results -maxdepth 1 -type f -name \"*.json\""
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-19T06:27:42.705309+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus\\n/root/symb_invariant_consensus/scripts\\n/root/symb_invariant_consensus/sica\\n/root/symb_invariant_consensus/baselines\\n/root/symb_invariant_consensus/utils\\n/root/symb_invariant_consensus/data\\n/root/symb_invariant_consensus/results\\n/root/symb_invariant_consensus/analysis\\n/root/symb_invariant_consensus/logs\\n/root/symb_invariant_consensus/__pycache__\\n/root/symb_invariant_consensus/artifacts\\n/root/symb_invariant_consensus/figures\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.85}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T06:27:42.705536+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/results/case_study_constraints.json\\n/root/symb_invariant_consensus/results/case_study_normalized.json\\n/root/symb_invariant_consensus/results/exp036b_cross_trace_unsat.json\\n/root/symb_invariant_consensus/results/exp033_per_problem_analysis.json\\n/root/symb_invariant_consensus/results/exp033_per_problem_analysis_v2.json\\n/root/symb_invariant_consensus/results/exp028b_discordant_tracking.json\\n/root/symb_invariant_consensus/results/k_sensitivity_summary.json\\n/root/symb_invariant_consensus/results/k_sensitivity_diversity_analysis.json\\n/root/symb_invariant_consensus/results/condorcet_independence_analysis.json\\n/root/symb_invariant_consensus/results/extraction_error_taxonomy.json\\n/root/symb_invariant_consensus/results/adaptive_sica_validation.json\\n/root/symb_invariant_consensus/results/discriminative_filter_exp033_test.json\\n/root/symb_invariant_consensus/results/discriminative_filter_exp044b.json\\n/root/symb_invariant_consensus/results/discriminative_filter_exp054.json\\n/root/symb_invariant_consensus/results/discriminative_filter_exp046.json\\n/root/symb_invariant_consensus/results/discriminative_filter_exp033.json\\n/root/symb_invariant_consensus/results/fleiss_kappa_exp033.json\\n/root/symb_invariant_consensus/results/fleiss_kappa_unified_25068.json\\n/root/symb_invariant_consensus/results/fleiss_kappa_unified.json\\n/root/symb_invariant_consensus/results/sc_tiebreak_revalidation_25068.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T06:27:42.705779+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "find /root/symb_invariant_consensus/results -type d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "find /root/symb_invariant_consensus/results -type d"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-19T06:27:42.706009+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "find /root/symb_invariant_consensus -name \"sica_results*\" -o -name \"per_problem*\" -o -name \"mcnemar*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "find /root/symb_invariant_consensus -name \"sica_results*\" -o -name \"per_problem*\" -o -name \"mcnemar*\""
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-19T06:27:42.706284+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/results\\n/root/symb_invariant_consensus/results/folio_204_14b\\n/root/symb_invariant_consensus/results/folio_204_14b/intermediates\\n/root/symb_invariant_consensus/results/folio_204_14b/per_trace_constraints\\n/root/symb_invariant_consensus/results/exp028_qwen3_14b_thinking\\n/root/symb_invariant_consensus/results/exp028_qwen3_14b_thinking/intermediates\\n/root/symb_invariant_consensus/results/exp027_qwen3_14b_nonthinking\\n/root/symb_invariant_consensus/results/exp027_qwen3_14b_nonthinking/intermediates\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/intermediates\\n/root/symb_invariant_consensus/results/cross_model_mistral_folio\\n/root/symb_invariant_consensus/results/oracle_folio_regen\\n/root/symb_invariant_consensus/results/exp-007-qwen72b-awq\\n/root/symb_invariant_consensus/results/exp004_qwen7b_rerun\\n/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204\\n/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates\\n/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/constraint_cache\\n/root/symb_invariant_consensus/results/exp034_llama31_8b_folio204\\n/root/symb_invariant_consensus/results/exp035_qwen25_7b_folio204\\n/root/symb_invariant_consensus/results/exp035_qwen25_7b_folio204/intermediates\\n/root/symb_invariant_consensus/results/exp034_qwen25_14b_proofwriter\\n/root/symb_invariant_consensus/results/exp034_qwen25_14b_proofwriter/intermediates\\n/root/symb_invariant_consensus/results/exp036_z3_feedback\\n/root/symb_invariant_consensus/results/icl_oracle_folio\\n/root/symb_invariant_consensus/results/icl_oracle_folio/intermediates\\n/root/symb_invariant_consensus/results/exp4_consistency_filtering\\n/root/symb_invariant_consensus/results/exp05_backward_verification\\n/root/symb_invariant_consensus/results/exp05_backward_verificat
…[truncated 2803 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T06:27:42.706508+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.22}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T06:27:42.706722+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-19T06:27:42.706936+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "find /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204 -name \"*.json\" -not -path \"*/intermediates/*\" -not -path \"*/constraint_cache/*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "find /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204 -name \"*.json\" -not -path \"*/intermediates/*\" -not -path \"*/constraint_cache/*\""
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-19T06:27:42.707144+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"constraint_cache\\nexp033.log\\nexp033_results.json\\nintermediates\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.92}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T06:27:42.707337+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.69}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T06:27:42.707528+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "head -100 /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "head -100 /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T06:27:42.707846+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n_problems\\\": 204,\\n    \\\"sica_accuracy\\\": 0.5931372549019608,\\n    \\\"sc_accuracy\\\": 0.5441176470588235,\\n    \\\"sica_correct\\\": 121,\\n    \\\"sc_correct\\\": 111,\\n    \\\"extraction_rate\\\": 0.9714052287581699,\\n    \\\"total_constraints_extracted\\\": 14042,\\n    \\\"total_unique_constraints\\\": 8021,\\n    \\\"contradiction_rate\\\": 0.03503303827452936,\\n    \\\"problems_with_contradictions\\\": 128,\\n    \\\"per_level_accuracy\\\": {\\n      \\\"validation\\\": {\\n        \\\"sica\\\": 0.5931372549019608,\\n        \\\"sc\\\": 0.5441176470588235,\\n        \\\"n\\\": 204\\n      }\\n    },\\n    \\\"per_dataset_accuracy\\\": {\\n      \\\"folio\\\": {\\n        \\\"sica\\\": 0.5931372549019608,\\n        \\\"sc\\\": 0.5441176470588235,\\n        \\\"n\\\": 204\\n      }\\n    },\\n    \\\"k\\\": 12,\\n    \\\"mode\\\": \\\"vllm\\\",\\n    \\\"total_wall_time_s\\\": 4881.8\\n  },\\n  \\\"results\\\": [\\n    {\\n      \\\"problem_idx\\\": 0,\\n      \\\"problem_id\\\": \\\"folio_0\\\",\\n      \\\"problem\\\": \\\"Given the following premises:\\\\nIf people perform in school talent shows often, then they attend and are very engaged with school events. People either perform in school talent shows often or are inactive and disinterested members of their community. If people chaperone high school dances, then they are not students who attend the school. All people who are inactive and disinterested members of their community chaperone high school dances. All young children and teenagers who wish to further their academic careers and educational opportunities are students who attend the school. Bonnie either both attends and is very engaged with school events and is a student who attends the school, or she neither attends and is very engaged with school events nor is a student who attends the school.\\\\n\\\\nDetermine whether the following conclusion
…[truncated 3574 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-19T06:27:42.708175+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "find /root/symb_invariant_consensus/results -name \"*results*.json\" -not -path \"*/intermediates/*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "find /root/symb_invariant_consensus/results -name \"*results*.json\" -not -path \"*/intermediates/*\""
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T06:27:42.708414+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/results/folio_204_14b/folio_204_results.json\\n/root/symb_invariant_consensus/results/exp028_qwen3_14b_thinking/exp028_results.json\\n/root/symb_invariant_consensus/results/exp027_qwen3_14b_nonthinking/exp027_results.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/contrastive_results.json\\n/root/symb_invariant_consensus/results/cross_model_mistral_folio/cross_model_mistral_results.json\\n/root/symb_invariant_consensus/results/oracle_folio_regen/exp031_results.json\\n/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json\\n/root/symb_invariant_consensus/results/exp035_qwen25_7b_folio204/exp035_results.json\\n/root/symb_invariant_consensus/results/exp034_qwen25_14b_proofwriter/exp034_results.json\\n/root/symb_invariant_consensus/results/exp036_z3_feedback/z3_feedback_results.json\\n/root/symb_invariant_consensus/results/icl_oracle_folio/results.json\\n/root/symb_invariant_consensus/results/exp4_consistency_filtering/results.json\\n/root/symb_invariant_consensus/results/exp05_backward_verification/results.json\\n/root/symb_invariant_consensus/results/exp046_mistral_7b_pw600/exp046_results.json\\n/root/symb_invariant_consensus/results/exp044b_icl_oracle_qwen14b/results.json\\n/root/symb_invariant_consensus/results/exp028b_qwen3_thinking_folio204/exp028b_results.json\\n/root/symb_invariant_consensus/results/exp051_mistral_k_sensitivity/k4/results.json\\n/root/symb_invariant_consensus/results/exp051_mistral_k_sensitivity/k8/results.json\\n/root/symb_invariant_consensus/results/exp051_mistral_k_sensitivity/k16/results.json\\n/root/symb_invariant_consensus/results/exp051_mistral_k_sensitivity/k20/results.json\\n/root/symb_invariant_consensus/results/exp054_mistral_folio204_t10/exp054_results.json\\n/root/symb_invariant_consensus/results/exp057_mistral_folio204_t03/exp057_results.json\\n/root/symb_invariant_consensus/results/exp058
…[truncated 147 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-19T06:27:42.708664+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "find /root/symb_invariant_consensus -name \"*052*\" -o -name \"*053*\" -o -name \"*seed*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "find /root/symb_invariant_consensus -name \"*052*\" -o -name \"*053*\" -o -name \"*seed*\""
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-19T06:27:42.708859+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "find /root/symb_invariant_consensus -name \"*026*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "find /root/symb_invariant_consensus -name \"*026*\""
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-19T06:27:42.709086+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.72}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T06:27:42.709305+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/results/exp034_qwen25_14b_proofwriter/intermediates/ProofWriter_RelNeg-OWA-D5-1026_Q13.json\\n/root/symb_invariant_consensus/results/exp034_qwen25_14b_proofwriter/intermediates/ProofWriter_RelNeg-OWA-D5-1026_Q4.json\\n/root/symb_invariant_consensus/results/exp034_qwen25_14b_proofwriter/intermediates/ProofWriter_RelNeg-OWA-D5-1026_Q9.json\\n/root/symb_invariant_consensus/results/exp046_mistral_7b_pw600/intermediates/ProofWriter_RelNeg-OWA-D5-1026_Q13.json\\n/root/symb_invariant_consensus/results/exp046_mistral_7b_pw600/intermediates/ProofWriter_RelNeg-OWA-D5-1026_Q4.json\\n/root/symb_invariant_consensus/results/exp046_mistral_7b_pw600/intermediates/ProofWriter_RelNeg-OWA-D5-1026_Q9.json\\n/root/symb_invariant_consensus/results/exp046_mistral_7b_pw600/per_trace_constraints/ProofWriter_RelNeg-OWA-D5-1026_Q13.json\\n/root/symb_invariant_consensus/results/exp046_mistral_7b_pw600/per_trace_constraints/ProofWriter_RelNeg-OWA-D5-1026_Q4.json\\n/root/symb_invariant_consensus/results/exp046_mistral_7b_pw600/per_trace_constraints/ProofWriter_RelNeg-OWA-D5-1026_Q9.json\\n/root/symb_invariant_consensus/logs/folio_regen_20260518_193948.log\\n/root/symb_invariant_consensus/logs/folio_regen_restart_20260518_194658.log\\n/root/symb_invariant_consensus/logs/folio_regen_final_20260518_201110.log\\n/root/symb_invariant_consensus/logs/folio_regen_v3_20260518_201127.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.05}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-19T06:27:42.709570+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "python3 -c \"import json; d=json.load(open('/root/symb_invariant_consensus/results/sc_tiebreak_revalidation_25068.json')); print('Summary exp_ids:', [x['exp_id'] for x in d['summary']]); print('Affected exp_ids:', list(d['affected_problems'].keys()))\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "python3 -c \"import json; d=json.load(open('/root/symb_invariant_consensus/results/sc_tiebreak_revalidation_25068.json')); print('Summary exp_ids:', [x['exp_id'] for x in d['summary']]); print('Affected exp_ids:', list(d['affected_problems'].keys()))\""
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T06:27:42.709775+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-19T06:27:42.709990+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "cat /root/symb_invariant_consensus/sc_tiebreak_revalidation.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "cat /root/symb_invariant_consensus/sc_tiebreak_revalidation.py"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T06:27:42.710519+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Batch SC tiebreaking revalidation: recompute SC with deterministic alphabetical tie-breaking.\\\"\\\"\\\"\\nimport json\\nfrom pathlib import Path\\n\\nEXPERIMENTS = [\\n    {\\\"exp_id\\\": \\\"exp-033\\\", \\\"label\\\": \\\"Mistral-7B FOLIO-204 seed=42 T=0.7 K=12\\\",\\n     \\\"path\\\": \\\"/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json\\\",\\n     \\\"old_sc\\\": 54.41, \\\"model\\\": \\\"Mistral-7B\\\", \\\"dataset\\\": \\\"FOLIO-204\\\"},\\n    {\\\"exp_id\\\": \\\"exp-057\\\", \\\"label\\\": \\\"Mistral-7B FOLIO-204 T=0.3\\\",\\n     \\\"path\\\": \\\"/root/symb_invariant_consensus/results/exp057_mistral_folio204_t03/exp057_results.json\\\",\\n     \\\"old_sc\\\": 57.35, \\\"model\\\": \\\"Mistral-7B\\\", \\\"dataset\\\": \\\"FOLIO-204\\\"},\\n    {\\\"exp_id\\\": \\\"exp-058\\\", \\\"label\\\": \\\"Mistral-7B FOLIO-204 T=0.5\\\",\\n     \\\"path\\\": \\\"/root/symb_invariant_consensus/results/exp058_mistral_folio204_t05/exp058_results.json\\\",\\n     \\\"old_sc\\\": 57.84, \\\"model\\\": \\\"Mistral-7B\\\", \\\"dataset\\\": \\\"FOLIO-204\\\"},\\n    {\\\"exp_id\\\": \\\"exp-054\\\", \\\"label\\\": \\\"Mistral-7B FOLIO-204 T=1.0\\\",\\n     \\\"path\\\": \\\"/root/symb_invariant_consensus/results/exp054_mistral_folio204_t10/exp054_results.json\\\",\\n     \\\"old_sc\\\": 55.39, \\\"model\\\": \\\"Mistral-7B\\\", \\\"dataset\\\": \\\"FOLIO-204\\\"},\\n    {\\\"exp_id\\\": \\\"exp-051-k4\\\", \\\"label\\\": \\\"Mistral-7B FOLIO-204 K=4\\\",\\n     \\\"path\\\": \\\"/root/symb_invariant_consensus/results/exp051_mistral_k_sensitivity/k4/results.json\\\",\\n     \\\"old_sc\\\": 54.41, \\\"model\\\": \\\"Mistral-7B\\\", \\\"dataset\\\": \\\"FOLIO-204\\\"},\\n    {\\\"exp_id\\\": \\\"exp-051-k8\\\", \\\"label\\\": \\\"Mistral-7B FOLIO-204 K=8\\\",\\n     \\\"path\\\": \\\"/root/symb_invariant_consensus/results/exp051_mistral_k_sensitivity/k8/results.json\\\"
…[truncated 8219 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-19T06:27:42.710834+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "find /root/symb_invariant_consensus -name \"*results*.json\" -not -path \"*/intermediates/*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "find /root/symb_invariant_consensus -name \"*results*.json\" -not -path \"*/intermediates/*\""
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-19T06:27:42.711062+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "find /root/symb_invariant_consensus -name \"sc_tiebreak*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "find /root/symb_invariant_consensus -name \"sc_tiebreak*\""
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-19T06:27:42.711276+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/results.json\\n/root/symb_invariant_consensus/results/exp033_qwen3_14b_pw600_nonthinking/results.json\\n/root/symb_invariant_consensus/results/exp036_qwen25_14b_folio204/results.json\\n/root/symb_invariant_consensus/results/exp038_qwen25_14b_logiqa200/results.json\\n/root/symb_invariant_consensus/results/exp050_FAILED_overflow/exp050_results.json\\n/root/symb_invariant_consensus/results/exp050b_mistral_icl_oracle/exp050b_results.json\\n/root/symb_invariant_consensus/results/exp049b_mistral_logiqa200/exp049b_results.json\\n/root/symb_invariant_consensus/results/exp052_mistral_folio204_seed123/exp052_results.json\\n/root/symb_invariant_consensus/results/exp053_mistral_folio204_seed456/exp053_results.json\\n/root/symb_invariant_consensus/results/exp048_llama8b_pw600/exp048_results.json\\n/root/symb_invariant_consensus/results/exp055_multitemp_mistral_folio/exp055_results.json\\n/root/symb_invariant_consensus/results/exp028b_qwen3_thinking_folio204/exp028b_remaining38_results.json\\n/root/symb_invariant_consensus/results/exp028b_dryrun/dryrun_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.98}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-19T06:27:42.711491+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/results/sc_tiebreak_revalidation_16639.json\\n/root/symb_invariant_consensus/sc_tiebreak_revalidation.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.33}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-19T06:27:42.711721+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "cat /root/symb_invariant_consensus/results/sc_tiebreak_revalidation_16639.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "cat /root/symb_invariant_consensus/results/sc_tiebreak_revalidation_16639.json"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-19T06:27:42.712169+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": [\\n    {\\n      \\\"exp_id\\\": \\\"exp-052\\\",\\n      \\\"label\\\": \\\"Mistral-7B FOLIO-204 seed=123\\\",\\n      \\\"model\\\": \\\"Mistral-7B\\\",\\n      \\\"dataset\\\": \\\"FOLIO-204\\\",\\n      \\\"n\\\": 204,\\n      \\\"registry_sc\\\": 56.37,\\n      \\\"old_sc_pct\\\": 53.92,\\n      \\\"new_sc_pct\\\": 54.41,\\n      \\\"change\\\": 0.49,\\n      \\\"sica_pct\\\": 57.35,\\n      \\\"old_delta_pp\\\": 3.43,\\n      \\\"new_delta_pp\\\": 2.94,\\n      \\\"n_affected\\\": 2\\n    },\\n    {\\n      \\\"exp_id\\\": \\\"exp-053\\\",\\n      \\\"label\\\": \\\"Mistral-7B FOLIO-204 seed=456\\\",\\n      \\\"model\\\": \\\"Mistral-7B\\\",\\n      \\\"dataset\\\": \\\"FOLIO-204\\\",\\n      \\\"n\\\": 204,\\n      \\\"registry_sc\\\": 56.37,\\n      \\\"old_sc_pct\\\": 56.37,\\n      \\\"new_sc_pct\\\": 55.88,\\n      \\\"change\\\": -0.49,\\n      \\\"sica_pct\\\": 55.88,\\n      \\\"old_delta_pp\\\": -0.49,\\n      \\\"new_delta_pp\\\": 0.0,\\n      \\\"n_affected\\\": 1\\n    },\\n    {\\n      \\\"exp_id\\\": \\\"exp-039\\\",\\n      \\\"label\\\": \\\"Qwen2.5-14B PW-600 (16639)\\\",\\n      \\\"model\\\": \\\"Qwen2.5-14B\\\",\\n      \\\"dataset\\\": \\\"PW-600\\\",\\n      \\\"n\\\": 600,\\n      \\\"registry_sc\\\": 73.5,\\n      \\\"old_sc_pct\\\": 73.5,\\n      \\\"new_sc_pct\\\": 74.0,\\n      \\\"change\\\": 0.5,\\n      \\\"sica_pct\\\": 71.5,\\n      \\\"old_delta_pp\\\": -2.0,\\n      \\\"new_delta_pp\\\": -2.5,\\n      \\\"n_affected\\\": 12\\n    }\\n  ],\\n  \\\"details\\\": {\\n    \\\"exp-052\\\": [\\n      {\\n        \\\"problem_id\\\": \\\"folio_2\\\",\\n        \\\"old_sc\\\": \\\"Unknown\\\",\\n        \\\"new_sc\\\": \\\"False\\\",\\n        \\\"gt\\\": \\\"False\\\",\\n        \\\"vote_dist\\\": {\\n          \\\"Unknown\\\": 4,\\n          \\\"False\\\": 4\\n        },\\n        \\\"old_correct\\\": false,\\n        \\\"new_correct\\\": true\\n      },
…[truncated 5884 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-19T06:27:42.712458+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "cat /root/symb_invariant_consensus/sc_tiebreak_revalidation.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "cat /root/symb_invariant_consensus/sc_tiebreak_revalidation.py"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-19T06:27:42.712667+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "find /root/symb_invariant_consensus/results -maxdepth 2 -name \"*.json\" -path \"*039*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "find /root/symb_invariant_consensus/results -maxdepth 2 -name \"*.json\" -path \"*039*\""
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-19T06:27:42.713079+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Batch SC tiebreaking revalidation (westd-16639).\\\"\\\"\\\"\\nimport json\\nfrom pathlib import Path\\n\\nEXPERIMENTS = [\\n    {\\\"exp_id\\\": \\\"exp-052\\\", \\\"label\\\": \\\"Mistral-7B FOLIO-204 seed=123\\\",\\n     \\\"path\\\": \\\"/root/symb_invariant_consensus/results/exp052_mistral_folio204_seed123/exp052_results.json\\\",\\n     \\\"old_sc\\\": 56.37, \\\"model\\\": \\\"Mistral-7B\\\", \\\"dataset\\\": \\\"FOLIO-204\\\"},\\n    {\\\"exp_id\\\": \\\"exp-053\\\", \\\"label\\\": \\\"Mistral-7B FOLIO-204 seed=456\\\",\\n     \\\"path\\\": \\\"/root/symb_invariant_consensus/results/exp053_mistral_folio204_seed456/exp053_results.json\\\",\\n     \\\"old_sc\\\": 56.37, \\\"model\\\": \\\"Mistral-7B\\\", \\\"dataset\\\": \\\"FOLIO-204\\\"},\\n    {\\\"exp_id\\\": \\\"exp-039\\\", \\\"label\\\": \\\"Qwen2.5-14B PW-600 (16639)\\\",\\n     \\\"path\\\": \\\"/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/results.json\\\",\\n     \\\"old_sc\\\": 73.50, \\\"model\\\": \\\"Qwen2.5-14B\\\", \\\"dataset\\\": \\\"PW-600\\\"},\\n]\\n\\n\\ndef normalize_answer(ans):\\n    if not ans:\\n        return \\\"\\\"\\n    a = ans.strip().lower()\\n    mapping = {\\n        \\\"true\\\": \\\"True\\\", \\\"false\\\": \\\"False\\\", \\\"unknown\\\": \\\"Unknown\\\",\\n        \\\"proved\\\": \\\"True\\\", \\\"disproved\\\": \\\"False\\\",\\n        \\\"a\\\": \\\"A\\\", \\\"b\\\": \\\"B\\\", \\\"c\\\": \\\"C\\\", \\\"d\\\": \\\"D\\\",\\n    }\\n    return mapping.get(a, ans.strip())\\n\\n\\ndef deterministic_sc(vote_dist):\\n    if not vote_dist:\\n        return \\\"\\\"\\n    return max(sorted(vote_dist.keys()), key=lambda k: vote_dist[k])\\n\\n\\ndef process_experiment(exp_info):\\n    path = Path(exp_info[\\\"path\\\"])\\n    if not path.exists():\\n        return {\\\"exp_id\\\": exp_info[\\\"exp_id\\\"], \\\"error\\\": f\\\"File not found: {path}\\\"}\\n\\n    with open(path) as f:\\n        d
…[truncated 6217 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-19T06:27:42.713327+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.29}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-19T06:27:42.713579+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "find /root/symb_invariant_consensus/results -maxdepth 1 -type d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "find /root/symb_invariant_consensus/results -maxdepth 1 -type d"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-19T06:27:42.713810+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/results\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600\\n/root/symb_invariant_consensus/results/exp033_qwen3_14b_pw600_nonthinking\\n/root/symb_invariant_consensus/results/exp036_qwen25_14b_folio204\\n/root/symb_invariant_consensus/results/exp037_mistral7b_folio204\\n/root/symb_invariant_consensus/results/exp038_qwen25_14b_logiqa200\\n/root/symb_invariant_consensus/results/exp050_FAILED_overflow\\n/root/symb_invariant_consensus/results/exp050b_mistral_icl_oracle\\n/root/symb_invariant_consensus/results/exp049b_mistral_logiqa200\\n/root/symb_invariant_consensus/results/exp052_mistral_folio204_seed123\\n/root/symb_invariant_consensus/results/exp053_mistral_folio204_seed456\\n/root/symb_invariant_consensus/results/exp048_llama8b_pw600\\n/root/symb_invariant_consensus/results/exp055_multitemp_mistral_folio\\n/root/symb_invariant_consensus/results/exp028b_qwen3_thinking_folio204\\n/root/symb_invariant_consensus/results/exp028b_dryrun\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.02}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-19T06:27:42.714095+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "head -20 /root/symb_invariant_consensus/results/exp034_qwen25_14b_proofwriter/exp034_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "head -20 /root/symb_invariant_consensus/results/exp034_qwen25_14b_proofwriter/exp034_results.json"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-19T06:27:42.714324+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n_problems\\\": 600,\\n    \\\"sica_accuracy\\\": 0.7083333333333334,\\n    \\\"sc_accuracy\\\": 0.7033333333333334,\\n    \\\"sica_correct\\\": 425,\\n    \\\"sc_correct\\\": 422,\\n    \\\"extraction_rate\\\": 0.9919444444444444,\\n    \\\"total_constraints_extracted\\\": 93251,\\n    \\\"total_unique_constraints\\\": 22114,\\n    \\\"contradiction_rate\\\": 0.006195170480238763,\\n    \\\"problems_with_contradictions\\\": 103,\\n    \\\"per_level_accuracy\\\": {\\n      \\\"OWA-D5\\\": {\\n        \\\"sica\\\": 0.7083333333333334,\\n        \\\"sc\\\": 0.7033333333333334,\\n        \\\"n\\\": 600\\n      }\\n    },\\n    \\\"per_dataset_accuracy\\\": {\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.15}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-19T06:27:42.714670+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "cat > /root/symb_invariant_consensus/mcnemar_recompute.py << 'PYEOF'\n\"\"\"McNemar exact test recomputation after SC tiebreaking fix.\"\"\"\nimport json\nfrom pathlib import Path\nfrom scipy.stats import binomtest\n\nEXPERIMENTS = [\n    {\"exp_id\": \"exp-033\", \"label\": \"Mistral-7B FOLIO-204 seed=42\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json\"},\n    {\"exp_id\": \"exp-057\", \"label\": \"Mistral-7B FOLIO-204 T=0.3\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp057_mistral_folio204_t03/exp057_results.json\"},\n    {\"exp_id\": \"exp-058\", \"label\": \"Mistral-7B FOLIO-204 T=0.5\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp058_mistral_folio204_t05/exp058_results.json\"},\n    {\"exp_id\": \"exp-054\", \"label\": \"Mistral-7B FOLIO-204 T=1.0\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp054_mistral_folio204_t10/exp054_results.json\"},\n    {\"exp_id\": \"exp-051-k8\", \"label\": \"Mistral-7B FOLIO-204 K=8\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp051_mistral_k_sensitivity/k8/results.json\"},\n    {\"exp_id\": \"exp-026\", \"label\": \"Qwen2.5-14B FOLIO-204\",\n     \"path\": \"/root/symb_invariant_consensus/results/folio_204_14b/folio_204_results.json\"},\n    {\"exp_id\": \"exp-027\", \"label\": \"Qwen3-14B FOLIO-204\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp027_qwen3_14b_nonthinking/exp027_results.json\"},\n    {\"exp_id\": \"exp-046\", \"label\": \"Mistral-7B PW-600 (sanity)\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp046_mistral_7b_pw600/exp046_results.json\"},\n    {\"exp_id\": \"exp-034\", \"label\": \"Qwen2.5-14B PW-600\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp034_qwen25_14b_proofwriter/exp034_results.json\"},\n]\n\n\ndef normalize_answer(ans):\n    if not ans:\n        return \"\"\n    a = ans.strip().lower()\n    mapping = {\n        \"true\": \"True\", \"false\": \"False\", \"unknown\": \"Unknown\",\n        \"proved\": \"True\", \"disproved\": \"False\",\n    }\n    return mapping.get(a, ans.strip())\n\n\ndef deterministic_sc(vote_dist):\n    if not vote_dist:\n        return \"\"\n    return max(sorted(vote_dist.keys()), key=lambda k: vote_dist[k])\n\n\ndef compute_mcnemar(exp_info):\n    path = Path(exp_info[\"path\"])\n    if not path.exists():\n        return {\"exp_id\": exp_info[\"exp_id\"], \"error\": f\"File not found: {path}\"}\n\n    with open(path) as f:\n        data = json.load(f)\n\n    results = data.get(\"results\", [])\n    n = len(results)\n\n    b = 0  # SC correct, SICA wrong\n    c = 0  # SC wrong, SICA correct\n    a_both = 0  # both correct\n    d_both = 0  # both wrong\n    new_sc_correct_count = 0\n    sica_correct_count = 0\n\n    for r in results:\n        gt = r.get(\"ground_truth\", \"\")\n        sica_correct = r.get(\"sica_correct\", False)\n        vote_dist = r.get(\"sc_vote_distribution\", {})\n        new_sc_answer = deterministic_sc(vote_dist)\n        new_sc_correct = (normalize_answer(new_sc_answer) == normalize_answer(gt))\n\n        if new_sc_correct:\n            new_sc_correct_count += 1\n        if sica_correct:\n            sica_correct_count += 1\n\n        if new_sc_correct and sica_correct:\n            a_both += 1\n        elif new_sc_correct and not sica_correct:\n            b += 1\n        elif not new_sc_correct and sica_correct:\n            c += 1\n        else:\n            d_both += 1\n\n    new_sc_pct = new_sc_correct_count / n * 100\n    sica_pct = sica_correct_count / n * 100\n    delta_pp = sica_pct - new_sc_pct\n\n    if b + c == 0:\n        p_value = 1.0\n    else:\n        result = binomtest(min(b, c), b + c, 0.5)\n        p_value = result.pvalue\n\n    if p_value < 0.02:\n        sig = \"**\"\n    elif p_value < 0.05:\n        sig = \"*\"\n    else:\n        sig = \"ns\"\n\n    return {\n        \"exp_id\": exp_info[\"exp_id\"],\n        \"label\": exp_info[\"label\"],\n        \"n\": n,\n        \"new_sc_pct\": round(new_sc_pct, 2),\n        \"sica_pct\": round(sica_pct, 2),\n        \"delta_pp\": round(delta_pp, 2),\n        \"a_both_correct\": a_both,\n        \"b_sc_correct_sica_wrong\": b,\n        \"c_sc_wrong_sica_correct\": c,\n        \"d_both_wrong\": d_both,\n        \"p_value\": p_value,\n        \"sig\": sig,\n    }\n\n\ndef main():\n    results = []\n    for exp in EXPERIMENTS:\n        r = compute_mcnemar(exp)\n        results.append(r)\n\n    print(f\"{'Exp':<14} {'n':>4} {'NewSC%':>8} {'SICA%':>8} {'Δ(pp)':>8} {'b(SC✓SICA✗)':>12} {'c(SC✗SICA✓)':>12} {'McNemar p':>12} {'Sig':>5}\")\n    print(\"-\" * 100)\n    for r in results:\n        if \"error\" in r:\n            print(f\"{r['exp_id']:<14} ERROR: {r['error']}\")\n            continue\n        print(f\"{r['exp_id']:<14} {r['n']:>4} {r['new_sc_pct']:>7.2f}% {r['sica_pct']:>7.2f}% {r['delta_pp']:>+7.2f} {r['b_sc_correct_sica_wrong']:>12} {r['c_sc_wrong_sica_correct']:>12} {r['p_value']:>12.6f} {r['sig']:>5}\")\n        print(f\"{'':>14} contingency: a={r['a_both_correct']} b={r['b_sc_correct_sica_wrong']} c={r['c_sc_wrong_sica_correct']} d={r['d_both_wrong']}\")\n\n    out = {\"server\": \"westd-25068\", \"results\": results}\n    out_path = Path(\"/root/symb_invariant_consensus/results/mcnemar_recomputed_25068.json\")\n    with open(out_path, \"w\") as f:\n        json.dump(out, f, indent=2)\n    print(f\"\\nSaved to {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\npython3 /root/symb_invariant_consensus/mcnemar_recompute.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "cat > /root/symb_invariant_consensus/mcnemar_recompute.py << 'PYEOF'\n\"\"\"McNemar exact test recomputation after SC tiebreaking fix.\"\"\"\nimport json\nfrom pathlib import Path\nfrom scipy.stats import binomtest\n\nEXPERIMENTS = [\n    {\"exp_id\": \"exp-033\", \"label\": \"Mistral-7B FOLIO-204 seed=42\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json\"},\n    {\"exp_id\": \"exp-057\", \"label\": \"Mistral-7B FOLIO-204 T=0.3\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp057_mistral_folio204_t03/exp057_results.json\"},\n    {\"exp_id\": \"exp-058\", \"label\": \"Mistral-7B FOLIO-204 T=0.5\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp058_mistral_folio204_t05/exp058_results.json\"},\n    {\"exp_id\": \"exp-054\", \"label\": \"Mistral-7B FOLIO-204 T=1.0\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp054_mistral_folio204_t10/exp054_results.json\"},\n    {\"exp_id\": \"exp-051-k8\", \"label\": \"Mistral-7B FOLIO-204 K=8\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp051_mistral_k_sensitivity/k8/results.json\"},\n    {\"exp_id\": \"exp-026\", \"label\": \"Qwen2.5-14B FOLIO-204\",\n     \"path\": \"/root/symb_invariant_consensus/results/folio_204_14b/folio_204_results.json\"},\n    {\"exp_id\": \"exp-027\", \"label\": \"Qwen3-14B FOLIO-204\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp027_qwen3_14b_nonthinking/exp027_results.json\"},\n    {\"exp_id\": \"exp-046\", \"label\": \"Mistral-7B PW-600 (sanity)\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp046_mistral_7b_pw600/exp046_results.json\"},\n    {\"exp_id\": \"exp-034\", \"label\": \"Qwen2.5-14B PW-600\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp034_qwen25_14b_proofwriter/exp034_results.json\"},\n]\n\n\ndef normalize_answer(ans):\n    if not ans:\n        return \"\"\n    a = ans.strip().lower()\n    mapping = {\n        \"true\": \"True\", \"false\": \"False\", \"unknown\": \"Unknown\",\n        \"proved\": \"True\", \"disproved\": \"False\",\n    }\n    return mapping.get(a, ans.strip())\n\n\ndef deterministic_sc(vote_dist):\n    if not vote_dist:\n        return \"\"\n    return max(sorted(vote_dist.keys()), key=lambda k: vote_dist[k])\n\n\ndef compute_mcnemar(exp_info):\n    path = Path(exp_info[\"path\"])\n    if not path.exists():\n        return {\"exp_id\": exp_info[\"exp_id\"], \"error\": f\"File not found: {path}\"}\n\n    with open(path) as f:\n        data = json.load(f)\n\n    results = data.get(\"results\", [])\n    n = len(results)\n\n    b = 0  # SC correct, SICA wrong\n    c = 0  # SC wrong, SICA correct\n    a_both = 0  # both correct\n    d_both = 0  # both wrong\n    new_sc_correct_count = 0\n    sica_correct_count = 0\n\n    for r in results:\n        gt = r.get(\"ground_truth\", \"\")\n        sica_correct = r.get(\"sica_correct\", False)\n        vote_dist = r.get(\"sc_vote_distribution\", {})\n        new_sc_answer = deterministic_sc(vote_dist)\n        new_sc_correct = (normalize_answer(new_sc_answer) == normalize_answer(gt))\n\n        if new_sc_correct:\n            new_sc_correct_count += 1\n        if sica_correct:\n            sica_correct_count += 1\n\n        if new_sc_correct and sica_correct:\n            a_both += 1\n        elif new_sc_correct and not sica_correct:\n            b += 1\n        elif not new_sc_correct and sica_correct:\n            c += 1\n        else:\n            d_both += 1\n\n    new_sc_pct = new_sc_correct_count / n * 100\n    sica_pct = sica_correct_count / n * 100\n    delta_pp = sica_pct - new_sc_pct\n\n    if b + c == 0:\n        p_value = 1.0\n    else:\n        result = binomtest(min(b, c), b + c, 0.5)\n        p_value = result.pvalue\n\n    if p_value < 0.02:\n        sig = \"**\"\n    elif p_value < 0.05:\n        sig = \"*\"\n    else:\n        sig = \"ns\"\n\n    return {\n        \"exp_id\": exp_info[\"exp_id\"],\n        \"label\": exp_info[\"label\"],\n        \"n\": n,\n        \"new_sc_pct\": round(new_sc_pct, 2),\n        \"sica_pct\": round(sica_pct, 2),\n        \"delta_pp\": round(delta_pp, 2),\n        \"a_both_correct\": a_both,\n        \"b_sc_correct_sica_wrong\": b,\n        \"c_sc_wrong_sica_correct\": c,\n        \"d_both_wrong\": d_both,\n        \"p_value\": p_value,\n        \"sig\": sig,\n    }\n\n\ndef main():\n    results = []\n    for exp in EXPERIMENTS:\n        r = compute_mcnemar(exp)\n        results.append(r)\n\n    print(f\"{'Exp':<14} {'n':>4} {'NewSC%':>8} {'SICA%':>8} {'Δ(pp)':>8} {'b(SC✓SICA✗)':>12} {'c(SC✗SICA✓)':>12} {'McNemar p':>12} {'Sig':>5}\")\n    print(\"-\" * 100)\n    for r in results:\n        if \"error\" in r:\n            print(f\"{r['exp_id']:<14} ERROR: {r['error']}\")\n            continue\n        print(f\"{r['exp_id']:<14} {r['n']:>4} {r['new_sc_pct']:>7.2f}% {r['sica_pct']:>7.2f}% {r['delta_pp']:>+7.2f} {r['b_sc_correct_sica_wrong']:>12} {r['c_sc_wrong_sica_correct']:>12} {r['p_value']:>12.6f} {r['sig']:>5}\")\n        print(f\"{'':>14} contingency: a={r['a_both_correct']} b={r['b_sc_correct_sica_wrong']} c={r['c_sc_wrong_sica_correct']} d={r['d_both_wrong']}\")\n\n    out = {\"server\": \"westd-25068\", \"results\": results}\n    out_path = Path(\"/root/symb_invariant_consensus/results/mcnemar_recomputed_25068.json\")\n    with open(out_path, \"w\") as f:\n        json.dump(out, f, indent=2)\n    print(f\"\\nSaved to {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\npython3 /root/symb_invariant_consensus/mcnemar_recompute.py"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-19T06:27:42.715237+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cat > /root/symb_invariant_consensus/mcnemar_recompute.py << \\\\'PYEOF\\\\'\\\\n\\\"\\\"\\\"McNemar exact test recomputation after SC tiebreaking fix.\\\"\\\"\\\"\\\\nimport json\\\\nfrom pathlib import Path\\\\nfrom scipy.stats import binomtest\\\\n\\\\nEXPERIMENTS = [\\\\n    {\\\"exp_id\\\": \\\"exp-033\\\", \\\"label\\\": \\\"Mistral-7B FOLIO-204 seed=42\\\",\\\\n     \\\"path\\\": \\\"/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json\\\"},\\\\n    {\\\"exp_id\\\": \\\"exp-057\\\", \\\"label\\\": \\\"Mistral-7B FOLIO-204 T=0.3\\\",\\\\n     \\\"path\\\": \\\"/root/symb_invariant_consensus/results/exp057_mistral_folio204_t03/exp057_results.json\\\"},\\\\n    {\\\"exp_id\\\": \\\"exp-058\\\", \\\"label\\\": \\\"Mistral-7B FOLIO-204 T=0.5\\\",\\\\n     \\\"path\\\": \\\"/root/symb_invariant_consensus/results/exp058_mistral_folio204_t05/exp058_results.json\\\"},\\\\n    {\\\"exp_id\\\": \\\"exp-054\\\", \\\"label\\\": \\\"Mistral-7B FOLIO-204 T=1.0\\\",\\\\n     \\\"path\\\": \\\"/root/symb_invariant_consensus/results/exp054_mistral_folio204_t10/exp054_results.json\\\"},\\\\n    {\\\"exp_id\\\": \\\"exp-051-k8\\\", \\\"label\\\": \\\"Mistral-7B FOLIO-204 K=8\\\",\\\\n     \\\"path\\\": \\\"/root/symb_invariant_consensus/results/exp051_mistral_k_sensitivity/k8/results.json\\\"},\\\\n    {\\\"exp_id\\\": \\\"exp-026\\\", \\\"label\\\": \\\"Qwen2.5-14B FOLIO-204\\\",\\\\n     \\\"path\\\": \\\"/root/symb_invariant_consensus/results/folio_204_14b/folio_204_results.json\\\"},\\\\n    {\\\"exp_id\\\": \\\"exp-027\\\", \\\"label\\\": \\\"Qwen3-14B FOLIO-204\\\",\\\\n     \\\"path\\\": \\\"/root/symb_invariant_consensus/results/exp027_qwen3_14b_nonthinking/exp027_results.json\\\"},\\\\n    {\\\"exp_id\\\": \\\"exp-046\\\", \\\"label\\\": \\\"Mistral-7B PW-600 (sanity)\\\",\\\\n     \\\"path\\\": \\\"/root/symb_invariant_consensu
…[truncated 4930 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-19T06:27:42.715504+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "find /usr -name \"python*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "find /usr -name \"python*\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-19T06:27:42.715712+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/usr/share/vim/vim82/autoload/python3complete.vim\\n/usr/share/vim/vim82/autoload/pythoncomplete.vim\\n/usr/share/vim/vim82/ftplugin/python.vim\\n/usr/share/vim/vim82/indent/python.vim\\n/usr/share/vim/vim82/syntax/python.vim\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.92}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-19T06:27:42.715994+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "find /root -name \"python*\" -type f -path \"*/bin/*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "find /root -name \"python*\" -type f -path \"*/bin/*\""
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-19T06:27:42.716219+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/bin/python3.12\\n/root/miniconda3/bin/python3.12-config\\n/root/miniconda3/pkgs/python-3.12.3-h996f2a0_1/bin/python3.12\\n/root/miniconda3/pkgs/python-3.12.3-h996f2a0_1/bin/python3.12-config\\n/root/miniconda3/pkgs/python-3.12.4-h5148396_1/bin/python3.12\\n/root/miniconda3/pkgs/python-3.12.4-h5148396_1/bin/python3.12-config\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.29}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-19T06:27:42.716419+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "find /root -name \"conda\" -type f -path \"*/bin/*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "find /root -name \"conda\" -type f -path \"*/bin/*\""
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-19T06:27:42.716618+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/bin/conda\\n/root/miniconda3/pkgs/conda-24.4.0-py312h06a4308_0/bin/conda\\n/root/miniconda3/pkgs/conda-24.4.0-py312h06a4308_0/lib/python3.12/site-packages/conda/shell/bin/conda\\n/root/miniconda3/pkgs/conda-24.11.3-py312h7900ff3_0/bin/conda\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-19T06:27:42.716811+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"from scipy.stats import binomtest; print('scipy ok')\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"from scipy.stats import binomtest; print('scipy ok')\""
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-19T06:27:42.717037+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"scipy ok\\n\", \"stderr\": \"Error while loading conda entry point: conda-libmamba-solver (module 'libmambapy' has no attribute 'QueryFormat')\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.25}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-19T06:27:42.717297+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/mcnemar_recompute.py",
  "content": "\"\"\"McNemar exact test recomputation after SC tiebreaking fix.\"\"\"\nimport json\nimport sys\nfrom pathlib import Path\nfrom scipy.stats import binomtest\n\n\ndef normalize_answer(ans):\n    if not ans:\n        return \"\"\n    a = ans.strip().lower()\n    mapping = {\n        \"true\": \"True\", \"false\": \"False\", \"unknown\": \"Unknown\",\n        \"proved\": \"True\", \"disproved\": \"False\",\n    }\n    return mapping.get(a, ans.strip())\n\n\ndef deterministic_sc(vote_dist):\n    \"\"\"Alphabetical tie-breaking: among tied-max answers, pick first alphabetically.\"\"\"\n    if not vote_dist:\n        return \"\"\n    return max(sorted(vote_dist.keys()), key=lambda k: vote_dist[k])\n\n\ndef compute_mcnemar(exp_info):\n    path = Path(exp_info[\"path\"])\n    if not path.exists():\n        return {\"exp_id\": exp_info[\"exp_id\"], \"error\": f\"File not found: {path}\"}\n\n    with open(path) as f:\n        data = json.load(f)\n\n    results = data.get(\"results\", [])\n    n = len(results)\n\n    b = 0\n    c = 0\n    a_both = 0\n    d_both = 0\n    new_sc_correct_count = 0\n    sica_correct_count = 0\n\n    for r in results:\n        gt = r.get(\"ground_truth\", \"\")\n        sica_correct = r.get(\"sica_correct\", False)\n        vote_dist = r.get(\"sc_vote_distribution\", {})\n        new_sc_answer = deterministic_sc(vote_dist)\n        new_sc_correct = (normalize_answer(new_sc_answer) == normalize_answer(gt))\n\n        if new_sc_correct:\n            new_sc_correct_count += 1\n        if sica_correct:\n            sica_correct_count += 1\n\n        if new_sc_correct and sica_correct:\n            a_both += 1\n        elif new_sc_correct and not sica_correct:\n            b += 1\n        elif not new_sc_correct and sica_correct:\n            c += 1\n        else:\n            d_both += 1\n\n    new_sc_pct = new_sc_correct_count / n * 100\n    sica_pct = sica_correct_count / n * 100\n    delta_pp = sica_pct - new_sc_pct\n\n    if b + c == 0:\n        p_value = 1.0\n    else:\n        result = binomtest(min(b, c), b + c, 0.5)\n        p_value = result.pvalue\n\n    if p_value < 0.02:\n        sig = \"**\"\n    elif p_value < 0.05:\n        sig = \"*\"\n    else:\n        sig = \"ns\"\n\n    return {\n        \"exp_id\": exp_info[\"exp_id\"],\n        \"label\": exp_info[\"label\"],\n        \"n\": n,\n        \"new_sc_pct\": round(new_sc_pct, 2),\n        \"sica_pct\": round(sica_pct, 2),\n        \"delta_pp\": round(delta_pp, 2),\n        \"a_both_correct\": a_both,\n        \"b_sc_correct_sica_wrong\": b,\n        \"c_sc_wrong_sica_correct\": c,\n        \"d_both_wrong\": d_both,\n        \"p_value\": p_value,\n        \"sig\": sig,\n    }\n\n\nEXPERIMENTS_25068 = [\n    {\"exp_id\": \"exp-033\", \"label\": \"Mistral-7B FOLIO-204 seed=42\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json\"},\n    {\"exp_id\": \"exp-057\", \"label\": \"Mistral-7B FOLIO-204 T=0.3\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp057_mistral_folio204_t03/exp057_results.json\"},\n    {\"exp_id\": \"exp-058\", \"label\": \"Mistral-7B FOLIO-204 T=0.5\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp058_mistral_folio204_t05/exp058_results.json\"},\n    {\"exp_id\": \"exp-054\", \"label\": \"Mistral-7B FOLIO-204 T=1.0\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp054_mistral_folio204_t10/exp054_results.json\"},\n    {\"exp_id\": \"exp-051-k8\", \"label\": \"Mistral-7B FOLIO-204 K=8\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp051_mistral_k_sensitivity/k8/results.json\"},\n    {\"exp_id\": \"exp-026\", \"label\": \"Qwen2.5-14B FOLIO-204\",\n     \"path\": \"/root/symb_invariant_consensus/results/folio_204_14b/folio_204_results.json\"},\n    {\"exp_id\": \"exp-027\", \"label\": \"Qwen3-14B FOLIO-204\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp027_qwen3_14b_nonthinking/exp027_results.json\"},\n    {\"exp_id\": \"exp-046\", \"label\": \"Mistral-7B PW-600 (sanity)\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp046_mistral_7b_pw600/exp046_results.json\"},\n    {\"exp_id\": \"exp-034\", \"label\": \"Qwen2.5-14B PW-600\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp034_qwen25_14b_proofwriter/exp034_results.json\"},\n]\n\nEXPERIMENTS_16639 = [\n    {\"exp_id\": \"exp-052\", \"label\": \"Mistral-7B FOLIO-204 seed=123\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp052_mistral_folio204_seed123/exp052_results.json\"},\n    {\"exp_id\": \"exp-053\", \"label\": \"Mistral-7B FOLIO-204 seed=456\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp053_mistral_folio204_seed456/exp053_results.json\"},\n    {\"exp_id\": \"exp-039\", \"label\": \"Qwen2.5-14B PW-600\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/results.json\"},\n]\n\n\ndef main():\n    server = sys.argv[1] if len(sys.argv) > 1 else \"25068\"\n    experiments = EXPERIMENTS_25068 if server == \"25068\" else EXPERIMENTS_16639\n\n    all_results = []\n    for exp in experiments:\n        r = compute_mcnemar(exp)\n        all_results.append(r)\n\n    header = f\"{'Exp':<14} {'n':>4} {'NewSC%':>8} {'SICA%':>8} {'D(pp)':>8} {'b':>4} {'c':>4} {'McNemar_p':>12} {'Sig':>5}\"\n    print(header)\n    print(\"-\" * len(header))\n    for r in all_results:\n        if \"error\" in r:\n            print(f\"{r['exp_id']:<14} ERROR: {r['error']}\")\n            continue\n        print(f\"{r['exp_id']:<14} {r['n']:>4} {r['new_sc_pct']:>7.2f}% {r['sica_pct']:>7.2f}% {r['delta_pp']:>+7.2f} {r['b_sc_correct_sica_wrong']:>4} {r['c_sc_wrong_sica_correct']:>4} {r['p_value']:>12.6f} {r['sig']:>5}\")\n\n    out = {\"server\": f\"westd-{server}\", \"results\": all_results}\n    out_path = Path(f\"/root/symb_invariant_consensus/results/mcnemar_recomputed_{server}.json\")\n    with open(out_path, \"w\") as f:\n        json.dump(out, f, indent=2)\n    print(f\"\\nSaved to {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/mcnemar_recompute.py",
    "content": "\"\"\"McNemar exact test recomputation after SC tiebreaking fix.\"\"\"\nimport json\nimport sys\nfrom pathlib import Path\nfrom scipy.stats import binomtest\n\n\ndef normalize_answer(ans):\n    if not ans:\n        return \"\"\n    a = ans.strip().lower()\n    mapping = {\n        \"true\": \"True\", \"false\": \"False\", \"unknown\": \"Unknown\",\n        \"proved\": \"True\", \"disproved\": \"False\",\n    }\n    return mapping.get(a, ans.strip())\n\n\ndef deterministic_sc(vote_dist):\n    \"\"\"Alphabetical tie-breaking: among tied-max answers, pick first alphabetically.\"\"\"\n    if not vote_dist:\n        return \"\"\n    return max(sorted(vote_dist.keys()), key=lambda k: vote_dist[k])\n\n\ndef compute_mcnemar(exp_info):\n    path = Path(exp_info[\"path\"])\n    if not path.exists():\n        return {\"exp_id\": exp_info[\"exp_id\"], \"error\": f\"File not found: {path}\"}\n\n    with open(path) as f:\n        data = json.load(f)\n\n    results = data.get(\"results\", [])\n    n = len(results)\n\n    b = 0\n    c = 0\n    a_both = 0\n    d_both = 0\n    new_sc_correct_count = 0\n    sica_correct_count = 0\n\n    for r in results:\n        gt = r.get(\"ground_truth\", \"\")\n        sica_correct = r.get(\"sica_correct\", False)\n        vote_dist = r.get(\"sc_vote_distribution\", {})\n        new_sc_answer = deterministic_sc(vote_dist)\n        new_sc_correct = (normalize_answer(new_sc_answer) == normalize_answer(gt))\n\n        if new_sc_correct:\n            new_sc_correct_count += 1\n        if sica_correct:\n            sica_correct_count += 1\n\n        if new_sc_correct and sica_correct:\n            a_both += 1\n        elif new_sc_correct and not sica_correct:\n            b += 1\n        elif not new_sc_correct and sica_correct:\n            c += 1\n        else:\n            d_both += 1\n\n    new_sc_pct = new_sc_correct_count / n * 100\n    sica_pct = sica_correct_count / n * 100\n    delta_pp = sica_pct - new_sc_pct\n\n    if b + c == 0:\n        p_value = 1.0\n    else:\n        result = binomtest(min(b, c), b + c, 0.5)\n        p_value = result.pvalue\n\n    if p_value < 0.02:\n        sig = \"**\"\n    elif p_value < 0.05:\n        sig = \"*\"\n    else:\n        sig = \"ns\"\n\n    return {\n        \"exp_id\": exp_info[\"exp_id\"],\n        \"label\": exp_info[\"label\"],\n        \"n\": n,\n        \"new_sc_pct\": round(new_sc_pct, 2),\n        \"sica_pct\": round(sica_pct, 2),\n        \"delta_pp\": round(delta_pp, 2),\n        \"a_both_correct\": a_both,\n        \"b_sc_correct_sica_wrong\": b,\n        \"c_sc_wrong_sica_correct\": c,\n        \"d_both_wrong\": d_both,\n        \"p_value\": p_value,\n        \"sig\": sig,\n    }\n\n\nEXPERIMENTS_25068 = [\n    {\"exp_id\": \"exp-033\", \"label\": \"Mistral-7B FOLIO-204 seed=42\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json\"},\n    {\"exp_id\": \"exp-057\", \"label\": \"Mistral-7B FOLIO-204 T=0.3\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp057_mistral_folio204_t03/exp057_results.json\"},\n    {\"exp_id\": \"exp-058\", \"label\": \"Mistral-7B FOLIO-204 T=0.5\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp058_mistral_folio204_t05/exp058_results.json\"},\n    {\"exp_id\": \"exp-054\", \"label\": \"Mistral-7B FOLIO-204 T=1.0\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp054_mistral_folio204_t10/exp054_results.json\"},\n    {\"exp_id\": \"exp-051-k8\", \"label\": \"Mistral-7B FOLIO-204 K=8\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp051_mistral_k_sensitivity/k8/results.json\"},\n    {\"exp_id\": \"exp-026\", \"label\": \"Qwen2.5-14B FOLIO-204\",\n     \"path\": \"/root/symb_invariant_consensus/results/folio_204_14b/folio_204_results.json\"},\n    {\"exp_id\": \"exp-027\", \"label\": \"Qwen3-14B FOLIO-204\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp027_qwen3_14b_nonthinking/exp027_results.json\"},\n    {\"exp_id\": \"exp-046\", \"label\": \"Mistral-7B PW-600 (sanity)\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp046_mistral_7b_pw600/exp046_results.json\"},\n    {\"exp_id\": \"exp-034\", \"label\": \"Qwen2.5-14B PW-600\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp034_qwen25_14b_proofwriter/exp034_results.json\"},\n]\n\nEXPERIMENTS_16639 = [\n    {\"exp_id\": \"exp-052\", \"label\": \"Mistral-7B FOLIO-204 seed=123\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp052_mistral_folio204_seed123/exp052_results.json\"},\n    {\"exp_id\": \"exp-053\", \"label\": \"Mistral-7B FOLIO-204 seed=456\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp053_mistral_folio204_seed456/exp053_results.json\"},\n    {\"exp_id\": \"exp-039\", \"label\": \"Qwen2.5-14B PW-600\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/results.json\"},\n]\n\n\ndef main():\n    server = sys.argv[1] if len(sys.argv) > 1 else \"25068\"\n    experiments = EXPERIMENTS_25068 if server == \"25068\" else EXPERIMENTS_16639\n\n    all_results = []\n    for exp in experiments:\n        r = compute_mcnemar(exp)\n        all_results.append(r)\n\n    header = f\"{'Exp':<14} {'n':>4} {'NewSC%':>8} {'SICA%':>8} {'D(pp)':>8} {'b':>4} {'c':>4} {'McNemar_p':>12} {'Sig':>5}\"\n    print(header)\n    print(\"-\" * len(header))\n    for r in all_results:\n        if \"error\" in r:\n            print(f\"{r['exp_id']:<14} ERROR: {r['error']}\")\n            continue\n        print(f\"{r['exp_id']:<14} {r['n']:>4} {r['new_sc_pct']:>7.2f}% {r['sica_pct']:>7.2f}% {r['delta_pp']:>+7.2f} {r['b_sc_correct_sica_wrong']:>4} {r['c_sc_wrong_sica_correct']:>4} {r['p_value']:>12.6f} {r['sig']:>5}\")\n\n    out = {\"server\": f\"westd-{server}\", \"results\": all_results}\n    out_path = Path(f\"/root/symb_invariant_consensus/results/mcnemar_recomputed_{server}.json\")\n    with open(out_path, \"w\") as f:\n        json.dump(out, f, indent=2)\n    print(f\"\\nSaved to {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-19T06:27:42.717627+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/mcnemar_recompute.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-19T06:27:42.717887+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "cat > /root/symb_invariant_consensus/mcnemar_recompute.py << 'HEREDOC'\n\"\"\"McNemar exact test recomputation after SC tiebreaking fix.\"\"\"\nimport json\nimport sys\nfrom pathlib import Path\nfrom scipy.stats import binomtest\n\n\ndef normalize_answer(ans):\n    if not ans:\n        return \"\"\n    a = ans.strip().lower()\n    mapping = {\n        \"true\": \"True\", \"false\": \"False\", \"unknown\": \"Unknown\",\n        \"proved\": \"True\", \"disproved\": \"False\",\n    }\n    return mapping.get(a, ans.strip())\n\n\ndef deterministic_sc(vote_dist):\n    if not vote_dist:\n        return \"\"\n    return max(sorted(vote_dist.keys()), key=lambda k: vote_dist[k])\n\n\ndef compute_mcnemar(exp_info):\n    path = Path(exp_info[\"path\"])\n    if not path.exists():\n        return {\"exp_id\": exp_info[\"exp_id\"], \"error\": f\"File not found: {path}\"}\n\n    with open(path) as f:\n        data = json.load(f)\n\n    results = data.get(\"results\", [])\n    n = len(results)\n\n    b = 0\n    c = 0\n    a_both = 0\n    d_both = 0\n    new_sc_correct_count = 0\n    sica_correct_count = 0\n\n    for r in results:\n        gt = r.get(\"ground_truth\", \"\")\n        sica_correct = r.get(\"sica_correct\", False)\n        vote_dist = r.get(\"sc_vote_distribution\", {})\n        new_sc_answer = deterministic_sc(vote_dist)\n        new_sc_correct = (normalize_answer(new_sc_answer) == normalize_answer(gt))\n\n        if new_sc_correct:\n            new_sc_correct_count += 1\n        if sica_correct:\n            sica_correct_count += 1\n\n        if new_sc_correct and sica_correct:\n            a_both += 1\n        elif new_sc_correct and not sica_correct:\n            b += 1\n        elif not new_sc_correct and sica_correct:\n            c += 1\n        else:\n            d_both += 1\n\n    new_sc_pct = new_sc_correct_count / n * 100\n    sica_pct = sica_correct_count / n * 100\n    delta_pp = sica_pct - new_sc_pct\n\n    if b + c == 0:\n        p_value = 1.0\n    else:\n        result = binomtest(min(b, c), b + c, 0.5)\n        p_value = result.pvalue\n\n    if p_value < 0.02:\n        sig = \"**\"\n    elif p_value < 0.05:\n        sig = \"*\"\n    else:\n        sig = \"ns\"\n\n    return {\n        \"exp_id\": exp_info[\"exp_id\"],\n        \"label\": exp_info[\"label\"],\n        \"n\": n,\n        \"new_sc_pct\": round(new_sc_pct, 2),\n        \"sica_pct\": round(sica_pct, 2),\n        \"delta_pp\": round(delta_pp, 2),\n        \"a_both_correct\": a_both,\n        \"b_sc_correct_sica_wrong\": b,\n        \"c_sc_wrong_sica_correct\": c,\n        \"d_both_wrong\": d_both,\n        \"p_value\": p_value,\n        \"sig\": sig,\n    }\n\n\nEXPERIMENTS_25068 = [\n    {\"exp_id\": \"exp-033\", \"label\": \"Mistral-7B FOLIO-204 seed=42\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json\"},\n    {\"exp_id\": \"exp-057\", \"label\": \"Mistral-7B FOLIO-204 T=0.3\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp057_mistral_folio204_t03/exp057_results.json\"},\n    {\"exp_id\": \"exp-058\", \"label\": \"Mistral-7B FOLIO-204 T=0.5\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp058_mistral_folio204_t05/exp058_results.json\"},\n    {\"exp_id\": \"exp-054\", \"label\": \"Mistral-7B FOLIO-204 T=1.0\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp054_mistral_folio204_t10/exp054_results.json\"},\n    {\"exp_id\": \"exp-051-k8\", \"label\": \"Mistral-7B FOLIO-204 K=8\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp051_mistral_k_sensitivity/k8/results.json\"},\n    {\"exp_id\": \"exp-026\", \"label\": \"Qwen2.5-14B FOLIO-204\",\n     \"path\": \"/root/symb_invariant_consensus/results/folio_204_14b/folio_204_results.json\"},\n    {\"exp_id\": \"exp-027\", \"label\": \"Qwen3-14B FOLIO-204\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp027_qwen3_14b_nonthinking/exp027_results.json\"},\n    {\"exp_id\": \"exp-046\", \"label\": \"Mistral-7B PW-600 (sanity)\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp046_mistral_7b_pw600/exp046_results.json\"},\n    {\"exp_id\": \"exp-034\", \"label\": \"Qwen2.5-14B PW-600\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp034_qwen25_14b_proofwriter/exp034_results.json\"},\n]\n\nEXPERIMENTS_16639 = [\n    {\"exp_id\": \"exp-052\", \"label\": \"Mistral-7B FOLIO-204 seed=123\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp052_mistral_folio204_seed123/exp052_results.json\"},\n    {\"exp_id\": \"exp-053\", \"label\": \"Mistral-7B FOLIO-204 seed=456\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp053_mistral_folio204_seed456/exp053_results.json\"},\n    {\"exp_id\": \"exp-039\", \"label\": \"Qwen2.5-14B PW-600\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/results.json\"},\n]\n\n\ndef main():\n    server = sys.argv[1] if len(sys.argv) > 1 else \"25068\"\n    experiments = EXPERIMENTS_25068 if server == \"25068\" else EXPERIMENTS_16639\n\n    all_results = []\n    for exp in experiments:\n        r = compute_mcnemar(exp)\n        all_results.append(r)\n\n    header = f\"{'Exp':<14} {'n':>4} {'NewSC%':>8} {'SICA%':>8} {'D(pp)':>8} {'b':>4} {'c':>4} {'McNemar_p':>12} {'Sig':>5}\"\n    print(header)\n    print(\"-\" * len(header))\n    for r in all_results:\n        if \"error\" in r:\n            print(f\"{r['exp_id']:<14} ERROR: {r['error']}\")\n            continue\n        print(f\"{r['exp_id']:<14} {r['n']:>4} {r['new_sc_pct']:>7.2f}% {r['sica_pct']:>7.2f}% {r['delta_pp']:>+7.2f} {r['b_sc_correct_sica_wrong']:>4} {r['c_sc_wrong_sica_correct']:>4} {r['p_value']:>12.6f} {r['sig']:>5}\")\n\n    out = {\"server\": f\"westd-{server}\", \"results\": all_results}\n    out_path = Path(f\"/root/symb_invariant_consensus/results/mcnemar_recomputed_{server}.json\")\n    with open(out_path, \"w\") as f:\n        json.dump(out, f, indent=2)\n    print(f\"\\nSaved to {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nHEREDOC"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "cat > /root/symb_invariant_consensus/mcnemar_recompute.py << 'HEREDOC'\n\"\"\"McNemar exact test recomputation after SC tiebreaking fix.\"\"\"\nimport json\nimport sys\nfrom pathlib import Path\nfrom scipy.stats import binomtest\n\n\ndef normalize_answer(ans):\n    if not ans:\n        return \"\"\n    a = ans.strip().lower()\n    mapping = {\n        \"true\": \"True\", \"false\": \"False\", \"unknown\": \"Unknown\",\n        \"proved\": \"True\", \"disproved\": \"False\",\n    }\n    return mapping.get(a, ans.strip())\n\n\ndef deterministic_sc(vote_dist):\n    if not vote_dist:\n        return \"\"\n    return max(sorted(vote_dist.keys()), key=lambda k: vote_dist[k])\n\n\ndef compute_mcnemar(exp_info):\n    path = Path(exp_info[\"path\"])\n    if not path.exists():\n        return {\"exp_id\": exp_info[\"exp_id\"], \"error\": f\"File not found: {path}\"}\n\n    with open(path) as f:\n        data = json.load(f)\n\n    results = data.get(\"results\", [])\n    n = len(results)\n\n    b = 0\n    c = 0\n    a_both = 0\n    d_both = 0\n    new_sc_correct_count = 0\n    sica_correct_count = 0\n\n    for r in results:\n        gt = r.get(\"ground_truth\", \"\")\n        sica_correct = r.get(\"sica_correct\", False)\n        vote_dist = r.get(\"sc_vote_distribution\", {})\n        new_sc_answer = deterministic_sc(vote_dist)\n        new_sc_correct = (normalize_answer(new_sc_answer) == normalize_answer(gt))\n\n        if new_sc_correct:\n            new_sc_correct_count += 1\n        if sica_correct:\n            sica_correct_count += 1\n\n        if new_sc_correct and sica_correct:\n            a_both += 1\n        elif new_sc_correct and not sica_correct:\n            b += 1\n        elif not new_sc_correct and sica_correct:\n            c += 1\n        else:\n            d_both += 1\n\n    new_sc_pct = new_sc_correct_count / n * 100\n    sica_pct = sica_correct_count / n * 100\n    delta_pp = sica_pct - new_sc_pct\n\n    if b + c == 0:\n        p_value = 1.0\n    else:\n        result = binomtest(min(b, c), b + c, 0.5)\n        p_value = result.pvalue\n\n    if p_value < 0.02:\n        sig = \"**\"\n    elif p_value < 0.05:\n        sig = \"*\"\n    else:\n        sig = \"ns\"\n\n    return {\n        \"exp_id\": exp_info[\"exp_id\"],\n        \"label\": exp_info[\"label\"],\n        \"n\": n,\n        \"new_sc_pct\": round(new_sc_pct, 2),\n        \"sica_pct\": round(sica_pct, 2),\n        \"delta_pp\": round(delta_pp, 2),\n        \"a_both_correct\": a_both,\n        \"b_sc_correct_sica_wrong\": b,\n        \"c_sc_wrong_sica_correct\": c,\n        \"d_both_wrong\": d_both,\n        \"p_value\": p_value,\n        \"sig\": sig,\n    }\n\n\nEXPERIMENTS_25068 = [\n    {\"exp_id\": \"exp-033\", \"label\": \"Mistral-7B FOLIO-204 seed=42\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json\"},\n    {\"exp_id\": \"exp-057\", \"label\": \"Mistral-7B FOLIO-204 T=0.3\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp057_mistral_folio204_t03/exp057_results.json\"},\n    {\"exp_id\": \"exp-058\", \"label\": \"Mistral-7B FOLIO-204 T=0.5\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp058_mistral_folio204_t05/exp058_results.json\"},\n    {\"exp_id\": \"exp-054\", \"label\": \"Mistral-7B FOLIO-204 T=1.0\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp054_mistral_folio204_t10/exp054_results.json\"},\n    {\"exp_id\": \"exp-051-k8\", \"label\": \"Mistral-7B FOLIO-204 K=8\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp051_mistral_k_sensitivity/k8/results.json\"},\n    {\"exp_id\": \"exp-026\", \"label\": \"Qwen2.5-14B FOLIO-204\",\n     \"path\": \"/root/symb_invariant_consensus/results/folio_204_14b/folio_204_results.json\"},\n    {\"exp_id\": \"exp-027\", \"label\": \"Qwen3-14B FOLIO-204\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp027_qwen3_14b_nonthinking/exp027_results.json\"},\n    {\"exp_id\": \"exp-046\", \"label\": \"Mistral-7B PW-600 (sanity)\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp046_mistral_7b_pw600/exp046_results.json\"},\n    {\"exp_id\": \"exp-034\", \"label\": \"Qwen2.5-14B PW-600\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp034_qwen25_14b_proofwriter/exp034_results.json\"},\n]\n\nEXPERIMENTS_16639 = [\n    {\"exp_id\": \"exp-052\", \"label\": \"Mistral-7B FOLIO-204 seed=123\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp052_mistral_folio204_seed123/exp052_results.json\"},\n    {\"exp_id\": \"exp-053\", \"label\": \"Mistral-7B FOLIO-204 seed=456\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp053_mistral_folio204_seed456/exp053_results.json\"},\n    {\"exp_id\": \"exp-039\", \"label\": \"Qwen2.5-14B PW-600\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/results.json\"},\n]\n\n\ndef main():\n    server = sys.argv[1] if len(sys.argv) > 1 else \"25068\"\n    experiments = EXPERIMENTS_25068 if server == \"25068\" else EXPERIMENTS_16639\n\n    all_results = []\n    for exp in experiments:\n        r = compute_mcnemar(exp)\n        all_results.append(r)\n\n    header = f\"{'Exp':<14} {'n':>4} {'NewSC%':>8} {'SICA%':>8} {'D(pp)':>8} {'b':>4} {'c':>4} {'McNemar_p':>12} {'Sig':>5}\"\n    print(header)\n    print(\"-\" * len(header))\n    for r in all_results:\n        if \"error\" in r:\n            print(f\"{r['exp_id']:<14} ERROR: {r['error']}\")\n            continue\n        print(f\"{r['exp_id']:<14} {r['n']:>4} {r['new_sc_pct']:>7.2f}% {r['sica_pct']:>7.2f}% {r['delta_pp']:>+7.2f} {r['b_sc_correct_sica_wrong']:>4} {r['c_sc_wrong_sica_correct']:>4} {r['p_value']:>12.6f} {r['sig']:>5}\")\n\n    out = {\"server\": f\"westd-{server}\", \"results\": all_results}\n    out_path = Path(f\"/root/symb_invariant_consensus/results/mcnemar_recomputed_{server}.json\")\n    with open(out_path, \"w\") as f:\n        json.dump(out, f, indent=2)\n    print(f\"\\nSaved to {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nHEREDOC"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-19T06:27:42.718177+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.59}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-19T06:27:42.718370+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/symb_invariant_consensus/mcnemar_recompute.py 25068"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/symb_invariant_consensus/mcnemar_recompute.py 25068"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-19T06:27:42.718581+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Exp               n   NewSC%    SICA%    D(pp)    b    c    McNemar_p   Sig\\n---------------------------------------------------------------------------\\nexp-033         204   55.88%   59.31%   +3.43    3   10     0.092285    ns\\nexp-057         204   58.33%   56.86%   -1.47    7    4     0.548828    ns\\nexp-058         204   58.33%   57.35%   -0.98    3    1     0.625000    ns\\nexp-054         204   55.39%   55.39%   +0.00    5    5     1.000000    ns\\nexp-051-k8      204   58.33%   56.37%   -1.96    7    3     0.343750    ns\\nexp-026         204   75.49%   74.51%   -0.98    3    1     0.625000    ns\\nexp-027         204   84.80%   84.31%   -0.49    4    3     1.000000    ns\\nexp-046         600   39.33%   36.50%   -2.83   30   13     0.013718    **\\nexp-034         600   71.33%   70.83%   -0.50   14   11     0.690038    ns\\n\\nSaved to /root/symb_invariant_consensus/results/mcnemar_recomputed_25068.json\\n\", \"stderr\": \"Error while loading conda entry point: conda-libmamba-solver (module 'libmambapy' has no attribute 'QueryFormat')\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.23}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-19T06:27:42.718841+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-16639",
  "command": "cat > /root/symb_invariant_consensus/mcnemar_recompute.py << 'HEREDOC'\n\"\"\"McNemar exact test recomputation after SC tiebreaking fix.\"\"\"\nimport json\nimport sys\nfrom pathlib import Path\nfrom scipy.stats import binomtest\n\n\ndef normalize_answer(ans):\n    if not ans:\n        return \"\"\n    a = ans.strip().lower()\n    mapping = {\n        \"true\": \"True\", \"false\": \"False\", \"unknown\": \"Unknown\",\n        \"proved\": \"True\", \"disproved\": \"False\",\n    }\n    return mapping.get(a, ans.strip())\n\n\ndef deterministic_sc(vote_dist):\n    if not vote_dist:\n        return \"\"\n    return max(sorted(vote_dist.keys()), key=lambda k: vote_dist[k])\n\n\ndef compute_mcnemar(exp_info):\n    path = Path(exp_info[\"path\"])\n    if not path.exists():\n        return {\"exp_id\": exp_info[\"exp_id\"], \"error\": f\"File not found: {path}\"}\n\n    with open(path) as f:\n        data = json.load(f)\n\n    results = data.get(\"results\", [])\n    n = len(results)\n\n    b = 0\n    c = 0\n    a_both = 0\n    d_both = 0\n    new_sc_correct_count = 0\n    sica_correct_count = 0\n\n    for r in results:\n        gt = r.get(\"ground_truth\", \"\")\n        sica_correct = r.get(\"sica_correct\", False)\n        vote_dist = r.get(\"sc_vote_distribution\", {})\n        new_sc_answer = deterministic_sc(vote_dist)\n        new_sc_correct = (normalize_answer(new_sc_answer) == normalize_answer(gt))\n\n        if new_sc_correct:\n            new_sc_correct_count += 1\n        if sica_correct:\n            sica_correct_count += 1\n\n        if new_sc_correct and sica_correct:\n            a_both += 1\n        elif new_sc_correct and not sica_correct:\n            b += 1\n        elif not new_sc_correct and sica_correct:\n            c += 1\n        else:\n            d_both += 1\n\n    new_sc_pct = new_sc_correct_count / n * 100\n    sica_pct = sica_correct_count / n * 100\n    delta_pp = sica_pct - new_sc_pct\n\n    if b + c == 0:\n        p_value = 1.0\n    else:\n        result = binomtest(min(b, c), b + c, 0.5)\n        p_value = result.pvalue\n\n    if p_value < 0.02:\n        sig = \"**\"\n    elif p_value < 0.05:\n        sig = \"*\"\n    else:\n        sig = \"ns\"\n\n    return {\n        \"exp_id\": exp_info[\"exp_id\"],\n        \"label\": exp_info[\"label\"],\n        \"n\": n,\n        \"new_sc_pct\": round(new_sc_pct, 2),\n        \"sica_pct\": round(sica_pct, 2),\n        \"delta_pp\": round(delta_pp, 2),\n        \"a_both_correct\": a_both,\n        \"b_sc_correct_sica_wrong\": b,\n        \"c_sc_wrong_sica_correct\": c,\n        \"d_both_wrong\": d_both,\n        \"p_value\": p_value,\n        \"sig\": sig,\n    }\n\n\nEXPERIMENTS_16639 = [\n    {\"exp_id\": \"exp-052\", \"label\": \"Mistral-7B FOLIO-204 seed=123\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp052_mistral_folio204_seed123/exp052_results.json\"},\n    {\"exp_id\": \"exp-053\", \"label\": \"Mistral-7B FOLIO-204 seed=456\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp053_mistral_folio204_seed456/exp053_results.json\"},\n    {\"exp_id\": \"exp-039\", \"label\": \"Qwen2.5-14B PW-600\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/results.json\"},\n]\n\n\ndef main():\n    experiments = EXPERIMENTS_16639\n\n    all_results = []\n    for exp in experiments:\n        r = compute_mcnemar(exp)\n        all_results.append(r)\n\n    header = f\"{'Exp':<14} {'n':>4} {'NewSC%':>8} {'SICA%':>8} {'D(pp)':>8} {'b':>4} {'c':>4} {'McNemar_p':>12} {'Sig':>5}\"\n    print(header)\n    print(\"-\" * len(header))\n    for r in all_results:\n        if \"error\" in r:\n            print(f\"{r['exp_id']:<14} ERROR: {r['error']}\")\n            continue\n        print(f\"{r['exp_id']:<14} {r['n']:>4} {r['new_sc_pct']:>7.2f}% {r['sica_pct']:>7.2f}% {r['delta_pp']:>+7.2f} {r['b_sc_correct_sica_wrong']:>4} {r['c_sc_wrong_sica_correct']:>4} {r['p_value']:>12.6f} {r['sig']:>5}\")\n\n    out = {\"server\": \"westd-16639\", \"results\": all_results}\n    out_path = Path(\"/root/symb_invariant_consensus/results/mcnemar_recomputed_16639.json\")\n    with open(out_path, \"w\") as f:\n        json.dump(out, f, indent=2)\n    print(f\"\\nSaved to {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nHEREDOC"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-16639",
    "command": "cat > /root/symb_invariant_consensus/mcnemar_recompute.py << 'HEREDOC'\n\"\"\"McNemar exact test recomputation after SC tiebreaking fix.\"\"\"\nimport json\nimport sys\nfrom pathlib import Path\nfrom scipy.stats import binomtest\n\n\ndef normalize_answer(ans):\n    if not ans:\n        return \"\"\n    a = ans.strip().lower()\n    mapping = {\n        \"true\": \"True\", \"false\": \"False\", \"unknown\": \"Unknown\",\n        \"proved\": \"True\", \"disproved\": \"False\",\n    }\n    return mapping.get(a, ans.strip())\n\n\ndef deterministic_sc(vote_dist):\n    if not vote_dist:\n        return \"\"\n    return max(sorted(vote_dist.keys()), key=lambda k: vote_dist[k])\n\n\ndef compute_mcnemar(exp_info):\n    path = Path(exp_info[\"path\"])\n    if not path.exists():\n        return {\"exp_id\": exp_info[\"exp_id\"], \"error\": f\"File not found: {path}\"}\n\n    with open(path) as f:\n        data = json.load(f)\n\n    results = data.get(\"results\", [])\n    n = len(results)\n\n    b = 0\n    c = 0\n    a_both = 0\n    d_both = 0\n    new_sc_correct_count = 0\n    sica_correct_count = 0\n\n    for r in results:\n        gt = r.get(\"ground_truth\", \"\")\n        sica_correct = r.get(\"sica_correct\", False)\n        vote_dist = r.get(\"sc_vote_distribution\", {})\n        new_sc_answer = deterministic_sc(vote_dist)\n        new_sc_correct = (normalize_answer(new_sc_answer) == normalize_answer(gt))\n\n        if new_sc_correct:\n            new_sc_correct_count += 1\n        if sica_correct:\n            sica_correct_count += 1\n\n        if new_sc_correct and sica_correct:\n            a_both += 1\n        elif new_sc_correct and not sica_correct:\n            b += 1\n        elif not new_sc_correct and sica_correct:\n            c += 1\n        else:\n            d_both += 1\n\n    new_sc_pct = new_sc_correct_count / n * 100\n    sica_pct = sica_correct_count / n * 100\n    delta_pp = sica_pct - new_sc_pct\n\n    if b + c == 0:\n        p_value = 1.0\n    else:\n        result = binomtest(min(b, c), b + c, 0.5)\n        p_value = result.pvalue\n\n    if p_value < 0.02:\n        sig = \"**\"\n    elif p_value < 0.05:\n        sig = \"*\"\n    else:\n        sig = \"ns\"\n\n    return {\n        \"exp_id\": exp_info[\"exp_id\"],\n        \"label\": exp_info[\"label\"],\n        \"n\": n,\n        \"new_sc_pct\": round(new_sc_pct, 2),\n        \"sica_pct\": round(sica_pct, 2),\n        \"delta_pp\": round(delta_pp, 2),\n        \"a_both_correct\": a_both,\n        \"b_sc_correct_sica_wrong\": b,\n        \"c_sc_wrong_sica_correct\": c,\n        \"d_both_wrong\": d_both,\n        \"p_value\": p_value,\n        \"sig\": sig,\n    }\n\n\nEXPERIMENTS_16639 = [\n    {\"exp_id\": \"exp-052\", \"label\": \"Mistral-7B FOLIO-204 seed=123\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp052_mistral_folio204_seed123/exp052_results.json\"},\n    {\"exp_id\": \"exp-053\", \"label\": \"Mistral-7B FOLIO-204 seed=456\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp053_mistral_folio204_seed456/exp053_results.json\"},\n    {\"exp_id\": \"exp-039\", \"label\": \"Qwen2.5-14B PW-600\",\n     \"path\": \"/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/results.json\"},\n]\n\n\ndef main():\n    experiments = EXPERIMENTS_16639\n\n    all_results = []\n    for exp in experiments:\n        r = compute_mcnemar(exp)\n        all_results.append(r)\n\n    header = f\"{'Exp':<14} {'n':>4} {'NewSC%':>8} {'SICA%':>8} {'D(pp)':>8} {'b':>4} {'c':>4} {'McNemar_p':>12} {'Sig':>5}\"\n    print(header)\n    print(\"-\" * len(header))\n    for r in all_results:\n        if \"error\" in r:\n            print(f\"{r['exp_id']:<14} ERROR: {r['error']}\")\n            continue\n        print(f\"{r['exp_id']:<14} {r['n']:>4} {r['new_sc_pct']:>7.2f}% {r['sica_pct']:>7.2f}% {r['delta_pp']:>+7.2f} {r['b_sc_correct_sica_wrong']:>4} {r['c_sc_wrong_sica_correct']:>4} {r['p_value']:>12.6f} {r['sig']:>5}\")\n\n    out = {\"server\": \"westd-16639\", \"results\": all_results}\n    out_path = Path(\"/root/symb_invariant_consensus/results/mcnemar_recomputed_16639.json\")\n    with open(out_path, \"w\") as f:\n        json.dump(out, f, indent=2)\n    print(f\"\\nSaved to {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nHEREDOC"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-19T06:27:42.719130+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-19T06:27:42.719325+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-16639",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/symb_invariant_consensus/mcnemar_recompute.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-16639",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/symb_invariant_consensus/mcnemar_recompute.py"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-19T06:27:42.719527+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Exp               n   NewSC%    SICA%    D(pp)    b    c    McNemar_p   Sig\\n---------------------------------------------------------------------------\\nexp-052         204   54.41%   57.35%   +2.94    1    7     0.070312    ns\\nexp-053         204   55.88%   55.88%   +0.00    3    3     1.000000    ns\\nexp-039         600   74.00%   71.50%   -2.50   23    8     0.010674    **\\n\\nSaved to /root/symb_invariant_consensus/results/mcnemar_recomputed_16639.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_computation_mcnemar-recompute_20260519T061929",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 75 · 2026-05-19T06:27:42.719829+00:00_

全部完成。汇总结果：

| Exp | n | 新SC% | SICA% | 新Δ(pp) | b(SC对SICA错) | c(SC错SICA对) | McNemar p | 显著性 |
|-----|---|-------|-------|---------|---------------|---------------|-----------|--------|
| exp-033 (seed42) | 204 | 55.88 | 59.31 | +3.43 | 3 | 10 | 0.0923 | ns |
| exp-052 (seed123) | 204 | 54.41 | 57.35 | +2.94 | 1 | 7 | 0.0703 | ns |
| exp-053 (seed456) | 204 | 55.88 | 55.88 | +0.00 | 3 | 3 | 1.0000 | ns |
| exp-057 (T=0.3) | 204 | 58.33 | 56.86 | -1.47 | 7 | 4 | 0.5488 | ns |
| exp-058 (T=0.5) | 204 | 58.33 | 57.35 | -0.98 | 3 | 1 | 0.6250 | ns |
| exp-054 (T=1.0) | 204 | 55.39 | 55.39 | +0.00 | 5 | 5 | 1.0000 | ns |
| exp-051 (K=8) | 204 | 58.33 | 56.37 | -1.96 | 7 | 3 | 0.3438 | ns |
| exp-026 (Qwen2.5-14B FOLIO) | 204 | 75.49 | 74.51 | -0.98 | 3 | 1 | 0.6250 | ns |
| exp-027 (Qwen3-14B FOLIO) | 204 | 84.80 | 84.31 | -0.49 | 4 | 3 | 1.0000 | ns |
| exp-034 (Qwen2.5-14B PW-600) | 600 | 71.33 | 70.83 | -0.50 | 14 | 11 | 0.6900 | ns |
| exp-039 (Qwen2.5-14B PW-600 v2) | 600 | 74.00 | 71.50 | -2.50 | 23 | 8 | 0.0107 | ** |
| exp-046 (Mistral PW-600, sanity) | 600 | 39.33 | 36.50 | -2.83 | 30 | 13 | 0.0137 | ** |

结论：
- **exp-046** (SC 未变，sanity check): p=0.0137**，与之前一致，SC 显著优于 SICA
- **exp-039**: p=0.0107**，SC 显著优于 SICA（b=23 > c=8）
- 其余 10 个实验均无显著差异（ns）
- exp-053/exp-054 的 Δ=0.00pp 确认 b=c（分别为 3=3 和 5=5）

JSON 结果已保存：
- `westd-25068:/root/symb_invariant_consensus/results/mcnemar_recomputed_25068.json`
- `westd-16639:/root/symb_invariant_consensus/results/mcnemar_recomputed_16639.json`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_computation_mcnemar-recompute_20260519T061929"
}
```

</details>

---
