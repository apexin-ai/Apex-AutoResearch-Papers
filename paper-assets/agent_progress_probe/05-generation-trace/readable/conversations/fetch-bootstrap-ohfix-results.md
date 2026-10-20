# fetch bootstrap ohfix results

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_fetch_bootstrap-ohfix-results_20260515T093958.jsonl`
- **Structured JSON:** [`95ee314d66b9163ee3bc.json`](../../sessions/95/95ee314d66b9163ee3bc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-15T09:40:54.684464+00:00_

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
  "session": "worker_fetch_bootstrap-ohfix-results_20260515T093958",
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

_source line 2 · 2026-05-15T09:40:54.684808+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fetch_bootstrap-ohfix-results_20260515T093958",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T09:40:54.684980+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-23165",
  "command": "cat /root/autodl-tmp/agent_progress_probe/artifacts/gold_set/bootstrap_ci_ohfix.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fetch_bootstrap-ohfix-results_20260515T093958",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-23165",
    "command": "cat /root/autodl-tmp/agent_progress_probe/artifacts/gold_set/bootstrap_ci_ohfix.json"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T09:40:54.685113+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-23165",
  "command": "grep -n \"oh_trajectories\\|openhands\\|trajectory_id\\|is_oh\" /root/autodl-tmp/agent_progress_probe/gold_bootstrap_ci.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fetch_bootstrap-ohfix-results_20260515T093958",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-23165",
    "command": "grep -n \"oh_trajectories\\|openhands\\|trajectory_id\\|is_oh\" /root/autodl-tmp/agent_progress_probe/gold_bootstrap_ci.py"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-15T09:40:54.685300+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"n_bootstrap\\\": 10000,\\n  \\\"seed\\\": 42,\\n  \\\"tests\\\": {\\n    \\\"gb_vs_mv\\\": {\\n      \\\"model_a\\\": \\\"Structural GB\\\",\\n      \\\"model_b\\\": \\\"MV Labels\\\",\\n      \\\"n_samples\\\": 195,\\n      \\\"n_bootstrap\\\": 10000,\\n      \\\"f1_a_on_shared\\\": 0.764361,\\n      \\\"f1_b_on_shared\\\": 0.718383,\\n      \\\"observed_delta\\\": 0.045978,\\n      \\\"ci_95_lo\\\": 0.006214,\\n      \\\"ci_95_hi\\\": 0.088402,\\n      \\\"p_value\\\": 0.0121,\\n      \\\"significant_005\\\": true\\n    },\\n    \\\"gb_vs_gru_probe\\\": {\\n      \\\"model_a\\\": \\\"Structural GB\\\",\\n      \\\"model_b\\\": \\\"GRU Probe\\\",\\n      \\\"n_samples\\\": 132,\\n      \\\"n_bootstrap\\\": 10000,\\n      \\\"f1_a_on_shared\\\": 0.784716,\\n      \\\"f1_b_on_shared\\\": 0.734833,\\n      \\\"observed_delta\\\": 0.049882,\\n      \\\"ci_95_lo\\\": -0.015686,\\n      \\\"ci_95_hi\\\": 0.120116,\\n      \\\"p_value\\\": 0.0698,\\n      \\\"significant_005\\\": false\\n    },\\n    \\\"rf_vs_gb\\\": {\\n      \\\"model_a\\\": \\\"Structural RF\\\",\\n      \\\"model_b\\\": \\\"Structural GB\\\",\\n      \\\"n_samples\\\": 195,\\n      \\\"n_bootstrap\\\": 10000,\\n      \\\"f1_a_on_shared\\\": 0.751621,\\n      \\\"f1_b_on_shared\\\": 0.764361,\\n      \\\"observed_delta\\\": -0.01274,\\n      \\\"ci_95_lo\\\": -0.037209,\\n      \\\"ci_95_hi\\\": 0.00933,\\n      \\\"p_value\\\": 0.136,\\n      \\\"significant_005\\\": false\\n    },\\n    \\\"twv_probe_vs_gb\\\": {\\n      \\\"model_a\\\": \\\"TWV Probe\\\",\\n      \\\"model_b\\\": \\\"Structural GB\\\",\\n      \\\"n_samples\\\": 132,\\n      \\\"n_bootstrap\\\": 10000,\\n      \\\"f1_a_on_shared\\\": 0.768421,\\n      \\\"f1_b_on_shared\\\": 0.784716,\\n      \\\"observed_delta\\\": -0.016295,\\n      \\\"ci_95_lo\\\": -0.066553,\\n      \\\"ci_95_hi\\\": 0.030622,\\n      \\\"p_value\\\": 0.2536,\\n      \\\"significant_005\\\": fal
…[truncated 600 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fetch_bootstrap-ohfix-results_20260515T093958",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T09:40:54.685460+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fetch_bootstrap-ohfix-results_20260515T093958",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T09:40:54.685628+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-23165",
  "command": "grep -nE \"oh_trajectories|openhands|trajectory_id|is_oh\" /root/autodl-tmp/agent_progress_probe/gold_bootstrap_ci.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fetch_bootstrap-ohfix-results_20260515T093958",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-23165",
    "command": "grep -nE \"oh_trajectories|openhands|trajectory_id|is_oh\" /root/autodl-tmp/agent_progress_probe/gold_bootstrap_ci.py"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T09:40:54.685805+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fetch_bootstrap-ohfix-results_20260515T093958",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T09:40:54.685931+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/gold_set/",
  "description": "Check local gold_set directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fetch_bootstrap-ohfix-results_20260515T093958",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/gold_set/",
    "description": "Check local gold_set directory exists"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T09:40:54.686050+00:00_

annotation_unknown_2026-05-15.csv
bootstrap_ci_canonical.json
bootstrap_ci_results.json
eval_canonical
eval_report.md
eval_report_full.md
eval_results.json
eval_results_full.json
gold_labels_unknown.csv
model_consistency_report.md
oh_fix_report.md
paper_draft_gold_section.md
quality_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fetch_bootstrap-ohfix-results_20260515T093958",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T09:40:54.686178+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-23165",
  "command": "grep -nE \"oh_trajectories|openhands|trajectory_id|is_oh\" /root/autodl-tmp/agent_progress_probe/gold_bootstrap_ci.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fetch_bootstrap-ohfix-results_20260515T093958",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-23165",
    "command": "grep -nE \"oh_trajectories|openhands|trajectory_id|is_oh\" /root/autodl-tmp/agent_progress_probe/gold_bootstrap_ci.py"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T09:40:54.686295+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fetch_bootstrap-ohfix-results_20260515T093958",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T09:40:54.686434+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-23165",
  "command": "grep -n \"oh_trajectories\" /root/autodl-tmp/agent_progress_probe/gold_bootstrap_ci.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fetch_bootstrap-ohfix-results_20260515T093958",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-23165",
    "command": "grep -n \"oh_trajectories\" /root/autodl-tmp/agent_progress_probe/gold_bootstrap_ci.py"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T09:40:54.686553+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"322:    parser.add_argument(\\\"--oh_trajectories\\\", type=str, default=None)\\n365:    if args.oh_trajectories:\\n366:        oh_traj_index = build_trajectory_index(str(base_dir / args.oh_trajectories))\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fetch_bootstrap-ohfix-results_20260515T093958",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T09:40:54.686684+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-23165",
  "command": "grep -n \"trajectory_id\" /root/autodl-tmp/agent_progress_probe/gold_bootstrap_ci.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fetch_bootstrap-ohfix-results_20260515T093958",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-23165",
    "command": "grep -n \"trajectory_id\" /root/autodl-tmp/agent_progress_probe/gold_bootstrap_ci.py"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T09:40:54.686824+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"181:    return f\\\"{w['trajectory_id']}__w{w['window_idx']}\\\"\\n374:        is_oh = \\\"__openhands__\\\" in w.get(\\\"trajectory_id\\\", \\\"\\\")\\n429:            twv_wid_to_emb_idx[f\\\"{w['trajectory_id']}__w{w['window_idx']}\\\"] = i\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fetch_bootstrap-ohfix-results_20260515T093958",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T09:40:54.686945+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-23165",
  "command": "grep -n \"openhands\" /root/autodl-tmp/agent_progress_probe/gold_bootstrap_ci.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fetch_bootstrap-ohfix-results_20260515T093958",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-23165",
    "command": "grep -n \"openhands\" /root/autodl-tmp/agent_progress_probe/gold_bootstrap_ci.py"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T09:40:54.687063+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"374:        is_oh = \\\"__openhands__\\\" in w.get(\\\"trajectory_id\\\", \\\"\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.33}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fetch_bootstrap-ohfix-results_20260515T093958",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T09:40:54.687260+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-23165",
  "command": "grep -n \"is_oh\" /root/autodl-tmp/agent_progress_probe/gold_bootstrap_ci.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fetch_bootstrap-ohfix-results_20260515T093958",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-23165",
    "command": "grep -n \"is_oh\" /root/autodl-tmp/agent_progress_probe/gold_bootstrap_ci.py"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T09:40:54.687405+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"374:        is_oh = \\\"__openhands__\\\" in w.get(\\\"trajectory_id\\\", \\\"\\\")\\n375:        if is_oh and oh_traj_index:\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fetch_bootstrap-ohfix-results_20260515T093958",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T09:40:54.687553+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/gold_set/bootstrap_ci_ohfix.json",
  "content": "{\n  \"n_bootstrap\": 10000,\n  \"seed\": 42,\n  \"tests\": {\n    \"gb_vs_mv\": {\n      \"model_a\": \"Structural GB\",\n      \"model_b\": \"MV Labels\",\n      \"n_samples\": 195,\n      \"n_bootstrap\": 10000,\n      \"f1_a_on_shared\": 0.764361,\n      \"f1_b_on_shared\": 0.718383,\n      \"observed_delta\": 0.045978,\n      \"ci_95_lo\": 0.006214,\n      \"ci_95_hi\": 0.088402,\n      \"p_value\": 0.0121,\n      \"significant_005\": true\n    },\n    \"gb_vs_gru_probe\": {\n      \"model_a\": \"Structural GB\",\n      \"model_b\": \"GRU Probe\",\n      \"n_samples\": 132,\n      \"n_bootstrap\": 10000,\n      \"f1_a_on_shared\": 0.784716,\n      \"f1_b_on_shared\": 0.734833,\n      \"observed_delta\": 0.049882,\n      \"ci_95_lo\": -0.015686,\n      \"ci_95_hi\": 0.120116,\n      \"p_value\": 0.0698,\n      \"significant_005\": false\n    },\n    \"rf_vs_gb\": {\n      \"model_a\": \"Structural RF\",\n      \"model_b\": \"Structural GB\",\n      \"n_samples\": 195,\n      \"n_bootstrap\": 10000,\n      \"f1_a_on_shared\": 0.751621,\n      \"f1_b_on_shared\": 0.764361,\n      \"observed_delta\": -0.01274,\n      \"ci_95_lo\": -0.037209,\n      \"ci_95_hi\": 0.00933,\n      \"p_value\": 0.136,\n      \"significant_005\": false\n    },\n    \"twv_probe_vs_gb\": {\n      \"model_a\": \"TWV Probe\",\n      \"model_b\": \"Structural GB\",\n      \"n_samples\": 132,\n      \"n_bootstrap\": 10000,\n      \"f1_a_on_shared\": 0.768421,\n      \"f1_b_on_shared\": 0.784716,\n      \"observed_delta\": -0.016295,\n      \"ci_95_lo\": -0.066553,\n      \"ci_95_hi\": 0.030622,\n      \"p_value\": 0.2536,\n      \"significant_005\": false\n    },\n    \"twv_probe_vs_gru_probe\": {\n      \"model_a\": \"TWV Probe\",\n      \"model_b\": \"GRU Probe\",\n      \"n_samples\": 132,\n      \"n_bootstrap\": 10000,\n      \"f1_a_on_shared\": 0.768421,\n      \"f1_b_on_shared\": 0.734833,\n      \"observed_delta\": 0.033588,\n      \"ci_95_lo\": -0.029252,\n      \"ci_95_hi\": 0.099071,\n      \"p_value\": 0.1499,\n      \"significant_005\": false\n    }\n  }\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fetch_bootstrap-ohfix-results_20260515T093958",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/gold_set/bootstrap_ci_ohfix.json",
    "content": "{\n  \"n_bootstrap\": 10000,\n  \"seed\": 42,\n  \"tests\": {\n    \"gb_vs_mv\": {\n      \"model_a\": \"Structural GB\",\n      \"model_b\": \"MV Labels\",\n      \"n_samples\": 195,\n      \"n_bootstrap\": 10000,\n      \"f1_a_on_shared\": 0.764361,\n      \"f1_b_on_shared\": 0.718383,\n      \"observed_delta\": 0.045978,\n      \"ci_95_lo\": 0.006214,\n      \"ci_95_hi\": 0.088402,\n      \"p_value\": 0.0121,\n      \"significant_005\": true\n    },\n    \"gb_vs_gru_probe\": {\n      \"model_a\": \"Structural GB\",\n      \"model_b\": \"GRU Probe\",\n      \"n_samples\": 132,\n      \"n_bootstrap\": 10000,\n      \"f1_a_on_shared\": 0.784716,\n      \"f1_b_on_shared\": 0.734833,\n      \"observed_delta\": 0.049882,\n      \"ci_95_lo\": -0.015686,\n      \"ci_95_hi\": 0.120116,\n      \"p_value\": 0.0698,\n      \"significant_005\": false\n    },\n    \"rf_vs_gb\": {\n      \"model_a\": \"Structural RF\",\n      \"model_b\": \"Structural GB\",\n      \"n_samples\": 195,\n      \"n_bootstrap\": 10000,\n      \"f1_a_on_shared\": 0.751621,\n      \"f1_b_on_shared\": 0.764361,\n      \"observed_delta\": -0.01274,\n      \"ci_95_lo\": -0.037209,\n      \"ci_95_hi\": 0.00933,\n      \"p_value\": 0.136,\n      \"significant_005\": false\n    },\n    \"twv_probe_vs_gb\": {\n      \"model_a\": \"TWV Probe\",\n      \"model_b\": \"Structural GB\",\n      \"n_samples\": 132,\n      \"n_bootstrap\": 10000,\n      \"f1_a_on_shared\": 0.768421,\n      \"f1_b_on_shared\": 0.784716,\n      \"observed_delta\": -0.016295,\n      \"ci_95_lo\": -0.066553,\n      \"ci_95_hi\": 0.030622,\n      \"p_value\": 0.2536,\n      \"significant_005\": false\n    },\n    \"twv_probe_vs_gru_probe\": {\n      \"model_a\": \"TWV Probe\",\n      \"model_b\": \"GRU Probe\",\n      \"n_samples\": 132,\n      \"n_bootstrap\": 10000,\n      \"f1_a_on_shared\": 0.768421,\n      \"f1_b_on_shared\": 0.734833,\n      \"observed_delta\": 0.033588,\n      \"ci_95_lo\": -0.029252,\n      \"ci_95_hi\": 0.099071,\n      \"p_value\": 0.1499,\n      \"significant_005\": false\n    }\n  }\n}\n"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T09:40:54.687723+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/gold_set/bootstrap_ci_ohfix.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fetch_bootstrap-ohfix-results_20260515T093958",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-15T09:40:54.687887+00:00_

完成。

**已拉取文件**：`artifacts/gold_set/bootstrap_ci_ohfix.json`

**OH 判断逻辑确认**（第374行）：
```python
is_oh = "__openhands__" in w.get("trajectory_id", "")
```
Worker 用的是 `trajectory_id` 字段中是否包含 `__openhands__` 来判断 OpenHands 轨迹，而非文件路径。

**关键结果摘要**：
| 对比 | n | ΔF1 | 95% CI | p | sig |
|------|---|-----|--------|---|-----|
| GB vs MV | 195 | +0.046 | [0.006, 0.088] | 0.012 | **yes** |
| GB vs GRU Probe | 132 | +0.050 | [−0.016, 0.120] | 0.070 | no |
| RF vs GB | 195 | −0.013 | [−0.037, 0.009] | 0.136 | no |
| TWV Probe vs GB | 132 | −0.016 | [−0.067, 0.031] | 0.254 | no |
| TWV Probe vs GRU | 132 | +0.034 | [−0.029, 0.099] | 0.150 | no |

唯一显著的仍是 GB vs MV（p=0.012）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_fetch_bootstrap-ohfix-results_20260515T093958"
}
```

</details>

---
