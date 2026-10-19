# analysis fix statistical analysis critical

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 93
- **Recorded user turns:** 0
- **Tool calls:** 46
- **Original source:** `logs/chats/worker_analysis_fix-statistical-analysis-critical_20260520T045526.jsonl`
- **Structured JSON:** [`4191e6765afcc4dcd93c.json`](../../sessions/41/4191e6765afcc4dcd93c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

93 recorded events

### Tool call

_source line 1 · 2026-05-20T05:02:29.769989+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T05:02:29.770495+00:00_

1	#!/usr/bin/env python3
2	"""
3	Statistical analysis of ACR-VLA Conformal Refinement experiments.
4	Compares CRM (obs_only) vs VLA-only baselines across LIBERO benchmarks.
5	Also includes Argmin and Adaptive-K baselines.
6	"""
7	
8	import numpy as np
9	from scipy import stats
10	
11	def print_separator(char='=', width=80):
12	    print(char * width)
13	
14	def print_group_stats(name, values):
15	    """Print mean +/- std for a group."""
16	    arr = np.array(values)
17	    print(f"  {name}: n={len(arr)}, mean={arr.mean():.4f}, std={arr.std(ddof=1):.4f}, "
18	          f"min={arr.min():.4f}, max={arr.max():.4f}")
19	    print(f"    values: {[round(v, 4) for v in values]}")
20	
21	def run_tests(name_a, vals_a, name_b, vals_b):
22	    """Run t-test and Mann-Whitney U test between two groups."""
23	    a = np.array(vals_a)
24	    b = np.array(vals_b)
25	
26	    # Independent two-sample t-test (Welch's, unequal variance)
27	    t_stat, t_pval = stats.ttest_ind(a, b, equal_var=False)
28	
29	    # Mann-Whitney U test (non-parametric)
30	    u_stat, u_pval = stats.mannwhitneyu(a, b, alternative='two-sided')
31	
32	    # Effect size: Cohen's d
33	    pooled_std = np.sqrt(((len(a)-1)*a.std(ddof=1)**2 + (len(b)-1)*b.std(ddof=1)**2) /
34	                         (len(a) + len(b) - 2))
35	    cohens_d = (a.mean() - b.mean()) / pooled_std if pooled_std > 0 else float('inf')
36	
37	    # Difference
38	    diff = a.mean() - b.mean()
39	    diff_pct = diff * 100  # percentage points
40	
41	    print(f"\n  {name_a} vs {name_b}:")
42	    print(f"    Difference: {diff:+.4f} ({diff_pct:+.2f} pp)")
43	    print(f"    Welch's t-test: t={t_stat:.4f}, p={t_pval:.6f} {'***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'}")
44	    print(f"    Mann-Whitney U: U={u_stat:.1f}, p={u_pval:.6f} {'***' if u_pval < 0.001 else '**' if u_pval < 0.01 else '*' if u_pval < 0.05 else 'n.s.'}")
45	    print(f"    Cohen's d: {cohens_d:.4f} ({'large' if abs(cohens_d) > 0.8
…[truncated 12863 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T05:02:29.770715+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T05:02:29.770866+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T05:02:29.771020+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'conclusion': 'success'}",
  "limit": "0",
  "fields": "['experiment_id', 'benchmark', 'method', 'seed', 'metrics', 'config', 'updated_at', 'notes']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'conclusion': 'success'}",
    "limit": "0",
    "fields": "['experiment_id', 'benchmark', 'method', 'seed', 'metrics', 'config', 'updated_at', 'notes']"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T05:02:29.771527+00:00_

Error: result (80,607 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2c831810-b162-4fab-9231-54578fcd9e23/tool-results/mcp-agent-ml-research-read_registry-1779252954586.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2c831810-b162-4fab-9231-54578fcd9e23/tool-results/mcp-agent-ml-research-read_registry-1779252954586.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T05:02:29.771726+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*argmin*seed43*\" -o -name \"*reconvla*seed43*argmin*\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*argmin*seed43*\" -o -name \"*reconvla*seed43*argmin*\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T05:02:29.771868+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T05:02:29.771994+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*long*vla*seed48*\" -o -name \"*vla*long*seed48*\" -o -name \"*vla_only*long*seed48*\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*long*vla*seed48*\" -o -name \"*vla*long*seed48*\" -o -name \"*vla_only*long*seed48*\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T05:02:29.772123+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T05:02:29.772283+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*argmin*seed43*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*argmin*seed43*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T05:02:29.772421+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.94}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T05:02:29.772542+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*long*seed48*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*long*seed48*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T05:02:29.772671+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T05:02:29.772822+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2c831810-b162-4fab-9231-54578fcd9e23/tool-results/mcp-agent-ml-research-read_registry-1779252954586.txt",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2c831810-b162-4fab-9231-54578fcd9e23/tool-results/mcp-agent-ml-research-read_registry-1779252954586.txt",
    "limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T05:02:29.772945+00:00_

File content (38393 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T05:02:29.773085+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2c831810-b162-4fab-9231-54578fcd9e23/tool-results/mcp-agent-ml-research-read_registry-1779252954586.txt",
  "limit": "150",
  "offset": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2c831810-b162-4fab-9231-54578fcd9e23/tool-results/mcp-agent-ml-research-read_registry-1779252954586.txt",
    "limit": "150",
    "offset": "0"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T05:02:29.773203+00:00_

File content (38393 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T05:02:29.773374+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*argmin*seed43*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*argmin*seed43*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T05:02:29.773538+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*long*seed48*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*long*seed48*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-20T05:02:29.773667+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed43.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.85}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T05:02:29.773788+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed48.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T05:02:29.773929+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed43.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed43.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T05:02:29.774106+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"reconvla\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.13,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 10\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"err
…[truncated 56 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T05:02:29.774258+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed48.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed48.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T05:02:29.774475+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"long\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.15,\\n  \\\"per_task\\\": {\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 8,\\n      \\\"total\\\": 10\\n    },\\n    \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 10\\n    },\\n    \\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"suc
…[truncated 353 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T05:02:29.774633+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*argmin*k10*seed43*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*argmin*k10*seed43*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T05:02:29.774763+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T05:02:29.774892+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2c831810-b162-4fab-9231-54578fcd9e23/tool-results/mcp-agent-ml-research-read_registry-1779252954586.txt | python3 -c \"\nimport json, sys\n\ndata = json.load(sys.stdin)\nexps = json.loads(data['result'])\n\n# Group by benchmark and method\ngroups = {}\nfor exp in exps:\n    bench = exp.get('benchmark', 'unknown')\n    method = exp.get('method', 'unknown')\n    seed = exp.get('seed', '?')\n    metrics = exp.get('metrics', {})\n    sr = metrics.get('success_rate', metrics.get('overall_success_rate', metrics.get('overall_sr', '?')))\n    config = exp.get('config', {})\n    exp_id = exp.get('experiment_id', '?')\n    updated = exp.get('updated_at', '?')\n    notes = exp.get('notes', '')\n    \n    key = f'{bench}|{method}'\n    if key not in groups:\n        groups[key] = []\n    groups[key].append({\n        'seed': seed, 'sr': sr, 'config': config, \n        'exp_id': exp_id, 'updated': updated, 'notes': notes\n    })\n\n# Print grouped\nfor key in sorted(groups.keys()):\n    bench, method = key.split('|')\n    entries = groups[key]\n    # Sort by seed\n    entries.sort(key=lambda x: str(x['seed']))\n    print(f'\\n=== {bench} | {method} ({len(entries)} exps) ===')\n    for e in entries:\n        config_str = ''\n        if e['config']:\n            norm = e['config'].get('norm_eps', e['config'].get('epsilon', ''))\n            k = e['config'].get('K', e['config'].get('k', ''))\n            p = e['config'].get('percentile', '')\n            if norm: config_str += f' eps={norm}'\n            if k: config_str += f' K={k}'\n            if p: config_str += f' p={p}'\n        print(f'  seed={e[\\\"seed\\\"]} SR={e[\\\"sr\\\"]}{config_str} | {e[\\\"exp_id\\\"]} | {e[\\\"updated\\\"][:10] if e[\\\"updated\\\"] != \\\"?\\\" else \\\"?\\\"} | {e[\\\"notes\\\"][:50] if e[\\\"notes\\\"] else \\\"\\\"}')\n\" 2>&1 | head -300",
  "description": "Parse registry JSON to extract all experiments grouped by benchmark/method"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2c831810-b162-4fab-9231-54578fcd9e23/tool-results/mcp-agent-ml-research-read_registry-1779252954586.txt | python3 -c \"\nimport json, sys\n\ndata = json.load(sys.stdin)\nexps = json.loads(data['result'])\n\n# Group by benchmark and method\ngroups = {}\nfor exp in exps:\n    bench = exp.get('benchmark', 'unknown')\n    method = exp.get('method', 'unknown')\n    seed = exp.get('seed', '?')\n    metrics = exp.get('metrics', {})\n    sr = metrics.get('success_rate', metrics.get('overall_success_rate', metrics.get('overall_sr', '?')))\n    config = exp.get('config', {})\n    exp_id = exp.get('experiment_id', '?')\n    updated = exp.get('updated_at', '?')\n    notes = exp.get('notes', '')\n    \n    key = f'{bench}|{method}'\n    if key not in groups:\n        groups[key] = []\n    groups[key].append({\n        'seed': seed, 'sr': sr, 'config': config, \n        'exp_id': exp_id, 'updated': updated, 'notes': notes\n    })\n\n# Print grouped\nfor key in sorted(groups.keys()):\n    bench, method = key.split('|')\n    entries = groups[key]\n    # Sort by seed\n    entries.sort(key=lambda x: str(x['seed']))\n    print(f'\\n=== {bench} | {method} ({len(entries)} exps) ===')\n    for e in entries:\n        config_str = ''\n        if e['config']:\n            norm = e['config'].get('norm_eps', e['config'].get('epsilon', ''))\n            k = e['config'].get('K', e['config'].get('k', ''))\n            p = e['config'].get('percentile', '')\n            if norm: config_str += f' eps={norm}'\n            if k: config_str += f' K={k}'\n            if p: config_str += f' p={p}'\n        print(f'  seed={e[\\\"seed\\\"]} SR={e[\\\"sr\\\"]}{config_str} | {e[\\\"exp_id\\\"]} | {e[\\\"updated\\\"][:10] if e[\\\"updated\\\"] != \\\"?\\\" else \\\"?\\\"} | {e[\\\"notes\\\"][:50] if e[\\\"notes\\\"] else \\\"\\\"}')\n\" 2>&1 | head -300",
    "description": "Parse registry JSON to extract all experiments grouped by benchmark/method"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T05:02:29.775036+00:00_

Traceback (most recent call last):
  File "&lt;string>", line 10, in &lt;module>
    bench = exp.get('benchmark', 'unknown')
            ^^^^^^^
AttributeError: 'str' object has no attribute 'get'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T05:02:29.775199+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2c831810-b162-4fab-9231-54578fcd9e23/tool-results/mcp-agent-ml-research-read_registry-1779252954586.txt | python3 -c \"\nimport json, sys\n\ndata = json.load(sys.stdin)\nresult_str = data['result']\nexps = json.loads(result_str)\n\n# Check if exps is a list of dicts or list of strings\nif isinstance(exps, list) and len(exps) > 0:\n    if isinstance(exps[0], str):\n        exps = [json.loads(e) for e in exps]\n    print(f'Total experiments: {len(exps)}')\n    print(f'Type of first: {type(exps[0])}')\n    if isinstance(exps[0], dict):\n        print(f'Keys: {list(exps[0].keys())[:10]}')\n        # Print first entry\n        print(json.dumps(exps[0], indent=2)[:500])\nelif isinstance(exps, dict):\n    print(f'Dict with keys: {list(exps.keys())[:10]}')\n    # Maybe it's experiment_id -> experiment_data\n    first_key = list(exps.keys())[0]\n    print(f'First key: {first_key}')\n    print(json.dumps(exps[first_key], indent=2)[:500])\n\" 2>&1",
  "description": "Inspect registry JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2c831810-b162-4fab-9231-54578fcd9e23/tool-results/mcp-agent-ml-research-read_registry-1779252954586.txt | python3 -c \"\nimport json, sys\n\ndata = json.load(sys.stdin)\nresult_str = data['result']\nexps = json.loads(result_str)\n\n# Check if exps is a list of dicts or list of strings\nif isinstance(exps, list) and len(exps) > 0:\n    if isinstance(exps[0], str):\n        exps = [json.loads(e) for e in exps]\n    print(f'Total experiments: {len(exps)}')\n    print(f'Type of first: {type(exps[0])}')\n    if isinstance(exps[0], dict):\n        print(f'Keys: {list(exps[0].keys())[:10]}')\n        # Print first entry\n        print(json.dumps(exps[0], indent=2)[:500])\nelif isinstance(exps, dict):\n    print(f'Dict with keys: {list(exps.keys())[:10]}')\n    # Maybe it's experiment_id -> experiment_data\n    first_key = list(exps.keys())[0]\n    print(f'First key: {first_key}')\n    print(json.dumps(exps[first_key], indent=2)[:500])\n\" 2>&1",
    "description": "Inspect registry JSON structure"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T05:02:29.775367+00:00_

Dict with keys: ['success', 'data', 'error', 'metadata']
First key: success
true

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T05:02:29.775519+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*argmin*seed43*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*argmin*seed43*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-20T05:02:29.775646+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*long*seed48*vla*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*long*seed48*vla*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-20T05:02:29.775770+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.79}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T05:02:29.775895+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T05:02:29.776031+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2c831810-b162-4fab-9231-54578fcd9e23/tool-results/mcp-agent-ml-research-read_registry-1779252954586.txt | python3 -c \"\nimport json, sys\n\nraw = json.load(sys.stdin)\nresult_str = raw['result']\nparsed = json.loads(result_str)\ndata = parsed.get('data', parsed)\n\nif isinstance(data, dict) and 'experiments' in data:\n    exps = data['experiments']\nelif isinstance(data, list):\n    exps = data\nelif isinstance(data, dict):\n    # Try to find the experiments\n    print('data keys:', list(data.keys())[:20])\n    # Maybe data itself is {exp_id: exp_data}\n    first_key = list(data.keys())[0]\n    first_val = data[first_key]\n    print(f'first key type: {type(first_key)}, val type: {type(first_val)}')\n    if isinstance(first_val, dict):\n        print(json.dumps(first_val, indent=2)[:800])\n    else:\n        print(str(first_val)[:500])\n    sys.exit(0)\nelse:\n    print(f'Unexpected type: {type(data)}')\n    sys.exit(1)\n\nprint(f'Total experiments: {len(exps)}')\n\" 2>&1",
  "description": "Parse registry data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2c831810-b162-4fab-9231-54578fcd9e23/tool-results/mcp-agent-ml-research-read_registry-1779252954586.txt | python3 -c \"\nimport json, sys\n\nraw = json.load(sys.stdin)\nresult_str = raw['result']\nparsed = json.loads(result_str)\ndata = parsed.get('data', parsed)\n\nif isinstance(data, dict) and 'experiments' in data:\n    exps = data['experiments']\nelif isinstance(data, list):\n    exps = data\nelif isinstance(data, dict):\n    # Try to find the experiments\n    print('data keys:', list(data.keys())[:20])\n    # Maybe data itself is {exp_id: exp_data}\n    first_key = list(data.keys())[0]\n    first_val = data[first_key]\n    print(f'first key type: {type(first_key)}, val type: {type(first_val)}')\n    if isinstance(first_val, dict):\n        print(json.dumps(first_val, indent=2)[:800])\n    else:\n        print(str(first_val)[:500])\n    sys.exit(0)\nelse:\n    print(f'Unexpected type: {type(data)}')\n    sys.exit(1)\n\nprint(f'Total experiments: {len(exps)}')\n\" 2>&1",
    "description": "Parse registry data structure"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T05:02:29.776158+00:00_

Total experiments: 211

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T05:02:29.776309+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2c831810-b162-4fab-9231-54578fcd9e23/tool-results/mcp-agent-ml-research-read_registry-1779252954586.txt | python3 -c \"\nimport json, sys\n\nraw = json.load(sys.stdin)\nparsed = json.loads(raw['result'])\nexps = parsed.get('data', parsed) if isinstance(parsed, dict) else parsed\n\n# Group by benchmark+method, extract SR\ngroups = {}\nfor exp in exps:\n    bench = exp.get('benchmark', 'unknown')\n    method = exp.get('method', 'unknown')\n    seed = exp.get('seed', '?')\n    metrics = exp.get('metrics', {})\n    if isinstance(metrics, str):\n        metrics = json.loads(metrics)\n    sr = metrics.get('success_rate', metrics.get('overall_success_rate', metrics.get('overall_sr', '?')))\n    config = exp.get('config', {})\n    if isinstance(config, str):\n        config = json.loads(config)\n    exp_id = exp.get('experiment_id', '?')\n    updated = exp.get('updated_at', '?')\n    notes = str(exp.get('notes', '') or '')\n    \n    key = f'{bench}|{method}'\n    if key not in groups:\n        groups[key] = []\n    groups[key].append({\n        'seed': seed, 'sr': sr, 'config': config, \n        'exp_id': exp_id, 'updated': str(updated)[:10], 'notes': notes[:60]\n    })\n\nfor key in sorted(groups.keys()):\n    bench, method = key.split('|', 1)\n    entries = groups[key]\n    entries.sort(key=lambda x: (str(x['seed']), x['updated']))\n    print(f'\\n=== {bench} | {method} ({len(entries)} exps) ===')\n    for e in entries:\n        config_str = ''\n        if e['config'] and isinstance(e['config'], dict):\n            for ck in ['norm_eps', 'epsilon', 'K', 'k', 'percentile', 'mode']:\n                if ck in e['config']:\n                    config_str += f' {ck}={e[\\\"config\\\"][ck]}'\n        print(f'  seed={e[\\\"seed\\\"]} SR={e[\\\"sr\\\"]}{config_str} | {e[\\\"exp_id\\\"]} | {e[\\\"updated\\\"]} | {e[\\\"notes\\\"]}')\n\" 2>&1",
  "description": "Parse and group all registry experiments",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2c831810-b162-4fab-9231-54578fcd9e23/tool-results/mcp-agent-ml-research-read_registry-1779252954586.txt | python3 -c \"\nimport json, sys\n\nraw = json.load(sys.stdin)\nparsed = json.loads(raw['result'])\nexps = parsed.get('data', parsed) if isinstance(parsed, dict) else parsed\n\n# Group by benchmark+method, extract SR\ngroups = {}\nfor exp in exps:\n    bench = exp.get('benchmark', 'unknown')\n    method = exp.get('method', 'unknown')\n    seed = exp.get('seed', '?')\n    metrics = exp.get('metrics', {})\n    if isinstance(metrics, str):\n        metrics = json.loads(metrics)\n    sr = metrics.get('success_rate', metrics.get('overall_success_rate', metrics.get('overall_sr', '?')))\n    config = exp.get('config', {})\n    if isinstance(config, str):\n        config = json.loads(config)\n    exp_id = exp.get('experiment_id', '?')\n    updated = exp.get('updated_at', '?')\n    notes = str(exp.get('notes', '') or '')\n    \n    key = f'{bench}|{method}'\n    if key not in groups:\n        groups[key] = []\n    groups[key].append({\n        'seed': seed, 'sr': sr, 'config': config, \n        'exp_id': exp_id, 'updated': str(updated)[:10], 'notes': notes[:60]\n    })\n\nfor key in sorted(groups.keys()):\n    bench, method = key.split('|', 1)\n    entries = groups[key]\n    entries.sort(key=lambda x: (str(x['seed']), x['updated']))\n    print(f'\\n=== {bench} | {method} ({len(entries)} exps) ===')\n    for e in entries:\n        config_str = ''\n        if e['config'] and isinstance(e['config'], dict):\n            for ck in ['norm_eps', 'epsilon', 'K', 'k', 'percentile', 'mode']:\n                if ck in e['config']:\n                    config_str += f' {ck}={e[\\\"config\\\"][ck]}'\n        print(f'  seed={e[\\\"seed\\\"]} SR={e[\\\"sr\\\"]}{config_str} | {e[\\\"exp_id\\\"]} | {e[\\\"updated\\\"]} | {e[\\\"notes\\\"]}')\n\" 2>&1",
    "description": "Parse and group all registry experiments",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T05:02:29.776469+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 11, in &lt;module>
    bench = exp.get('benchmark', 'unknown')
            ^^^^^^^
AttributeError: 'str' object has no attribute 'get'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T05:02:29.776595+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2c831810-b162-4fab-9231-54578fcd9e23/tool-results/mcp-agent-ml-research-read_registry-1779252954586.txt | python3 -c \"\nimport json, sys\n\nraw = json.load(sys.stdin)\nparsed = json.loads(raw['result'])\ndata = parsed.get('data', parsed) if isinstance(parsed, dict) else parsed\n\nif isinstance(data, list):\n    print(f'List of {len(data)} items')\n    print(f'First item type: {type(data[0])}')\n    if isinstance(data[0], str):\n        first = json.loads(data[0])\n        print(json.dumps(first, indent=2)[:600])\n    else:\n        print(json.dumps(data[0], indent=2)[:600])\n\" 2>&1",
  "description": "Check individual experiment structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2c831810-b162-4fab-9231-54578fcd9e23/tool-results/mcp-agent-ml-research-read_registry-1779252954586.txt | python3 -c \"\nimport json, sys\n\nraw = json.load(sys.stdin)\nparsed = json.loads(raw['result'])\ndata = parsed.get('data', parsed) if isinstance(parsed, dict) else parsed\n\nif isinstance(data, list):\n    print(f'List of {len(data)} items')\n    print(f'First item type: {type(data[0])}')\n    if isinstance(data[0], str):\n        first = json.loads(data[0])\n        print(json.dumps(first, indent=2)[:600])\n    else:\n        print(json.dumps(data[0], indent=2)[:600])\n\" 2>&1",
    "description": "Check individual experiment structure"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-20T05:02:29.776741+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T05:02:29.776874+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2c831810-b162-4fab-9231-54578fcd9e23/tool-results/mcp-agent-ml-research-read_registry-1779252954586.txt | python3 -c \"\nimport json, sys\n\nraw = json.load(sys.stdin)\nresult_str = raw['result']\nparsed = json.loads(result_str)\n\n# Navigate to the actual data\nif isinstance(parsed, dict):\n    if 'data' in parsed:\n        data = parsed['data']\n    else:\n        data = parsed\nelse:\n    data = parsed\n\nprint(f'type(data)={type(data).__name__}')\nif isinstance(data, list):\n    print(f'len={len(data)}')\n    for i, item in enumerate(data[:3]):\n        print(f'  [{i}] type={type(item).__name__}')\n        if isinstance(item, str):\n            sub = json.loads(item) if item.startswith('{') else item\n            print(f'       parsed type={type(sub).__name__}')\n            if isinstance(sub, dict):\n                print(f'       keys={list(sub.keys())[:8]}')\n        elif isinstance(item, dict):\n            print(f'       keys={list(item.keys())[:8]}')\nelif isinstance(data, dict):\n    print(f'keys={list(data.keys())[:15]}')\n    for k in list(data.keys())[:3]:\n        v = data[k]\n        print(f'  {k}: type={type(v).__name__}, val={str(v)[:100]}')\n\" 2>&1",
  "description": "Debug registry data structure at data level"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2c831810-b162-4fab-9231-54578fcd9e23/tool-results/mcp-agent-ml-research-read_registry-1779252954586.txt | python3 -c \"\nimport json, sys\n\nraw = json.load(sys.stdin)\nresult_str = raw['result']\nparsed = json.loads(result_str)\n\n# Navigate to the actual data\nif isinstance(parsed, dict):\n    if 'data' in parsed:\n        data = parsed['data']\n    else:\n        data = parsed\nelse:\n    data = parsed\n\nprint(f'type(data)={type(data).__name__}')\nif isinstance(data, list):\n    print(f'len={len(data)}')\n    for i, item in enumerate(data[:3]):\n        print(f'  [{i}] type={type(item).__name__}')\n        if isinstance(item, str):\n            sub = json.loads(item) if item.startswith('{') else item\n            print(f'       parsed type={type(sub).__name__}')\n            if isinstance(sub, dict):\n                print(f'       keys={list(sub.keys())[:8]}')\n        elif isinstance(item, dict):\n            print(f'       keys={list(item.keys())[:8]}')\nelif isinstance(data, dict):\n    print(f'keys={list(data.keys())[:15]}')\n    for k in list(data.keys())[:3]:\n        v = data[k]\n        print(f'  {k}: type={type(v).__name__}, val={str(v)[:100]}')\n\" 2>&1",
    "description": "Debug registry data structure at data level"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-20T05:02:29.777006+00:00_

type(data)=dict
keys=['experiments', 'count', 'total', 'baseline']
  experiments: type=dict, val={'eval-vla-only-spatial-seed50': {'updated_at': '2026-05-20T04:13:56.340Z', 'metrics': {'success_rat
  count: type=int, val=211
  total: type=int, val=211

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-20T05:02:29.777134+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2c831810-b162-4fab-9231-54578fcd9e23/tool-results/mcp-agent-ml-research-read_registry-1779252954586.txt | python3 -c \"\nimport json, sys\n\nraw = json.load(sys.stdin)\nparsed = json.loads(raw['result'])\nexps_dict = parsed['data']['experiments']\n\n# Group by benchmark+method\ngroups = {}\nfor exp_id, exp in exps_dict.items():\n    bench = exp.get('benchmark', 'unknown')\n    method = exp.get('method', 'unknown')\n    seed = exp.get('seed', '?')\n    metrics = exp.get('metrics', {})\n    if isinstance(metrics, str):\n        metrics = json.loads(metrics)\n    sr = metrics.get('success_rate', metrics.get('overall_success_rate', metrics.get('overall_sr', '?')))\n    config = exp.get('config', {})\n    if isinstance(config, str):\n        config = json.loads(config)\n    updated = str(exp.get('updated_at', '?'))[:10]\n    notes = str(exp.get('notes', '') or '')[:60]\n    \n    key = f'{bench}|{method}'\n    if key not in groups:\n        groups[key] = []\n    groups[key].append({\n        'seed': seed, 'sr': sr, 'config': config, \n        'exp_id': exp_id, 'updated': updated, 'notes': notes\n    })\n\nfor key in sorted(groups.keys()):\n    bench, method = key.split('|', 1)\n    entries = groups[key]\n    entries.sort(key=lambda x: (str(x['seed']), x['updated']))\n    print(f'\\n=== {bench} | {method} ({len(entries)} exps) ===')\n    for e in entries:\n        config_str = ''\n        if e['config'] and isinstance(e['config'], dict):\n            for ck in ['norm_eps', 'epsilon', 'K', 'k', 'percentile', 'mode', 'norm']:\n                if ck in e['config']:\n                    config_str += f' {ck}={e[\\\"config\\\"][ck]}'\n        print(f'  seed={e[\\\"seed\\\"]} SR={e[\\\"sr\\\"]}{config_str} | {e[\\\"exp_id\\\"]} | {e[\\\"updated\\\"]} | {e[\\\"notes\\\"]}')\n\" 2>&1",
  "description": "Parse registry experiments grouped by benchmark/method",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2c831810-b162-4fab-9231-54578fcd9e23/tool-results/mcp-agent-ml-research-read_registry-1779252954586.txt | python3 -c \"\nimport json, sys\n\nraw = json.load(sys.stdin)\nparsed = json.loads(raw['result'])\nexps_dict = parsed['data']['experiments']\n\n# Group by benchmark+method\ngroups = {}\nfor exp_id, exp in exps_dict.items():\n    bench = exp.get('benchmark', 'unknown')\n    method = exp.get('method', 'unknown')\n    seed = exp.get('seed', '?')\n    metrics = exp.get('metrics', {})\n    if isinstance(metrics, str):\n        metrics = json.loads(metrics)\n    sr = metrics.get('success_rate', metrics.get('overall_success_rate', metrics.get('overall_sr', '?')))\n    config = exp.get('config', {})\n    if isinstance(config, str):\n        config = json.loads(config)\n    updated = str(exp.get('updated_at', '?'))[:10]\n    notes = str(exp.get('notes', '') or '')[:60]\n    \n    key = f'{bench}|{method}'\n    if key not in groups:\n        groups[key] = []\n    groups[key].append({\n        'seed': seed, 'sr': sr, 'config': config, \n        'exp_id': exp_id, 'updated': updated, 'notes': notes\n    })\n\nfor key in sorted(groups.keys()):\n    bench, method = key.split('|', 1)\n    entries = groups[key]\n    entries.sort(key=lambda x: (str(x['seed']), x['updated']))\n    print(f'\\n=== {bench} | {method} ({len(entries)} exps) ===')\n    for e in entries:\n        config_str = ''\n        if e['config'] and isinstance(e['config'], dict):\n            for ck in ['norm_eps', 'epsilon', 'K', 'k', 'percentile', 'mode', 'norm']:\n                if ck in e['config']:\n                    config_str += f' {ck}={e[\\\"config\\\"][ck]}'\n        print(f'  seed={e[\\\"seed\\\"]} SR={e[\\\"sr\\\"]}{config_str} | {e[\\\"exp_id\\\"]} | {e[\\\"updated\\\"]} | {e[\\\"notes\\\"]}')\n\" 2>&1",
    "description": "Parse registry experiments grouped by benchmark/method",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T05:02:29.777386+00:00_

=== unknown | unknown (211 exps) ===
  seed=? SR=? | crm-train-v3-norm-scalar-unc | 2026-05-14 | 
  seed=? SR=? | crm-train-v3-norm-obs-only | 2026-05-14 | 
  seed=? SR=? | crm-train-v3-norm | 2026-05-14 | 
  seed=? SR=? | eval-mag-obsonly-norm03-r2 | 2026-05-15 | 
  seed=? SR=12 | eval-vla-mean-object | 2026-05-15 | 
  seed=? SR=0.12 | eval-reconvla-object | 2026-05-15 | 
  seed=? SR=19.0% (19/100) | eval-acr-object-v4-obs-only | 2026-05-15 | 
  seed=? SR=11.0% (11/100) | eval-acr-object-v4-perdof | 2026-05-15 | 
  seed=? SR=32.0% (32/100) | eval-acr-spatial-v4-scalar-r2 | 2026-05-15 | 
  seed=? SR=35.0% (35/100) | eval-acr-spatial-v4-obs-only-r3 | 2026-05-15 | 
  seed=? SR=35.0% (35/100) | eval-acr-spatial-v4-small-r2 | 2026-05-15 | [D027] Framing 暂不裁决。Scenario A/B/C 取决于 magnitude sweep + obj
  seed=? SR=0.34 | eval-argmin-only-spatial-r2 | 2026-05-15 | 10-task complete. T9 (wooden_cabinet) = 10%. Overall 34% (34
  seed=? SR=0.12 | eval-vla-only-object | 2026-05-15 | 
  seed=? SR=0.16 | eval-obs-only-object-norm02-seed45 | 2026-05-16 | 
  seed=? SR=0.18 | eval-obs-only-object-norm03-seed44 | 2026-05-16 | 
  seed=? SR=0.1 | eval-vla-mean-object-seed44 | 2026-05-16 | 
  seed=? SR=0.13 | eval-argmin-object-seed44-r2 | 2026-05-16 | 
  seed=? SR=0.16 | eval-obs-only-object-norm02-seed44-r2 | 2026-05-16 | 
  seed=? SR=0 | eval-acr-object-v4-default-r2 | 2026-05-16 | 
  seed=? SR=0.14 | eval-mag-perdof-norm003-object | 2026-05-16 | 
  seed=? SR=0.16 | eval-obs-only-object-norm02-seed43-r2 | 2026-05-16 | 
  seed=? SR=0.1 | eval-vla-only-object-seed44-r2 | 2026-05-16 | 
  seed=? SR=0.17 | eval-acr-object-obs-only-default | 2026-05-16 | 
  seed=? SR=? | eval-scalar-object-seed43 | 2026-05-16 | 
  seed=? SR=0.16 | eval-mag-obsonly-norm003-object | 2026-05-16 | 
  seed=? SR=0.15 | eval-vla-mean-object-seed43 | 2026-05-16 | 
  seed=? SR=0.12 | eval-perdof-object-seed43 | 2026-05-16 | 
  seed=? SR=0.17 | eval-argmin-object-seed43 | 2026-05-16 | 
  seed=? SR=0.09 | eval-perdof-o
…[truncated 12873 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-20T05:02:29.777637+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*argmin*object*seed43*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*argmin*object*seed43*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-20T05:02:29.777780+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-20T05:02:29.777917+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*goal*seed47*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*goal*seed47*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-20T05:02:29.778083+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-20T05:02:29.778209+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*vla*spatial*seed48*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*vla*spatial*seed48*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-20T05:02:29.778371+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-20T05:02:29.778499+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*vla*spatial*seed49*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*vla*spatial*seed49*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-20T05:02:29.778623+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-20T05:02:29.778753+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*argmin*object*seed43*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*argmin*object*seed43*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-20T05:02:29.778875+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-20T05:02:29.778997+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*goal*seed47*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*goal*seed47*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-20T05:02:29.779118+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-20T05:02:29.779233+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*vla*spatial*seed48*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*vla*spatial*seed48*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-20T05:02:29.779378+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-20T05:02:29.779495+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*vla*long*seed48*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*vla*long*seed48*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-20T05:02:29.779614+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-20T05:02:29.779725+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*argmin*object*k10*seed43*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*argmin*object*k10*seed43*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-20T05:02:29.779840+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-20T05:02:29.779985+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/logs/ -name \"*argmin*seed43*\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/logs/ -name \"*argmin*seed43*\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-20T05:02:29.780105+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-20T05:02:29.780229+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*argmin*seed43*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*argmin*seed43*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-20T05:02:29.780371+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed43.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-20T05:02:29.780489+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "find /root/logs/ -name \"*argmin*seed43*\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "find /root/logs/ -name \"*argmin*seed43*\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-20T05:02:29.780604+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-20T05:02:29.780738+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "find /root/logs/ -name \"*long*seed48*\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "find /root/logs/ -name \"*long*seed48*\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-20T05:02:29.780912+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-20T05:02:29.781083+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/logs/ -name \"*argmin*seed43*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/logs/ -name \"*argmin*seed43*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-20T05:02:29.781203+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "find /root/logs/ -name \"*argmin*seed43*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "find /root/logs/ -name \"*argmin*seed43*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-20T05:02:29.781343+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-20T05:02:29.781470+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-20T05:02:29.781590+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "find /root/logs/ -name \"*long*seed48*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "find /root/logs/ -name \"*long*seed48*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-20T05:02:29.781707+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-20T05:02:29.781821+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/logs/ -name \"*long*seed48*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/logs/ -name \"*long*seed48*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-20T05:02:29.781936+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-20T05:02:29.782105+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*argmin*seed43*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*argmin*seed43*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-20T05:02:29.782226+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*long*seed48*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*long*seed48*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-20T05:02:29.782366+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.91}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-20T05:02:29.782482+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-20T05:02:29.782607+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/logs/ -name \"*argmin*seed43*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "find /root/logs/ -name \"*argmin*seed43*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-20T05:02:29.782725+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/logs/ -name \"*argmin*seed43*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "find /root/logs/ -name \"*argmin*seed43*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-20T05:02:29.782848+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-20T05:02:29.782965+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"find: '/root/logs/': No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-20T05:02:29.783172+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
  "content": "#!/usr/bin/env python3\n\"\"\"\nStatistical analysis of ACR-VLA Conformal Refinement experiments.\nCompares CRM (obs_only) vs VLA-only baselines across LIBERO benchmarks.\nAlso includes Argmin and Adaptive-K baselines.\n\nPrimary CRM config for Object: norm02 (ε=0.2), K=10.\n\"\"\"\n\nimport numpy as np\nfrom scipy import stats\n\ndef print_separator(char='=', width=80):\n    print(char * width)\n\ndef print_group_stats(name, values):\n    arr = np.array(values)\n    print(f\"  {name}: n={len(arr)}, mean={arr.mean():.4f}, std={arr.std(ddof=1):.4f}, \"\n          f\"min={arr.min():.4f}, max={arr.max():.4f}\")\n    print(f\"    values: {[round(v, 4) for v in values]}\")\n\ndef run_tests(name_a, vals_a, name_b, vals_b):\n    a = np.array(vals_a)\n    b = np.array(vals_b)\n\n    t_stat, t_pval = stats.ttest_ind(a, b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(a, b, alternative='two-sided')\n\n    pooled_std = np.sqrt(((len(a)-1)*a.std(ddof=1)**2 + (len(b)-1)*b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    cohens_d = (a.mean() - b.mean()) / pooled_std if pooled_std > 0 else float('inf')\n\n    diff = a.mean() - b.mean()\n    diff_pct = diff * 100\n\n    print(f\"\\n  {name_a} vs {name_b}:\")\n    print(f\"    Difference: {diff:+.4f} ({diff_pct:+.2f} pp)\")\n    print(f\"    Welch's t-test: t={t_stat:.4f}, p={t_pval:.6f} {'***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Mann-Whitney U: U={u_stat:.1f}, p={u_pval:.6f} {'***' if u_pval < 0.001 else '**' if u_pval < 0.01 else '*' if u_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Cohen's d: {cohens_d:.4f} ({'large' if abs(cohens_d) > 0.8 else 'medium' if abs(cohens_d) > 0.5 else 'small' if abs(cohens_d) > 0.2 else 'negligible'})\")\n\n    return t_pval, u_pval\n\n# ============================================================================\n# DATA (from registry, conclusion=success, 2026-05-20)\n# Each seed appears once; r2/r3 supersedes earlier runs.\n# ============================================================================\n\n# --- LIBERO-Spatial ---\n# CRM obs_only norm02 K=10 (seeds 43-48); seed42 uses K=5 fallback\ncrm_spatial = [0.35, 0.34, 0.36, 0.34, 0.32, 0.35]  # s42(k5), s43-r2, s44, s45, s47, s48\n\n# VLA-only Spatial (seeds 42-50)\nvla_spatial = [0.30, 0.29, 0.31, 0.27, 0.30, 0.30, 0.30, 0.29, 0.30]  # s42, s43, s44, s45, s46, s47, s48, s49, s50\n\n# --- LIBERO-Long ---\n# CRM obs_only Long (seeds 42-47)\ncrm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17]  # s42, s43, s44, s45, s46, s47\n\n# VLA-only Long (seeds 42-48)\nvla_long = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14]  # s42, s43, s44, s45, s46, s47, s48\n\n# --- LIBERO-Goal ---\n# CRM obs_only Goal (seeds 42-47)\ncrm_goal = [0.67, 0.72, 0.64, 0.65, 0.72, 0.69]  # s42, s43, s44-r2, s45-r2, s46, s47\n\n# VLA-only Goal (seeds 42-46)\nvla_goal = [0.71, 0.69, 0.73, 0.63, 0.71]  # s42, s43, s44-r2, s45, s46\n\n# --- LIBERO-Object ---\n# PRIMARY: CRM obs_only norm02 K=10 (seeds 43-48)\ncrm_object = [0.16, 0.16, 0.16, 0.15, 0.20, 0.18]  # s43-r2, s44-r2, s45, s46, s47, s48-r2\n\n# Supplementary: CRM obs_only norm01 (seeds 42-48)\ncrm_object_norm01 = [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]  # s42, s44, s45-r2, s46-r3, s47, s48\n\n# Supplementary: CRM obs_only norm02 K=5 (seeds 42-48)\ncrm_object_k5 = [0.14, 0.19, 0.17, 0.15, 0.16, 0.13, 0.18]  # s42, s43, s44, s45, s46, s47, s48\n\n# VLA-only Object (seeds 42-50, using r2 for seed45)\nvla_object = [0.12, 0.12, 0.10, 0.11, 0.13, 0.10, 0.10, 0.09]  # s42, s43, s44-r2, s45-r2, s46, s47, s48, s50\n\n# --- Argmin Object ---\n# K=10: seed43=0.17 is outlier (JSON not found on any server for verification)\nargmin_object_k10 = [0.17, 0.13, 0.12, 0.10, 0.10]  # s43, s44-r2, s45, s46, s47\nargmin_object_k5 = [0.15, 0.13, 0.11, 0.13]  # s42, s43, s44-r2, s45\n\n# --- Adaptive-K Object ---\nadaptive_k_p25 = [0.15, 0.13]  # s42, s43\nadaptive_k_p50 = [0.16, 0.16, 0.14]  # s42, s43, s44\nadaptive_k_p75 = [0.12, 0.13, 0.16]  # s42, s43, s44\nadaptive_k_p90 = [0.12, 0.14, 0.14]  # s42, s43, s44\n\n\n# ============================================================================\n# ANALYSIS\n# ============================================================================\n\nprint_separator()\nprint(\"STATISTICAL ANALYSIS: ACR-VLA Conformal Refinement Experiments\")\nprint(\"All success rates are fractions (0.0 to 1.0)\")\nprint(\"Object benchmark primary CRM config: norm02 (ε=0.2), K=10\")\nprint_separator()\n\n# ============================================================================\n# 1. LIBERO-SPATIAL\n# ============================================================================\nprint(\"\\n1. LIBERO-SPATIAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_spatial)\nprint_group_stats(\"VLA-only (n=9)\", vla_spatial)\nrun_tests(\"CRM\", crm_spatial, \"VLA-only\", vla_spatial)\n\n# ============================================================================\n# 2. LIBERO-LONG\n# ============================================================================\nprint(\"\\n\\n2. LIBERO-LONG\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_long)\nprint_group_stats(\"VLA-only (n=7)\", vla_long)\nrun_tests(\"CRM\", crm_long, \"VLA-only\", vla_long)\n\n# ============================================================================\n# 3. LIBERO-GOAL\n# ============================================================================\nprint(\"\\n\\n3. LIBERO-GOAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_goal)\nprint_group_stats(\"VLA-only (n=5)\", vla_goal)\nrun_tests(\"CRM\", crm_goal, \"VLA-only\", vla_goal)\n\n# ============================================================================\n# 4. LIBERO-OBJECT (primary: norm02 K=10)\n# ============================================================================\nprint(\"\\n\\n4. LIBERO-OBJECT\")\nprint_separator('-')\n\nprint(\"\\n  [PRIMARY: CRM norm02 K=10]\")\nprint_group_stats(\"CRM obs_only norm02 K=10 (n=6)\", crm_object)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nrun_tests(\"CRM norm02 K=10\", crm_object, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm01]\")\nprint_group_stats(\"CRM obs_only norm01 (n=6)\", crm_object_norm01)\nrun_tests(\"CRM norm01\", crm_object_norm01, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm02 K=5]\")\nprint_group_stats(\"CRM obs_only norm02 K=5 (n=7)\", crm_object_k5)\nrun_tests(\"CRM norm02 K=5\", crm_object_k5, \"VLA-only\", vla_object)\n\n# ============================================================================\n# 5. ARGMIN BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n5. ARGMIN BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Argmin K=10 (n=5)\", argmin_object_k10)\nprint_group_stats(\"Argmin K=5 (n=4)\", argmin_object_k5)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Argmin K=10 vs VLA-only:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"VLA-only\", vla_object)\nprint(\"\\n  Argmin K=10 vs CRM norm02 K=10:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 6. ADAPTIVE-K BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n6. ADAPTIVE-K BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Adaptive-K p25 (n=2)\", adaptive_k_p25)\nprint_group_stats(\"Adaptive-K p50 (n=3)\", adaptive_k_p50)\nprint_group_stats(\"Adaptive-K p75 (n=3)\", adaptive_k_p75)\nprint_group_stats(\"Adaptive-K p90 (n=3)\", adaptive_k_p90)\nall_adaptive = adaptive_k_p25 + adaptive_k_p50 + adaptive_k_p75 + adaptive_k_p90\nprint_group_stats(\"Adaptive-K all (n=11)\", all_adaptive)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Adaptive-K (all) vs VLA-only:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"VLA-only\", vla_object)\nprint(\"\\n  Adaptive-K (all) vs CRM norm02 K=10:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 7. SUMMARY TABLE\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"SUMMARY TABLE\")\nprint_separator()\nprint(f\"{'Benchmark':<18} {'Method':<22} {'n':>3} {'Mean':>7} {'Std':>7} {'Δ vs VLA':>9} {'p-value':>10} {'Sig':>5}\")\nprint_separator('-')\n\ndef get_vla_baseline(bench):\n    if bench == \"LIBERO-Spatial\": return vla_spatial\n    if bench == \"LIBERO-Long\": return vla_long\n    if bench == \"LIBERO-Goal\": return vla_goal\n    if bench == \"LIBERO-Object\": return vla_object\n    return None\n\ndef print_summary_row(bench, method, vals, is_vla=False):\n    arr = np.array(vals)\n    n = len(arr)\n    mean = arr.mean()\n    std = arr.std(ddof=1)\n    baseline = get_vla_baseline(bench)\n    if is_vla or baseline is None:\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {'—':>9} {'—':>10} {'—':>5}\")\n    else:\n        bl_arr = np.array(baseline)\n        diff = mean - bl_arr.mean()\n        _, t_pval = stats.ttest_ind(arr, bl_arr, equal_var=False)\n        sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {diff:>+9.4f} {t_pval:>10.6f} {sig:>5}\")\n\nprint_summary_row(\"LIBERO-Spatial\", \"CRM obs_only\", crm_spatial)\nprint_summary_row(\"LIBERO-Spatial\", \"VLA-only\", vla_spatial, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Long\", \"CRM obs_only\", crm_long)\nprint_summary_row(\"LIBERO-Long\", \"VLA-only\", vla_long, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Goal\", \"CRM obs_only\", crm_goal)\nprint_summary_row(\"LIBERO-Goal\", \"VLA-only\", vla_goal, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=10\", crm_object)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm01 (supp)\", crm_object_norm01)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=5 (supp)\", crm_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"VLA-only\", vla_object, is_vla=True)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=10\", argmin_object_k10)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=5\", argmin_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"Adaptive-K (all)\", all_adaptive)\n\n# ============================================================================\n# 8. KEY SIGNIFICANCE RESULTS\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"KEY SIGNIFICANCE RESULTS\")\nprint_separator()\n\ntests = [\n    (\"Spatial: CRM vs VLA\", crm_spatial, vla_spatial),\n    (\"Long: CRM vs VLA\", crm_long, vla_long),\n    (\"Goal: CRM vs VLA\", crm_goal, vla_goal),\n    (\"Object(norm02): CRM vs VLA\", crm_object, vla_object),\n    (\"Object(norm01-supp): CRM vs VLA\", crm_object_norm01, vla_object),\n    (\"Object: Argmin-K10 vs VLA\", argmin_object_k10, vla_object),\n    (\"Object: CRM-norm02 vs Argmin-K10\", crm_object, argmin_object_k10),\n    (\"Object: Adaptive-K vs VLA\", all_adaptive, vla_object),\n    (\"Object: CRM-norm02 vs Adaptive-K\", crm_object, all_adaptive),\n]\n\nprint(f\"\\n{'Comparison':<40} {'Diff':>7} {'t-test p':>10} {'MW-U p':>10} {'Sig':>5} {'Cohen d':>9}\")\nprint('-' * 85)\nfor name, a, b in tests:\n    arr_a, arr_b = np.array(a), np.array(b)\n    diff = arr_a.mean() - arr_b.mean()\n    t_stat, t_pval = stats.ttest_ind(arr_a, arr_b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(arr_a, arr_b, alternative='two-sided')\n    pooled_std = np.sqrt(((len(a)-1)*arr_a.std(ddof=1)**2 + (len(b)-1)*arr_b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    d = diff / pooled_std if pooled_std > 0 else float('inf')\n    sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n    print(f\"{name:<40} {diff:>+.4f} {t_pval:>10.6f} {u_pval:>10.6f} {sig:>5} {d:>+9.4f}\")\n\n# ============================================================================\n# 9. VERIFICATION NOTES\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"VERIFICATION NOTES\")\nprint_separator()\nprint(\"- Argmin K=10 seed43 = 0.17: severe outlier (other seeds 0.10-0.13).\")\nprint(\"  Original JSON not found on any server (bjb2-40593, bjb2-28827, bjb1-18228, bjb1-32546).\")\nprint(\"  Registry value retained but unverified.\")\nprint(\"- VLA-only Long seed48 = 0.14: confirmed by registry (eval-vla-only-long-seed48).\")\nprint(\"- CRM-Goal seed47 = 0.69: included per Director directive (not yet in registry).\")\nprint(\"- VLA-Spatial seed48=0.30, seed49=0.29: included per Director directive.\")\n\nprint(\"\\nSignificance levels: *** p<0.001, ** p<0.01, * p<0.05, n.s. not significant\")\nprint()\nprint_separator()\nprint(\"END OF ANALYSIS\")\nprint_separator()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
    "content": "#!/usr/bin/env python3\n\"\"\"\nStatistical analysis of ACR-VLA Conformal Refinement experiments.\nCompares CRM (obs_only) vs VLA-only baselines across LIBERO benchmarks.\nAlso includes Argmin and Adaptive-K baselines.\n\nPrimary CRM config for Object: norm02 (ε=0.2), K=10.\n\"\"\"\n\nimport numpy as np\nfrom scipy import stats\n\ndef print_separator(char='=', width=80):\n    print(char * width)\n\ndef print_group_stats(name, values):\n    arr = np.array(values)\n    print(f\"  {name}: n={len(arr)}, mean={arr.mean():.4f}, std={arr.std(ddof=1):.4f}, \"\n          f\"min={arr.min():.4f}, max={arr.max():.4f}\")\n    print(f\"    values: {[round(v, 4) for v in values]}\")\n\ndef run_tests(name_a, vals_a, name_b, vals_b):\n    a = np.array(vals_a)\n    b = np.array(vals_b)\n\n    t_stat, t_pval = stats.ttest_ind(a, b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(a, b, alternative='two-sided')\n\n    pooled_std = np.sqrt(((len(a)-1)*a.std(ddof=1)**2 + (len(b)-1)*b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    cohens_d = (a.mean() - b.mean()) / pooled_std if pooled_std > 0 else float('inf')\n\n    diff = a.mean() - b.mean()\n    diff_pct = diff * 100\n\n    print(f\"\\n  {name_a} vs {name_b}:\")\n    print(f\"    Difference: {diff:+.4f} ({diff_pct:+.2f} pp)\")\n    print(f\"    Welch's t-test: t={t_stat:.4f}, p={t_pval:.6f} {'***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Mann-Whitney U: U={u_stat:.1f}, p={u_pval:.6f} {'***' if u_pval < 0.001 else '**' if u_pval < 0.01 else '*' if u_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Cohen's d: {cohens_d:.4f} ({'large' if abs(cohens_d) > 0.8 else 'medium' if abs(cohens_d) > 0.5 else 'small' if abs(cohens_d) > 0.2 else 'negligible'})\")\n\n    return t_pval, u_pval\n\n# ============================================================================\n# DATA (from registry, conclusion=success, 2026-05-20)\n# Each seed appears once; r2/r3 supersedes earlier runs.\n# ============================================================================\n\n# --- LIBERO-Spatial ---\n# CRM obs_only norm02 K=10 (seeds 43-48); seed42 uses K=5 fallback\ncrm_spatial = [0.35, 0.34, 0.36, 0.34, 0.32, 0.35]  # s42(k5), s43-r2, s44, s45, s47, s48\n\n# VLA-only Spatial (seeds 42-50)\nvla_spatial = [0.30, 0.29, 0.31, 0.27, 0.30, 0.30, 0.30, 0.29, 0.30]  # s42, s43, s44, s45, s46, s47, s48, s49, s50\n\n# --- LIBERO-Long ---\n# CRM obs_only Long (seeds 42-47)\ncrm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17]  # s42, s43, s44, s45, s46, s47\n\n# VLA-only Long (seeds 42-48)\nvla_long = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14]  # s42, s43, s44, s45, s46, s47, s48\n\n# --- LIBERO-Goal ---\n# CRM obs_only Goal (seeds 42-47)\ncrm_goal = [0.67, 0.72, 0.64, 0.65, 0.72, 0.69]  # s42, s43, s44-r2, s45-r2, s46, s47\n\n# VLA-only Goal (seeds 42-46)\nvla_goal = [0.71, 0.69, 0.73, 0.63, 0.71]  # s42, s43, s44-r2, s45, s46\n\n# --- LIBERO-Object ---\n# PRIMARY: CRM obs_only norm02 K=10 (seeds 43-48)\ncrm_object = [0.16, 0.16, 0.16, 0.15, 0.20, 0.18]  # s43-r2, s44-r2, s45, s46, s47, s48-r2\n\n# Supplementary: CRM obs_only norm01 (seeds 42-48)\ncrm_object_norm01 = [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]  # s42, s44, s45-r2, s46-r3, s47, s48\n\n# Supplementary: CRM obs_only norm02 K=5 (seeds 42-48)\ncrm_object_k5 = [0.14, 0.19, 0.17, 0.15, 0.16, 0.13, 0.18]  # s42, s43, s44, s45, s46, s47, s48\n\n# VLA-only Object (seeds 42-50, using r2 for seed45)\nvla_object = [0.12, 0.12, 0.10, 0.11, 0.13, 0.10, 0.10, 0.09]  # s42, s43, s44-r2, s45-r2, s46, s47, s48, s50\n\n# --- Argmin Object ---\n# K=10: seed43=0.17 is outlier (JSON not found on any server for verification)\nargmin_object_k10 = [0.17, 0.13, 0.12, 0.10, 0.10]  # s43, s44-r2, s45, s46, s47\nargmin_object_k5 = [0.15, 0.13, 0.11, 0.13]  # s42, s43, s44-r2, s45\n\n# --- Adaptive-K Object ---\nadaptive_k_p25 = [0.15, 0.13]  # s42, s43\nadaptive_k_p50 = [0.16, 0.16, 0.14]  # s42, s43, s44\nadaptive_k_p75 = [0.12, 0.13, 0.16]  # s42, s43, s44\nadaptive_k_p90 = [0.12, 0.14, 0.14]  # s42, s43, s44\n\n\n# ============================================================================\n# ANALYSIS\n# ============================================================================\n\nprint_separator()\nprint(\"STATISTICAL ANALYSIS: ACR-VLA Conformal Refinement Experiments\")\nprint(\"All success rates are fractions (0.0 to 1.0)\")\nprint(\"Object benchmark primary CRM config: norm02 (ε=0.2), K=10\")\nprint_separator()\n\n# ============================================================================\n# 1. LIBERO-SPATIAL\n# ============================================================================\nprint(\"\\n1. LIBERO-SPATIAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_spatial)\nprint_group_stats(\"VLA-only (n=9)\", vla_spatial)\nrun_tests(\"CRM\", crm_spatial, \"VLA-only\", vla_spatial)\n\n# ============================================================================\n# 2. LIBERO-LONG\n# ============================================================================\nprint(\"\\n\\n2. LIBERO-LONG\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_long)\nprint_group_stats(\"VLA-only (n=7)\", vla_long)\nrun_tests(\"CRM\", crm_long, \"VLA-only\", vla_long)\n\n# ============================================================================\n# 3. LIBERO-GOAL\n# ============================================================================\nprint(\"\\n\\n3. LIBERO-GOAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_goal)\nprint_group_stats(\"VLA-only (n=5)\", vla_goal)\nrun_tests(\"CRM\", crm_goal, \"VLA-only\", vla_goal)\n\n# ============================================================================\n# 4. LIBERO-OBJECT (primary: norm02 K=10)\n# ============================================================================\nprint(\"\\n\\n4. LIBERO-OBJECT\")\nprint_separator('-')\n\nprint(\"\\n  [PRIMARY: CRM norm02 K=10]\")\nprint_group_stats(\"CRM obs_only norm02 K=10 (n=6)\", crm_object)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nrun_tests(\"CRM norm02 K=10\", crm_object, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm01]\")\nprint_group_stats(\"CRM obs_only norm01 (n=6)\", crm_object_norm01)\nrun_tests(\"CRM norm01\", crm_object_norm01, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm02 K=5]\")\nprint_group_stats(\"CRM obs_only norm02 K=5 (n=7)\", crm_object_k5)\nrun_tests(\"CRM norm02 K=5\", crm_object_k5, \"VLA-only\", vla_object)\n\n# ============================================================================\n# 5. ARGMIN BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n5. ARGMIN BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Argmin K=10 (n=5)\", argmin_object_k10)\nprint_group_stats(\"Argmin K=5 (n=4)\", argmin_object_k5)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Argmin K=10 vs VLA-only:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"VLA-only\", vla_object)\nprint(\"\\n  Argmin K=10 vs CRM norm02 K=10:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 6. ADAPTIVE-K BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n6. ADAPTIVE-K BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Adaptive-K p25 (n=2)\", adaptive_k_p25)\nprint_group_stats(\"Adaptive-K p50 (n=3)\", adaptive_k_p50)\nprint_group_stats(\"Adaptive-K p75 (n=3)\", adaptive_k_p75)\nprint_group_stats(\"Adaptive-K p90 (n=3)\", adaptive_k_p90)\nall_adaptive = adaptive_k_p25 + adaptive_k_p50 + adaptive_k_p75 + adaptive_k_p90\nprint_group_stats(\"Adaptive-K all (n=11)\", all_adaptive)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Adaptive-K (all) vs VLA-only:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"VLA-only\", vla_object)\nprint(\"\\n  Adaptive-K (all) vs CRM norm02 K=10:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 7. SUMMARY TABLE\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"SUMMARY TABLE\")\nprint_separator()\nprint(f\"{'Benchmark':<18} {'Method':<22} {'n':>3} {'Mean':>7} {'Std':>7} {'Δ vs VLA':>9} {'p-value':>10} {'Sig':>5}\")\nprint_separator('-')\n\ndef get_vla_baseline(bench):\n    if bench == \"LIBERO-Spatial\": return vla_spatial\n    if bench == \"LIBERO-Long\": return vla_long\n    if bench == \"LIBERO-Goal\": return vla_goal\n    if bench == \"LIBERO-Object\": return vla_object\n    return None\n\ndef print_summary_row(bench, method, vals, is_vla=False):\n    arr = np.array(vals)\n    n = len(arr)\n    mean = arr.mean()\n    std = arr.std(ddof=1)\n    baseline = get_vla_baseline(bench)\n    if is_vla or baseline is None:\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {'—':>9} {'—':>10} {'—':>5}\")\n    else:\n        bl_arr = np.array(baseline)\n        diff = mean - bl_arr.mean()\n        _, t_pval = stats.ttest_ind(arr, bl_arr, equal_var=False)\n        sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {diff:>+9.4f} {t_pval:>10.6f} {sig:>5}\")\n\nprint_summary_row(\"LIBERO-Spatial\", \"CRM obs_only\", crm_spatial)\nprint_summary_row(\"LIBERO-Spatial\", \"VLA-only\", vla_spatial, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Long\", \"CRM obs_only\", crm_long)\nprint_summary_row(\"LIBERO-Long\", \"VLA-only\", vla_long, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Goal\", \"CRM obs_only\", crm_goal)\nprint_summary_row(\"LIBERO-Goal\", \"VLA-only\", vla_goal, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=10\", crm_object)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm01 (supp)\", crm_object_norm01)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=5 (supp)\", crm_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"VLA-only\", vla_object, is_vla=True)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=10\", argmin_object_k10)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=5\", argmin_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"Adaptive-K (all)\", all_adaptive)\n\n# ============================================================================\n# 8. KEY SIGNIFICANCE RESULTS\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"KEY SIGNIFICANCE RESULTS\")\nprint_separator()\n\ntests = [\n    (\"Spatial: CRM vs VLA\", crm_spatial, vla_spatial),\n    (\"Long: CRM vs VLA\", crm_long, vla_long),\n    (\"Goal: CRM vs VLA\", crm_goal, vla_goal),\n    (\"Object(norm02): CRM vs VLA\", crm_object, vla_object),\n    (\"Object(norm01-supp): CRM vs VLA\", crm_object_norm01, vla_object),\n    (\"Object: Argmin-K10 vs VLA\", argmin_object_k10, vla_object),\n    (\"Object: CRM-norm02 vs Argmin-K10\", crm_object, argmin_object_k10),\n    (\"Object: Adaptive-K vs VLA\", all_adaptive, vla_object),\n    (\"Object: CRM-norm02 vs Adaptive-K\", crm_object, all_adaptive),\n]\n\nprint(f\"\\n{'Comparison':<40} {'Diff':>7} {'t-test p':>10} {'MW-U p':>10} {'Sig':>5} {'Cohen d':>9}\")\nprint('-' * 85)\nfor name, a, b in tests:\n    arr_a, arr_b = np.array(a), np.array(b)\n    diff = arr_a.mean() - arr_b.mean()\n    t_stat, t_pval = stats.ttest_ind(arr_a, arr_b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(arr_a, arr_b, alternative='two-sided')\n    pooled_std = np.sqrt(((len(a)-1)*arr_a.std(ddof=1)**2 + (len(b)-1)*arr_b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    d = diff / pooled_std if pooled_std > 0 else float('inf')\n    sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n    print(f\"{name:<40} {diff:>+.4f} {t_pval:>10.6f} {u_pval:>10.6f} {sig:>5} {d:>+9.4f}\")\n\n# ============================================================================\n# 9. VERIFICATION NOTES\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"VERIFICATION NOTES\")\nprint_separator()\nprint(\"- Argmin K=10 seed43 = 0.17: severe outlier (other seeds 0.10-0.13).\")\nprint(\"  Original JSON not found on any server (bjb2-40593, bjb2-28827, bjb1-18228, bjb1-32546).\")\nprint(\"  Registry value retained but unverified.\")\nprint(\"- VLA-only Long seed48 = 0.14: confirmed by registry (eval-vla-only-long-seed48).\")\nprint(\"- CRM-Goal seed47 = 0.69: included per Director directive (not yet in registry).\")\nprint(\"- VLA-Spatial seed48=0.30, seed49=0.29: included per Director directive.\")\n\nprint(\"\\nSignificance levels: *** p<0.001, ** p<0.01, * p<0.05, n.s. not significant\")\nprint()\nprint_separator()\nprint(\"END OF ANALYSIS\")\nprint_separator()\n"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-20T05:02:29.783744+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-20T05:02:29.783934+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 artifacts/statistical_analysis.py 2>&1 | tee artifacts/statistical_analysis_output.txt",
  "description": "Run statistical analysis script and save output",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 artifacts/statistical_analysis.py 2>&1 | tee artifacts/statistical_analysis_output.txt",
    "description": "Run statistical analysis script and save output",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-20T05:02:29.784133+00:00_

================================================================================
STATISTICAL ANALYSIS: ACR-VLA Conformal Refinement Experiments
All success rates are fractions (0.0 to 1.0)
Object benchmark primary CRM config: norm02 (ε=0.2), K=10
================================================================================

1. LIBERO-SPATIAL
--------------------------------------------------------------------------------
  CRM obs_only (n=6): n=6, mean=0.3433, std=0.0137, min=0.3200, max=0.3600
    values: [0.35, 0.34, 0.36, 0.34, 0.32, 0.35]
  VLA-only (n=9): n=9, mean=0.2956, std=0.0113, min=0.2700, max=0.3100
    values: [0.3, 0.29, 0.31, 0.27, 0.3, 0.3, 0.3, 0.29, 0.3]

  CRM vs VLA-only:
    Difference: +0.0478 (+4.78 pp)
    Welch's t-test: t=7.0980, p=0.000046 ***
    Mann-Whitney U: U=54.0, p=0.001426 **
    Cohen's d: 3.8955 (large)


2. LIBERO-LONG
--------------------------------------------------------------------------------
  CRM obs_only (n=6): n=6, mean=0.1750, std=0.0164, min=0.1500, max=0.2000
    values: [0.17, 0.15, 0.2, 0.18, 0.18, 0.17]
  VLA-only (n=7): n=7, mean=0.1414, std=0.0254, min=0.1100, max=0.1800
    values: [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14]

  CRM vs VLA-only:
    Difference: +0.0336 (+3.36 pp)
    Welch's t-test: t=2.8628, p=0.016373 *
    Mann-Whitney U: U=36.0, p=0.035947 *
    Cohen's d: 1.5388 (large)


3. LIBERO-GOAL
--------------------------------------------------------------------------------
  CRM obs_only (n=6): n=6, mean=0.6817, std=0.0343, min=0.6400, max=0.7200
    values: [0.67, 0.72, 0.64, 0.65, 0.72, 0.69]
  VLA-only (n=5): n=5, mean=0.6940, std=0.0385, min=0.6300, max=0.7300
    values: [0.71, 0.69, 0.73, 0.63, 0.71]

  CRM vs VLA-only:
    Difference: -0.0123 (-1.23 pp)
    Welch's t-test: t=-0.5560, p=0.593106 n.s.
    Mann-Whitney U: U=12.5, p=0.713124 n.s.
    Cohen's d: -0.3406 (small)


4. LIBERO-OBJECT
--------------------------------------------------------------------------------

  [PRIMARY: C
…[truncated 7110 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 93 · 2026-05-20T05:02:29.784364+00:00_

Script ran successfully. Output saved to `artifacts/statistical_analysis_output.txt`.

---

## 修正后 Summary Table

| Benchmark | Method | n | Mean | Std | Δ vs VLA | p-value | Sig |
|---|---|---|---|---|---|---|---|
| LIBERO-Spatial | CRM obs_only | 6 | 0.3433 | 0.0137 | +0.0478 | 0.000046 | *** |
| LIBERO-Spatial | VLA-only | 9 | 0.2956 | 0.0113 | — | — | — |
| LIBERO-Long | CRM obs_only | 6 | 0.1750 | 0.0164 | +0.0336 | 0.016373 | * |
| LIBERO-Long | VLA-only | 7 | 0.1414 | 0.0254 | — | — | — |
| LIBERO-Goal | CRM obs_only | 6 | 0.6817 | 0.0343 | -0.0123 | 0.593106 | n.s. |
| LIBERO-Goal | VLA-only | 5 | 0.6940 | 0.0385 | — | — | — |
| LIBERO-Object | CRM norm02 K=10 | 6 | 0.1683 | 0.0183 | +0.0596 | 0.000095 | *** |
| LIBERO-Object | CRM norm01 (supp) | 6 | 0.1750 | 0.0105 | +0.0663 | <0.000001 | *** |
| LIBERO-Object | CRM norm02 K=5 (supp) | 7 | 0.1600 | 0.0216 | +0.0512 | 0.000312 | *** |
| LIBERO-Object | VLA-only | 8 | 0.1088 | 0.0136 | — | — | — |
| LIBERO-Object | Argmin K=10 | 5 | 0.1240 | 0.0288 | +0.0152 | 0.316589 | n.s. |
| LIBERO-Object | Argmin K=5 | 4 | 0.1300 | 0.0163 | +0.0212 | 0.073136 | n.s. |
| LIBERO-Object | Adaptive-K (all) | 11 | 0.1409 | 0.0151 | +0.0322 | 0.000170 | *** |

## 修正内容总结

1. **Object 主配置改为 norm02 (ε=0.2) K=10** — 所有 summary table 和 comparison 中 Object 的 CRM 用 `crm_object` (norm02 K=10)，norm01 降为 supplementary
2. **新增数据**: CRM-Goal seed47=0.69 (n:5→6), VLA-Spatial seed48=0.30/seed49=0.29/seed50=0.30 (n:7→9)
3. **VLA-Long seed48 = 0.14** 已确认
4. **Argmin K=10 seed43 = 0.17**: 在 4 台服务器均未找到原始 JSON，registry 值保留但标注为 unverified outlier

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_fix-statistical-analysis-critical_20260520T045526"
}
```

</details>

---
