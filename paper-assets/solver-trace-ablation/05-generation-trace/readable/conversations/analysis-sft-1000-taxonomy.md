# analysis sft 1000 taxonomy

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_analysis_sft-1000-taxonomy_20260515T153612.jsonl`
- **Structured JSON:** [`3ca2b9d38080c5386155.json`](../../sessions/3c/3ca2b9d38080c5386155.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-15T15:37:47.772514+00:00_

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
  "session": "worker_analysis_sft-1000-taxonomy_20260515T153612",
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

_source line 2 · 2026-05-15T15:37:47.772879+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sft-1000-taxonomy_20260515T153612",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T15:37:47.773051+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "cat /root/autodl-tmp/outputs/plan009_sft_baseline_s42_1000/classify_h7_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_sft-1000-taxonomy_20260515T153612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "cat /root/autodl-tmp/outputs/plan009_sft_baseline_s42_1000/classify_h7_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T15:37:47.773187+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "cat /root/autodl-tmp/outputs/plan009_sft_baseline_s43_1000/classify_h7_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_sft-1000-taxonomy_20260515T153612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "cat /root/autodl-tmp/outputs/plan009_sft_baseline_s43_1000/classify_h7_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-15T15:37:47.773343+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"plan009_sft_baseline_s42_1000\\\": {\\n    \\\"n_total\\\": 100,\\n    \\\"n_proved\\\": 13,\\n    \\\"h7_strict_count\\\": 0,\\n    \\\"h7_strict_rate\\\": 0.0,\\n    \\\"h1_strict_count\\\": 1,\\n    \\\"h1_strict_rate\\\": 0.0769,\\n    \\\"h8_conjunction_collapse_count\\\": 0,\\n    \\\"h8_conjunction_collapse_rate\\\": 0.0,\\n    \\\"conclusion_in_premise_count\\\": 1,\\n    \\\"conclusion_in_premise_rate\\\": 0.0769,\\n    \\\"h7_relaxed_count\\\": 0,\\n    \\\"h7_relaxed_rate\\\": 0.0,\\n    \\\"single_premise_count\\\": 0,\\n    \\\"single_premise_rate\\\": 0.0,\\n    \\\"isr_1_count\\\": 0,\\n    \\\"isr_1_rate\\\": 0.0,\\n    \\\"content_independent_count\\\": 0,\\n    \\\"content_independent_rate\\\": 0.0,\\n    \\\"genuine_count\\\": 12,\\n    \\\"genuine_rate\\\": 0.9231\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.26}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sft-1000-taxonomy_20260515T153612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T15:37:47.773497+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"plan009_sft_baseline_s43_1000\\\": {\\n    \\\"n_total\\\": 100,\\n    \\\"n_proved\\\": 11,\\n    \\\"h7_strict_count\\\": 0,\\n    \\\"h7_strict_rate\\\": 0.0,\\n    \\\"h1_strict_count\\\": 1,\\n    \\\"h1_strict_rate\\\": 0.0909,\\n    \\\"h8_conjunction_collapse_count\\\": 0,\\n    \\\"h8_conjunction_collapse_rate\\\": 0.0,\\n    \\\"conclusion_in_premise_count\\\": 1,\\n    \\\"conclusion_in_premise_rate\\\": 0.0909,\\n    \\\"h7_relaxed_count\\\": 0,\\n    \\\"h7_relaxed_rate\\\": 0.0,\\n    \\\"single_premise_count\\\": 0,\\n    \\\"single_premise_rate\\\": 0.0,\\n    \\\"isr_1_count\\\": 1,\\n    \\\"isr_1_rate\\\": 0.0909,\\n    \\\"content_independent_count\\\": 0,\\n    \\\"content_independent_rate\\\": 0.0,\\n    \\\"genuine_count\\\": 10,\\n    \\\"genuine_rate\\\": 0.9091\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sft-1000-taxonomy_20260515T153612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T15:37:47.773639+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "cat /root/autodl-tmp/outputs/plan009_sft_baseline_s44_1000/classify_h7_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_sft-1000-taxonomy_20260515T153612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "cat /root/autodl-tmp/outputs/plan009_sft_baseline_s44_1000/classify_h7_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T15:37:47.773812+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"plan009_sft_baseline_s44_1000\\\": {\\n    \\\"n_total\\\": 100,\\n    \\\"n_proved\\\": 15,\\n    \\\"h7_strict_count\\\": 0,\\n    \\\"h7_strict_rate\\\": 0.0,\\n    \\\"h1_strict_count\\\": 1,\\n    \\\"h1_strict_rate\\\": 0.0667,\\n    \\\"h8_conjunction_collapse_count\\\": 0,\\n    \\\"h8_conjunction_collapse_rate\\\": 0.0,\\n    \\\"conclusion_in_premise_count\\\": 1,\\n    \\\"conclusion_in_premise_rate\\\": 0.0667,\\n    \\\"h7_relaxed_count\\\": 0,\\n    \\\"h7_relaxed_rate\\\": 0.0,\\n    \\\"single_premise_count\\\": 0,\\n    \\\"single_premise_rate\\\": 0.0,\\n    \\\"isr_1_count\\\": 0,\\n    \\\"isr_1_rate\\\": 0.0,\\n    \\\"content_independent_count\\\": 0,\\n    \\\"content_independent_rate\\\": 0.0,\\n    \\\"genuine_count\\\": 14,\\n    \\\"genuine_rate\\\": 0.9333\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sft-1000-taxonomy_20260515T153612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T15:37:47.773948+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "cat /root/autodl-tmp/outputs/plan009_sft_baseline_s42_1000/eval_sta_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_sft-1000-taxonomy_20260515T153612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "cat /root/autodl-tmp/outputs/plan009_sft_baseline_s42_1000/eval_sta_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T15:37:47.774266+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n_problems\\\": 100,\\n    \\\"n_proved\\\": 13,\\n    \\\"prove_rate\\\": 0.13,\\n    \\\"mean_isr\\\": 0.0738,\\n    \\\"isr_std\\\": 0.2077,\\n    \\\"median_isr\\\": 0.0,\\n    \\\"isr_pr_ratio\\\": 0.5677,\\n    \\\"proved_only_mean_isr\\\": 0.5677,\\n    \\\"min_isr\\\": 0.0,\\n    \\\"max_isr\\\": 0.8333,\\n    \\\"by_answer_type\\\": {\\n      \\\"false\\\": {\\n        \\\"count\\\": 25,\\n        \\\"proved\\\": 1,\\n        \\\"prove_rate\\\": 0.04,\\n        \\\"mean_isr\\\": 0.011428571428571429\\n      },\\n      \\\"unknown\\\": {\\n        \\\"count\\\": 41,\\n        \\\"proved\\\": 0,\\n        \\\"prove_rate\\\": 0.0,\\n        \\\"mean_isr\\\": 0.0\\n      },\\n      \\\"true\\\": {\\n        \\\"count\\\": 34,\\n        \\\"proved\\\": 12,\\n        \\\"prove_rate\\\": 0.35294117647058826,\\n        \\\"mean_isr\\\": 0.2086484593837535\\n      }\\n    },\\n    \\\"elapsed_seconds\\\": 303.4,\\n    \\\"avg_time_per_sample\\\": 3.0,\\n    \\\"solver\\\": \\\"Prover9Solver\\\",\\n    \\\"logic_type\\\": \\\"fol\\\",\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/outputs/plan009_sft_baseline_s42_1000\\\"\\n  },\\n  \\\"results\\\": [\\n    {\\n      \\\"index\\\": 0,\\n      \\\"id\\\": \\\"folio_765\\\",\\n      \\\"context\\\": \\\"Tipped employees are not entitled to be paid the federal minimum wage by their employees. \\\\nIf a person is a white-collar worker, they are entitled to be paid the federal minimum wage by their employees. \\\\nAll lawyers are white-collar workers.\\\\nEvery advocate is a lawyer.\\\\nMary is not a lawyer or a tipped employee.\\\",\\n      \\\"question\\\": \\\"Mary is an advocate.\\\",\\n      \\\"answer\\\": \\\"false\\\",\\n      \\\"formalization\\\": \\\"Premises:\\\\n1. ∀x (TippedEmployee(x) → ¬EntitledTo(x, federalMinimumWage))\\\\n2. ∀x (WhiteCollarWorker(x) → EntitledTo(x, federalMinimumWage))\\\\n3. ∀x (Lawyer(x) → White
…[truncated 7631 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sft-1000-taxonomy_20260515T153612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T15:37:47.774450+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "cat /root/autodl-tmp/outputs/plan009_sft_baseline_s43_1000/eval_sta_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_sft-1000-taxonomy_20260515T153612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "cat /root/autodl-tmp/outputs/plan009_sft_baseline_s43_1000/eval_sta_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T15:37:47.774583+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "cat /root/autodl-tmp/outputs/plan009_sft_baseline_s44_1000/eval_sta_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_sft-1000-taxonomy_20260515T153612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "cat /root/autodl-tmp/outputs/plan009_sft_baseline_s44_1000/eval_sta_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T15:37:47.774911+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n_problems\\\": 100,\\n    \\\"n_proved\\\": 11,\\n    \\\"prove_rate\\\": 0.11,\\n    \\\"mean_isr\\\": 0.0699,\\n    \\\"isr_std\\\": 0.2155,\\n    \\\"median_isr\\\": 0.0,\\n    \\\"isr_pr_ratio\\\": 0.6352,\\n    \\\"proved_only_mean_isr\\\": 0.6352,\\n    \\\"min_isr\\\": 0.0,\\n    \\\"max_isr\\\": 1.0,\\n    \\\"by_answer_type\\\": {\\n      \\\"false\\\": {\\n        \\\"count\\\": 25,\\n        \\\"proved\\\": 0,\\n        \\\"prove_rate\\\": 0.0,\\n        \\\"mean_isr\\\": 0.0\\n      },\\n      \\\"unknown\\\": {\\n        \\\"count\\\": 41,\\n        \\\"proved\\\": 0,\\n        \\\"prove_rate\\\": 0.0,\\n        \\\"mean_isr\\\": 0.0\\n      },\\n      \\\"true\\\": {\\n        \\\"count\\\": 34,\\n        \\\"proved\\\": 11,\\n        \\\"prove_rate\\\": 0.3235294117647059,\\n        \\\"mean_isr\\\": 0.2054971988795518\\n      }\\n    },\\n    \\\"elapsed_seconds\\\": 326.1,\\n    \\\"avg_time_per_sample\\\": 3.3,\\n    \\\"solver\\\": \\\"Prover9Solver\\\",\\n    \\\"logic_type\\\": \\\"fol\\\",\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/outputs/plan009_sft_baseline_s43_1000/checkpoint-1000\\\"\\n  },\\n  \\\"results\\\": [\\n    {\\n      \\\"index\\\": 0,\\n      \\\"id\\\": \\\"folio_765\\\",\\n      \\\"context\\\": \\\"Tipped employees are not entitled to be paid the federal minimum wage by their employees. \\\\nIf a person is a white-collar worker, they are entitled to be paid the federal minimum wage by their employees. \\\\nAll lawyers are white-collar workers.\\\\nEvery advocate is a lawyer.\\\\nMary is not a lawyer or a tipped employee.\\\",\\n      \\\"question\\\": \\\"Mary is an advocate.\\\",\\n      \\\"answer\\\": \\\"false\\\",\\n      \\\"formalization\\\": \\\"Premises:\\\\n1. ∀x (TippedEmployee(x) → ¬EntitledTo(x, federalMinimumWage))\\\\n2. ∀x (WhiteCollarWorker(x) → EntitledTo(x, federalMinimumWage))\\\\n3. ∀x (Lawyer(x) → WhiteCollar
…[truncated 7632 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sft-1000-taxonomy_20260515T153612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T15:37:47.775278+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n_problems\\\": 100,\\n    \\\"n_proved\\\": 15,\\n    \\\"prove_rate\\\": 0.15,\\n    \\\"mean_isr\\\": 0.0884,\\n    \\\"isr_std\\\": 0.2268,\\n    \\\"median_isr\\\": 0.0,\\n    \\\"isr_pr_ratio\\\": 0.5892,\\n    \\\"proved_only_mean_isr\\\": 0.5892,\\n    \\\"min_isr\\\": 0.0,\\n    \\\"max_isr\\\": 0.8571,\\n    \\\"by_answer_type\\\": {\\n      \\\"false\\\": {\\n        \\\"count\\\": 25,\\n        \\\"proved\\\": 0,\\n        \\\"prove_rate\\\": 0.0,\\n        \\\"mean_isr\\\": 0.0\\n      },\\n      \\\"unknown\\\": {\\n        \\\"count\\\": 41,\\n        \\\"proved\\\": 0,\\n        \\\"prove_rate\\\": 0.0,\\n        \\\"mean_isr\\\": 0.0\\n      },\\n      \\\"true\\\": {\\n        \\\"count\\\": 34,\\n        \\\"proved\\\": 15,\\n        \\\"prove_rate\\\": 0.4411764705882353,\\n        \\\"mean_isr\\\": 0.25994397759103643\\n      }\\n    },\\n    \\\"elapsed_seconds\\\": 391.8,\\n    \\\"avg_time_per_sample\\\": 3.9,\\n    \\\"solver\\\": \\\"Prover9Solver\\\",\\n    \\\"logic_type\\\": \\\"fol\\\",\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/outputs/plan009_sft_baseline_s44_1000\\\"\\n  },\\n  \\\"results\\\": [\\n    {\\n      \\\"index\\\": 0,\\n      \\\"id\\\": \\\"folio_765\\\",\\n      \\\"context\\\": \\\"Tipped employees are not entitled to be paid the federal minimum wage by their employees. \\\\nIf a person is a white-collar worker, they are entitled to be paid the federal minimum wage by their employees. \\\\nAll lawyers are white-collar workers.\\\\nEvery advocate is a lawyer.\\\\nMary is not a lawyer or a tipped employee.\\\",\\n      \\\"question\\\": \\\"Mary is an advocate.\\\",\\n      \\\"answer\\\": \\\"false\\\",\\n      \\\"formalization\\\": \\\"Premises:\\\\n1. ∀x (TippedEmployee(x) → ¬EntitledTo(x, federalMinimumWage))\\\\n2. ∀x (WhiteCollarWorker(x) → EntitledTo(x, federalMinimumWage))\\\\n3. ∀x (Lawyer(x) → WhiteCollarWorker(x))\\
…[truncated 7629 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sft-1000-taxonomy_20260515T153612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T15:37:47.775505+00:00_

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
  "session": "worker_analysis_sft-1000-taxonomy_20260515T153612",
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

_source line 16 · 2026-05-15T15:37:47.775644+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sft-1000-taxonomy_20260515T153612",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T15:37:47.775806+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-39279",
  "command": "cat > /root/autodl-tmp/outputs/sft_1000_taxonomy_summary.json << 'ENDJSON'\n{\n  \"description\": \"SFT 1000-step 3-seed taxonomy summary\",\n  \"created\": \"2026-05-15\",\n  \"per_seed\": {\n    \"s42\": {\n      \"n_problems\": 100,\n      \"n_proved\": 13,\n      \"prove_rate\": 0.13,\n      \"mean_isr\": 0.0738,\n      \"proved_only_mean_isr\": 0.5677,\n      \"h7_strict\": 0,\n      \"h1_strict\": 1,\n      \"h8_conjunction_collapse\": 0,\n      \"conclusion_in_premise\": 1,\n      \"isr_1_count\": 0,\n      \"genuine_count\": 12,\n      \"genuine_rate\": 0.9231\n    },\n    \"s43\": {\n      \"n_problems\": 100,\n      \"n_proved\": 11,\n      \"prove_rate\": 0.11,\n      \"mean_isr\": 0.0699,\n      \"proved_only_mean_isr\": 0.6352,\n      \"h7_strict\": 0,\n      \"h1_strict\": 1,\n      \"h8_conjunction_collapse\": 0,\n      \"conclusion_in_premise\": 1,\n      \"isr_1_count\": 1,\n      \"genuine_count\": 10,\n      \"genuine_rate\": 0.9091\n    },\n    \"s44\": {\n      \"n_problems\": 100,\n      \"n_proved\": 15,\n      \"prove_rate\": 0.15,\n      \"mean_isr\": 0.0884,\n      \"proved_only_mean_isr\": 0.5892,\n      \"h7_strict\": 0,\n      \"h1_strict\": 1,\n      \"h8_conjunction_collapse\": 0,\n      \"conclusion_in_premise\": 1,\n      \"isr_1_count\": 0,\n      \"genuine_count\": 14,\n      \"genuine_rate\": 0.9333\n    }\n  },\n  \"aggregate\": {\n    \"prove_rate\": {\"mean\": 0.13, \"std\": 0.02},\n    \"genuine_rate\": {\"mean\": 0.9218, \"std\": 0.0122},\n    \"h7_rate\": {\"mean\": 0.0, \"std\": 0.0},\n    \"h1_rate\": {\"mean\": 0.0782, \"std\": 0.0122},\n    \"h8_rate\": {\"mean\": 0.0, \"std\": 0.0},\n    \"proved_only_isr\": {\"mean\": 0.5974, \"std\": 0.0345}\n  },\n  \"comparison_500step_sft\": {\n    \"s42\": {\"prove_rate\": 0.14, \"genuine_rate\": 0.929},\n    \"s43\": {\"prove_rate\": 0.15, \"genuine_rate\": 0.933},\n    \"s44\": {\"prove_rate\": 0.17, \"genuine_rate\": 0.882},\n    \"aggregate\": {\"prove_rate_mean\": 0.153, \"genuine_rate_mean\": 0.915}\n  },\n  \"comparison_grpo_1000step\": {\n    \"exec_only_s42\": {\"h7\": 1, \"h1\": 80, \"genuine_rate\": 0.075},\n    \"isr_s42\": {\"h7\": 87, \"genuine_rate\": 0.022},\n    \"random_s42\": {\"h7\": 97, \"genuine_rate\": 0.0}\n  }\n}\nENDJSON",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_sft-1000-taxonomy_20260515T153612",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-39279",
    "command": "cat > /root/autodl-tmp/outputs/sft_1000_taxonomy_summary.json << 'ENDJSON'\n{\n  \"description\": \"SFT 1000-step 3-seed taxonomy summary\",\n  \"created\": \"2026-05-15\",\n  \"per_seed\": {\n    \"s42\": {\n      \"n_problems\": 100,\n      \"n_proved\": 13,\n      \"prove_rate\": 0.13,\n      \"mean_isr\": 0.0738,\n      \"proved_only_mean_isr\": 0.5677,\n      \"h7_strict\": 0,\n      \"h1_strict\": 1,\n      \"h8_conjunction_collapse\": 0,\n      \"conclusion_in_premise\": 1,\n      \"isr_1_count\": 0,\n      \"genuine_count\": 12,\n      \"genuine_rate\": 0.9231\n    },\n    \"s43\": {\n      \"n_problems\": 100,\n      \"n_proved\": 11,\n      \"prove_rate\": 0.11,\n      \"mean_isr\": 0.0699,\n      \"proved_only_mean_isr\": 0.6352,\n      \"h7_strict\": 0,\n      \"h1_strict\": 1,\n      \"h8_conjunction_collapse\": 0,\n      \"conclusion_in_premise\": 1,\n      \"isr_1_count\": 1,\n      \"genuine_count\": 10,\n      \"genuine_rate\": 0.9091\n    },\n    \"s44\": {\n      \"n_problems\": 100,\n      \"n_proved\": 15,\n      \"prove_rate\": 0.15,\n      \"mean_isr\": 0.0884,\n      \"proved_only_mean_isr\": 0.5892,\n      \"h7_strict\": 0,\n      \"h1_strict\": 1,\n      \"h8_conjunction_collapse\": 0,\n      \"conclusion_in_premise\": 1,\n      \"isr_1_count\": 0,\n      \"genuine_count\": 14,\n      \"genuine_rate\": 0.9333\n    }\n  },\n  \"aggregate\": {\n    \"prove_rate\": {\"mean\": 0.13, \"std\": 0.02},\n    \"genuine_rate\": {\"mean\": 0.9218, \"std\": 0.0122},\n    \"h7_rate\": {\"mean\": 0.0, \"std\": 0.0},\n    \"h1_rate\": {\"mean\": 0.0782, \"std\": 0.0122},\n    \"h8_rate\": {\"mean\": 0.0, \"std\": 0.0},\n    \"proved_only_isr\": {\"mean\": 0.5974, \"std\": 0.0345}\n  },\n  \"comparison_500step_sft\": {\n    \"s42\": {\"prove_rate\": 0.14, \"genuine_rate\": 0.929},\n    \"s43\": {\"prove_rate\": 0.15, \"genuine_rate\": 0.933},\n    \"s44\": {\"prove_rate\": 0.17, \"genuine_rate\": 0.882},\n    \"aggregate\": {\"prove_rate_mean\": 0.153, \"genuine_rate_mean\": 0.915}\n  },\n  \"comparison_grpo_1000step\": {\n    \"exec_only_s42\": {\"h7\": 1, \"h1\": 80, \"genuine_rate\": 0.075},\n    \"isr_s42\": {\"h7\": 87, \"genuine_rate\": 0.022},\n    \"random_s42\": {\"h7\": 97, \"genuine_rate\": 0.0}\n  }\n}\nENDJSON",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T15:37:47.775967+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sft-1000-taxonomy_20260515T153612",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-15T15:37:47.776140+00:00_

汇总 JSON 已保存。以下是完整结果。

## SFT 1000-step 3-seed Taxonomy

| | s42 | s43 | s44 | **mean±std** |
|---|---|---|---|---|
| **n_proved / 100** | 13 | 11 | 15 | **13.0±2.0** |
| **Prove Rate** | 13% | 11% | 15% | **13.0±2.0%** |
| H7 (strict) | 0 | 0 | 0 | **0** |
| H1 (strict) | 1 | 1 | 1 | **1.0±0** |
| H8 (conjunction collapse) | 0 | 0 | 0 | **0** |
| **Genuine** | 12 | 10 | 14 | **12.0±2.0** |
| **Genuine Rate** | 92.3% | 90.9% | 93.3% | **92.2±1.2%** |
| Proved-only ISR | 0.568 | 0.635 | 0.589 | **0.597±0.035** |

### 关键发现

**SFT 1000-step 几乎零 hacking：** H7=0（全部 seed），H8=0，每个 seed 仅 1 例 H1（conclusion in premise）。Genuine rate 稳定在 90.9%–93.3%。

### 与 500-step SFT 对比

| | 500-step mean | 1000-step mean | 变化 |
|---|---|---|---|
| Prove Rate | 15.3% | 13.0% | ↓2.3pp |
| Genuine Rate | 91.5% | 92.2% | ↑0.7pp |

PR 略降但 genuine rate 基本持平。1000-step SFT 没有出现 hacking 恶化——与 GRPO 的退化形成鲜明对比。

### 与 GRPO 1000-step 对比

| Method | PR | H7 | Genuine Rate |
|---|---|---|---|
| **SFT 1000-step** (3-seed avg) | 13% | 0 | **92.2%** |
| GRPO exec-only s42 | — | 1 | 7.5% |
| GRPO ISR s42 | — | 87 | 2.2% |
| GRPO Random s42 | — | 97 | 0% |

SFT 在 1000 步训练后 genuine rate 保持 >90%，而所有 GRPO 变体在同样步数下 genuine rate 都崩溃到 <10%。这确认 SFT 不产生 reward hacking，可作为论文的 clean baseline。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_sft-1000-taxonomy_20260515T153612"
}
```

</details>

---
